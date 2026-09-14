/* -- quiz engine -------------------------------------------------------
   One engine drives the chapter quizzes and the Section A of a past paper.
   A question is normalised to { q, o, a, w, calc, src, flag, pre }. */
(function () {
  var A = ATSWA, V = A.VIEWS;
  var Q = null;   // live quiz state

  function key(k) { return A.PK + 'quiz:' + k; }

  function normPast(q, ans, label) {
    return {
      q: q.stem, o: q.options, a: 'ABCDE'.indexOf(ans),
      pre: q.pre || [], src: label, past: true, w: q.w || '', calc: q.calc || '',
      flag: q.flag || '', sec: q.sec || ''
    };
  }

  /* build the question list for a chapter: authored first, then the real
     past-paper questions that were mapped to this chapter — MCQs and short
     answers feed the multiple-choice run, Section B essays feed the theory
     run, so every past question this chapter was matched to shows up as
     practice here, not only in the paper it was sat in. */
  function chapterQuestions(code, n, chapter, exams) {
    var mcq = ((chapter.quiz && chapter.quiz.mcq) || []).map(function (q) {
      return {
        q: q.q, o: q.o, a: q.a, w: q.w || '', calc: q.calc || '',
        src: q.src || 'Written for this chapter', pre: q.pre || [], flag: q.flag || '',
        sec: q.sec || ''
      };
    });
    if (exams) {
      exams.papers.forEach(function (p) {
        if (p.subject !== code) return;
        p.mcq.forEach(function (q) {
          if (q.ch !== n) return;
          var ans = p.key[q.n];
          if (!ans) return;
          var built = normPast(q, ans, p.name + ' &middot; Q' + q.n);
          built.w = (exams.notes[p.diet + '/' + p.subject + '/mcq/' + q.n] || '');
          built.flag = (exams.flags[p.diet + '/' + p.subject + '/mcq/' + q.n] || '');
          mcq.push(built);
        });
      });
    }
    var theory = ((chapter.quiz && chapter.quiz.theory) || []).slice();
    if (exams) {
      exams.papers.forEach(function (p) {
        if (p.subject !== code) return;
        p.saq.forEach(function (q) {
          if (q.ch !== n || !q.ans) return;
          theory.push({
            q: q.body.join(' '), marks: 1, short: true,
            a: [{ p: '**' + q.ans.join(' ') + '**' }],
            src: p.name + ' &middot; Short answer ' + q.n, pre: q.pre || [], sec: q.sec || ''
          });
        });
      });
      exams.papers.forEach(function (p) {
        if (p.subject !== code) return;
        p.secb.forEach(function (b) {
          if (b.ch !== n || !b.solution || !b.solution.length) return;
          var a = [{ pre: b.solution.join('\n') }];
          if (b.examiner && b.examiner.length) a.push({ note: b.examiner.join(' ') });
          theory.push({
            q: 'Section B &middot; Question ' + b.n + ' &mdash; the full text is above.',
            marks: 12.5, pre: b.q || [], a: a,
            src: p.name + ' &middot; Question ' + b.n, sec: b.sec || ''
          });
        });
      });
    }
    return { mcq: mcq, theory: theory };
  }
  /* a source citation becomes a link back to the exact section, when a
     section match exists; otherwise it stays as plain, honest text */
  function citeHTML(q, code, ch, style) {
    if (!q.src) return '';
    var label = 'Source &middot; ' + q.src;
    var sty = style ? ' style="' + style + '"' : '';
    var useCh = q.ch || ch;
    if (q.sec && code && useCh) {
      return '<a class="cite"' + sty + ' href="#/s/' + code + '/' + useCh + '?sec=' +
        String(q.sec).replace(/\./g, '-') + '">' + label + ' &rarr;</a>';
    }
    return '<div class="cite"' + sty + '>' + label + '</div>';
  }

  /* ---- state -------------------------------------------------------- */
  function load(k, n) {
    var s = A.get(key(k), null);
    if (!s || s.n !== n) s = { n: n, i: 0, ans: {}, look: {}, phase: 'mcq', ti: 0 };
    return s;
  }
  function save() { if (Q) A.set(key(Q.key), Q.s); }

  function tally() {
    var r = 0, w = 0, l = 0;
    Q.mcq.forEach(function (q, i) {
      if (Q.s.look[i]) { l++; return; }
      var a = Q.s.ans[i];
      if (a === undefined) return;
      if (a === q.a) r++; else w++;
    });
    return { r: r, w: w, l: l, done: r + w + l, n: Q.mcq.length };
  }

  /* ---- chapter quiz view -------------------------------------------- */
  V.quiz = function (code, n) {
    var s = A.subOf(code);
    if (!s) return V.home();
    A.loading('Quiz');
    A.need(code, s.file, function (d) {
      if (!d) return V.subject(code);
      var c = null;
      d.chapters.forEach(function (x) { if (x.n === n) c = x; });
      if (!c) return V.subject(code);
      A.need('EXAMS', 'exams', function (ex) {
        var built = chapterQuestions(code, n, c, ex);
        if (!built.mcq.length && !built.theory.length) {
          return A.h('<div class="wrap"><div class="col" style="padding:60px 0">' +
            '<h1>No quiz yet</h1><p>This chapter has no questions attached.</p>' +
            '<a class="btn" href="#/s/' + code + '/' + n + '">Back to the chapter</a></div></div>');
        }
        start({
          key: code + '/' + n,
          title: 'Ch ' + n + ' &middot; ' + c.t,
          back: '#/s/' + code + '/' + n,
          code: code, ch: n,
          mcq: built.mcq, theory: built.theory
        });
      });
    });
  };

  function start(cfg) {
    Q = {
      key: cfg.key, title: cfg.title, back: cfg.back, code: cfg.code, ch: cfg.ch,
      mcq: cfg.mcq, theory: cfg.theory,
      s: load(cfg.key, cfg.mcq.length + cfg.theory.length),
      exam: cfg.exam || false, deadline: cfg.deadline || 0
    };
    if (Q.s.i >= Q.mcq.length) Q.s.i = Math.max(0, Math.min(Q.s.i, Q.mcq.length - 1));
    draw();
  }

  function draw() {
    if (!Q) return;
    if (Q.s.phase === 'results') return results();
    if (Q.s.phase === 'theory') return theoryView();
    mcqView();
  }

  function bar(extra) {
    var t = tally();
    if (Q.exam && Q.deadline) {
      var left = Q.deadline - Date.now();
      extra = '<span class="clock' + (left < 15 * 60000 ? ' low' : '') + '" id="clk">' +
              A.fmtClock(left) + '</span>' + (extra || '');
    }
    return '<div class="qbar"><div class="qbar-in">' +
      '<a class="x" href="' + Q.back + '">&larr; Exit</a>' +
      '<span class="nm">' + Q.title + '</span>' +
      '<span class="sc">' + (extra || '') +
      (Q.exam ? '' :
        '<span><b class="r">' + t.r + '</b> <em>right</em></span>' +
        '<span><b class="w">' + t.w + '</b> <em>wrong</em></span>') +
      '</span></div>' +
      '<div class="qprog"><i style="width:' + A.pct(t.done, t.n) + '%"></i></div></div>';
  }

  function mcqView() {
    var i = Q.s.i, q = Q.mcq[i];
    if (!q) { Q.s.phase = Q.theory.length ? 'theory' : 'results'; save(); return draw(); }
    var picked = Q.s.ans[i], looked = Q.s.look[i];
    var shown = (picked !== undefined || looked) && !Q.exam;
    var opts = q.o.map(function (o, k) {
      var st = '';
      if (shown) {
        if (k === q.a) st = 'ok';
        else if (k === picked) st = 'no';
      } else if (k === picked) st = 'pick';
      if (!shown && k === picked) st = 'pick';
      return '<button class="opt" data-pick="' + k + '"' + (shown ? ' disabled' : '') +
        (st ? ' data-s="' + st + '"' : '') + '>' +
        '<span class="bub">' + 'ABCDE'[k] + '</span>' +
        '<span class="tx">' + A.optText(o) + '</span>' +
        (shown && k === q.a ? '<span class="mk">Correct</span>' :
         shown && k === picked ? '<span class="mk">Your answer</span>' : '') +
        '</button>';
    }).join('');

    var why = '';
    if (shown) {
      why = '<div class="why"><div class="lbl">' +
        (looked ? 'Answer' : (picked === q.a ? 'Why that is right' : 'Why the answer is ' +
          'ABCDE'[q.a])) + '</div>' +
        (q.w ? R.blocks(typeof q.w === 'string' ? [{ p: q.w }] : q.w)
             : '<p>The correct option is <b>' + 'ABCDE'[q.a] + '</b> — ' +
               A.optText(q.o[q.a]) + '.</p>') +
        (q.calc ? '<div class="calc">' + (typeof q.calc === 'string'
            ? R.blocks([{ tex: q.calc }]) : R.blocks(q.calc)) + '</div>' : '') +
        citeHTML(q, Q.code, Q.ch) +
        '</div>';
    }

    A.h('<div class="qwrap">' + bar() +
      '<div class="qbody"><div class="qcol">' +
      '<div class="qcard">' +
      '<div class="qhead"><span class="n">' + (i + 1) + '</span>' +
      '<span class="tp">' + (q.past ? 'Past question' : 'Practice') + '</span>' +
      '<span class="sr">' + (i + 1) + ' of ' + Q.mcq.length + '</span></div>' +
      A.preBlock(q.pre) +
      (q.flag ? '<div class="flagbox"><div class="lbl">Check this</div>' +
                R.inl(q.flag) + '</div>' : '') +
      '<div class="qstem">' + A.stemHTML(q) + '</div>' +
      '<div class="opts">' + opts + '</div>' +
      (!shown && !Q.exam
        ? '<button class="showans" data-look="1">I do not know &mdash; show the answer</button>' : '') +
      why +
      '</div></div></div>' +
      '<div class="actbar"><div class="actbar-in">' +
      '<button class="btn" data-nav="-1">&larr; Prev</button>' +
      '<button class="btn" data-jump="1">Jump</button>' +
      '<span class="sp"></span>' +
      '<button class="btn ' + (shown ? 'pri' : '') + '" data-nav="1">' +
      (i === Q.mcq.length - 1 ? (Q.theory.length ? 'Theory section' : 'Finish') : 'Next') +
      ' &rarr;</button>' +
      '</div></div></div>');
    tick();
  }

  var timer = null;
  function tick() {
    if (timer) clearInterval(timer);
    if (!Q || !Q.exam || !Q.deadline) return;
    timer = setInterval(function () {
      var c = document.getElementById('clk');
      if (!c) { clearInterval(timer); return; }
      var left = Q.deadline - Date.now();
      c.textContent = A.fmtClock(left);
      c.className = 'clock' + (left < 15 * 60000 ? ' low' : '');
      if (left <= 0) { clearInterval(timer); Q.s.phase = 'results'; save(); draw(); }
    }, 1000);
  }

  function theoryView() {
    var i = Q.s.ti || 0, t = Q.theory[i];
    if (!t) { Q.s.phase = 'results'; save(); return draw(); }
    var wkey = A.PK + 'wr:' + Q.key + ':' + i;
    var written = A.get(wkey, '');
    var open = Q.s.look['t' + i];
    A.h('<div class="qwrap">' + bar() +
      '<div class="qbody"><div class="qcol">' +
      '<div class="tq">' +
      '<div class="h"><span class="n">' + (i + 1) + '</span>' +
      '<span class="tp" style="font-family:var(--mono);font-size:9.5px;letter-spacing:.12em;' +
      'text-transform:uppercase;color:var(--accent)">' +
      (t.short ? 'Short answer' : 'Theory') + '</span>' +
      '<span class="mk">' + (t.marks ? t.marks + ' marks' : '') + '</span></div>' +
      A.preBlock(t.pre) +
      '<div class="qz">' + R.inl(t.q) + '</div>' +
      '<div class="pad"><textarea id="wr" placeholder="Write your answer here — it is saved as you type.">' +
      A.esc(written) + '</textarea></div>' +
      (open ? '<div class="model">' + R.blocks(t.a) +
              citeHTML(t, Q.code, Q.ch, 'display:block;margin-top:12px;padding-top:10px;' +
                'border-top:1px solid var(--rule2);font-family:var(--mono);font-size:11px;' +
                'color:var(--ink3)') + '</div>'
            : '<button class="showans" data-model="' + i + '">Compare with the model answer</button>') +
      '</div>' +
      '<div style="text-align:center;margin-top:16px" class="eyebrow">Theory ' + (i + 1) +
      ' of ' + Q.theory.length + '</div>' +
      '</div></div>' +
      '<div class="actbar"><div class="actbar-in">' +
      '<button class="btn" data-tnav="-1">&larr; Prev</button>' +
      '<span class="sp"></span>' +
      '<button class="btn pri" data-tnav="1">' +
      (i === Q.theory.length - 1 ? 'See results' : 'Next') + ' &rarr;</button>' +
      '</div></div></div>');
    var ta = A.el('wr');
    if (ta) ta.addEventListener('input', function () { A.set(wkey, ta.value); });
  }

  function results() {
    if (timer) clearInterval(timer);
    if (Q.exam) Q.exam = false;      // reviewing is always in study mode
    var t = tally();
    var score = t.r, out = t.n;
    if (Q.code) A.saveScore(Q.code, Q.ch, score, out);
    var missed = [];
    Q.mcq.forEach(function (q, i) {
      if (Q.s.look[i] || (Q.s.ans[i] !== undefined && Q.s.ans[i] !== q.a)) missed.push({ q: q, i: i });
    });
    var missHTML = missed.length ? missed.map(function (m) {
      return '<div class="brk"><div class="r"><span class="t">' +
        A.stemHTML(m.q).replace(/<[^>]+>/g, '').slice(0, 150) + '</span>' +
        '<button class="btn sm" data-goto="' + m.i + '">Review</button></div></div>';
    }).join('') : '<p style="color:var(--ink3)">Nothing missed.</p>';

    A.h('<div class="qwrap">' + bar() + '<div class="qbody"><div class="qcol res">' +
      '<div class="eyebrow">' + Q.title + '</div>' +
      '<div class="big"><b>' + A.pct(score, out) + '%</b><span>' + score + ' of ' + out + '</span></div>' +
      '<div class="grid3">' +
      '<div><b class="num" style="color:var(--ok)">' + t.r + '</b><span>Right</span></div>' +
      '<div><b class="num" style="color:var(--no)">' + t.w + '</b><span>Wrong</span></div>' +
      '<div><b class="num" style="color:var(--look)">' + t.l + '</b><span>Looked up</span></div>' +
      '<div><b class="num">' + (t.n - t.done) + '</b><span>Skipped</span></div>' +
      '</div>' +
      '<h3 style="margin:30px 0 12px;font-size:19px">What you missed</h3>' + missHTML +
      '<div style="display:flex;gap:10px;margin-top:30px;flex-wrap:wrap">' +
      '<button class="btn pri" data-again="1">Try again</button>' +
      '<a class="btn" href="' + Q.back + '">Back to the chapter</a>' +
      (Q.theory.length ? '<button class="btn" data-phase="theory">Theory questions</button>' : '') +
      '</div></div></div></div>');
  }

  /* ---- jump sheet ---------------------------------------------------- */
  function jump() {
    var cells = Q.mcq.map(function (q, i) {
      var c = '';
      if (Q.s.look[i]) c = 'lk';
      else if (Q.s.ans[i] !== undefined) c = Q.s.ans[i] === q.a ? 'ok' : 'no';
      if (i === Q.s.i) c += ' now';
      return '<button class="' + c + '" data-goto="' + i + '">' + (i + 1) + '</button>';
    }).join('');
    A.el('sheet-t').innerHTML = 'Answer sheet';
    A.el('sheet-b').innerHTML = '<div class="answersheet">' + cells + '</div>' +
      '<div style="display:flex;gap:10px;flex-wrap:wrap">' +
      '<button class="btn" data-shuffle="1">Shuffle</button>' +
      '<button class="btn" data-reset="1">Reset this quiz</button>' +
      (Q.theory.length ? '<button class="btn" data-phase="theory">Theory (' +
        Q.theory.length + ')</button>' : '') +
      '<button class="btn" data-phase="results">Finish and see results</button>' +
      '</div>';
    A.el('sheet').classList.add('on'); A.el('veil').classList.add('on');
  }

  /* ---- events -------------------------------------------------------- */
  document.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target.closest('[data-pick],[data-nav],[data-jump],' +
      '[data-look],[data-goto],[data-again],[data-phase],[data-tnav],[data-model],' +
      '[data-shuffle],[data-reset],[data-reveal]') : null;
    if (!t) return;
    var d = t.dataset;
    if (d.reveal) {
      var box = document.getElementById(d.reveal);
      if (box) { box.classList.remove('hid'); t.remove(); }
      return;
    }
    if (!Q) return;
    if (d.pick !== undefined) {
      Q.s.ans[Q.s.i] = +d.pick; delete Q.s.look[Q.s.i]; save(); draw();
    } else if (d.look) {
      Q.s.look[Q.s.i] = 1; save(); draw();
    } else if (d.nav) {
      var ni = Q.s.i + (+d.nav);
      if (ni < 0) ni = 0;
      if (ni >= Q.mcq.length) {
        Q.s.phase = Q.theory.length ? 'theory' : 'results'; save(); return draw();
      }
      Q.s.i = ni; save(); draw(); window.scrollTo(0, 0);
    } else if (d.tnav) {
      var ti = (Q.s.ti || 0) + (+d.tnav);
      if (ti < 0) { Q.s.phase = 'mcq'; Q.s.ti = 0; save(); return draw(); }
      if (ti >= Q.theory.length) { Q.s.phase = 'results'; save(); return draw(); }
      Q.s.ti = ti; save(); draw(); window.scrollTo(0, 0);
    } else if (d.model !== undefined) {
      Q.s.look['t' + d.model] = 1; save(); draw();
    } else if (d.jump) {
      jump();
    } else if (d.goto !== undefined) {
      Q.s.i = +d.goto; Q.s.phase = 'mcq'; save(); A.closeSheet(); draw(); window.scrollTo(0, 0);
    } else if (d.phase) {
      Q.s.phase = d.phase; save(); A.closeSheet(); draw(); window.scrollTo(0, 0);
    } else if (d.again) {
      Q.s = { n: Q.s.n, i: 0, ans: {}, look: {}, phase: 'mcq', ti: 0 }; save(); draw();
    } else if (d.shuffle) {
      for (var i = Q.mcq.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = Q.mcq[i]; Q.mcq[i] = Q.mcq[j]; Q.mcq[j] = tmp;
      }
      Q.s = { n: Q.s.n, i: 0, ans: {}, look: {}, phase: 'mcq', ti: 0 };
      save(); A.closeSheet(); draw();
    } else if (d.reset) {
      Q.s = { n: Q.s.n, i: 0, ans: {}, look: {}, phase: 'mcq', ti: 0 };
      save(); A.closeSheet(); draw();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (!Q || /^(INPUT|TEXTAREA)$/.test(e.target.tagName)) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key.toUpperCase();
    if (Q.s.phase === 'mcq') {
      var idx = 'ABCDE'.indexOf(k);
      if (idx >= 0 && idx < (Q.mcq[Q.s.i] || { o: [] }).o.length) {
        e.preventDefault();
        if (Q.s.ans[Q.s.i] === undefined && !Q.s.look[Q.s.i]) {
          Q.s.ans[Q.s.i] = idx; save(); draw();
        }
        return;
      }
      if (k === 'S') { Q.s.look[Q.s.i] = 1; save(); draw(); e.preventDefault(); return; }
    }
    if (e.key === 'ArrowRight' || e.key === 'Enter') {
      var b = document.querySelector('[data-nav="1"],[data-tnav="1"]');
      if (b) { b.click(); e.preventDefault(); }
    }
    if (e.key === 'ArrowLeft') {
      var p = document.querySelector('[data-nav="-1"],[data-tnav="-1"]');
      if (p) { p.click(); e.preventDefault(); }
    }
    if (k === 'J' && Q.s.phase === 'mcq') { jump(); e.preventDefault(); }
  });

  ATSWA.quizStart = start;
  ATSWA.quizClear = function () { Q = null; };
  ATSWA.chapterQuestions = chapterQuestions;
})();
