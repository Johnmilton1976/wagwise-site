const puppeteer = require('puppeteer-core');

/* Turn the food-safety chart into a PDF a clinic can print and pin to a wall.

   Why a real file instead of the browser's "Print or save as PDF" button: the
   button only helps someone already on the page. Outreach to vet clinics and
   breeders works better when you can say "here is the file, print it" - and a
   PDF in a mail attachment or a shared drive travels where a URL does not.

   The print stylesheet is injected rather than written into style.css so the
   web page stays untouched: same single source of truth for the data, a
   different presentation layer for paper.
*/

/* Two products come out of this script.

   Default: the six-page handout, the whole 47-food list. That is the document
   you email to someone who asked for everything.

   --poster: one A4 page, the seven foods that have no safe dose. A kennel does
   not pin six pages to a wall - it pins one. The six-page file is also a bad
   first attachment: it asks the reader to print and collate before it is any
   use. The poster answers "what goes on the kitchen wall" in one sheet. */

const args = process.argv.slice(2);
const OUT = args[0] || 'public/dog-nutrition/food-safety-chart/foods-dogs-can-eat-chart.pdf';
const URL = args.find(a => a.startsWith('http')) || 'http://127.0.0.1:8831/dog-nutrition/food-safety-chart/';
const POSTER = args.includes('--poster');

const PRINT_CSS = `
  @page { size: A4; margin: 14mm 12mm 16mm 12mm; }

  /* chrome that means nothing on paper */
  .site-head, .site-foot, .crumbs, .eyebrow, .chart-tools, .embed-block,
  #embed, .embed-credit, .cfc-bar, #fc-csv, #fc-print { display: none !important; }

  body { background: #fff !important; color: #1E2125 !important; }

  /* the paper header, injected as a pseudo element so the DOM stays as-is */
  main .wrap.narrow::before {
    content: "WagWise Pet  ·  Foods dogs can eat  ·  47 foods, four risk tiers  ·  reviewed 2 November 2026  ·  wagwise.org";
    display: block;
    font-size: 8.5pt;
    letter-spacing: .01em;
    color: #5F6B65;
    border-bottom: 1px solid #d8d5cd;
    padding-bottom: 5px;
    margin-bottom: 14px;
  }

  h1 { font-size: 19pt !important; line-height: 1.2 !important; margin: 0 0 8px !important; }
  h2 { font-size: 12pt !important; margin: 16px 0 6px !important;
       page-break-after: avoid; break-after: avoid; }
  h3 { font-size: 10.5pt !important; page-break-after: avoid; break-after: avoid; }
  p, li, td, th { font-size: 9.2pt !important; line-height: 1.45 !important; }
  .lede { font-size: 10pt !important; color: #333b36 !important; }

  /* With a real thead in place a table may cross a page safely - the column
     labels come with it. Letting it flow fills the page instead of leaving a
     third of it blank, which is what break-inside:avoid was doing. */
  table { page-break-inside: auto; break-inside: auto; width: 100% !important; }
  thead { display: table-header-group; }
  tr { page-break-inside: avoid; break-inside: avoid; }
  td, th { padding: 4px 6px !important; }

  .callout { page-break-inside: avoid; break-inside: avoid;
             border: 1px solid #d8d5cd !important; background: #faf9f5 !important; }
  a { color: #1E2125 !important; text-decoration: none !important; }

  /* the FAQ reads fine on paper but should not leave orphan headings */
  .faq-item { page-break-inside: avoid; break-inside: avoid; }
`;

