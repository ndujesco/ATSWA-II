CH = {
 'n': 11,
 't': 'Functional Relationships',
 'brief': 'Functions and their graphs, linear and quadratic equations, simultaneous equations, '
          'exponential and logarithmic functions, and the business applications: break-even, '
          'market equilibrium and revenue functions.',
 'outcomes': [
   'Define a function and identify its domain and range',
   'Find the equation of a straight line from two points',
   'Solve simultaneous linear equations by substitution or elimination',
   'Solve a quadratic equation by factorisation and by formula',
   'Locate the vertex of a quadratic and interpret it as a maximum or minimum',
   'Apply linear and quadratic models to break-even and equilibrium problems',
 ],
 'secs': [
  {'n': '11.1', 't': 'Functions', 'b': [
    {'def': {'t': 'Function',
             'd': 'A rule that assigns to each element of a set (the **domain**) exactly one '
                  'element of another set (the **co-domain**). The set of values actually taken '
                  'is the **range**. Written $y = f(x)$, where $x$ is the independent variable '
                  'and $y$ the dependent variable.'}},
    {'ul': [
      '**Linear**: $y = a + bx$ — a straight line, gradient $b$, intercept $a$.',
      '**Quadratic**: $y = ax^2 + bx + c$ — a parabola, opening upwards if $a > 0$ and '
      'downwards if $a < 0$.',
      '**Polynomial** of degree $n$: highest power of $x$ is $n$.',
      '**Exponential**: $y = ab^{x}$ — the variable is in the exponent; constant '
      '*proportional* growth.',
      '**Logarithmic**: $y = \\log_b x$, the inverse of the exponential.',
    ]},
    {'note': 'The test for a function is that no value of $x$ gives two values of $y$. On a '
             'graph, any vertical line meets the curve at most once.'},
  ]},

  {'n': '11.2', 't': 'Linear functions', 'b': [
    {'fbox': {'h': 'The straight line', 'rows': [
      {'lb': 'Slope–intercept form', 'tex': 'y = a + bx'},
      {'lb': 'Gradient from two points',
       'tex': 'b = \\frac{y_2 - y_1}{x_2 - x_1}'},
      {'lb': 'Point–slope form', 'tex': 'y - y_1 = b(x - x_1)'},
      {'lb': 'Parallel lines', 'tex': 'b_1 = b_2'},
      {'lb': 'Perpendicular lines', 'tex': 'b_1 b_2 = -1'},
    ]}},
    {'eg': {'t': 'Equation of a line through two points', 'q': [
      {'p': 'Find the equation of the straight line passing through $(2, 7)$ and $(5, 16)$, and '
            'hence the value of $y$ when $x = 10$.'}],
      'a': [
      {'tex': 'b = \\frac{16 - 7}{5 - 2} = \\frac{9}{3} = 3'},
      {'p': 'Substitute $(2, 7)$ into $y = a + bx$:'},
      {'tex': '7 = a + 3(2) \\quad\\Rightarrow\\quad a = 1'},
      {'tex': 'y = 1 + 3x'},
      {'tex': 'x = 10: \\quad y = 1 + 30 = 31'}]}},

    {'eg': {'t': 'Simultaneous linear equations', 'q': [
      {'p': 'Solve: $2x + 3y = 13$ and $4x - y = 5$.'}],
      'a': [
      {'p': '**Substitution.** From the second equation, $y = 4x - 5$. Substitute into the '
            'first:'},
      {'tex': '2x + 3(4x - 5) = 13'},
      {'tex': '2x + 12x - 15 = 13 \\quad\\Rightarrow\\quad 14x = 28 \\quad\\Rightarrow\\quad '
              'x = 2'},
      {'tex': 'y = 4(2) - 5 = 3'},
      {'p': '**Check** in the first equation: $2(2) + 3(3) = 4 + 9 = 13$ ✓, and in the second: '
            '$4(2) - 3 = 5$ ✓.'},
      {'note': 'Always substitute your answer back into the equation you did **not** use to '
               'find the last variable. A slip in the algebra will show up immediately.'}]}},
  ]},

  {'n': '11.3', 't': 'Quadratic functions', 'b': [
    {'fbox': {'h': 'Solving and analysing a quadratic', 'rows': [
      {'lb': 'General form', 'tex': 'y = ax^2 + bx + c, \\quad a \\ne 0'},
      {'lb': 'Quadratic formula',
       'tex': 'x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}'},
      {'lb': 'Discriminant', 'tex': '\\Delta = b^2 - 4ac'},
      {'lb': 'Vertex (turning point)',
       'tex': 'x = -\\frac{b}{2a}'},
      {'lb': 'Sum and product of roots',
       'tex': '\\alpha + \\beta = -\\frac{b}{a}, \\qquad \\alpha\\beta = \\frac{c}{a}'},
    ]}},
    {'ul': [
      '$\\Delta > 0$ — two distinct real roots; the curve cuts the $x$-axis twice.',
      '$\\Delta = 0$ — one repeated root; the curve touches the $x$-axis.',
      '$\\Delta < 0$ — no real roots; the curve does not meet the $x$-axis.',
    ]},
    {'eg': {'t': 'Solving by formula', 'q': [
      {'p': 'Solve $2x^2 - 7x + 3 = 0$.'}],
      'a': [
      {'p': 'Here $a = 2$, $b = -7$, $c = 3$.'},
      {'tex': '\\Delta = (-7)^2 - 4(2)(3) = 49 - 24 = 25'},
      {'tex': 'x = \\frac{7 \\pm \\sqrt{25}}{2(2)} = \\frac{7 \\pm 5}{4}'},
      {'tex': 'x = \\frac{12}{4} = 3 \\qquad\\text{or}\\qquad x = \\frac{2}{4} = 0.5'},
      {'p': 'By factorisation the same result: $(2x - 1)(x - 3) = 0$. Check the sum and product '
            'of roots: $3 + 0.5 = 3.5 = -b/a = 7/2$ ✓, and $3 \\times 0.5 = 1.5 = c/a = 3/2$ ✓.'}]}},

    {'eg': {'t': 'Maximum of a profit function', 'q': [
      {'p': 'A firm\'s profit in naira thousand is given by $P = -2q^2 + 120q - 800$, where $q$ '
            'is output in units. Find the output that maximises profit, the maximum profit, and '
            'the break-even levels of output.'}],
      'a': [
      {'p': 'Since $a = -2 < 0$ the parabola opens downwards and the vertex is a **maximum**.'},
      {'tex': 'q = -\\frac{b}{2a} = -\\frac{120}{2(-2)} = \\frac{120}{4} = 30 \\text{ units}'},
      {'tex': 'P_{\\max} = -2(30)^2 + 120(30) - 800 = -1{,}800 + 3{,}600 - 800 = ₦1{,}000\\text{k}'},
      {'p': 'Break-even is where $P = 0$:'},
      {'tex': '-2q^2 + 120q - 800 = 0 \\quad\\Rightarrow\\quad q^2 - 60q + 400 = 0'},
      {'tex': 'q = \\frac{60 \\pm \\sqrt{3{,}600 - 1{,}600}}{2} = \\frac{60 \\pm \\sqrt{2{,}000}}{2} '
              '= \\frac{60 \\pm 44.72}{2}'},
      {'tex': 'q = 7.64 \\quad\\text{or}\\quad q = 52.36 \\text{ units}'},
      {'p': 'The firm is profitable for outputs between about **8 and 52 units**, with profit '
            'peaking at 30 units. Note that the maximum lies exactly halfway between the two '
            'break-even points — a property of every parabola.'}]}},
  ]},

  {'n': '11.4', 't': 'Business applications', 'b': [
    {'fbox': {'h': 'Break-even analysis', 'rows': [
      {'lb': 'Contribution per unit',
       'tex': 'c = s - v'},
      {'lb': 'Break-even point (units)',
       'tex': 'q^{*} = \\frac{F}{s - v}'},
      {'lb': 'Break-even point (sales value)',
       'tex': '\\frac{F}{\\text{C/S ratio}}, \\quad \\text{C/S} = \\frac{s-v}{s}'},
      {'lb': 'Output for a target profit',
       'tex': 'q = \\frac{F + \\pi}{s - v}'},
      {'lb': 'Margin of safety',
       'tex': '\\frac{\\text{Budgeted sales} - \\text{Break-even sales}}{\\text{Budgeted sales}}'},
    ]}},
    {'eg': {'t': 'Break-even and target profit', 'q': [
      {'p': 'A product sells for ₦250 per unit with variable cost ₦150 per unit. Fixed costs '
            'are ₦500,000 per period. Compute (a) the break-even output and sales value; '
            '(b) the output needed for a profit of ₦200,000; (c) the margin of safety if '
            'budgeted sales are 8,000 units.'}],
      'a': [
      {'tex': 'c = 250 - 150 = ₦100 \\text{ per unit}'},
      {'p': '**(a)**'},
      {'tex': 'q^{*} = \\frac{500{,}000}{100} = 5{,}000 \\text{ units}'},
      {'tex': '\\text{Break-even sales} = 5{,}000 \\times 250 = ₦1{,}250{,}000'},
      {'p': '**(b)**'},
      {'tex': 'q = \\frac{500{,}000 + 200{,}000}{100} = 7{,}000 \\text{ units}'},
      {'p': '**(c)**'},
      {'tex': '\\text{Margin of safety} = \\frac{8{,}000 - 5{,}000}{8{,}000} \\times 100 '
              '= 37.5\\%'},
      {'p': 'Sales could fall by 37.5% before the product began to make a loss. Profit at '
            'budgeted volume is $8{,}000 \\times 100 - 500{,}000 = ₦300{,}000$.'}]}},

    {'eg': {'t': 'Market equilibrium', 'q': [
      {'p': 'The demand and supply functions for a commodity are $Q_d = 100 - 2P$ and '
            '$Q_s = 20 + 3P$. Find the equilibrium price and quantity.'}],
      'a': [
      {'p': 'Equilibrium is where quantity demanded equals quantity supplied:'},
      {'tex': '100 - 2P = 20 + 3P'},
      {'tex': '80 = 5P \\quad\\Rightarrow\\quad P = 16'},
      {'tex': 'Q = 100 - 2(16) = 68 \\quad(\\text{check: } 20 + 3(16) = 68 ;\\checkmark)'},
      {'p': 'The equilibrium price is **₦16** and the equilibrium quantity **68 units**.'}]}},
  ]},

  {'n': '11.5', 't': 'Exponentials, logarithms and indices', 'b': [
    {'fbox': {'h': 'Laws of indices and logarithms', 'rows': [
      {'lb': 'Product', 'tex': 'a^m \\times a^n = a^{m+n}'},
      {'lb': 'Quotient', 'tex': 'a^m \\div a^n = a^{m-n}'},
      {'lb': 'Power', 'tex': '(a^m)^n = a^{mn}'},
      {'lb': 'Zero and negative',
       'tex': 'a^0 = 1, \\qquad a^{-n} = \\frac{1}{a^n}'},
      {'lb': 'Definition of a logarithm',
       'tex': 'y = \\log_a x \\iff a^y = x'},
      {'lb': 'Log of a product', 'tex': '\\log(xy) = \\log x + \\log y'},
      {'lb': 'Log of a quotient',
       'tex': '\\log\\!\\left(\\frac{x}{y}\\right) = \\log x - \\log y'},
      {'lb': 'Log of a power', 'tex': '\\log x^n = n \\log x'},
    ]}},
    {'eg': {'t': 'Solving an exponential equation', 'q': [
      {'p': 'A sum of ₦400,000 grows at 15% per annum compound. Using logarithms, find how many '
            'complete years it takes to exceed ₦1,000,000.'}],
      'a': [
      {'tex': '400{,}000 (1.15)^n > 1{,}000{,}000 \\quad\\Rightarrow\\quad (1.15)^n > 2.5'},
      {'p': 'Take logarithms of both sides and use $\\log x^n = n \\log x$:'},
      {'tex': 'n \\log 1.15 > \\log 2.5'},
      {'tex': 'n > \\frac{\\log 2.5}{\\log 1.15} = \\frac{0.39794}{0.06070} = 6.556'},
      {'p': 'So **7 complete years** are needed. Check: $400{,}000(1.15)^7 = ₦1{,}063{,}802$, '
            'while $400{,}000(1.15)^6 = ₦925{,}045$.'},
      {'note': 'The logarithm may be taken to any base provided the same base is used top and '
               'bottom, because the base cancels in the ratio.'}]}},
  ]},

  {'n': '11.6', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'All the terms'},
    {'ul': [
      '**Function** — a rule assigning to each input $x$ exactly one output $y$; written '
      '$y = f(x)$ ("$f$ of $x$"). $f(a)$ = the value when $x = a$.',
      '**Domain** — the set of permitted input values. **Range** — the set of resulting output '
      'values.',
      '**Independent variable $x$** (input); **dependent variable $y$** (output).',
      '**Explicit function** — $y$ alone on one side: $y = 5x + 9$. **Implicit function** — all '
      'variables mixed: $2x^2 + 3xy + 3y^2 + 10 = 0$.',
      '**Linear function** — $y = a + bx$; highest power of $x$ is 1; graph is a straight line.',
      '**Intercept $a$** — value of $y$ where $x = 0$ (crosses the $y$-axis). The **$x$-intercept** '
      'is where $y = 0$.',
      '**Gradient / slope $b$** — increase in $y$ per unit increase in $x$; one value per line; '
      'positive (rising) or negative (falling).',
      '**Quadratic function** — $y = ax^2 + bx + c$, $a \\neq 0$; graph is a parabola — '
      'U-shaped ($\\cup$) if $a > 0$, cap-shaped ($\\cap$) if $a < 0$.',
      '**Root / solution / zero** — a value of $x$ making $y = 0$ (where the graph cuts the '
      '$x$-axis).',
      '**Vertex / turning point** — the maximum ($a < 0$) or minimum ($a > 0$) point of a '
      'parabola.',
      '**Simultaneous equations** — two or more equations solved together; need at least as '
      'many independent equations as unknowns.',
      '**Exponential function** — constant base, variable exponent: $y = a^{x}$ (or $y = e^{x}$). '
      '$a > 1$ → growth; $0 < a < 1$ → decay.',
      '**Logarithmic function** — the inverse of an exponential: if $y = a^{x}$ then '
      '$x = \\log_{a} y$.',
      '**Break-even point (BEP)** — the output at which total revenue = total cost, so profit '
      '$= 0$ (no profit, no loss).',
      '**Contribution** — selling price per unit minus variable cost per unit; what each unit '
      'contributes toward fixed costs and profit.',
      '**Margin of safety** — the excess of the planned/actual output over the break-even '
      'output.',
    ]},
    {'h3': 'A. Linear functions'},
    {'fbox': {'h': 'Straight line', 'rows': [
      {'lb': 'Equation', 'tex': 'y = a + bx \\quad (\\text{or } y = mx + c)'},
      {'lb': 'Gradient from two points',
       'tex': 'b = \\dfrac{y_2 - y_1}{x_2 - x_1}'},
      {'lb': 'Point–slope form', 'tex': 'y - y_1 = b(x - x_1)'},
      {'lb': '$x$-intercept', 'tex': 'x = -\\dfrac{a}{b} \\ \\ (\\text{set } y = 0)'},
    ]}},
    {'h3': 'B. Quadratic functions and equations'},
    {'fbox': {'h': 'Solving \\(ax^2 + bx + c = 0\\)', 'rows': [
      {'lb': 'By formula',
       'tex': 'x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}'},
      {'lb': 'Discriminant',
       'tex': '\\Delta = b^2 - 4ac \\ \\ \\begin{cases} > 0 & \\text{two real roots} \\\\ '
              '= 0 & \\text{one repeated root} \\\\ < 0 & \\text{no real roots} \\end{cases}'},
      {'lb': 'By factorisation',
       'tex': '\\text{find two numbers with sum } b \\text{ and product } ac'},
      {'lb': 'Sum and product of roots',
       'tex': '\\alpha + \\beta = -\\dfrac{b}{a}, \\qquad \\alpha\\beta = \\dfrac{c}{a}'},
      {'lb': 'Axis of symmetry / vertex $x$-coordinate',
       'tex': 'x = -\\dfrac{b}{2a}'},
      {'lb': 'Reconstruct the equation from its roots',
       'tex': 'x^2 - (\\alpha + \\beta)x + \\alpha\\beta = 0'},
    ]}},
    {'h3': 'C. Business applications'},
    {'fbox': {'h': 'Cost, revenue, profit, break-even', 'rows': [
      {'lb': 'Total cost', 'tex': 'C(x) = F + vx \\quad (F = \\text{fixed cost}, \\ v = '
              '\\text{variable cost per unit})'},
      {'lb': 'Total revenue', 'tex': 'R(x) = sx \\quad (s = \\text{selling price per unit})'},
      {'lb': 'Profit', 'tex': 'P(x) = R(x) - C(x)'},
      {'lb': 'Contribution per unit', 'tex': 'c = s - v'},
      {'lb': 'Break-even output',
       'tex': 'R(x) = C(x) \\implies x^{*} = \\dfrac{F}{s - v}'},
      {'lb': 'Output for a target profit $\\pi$',
       'tex': 'x = \\dfrac{F + \\pi}{s - v}'},
      {'lb': 'Contribution / sales (C/S) ratio',
       'tex': '\\dfrac{s - v}{s}'},
      {'lb': 'Break-even revenue', 'tex': '\\dfrac{F}{\\text{C/S ratio}}'},
      {'lb': 'Margin of safety', 'tex': '\\text{actual output} - x^{*}'},
    ]}},
    {'note': 'A non-linear (quadratic) revenue or cost function gives a **quadratic** '
             'break-even equation $R(x) = C(x)$ — solve it with the quadratic formula.'},
    {'h3': 'D. Indices (laws)'},
    {'fbox': {'h': 'Laws of indices', 'rows': [
      {'lb': 'Product', 'tex': 'a^{m} \\times a^{n} = a^{m+n}'},
      {'lb': 'Quotient', 'tex': 'a^{m} \\div a^{n} = a^{m-n}'},
      {'lb': 'Power of a power', 'tex': '(a^{m})^{n} = a^{mn}'},
      {'lb': 'Zero index', 'tex': 'a^{0} = 1'},
      {'lb': 'Negative index', 'tex': 'a^{-n} = \\dfrac{1}{a^{n}}'},
      {'lb': 'Fractional index',
       'tex': 'a^{m/n} = \\sqrt[n]{a^{m}} = \\left(\\sqrt[n]{a}\\right)^{m}'},
      {'lb': 'Product/quotient of bases',
       'tex': '(ab)^{n} = a^{n}b^{n}, \\quad \\left(\\dfrac{a}{b}\\right)^{n} = '
              '\\dfrac{a^{n}}{b^{n}}'},
    ]}},
    {'h3': 'E. Logarithms (laws)'},
    {'fbox': {'h': 'Laws of logarithms', 'rows': [
      {'lb': 'Definition', 'tex': 'y = a^{x} \\iff x = \\log_{a} y'},
      {'lb': 'Product', 'tex': '\\log(MN) = \\log M + \\log N'},
      {'lb': 'Quotient', 'tex': '\\log\\!\\left(\\dfrac{M}{N}\\right) = \\log M - \\log N'},
      {'lb': 'Power', 'tex': '\\log M^{n} = n \\log M'},
      {'lb': 'Log of 1 / log of the base', 'tex': '\\log_{a} 1 = 0, \\quad \\log_{a} a = 1'},
      {'lb': 'Change of base', 'tex': '\\log_{a} M = \\dfrac{\\log_{b} M}{\\log_{b} a}'},
      {'lb': 'Solving $a^{x} = k$', 'tex': 'x = \\dfrac{\\log k}{\\log a} \\ \\ '
              '(\\text{any base, top and bottom the same})'},
      {'lb': 'Fitting $y = ax^{b}$ (log–log linear)',
       'tex': '\\log y = \\log a + b \\log x'},
    ]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Straight line', 'tex': 'y = a + bx'},
  {'lb': 'Gradient', 'tex': 'b = \\frac{y_2-y_1}{x_2-x_1}'},
  {'lb': 'Point–slope form', 'tex': 'y - y_1 = b(x - x_1)'},
  {'lb': 'Quadratic formula',
   'tex': 'x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}'},
  {'lb': 'Discriminant', 'tex': '\\Delta = b^2 - 4ac'},
  {'lb': 'Vertex / axis of symmetry', 'tex': 'x = -\\frac{b}{2a}'},
  {'lb': 'Sum / product of roots',
   'tex': '\\alpha+\\beta = -\\frac{b}{a}, \\ \\alpha\\beta = \\frac{c}{a}'},
  {'lb': 'Equation from roots',
   'tex': 'x^2 - (\\alpha+\\beta)x + \\alpha\\beta = 0'},
  {'lb': 'Total cost / revenue / profit',
   'tex': 'C = F + vx, \\ \\ R = sx, \\ \\ P = R - C'},
  {'lb': 'Contribution per unit', 'tex': 'c = s - v'},
  {'lb': 'Break-even output', 'tex': 'x^{*} = \\frac{F}{s-v}'},
  {'lb': 'Output for target profit', 'tex': 'x = \\frac{F+\\pi}{s-v}'},
  {'lb': 'Contribution/sales ratio', 'tex': '\\frac{s-v}{s}'},
  {'lb': 'Break-even revenue', 'tex': '\\frac{F}{\\text{C/S ratio}}'},
  {'lb': 'Laws of indices',
   'tex': 'a^{m}a^{n}=a^{m+n}, \\ \\frac{a^{m}}{a^{n}}=a^{m-n}, \\ (a^{m})^{n}=a^{mn}, \\ '
          'a^{0}=1, \\ a^{-n}=\\frac{1}{a^{n}}, \\ a^{m/n}=\\sqrt[n]{a^{m}}'},
  {'lb': 'Laws of logarithms',
   'tex': '\\log(MN)=\\log M+\\log N, \\ \\log\\frac{M}{N}=\\log M-\\log N, \\ '
          '\\log M^{n}=n\\log M'},
  {'lb': 'Change of base', 'tex': '\\log_{a}M = \\frac{\\log_{b}M}{\\log_{b}a}'},
  {'lb': 'Solving $a^{x}=k$', 'tex': 'x = \\frac{\\log k}{\\log a}'},
 ],
 'focus':
   'Two or three Section A marks — solving a quadratic, a gradient, a break-even output, or a '
   'law of logarithms. Section B questions usually build a small model: a cost function and a '
   'revenue function, then break-even and a profit-maximising output. The algebra is '
   'elementary; the marks are lost on setting up the model rather than on solving it.',
 'errors': [
   'Sign errors in the quadratic formula, especially with $b$ negative — $-b$ becomes $+7$ when '
   '$b = -7$.',
   'Using $s$ instead of $s - v$ in the break-even denominator.',
   'Dividing fixed cost by the selling price to get break-even sales value instead of by the '
   'C/S ratio.',
   'Treating $\\log(x + y)$ as $\\log x + \\log y$; only products split.',
   'Rounding a "complete years" answer down instead of up.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The gradient of the line joining $(1, 4)$ and $(3, 10)$ is',
    'o': ['2', '3', '6', '7', '½'],
    'a': 1,
    'w': 'Gradient is the change in $y$ divided by the change in $x$.',
    'calc': 'b = \\frac{10-4}{3-1} = \\frac{6}{2} = 3',
    'src': 'Chapter 11.2'},
   {'q': 'The roots of $x^2 - 5x + 6 = 0$ are',
    'o': ['1 and 6', '2 and 3', '−2 and −3', '5 and 6', '1 and 5'],
    'a': 1,
    'w': 'Factorise: two numbers whose sum is 5 and product is 6.',
    'calc': '(x-2)(x-3) = 0 \\Rightarrow  x = 2 \\text{ or } 3',
    'src': 'Chapter 11.3'},
   {'q': 'Fixed costs are ₦300,000, selling price ₦80 and variable cost ₦50 per unit. The '
         'break-even output is',
    'o': ['3,750 units', '10,000 units', '6,000 units', '5,000 units', '3,000 units'],
    'a': 1,
    'w': 'Contribution per unit is ₦30; divide fixed costs by contribution.',
    'calc': 'q^{*} = \\frac{300{,}000}{80-50} = \\frac{300{,}000}{30} = 10{,}000',
    'src': 'Chapter 11.4'},
   {'q': 'If $b^2 - 4ac < 0$, the quadratic equation has',
    'o': ['two distinct real roots', 'no real roots', 'one repeated root',
          'roots that sum to zero', 'infinitely many roots'],
    'a': 1,
    'w': 'A negative discriminant means the square root is imaginary, so the parabola never '
         'meets the $x$-axis.',
    'src': 'Chapter 11.3'},
   {'q': 'Given $Q_d = 60 - 4P$ and $Q_s = 10 + P$, the equilibrium price is',
    'o': ['₦8', '₦10', '₦12', '₦14', '₦20'],
    'a': 1,
    'w': 'Set demand equal to supply and solve for $P$.',
    'calc': '60 - 4P = 10 + P \\Rightarrow  50 = 5P \\Rightarrow  P = 10',
    'src': 'Chapter 11.4'},
   {'q': 'The maximum value of $y = -x^2 + 8x - 5$ occurs at $x =$',
    'o': ['−4', '4', '8', '2', '5'],
    'a': 1,
    'w': 'The turning point of a parabola is at $x = -b/2a$; with $a<0$ it is a maximum.',
    'calc': 'x = -\\frac{8}{2(-1)} = 4',
    'src': 'Chapter 11.3'},
  ],
  'theory': [
   {'q': 'A manufacturer sells a product at ₦400 per unit. Variable costs are ₦240 per unit and '
         'fixed costs ₦960,000 per period. (a) Derive the total cost, total revenue and profit '
         'functions. (b) Compute the break-even output in units and in sales value. (c) Compute '
         'the output required to earn a profit of ₦320,000. (d) If budgeted output is 9,000 '
         'units, compute the margin of safety and comment on it.',
    'marks': 12,
    'a': [
      {'h4': '(a) The functions'},
      {'p': 'Let $q$ be the number of units produced and sold.'},
      {'tex': 'TC = 960{,}000 + 240q'},
      {'tex': 'TR = 400q'},
      {'tex': '\\pi = TR - TC = 400q - (960{,}000 + 240q) = 160q - 960{,}000'},
      {'p': 'The coefficient 160 is the **contribution per unit**, $s - v = 400 - 240$. Each '
            'additional unit adds ₦160 towards covering fixed costs and then to profit.'},
      {'h4': '(b) Break-even'},
      {'p': 'Break-even is the output at which profit is zero, i.e. where $TR = TC$:'},
      {'tex': '160q - 960{,}000 = 0 \\quad\\Rightarrow\\quad q^{*} '
              '= \\frac{960{,}000}{160} = 6{,}000 \\text{ units}'},
      {'tex': '\\text{Break-even sales value} = 6{,}000 \\times 400 = ₦2{,}400{,}000'},
      {'p': 'Equivalently, using the contribution/sales ratio:'},
      {'tex': '\\text{C/S} = \\frac{160}{400} = 0.40 \\quad\\Rightarrow\\quad '
              '\\frac{960{,}000}{0.40} = ₦2{,}400{,}000'},
      {'h4': '(c) Output for a target profit'},
      {'tex': 'q = \\frac{F + \\pi}{s - v} = \\frac{960{,}000 + 320{,}000}{160} '
              '= \\frac{1{,}280{,}000}{160} = 8{,}000 \\text{ units}'},
      {'p': 'Check: $\\pi = 160(8{,}000) - 960{,}000 = 1{,}280{,}000 - 960{,}000 = ₦320{,}000$ ✓'},
      {'h4': '(d) Margin of safety'},
      {'tex': '\\text{Margin of safety} = \\frac{9{,}000 - 6{,}000}{9{,}000} \\times 100 '
              '= 33.3\\%'},
      {'p': 'In units this is 3,000; in sales value, $3{,}000 \\times 400 = ₦1{,}200{,}000$. '
            'Profit at budget is $160(9{,}000) - 960{,}000 = ₦480{,}000$.'},
      {'h4': 'Comment'},
      {'ul': [
        'Sales volume could fall by one third before the product moved into loss, which is a '
        'reasonably comfortable cushion.',
        'The C/S ratio of 40% means every ₦1 of additional sales generates 40 kobo of extra '
        'profit once break-even has been passed — and destroys 40 kobo of profit for every ₦1 '
        'lost.',
        'The high proportion of fixed costs (they are ₦960,000 against contribution of '
        '₦1,440,000 at budget) makes profit sensitive to volume. A 10% fall in sales cuts '
        'profit by ₦144,000, or 30%.',
        'The analysis assumes selling price and unit variable cost are constant across the '
        'whole range, that fixed costs do not step up, and that everything produced is sold. '
        'These assumptions weaken well outside the relevant range.',
      ]}],
    'src': 'Chapter 11.4'},
  ]},
}
