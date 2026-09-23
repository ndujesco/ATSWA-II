/* -- past papers, search, formulas, progress, boot --------------------- */
(function () {
  var A = ATSWA, V = A.VIEWS;

  function withExams(cb) {
    A.loading('Past papers');
    A.need('EXAMS', 'exams', function (ex) {
      if (!ex) return A.h('<div class="wrap"><p style="padding:60px 0">Could not load the past ' +
        'papers. Serve this folder over http:// rather than opening the file directly.</p></div>');
      cb(ex);
    });
  }
  function findPaper(ex, diet, code) {
    for (var i = 0; i < ex.papers.length; i++)
      if (ex.papers[i].diet === diet && ex.papers[i].subject === code) return ex.papers[i];
    return null;
  }
  /* the "Chapter N" tag on a past question: a plain badge where there is no
     confident section match, a link straight to the passage it was worked
     from where there is */
  function chBadge(subj, q) {
    if (!q.ch) return '';
    if (q.sec) return '<a class="ch" href="#/s/' + subj + '/' + q.ch + '?sec=' +
      String(q.sec).replace(/\./g, '-') + '">Chapter ' + q.ch + ' &rarr;</a>';
    return '<a class="ch" href="#/s/' + subj + '/' + q.ch + '">Chapter ' + q.ch + '</a>';
  }

  /* ---- index -------------------------------------------------------- */
  V.exams = function () {
    withExams(function (ex) {
      var only = route_q('s');
      var diets = {};
      ex.papers.forEach(function (p) { (diets[p.diet] = diets[p.diet] || []).push(p); });
      var order = Object.keys(diets).sort().reverse();
      var body = order.map(function (d) {
        var ps = diets[d].filter(function (p) { return !only || p.subject === only; });
        if (!ps.length) return '';
        return '<h3 style="font-size:20px;margin:34px 0 12px;letter-spacing:-.02em">' +
          A.esc(ps[0].name) + '</h3><div class="dietgrid">' +
          ps.map(function (p) {
            var s = A.subOf(p.subject);
            return '<a class="dietcard" href="#/exams/' + p.diet + '/' + p.subject + '" ' +
              'data-sub="' + p.subject + '">' +
              '<div class="d">' + p.subject + '</div><h3>' + A.esc(s ? s.name : p.subject) + '</h3>' +
              '<div class="m"><span>' + p.mcq.length + ' MCQ</span><span>' + p.saq.length +
              ' short</span><span>' + p.secb.length + ' essay</span></div></a>';
          }).join('') + '</div>';
      }).join('');
      var oldest = diets[order[order.length - 1]][0].name;
      var newest = diets[order[0]][0].name;
      A.h('<div class="wrap"><section class="shead" style="border:none">' +
        '<div class="code">Past papers</div><h1>' + order.length + ' diets, ' +
        ex.papers.length + ' papers</h1>' +
        '<p>Every ATSWA Part II paper from ' + A.esc(oldest) + ' to ' + A.esc(newest) +
        ', exactly as sat, with the examiners&rsquo; own solutions and reports. Read one ' +
        'through, or sit it against the clock.</p>' +
        (only ? '<div class="sbar"><a class="btn" href="#/exams">Show all subjects</a></div>' : '') +
        '</section>' + body + '<div style="height:60px"></div></div>');
    });
  };
  function route_q(k) {
    var raw = location.hash, i = raw.indexOf('?');
    if (i < 0) return '';
    var out = '';
    raw.slice(i + 1).split('&').forEach(function (kv) {
      var p = kv.split('='); if (decodeURIComponent(p[0]) === k) out = decodeURIComponent(p[1] || '');
    });
    return out;
  }

  /* ---- one paper, read through ------------------------------------- */
  V.paper = function (diet, code) {
    withExams(function (ex) {
      var p = findPaper(ex, diet, code);
      if (!p) return V.exams();
      var s = A.subOf(code);

      var mcq = p.mcq.map(function (q) {
        var ans = p.key[q.n];
        var flag = ex.flags[diet + '/' + code + '/mcq/' + q.n];
        return '<div class="bq"><div class="h"><span class="n">' + q.n + '</span>' +
          chBadge(code, q) + '</div>' +
          '<div class="body">' + A.preBlock(q.pre) + A.stemHTML(q) +
          '<div style="margin-top:10px">' + q.options.map(function (o, k) {
            var on = ans === 'ABCDE'[k];
            return '<div style="display:flex;gap:10px;padding:4px 0' +
              (on ? ';color:var(--ok);font-weight:600' : '') + '">' +
              '<span class="mono" style="width:1.4em;flex:none">' + 'ABCDE'[k] + '</span>' +
              '<span style="flex:1">' + A.optText(o) + '</span>' +
              (on ? '<span class="mono" style="font-size:10px;letter-spacing:.1em">ANSWER</span>' : '') +
              '</div>';
          }).join('') + '</div>' +
          (flag ? '<div class="flagbox" style="margin:12px 0 0"><div class="lbl">Check this</div>' +
                  A.esc(flag) + '</div>' : '') +
          '</div></div>';
      }).join('');

      var saq = p.saq.map(function (q) {
        var badge = chBadge(code, q);
        return '<div class="saqrow"><span class="n">' + q.n + '</span><div class="b">' +
          A.preBlock(q.pre) +
          '<div>' + R.inl(q.body.join(' ')) + '</div>' +
          (q.ans ? '<div class="ans"><div class="lbl">Official answer</div>' +
                   R.inl(q.ans.join(' ')) + '</div>' : '') +
          (badge ? '<div style="margin-top:8px">' + badge + '</div>' : '') +
          '</div></div>';
      }).join('');

      var secb = p.secb.map(function (b) {
        return '<div class="bq"><div class="h"><span class="n">Question ' + b.n + '</span>' +
          chBadge(code, b) + '</div>' +
          (b.q && b.q.length ? '<div class="body"><div class="pre">' +
            A.esc(b.q.join('\n')) + '</div></div>' : '') +
          '<button class="reveal" data-reveal="sol' + p.diet + code + b.n + '">' +
          'Show the official solution</button>' +
          '<div class="sol hid" id="sol' + p.diet + code + b.n + '">' +
          (b.note ? R.blocks(b.note) : '') +
          '<div class="pre">' + A.esc(b.solution.join('\n')) + '</div>' +
          (b.examiner && b.examiner.length
            ? '<div class="exm"><div class="lbl">Examiner&rsquo;s report</div>' +
              A.esc(b.examiner.join(' ')) + '</div>' : '') +
          '</div></div>';
      }).join('');

      A.h('<div class="wrap"><section class="paperhead">' +
        '<div class="code">' + A.esc(p.name) + ' &middot; ' + code + '</div>' +
        '<h1 style="font-size:clamp(28px,4.4vw,42px);letter-spacing:-.032em;margin-top:8px">' +
        A.esc(s ? s.name : code) + '</h1>' +
        '<div class="sbar"><a class="btn pri" href="#/exams/' + diet + '/' + code + '/sit">' +
        'Sit this paper &middot; 3 hours</a>' +
        '<a class="btn" href="#/exams">All papers</a>' +
        '<button class="btn" data-revealall="1">Reveal every solution</button></div>' +
        '</section>' +
        '<div class="secmark"><h2>Section A, Part I</h2><span class="mk">Multiple choice ' +
        '&middot; 30 marks</span></div>' + mcq +
        '<div class="secmark"><h2>Section A, Part II</h2><span class="mk">Short answer ' +
        '&middot; 20 marks</span></div><div style="margin-bottom:30px">' + saq + '</div>' +
        '<div class="secmark"><h2>Section B</h2><span class="mk">Answer any four ' +
        '&middot; 50 marks</span></div>' + secb +
        '<div style="height:60px"></div></div>');
    });
  };

  /* ---- sit the paper ------------------------------------------------- */
  V.sit = function (diet, code) {
    withExams(function (ex) {
      var p = findPaper(ex, diet, code);
      if (!p) return V.exams();
      var s = A.subOf(code);
      var mcq = p.mcq.map(function (q) {
        var ans = p.key[q.n];
        return {
          q: q.stem, o: q.options, a: 'ABCDE'.indexOf(ans), pre: q.pre || [], past: true,
          src: p.name + ' &middot; Q' + q.n, ch: q.ch, sec: q.sec,
          w: ex.notes[diet + '/' + code + '/mcq/' + q.n] || '',
          flag: ex.flags[diet + '/' + code + '/mcq/' + q.n] || ''
        };
      }).filter(function (q) { return q.a >= 0; });
      var theory = p.saq.filter(function (q) { return q.ans; }).map(function (q) {
        return { q: q.body.join(' '), marks: 1, short: true, pre: q.pre || [],
                 a: [{ p: '**' + q.ans.join(' ') + '**' }],
                 src: p.name + ' &middot; Short answer ' + q.n, ch: q.ch, sec: q.sec };
      }).concat(p.secb.map(function (b) {
        return { q: 'Question ' + b.n + ' — see the paper for the full text.',
                 marks: 12.5, pre: b.q || [],
                 a: [{ pre: b.solution.join('\n') }].concat(
                    b.examiner && b.examiner.length
                      ? [{ note: b.examiner.join(' '), lbl: "Examiner's report" }] : []),
                 src: p.name + ' &middot; Section B, Q' + b.n, ch: b.ch, sec: b.sec };
      }));
      var kkey = A.PK + 'sit:' + diet + '/' + code + ':start';
      var started = A.get(kkey, 0);
      if (!started) { started = Date.now(); A.set(kkey, started); }
      A.quizStart({
        key: 'sit:' + diet + '/' + code,
        title: A.esc(p.name) + ' &middot; ' + (s ? s.name : code),
        back: '#/exams/' + diet + '/' + code,
        code: code,
        mcq: mcq, theory: theory,
        exam: true, deadline: started + 3 * 60 * 60 * 1000
      });
    });
  };

  /* ---- formula index ------------------------------------------------- */
  V.formulas = function () {
    var want = SUBJECTS.filter(function (s) { return s.formulas !== false; });
    A.loading('Formulas');
    var got = 0, all = {};
    want.forEach(function (s) {
      A.need(s.code, s.file, function (d) {
        all[s.code] = d; got++;
        if (got === want.length) show();
      });
    });
    function show() {
      var body = want.map(function (s) {
        var d = all[s.code];
        if (!d) return '';
        var chunks = d.chapters.filter(function (c) { return c.formulas && c.formulas.length; })
          .map(function (c) {
            return '<h3 style="font-size:18px;margin:26px 0 10px;letter-spacing:-.02em">' +
              '<a href="#/s/' + s.code + '/' + c.n + '">' + c.n + '. ' + A.esc(c.t) + '</a></h3>' +
              R.block({ fbox: { h: '', rows: c.formulas } });
          }).join('');
        if (!chunks) return '';
        return '<section data-sub="' + s.code + '" style="margin-bottom:44px">' +
          '<div class="secmark"><h2>' + A.esc(s.name) + '</h2>' +
          '<span class="mk">' + s.code + '</span></div>' + chunks + '</section>';
      }).join('');
      A.h('<div class="wrap"><section class="shead" style="border:none">' +
        '<div class="code">Reference</div><h1>Every formula, in one place</h1>' +
        '<p>Pulled from the chapters, in chapter order. Each heading links back to where the ' +
        'formula is derived and used.</p></section>' + (body ||
        '<p style="padding:40px 0;color:var(--ink3)">No formulas recorded yet.</p>') +
        '<div style="height:60px"></div></div>');
    }
  };

  /* ---- progress ------------------------------------------------------ */
  V.progress = function () {
    var p = A.prog();
    var cards = SUBJECTS.map(function (s) {
      var st = A.subStats(s.code);
      var heat = [];
      for (var i = 1; i <= s.n; i++) {
        var r = p[s.code + '/' + i] || {};
        var v = 0;
        if (r.read) v = 1;
        if (r.quiz) v = r.best >= 0.8 ? 4 : r.best >= 0.6 ? 3 : 2;
        heat.push('<i data-v="' + v + '" title="Chapter ' + i + '"></i>');
      }
      return '<div class="pcard" data-sub="' + s.code + '">' +
        '<div class="s">' + s.code + '</div><h3>' + A.esc(s.name) + '</h3>' +
        '<div class="heat">' + heat.join('') + '</div>' +
        '<div style="margin-top:14px;display:flex;gap:18px;font-family:var(--mono);' +
        'font-size:11px;color:var(--ink3)">' +
        '<span><b style="color:var(--ink)">' + st.read + '</b>/' + st.n + ' read</span>' +
        '<span><b style="color:var(--ink)">' + st.done + '</b> quizzed</span>' +
        (st.done ? '<span><b style="color:var(--ink)">' + st.avg + '%</b> avg</span>' : '') +
        '</div>' +
        '<div style="margin-top:14px"><a class="btn sm" href="#/s/' + s.code + '">Open</a></div>' +
        '</div>';
    }).join('');
    A.h('<div class="wrap"><section class="shead" style="border:none">' +
      '<div class="code">Progress</div><h1>Where you are</h1>' +
      '<p>Kept in this browser only. Reading a chapter marks it; taking its quiz records your ' +
      'best score.</p></section>' +
      '<div class="pgrid">' + cards + '</div>' +
      '<div style="margin-bottom:70px"><button class="btn" id="wipe">Clear all progress</button></div>' +
      '</div>');
    var w = A.el('wipe');
    if (w) w.addEventListener('click', function () {
      if (w.dataset.armed) {
        try {
          var ks = [];
          for (var i = 0; i < localStorage.length; i++) {
            var k = localStorage.key(i);
            if (k.indexOf(A.PK) === 0) ks.push(k);
          }
          ks.forEach(function (k) { localStorage.removeItem(k); });
        } catch (e) {}
        location.reload();
      } else { w.dataset.armed = '1'; w.textContent = 'Click again to erase everything'; }
    });
  };

  /* ---- search --------------------------------------------------------- */
  var IDX = null, building = false;
  function buildIndex(done) {
    if (IDX) return done(IDX);
    if (building) return;
    building = true;
    var got = 0;
    IDX = [];
    SUBJECTS.forEach(function (s) {
      A.need(s.code, s.file, function (d) {
        if (d) d.chapters.forEach(function (c) {
          IDX.push({ t: c.n + '. ' + c.t, c: c.brief || '', w: s.code + ' chapter',
                     u: '#/s/' + s.code + '/' + c.n,
                     x: (c.t + ' ' + (c.brief || '') + ' ' +
                         (c.outcomes || []).join(' ')).toLowerCase() });
          (c.secs || []).forEach(function (sec) {
            IDX.push({ t: sec.t, c: R.text(sec.b).slice(0, 220),
                       w: s.code + ' ' + sec.n,
                       u: '#/s/' + s.code + '/' + c.n + '#sec-' + String(sec.n).replace(/\./g, '-'),
                       x: (sec.t + ' ' + R.text(sec.b)).toLowerCase() });
          });
        });
        if (++got === SUBJECTS.length) { building = false; done(IDX); }
      });
    });
  }
  function runSearch(qs) {
    var out = A.el('srch-o');
    var q = qs.trim().toLowerCase();
    if (q.length < 2) { out.innerHTML = '<div class="empty">Type at least two letters.</div>'; return; }
    buildIndex(function (idx) {
      var terms = q.split(/\s+/);
      var hits = [];
      idx.forEach(function (r) {
        var sc = 0;
        terms.forEach(function (t) {
          var i = r.x.indexOf(t);
          if (i < 0) { sc = -1e9; return; }
          sc += 12 - Math.min(10, i / 60);
          if (r.t.toLowerCase().indexOf(t) >= 0) sc += 24;
        });
        if (sc > 0) hits.push({ r: r, s: sc });
      });
      hits.sort(function (a, b) { return b.s - a.s; });
      if (!hits.length) { out.innerHTML = '<div class="empty">Nothing found.</div>'; return; }
      out.innerHTML = hits.slice(0, 40).map(function (x, i) {
        return '<a class="hit' + (i === 0 ? ' on' : '') + '" href="' + x.r.u + '">' +
          '<span class="w">' + A.esc(x.r.w) + '</span>' +
          '<div class="t">' + hl(x.r.t, terms) + '</div>' +
          '<div class="c">' + hl(x.r.c, terms) + '</div></a>';
      }).join('');
    });
  }
  function hl(s, terms) {
    s = A.esc(s);
    terms.forEach(function (t) {
      if (!t) return;
      s = s.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'),
                    '<mark>$1</mark>');
    });
    return s;
  }
  function openSearch() {
    A.el('srch').classList.add('on');
    var i = A.el('srch-i'); i.value = ''; i.focus();
    A.el('srch-o').innerHTML = '<div class="empty">Search every chapter and section.</div>';
    buildIndex(function () {});
  }

  /* ---- boot ----------------------------------------------------------- */
  function theme() {
    var t = A.get(A.PK + 'theme', null);
    if (t) document.documentElement.setAttribute('data-theme', t);
  }
  function toggleTheme() {
    var cur = document.documentElement.getAttribute('data-theme');
    var dark = window.matchMedia && window.matchMedia('(prefers-color-scheme:dark)').matches;
    var next = cur ? (cur === 'dark' ? 'light' : 'dark') : (dark ? 'light' : 'dark');
    document.documentElement.setAttribute('data-theme', next);
    A.set(A.PK + 'theme', next);
  }

  function foot() {
    A.el('foot').innerHTML = '<p>Written from the 2025 ATSWA Part&nbsp;II study texts (fifth ' +
      'edition) and the INSIGHT past-question packs, March 2014 to March 2026. The chapter notes ' +
      'are a study aid, not a substitute for the study text; check anything that matters against ' +
      'it and against your tutor. <a href="#/about">About</a></p>' +
      '<p style="margin-top:10px;font-size:13px;color:var(--ink4)">Keys: <b>A</b>&ndash;<b>E</b> ' +
      'answer &middot; <b>S</b> show answer &middot; <b>J</b> jump &middot; <b>/</b> search ' +
      '&middot; <b>Esc</b> close</p>';
  }

  function boot() {
    theme(); foot();
    A.el('btn-theme').addEventListener('click', toggleTheme);
    A.el('btn-search').addEventListener('click', openSearch);
    A.el('btn-menu').addEventListener('click', A.toggleMobileNav);
    A.el('sheet-x').addEventListener('click', A.closeSheet);
    A.el('veil').addEventListener('click', A.closeSheet);
    A.el('srch').addEventListener('click', function (e) {
      if (e.target.id === 'srch') A.el('srch').classList.remove('on');
    });
    A.el('srch-i').addEventListener('input', function (e) { runSearch(e.target.value); });
    A.el('srch-i').addEventListener('keydown', function (e) {
      var hits = [].slice.call(document.querySelectorAll('.srch .hit'));
      var cur = hits.findIndex(function (x) { return x.classList.contains('on'); });
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (!hits.length) return;
        var ni = Math.max(0, Math.min(hits.length - 1, cur + (e.key === 'ArrowDown' ? 1 : -1)));
        hits.forEach(function (x) { x.classList.remove('on'); });
        hits[ni].classList.add('on'); hits[ni].scrollIntoView({ block: 'nearest' });
      }
      if (e.key === 'Enter' && hits[cur < 0 ? 0 : cur]) {
        e.preventDefault();
        location.hash = hits[cur < 0 ? 0 : cur].getAttribute('href');
        A.el('srch').classList.remove('on');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (/^(INPUT|TEXTAREA)$/.test(e.target.tagName)) {
        if (e.key === 'Escape') { A.el('srch').classList.remove('on'); e.target.blur(); }
        return;
      }
      if (e.key === '/' && !e.metaKey && !e.ctrlKey) { e.preventDefault(); openSearch(); }
      if (e.key === 'Escape') { A.el('srch').classList.remove('on'); A.closeSheet(); A.closeMobileNav(); }
    });
    document.addEventListener('click', function (e) {
      var mn = A.el('mobilenav');
      if (mn && mn.classList.contains('on') &&
          !e.target.closest('#mobilenav') && !e.target.closest('#btn-menu')) {
        A.closeMobileNav();
      }
    });
    document.addEventListener('click', function (e) {
      var t = e.target.closest && e.target.closest('[data-revealall]');
      if (!t) return;
      [].slice.call(document.querySelectorAll('.sol.hid, .az.hid')).forEach(function (x) {
        x.classList.remove('hid');
      });
      [].slice.call(document.querySelectorAll('.reveal')).forEach(function (x) { x.remove(); });
      t.remove();
    });
    window.addEventListener('hashchange', function () {
      /* A bare "#sec-2-6" hash is an in-page jump — the "In this chapter"
         sidebar links on the chapter reader use exactly this — not a route.
         Re-rendering on it would tear down the very page it is meant to
         scroll within (parseHash sees no "/s/..." prefix and falls back to
         the home view), so it gets a plain native-style scroll and nothing
         else. Every real route change still re-renders as before. */
      if (/^#sec-[\w-]+$/.test(location.hash)) {
        var el = document.getElementById(location.hash.slice(1));
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        return;
      }
      ATSWA.quizClear();
      A.render(); A.tabs();
      var m = location.hash.match(/#sec-[\w-]+$/);
      if (m) {
        setTimeout(function () {
          var t = document.getElementById(m[0].slice(1));
          if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 60);
      }
    });
    A.render(); A.tabs();
  }

  if (document.readyState === 'loading')
    document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
