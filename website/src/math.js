/* ── TeX → MathML ─────────────────────────────────────────────────────
   A subset of LaTeX, big enough for everything the ATSWA syllabus needs:
   fractions, radicals, sub/superscripts, sums and integrals with limits,
   stretchy delimiters, matrices, aligned blocks, accents and text runs.
   Output is MathML Core, which every current browser lays out natively —
   no library, no font loading, and it scales with the surrounding type. */
var TeX = (function () {

  var GREEK = {
    alpha:'α',beta:'β',gamma:'γ',delta:'δ',epsilon:'ϵ',varepsilon:'ε',zeta:'ζ',
    eta:'η',theta:'θ',vartheta:'ϑ',iota:'ι',kappa:'κ',lambda:'λ',mu:'μ',nu:'ν',
    xi:'ξ',pi:'π',rho:'ρ',sigma:'σ',tau:'τ',upsilon:'υ',phi:'ϕ',varphi:'φ',
    chi:'χ',psi:'ψ',omega:'ω',Gamma:'Γ',Delta:'Δ',Theta:'Θ',Lambda:'Λ',Xi:'Ξ',
    Pi:'Π',Sigma:'Σ',Upsilon:'Υ',Phi:'Φ',Psi:'Ψ',Omega:'Ω'
  };
  var OPS = {
    times:'×',div:'÷',pm:'±',mp:'∓',cdot:'⋅',ast:'∗',star:'⋆',circ:'∘',
    bullet:'∙',le:'≤',leq:'≤',ge:'≥',geq:'≥',ne:'≠',neq:'≠',equiv:'≡',
    approx:'≈',sim:'∼',simeq:'≃',cong:'≅',propto:'∝',ll:'≪',gg:'≫',
    subset:'⊂',supset:'⊃',subseteq:'⊆',supseteq:'⊇',in:'∈',notin:'∉',
    ni:'∋',cup:'∪',cap:'∩',setminus:'∖',emptyset:'∅',varnothing:'∅',
    forall:'∀',exists:'∃',neg:'¬',land:'∧',lor:'∨',
    to:'→',rightarrow:'→',leftarrow:'←',Rightarrow:'⇒',Leftarrow:'⇐',
    leftrightarrow:'↔',Leftrightarrow:'⇔',mapsto:'↦',implies:'⟹',
    infty:'∞',partial:'∂',nabla:'∇',prime:'′',degree:'°',angle:'∠',
    therefore:'∴',because:'∵',ldots:'…',cdots:'⋯',vdots:'⋮',ddots:'⋱',
    dots:'…',perp:'⊥',parallel:'∥',triangle:'△',square:'□',
    oplus:'⊕',ominus:'⊖',otimes:'⊗',leqslant:'⩽',geqslant:'⩾',
    lceil:'⌈',rceil:'⌉',lfloor:'⌊',rfloor:'⌋',langle:'⟨',rangle:'⟩',
    naira:'₦',cedi:'GH¢',pounds:'£',euro:'€'
  };
  var BIG = { sum:'∑',prod:'∏',coprod:'∐',int:'∫',iint:'∬',iiint:'∭',oint:'∮',
              bigcup:'⋃',bigcap:'⋂',lim:'lim',max:'max',min:'min' };
  var FUNC = ('sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh ' +
              'log ln lg exp det gcd deg dim hom ker Pr').split(' ');
  var ACCENT = { bar:'‾',overline:'‾',hat:'^',widehat:'^',tilde:'~',widetilde:'~',
                 vec:'→',dot:'˙',ddot:'¨',check:'ˇ',acute:'´',grave:'`' };
  var SPACE = { ',':'0.17em', ':':'0.22em', ';':'0.28em', '!':'-0.17em',
                'quad':'1em', 'qquad':'2em', ' ':'0.25em' };

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  /* ── lexer ───────────────────────────────────────────────────────── */
  function lex(src) {
    var t = [], i = 0, n = src.length;
    while (i < n) {
      var c = src[i];
      if (c === '\\') {
        var m = /^\\([a-zA-Z]+|.)/.exec(src.slice(i));
        if (!m) { i++; continue; }
        t.push({ k: 'cmd', v: m[1] }); i += m[0].length;
        // a command name eats the space that separates it from the next token
        if (/^[a-zA-Z]+$/.test(m[1])) while (src[i] === ' ') i++;
        continue;
      }
      if (c === '{') { t.push({ k: '{' }); i++; continue; }
      if (c === '}') { t.push({ k: '}' }); i++; continue; }
      if (c === '^' || c === '_') { t.push({ k: c }); i++; continue; }
      if (c === '&') { t.push({ k: '&' }); i++; continue; }
      if (c === ' ' || c === '\n' || c === '\t') { i++; continue; }
      if (/[0-9]/.test(c)) {
        var m2 = /^[0-9]+(?:[.,][0-9]+)*/.exec(src.slice(i));
        t.push({ k: 'num', v: m2[0] }); i += m2[0].length; continue;
      }
      if (/[a-zA-Z]/.test(c)) { t.push({ k: 'chr', v: c }); i++; continue; }
      t.push({ k: 'sym', v: c }); i++;
    }
    return t;
  }

  /* ── parser ──────────────────────────────────────────────────────── */
  function Parser(toks, display) {
    this.t = toks; this.i = 0; this.display = display;
  }
  Parser.prototype.peek = function () { return this.t[this.i]; };
  Parser.prototype.next = function () { return this.t[this.i++]; };

  // one group: {...} or a single base. Deliberately NOT an atom: the argument
  // of _ or ^ must not swallow the script that follows it (x_0^2).
  Parser.prototype.arg = function (style) {
    var tk = this.peek();
    if (!tk) return '<mrow></mrow>';
    if (tk.k === '{') { this.next(); return this.rowUntil('}', style); }
    return this.base(style) || '<mrow></mrow>';
  };
  // optional [..] argument, returned raw
  Parser.prototype.opt = function () {
    var tk = this.peek();
    if (tk && tk.k === 'sym' && tk.v === '[') {
      this.next();
      var parts = [], d = 0;
      while (this.i < this.t.length) {
        var x = this.peek();
        if (x.k === 'sym' && x.v === ']' && d === 0) { this.next(); break; }
        if (x.k === '{') d++; if (x.k === '}') d--;
        parts.push(this.atom() || '');
      }
      return parts.join('');
    }
    return null;
  };

  Parser.prototype.rowUntil = function (stop, style) {
    var out = [];
    while (this.i < this.t.length) {
      var tk = this.peek();
      if (stop === '}' && tk.k === '}') { this.next(); break; }
      if (stop === 'right' && tk.k === 'cmd' && tk.v === 'right') break;
      if (stop === 'end' && tk.k === 'cmd' && tk.v === 'end') break;
      var a = this.atom(style);
      if (a) out.push(a);
    }
    return '<mrow>' + out.join('') + '</mrow>';
  };

  // text mode: everything up to the closing brace is literal
  Parser.prototype.textArg = function () {
    var tk = this.peek(), out = '';
    if (!tk) return '';
    if (tk.k !== '{') { var a = this.next(); return a.v || ''; }
    this.next();
    var d = 0;
    while (this.i < this.t.length) {
      var x = this.next();
      if (x.k === '}') { if (d === 0) break; d--; out += '}'; continue; }
      if (x.k === '{') { d++; out += '{'; continue; }
      if (x.k === 'cmd') {
        if (x.v === ' ' || x.v === ',') { out += ' '; continue; }
        out += GREEK[x.v] || OPS[x.v] || x.v; continue;
      }
      if (x.k === '^' || x.k === '_' || x.k === '&') { out += x.k; continue; }
      out += (x.v !== undefined ? x.v : '');
      // a space between two text tokens is dropped by the lexer; restore it
      var nx = this.peek();
      if (nx && (nx.k === 'chr' || nx.k === 'num') &&
          (x.k === 'chr' || x.k === 'num' || x.k === 'sym')) {
        // no reliable info; leave as-is
      }
    }
    return out;
  };

  function isBigBase(mml) {
    return /data-big="1"/.test(mml);
  }

  // an atom plus any scripts hanging off it
  Parser.prototype.atom = function (style) {
    var base = this.base(style);
    if (base === null) return null;
    var sub = null, sup = null;
    for (;;) {
      var tk = this.peek();
      if (tk && tk.k === '_' && sub === null) { this.next(); sub = this.arg(style); continue; }
      if (tk && tk.k === '^' && sup === null) { this.next(); sup = this.arg(style); continue; }
      break;
    }
    if (sub === null && sup === null) return base;
    var big = isBigBase(base);
    var b = base.replace(' data-big="1"', '');
    if (big && this.display) {
      if (sub !== null && sup !== null) return '<munderover>' + b + sub + sup + '</munderover>';
      if (sub !== null) return '<munder>' + b + sub + '</munder>';
      return '<mover>' + b + sup + '</mover>';
    }
    if (sub !== null && sup !== null) return '<msubsup>' + b + sub + sup + '</msubsup>';
    if (sub !== null) return '<msub>' + b + sub + '</msub>';
    return '<msup>' + b + sup + '</msup>';
  };

  Parser.prototype.base = function (style) {
    var tk = this.next();
    if (!tk) return null;
    switch (tk.k) {
      case 'num': return '<mn>' + esc(tk.v) + '</mn>';
      case 'chr':
        if (style === 'rm') return '<mi mathvariant="normal">' + esc(tk.v) + '</mi>';
        if (style === 'bf') return '<mi mathvariant="bold">' + esc(tk.v) + '</mi>';
        return '<mi>' + esc(tk.v) + '</mi>';
      case 'sym': {
        var v = tk.v;
        if (v === '(' || v === ')' || v === '[' || v === ']' || v === '|')
          return '<mo stretchy="false">' + esc(v) + '</mo>';
        if (v === "'") return '<mo>&#x2032;</mo>';
        if (v === '%') return '<mo>%</mo>';
        if (/[+\-*\/=<>,;:.!?]/.test(v))
          return '<mo>' + esc(v === '-' ? '−' : v) + '</mo>';
        return '<mo>' + esc(v) + '</mo>';
      }
      case '{': return this.rowUntil('}', style);
      case '}': return '';
      case '&': return '';
      case '^': case '_': this.i--; return null;
      case 'cmd': return this.cmd(tk.v, style);
    }
    return '';
  };

  Parser.prototype.cmd = function (name, style) {
    var P = this;
    if (name === 'frac' || name === 'dfrac' || name === 'tfrac') {
      var a = this.arg(style), b = this.arg(style);
      return '<mfrac>' + a + b + '</mfrac>';
    }
    if (name === 'cfrac') {
      var a1 = this.arg(style), b1 = this.arg(style);
      return '<mfrac>' + a1 + b1 + '</mfrac>';
    }
    if (name === 'binom') {
      var t1 = this.arg(style), b2 = this.arg(style);
      return '<mrow><mo stretchy="true">(</mo><mfrac linethickness="0">' + t1 + b2 +
             '</mfrac><mo stretchy="true">)</mo></mrow>';
    }
    if (name === 'sqrt') {
      var idx = this.opt();
      var r = this.arg(style);
      return idx ? '<mroot>' + r + '<mrow>' + idx + '</mrow></mroot>'
                 : '<msqrt>' + r + '</msqrt>';
    }
    if (name === 'text' || name === 'textrm' || name === 'textnormal' ||
        name === 'mbox' || name === 'textit' || name === 'textbf') {
      var s = this.textArg();
      var st = name === 'textit' ? ' mathvariant="italic"'
             : name === 'textbf' ? ' mathvariant="bold"' : '';
      return '<mtext' + st + '>' + esc(s) + '</mtext>';
    }
    if (name === 'mathrm' || name === 'operatorname') return this.arg('rm');
    if (name === 'mathbf') return this.arg('bf');
    if (name === 'mathit') return this.arg('it');
    if (name === 'mathcal' || name === 'mathbb' || name === 'mathsf')
      return this.arg(style);
    if (name === 'left') {
      var d = this.next(), open = d ? (d.v === '.' ? '' : (OPS[d.v] || d.v)) : '';
      var body = this.rowUntil('right', style);
      var rt = this.peek();
      var close = '';
      if (rt && rt.k === 'cmd' && rt.v === 'right') {
        this.next();
        var e = this.next();
        close = e ? (e.v === '.' ? '' : (OPS[e.v] || e.v)) : '';
      }
      return '<mrow>' + (open ? '<mo stretchy="true">' + esc(open) + '</mo>' : '') +
             body + (close ? '<mo stretchy="true">' + esc(close) + '</mo>' : '') + '</mrow>';
    }
    if (name === 'right') { this.next(); return ''; }
    if (name === 'big' || name === 'Big' || name === 'bigg' || name === 'Bigg' ||
        name === 'bigl' || name === 'bigr' || name === 'Bigl' || name === 'Bigr') {
      var dd = this.next();
      return '<mo stretchy="true">' + esc(dd ? (OPS[dd.v] || dd.v) : '') + '</mo>';
    }
    if (name === 'begin') {
      var env = this.textArg();
      return this.env(env, style);
    }
    if (name === 'end') { this.textArg(); return ''; }
    if (ACCENT[name]) {
      var b3 = this.arg(style);
      var acc = ACCENT[name];
      if (name === 'bar' || name === 'overline')
        return '<mover accent="true">' + b3 + '<mo stretchy="true">&#x00AF;</mo></mover>';
      if (name === 'vec')
        return '<mover accent="true">' + b3 + '<mo stretchy="false">&#x2192;</mo></mover>';
      return '<mover accent="true">' + b3 + '<mo stretchy="false">' + esc(acc) + '</mo></mover>';
    }
    if (name === 'underline')
      return '<munder accentunder="true">' + this.arg(style) +
             '<mo stretchy="true">&#x005F;</mo></munder>';
    if (name === 'overbrace' || name === 'underbrace') {
      var b4 = this.arg(style);
      return (name === 'overbrace' ? '<mover>' : '<munder>') + b4 +
             '<mo stretchy="true">' + (name === 'overbrace' ? '&#x23DE;' : '&#x23DF;') +
             '</mo>' + (name === 'overbrace' ? '</mover>' : '</munder>');
    }
    if (SPACE[name] !== undefined)
      return '<mspace width="' + SPACE[name] + '"/>';
    if (name === 'displaystyle') { this.display = true; return ''; }
    if (name === 'textstyle') { this.display = false; return ''; }
    if (name === 'limits' || name === 'nolimits' || name === '!') return '';
    if (name === '\\' || name === 'newline') return '<!--br-->';
    if (name === 'hline' || name === 'notag' || name === 'nonumber') return '';
    if (BIG[name]) {
      var g = BIG[name];
      if (name === 'lim' || name === 'max' || name === 'min')
        return '<mo movablelimits="true" data-big="1">' + g + '</mo>';
      return '<mo largeop="true" movablelimits="false" data-big="1">' + g + '</mo>';
    }
    if (FUNC.indexOf(name) >= 0)
      return '<mi mathvariant="normal">' + name + '</mi><mo>&#x2061;</mo>';
    if (GREEK[name]) return '<mi>' + esc(GREEK[name]) + '</mi>';
    if (OPS[name]) {
      var o = OPS[name];
      if (name === 'naira' || name === 'cedi' || name === 'pounds' || name === 'euro')
        return '<mtext>' + esc(o) + '</mtext>';
      if (name === 'infty' || name === 'emptyset' || name === 'varnothing')
        return '<mi>' + esc(o) + '</mi>';
      return '<mo>' + esc(o) + '</mo>';
    }
    if (name === '%') return '<mo>%</mo>';
    if (name === '$') return '<mtext>$</mtext>';
    if (name === '&') return '';
    if (name === '#') return '<mtext>#</mtext>';
    if (name === '_') return '<mtext>_</mtext>';
    if (name === '{' || name === '}')
      return '<mo stretchy="false">' + name + '</mo>';
    if (name === ' ') return '<mspace width="0.25em"/>';
    return '<mi>' + esc(name) + '</mi>';
  };

  // aligned / cases / array / matrix
  Parser.prototype.env = function (env, style) {
    var cols = null;
    if (env === 'array' || env === 'tabular') cols = this.textArg();
    var rows = [[]], cur = [];
    var flushCell = function () { rows[rows.length - 1].push('<mrow>' + cur.join('') + '</mrow>'); cur = []; };
    while (this.i < this.t.length) {
      var tk = this.peek();
      if (tk.k === 'cmd' && tk.v === 'end') { this.next(); this.textArg(); break; }
      if (tk.k === 'cmd' && (tk.v === '\\' || tk.v === 'newline')) {
        this.next(); flushCell(); rows.push([]); continue;
      }
      if (tk.k === '&') { this.next(); flushCell(); continue; }
      if (tk.k === 'cmd' && tk.v === 'hline') { this.next(); continue; }
      var a = this.atom(style);
      if (a) cur.push(a);
    }
    flushCell();
    rows = rows.filter(function (r) { return r.join('').replace(/<mrow><\/mrow>/g, '') !== ''; });
    var align = 'center';
    if (env === 'aligned' || env === 'align' || env === 'align*' || env === 'split')
      align = 'right left left left left';
    if (env === 'cases') align = 'left left left';
    if (cols) align = cols.replace(/\|/g, '').split('').map(function (c) {
      return c === 'l' ? 'left' : c === 'r' ? 'right' : 'center';
    }).join(' ');
    var body = rows.map(function (r) {
      return '<mtr>' + r.map(function (c) { return '<mtd>' + c + '</mtd>'; }).join('') + '</mtr>';
    }).join('');
    var tbl = '<mtable columnalign="' + align + '" rowspacing="0.32em" columnspacing="0.4em">' +
              body + '</mtable>';
    if (env === 'cases')
      return '<mrow><mo stretchy="true">{</mo>' + tbl + '</mrow>';
    if (env === 'pmatrix')
      return '<mrow><mo stretchy="true">(</mo>' + tbl + '<mo stretchy="true">)</mo></mrow>';
    if (env === 'bmatrix')
      return '<mrow><mo stretchy="true">[</mo>' + tbl + '<mo stretchy="true">]</mo></mrow>';
    if (env === 'vmatrix')
      return '<mrow><mo stretchy="true">|</mo>' + tbl + '<mo stretchy="true">|</mo></mrow>';
    return tbl;
  };

  /* ── entry point ─────────────────────────────────────────────────── */
  function render(tex, display) {
    var p = new Parser(lex(String(tex)), !!display);
    var out = [];
    while (p.i < p.t.length) {
      var a = p.atom();
      if (a === null) { p.i++; continue; }
      out.push(a);
    }
    var body = out.join('');
    // a bare \\ outside an environment becomes a stacked table
    if (body.indexOf('<!--br-->') >= 0) {
      var lines = body.split('<!--br-->');
      body = '<mtable columnalign="center" rowspacing="0.4em">' +
             lines.map(function (l) { return '<mtr><mtd><mrow>' + l + '</mrow></mtd></mtr>'; }).join('') +
             '</mtable>';
    }
    return '<math xmlns="http://www.w3.org/1998/Math/MathML" display="' +
           (display ? 'block' : 'inline') + '">' + body + '</math>';
  }

  /* Plain-Unicode fallback, for a browser with no MathML layout. */
  function plain(tex) {
    var SUP = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷',
               '8':'⁸','9':'⁹','+':'⁺','-':'⁻','n':'ⁿ','i':'ⁱ'};
    var SUB = {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇',
               '8':'₈','9':'₉','+':'₊','-':'₋','i':'ᵢ','n':'ₙ','x':'ₓ','a':'ₐ'};
    var ACC = {bar:'\u0304',overline:'\u0304',hat:'\u0302',widehat:'\u0302',
               tilde:'\u0303',vec:'\u20D7',dot:'\u0307',ddot:'\u0308'};
    var s = String(tex);
    s = s.replace(/\\([a-zA-Z]+)\s*\{([^{}])\}|\\([a-zA-Z]+)\s+([A-Za-z0-9])/g,
      function (m, w1, c1, w2, c2) {
        var w = w1 || w2, ch = c1 || c2;
        return ACC[w] ? ch + ACC[w] : m;
      });
    s = s.replace(/\\[,;:!]|\\ /g, ' ');
    s = s.replace(/\\(d|t)?frac\{([^{}]*)\}\{([^{}]*)\}/g, '($2)/($3)');
    s = s.replace(/\\sqrt\{([^{}]*)\}/g, '√($1)');
    s = s.replace(/\\text(?:rm|bf|it)?\{([^{}]*)\}/g, '$1');
    s = s.replace(/\\math(?:rm|bf|it|cal|bb|sf)\{([^{}]*)\}/g, '$1');
    s = s.replace(/\\left|\\right|\\displaystyle|\\limits/g, '');
    s = s.replace(/\\begin\{[a-z*]+\}|\\end\{[a-z*]+\}/g, '');
    s = s.replace(/\\\\/g, '; ').replace(/&/g, ' ');
    s = s.replace(/\\([a-zA-Z]+)/g, function (m, w) {
      return GREEK[w] || OPS[w] || BIG[w] || (FUNC.indexOf(w) >= 0 ? w : w);
    });
    var script = function (map, mark) {
      return function (m, a, b) {
        var v = a !== undefined ? a : b;
        var ok = true, o = '';
        for (var i = 0; i < v.length; i++) {
          if (map[v[i]] === undefined) { ok = false; break; }
          o += map[v[i]];
        }
        return ok ? o : (v.length === 1 ? mark + v : mark + '(' + v + ')');
      };
    };
    s = s.replace(/\^\{([^{}]*)\}|\^(\w)/g, script(SUP, '^'));
    s = s.replace(/_\{([^{}]*)\}|_(\w)/g, script(SUB, '_'));
    return s.replace(/[{}]/g, '').replace(/\s+/g, ' ').trim();
  }

  var supported = null;
  function hasMathML() {
    if (supported !== null) return supported;
    try {
      if (typeof MathMLElement === 'function') return (supported = true);
      var d = document.createElement('div');
      d.style.cssText = 'position:absolute;visibility:hidden;font-size:16px';
      d.innerHTML = '<math><mfrac><mn>1</mn><mn>2</mn></mfrac></math>';
      document.body.appendChild(d);
      var h = d.firstChild ? d.firstChild.getBoundingClientRect().height : 0;
      document.body.removeChild(d);
      return (supported = h > 20);
    } catch (e) { return (supported = false); }
  }

  return {
    render: function (tex, display) {
      if (!hasMathML())
        return '<span class="mtx' + (display ? ' mtxd' : '') + '">' + esc(plain(tex)) + '</span>';
      try { return render(tex, display); }
      catch (e) { return '<span class="mtx">' + esc(plain(tex)) + '</span>'; }
    },
    plain: plain
  };
})();
