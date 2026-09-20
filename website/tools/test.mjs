/* Headless regression suite for the ATSWA II study site.
 *
 * Boots index.html in jsdom, intercepts the <script src="data/*.js"> injection
 * so the data files are evaluated straight from disk (jsdom will not fetch over
 * file://), then drives the hash router and asserts on the rendered HTML.
 *
 *   npm install jsdom                    # in website/, or anywhere
 *   node tools/test.mjs                  # resolves jsdom from website/
 *   JSDOM=<dir>/node_modules/jsdom node tools/test.mjs   # or from elsewhere
 */
import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');

const { JSDOM } = await (async () => {
  const where = process.env.JSDOM;
  try { return await import(where ? pathToFileURL(join(where, 'lib/api.js')).href : 'jsdom'); }
  catch (e) {
    console.error('jsdom not found. Run "npm install jsdom" in ' + ROOT +
                  ', or set JSDOM=<path>/node_modules/jsdom\n' + e.message);
    process.exit(2);
  }
})();

function boot() {
  const dom = new JSDOM(readFileSync(join(ROOT, 'index.html'), 'utf8'), {
    url: 'https://x.test/#/',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    // The patch must be installed before the page's scripts run: boot() fires on
    // DOMContentLoaded during construction and immediately asks for a data file.
    beforeParse(w) {
      // jsdom has no MathML, so the renderer would take its Unicode fallback path
      // and the MathML generator would never be exercised. Declare support.
      w.MathMLElement = function MathMLElement() {};
      const real = w.Node.prototype.appendChild;
      w.Node.prototype.appendChild = function (node) {
        const src = node && node.tagName === 'SCRIPT' && node.getAttribute
          ? node.getAttribute('src') : null;
        if (src && src.indexOf('data/') === 0) {
          const p = join(ROOT, src);
          if (existsSync(p)) {
            try { w.eval(readFileSync(p, 'utf8')); }
            catch (e) { console.error('data eval ' + src + ': ' + e.message); }
          } else if (node.onerror) { node.onerror(); }
          return node;
        }
        return real.call(this, node);
      };
    },
  });
  return dom.window;
}

/* The page boots on DOMContentLoaded, which jsdom fires asynchronously after the
   constructor returns. Give the event loop a turn before asserting on anything. */
function tick() { return new Promise(r => setTimeout(r, 0)); }

function view(w, route) {
  w.location.hash = route;
  w.dispatchEvent(new w.Event('hashchange'));
  return w.document.getElementById('view').innerHTML;
}

let pass = 0, fail = 0;
function t(name, fn) {
  try { fn(); pass++; console.log('  ok   ' + name); }
  catch (e) { fail++; console.log('  FAIL ' + name + '\n       ' + e.message); }
}
function ok(cond, msg) { if (!cond) throw new Error(msg || 'assertion failed'); }
function has(html, needle, label) {
  ok(html.indexOf(needle) >= 0, (label || 'missing') + ': ' + JSON.stringify(needle));
}
function count(html, needle) { return html.split(needle).length - 1; }

const w = boot();
await tick();
console.log('\nATSWA II - regression suite\n');

t('home page lists all four subjects', () => {
  const v = view(w, '#/');
  ['Financial Accounting', 'Public Sector Accounting', 'Quantitative Analysis',
   'Information Technology'].forEach(s => has(v, s));
  ok(v.indexOf('undefined') < 0, 'contains "undefined"');
});

t('home page links to all three study guides', () => {
  const v = view(w, '#/');
  has(v, 'Study guides');
  ['guides/crf.html', 'guides/ipsas.html', 'guides/statements.html'].forEach(href =>
    has(v, 'href="' + href + '"'));
});

t('FA subject page shows 16 chapters', () => {
  const v = view(w, '#/s/FA');
  has(v, 'Accounting for Non-Current Assets');
  ok(count(v, '#/s/FA/') >= 16, 'fewer than 16 chapter links');
});

t('QA subject page shows all 20 chapters', () => {
  const v = view(w, '#/s/QA');
  ['Test of Hypothesis', 'Set Theory', 'Mathematics of Finance',
   'Linear Programming', 'Network Analysis', 'Simulation'].forEach(s => has(v, s));
  ok(v.indexOf('undefined') < 0, 'contains "undefined"');
});

t('QA ch12 renders MathML and a formula box', () => {
  const v = view(w, '#/s/QA/12');
  has(v, '<math');
  has(v, 'Sinking fund');
  ok(count(v, '<math') > 30, 'expected many equations, got ' + count(v, '<math'));
});

t('QA ch15 renders simplex tableaux', () => {
  const v = view(w, '#/s/QA/15');
  has(v, 'Final tableau');
  has(v, 'Shadow price');
  has(v, '<table');
});

t('QA ch17 float table and critical path', () => {
  const v = view(w, '#/s/QA/17');
  has(v, 'Free float');
  has(v, 'critical path');
});

t('QA ch20 random-number ranges render', () => {
  const v = view(w, '#/s/QA/20');
  has(v, 'Monte Carlo');
  has(v, '00 – 04');
});

