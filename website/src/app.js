/* -- ATSWA Part II study app ------------------------------------------
   Hash routing, lazy per-subject data, a quiz engine shared by chapter
   quizzes and exam mode, full-text search, and progress in localStorage. */
var ATSWA = (function () {

  /* ---- storage, with an in-memory fallback when it is blocked ------- */
  var mem = {};
  var LS = (function () {
    try { var k = '__t'; localStorage.setItem(k, '1'); localStorage.removeItem(k); return localStorage; }
    catch (e) { return null; }
  })();
  function get(k, d) {
    try { var v = LS ? LS.getItem(k) : mem[k]; return v == null ? d : JSON.parse(v); }
    catch (e) { return d; }
  }
  function set(k, v) {
    try { var s = JSON.stringify(v); if (LS) LS.setItem(k, s); else mem[k] = s; } catch (e) {}
  }
  var PK = 'atswa2:';

  /* ---- data registry ----------------------------------------------- */
  var DATA = {}, PEND = {};
  function put(key, obj) {
    DATA[key] = obj;
    if (PEND[key]) { PEND[key].forEach(function (f) { f(obj); }); delete PEND[key]; }
  }
  function need(key, file, cb) {
    if (DATA[key]) return cb(DATA[key]);
    if (PEND[key]) { PEND[key].push(cb); return; }
    PEND[key] = [cb];
    var s = document.createElement('script');
    s.src = 'data/' + file + '.js';
    s.onerror = function () {
      var w = PEND[key] || []; delete PEND[key];
      w.forEach(function (f) { f(null); });
    };
    document.head.appendChild(s);
  }

  /* ---- helpers ------------------------------------------------------ */
  var esc = function (s) { return R.esc(s); };
  function el(id) { return document.getElementById(id); }
  function h(html) { el('view').innerHTML = html; }
  function subOf(code) {
    for (var i = 0; i < SUBJECTS.length; i++) if (SUBJECTS[i].code === code) return SUBJECTS[i];
    return null;
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fmtClock(ms) {
    if (ms < 0) ms = 0;
    var s = Math.floor(ms / 1000);
    return pad(Math.floor(s / 3600)) + ':' + pad(Math.floor(s / 60) % 60) + ':' + pad(s % 60);
  }
  function pct(a, b) { return b ? Math.round(a / b * 100) : 0; }
  function optText(o) {
    if (typeof o === 'string') return R.inl(o);
    if (o && o.pre) return '<div class="pre">' + esc(o.pre.join('\n')) + '</div>';
    return R.inl(o && o.t);
  }
  function optPlain(o) {
    if (typeof o === 'string') return o;
    if (o && o.pre) return o.pre.join(' ');
    return (o && o.t) || '';
  }
  function stemHTML(q) {
    var s = q.stem !== undefined ? q.stem : q.q;
    var out = typeof s === 'string' ? R.inl(s) : R.inl(s && s.t);
    if (s && s.pre) out += '<div class="pre">' + esc(s.pre.join('\n')) + '</div>';
    return out;
  }
  function preBlock(pre, label) {
    if (!pre || !pre.length) return '';
    return '<div class="qpre"><div class="lbl">' + (label || 'Shared data') + '</div>' +
           '<div class="pre">' + esc(pre.join('\n')) + '</div></div>';
  }

  /* ---- progress ----------------------------------------------------- */
  function prog() { return get(PK + 'prog', {}); }
  function markRead(code, n) {
    var p = prog(), k = code + '/' + n;
    p[k] = p[k] || {};
    if (!p[k].read) { p[k].read = Date.now(); set(PK + 'prog', p); }
  }
  function saveScore(code, n, right, total) {
    var p = prog(), k = code + '/' + n;
    p[k] = p[k] || {};
    var best = p[k].best || 0;
    p[k].quiz = { r: right, t: total, at: Date.now() };
    p[k].best = Math.max(best, total ? right / total : 0);
    set(PK + 'prog', p);
  }
  function subStats(code) {
    var p = prog(), s = subOf(code), read = 0, done = 0, sum = 0;
    for (var i = 1; i <= s.n; i++) {
      var r = p[code + '/' + i];
      if (r && r.read) read++;
      if (r && r.quiz) { done++; sum += r.best || 0; }
    }
    return { read: read, done: done, avg: done ? Math.round(sum / done * 100) : 0, n: s.n };
  }

  /* ---- routing ------------------------------------------------------ */
  var route = { parts: [], q: {} };
  function go(hash) { location.hash = hash; }
  function parseHash() {
    var raw = location.hash.replace(/^#\/?/, '');
    var qi = raw.indexOf('?'), q = {};
    if (qi >= 0) {
      raw.slice(qi + 1).split('&').forEach(function (kv) {
        var p = kv.split('='); q[decodeURIComponent(p[0])] = decodeURIComponent(p[1] || '');
      });
      raw = raw.slice(0, qi);
    }
    return { parts: raw.split('/').filter(Boolean).map(decodeURIComponent), q: q };
  }

  var VIEWS = {};

  function render() {
    route = parseHash();
    var p = route.parts;
    closeSheet(); closeSearch(); closeMobileNav();
    document.body.removeAttribute('data-sub');
    if (!p.length) return VIEWS.home();
    if (p[0] === 's' && p[1]) {
      document.body.setAttribute('data-sub', p[1]);
      if (!p[2]) return VIEWS.subject(p[1]);
      if (p[3] === 'quiz') return VIEWS.quiz(p[1], +p[2]);
      return VIEWS.chapter(p[1], +p[2]);
    }
    if (p[0] === 'exams') {
      if (!p[1]) return VIEWS.exams();
      if (p[3] === 'sit') { document.body.setAttribute('data-sub', p[2]); return VIEWS.sit(p[1], p[2]); }
      document.body.setAttribute('data-sub', p[2]);
      return VIEWS.paper(p[1], p[2]);
    }
    if (p[0] === 'revision') {
      if (!p[1]) return VIEWS.revision();
      document.body.setAttribute('data-sub', p[1]);
      if (!p[2]) return VIEWS.revisionSub(p[1]);
      return VIEWS.revisionList(p[1], p[2]);
    }
    if (p[0] === 'formulas') return VIEWS.formulas();
    if (p[0] === 'progress') return VIEWS.progress();
    if (p[0] === 'about') return VIEWS.about();
    return VIEWS.home();
  }

  function tabs() {
    var p = route.parts;
    var cur = p[0] === 's' ? p[1] : p[0];
    var out = SUBJECTS.map(function (s) {
      return '<a href="#/s/' + s.code + '"' + (cur === s.code ? ' aria-current="page"' : '') +
             '>' + esc(s.name) + '</a>';
    });
    out.push('<a href="#/exams"' + (p[0] === 'exams' ? ' aria-current="page"' : '') + '>Past papers</a>');
    out.push('<a href="#/revision"' + (p[0] === 'revision' ? ' aria-current="page"' : '') + '>Final Revision</a>');
    out.push('<a href="#/formulas"' + (p[0] === 'formulas' ? ' aria-current="page"' : '') + '>Formulas</a>');
    out.push('<a href="#/progress"' + (p[0] === 'progress' ? ' aria-current="page"' : '') + '>Progress</a>');
    el('tabs').innerHTML = out.join('');
    var mn = el('mobilenav');
    if (mn) mn.innerHTML = out.join('');
  }

  function loading(msg) {
    h('<div class="wrap"><div style="padding:70px 0;text-align:center;color:var(--ink3)">' +
      '<div class="eyebrow">' + esc(msg || 'Loading') + '</div></div></div>');
  }

  /* =================================================================== */
  /*  home                                                               */
  /* =================================================================== */
  VIEWS.home = function () {
    var totalCh = SUBJECTS.reduce(function (a, s) { return a + s.n; }, 0);
    var cards = SUBJECTS.map(function (s) {
      var st = subStats(s.code);
      return '<a class="subcard" href="#/s/' + s.code + '" data-sub="' + s.code + '">' +
        '<div class="r1"><span class="code">' + s.code + '</span>' +
        '<span class="cnt">' + s.n + ' chapters</span></div>' +
        '<h2>' + esc(s.name) + '</h2>' +
        '<div class="sub">' + esc(s.blurb) + '</div>' +
        '<div class="bar"><i style="width:' + pct(st.read, st.n) + '%"></i></div>' +
        '<div class="foot"><span><b>' + st.read + '</b>/' + st.n + ' read</span>' +
        '<span><b>' + st.done + '</b> quizzed</span>' +
        (st.done ? '<span><b>' + st.avg + '%</b> best avg</span>' : '') +
        '</div></a>';
    }).join('');
    h('<div class="wrap">' +
      '<section class="hero"><div class="eyebrow">Accounting Technicians Scheme, West Africa</div>' +
      '<h1>Part II, chapter by chapter.</h1>' +
      '<p class="lede">The four Part&nbsp;II subjects set out as study notes you can actually read — ' +
      'every chapter with its own worked examples, formula sheet and quiz — next to 24 diets of ' +
      'past papers with the official solutions expanded into full working.</p>' +
      '<div class="tally">' +
      '<div><b>' + totalCh + '</b>chapters</div>' +
      '<div><b>2,859</b>past MCQs</div>' +
      '<div><b>1,920</b>short answers</div>' +
      '<div><b>562</b>essay questions</div>' +
      '<div><b>24</b>exam diets</div>' +
      '</div></section>' +
      '<div class="subs">' + cards + '</div>' +
      '<div class="panels">' +
      '<div class="panel"><h3>Read it chapter-first</h3><p>Each subject opens as a list of chapters, ' +
      'not a pile of topics. Inside a chapter the subtopics are numbered as the study text numbers ' +
      'them, so what you read here lines up with what you revise from.</p></div>' +
      '<div class="panel"><h3>Maths set as maths</h3><p>Every formula is typeset — real fractions, ' +
      'radicals, summations and limits — rendered natively by the browser. <b>Quantitative Analysis</b> ' +
      'and the calculation side of <b>Financial Accounting</b> are written that way throughout.</p></div>' +
      '<div class="panel"><h3>Quiz after every chapter</h3><p>Objective questions drawn from the past ' +
      'papers and written fresh from the chapter, each with the reasoning underneath, plus theory ' +
      'questions with model answers you can write against.</p></div>' +
      '<div class="panel"><h3>Sit a whole paper</h3><p>24 diets, four papers each, three hours on ' +
      'the clock. Section A marks itself; Section B gives you the official solution and the ' +
      'examiner&rsquo;s report once you have written yours.</p></div>' +
      '</div>' +
      '<section class="ghead"><h2>Study guides</h2><p>One topic, everything about it, in one ' +
      'page — pulled together across chapters, with every past question that touches it.</p>' +
      '</section>' +
      '<div class="subs">' + GUIDES.map(function (g) {
        return '<a class="subcard" href="' + g.href + '">' +
          '<div class="r1"><span class="code">' + esc(g.tag) + '</span></div>' +
          '<h2>' + esc(g.title) + '</h2>' +
          '<div class="sub">' + esc(g.blurb) + '</div></a>';
      }).join('') + '</div>' +
      '</div>');
  };

  VIEWS.about = function () {
    h('<div class="wrap"><div class="col" style="padding:44px 0 70px">' +
      '<h1 style="font-size:34px;letter-spacing:-.03em">About this site</h1>' +
      '<p style="margin-top:16px;color:var(--ink2)">Built from the 2025 ATSWA Part II study texts ' +
      '(fifth edition) and the 24 INSIGHT past-question packs from March 2014 to March 2026. ' +
      'The chapter notes are written from the study texts; the past papers are the real papers, ' +
      'with the examiners&rsquo; own solutions.</p>' +
      '<p style="color:var(--ink2)">Nothing here replaces the study text or your tutor. Where a ' +
      'printed paper is defective, this site says so rather than quietly picking a side.</p>' +
      '</div></div>');
  };

  /* =================================================================== */
  /*  subject                                                            */
  /* =================================================================== */
  VIEWS.subject = function (code) {
    var s = subOf(code);
    if (!s) return VIEWS.home();
    loading(s.name);
    need(code, s.file, function (d) {
      if (!d) return h('<div class="wrap"><p style="padding:60px 0">Could not load ' +
        esc(s.name) + '. Serve this folder over http:// rather than opening the file directly.</p></div>');
      var p = prog();
      var rows = d.chapters.map(function (c) {
        var r = p[code + '/' + c.n] || {};
        var mark = r.quiz ? '<span class="pill on">' + Math.round((r.best || 0) * 100) + '%</span>'
                          : (r.read ? '<span class="pill">read</span>' : '');
        return '<a class="chrow" href="#/s/' + code + '/' + c.n + '">' +
          '<span class="n">' + c.n + '</span>' +
          '<span class="body"><span class="t">' + esc(c.t) + '</span>' +
          '<span class="d">' + esc(c.brief || '') + '</span></span>' +
          '<span class="meta">' + mark +
          '<span class="dot' + (r.read ? ' on' : '') + '"></span></span></a>';
      }).join('');
      var st = subStats(code);
      h('<div class="wrap"><section class="shead">' +
        '<div class="code">' + code + ' &middot; Part II</div>' +
        '<h1>' + esc(s.name) + '</h1>' +
        '<p>' + esc(d.intro || s.blurb) + '</p>' +
        '<div class="sbar">' +
        '<a class="btn pri" href="#/s/' + code + '/1">Start at chapter 1</a>' +
        '<a class="btn" href="#/exams?s=' + code + '">Past papers</a>' +
        '<span style="flex:1"></span>' +
        '<span class="eyebrow">' + st.read + ' of ' + st.n + ' read &middot; ' +
        st.done + ' quizzed</span>' +
        '</div></section>' +
        '<div class="chlist" style="margin-top:26px">' + rows + '</div></div>');
    });
  };

  /* Past questions this chapter's material has actually been examined
     with, gathered lazily (the exam bank is a separate, larger file) and
     dropped into the #pq-panel placeholder once it loads. Each row goes to
     the full past paper, official solution and all — the reverse direction
     of the "Source" links on a past question, which land back here. */
  function stemText(q) {
    var s = q.stem !== undefined ? q.stem : q.q;
    return (typeof s === 'string' ? s : (s && s.t) || '').replace(/\*\*/g, '');
  }
  function fillPqPanel(code, n, c) {
    need('EXAMS', 'exams', function (ex) {
      updateQuizCta(code, n, c, ex);
      var box = el('pq-panel');
      if (!box || !ex) return;
      /* diet (e.g. "2026-03") -> { name, rows: [...] }; 24 diets deep now,
         so grouped by diet and collapsed by default rather than one long
         flat list — the group header carries the year, so each row no
         longer needs to repeat it. */
      var groups = {};
      function add(diet, name, row) {
        var g = groups[diet] || (groups[diet] = { name: name, rows: [] });
        g.rows.push(row);
      }
      ex.papers.forEach(function (p) {
        if (p.subject !== code) return;
        p.mcq.forEach(function (q) {
          if (q.ch === n && p.key[q.n]) add(p.diet, p.name, { kind: 'MCQ', label: 'Q' + q.n,
            txt: stemText(q), href: '#/exams/' + p.diet + '/' + code });
        });
        p.saq.forEach(function (q) {
          if (q.ch === n && q.ans) add(p.diet, p.name, { kind: 'Short answer', label: 'Q' + q.n,
            txt: q.body.join(' '), href: '#/exams/' + p.diet + '/' + code });
        });
        p.secb.forEach(function (b) {
          if (b.ch === n && b.solution && b.solution.length) add(p.diet, p.name, {
            kind: 'Section B', label: 'Q' + b.n,
            txt: (b.q && b.q[0]) || 'See the full question in the paper.',
            href: '#/exams/' + p.diet + '/' + code });
        });
      });
      var diets = Object.keys(groups).sort().reverse();
      var total = diets.reduce(function (a, d) { return a + groups[d].rows.length; }, 0);
      if (!total) return;
      var body = diets.map(function (d) {
        var g = groups[d];
        return '<details class="pqgroup"><summary>' + esc(g.name) +
          '<span class="n">' + g.rows.length + ' question' +
          (g.rows.length === 1 ? '' : 's') + '</span></summary>' +
          '<div class="pqlist">' + g.rows.map(function (r) {
            return '<a class="pqrow" href="' + r.href + '">' +
              '<span class="tag">' + esc(r.kind) + ' ' + esc(r.label) + '</span>' +
              '<span class="tx">' + esc(r.txt.slice(0, 130)) + (r.txt.length > 130 ? '…' : '') +
              '</span></a>';
          }).join('') + '</div></details>';
      }).join('');
      box.innerHTML = '<section class="sec"><h2><span class="sn">&#9679;</span>' +
        '<span>Examined before</span></h2>' +
        '<p>This chapter’s material has come up ' + total + ' time' +
        (total === 1 ? '' : 's') + ' across ' + diets.length + ' diet' +
        (diets.length === 1 ? '' : 's') + ' of past papers. Attempt them, with the official ' +
        'answer, in the <a href="#/s/' + code + '/' + n + '/quiz">chapter quiz</a> — or open a ' +
        'diet below to see the paper itself.</p>' + body + '</section>';
    });
  }

  /* The "Take the chapter quiz · N" button is first painted with only the
     authored count, because that is all that is known synchronously — the
     quiz itself also folds in every past question matched to this chapter
     (see quiz.js chapterQuestions), which can only be counted once the exam
     bank has loaded. Reconcile the two once it has, rather than leave the
     button quietly promising fewer questions than the quiz actually has. */
  function updateQuizCta(code, n, c, ex) {
    var btn = el('quiz-cta'), span = el('quiz-cta-n');
    if (!btn || !span || !ex || !ATSWA.chapterQuestions) return;
    var built = ATSWA.chapterQuestions(code, n, c, ex);
    var total = built.mcq.length + built.theory.length;
    if (!total) { btn.style.display = 'none'; return; }
    span.textContent = total;
    btn.style.display = '';
  }

  /* =================================================================== */
  /*  chapter reader                                                     */
  /* =================================================================== */
  VIEWS.chapter = function (code, n) {
    var s = subOf(code);
    if (!s) return VIEWS.home();
    loading(s.name);
    need(code, s.file, function (d) {
      if (!d) return VIEWS.subject(code);
      var c = null;
      for (var i = 0; i < d.chapters.length; i++) if (d.chapters[i].n === n) c = d.chapters[i];
      if (!c) return VIEWS.subject(code);
      markRead(code, n);

      var toc = (c.secs || []).map(function (sec) {
        return '<a href="#sec-' + esc(sec.n).replace(/\./g, '-') + '">' + esc(sec.t) + '</a>';
      }).join('');
      var secs = (c.secs || []).map(function (sec) {
        return '<section class="sec" id="sec-' + esc(sec.n).replace(/\./g, '-') + '">' +
          '<h2><span class="sn">' + esc(sec.n) + '</span><span>' + esc(sec.t) + '</span></h2>' +
          R.blocks(sec.b) + '</section>';
      }).join('');
      var fbox = c.formulas && c.formulas.length
        ? R.block({ fbox: { h: 'Formulas in this chapter', rows: c.formulas } }) : '';
      var focus = '';
      if (c.focus || (c.errors && c.errors.length)) {
        focus = '<section class="sec"><h2><span class="sn">&#9679;</span><span>In the exam</span></h2>' +
          (c.focus ? '<p>' + R.inl(c.focus) + '</p>' : '') +
          (c.errors && c.errors.length
            ? R.block({ warn: c.errors.map(function (e) { return { p: e }; }),
                        lbl: 'Marks are lost here' }) : '') +
          '</section>';
      }
      var prev = null, next = null;
      d.chapters.forEach(function (x) {
        if (x.n === n - 1) prev = x; if (x.n === n + 1) next = x;
      });
      var nq = ((c.quiz && c.quiz.mcq) || []).length + ((c.quiz && c.quiz.theory) || []).length;
      var pqBox = '<div id="pq-panel"></div>';

      h('<div class="wrap"><div class="rlayout"><div>' +
        '<header class="chead"><div class="kicker">' + code + ' &middot; Chapter ' + n +
        ' of ' + s.n + '</div><h1>' + esc(c.t) + '</h1>' +
        (c.brief ? '<p class="brief">' + R.inl(c.brief) + '</p>' : '') + '</header>' +
        (c.outcomes && c.outcomes.length
          ? '<div class="lo"><h4>By the end of this chapter you can</h4><ul>' +
            c.outcomes.map(function (o) { return '<li>' + R.inl(o) + '</li>'; }).join('') +
            '</ul></div>' : '') +
        secs + fbox + focus + pqBox +
        '<div class="cfoot">' +
        '<a id="quiz-cta" class="btn pri" href="#/s/' + code + '/' + n + '/quiz"' +
        (nq ? '' : ' style="display:none"') + '>Take the chapter quiz' +
        ' &middot; <span id="quiz-cta-n">' + nq + '</span></a>' +
        '<a class="btn" href="#/s/' + code + '">All chapters</a>' +
        '</div>' +
        '<div class="cnav">' +
        (prev ? '<a href="#/s/' + code + '/' + prev.n + '"><span class="l">Previous</span>' +
                '<span class="t">' + esc(prev.t) + '</span></a>' : '<span style="flex:1"></span>') +
        (next ? '<a class="nx" href="#/s/' + code + '/' + next.n + '"><span class="l">Next</span>' +
                '<span class="t">' + esc(next.t) + '</span></a>' : '<span style="flex:1"></span>') +
        '</div>' +
        '</div><aside class="rtoc"><h4>In this chapter</h4>' + toc + '</aside></div></div>');
      spyToc();
      scrollToAnchor();
      fillPqPanel(code, n, c);
    });
  };

  /* A past-question citation links to "#/s/FA/2?sec=2-6" — the chapter route
     already carries the reader there; this lands them on the exact section
     the question was worked from, with a brief highlight so it is easy to
     find on the page rather than merely scrolled past. */
  function scrollToAnchor() {
    var sec = route.q.sec;
    if (!sec) { window.scrollTo(0, 0); return; }
    var el = document.getElementById('sec-' + sec);
    if (!el) { window.scrollTo(0, 0); return; }
    window.scrollTo(0, 0);
    setTimeout(function () {
      el.scrollIntoView({ block: 'start', behavior: 'smooth' });
      el.classList.add('landed');
      setTimeout(function () { el.classList.remove('landed'); }, 2600);
    }, 30);
  }
  function spyToc() {
    var links = [].slice.call(document.querySelectorAll('.rtoc a'));
    var secs = [].slice.call(document.querySelectorAll('.sec[id]'));
    if (!links.length) return;
    var onScroll = function () {
      var y = window.scrollY + 120, cur = secs[0];
      secs.forEach(function (s) { if (s.offsetTop <= y) cur = s; });
      links.forEach(function (a) {
        a.classList.toggle('here', cur && a.getAttribute('href') === '#' + cur.id);
      });
    };
    window.removeEventListener('scroll', spyToc._h || function () {});
    spyToc._h = onScroll;
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  return { put: put, need: need, go: go, render: render, tabs: tabs,
           VIEWS: VIEWS, get: get, set: set, PK: PK, prog: prog,
           saveScore: saveScore, subOf: subOf, esc: esc, el: el, h: h,
           fmtClock: fmtClock, pct: pct, optText: optText, optPlain: optPlain,
           stemHTML: stemHTML, preBlock: preBlock, loading: loading,
           closeSheet: function () { closeSheet(); },
           toggleMobileNav: toggleMobileNav, closeMobileNav: closeMobileNav, DATA: DATA,
           subStats: subStats };

  function closeSheet() {
    el('sheet').classList.remove('on'); el('veil').classList.remove('on');
  }
  function closeSearch() { el('srch').classList.remove('on'); }
  function closeMobileNav() {
    var mn = el('mobilenav'), btn = el('btn-menu');
    if (mn) mn.classList.remove('on');
    if (btn) btn.setAttribute('aria-expanded', 'false');
  }
  function toggleMobileNav() {
    var mn = el('mobilenav'), btn = el('btn-menu');
    if (!mn || !btn) return;
    var open = mn.classList.toggle('on');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
})();
