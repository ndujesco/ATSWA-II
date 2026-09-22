CH = {
 'n': 13,
 't': 'Differential and Integral Calculus',
 'brief': 'The three rules for differentiating a polynomial, maxima and minima by the second '
          'derivative, marginal functions and elasticity of demand, and integration as the '
          'reverse process — recovering totals from marginals and computing consumers\' and '
          'producers\' surpluses.',
 'outcomes': [
   'Find the first and second derivatives of functions',
   'Find the maximum and minimum points for functions',
   'Understand marginal functions',
   'Determine elasticity of demand',
   'Find the indefinite integrals of functions',
   'Evaluate the definite integrals for functions',
   'Find totals from marginals',
   'Apply all the above to economic and business problems',
 ],
 'secs': [
  {'n': '13.1', 't': 'Introduction', 'b': [
    {'p': 'This chapter discusses the principles of **differentiation** and **integration**, '
          'and the basic difference between them. Marginals of revenue, cost, profit and loss '
          'are obtained via the first derivatives of the relevant totals; conversely, revenue, '
          'cost, profit and loss are recovered from their respective marginals through '
          'integration. The use of integration to assess consumers\' and producers\' surpluses '
          'is also covered.'},
  ]},

  {'n': '13.2', 't': 'Differentiation', 'b': [
    {'p': 'The gradient (slope) of a straight line is constant — whatever two points are used, '
          'the same value results: the increase in $y$ divided by the increase in $x$. The '
          'gradient of a **curve** at a point is the gradient of the tangent to the curve at '
          'that point, and different points give different gradients, so the gradient of a '
          'curve is not constant.'},
    {'p': 'For $y = x^2$, taking a point $P(x, x^2)$ and a nearby point $Q(x+\\delta x,\\, '
          '(x+\\delta x)^2)$, the gradient of the chord $PQ$ is:'},
    {'tex': '\\frac{\\delta y}{\\delta x} = \\frac{(x+\\delta x)^2 - x^2}{\\delta x} '
            '= \\frac{2x\\,\\delta x + (\\delta x)^2}{\\delta x} = 2x + \\delta x'},
    {'p': 'In the limit as $\\delta x \\to 0$, $\\delta y/\\delta x \\to dy/dx$, so:'},
    {'tex': '\\frac{dy}{dx} = 2x'},
    {'p': 'The gradient is also called the **rate of change**. $\\dfrac{dy}{dx}$ is the '
          '**derivative** of $y$ with respect to $x$, and may also be written $y\'$ or '
          '$f\'(x)$.'},
  ]},

  {'n': '13.3', 't': 'The three rules for differentiating a polynomial in one variable', 'b': [
    {'p': 'Generally, if $y = x^n$, then $\\dfrac{dy}{dx} = nx^{n-1}$ — multiply $x$ by its '
          'original index and reduce that index by one. Let $c$ and $k$ be constants:'},
    {'ol': [
      'if $y = cx^n$, then $\\dfrac{dy}{dx} = ncx^{n-1}$;',
      'a constant on its own has zero derivative — since $c = cx^0$, $\\dfrac{dc}{dx} '
      '= 0 \\cdot cx^{-1} = 0$; and',
      'if $y = cx^n + kx^m + x^r$, then $\\dfrac{dy}{dx} = ncx^{n-1} + mkx^{m-1} + rx^{r-1}$ — '
      'the derivative of a sum of functions is the sum of the derivatives of each function.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 13.1 — first derivatives', 'open': True, 'q': [
      {'p': 'Find the derivative of each of the following functions: (a) $2x^2+5x$; '
            '(b) $4x^3-7x^2+6x-14$.'}],
      'a': [
      {'tex': '\\text{(a) } \\frac{dy}{dx} = 4x + 5'},
      {'tex': '\\text{(b) } \\frac{dy}{dx} = 12x^2 - 14x + 6'}]}},
    {'h4': 'The second derivative'},
    {'p': 'If $y = f(x)$, then $\\dfrac{dy}{dx}$ is the first derivative; differentiating '
          'again gives the **second derivative**, written $\\dfrac{d^2y}{dx^2}$ or $f\'\'(x)$.'},
    {'eg': {'tag': 'Study text', 't': 'Example 13.2 — second derivatives', 'open': True, 'q': [
      {'p': 'Find the second derivative of each of the following: (a) $16x^2-5x$; '
            '(b) $7x^3+2x^2+3x-21$; (c) $(x+4)(11x+1)(3x-2)$.'}],
      'a': [
      {'tex': '\\text{(a) } \\frac{dy}{dx}=32x-5, \\qquad \\frac{d^2y}{dx^2}=32'},
      {'tex': '\\text{(b) } \\frac{dy}{dx}=21x^2+4x+3, \\qquad \\frac{d^2y}{dx^2}=42x+4'},
      {'p': '**(c)** Expand first, then differentiate — the study text\'s own method for a '
            'product of factors is to multiply out completely rather than apply a separate '
            'product rule:'},
      {'tex': '(x+4)(11x+1)(3x-2) = (11x^2+45x+4)(3x-2) = 33x^3+113x^2-78x-8'},
      {'tex': '\\frac{dy}{dx} = 99x^2+226x-78, \\qquad \\frac{d^2y}{dx^2} = 198x+226'}]}},
  ]},

  {'n': '13.4', 't': 'Applications of differentiation', 'b': [
    {'h3': 'Maximum and minimum points'},
    {'p': 'If the graph of $y=f(x)$ is drawn, its turning points may be a maximum, a minimum, '
          'or a point of inflexion. These can be found without drawing the graph:'},
    {'steps': [
      'Find $\\dfrac{dy}{dx}$.',
      'Set $\\dfrac{dy}{dx}=0$ and solve for $x$ — this gives the turning point(s).',
      'Find $\\dfrac{d^2y}{dx^2}$.',
      'Substitute the value(s) of $x$ from step 2 into $\\dfrac{d^2y}{dx^2}$.',
      'If the result is **negative**, the point is a maximum; if **positive**, a minimum; if '
      '**zero**, it is neither — it is taken as a point of inflexion.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 13.3 — classifying turning points', 'open': True,
      'q': [
      {'p': 'Find the maximum or minimum points for: (a) $4x^2+9x-2$; (b) $12x-3x^2-7$; '
            '(c) $5x-8.5x^2-4x^3+18$.'}],
      'a': [
      {'tex': '\\text{(a) } \\frac{dy}{dx}=8x+9=0 \\Rightarrow x=-\\tfrac98; \\quad '
              '\\frac{d^2y}{dx^2}=8>0 \\Rightarrow \\text{minimum}'},
      {'tex': '\\text{(b) } \\frac{dy}{dx}=12-6x=0 \\Rightarrow x=2; \\quad '
              '\\frac{d^2y}{dx^2}=-6<0 \\Rightarrow \\text{maximum}'},
      {'p': '**(c)** $\\dfrac{dy}{dx}=5-17x-12x^2=0 \\Rightarrow 12x^2+17x-5=0$, which '
            'factorises to $(3x+5)(4x-1)=0$, so $x=-\\tfrac53$ or $x=\\tfrac14$.'},
      {'tex': '\\frac{d^2y}{dx^2} = -17-24x'},
      {'p': 'At $x=-\\tfrac53$: $d^2y/dx^2=23>0$, a **minimum**. At $x=\\tfrac14$: '
            '$d^2y/dx^2=-23<0$, a **maximum**.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 13.4 — maximum and minimum profit', 'open': True,
      'q': [
      {'p': 'The gross annual profit of DUOYEJABS Ventures is estimated as '
            '$P(x)=4x^3-10{,}800x^2+5{,}400{,}000x$, where $x$ is the number of products made '
            'and sold. Calculate (a) the number of products for maximum and/or minimum profit; '
            '(b) the maximum and/or minimum profit.'}],
      'a': [
      {'tex': '\\frac{dP(x)}{dx} = 12x^2-21{,}600x+5{,}400{,}000 = 0'},
      {'p': 'Dividing by 12 and factorising: $x^2-1{,}800x+450{,}000=0 \\Rightarrow '
            '(x-1{,}500)(x-300)=0$, so $x=1{,}500$ or $x=300$.'},
      {'tex': '\\frac{d^2P(x)}{dx^2} = 24x-21{,}600'},
      {'p': 'At $x=1{,}500$: $24(1{,}500)-21{,}600=14{,}400>0$, a **minimum**. At $x=300$: '
            '$24(300)-21{,}600=-13{,}600<0$, a **maximum**.'},
      {'tex': 'P(1{,}500) = 4(1{,}500)^3-10{,}800(1{,}500)^2+5{,}400{,}000(1{,}500) '
              '\\approx -9.18\\times10^{9}\\;(\\text{a loss})'},
      {'tex': 'P(300) = 4(300)^3-10{,}800(300)^2+5{,}400{,}000(300) = 756\\times10^{6}'},
      {'note': 'Though unusual, this shows profit can *decrease* as output rises beyond the '
               'maximising level — the maximum here is at the smaller output, 300 units.'}]}},
    {'h3': 'Marginal functions'},
    {'p': 'Let $C(x)$, $R(x)$ and $P(x)$ be the cost, revenue and profit functions, where $x$ '
          'is the number of items produced and sold. Then:'},
    {'fbox': {'h': 'Marginal functions', 'rows': [
      {'lb': 'Marginal cost', 'tex': 'C\'(x) = \\frac{dC(x)}{dx}'},
      {'lb': 'Marginal revenue', 'tex': 'R\'(x) = \\frac{dR(x)}{dx}'},
      {'lb': 'Marginal profit', 'tex': 'P\'(x) = \\frac{dP(x)}{dx}'},
    ]}},
    {'p': 'Profit is maximised or minimised where the derivative of the marginal profit '
          '$dP(x)/dx$ is less than or greater than zero respectively (the same second-derivative '
          'test as before applies to revenue and cost too). It follows that **profit is maximum '
          'when marginal revenue equals marginal cost**:'},
    {'tex': '\\frac{dR(x)}{dx} = \\frac{dC(x)}{dx}'},
    {'eg': {'tag': 'Study text', 't': 'Example 13.5 — marginal revenue and marginal profit',
      'open': True, 'q': [
      {'p': 'The demand and cost functions of COAWOS (Nig) Ltd are $p=22{,}500-3q^2$ and '
            '$C=5{,}000+14{,}400q$, where $p$ is price per item, $q$ is quantity produced and '
            'sold, and $C$ is total cost. Calculate (a) the marginal revenue; (b) the quantity '
            'and price for maximum revenue; (c) the marginal profit function and the maximum '
            'profit; (d) the price for maximum profit.'}],
      'a': [
      {'tex': '\\text{(a) } R = pq = 22{,}500q-3q^3, \\qquad \\frac{dR}{dq}=22{,}500-9q^2'},
      {'p': '**(b)** At the turning point, $dR/dq=0 \\Rightarrow 9q^2=22{,}500 \\Rightarrow '
            'q=\\pm50$; since $q$ cannot be negative, $q=50$. $d^2R/dq^2=-18q=-900<0$ at '
            '$q=50$, a maximum.'},
      {'tex': 'R_{\\max} = 22{,}500(50)-3(50)^3 = 75{,}000, \\qquad '
              'p = \\frac{75{,}000}{50} = 15{,}000'},
      {'p': '**(c)** $P = R-C = (22{,}500q-3q^3)-(5{,}000+14{,}400q) = 8{,}100q-3q^3-5{,}000$.'},
      {'tex': '\\frac{dP}{dq} = 8{,}100-9q^2 = 0 \\Rightarrow q^2=900 \\Rightarrow q=30'},
      {'p': '$d^2P/dq^2=-18(30)=-540<0$, a maximum. Maximum profit '
            '$=8{,}100(30)-3(30)^3-5{,}000=157{,}000$.'},
      {'p': '**(d)** Revenue at $q=30$ is $22{,}500(30)-3(30)^3=594{,}000$, so '
            '$p=594{,}000/30=19{,}800$. Note the price for maximum revenue (15,000) differs '
            'from the price for maximum profit (19,800) — the effect of the cost function.'}]}},
    {'h3': 'Elasticity'},
    {'p': 'The elasticity of $y=f(x)$ at a point $x$ is the ratio of the relative change in $y$ '
          'to the relative change in $x$:'},
    {'tex': '\\varepsilon_{y/x} = \\frac{dy/y}{dx/x} = \\frac{x}{y}\\cdot\\frac{dy}{dx}'},
    {'p': 'Elasticity is **dimensionless**. Elasticities are used most often to measure the '
          'responsiveness of demand (or supply) to a change in price. The **price elasticity of '
          'demand** is defined by:'},
    {'tex': '\\eta = -\\frac{p}{q}\\cdot\\frac{dq}{dp}',
     'nt': 'The minus sign makes $\\eta$ positive, since price and quantity demanded normally '
           'move in opposite directions.'},
    {'ul': [
      'A demand curve is **elastic** if $\\eta > 1$; of **unit elasticity** if $\\eta = 1$; '
      '**inelastic** if $\\eta < 1$.',
      'If $\\eta > 1$, an increase in price **decreases** revenue. If $\\eta < 1$, an increase '
      'in price **increases** revenue.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 13.6 — price elasticity of demand', 'open': True,
      'q': [
      {'p': 'The demand function for an item is $p=40-0.03\\sqrt{q}$. Investigate the effect of '
            'a price increase when (a) $q=3{,}600$; (b) $q=6{,}400$ items are demanded.'}],
      'a': [
      {'tex': '\\frac{dp}{dq} = -\\frac{0.03}{2\\sqrt{q}}'},
      {'p': '**(a)** At $q=3{,}600$: $dp/dq=-0.00025$, $p=40-0.03\\sqrt{3{,}600}=38.2$.'},
      {'tex': '\\eta = -\\frac{p}{q}\\cdot\\frac{dq}{dp} '
              '= -\\frac{38.2}{3{,}600}\\times\\frac{1}{-0.00025} = 4.24'},
      {'p': 'Since $\\eta>1$, an increase in price will **decrease** revenue when 3,600 items '
            'are demanded.'},
      {'p': '**(b)** At $q=6{,}400$: $dp/dq=-0.0001875$, $p=40-0.03\\sqrt{6{,}400}=37.6$.'},
      {'tex': '\\eta = -\\frac{37.6}{6{,}400}\\times\\frac{1}{-0.0001875} = 31.33'},
      {'p': 'Since $\\eta>1$ again, revenue will still **decrease** on a price increase when '
            '6,400 items are demanded.'}]}},
  ]},

  {'n': '13.5', 't': 'Integration', 'b': [
    {'p': 'Integration is the reverse of differentiation (anti-differentiation): given '
          '$dy/dx$, integration recovers $y$. For differentiation, an index is multiplied and '
          'then reduced by 1; reversing this means the index is **increased** by 1 and then '
          '**divided** by the new index. The integral sign is $\\int$ (an elongated S):'},
    {'tex': '\\int \\frac{dy}{dx}\\,dx = y, \\qquad \\text{e.g.} \\int 2x\\,dx = x^2'},
    {'table': {'align': 'll', 'head': ['', 'Old/new index', 'Multiply/divide'], 'rows': [
      ['Differentiation', 'decrease, old', 'multiply'],
      ['Integration', 'increase, new', 'divide'],
    ]}},
    {'p': 'This is incomplete as it stands: $x^2$, $x^2+8$, $x^2+400$ and $x^2+c$ all have the '
          'same derivative $2x$, so a **constant of integration** $c$ must be added:'},
    {'tex': '\\int 2x\\,dx = x^2 + c, \\quad \\text{where } c \\text{ can take any value}'},
  ]},

  {'n': '13.6', 't': 'Rules of integrating a polynomial in one variable', 'b': [
    {'p': 'Generally, if $y=x^n$:'},
    {'tex': '\\int x^n\\,dx = \\frac{x^{n+1}}{n+1} + c \\qquad (n \\neq -1)'},
    {'p': 'If $a$, $b$ and $k$ are constants:'},
    {'ol': [
      '$\\displaystyle\\int ax^n\\,dx = a\\int x^n\\,dx = \\frac{ax^{n+1}}{n+1}+c$ '
      '$(n\\neq-1)$;',
      '$\\displaystyle\\int (ax^n+bx^m+kx^r)\\,dx = \\frac{ax^{n+1}}{n+1}+\\frac{bx^{m+1}}{m+1}'
      '+\\frac{kx^{r+1}}{r+1}+c$ $(n,m,r\\neq-1)$; and',
      '$\\displaystyle\\int a\\,dx = \\int ax^0\\,dx = ax + c$.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 13.7 — indefinite integrals', 'open': True, 'q': [
      {'p': 'Integrate with respect to $x$: (a) $2x^3-7x^5+17$; (b) $(5x^2+6x)(4x-15)$.'}],
      'a': [
      {'tex': '\\text{(a) } \\int (2x^3-7x^5+17)\\,dx = \\frac{x^4}{2}-\\frac{7x^6}{6}+17x+c'},
      {'p': '**(b)** Expand first: $(5x^2+6x)(4x-15)=20x^3-51x^2-90x$.'},
      {'tex': '\\int (20x^3-51x^2-90x)\\,dx = 5x^4-17x^3-45x^2+c'}]}},
    {'def': {'t': 'Indefinite integral', 'd': 'an integral performed without limits, '
             '$\\int f(x)\\,dx$.'}},
    {'def': {'t': 'Definite integral', 'd': 'an integral evaluated within given limits, '
             '$\\int_a^b f(x)\\,dx$ ($b>a$) — its value is obtained by subtracting the '
             'value of the integral at the lower limit $a$ from its value at the upper limit '
             '$b$.'}},
    {'eg': {'tag': 'Study text', 't': 'Example 13.8 — evaluating definite integrals', 'open': True,
      'q': [
      {'p': 'Evaluate: (a) $\\displaystyle\\int_2^5 15x^2\\,dx$; '
            '(b) $\\displaystyle\\int_{10}^{50} (3x^2+4x+1)\\,dx$.'}],
      'a': [
      {'tex': '\\text{(a) } \\Big[5x^3\\Big]_2^5 = 5(5)^3-5(2)^3 = 625-40 = 585'},
      {'tex': '\\text{(b) } \\Big[x^3+2x^2+x\\Big]_{10}^{50} = 128{,}840'},
      {'note': 'The constant of integration $c$ cancels out in a definite integral, so it is '
               'not necessary to include it when evaluating one.'}]}},
  ]},

  {'n': '13.7', 't': 'Applications of integration', 'b': [
    {'h3': 'Totals from marginals'},
    {'p': 'Integration reverses marginal functions back into totals. Since nothing is sold '
          'when nothing is produced, $R(x)=0$ at $x=0$, so total revenue from marginal revenue '
          'is always:'},
    {'tex': '\\int \\frac{dR(x)}{dx}\\,dx = R(x)'},
    {'p': 'For cost, a fixed cost $k$ may exist even at zero output, so:'},
    {'tex': '\\int \\frac{dC(x)}{dx}\\,dx = C(x) + k'},
    {'p': 'And for profit, between two output levels $x_1$ and $x_2$:'},
    {'tex': '\\int_{x_1}^{x_2} \\frac{dP(x)}{dx}\\,dx = P(x_2) - P(x_1)'},
    {'eg': {'tag': 'Study text', 't': 'Example 13.9 — total revenue and total profit from '
      'marginals', 'open': True, 'q': [
      {'p': 'A production company\'s marginal revenue function is $3x^2-5x-50$ and its marginal '
            'cost function is $6x^2-500x+400$, where $x$ is the number of items produced and '
            'sold. Calculate (a) the number of items yielding maximum or minimum revenue; '
            '(b) the total revenue if 200 items are produced and sold; (c) the total profit for '
            'the 200 items.'}],
      'a': [
      {'p': '**(a)** $dR/dx=3x^2-5x-50=0 \\Rightarrow (3x+10)(x-5)=0 \\Rightarrow x=5$ ($x$ '
            'cannot be negative). $d^2R/dx^2=6x-5=25>0$ at $x=5$: **minimum** revenue at 5 '
            'items.'},
      {'p': '**(b)** Because nothing is produced (and so nothing sold) at $x=0$, the lower '
            'limit is zero:'},
      {'tex': 'R(200) = \\int_0^{200} (3x^2-5x-50)\\,dx = \\Big[x^3-\\tfrac52x^2-50x\\Big]_0^{200} '
              '= 7{,}890{,}000'},
      {'p': '**(c)** Marginal profit $= dR/dx - dC/dx = (3x^2-5x-50)-(6x^2-500x+400) '
            '= -3x^2+495x-450$.'},
      {'tex': 'P(200) = \\int_0^{200} (-3x^2+495x-450)\\,dx = 1{,}810{,}000'}]}},
  ]},

  {'n': '13.8', 't': 'Consumers\' and producers\' surpluses', 'b': [
    {'h3': 'Consumers\' surplus'},
    {'p': 'A demand function gives the quantity of a commodity purchased at various prices. '
          'Some consumers would be willing to pay more than the fixed market price, and gain '
          'because they pay less than that. This total consumer gain is the **consumers\' '
          'surplus**. If the price is $y_0$ and the corresponding demand is $x_0$, where '
          '$y=f(x)$ is the demand function:'},
    {'tex': '\\text{Consumers\' surplus} = \\int_0^{x_0} f(x)\\,dx - x_0y_0'},
    {'p': 'Equivalently, if $x=g(y)$ is the demand function and $y_1$ is the value of $y$ when '
          '$x=0$:'},
    {'tex': '\\text{Consumers\' surplus} = \\int_{y_0}^{y_1} g(y)\\,dy'},
    {'eg': {'tag': 'Study text', 't': 'Example 13.10 — consumers\' surplus', 'open': True, 'q': [
      {'p': 'The demand function for a commodity is $y=128+5x-2x^2$. Find the consumers\' '
            'surplus when (a) $x_0=5$; (b) $y_0=40$.'}],
      'a': [
      {'p': '**(a)** When $x_0=5$: $y_0=128+25-50=103$.'},
      {'tex': '\\text{CS} = \\int_0^5 (128+5x-2x^2)\\,dx - 5(103) '
              '= \\Big[128x+\\tfrac52x^2-\\tfrac23x^3\\Big]_0^5 - 515 = 104.17'},
      {'p': '**(b)** When $y_0=40$: $40=128+5x-2x^2 \\Rightarrow 2x^2-5x-88=0 \\Rightarrow '
            '(2x+11)(x-8)=0 \\Rightarrow x_0=8$ ($x$ cannot be negative).'},
      {'tex': '\\text{CS} = \\int_0^8 (128+5x-2x^2)\\,dx - 8(40) = 522.67'}]}},
    {'h3': 'Producers\' surplus'},
    {'p': 'A supply function gives the quantity supplied at various prices. Some producers '
          'would supply below the fixed market price, and gain because they in fact receive '
          'more. This total producer gain is the **producers\' surplus**. If the fixed price is '
          '$y_0$, the supply is $x_0$, and $f(x)$ is the supply function:'},
    {'tex': '\\text{Producers\' surplus} = x_0y_0 - \\int_0^{x_0} f(x)\\,dx'},
    {'p': 'Equivalently, with $g(y)$ the supply function and $y_1$ the value of $y$ when '
          '$x=0$:'},
    {'tex': '\\text{Producers\' surplus} = \\int_{y_1}^{y_0} g(y)\\,dy'},
    {'eg': {'tag': 'Study text', 't': 'Example 13.12 — producers\' surplus', 'open': True, 'q': [
      {'p': 'The supply function for a commodity is $y=(x+3)^2$. Find the producers\' surplus '
            'when (a) $y_0=16$; (b) $x_0=5$.'}],
      'a': [
      {'p': '**(a)** When $y_0=16$: $x_0=\\sqrt{16}-3=1$.'},
      {'tex': '\\text{PS} = 1(16) - \\int_0^1 (x+3)^2\\,dx = 3.67'},
      {'p': '**(b)** When $x_0=5$: $y_0=(5+3)^2=64$.'},
      {'tex': '\\text{PS} = 5(64) - \\int_0^5 (x+3)^2\\,dx = 149.33'}]}},
    {'h3': 'Both surpluses at market equilibrium'},
    {'p': 'If both the supply function $S(q)$ and demand function $D(q)$ for a commodity are '
          'given, equilibrium price $p_0$ and quantity $q_0$ are found where $S(q)=D(q)$, and:'},
    {'tex': '\\text{Producers\' surplus} = \\int_0^{q_0} \\big(p_0-S(q)\\big)\\,dq, \\qquad '
            '\\text{Consumers\' surplus} = \\int_0^{q_0} \\big(D(q)-p_0\\big)\\,dq'},
    {'eg': {'tag': 'Study text', 't': 'Example 13.13 — equilibrium price and both surpluses',
      'open': True, 'q': [
      {'p': 'The supply and demand functions of a commodity are $S(q)=400+15q$ and '
            '$D(q)=900-5q$. Calculate (a) the equilibrium quantity; (b) the equilibrium price; '
            '(c) the producers\' surplus; (d) the consumers\' surplus.'}],
      'a': [
      {'p': '**(a)** At equilibrium, $S(q)=D(q)$: $400+15q=900-5q \\Rightarrow 20q=500 '
            '\\Rightarrow q_0=25$.'},
      {'p': '**(b)** $p_0 = 400+15(25) = 900-5(25) = 775$.'},
      {'tex': '\\text{(c) PS} = \\int_0^{25} \\big(775-(400+15q)\\big)\\,dq '
              '= \\int_0^{25} (375-15q)\\,dq = 4{,}687.5'},
      {'tex': '\\text{(d) CS} = \\int_0^{25} \\big((900-5q)-775\\big)\\,dq '
              '= \\int_0^{25} (125-5q)\\,dq = 1{,}562.5'}]}},
  ]},

  {'n': '13.9', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§13.2 Differentiation** — $dy/dx$ is the gradient of the tangent to a curve at a '
      'point, obtained as the limit of $\\delta y/\\delta x$ as $\\delta x\\to0$; also called '
      'the rate of change.',
      '**§13.3 The three rules** — power rule (with a constant multiplier) $d(cx^n)/dx=ncx^{n-1}$; '
      'a constant differentiates to zero; the derivative of a sum is the sum of the derivatives. '
      'Products of factors are handled by **expanding first**, not a separate product rule.',
      '**§13.4 Applications** — turning points: $dy/dx=0$ then classify by $d^2y/dx^2$ '
      '(negative$=$max, positive$=$min, zero$=$inflexion). Marginal cost/revenue/profit are the '
      'derivatives of the totals; **profit is maximum when $MR=MC$**. Elasticity '
      '$\\varepsilon_{y/x}=(x/y)(dy/dx)$; price elasticity of demand '
      '$\\eta=-(p/q)(dq/dp)$ — elastic if $\\eta>1$ (price rise cuts revenue), inelastic if '
      '$\\eta<1$ (price rise raises revenue).',
      '**§13.5–13.6 Integration** — the reverse of differentiation; increase the index by 1 '
      'and divide by the new index; always add the constant $c$ for an indefinite integral '
      '(it cancels for a definite one).',
      '**§13.7 Totals from marginals** — $\\int dR(x)/dx\\,dx=R(x)$ (revenue is zero at zero '
      'output, so no extra constant); $\\int dC(x)/dx\\,dx=C(x)+k$ (a fixed cost $k$ can exist '
      'at zero output).',
      '**§13.8 Surpluses** — consumers\' surplus $=\\int_0^{x_0}f(x)dx-x_0y_0$ (area under '
      'demand, above price); producers\' surplus $=x_0y_0-\\int_0^{x_0}f(x)dx$ (area above '
      'supply, below price). At market equilibrium, $S(q)=D(q)$ gives $p_0,q_0$, and both '
      'surpluses can be found directly against that price.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Derivative** $dy/dx$ — the instantaneous rate of change / gradient of the tangent.',
      '**Second derivative** $d^2y/dx^2$ — the derivative of the derivative; classifies a '
      'turning point.',
      '**Marginal function** — the derivative of a total function (cost, revenue, profit).',
      '**Elasticity** — the ratio of the relative change in $y$ to the relative change in $x$; '
      'dimensionless.',
      '**Integration** — the reverse of differentiation (anti-differentiation).',
      '**Indefinite integral** — $\\int f(x)\\,dx$, evaluated without limits, carrying a '
      'constant $c$.',
      '**Definite integral** — $\\int_a^b f(x)\\,dx$, evaluated between limits $a$ and $b$; a '
      'number, with no constant needed.',
      '**Consumers\' surplus** — the total gain to consumers who would have paid more than the '
      'market price.',
      '**Producers\' surplus** — the total gain to producers who would have supplied below the '
      'market price.',
    ]},
  ]},

  {'n': '13.10', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'The second derivative of a function is used to determine its (A) Turning point(s) '
        '(B) Maximum point only (C) Minimum point only (D) Point of inflection only '
        '(E) Minimum or maximum point or point of inflection',
        'The demand function for a certain item is $p=10-0.04\\sqrt{q}$. Calculate the '
        'elasticity of demand when 1,600 items are demanded. (A) 8.4 (B) $-8.4$ (C) 10.5 '
        '(D) $-10.5$ (E) 16',
        'If the marginal revenue function is $x^2-5x$, what is the total revenue when $x=10$? '
        '(A) 50 (B) 833.33 (C) 83 (D) 83.33 (E) 500',
        'Given that the profit function is $2x^2-8x$, the minimum profit is (A) 8 (B) 10 '
        '(C) 12 (D) 14 (E) 16',
        'If $y=(8+5x)^3$, then $dy/dx = $ ……….',
        'The maximum cost is obtainable when the first derivative of the marginal cost function '
        'is ………..',
        'A demand is elastic if the elasticity ($\\eta$) is such that ……………',
        'Consumers\' surplus arises when consumers pay ..................................... '
        'than what they are …............................. to pay',
        'If the marginal profit function is $3x^2-2x$, then the total profit when $x=5$ is '
        '…………',
        'The equilibrium price is obtained at the point of intersection of...................... '
        'and …............ functions',
      ]}],
      'a': [
      {'ol': [
        '**E** — first derivative zero at a turning point; second derivative negative$=$'
        'maximum, positive$=$minimum, zero$=$point of inflection.',
        '**C, 10.5.**',
        '**D, 83.33** — $R(10)=\\int_0^{10}(x^2-5x)dx=\\big[x^3/3-5x^2/2\\big]_0^{10}=83.33$.',
        '**C, $-8$ (i.e. a loss)** — $dP/dx=4x-8=0 \\Rightarrow x=2$; $d^2P/dx^2=4>0$ '
        '(minimum); $P(2)=2(2)^2-8(2)=-8$.',
        '$\\dfrac{dy}{dx}=15(8+5x)^2$ — using $u=8+5x$, $y=u^3$: '
        '$dy/dx=(dy/du)(du/dx)=(3u^2)(5)$.',
        '**less than zero.**',
        '$\\eta > 1$.',
        '**less, willing** (in that order).',
        '$P(5)=\\int_0^5(3x^2-2x)dx=\\big[x^3-x^2\\big]_0^5=100$.',
        '**Demand, Supply** (or vice versa).',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Power rule (differentiation)', 'tex': '\\frac{d}{dx}(cx^n) = ncx^{n-1}'},
  {'lb': 'Second-derivative test',
   'tex': '\\frac{d^2y}{dx^2}<0 \\Rightarrow \\text{max}; \\ >0 \\Rightarrow \\text{min}; \\ '
          '=0 \\Rightarrow \\text{inflexion}'},
  {'lb': 'Marginal cost / revenue / profit',
   'tex': "C'(x)=\\frac{dC(x)}{dx}, \\ R'(x)=\\frac{dR(x)}{dx}, \\ P'(x)=\\frac{dP(x)}{dx}"},
  {'lb': 'Profit maximisation', 'tex': "R'(x) = C'(x)"},
  {'lb': 'Elasticity of $y=f(x)$', 'tex': '\\varepsilon_{y/x} = \\frac{x}{y}\\cdot\\frac{dy}{dx}'},
  {'lb': 'Price elasticity of demand', 'tex': '\\eta = -\\frac{p}{q}\\cdot\\frac{dq}{dp}'},
  {'lb': 'Power rule (integration)',
   'tex': '\\int x^n\\,dx = \\frac{x^{n+1}}{n+1}+c \\ (n\\neq-1)'},
  {'lb': 'Definite integral', 'tex': '\\int_a^b f(x)\\,dx = F(b)-F(a)'},
  {'lb': 'Total revenue from marginal revenue', 'tex': '\\int \\frac{dR(x)}{dx}\\,dx = R(x)'},
  {'lb': 'Total cost from marginal cost', 'tex': '\\int \\frac{dC(x)}{dx}\\,dx = C(x)+k'},
  {'lb': "Consumers' surplus", 'tex': "\\int_0^{x_0} f(x)\\,dx - x_0y_0"},
  {'lb': "Producers' surplus", 'tex': "x_0y_0 - \\int_0^{x_0} f(x)\\,dx"},
 ],
 'focus':
   'Two or three Section A marks on a straightforward derivative or the second-derivative test, '
   'and a Section B question in most diets combining differentiation (profit maximisation, '
   'elasticity) with integration (recovering a total, or a consumers\'/producers\' surplus). '
   'Always classify a turning point with the second derivative, and always substitute the '
   '$x$-value back to answer the question actually asked — a $q$ on its own is rarely the mark.',
 'errors': [
   'Forgetting the constant of integration in an indefinite integral.',
   'Stopping at $q$ without substituting back for the price, profit or cost actually asked for.',
   'Omitting the second-derivative test, so a maximum is never distinguished from a minimum.',
   'Applying a product rule instead of expanding a product of factors first, as the study text '
   'does.',
   'Using the wrong lower limit for total revenue — it must be zero, since nothing is sold when '
   'nothing is produced.',
   'Confusing elastic ($\\eta>1$, a price rise cuts revenue) with inelastic ($\\eta<1$, a price '
   'rise raises revenue).',
 ],
 'quiz': {
  'mcq': [
   {'q': 'If $y = 5x^3 - 2x^2 + 7$, then $\\dfrac{dy}{dx}$ is',
    'o': ['$15x^2 - 4x + 7$', '$15x^2 - 4x$', '$15x^3 - 4x^2$', '$5x^2 - 2x$', '$30x - 4$'],
    'a': 1,
    'w': 'Apply the power rule to each term; the derivative of the constant 7 is zero.',
    'calc': '\\frac{dy}{dx} = 15x^2 - 4x',
    'src': 'Chapter 13.3', 'sec': '13.3'},
   {'q': 'A stationary point of $y = f(x)$ is a maximum if, at that point,',
    'o': ['$\\frac{d^2y}{dx^2} > 0$', '$\\frac{d^2y}{dx^2} < 0$', '$\\frac{dy}{dx} > 0$',
          '$\\frac{dy}{dx} < 0$', '$\\frac{d^2y}{dx^2} = 0$'],
    'a': 1,
    'w': 'At a maximum the gradient is falling as $x$ increases, so the second derivative is '
         'negative.',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'If $C(x) = 100 + 8x + x^2$, the marginal cost at $x = 10$ is',
    'o': ['₦18', '₦28', '₦280', '₦108', '₦8'],
    'a': 1,
    'w': 'Marginal cost is the derivative of total cost.',
    'calc': "C'(x) = 8 + 2x = 8 + 2(10) = ₦28",
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': '$\\displaystyle\\int (6x^2 + 4)\\, dx$ equals',
    'o': ['$12x + c$', '$2x^3 + 4x + c$', '$6x^3 + 4x + c$', '$2x^3 + 4 + c$', '$3x^3 + 4x$'],
    'a': 1,
    'w': 'Raise each power by one and divide by the new power, then add the constant.',
    'calc': '\\int (6x^2+4)dx = \\frac{6x^3}{3} + 4x + c = 2x^3 + 4x + c',
    'src': 'Chapter 13.6', 'sec': '13.6'},
   {'q': 'Profit is maximised at the output where',
    'o': ['total revenue is maximised', 'marginal revenue equals marginal cost',
          'average cost is minimised', 'marginal cost is zero', 'total cost is minimised'],
    'a': 1,
    'w': 'Profit is $R(x)-C(x)$; setting its derivative to zero gives $R\'(x)=C\'(x)$.',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': '$\\displaystyle\\int_{1}^{3} 2x \\, dx$ equals',
    'o': ['4', '8', '9', '6', '10'],
    'a': 1,
    'w': 'Integrate to $x^2$ and evaluate between the limits.',
    'calc': '\\Big[x^2\\Big]_{1}^{3} = 9 - 1 = 8',
    'src': 'Chapter 13.6', 'sec': '13.6'},
  ],
  'theory': [
   {'q': 'A firm\'s demand function is $p=400-4q$ and its total cost function is '
         '$C(q)=1{,}000+40q+2q^2$. (a) Derive the total revenue, marginal revenue and marginal '
         'cost functions. (b) Determine the output and price at which profit is maximised, '
         'verifying it is a maximum. (c) Compute the maximum profit.',
    'marks': 12,
    'a': [
      {'h4': '(a) The functions'},
      {'tex': 'R(q) = pq = (400-4q)q = 400q-4q^2, \\qquad R\'(q)=400-8q, \\qquad '
              "C'(q)=40+4q"},
      {'h4': '(b) Profit-maximising output and price'},
      {'p': 'Set $R\'(q)=C\'(q)$:'},
      {'tex': '400-8q = 40+4q \\Rightarrow 360=12q \\Rightarrow q=30'},
      {'tex': 'p = 400-4(30) = ₦280'},
      {'tex': 'P(q) = R(q)-C(q) = -6q^2+360q-1{,}000, \\qquad \\frac{dP}{dq}=-12q+360=0 '
              '\\Rightarrow q=30'},
      {'tex': '\\frac{d^2P}{dq^2} = -12 < 0 \\ \\text{(confirms a maximum)}'},
      {'h4': '(c) Maximum profit'},
      {'tex': 'P(30) = -6(30)^2+360(30)-1{,}000 = ₦4{,}400'}],
    'src': 'Chapter 13.4', 'sec': '13.4'},
  ]},
}