t('every QA chapter renders without "undefined"', () => {
  for (let n = 1; n <= 20; n++) {
    const v = view(w, '#/s/QA/' + n);
    ok(v.length > 2000, 'chapter ' + n + ' rendered only ' + v.length + ' chars');
    ok(v.indexOf('undefined') < 0, 'chapter ' + n + ' contains "undefined"');
  }
});

t('every FA chapter renders without "undefined"', () => {
  for (let n = 1; n <= 16; n++) {
    const v = view(w, '#/s/FA/' + n);
    ok(v.length > 2000, 'chapter ' + n + ' rendered only ' + v.length + ' chars');
    ok(v.indexOf('undefined') < 0, 'chapter ' + n + ' contains "undefined"');
  }
});

t('every QA chapter quiz builds', () => {
  for (let n = 1; n <= 20; n++) {
    const v = view(w, '#/s/QA/' + n + '/quiz');
    ok(v.indexOf('undefined') < 0, 'chapter ' + n + ' quiz contains "undefined"');
    ok(v.length > 500, 'chapter ' + n + ' quiz rendered almost nothing');
  }
});

t('PS subject page shows all 23 chapters', () => {
  const v = view(w, '#/s/PS');
  ok(count(v, 'class="chrow"') === 23, 'expected 23 chapter rows, got ' + count(v, 'class="chrow"'));
});

t('IT subject page shows all 6 chapters', () => {
  const v = view(w, '#/s/IT');
  ok(count(v, 'class="chrow"') === 6, 'expected 6 chapter rows, got ' + count(v, 'class="chrow"'));
});

t('PS chapter 1 renders (a legitimate "undefined" in its own prose is not a bug)', () => {
  const v = view(w, '#/s/PS/1');
  ok(v.length > 2000, 'PS ch1 rendered almost nothing');
  ok(/left completely undefined until then/.test(v), 'expected prose sentence missing — page may not have rendered ch1 at all');
});

t('exams index lists all 20 papers', () => {
  const v = view(w, '#/exams');
  ['2024-03', '2024-09', '2025-03', '2025-09', '2026-03'].forEach(s => has(v, s));
  ok(count(v, '#/exams/') >= 20, 'fewer than 20 paper links');
});

t('a QA past paper renders with answers', () => {
  const v = view(w, '#/exams/2026-03/QA');
  ok(v.length > 20000, 'paper looks truncated: ' + v.length + ' chars');
  ok(v.indexOf('undefined') < 0, 'contains "undefined"');
});

t('formula index includes the new QA formulas', () => {
  const v = view(w, '#/formulas');
  ['Sinking fund', 'Economic order quantity', 'PERT expected time',
   'Total float'].forEach(s => has(v, s));
});

t('progress page renders', () => {
  const v = view(w, '#/progress');
  ok(v.length > 500, 'progress page nearly empty');
  ok(v.indexOf('undefined') < 0, 'contains "undefined"');
});

t('revision subject picker lists all four subjects', () => {
  const v = view(w, '#/revision');
  ['Financial Accounting', 'Public Sector Accounting', 'Quantitative Analysis',
   'Information Technology'].forEach(s => has(v, s));
  ok(v.indexOf('undefined') < 0, 'contains "undefined"');
});

t('revision type picker shows MCQ/short-answer/essay for PS', () => {
  const v = view(w, '#/revision/PS');
  ['Multiple choice', 'Short answer', 'Essay'].forEach(s => has(v, s));
  ok(/#\/revision\/PS\/mcq/.test(v), 'missing link to the MCQ list');
  ok(v.indexOf('undefined') < 0, 'contains "undefined"');
});

t('revision MCQ list for PS renders questions, most-asked first', () => {
  const v = view(w, '#/revision/PS/mcq');
  ok(v.indexOf('undefined') < 0, 'contains "undefined"');
  ok(v.length > 5000, 'list looks truncated: ' + v.length + ' chars');
  ok(count(v, 'class="bq"') > 100, 'fewer than 100 MCQ rendered');
  const freqs = [...v.matchAll(/ASKED (\d+)\s*[×x]/g)].map(m => +m[1]);
  ok(freqs.length > 10, 'no frequency badges found');
  for (let i = 1; i < freqs.length; i++)
    ok(freqs[i] <= freqs[i - 1], 'not sorted most-asked-first at index ' + i);
});

t('revision short-answer and essay lists render for every subject', () => {
  ['FA', 'PS', 'QA', 'IT'].forEach(code => {
    ['saq', 'essay'].forEach(kind => {
      const v = view(w, '#/revision/' + code + '/' + kind);
      ok(v.indexOf('undefined') < 0, code + '/' + kind + ' contains "undefined"');
      ok(v.length > 2000, code + '/' + kind + ' looks truncated: ' + v.length + ' chars');
    });
  });
});

console.log('\n' + pass + ' passed, ' + fail + ' failed\n');
process.exit(fail ? 1 : 0);
