/*
  WagWise Pet — cookie consent notice.

  Why this exists
  ---------------
  1. GDPR / ePrivacy. Visitors in the EU, UK and Switzerland must be asked
     before anything non-essential is stored on their device. "Reject" has to
     be as easy to press as "Accept".
  2. Google Consent Mode v2. Google requires ad_storage, ad_user_data,
     ad_personalization and analytics_storage to default to "denied" until the
     visitor agrees. Defaults are set inline in the page <head>; this file only
     sends the update.

  Banner styling is injected from here on purpose: /assets/* is served with
  Cache-Control: immutable, so editing style.css would leave existing visitors
  on a stale copy for up to a year.
*/
(function () {
  'use strict';

  var KEY = 'wagwise_consent_v1';
  var TWELVE_MONTHS = 31536000000;

  function stored() {
    try {
      var raw = window.localStorage.getItem(KEY);
      if (!raw) return null;
      var rec = JSON.parse(raw);
      if (!rec || (rec.choice !== 'all' && rec.choice !== 'essential')) return null;
      if (rec.ts && (Date.now() - rec.ts) > TWELVE_MONTHS) return null;
      return rec.choice;
    } catch (e) {
      return null;
    }
  }

  function pushConsent(choice) {
    if (typeof window.gtag !== 'function') return;
    var granted = choice === 'all' ? 'granted' : 'denied';
    window.gtag('consent', 'update', {
      ad_storage: granted,
      ad_user_data: granted,
      ad_personalization: granted,
      analytics_storage: granted
    });
  }

  function persist(choice) {
    try {
      window.localStorage.setItem(KEY, JSON.stringify({ choice: choice, ts: Date.now() }));
    } catch (e) {
      /* private mode — choice applies to this page only */
    }
    pushConsent(choice);
  }

  var CSS = [
    '.cfc-bar{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;padding:14px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;font-size:13px;line-height:1.6;transform:translateY(115%);transition:transform .32s ease-out}',
    '.cfc-bar.cfc-in{transform:translateY(0)}',
    '@media(prefers-reduced-motion:reduce){.cfc-bar{transition:none}}',
    '.cfc-bar *{box-sizing:border-box}',
    '.cfc-in{max-width:1000px;margin:0 auto;background:#23262B;border-radius:16px;padding:18px 20px;display:flex;gap:20px;align-items:center;flex-wrap:wrap;box-shadow:0 10px 30px rgba(0,0,0,.18)}',
    '.cfc-text{flex:1 1 380px;min-width:0;color:#C9C7C2}',
    '.cfc-text b{display:block;color:#F1EFEA;font-weight:600;font-size:13.5px;margin-bottom:4px}',
    '.cfc-text a{color:#7FD3B6;text-decoration:none}',
    '.cfc-text a:hover{text-decoration:underline}',
    '.cfc-act{display:flex;gap:8px;flex-wrap:wrap;align-items:center}',
    '.cfc-btn{font-family:inherit;font-size:13px;border-radius:10px;padding:10px 18px;cursor:pointer;white-space:nowrap;transition:all .15s}',
    '.cfc-ok{background:#3FA97E;border:1px solid #3FA97E;color:#0F1114;font-weight:600}',
    '.cfc-ok:hover{background:#58C49A;border-color:#58C49A}',
    '.cfc-no{background:transparent;border:1px solid rgba(255,255,255,.22);color:#D7D5D0}',
    '.cfc-no:hover{border-color:rgba(255,255,255,.45);color:#F1EFEA}',
    'body.cfc-open{padding-bottom:170px}',
    '@media(max-width:620px){.cfc-in{padding:16px;gap:14px}.cfc-act{width:100%}.cfc-btn{flex:1 1 0;text-align:center;padding:11px 12px}}'
  ].join('');

  var HTML = '' +
    '<div class="cfc-in">' +
      '<div class="cfc-text">' +
        '<b>Cookies on WagWise Pet</b>' +
        'Essential cookies keep the site running. Advertising and analytics cookies are optional — they are only set if you agree, and declining does not change how the site works. ' +
        'See the <a href="/privacy/">privacy policy</a>.' +
      '</div>' +
      '<div class="cfc-act">' +
        '<button type="button" class="cfc-btn cfc-no" data-cfc="essential">Reject optional</button>' +
        '<button type="button" class="cfc-btn cfc-ok" data-cfc="all">Accept all</button>' +
      '</div>' +
    '</div>';

  var bar = null;

  function remove() {
    if (!bar) return;
    if (bar.parentNode) bar.parentNode.removeChild(bar);
    bar = null;
    document.body.classList.remove('cfc-open');
  }

  function show() {
    if (bar) return;
    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    bar = document.createElement('div');
    bar.className = 'cfc-bar';
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-label', 'Cookie consent');
    bar.innerHTML = HTML;
    document.body.appendChild(bar);

    bar.addEventListener('click', function (e) {
      var btn = e.target.closest ? e.target.closest('[data-cfc]') : null;
      if (!btn) return;
      persist(btn.getAttribute('data-cfc'));
      remove();
    });

    document.body.classList.add('cfc-open');
    window.requestAnimationFrame(function () {
      window.requestAnimationFrame(function () { bar.classList.add('cfc-in'); });
    });
  }

  function settingsLink() {
    var row = document.querySelector('.site-foot .fb');
    if (!row) return;
    var a = document.createElement('a');
    a.href = '#cookie-settings';
    a.textContent = 'Cookie settings';
    a.addEventListener('click', function (e) {
      e.preventDefault();
      show();
    });
    row.appendChild(a);
  }

  var choice = stored();
  if (choice) {
    pushConsent(choice);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', show);
  } else {
    show();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', settingsLink);
  } else {
    settingsLink();
  }
})();
