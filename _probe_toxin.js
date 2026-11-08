/* Probe the toxic-food dose calculator with real input events.
 *
 * The point of driving the page rather than reading the source: every previous
 * bug in these calculators was a unit that was silently off by a factor —
 * lb converted twice, a select whose value did not match the option list, a
 * status that only updated on one of the two events it listened for. So this
 * sets the fields the way a browser would and reads the rendered text back.
 *
 * It runs against a local static server, not a file:// URL: without the real
 * stylesheet the mobile width measurements are wrong in both directions, and a
 * file:// page cannot report the overflow it would have in production.
 *
 * Usage:  python -m http.server 8795 --bind 127.0.0.1   (from public/)
 *         MSYS_NO_PATHCONV=1 node _probe_toxin.js
 */
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const PAGE = 'http://127.0.0.1:8795/tools/toxic-food-dose-calculator/index.html';

function findChrome() {
  const cands = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  ];
  for (const c of cands) if (fs.existsSync(c)) return c;
  throw new Error('no chrome/edge found');
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: findChrome(), headless: 'new',
    args: ['--no-sandbox'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1100, height: 900 });
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });

  await page.goto(PAGE, { waitUntil: 'load' });

  // Set a field the way a user does: one input event, one change event.
  async function set(sel, value, evt) {
    await page.$eval(sel, (el, v, e) => {
      el.value = v;
      el.dispatchEvent(new Event(e, { bubbles: true }));
    }, String(value), evt || 'change');
  }
  async function out() {
    return page.$eval('#tx-out', el => el.textContent.replace(/\s+/g, ' ').trim());
  }
  async function unitOptions() {
    return page.$eval('#tx-unit', el => Array.from(el.options).map(o => o.value));
  }
  const cases = [
    // label, food, weight, wunit, amount, unit, abv, expect substring
    ['xylitol 10kg 2g -> 200 mg/kg', 'xylitol', 10, 'kg', 2, 'g', null, '200 mg/kg', 'hypoglycaemia'],
    ['xylitol 10kg 500mg -> 50 mg/kg', 'xylitol', 10, 'kg', 500, 'mg', null, '50 mg/kg', 'decontamination band'],
    ['xylitol 10kg 5g -> 500 mg/kg', 'xylitol', 10, 'kg', 5, 'g', null, '500 mg/kg', 'liver-failure'],
    ['onion 10kg 150g -> 15 g/kg', 'onion', 10, 'kg', 150, 'g', null, '15 g/kg', 'reported threshold band'],
    ['onion 10kg 1 onion -> 15 g/kg', 'onion', 10, 'kg', 1, 'onion', null, '15 g/kg', 'reported threshold band'],
    ['garlic 10kg 7 cloves -> 3.5 g/kg', 'garlic', 10, 'kg', 7, 'clove', null, '3.5 g/kg', 'below the derived'],
    ['macadamia 10kg 3 nuts -> 0.75 g/kg', 'macadamia', 10, 'kg', 3, 'nut', null, '0.75 g/kg', 'lowest reported'],
    ['caffeine 10kg 1 tablet -> 20 mg/kg', 'caffeine', 10, 'kg', 1, 'tablet', null, '20 mg/kg', 'mild-signs'],
    ['caffeine 10kg 1 coffee -> 9.5 mg/kg', 'caffeine', 10, 'kg', 1, 'coffee', null, '10 mg/kg', 'below the symptomatic'],
    ['alcohol 10kg 100ml wine -> 0.95 g/kg', 'alcohol', 10, 'kg', 100, 'ml', 12, '0.95 g/kg', 'below the level'],
    ['alcohol 10kg 300ml wine -> 2.8 g/kg', 'alcohol', 10, 'kg', 300, 'ml', 12, '2.8 g/kg', 'severe depression'],
    ['alcohol 1kg 25ml spirits -> lethal', 'alcohol', 1, 'kg', 25, 'ml', 40, '7.9 g/kg', 'lethal'],
    ['grapes 10kg 100g -> any amount', 'grapes', 10, 'kg', 100, 'g', null, 'no safe dose', 'exposure at any dose'],
    ['grapes 10kg 12 grapes', 'grapes', 10, 'kg', 12, 'grape', null, '6 g/kg', 'no safe dose'],
    ['lb: 22lb dog 100g onion', 'onion', 22, 'lb', 100, 'g', null, '10 g/kg', 'below the single-dose'],
  ];

  let pass = 0, fail = 0;
  for (const [label, food, w, wu, a, au, abv, want1, want2] of cases) {
    await set('#tx-food', food, 'change');
    await set('#tx-wunit', wu, 'change');
    await set('#tx-weight', w, 'input');
    if (abv !== null) await set('#tx-abv', String(abv), 'change');
    // unit list is rebuilt on food change, so set it after
    const opts = await unitOptions();
    if (!opts.includes(au)) { console.log('FAIL  ' + label + '  unit ' + au + ' missing, have ' + opts.join(',')); fail++; continue; }
    await set('#tx-unit', au, 'change');
    await set('#tx-amount', a, 'input');
    const t = await out();
    const ok = t.toLowerCase().includes(want1.toLowerCase()) && t.toLowerCase().includes(want2.toLowerCase());
    if (ok) { pass++; console.log('ok    ' + label + '  -> ' + t.slice(0, 90)); }
    else { fail++; console.log('FAIL  ' + label + '\n      want "' + want1 + '" + "' + want2 + '"\n      got  ' + t); }
  }

  // reference table: 7 rows + header
  const rows = await page.$eval('#tx-ref', el => el.querySelectorAll('tr').length);
  console.log((rows === 8 ? 'ok    ' : 'FAIL  ') + 'reference table rows = ' + rows + ' (want 8 incl header)');

  // query-string restore: the state must arrive pre-filled, not on the defaults
  await page.goto(PAGE + '?food=onion&w=10&wu=kg&a=1&au=onion', { waitUntil: 'load' });
  const restored = await out();
  console.log((restored.includes('15 g/kg') ? 'ok    ' : 'FAIL  ') + 'restore from URL -> ' + restored.slice(0, 80));

  // ?food=grapes must switch both the select and the unit list
  await page.goto(PAGE + '?food=grapes&w=10&a=12&au=grape', { waitUntil: 'load' });
  const g = await out();
  const gopts = await unitOptions();
  console.log((g.includes('no safe dose') && gopts.includes('grape') ? 'ok    ' : 'FAIL  ') +
    'restore grapes -> ' + g.slice(0, 70) + ' units=' + gopts.join(','));

  // no horizontal overflow at three widths
  for (const w of [320, 360, 414]) {
    await page.setViewport({ width: w, height: 900 });
    await page.goto(PAGE, { waitUntil: 'load' });
    const m = await page.evaluate(() => ({
      sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth,
    }));
    console.log((m.sw <= m.cw + 1 ? 'ok    ' : 'FAIL  ') + w + 'px scrollWidth=' + m.sw + ' clientWidth=' + m.cw);
  }

  // embed mode: html.embed present, .doc hidden, credit visible
  await page.setViewport({ width: 390, height: 900 });
  await page.goto(PAGE + '?embed=1', { waitUntil: 'load' });
  await new Promise(r => setTimeout(r, 400));
  const emb = await page.evaluate(() => {
    const vis = el => el && el.getBoundingClientRect().height > 0;
    return {
      cls: document.documentElement.className,
      docVisible: vis(document.querySelector('.doc')),
      creditVisible: vis(document.querySelector('.embed-credit')),
      creditLink: (document.querySelector('.embed-credit a') || {}).href || null,
      height: Math.ceil((document.querySelector('.wrap.narrow') || document.body).getBoundingClientRect().bottom + 8),
      sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth,
    };
  });
  console.log('embed: class="' + emb.cls + '" docVisible=' + emb.docVisible +
    ' creditVisible=' + emb.creditVisible + ' link=' + emb.creditLink +
    ' measuredHeight=' + emb.height + ' overflow=' + (emb.sw > emb.cw + 1));

  if (errors.length) { console.log('\nJS ERRORS:'); errors.forEach(e => console.log('  ' + e)); }
  else console.log('\nno js errors');
  console.log('\n' + pass + ' passed, ' + fail + ' failed');
  await browser.close();
  process.exit(fail ? 1 : 0);
})();
