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

const OUT = process.argv[2] || 'public/dog-nutrition/food-safety-chart/foods-dogs-can-eat-chart.pdf';
const URL = process.argv[3] || 'http://127.0.0.1:8831/dog-nutrition/food-safety-chart/';

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

  await page.addStyleTag({ content: PRINT_CSS });

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
    // The URL has to sit in the footer, not only in the page-1 header. A printed
    // sheet gets photocopied, pinned on its own, or handed to one person - and
    // then the only thing that can lead a reader back to the source is whatever
    // is printed at the edge of that page.
    footerTemplate:
      '<div style="width:100%;font-size:7.5pt;color:#7a827d;padding:0 12mm;' +
      'font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between">' +
      '<span>wagwise.org/dog-nutrition/food-safety-chart</span>' +
      '<span>General information, not veterinary advice &nbsp;·&nbsp; ' +
      '<span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '14mm', bottom: '16mm', left: '12mm', right: '12mm' }
  });

  console.log(JSON.stringify({ ...stats, theadWrapped: wrapped }));
  await browser.close();
})();
