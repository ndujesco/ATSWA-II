/* -- Final Revision: every past question, grouped by course, then by
   question type, then ordered by how often-ish it's been asked. Data comes
   pre-clustered from tools/final_revision.py (data/revision.js). ---------- */
(function () {
  var A = ATSWA, V = A.VIEWS;

  function withRevision(cb) {
    A.loading('Final Revision');
    A.need('REVISION', 'revision', function (rev) {
      if (!rev) return A.h('<div class="wrap"><p style="padding:60px 0">Could not load the ' +
        'revision bank. Serve this folder over http:// rather than opening the file directly.</p></div>');
      cb(rev);
    });
  }

  function chBadge(subj, ch, sec) {
    if (!ch) return '';
    if (sec) return '<a class="ch" href="#/s/' + subj + '/' + ch + '?sec=' +
      String(sec).replace(/\./g, '-') + '">Chapter ' + ch + ' &rarr;</a>';
    return '<a class="ch" href="#/s/' + subj + '/' + ch + '">Chapter ' + ch + '</a>';
  }

  function freqBadge(freq) {
    return '<span class="mono" style="font-size:10px;letter-spacing:.08em;color:var(--ink3);' +
      'white-space:nowrap">ASKED ' + freq + '&times;</span>';
  }

  /* Every diet a cluster was asked in ('2019-03', '2020-09', ...) reduced to
     its distinct years, for the year-range sorter below. */
  function yearsOf(diets) {
    var seen = {}, out = [];
    (diets || []).forEach(function (d) {
      var y = d.slice(0, 4);
      if (!seen[y]) { seen[y] = 1; out.push(y); }
    });
    return out;
  }

  /* ---- year-range sorter, mcq/saq/essay lists ------------------------ */
  function yearFilterBar(list) {
    var all = {};
    list.forEach(function (q) { yearsOf(q.diets).forEach(function (y) { all[y] = 1; }); });
    // Most-recent-first in the dropdown list, since a recent diet is what
    // most users actually want to jump to — but the *default* selection
    // (wired in wireYearFilter) still spans the full min..max range,
    // independent of this display order.
    var years = Object.keys(all).sort().reverse();
    if (years.length < 2) return '';
    var opts = years.map(function (y) { return '<option value="' + y + '">' + y + '</option>'; }).join('');
    return '<div class="revfilter">' +
      '<span class="lbl">Diet years</span>' +
      '<select id="revYearFrom" aria-label="From year">' + opts + '</select>' +
      '<span class="to">&ndash;</span>' +
      '<select id="revYearTo" aria-label="To year">' + opts + '</select>' +
      '<span class="mono revcount" id="revCount"></span>' +
      '<button class="btn sm" id="revYearReset" type="button">Reset</button>' +
      '</div>';
  }

  function wireYearFilter() {
    var from = A.el('revYearFrom'), to = A.el('revYearTo'), reset = A.el('revYearReset');
    if (!from || !to) return;
    // Options are listed most-recent-first, but the default selection is
    // still the full min..max span regardless of that display order.
    var optYears = [].slice.call(from.options).map(function (o) { return o.value; });
    var minYear = optYears[optYears.length - 1], maxYear = optYears[0];
    from.value = minYear; to.value = maxYear;
    var items = [].slice.call(document.querySelectorAll('[data-years]'));
    var topics = [].slice.call(document.querySelectorAll('.revtopic'));
    function apply() {
      var lo = from.value, hi = to.value;
      if (lo > hi) { var t = lo; lo = hi; hi = t; }
      var shown = 0;
      items.forEach(function (el) {
        var ys = el.getAttribute('data-years').split(' ');
        var inRange = ys.some(function (y) { return y >= lo && y <= hi; });
        el.classList.toggle('hid', !inRange);
        if (inRange) shown++;
      });
      // A topic header (short-answer grouping) hides itself when every
      // question in that topic has been filtered out.
      topics.forEach(function (h) {
        var sib = h.nextElementSibling, anyShown = false;
        while (sib && !sib.classList.contains('revtopic')) {
          if (sib.hasAttribute('data-years') && !sib.classList.contains('hid')) anyShown = true;
          sib = sib.nextElementSibling;
        }
        h.classList.toggle('hid', !anyShown);
      });
      var cnt = A.el('revCount');
      if (cnt) cnt.textContent = shown + ' of ' + items.length + ' shown';
    }
    from.addEventListener('change', apply);
    to.addEventListener('change', apply);
    if (reset) reset.addEventListener('click', function () {
      from.value = minYear;
      to.value = maxYear;
      apply();
    });
    apply();
  }

  /* ---- subject picker ------------------------------------------------ */
  V.revision = function () {
    withRevision(function (rev) {
      var cards = SUBJECTS.map(function (s) {
        var d = rev[s.code];
        var total = d ? d.mcq.length + d.saq.length + d.essay.length : 0;
        return '<a class="subcard" href="#/revision/' + s.code + '" data-sub="' + s.code + '">' +
          '<div class="r1"><span class="code">' + s.code + '</span>' +
          '<span class="cnt">' + total + ' questions</span></div>' +
          '<h2>' + A.esc(s.name) + '</h2>' +
          '<div class="sub">' + A.esc(s.blurb) + '</div></a>';
      }).join('');
      A.h('<div class="wrap"><section class="shead" style="border:none">' +
        '<div class="code">Final Revision</div><h1>Every past question, ranked by how ' +
        'often it comes up</h1>' +
        '<p>All 24 diets\' MCQ, short-answer and Section B questions, grouped by subject, ' +
        'then by question type, near-duplicates across diets merged and ordered most-asked ' +
        'first. Pick a subject.</p></section>' +
        '<div class="subs">' + cards + '</div><div style="height:60px"></div></div>');
    });
  };

  /* ---- type picker ----------------------------------------------------- */
  V.revisionSub = function (code) {
    var s = A.subOf(code);
    if (!s) return V.revision();
    withRevision(function (rev) {
      var d = rev[code];
      if (!d) return V.revision();
      var kinds = [
        { key: 'mcq', label: 'Multiple choice', d: 'Every past MCQ, options and the ' +
          'examiner\'s own answer, most-repeated first.', n: d.mcq.length },
        { key: 'saq', label: 'Short answer', d: 'Fill-in-the-blank and one-line questions, ' +
          'with the official answer, grouped by topic — most-tested topics and most-' +
          'repeated questions first.', n: d.saq.length },
        { key: 'essay', label: 'Essay (Section B)', d: 'Full Section B questions with the ' +
          'official worked solution, most-repeated first.', n: d.essay.length },
      ];
      var cards = kinds.map(function (k) {
        return '<a class="subcard" href="#/revision/' + code + '/' + k.key + '">' +
          '<div class="r1"><span class="cnt">' + k.n + ' questions</span></div>' +
          '<h2>' + k.label + '</h2><div class="sub">' + k.d + '</div></a>';
      }).join('');
      A.h('<div class="wrap"><section class="shead" style="border:none">' +
        '<div class="code">Final Revision &middot; ' + code + '</div><h1>' + A.esc(s.name) + '</h1>' +
        '<div class="sbar"><a class="btn" href="#/revision">All subjects</a></div>' +
        '</section><div class="subs">' + cards + '</div><div style="height:60px"></div></div>');
    });
  };

  /* ---- full list, one question type -------------------------------- */
  V.revisionList = function (code, kind) {
    var s = A.subOf(code);
    if (!s) return V.revision();
    withRevision(function (rev) {
      var d = rev[code];
      if (!d || !d[kind]) return V.revisionSub(code);
      var list = d[kind];
      var title = kind === 'mcq' ? 'Multiple choice' :
                  kind === 'saq' ? 'Short answer' : 'Essay (Section B)';
      var body;
      if (kind === 'mcq') {
        body = list.map(function (q) {
          return '<div class="bq" data-years="' + yearsOf(q.diets).join(' ') + '">' +
            '<div class="h"><span class="n">' + q.n + '</span>' +
            freqBadge(q.freq) + chBadge(code, q.ch, q.sec) + '</div>' +
            '<div class="body">' + A.preBlock(q.pre) + A.stemHTML(q) +
            '<div style="margin-top:10px">' + q.options.map(function (o, k) {
              var on = k === q.a;
              return '<div style="display:flex;gap:10px;padding:4px 0' +
                (on ? ';color:var(--ok);font-weight:600' : '') + '">' +
                '<span class="mono" style="width:1.4em;flex:none">' + 'ABCDE'[k] + '</span>' +
                '<span style="flex:1">' + A.optText(o) + '</span>' +
                (on ? '<span class="mono" style="font-size:10px;letter-spacing:.1em">ANSWER</span>' : '') +
                '</div>';
            }).join('') + '</div></div></div>';
        }).join('');
      } else if (kind === 'saq') {
        // Topically grouped (see tools/final_revision.py): the list already
        // arrives ordered by topic, most-tested topics first, so a header
        // whenever the chapter changes is enough to render the grouping —
        // no client-side re-sorting needed.
        var lastCh = undefined, topicN = 0;
        body = list.map(function (q) {
          var head = '';
          if (q.ch !== lastCh) {
            lastCh = q.ch;
            topicN++;
            var label = q.ch ? ('Chapter ' + q.ch + ' &middot; ' +
              A.esc((d.chapters && d.chapters[q.ch]) || '')) : 'Unclassified';
            head = '<div class="revtopic"><span class="mono">' +
              (String(topicN).length < 2 ? '0' : '') + topicN + '</span>' +
              (q.ch ? '<a href="#/s/' + code + '/' + q.ch + '">' + label + '</a>' :
                '<span>' + label + '</span>') + '</div>';
          }
          return head +
            '<div class="saqrow" data-years="' + yearsOf(q.diets).join(' ') + '">' +
            '<span class="n">' + q.n + '</span><div class="b">' +
            A.preBlock(q.pre) +
            '<div style="display:flex;justify-content:space-between;gap:14px;align-items:baseline">' +
            '<div style="flex:1">' + R.inl(q.body.join(' ')) + '</div>' + freqBadge(q.freq) + '</div>' +
            (q.ans ? '<div class="ans"><div class="lbl">Official answer</div>' +
                     R.inl(q.ans.join(' ')) + '</div>' : '') +
            (q.sec ? '<div style="margin-top:8px">' +
              chBadge(code, q.ch, q.sec) + '</div>' : '') +
            '</div></div>';
        }).join('');
      } else {
        body = list.map(function (b) {
          var rid = 'rev' + code + kind + b.n;
          return '<div class="bq" data-years="' + yearsOf(b.diets).join(' ') + '">' +
            '<div class="h"><span class="n">Question ' + b.n + '</span>' +
            freqBadge(b.freq) + chBadge(code, b.ch, b.sec) + '</div>' +
            (b.q && b.q.length ? '<div class="body"><div class="pre">' +
              A.esc(b.q.join('\n')) + '</div></div>' : '') +
            '<button class="reveal" data-reveal="' + rid + '">Show the official solution</button>' +
            '<div class="sol hid" id="' + rid + '">' +
            '<div class="pre">' + A.esc(b.solution.join('\n')) + '</div>' +
            (b.examiner && b.examiner.length
              ? '<div class="exm"><div class="lbl">Examiner&rsquo;s report</div>' +
                A.esc(b.examiner.join(' ')) + '</div>' : '') +
            '</div></div>';
        }).join('');
      }
      A.h('<div class="wrap"><section class="paperhead">' +
        '<div class="code">Final Revision &middot; ' + code + '</div>' +
        '<h1 style="font-size:clamp(28px,4.4vw,42px);letter-spacing:-.032em;margin-top:8px">' +
        title + '</h1>' +
        '<p>' + list.length + (kind === 'saq' ?
          ' questions, grouped by topic — the most-tested topics first, and the most-' +
          'repeated question within each topic first.' :
          ' questions, most-asked first.') +
        ' "Asked N&times;" counts how many diets carried a near-identical version of ' +
        'that question.</p>' +
        '<div class="sbar"><a class="btn" href="#/revision/' + code + '">' + A.esc(s.name) + '</a>' +
        '<a class="btn" href="#/revision">All subjects</a>' +
        (kind === 'essay' ? '<button class="btn" data-revealall="1">Reveal every solution</button>' : '') +
        '</div>' + yearFilterBar(list) +
        '</section>' + body + '<div style="height:60px"></div></div>');
      wireYearFilter();
    });
  };
})();