const POSTER_CSS = `
  @page { size: A4; margin: 13mm 13mm 12mm 13mm; }
  body { background: #fff !important; color: #1E2125 !important; }
  .site-head, .site-foot, .crumbs, .eyebrow, .chart-tools, .embed-block,
  #embed, .embed-credit, .cfc-bar { display: none !important; }

  #poster { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
  #poster .brand { font-size: 9pt; letter-spacing: .15em; text-transform: uppercase;
                   color: #6a726d; margin: 0 0 16px; font-weight: 600; }
  #poster h1 { font-size: 35pt !important; line-height: 1.02 !important;
               margin: 0 0 10px !important; letter-spacing: -.015em !important; }
  #poster .lead { font-size: 13pt !important; line-height: 1.45 !important;
                  color: #333b36 !important; margin: 0 0 18px !important; max-width: 172mm; }
  #poster table { width: 100% !important; border-collapse: collapse !important; margin: 0 0 16px !important; }
  #poster thead th { background: #1E2125 !important; color: #fff !important;
                     font-size: 10pt !important; letter-spacing: .05em; text-transform: uppercase;
                     text-align: left !important; padding: 9px 10px !important; }
  #poster tbody td { font-size: 12.5pt !important; line-height: 1.42 !important;
                     padding: 12px 10px !important; border-bottom: 1px solid #d8d5cd !important;
                     vertical-align: top !important; }
  #poster tbody td:first-child { font-weight: 700; width: 26% !important; }
  #poster tr { break-inside: avoid; }
  #poster .rule { font-size: 13pt !important; line-height: 1.45 !important; font-weight: 600;
                  border-left: 5px solid #8a2b1e; background: #faf6f4;
                  padding: 12px 15px !important; margin: 0 0 16px !important; }
  #poster .meta { font-size: 9pt !important; line-height: 1.5 !important;
                  color: #6a726d !important; border-top: 1px solid #d8d5cd;
                  padding-top: 10px; margin: 0 !important; }
`;

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: 'new',
    args: ['--no-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 1200, deviceScaleFactor: 2 });
  await page.goto(URL, { waitUntil: 'networkidle2', timeout: 60000 });

  // drop the cookie bar if it rendered
  await page.evaluate(() => {
    document.querySelectorAll('.cfc-bar').forEach(e => e.remove());
    document.body.classList.remove('cfc-open');
  });

  /* Wrap each table's header row in a real <thead>.

     The source markup marks column headers with <th> but never groups them, so
     a table that crosses a page boundary resumes with no column labels - the
     reader gets "About 81 kcal and 5 g protein per 100 g" with nothing saying
     which column it belongs to. `thead` is the only thing that makes a header
     repeat on paper.

     This runs in the browser at PDF time, not in the source, because style.css
     keys a mobile layout off `.chart-tbl tr:first-child` - adding a thead to
     the markup would make tr:first-child stop matching and break the stacked
     phone layout. The 620px breakpoint does not fire on an A4 page, so
     restructuring here leaves both the web page and the print output correct.
  */
  const wrapped = await page.evaluate(() => {
    let n = 0;
    document.querySelectorAll('table').forEach(t => {
      if (t.tHead) return;
      const first = t.rows[0];
      if (!first || !first.querySelector('th')) return;
      /* the parser inserts an implicit <tbody>, so rows[0].parentNode is the
         tbody and not the table - insert the thead above whichever container
         actually holds that row. */
      const holder = first.parentNode;
      const thead = document.createElement('thead');
      thead.appendChild(first.cloneNode(true));
      if (holder === t) t.insertBefore(thead, first);
      else t.insertBefore(thead, holder);
      first.remove();
      n++;
    });
    return n;
  });

  if (POSTER) {
    /* Rebuild the page as a single sheet rather than re-typesetting the
       article. The table is cloned from the live DOM, so the numbers on the
       poster are the same numbers as on the page - a poster with its own copy
       of the data would drift within a month. */
    await page.evaluate(() => {
      const table = document.querySelector('table');
      if (!table) throw new Error('no table found on the chart page');
      const clone = table.cloneNode(true);

      /* An instruction that only works with a mouse. The chocolate row ends
         "run the dose for your own dog's weight", where "run the dose" is a
         link to the weight-based calculator - on paper that sentence tells the
         reader to do something the sheet cannot do. Drop the clause rather
         than reword the table, so the numbers stay byte-identical to the page. */
      clone.querySelectorAll('tbody tr').forEach(tr => {
        const cell = tr.cells[tr.cells.length - 1];
        // the anchor is only the words "run the dose"; "for your own dog's
        // weight" trails outside it, so cut from the dash to the end of the cell
        if (cell) cell.innerHTML = cell.innerHTML.replace(/\s*[—-]\s*(?:<a[^>]*>)?\s*run the dose[\s\S]*$/i, '');
      });

      const holder = document.createElement('div');
      holder.id = 'poster';
      holder.innerHTML =
        '<p class="brand">WagWise Pet &nbsp;·&nbsp; print and pin up: kennel kitchen, daycare desk, clinic exam room</p>' +
        '<h1>Seven foods with no safe dose</h1>' +
        '<p class="lead">Most food charts split the world into safe and toxic. These seven are a third thing: ' +
        'there is no amount that can be called safe, so the answer is never a portion — it is a phone call. ' +
        'The right-hand column is what the vet will ask for.</p>';
      holder.appendChild(clone);

      const tail = document.createElement('div');
      tail.innerHTML =
        '<p class="rule">Remove the food. Keep the packaging. Call your vet or the nearest emergency clinic, ' +
        'and have the dog\'s weight and roughly how much was eaten ready. Do not make the dog vomit unless a vet tells you to.</p>' +
        '<p class="meta">The full chart — 47 foods in four risk tiers, one dose per row — is at ' +
        '<b>wagwise.org/dog-nutrition/food-safety-chart</b>. Figures checked against the references listed on that page, ' +
        '2 November 2026, and re-checked when a source changes. General information, not veterinary advice.</p>';
      holder.appendChild(tail);

      document.body.innerHTML = '';
      document.body.appendChild(holder);
    });
  }

  await page.addStyleTag({ content: POSTER ? POSTER_CSS : PRINT_CSS });

  const stats = await page.evaluate(() => ({
    tables: document.querySelectorAll('table').length,
    rows: document.querySelectorAll('tbody tr').length,
    h2: document.querySelectorAll('h2').length
  }));

  await page.pdf({
    path: OUT,
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    /* The URL goes in the footer, not only in the page-1 header: a printed
       sheet gets photocopied, pinned on its own, or handed to one person, and
       then whatever is printed at the edge is the only route back to source. */
    footerTemplate: POSTER
      // a one-page poster has no page count to show, and the meta line already
      // carries the URL - so the footer stays a single quiet rule
      ? '<div style="width:100%;font-size:7.5pt;color:#8a8f8b;padding:0 13mm;' +
        'font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between">' +
        '<span>wagwise.org/dog-nutrition/food-safety-chart</span>' +
        '<span>General information, not veterinary advice</span></div>'
      : '<div style="width:100%;font-size:7.5pt;color:#7a827d;padding:0 12mm;' +
        'font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between">' +
        '<span>wagwise.org/dog-nutrition/food-safety-chart</span>' +
        '<span>General information, not veterinary advice &nbsp;·&nbsp; ' +
        '<span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: POSTER
      ? { top: '13mm', bottom: '12mm', left: '13mm', right: '13mm' }
      : { top: '14mm', bottom: '16mm', left: '12mm', right: '12mm' }
  });

  console.log(JSON.stringify({ ...stats, theadWrapped: wrapped }));
  await browser.close();
})();
