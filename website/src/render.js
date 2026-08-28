/* -- content renderer -------------------------------------------------
   Turns the authored block schema into HTML. Inline markup inside any
   string: $tex$ for maths, **bold**, *italic*, `mono`, ~aside~, and
   [label](#/route) for a link. */
var R = (function () {

  function esc(s) {
    return String(s === undefined || s === null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  /* inline: maths is lifted out first so markup inside it is left alone */
  var MARK = String.fromCharCode(1);
  function inl(s) {
    if (s === undefined || s === null) return '';
    s = String(s);
    var math = [];
    s = s.replace(/\$\$([\s\S]+?)\$\$/g, function (m, t) {
      math.push(TeX.render(t, true)); return MARK + (math.length - 1) + MARK;
    });
    s = s.replace(/\$([^$]+?)\$/g, function (m, t) {
      math.push(TeX.render(t, false)); return MARK + (math.length - 1) + MARK;
    });
    s = esc(s);
    s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, function (m, a, b) {
      return '<a href="' + esc(b) + '">' + a + '</a>';
    });
    s = s.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
    s = s.replace(/(^|[\s(—-])\*([^*\n]+)\*/g, '$1<i>$2</i>');
    s = s.replace(/`([^`]+)`/g, '<code class="mono">$1</code>');
    s = s.replace(/~([^~\n]+)~/g, '<span style="color:var(--ink3)">$1</span>');
    s = s.replace(new RegExp(MARK + '(\\d+)' + MARK, 'g'), function (m, i) {
      return math[+i];
    });
    return s;
  }

  function money(v) {
    if (v === undefined || v === null || v === '') return '';
    if (typeof v === 'number') {
      var neg = v < 0, a = Math.abs(v);
      var t = (Math.round(a * 100) / 100).toLocaleString('en-US',
        { minimumFractionDigits: (a % 1 ? 2 : 0), maximumFractionDigits: 2 });
      return neg ? '(' + t + ')' : t;
    }
    return inl(v);
  }

  var B = {};

  B.p  = function (b) { return '<p>' + inl(b.p) + '</p>'; };
  B.h3 = function (b) { return '<h3' + (b.id ? ' id="' + esc(b.id) + '"' : '') + '>' + inl(b.h3) + '</h3>'; };
  B.h4 = function (b) { return '<h4>' + inl(b.h4) + '</h4>'; };
  B.ul = function (b) {
    return '<ul>' + b.ul.map(function (x) { return '<li>' + inl(x) + '</li>'; }).join('') + '</ul>';
  };
  B.ol = function (b) {
    return '<ol>' + b.ol.map(function (x) { return '<li>' + inl(x) + '</li>'; }).join('') + '</ol>';
  };
  B.steps = function (b) {
    return '<ol class="steps">' + b.steps.map(function (x) {
      return '<li>' + inl(x) + '</li>'; }).join('') + '</ol>';
  };
  B.tex = function (b) {
    var eq = '<div class="eq">' + TeX.render(b.tex, true) + '</div>';
    return b.tag ? '<div class="eqn">' + eq + '<span class="tag">' + esc(b.tag) + '</span></div>' : eq;
  };
  B.def = function (b) {
    return '<div class="dfn"><b>' + inl(b.def.t) + '</b> &mdash; ' + inl(b.def.d) + '</div>';
  };
  function callout(kind, label, body) {
    return '<div class="callout ' + kind + '"><span class="lbl">' + esc(label) +
           '</span><div class="cbody">' +
           (Array.isArray(body) ? blocks(body) : '<p>' + inl(body) + '</p>') +
           '</div></div>';
  }
  B.note = function (b) { return callout('note', b.lbl || 'Note', b.note); };
  B.key  = function (b) { return callout('key',  b.lbl || 'Key idea', b.key); };
  B.warn = function (b) { return callout('warn', b.lbl || 'Careful', b.warn); };
  B.pre  = function (b) { return '<div class="pre">' + esc(b.pre) + '</div>'; };

  B.table = function (b) {
    var t = b.table, al = (t.align || '').split('');
    var cls = function (i) { return al[i] === 'r' ? ' class="r"' : ''; };
    var h = '';
    if (t.head) h = '<thead><tr>' + t.head.map(function (c, i) {
      return '<th' + cls(i) + '>' + inl(c) + '</th>'; }).join('') + '</tr></thead>';
    var rows = t.rows.map(function (row) {
      var r = row.slice(), rc = '';
      if (r.length && typeof r[r.length - 1] === 'string' && /^@\w+$/.test(r[r.length - 1])) {
        rc = ' class="' + r.pop().slice(1) + '"';
      }
      return '<tr' + rc + '>' + r.map(function (c, i) {
        return '<td' + cls(i) + '>' + inl(c) + '</td>'; }).join('') + '</tr>';
    }).join('');
    return '<div class="tbl"><table>' +
           (t.cap ? '<caption>' + inl(t.cap) + '</caption>' : '') + h +
           '<tbody>' + rows + '</tbody></table>' +
           (t.note ? '<div class="tnote">' + inl(t.note) + '</div>' : '') + '</div>';
  };

  var egn = 0;
  B.eg = function (b) {
    var e = b.eg, id = 'eg' + (++egn);
    return '<div class="eg"><div class="h"><span class="tag">' +
      esc(e.tag || 'Worked example') + '</span><span class="t">' + inl(e.t || '') + '</span></div>' +
      '<div class="qz">' + blocks(e.q) + '</div>' +
      (e.open === true
        ? '<div class="az">' + blocks(e.a) + '</div>'
        : '<button class="reveal" data-reveal="' + id + '">Show the solution</button>' +
          '<div class="az hid" id="' + id + '">' + blocks(e.a) + '</div>') +
      '</div>';
  };

  B.tacc = function (b) {
    var t = b.tacc;
    var side = function (label, lines) {
      return '<div class="side"><div class="sh">' + esc(label) + '</div>' +
        lines.map(function (l) {
          var c = l[2] === '@tot' ? ' tot' : '';
          return '<div class="ln' + c + '"><span>' + inl(l[0]) + '</span><b>' +
                 money(l[1]) + '</b></div>';
        }).join('') + '</div>';
    };
    return '<div class="tacc"><div class="h">' + inl(t.t) + '</div><div class="g">' +
      side(t.drl || 'Dr', t.dr || []) + side(t.crl || 'Cr', t.cr || []) + '</div></div>';
  };

  B.stmt = function (b) {
    var s = b.stmt;
    var rows = s.rows.map(function (row) {
      if (row === '@gap') return '<tr class="gap"><td colspan="9"></td></tr>';
      if (typeof row === 'string') return '<tr class="hd"><td colspan="9">' + inl(row) + '</td></tr>';
      var r = row.slice(), cls = '';
      if (typeof r[r.length - 1] === 'string' && /^@\w+$/.test(r[r.length - 1]))
        cls = ' class="' + r.pop().slice(1) + '"';
      var cells = '<td>' + inl(r[0]) + '</td>';
      for (var i = 1; i < r.length; i++) cells += '<td class="v">' + money(r[i]) + '</td>';
      return '<tr' + cls + '>' + cells + '</tr>';
    }).join('');
    return '<div class="stmt">' +
      (s.t ? '<div class="h"><div class="t">' + inl(s.t) + '</div>' +
             (s.sub ? '<div class="s">' + inl(s.sub) + '</div>' : '') + '</div>' : '') +
      '<table><tbody>' + rows + '</tbody></table></div>';
  };

  B.fbox = function (b) {
    var f = b.fbox;
    return '<div class="fbox"><h4>' + esc(f.h || 'Formulas') + '</h4>' +
      f.rows.map(function (r) {
        return '<div class="row">' + (r.lb ? '<div class="lb">' + inl(r.lb) + '</div>' : '') +
          '<div class="eq">' + TeX.render(r.tex, true) + '</div>' +
          (r.nt ? '<div class="nt">' + inl(r.nt) + '</div>' : '') + '</div>';
      }).join('') + '</div>';
  };

  function block(b) {
    if (b === null || b === undefined) return '';
    if (typeof b === 'string') return '<p>' + inl(b) + '</p>';
    for (var k in B) if (Object.prototype.hasOwnProperty.call(b, k)) return B[k](b);
    return '';
  }

  function blocks(list) {
    if (!list) return '';
    if (!Array.isArray(list)) list = [list];
    return list.map(block).join('');
  }

  /* every string in a tree, for search indexing and previews */
  function text(list) {
    var out = [];
    (function walk(x) {
      if (x === null || x === undefined) return;
      if (typeof x === 'string') { out.push(x); return; }
      if (Array.isArray(x)) { x.forEach(walk); return; }
      if (typeof x === 'object') for (var k in x) walk(x[k]);
    })(list);
    return out.join(' ')
      .replace(/\$\$?([^$]*)\$?\$/g, ' $1 ')
      .replace(/[*`~\\{}]/g, ' ')
      .replace(/\s+/g, ' ').trim();
  }

  return { blocks: blocks, block: block, inl: inl, esc: esc, text: text, money: money };
})();
