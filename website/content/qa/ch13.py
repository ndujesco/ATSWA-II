CH = {
 'n': 13,
 't': 'Differentiation and Integration',
 'brief': 'The rules of differentiation, maxima and minima, marginal cost and revenue, '
          'profit maximisation, and integration as the reverse process with its business '
          'applications.',
 'outcomes': [
   'Differentiate polynomial, product, quotient and composite functions',
   'Locate stationary points and classify them with the second derivative',
   'Derive marginal cost and marginal revenue from total functions',
   'Find the output that maximises profit or minimises average cost',
   'Integrate standard functions and evaluate a definite integral',
   'Recover a total function from a marginal function',
 ],
 'secs': [
  {'n': '13.1', 't': 'Rules of differentiation', 'b': [
    {'p': 'The derivative $\\dfrac{dy}{dx}$ measures the **instantaneous rate of change** of '
          '$y$ with respect to $x$ — geometrically, the gradient of the tangent to the curve. '
          'In economics it is the marginal quantity: the change in the total caused by a '
          'one-unit change in the variable.'},
    {'fbox': {'h': 'Standard derivatives', 'rows': [
      {'lb': 'Constant', 'tex': '\\frac{d}{dx}(c) = 0'},
      {'lb': 'Power rule', 'tex': '\\frac{d}{dx}(x^n) = n x^{\\,n-1}'},
      {'lb': 'Constant multiple',
       'tex': '\\frac{d}{dx}\\big(c\\,f(x)\\big) = c\\,f\'(x)'},
      {'lb': 'Sum rule',
       'tex': '\\frac{d}{dx}(u + v) = \\frac{du}{dx} + \\frac{dv}{dx}'},
      {'lb': 'Product rule',
       'tex': '\\frac{d}{dx}(uv) = u\\frac{dv}{dx} + v\\frac{du}{dx}'},
      {'lb': 'Quotient rule',
       'tex': '\\frac{d}{dx}\\!\\left(\\frac{u}{v}\\right) '
              '= \\frac{v\\dfrac{du}{dx} - u\\dfrac{dv}{dx}}{v^2}'},
      {'lb': 'Chain rule',
       'tex': '\\frac{dy}{dx} = \\frac{dy}{du} \\times \\frac{du}{dx}'},
      {'lb': 'Exponential', 'tex': '\\frac{d}{dx}(e^{kx}) = k e^{kx}'},
      {'lb': 'Logarithm', 'tex': '\\frac{d}{dx}(\\ln x) = \\frac{1}{x}'},
    ]}},
    {'eg': {'t': 'Applying the rules', 'q': [
      {'p': 'Differentiate (a) $y = 4x^3 - 6x^2 + 5x - 9$; (b) $y = (2x+1)(x^2-3)$; '
            '(c) $y = \\dfrac{3x+2}{x-1}$; (d) $y = (3x^2 + 1)^4$.'}],
      'a': [
      {'p': '**(a)** Power rule term by term:'},
      {'tex': '\\frac{dy}{dx} = 12x^2 - 12x + 5'},
      {'p': '**(b)** Product rule with $u = 2x+1$, $v = x^2-3$:'},
      {'tex': '\\frac{dy}{dx} = (2x+1)(2x) + (x^2-3)(2) = 4x^2 + 2x + 2x^2 - 6 = 6x^2 + 2x - 6'},
      {'p': '**(c)** Quotient rule with $u = 3x+2$, $v = x-1$:'},
      {'tex': '\\frac{dy}{dx} = \\frac{(x-1)(3) - (3x+2)(1)}{(x-1)^2} '
              '= \\frac{3x - 3 - 3x - 2}{(x-1)^2} = \\frac{-5}{(x-1)^2}'},
      {'p': '**(d)** Chain rule: differentiate the outside, then the inside.'},
      {'tex': '\\frac{dy}{dx} = 4(3x^2+1)^3 \\times 6x = 24x(3x^2+1)^3'},
      {'note': 'In (b) the answer can be checked by expanding first: '
               '$y = 2x^3 + x^2 - 6x - 3$, so $\\frac{dy}{dx} = 6x^2 + 2x - 6$ ✓. Where '
               'expansion is easy, it is a free check on the product rule.'}]}},
  ]},

  {'n': '13.2', 't': 'Maxima and minima', 'b': [
    {'steps': [
      'Differentiate to obtain $\\dfrac{dy}{dx}$.',
      'Set $\\dfrac{dy}{dx} = 0$ and solve for $x$ — these are the **stationary points**.',
      'Differentiate again to obtain $\\dfrac{d^2y}{dx^2}$.',
      'Evaluate the second derivative at each stationary point.',
      'Substitute back into the original function to find the value at the turning point.',
    ]},
    {'fbox': {'h': 'The second-derivative test', 'rows': [
      {'lb': 'Maximum', 'tex': '\\frac{d^2y}{dx^2} < 0'},
      {'lb': 'Minimum', 'tex': '\\frac{d^2y}{dx^2} > 0'},
      {'lb': 'Point of inflexion (test inconclusive)',
       'tex': '\\frac{d^2y}{dx^2} = 0'},
    ]}},
    {'key': 'The sign is easily remembered from the shape: at a **maximum** the curve is '
            'shaped like a frown — the gradient is falling, so the second derivative is '
            '**negative**. At a **minimum** it is a smile and the second derivative is '
            '**positive**.'},
  ]},

  {'n': '13.3', 't': 'Marginal analysis', 'b': [
    {'fbox': {'h': 'Marginal functions', 'rows': [
      {'lb': 'Marginal cost', 'tex': 'MC = \\frac{d(TC)}{dq}'},
      {'lb': 'Marginal revenue', 'tex': 'MR = \\frac{d(TR)}{dq}'},
      {'lb': 'Average cost', 'tex': 'AC = \\frac{TC}{q}'},
      {'lb': 'Total revenue from a demand function',
       'tex': 'TR = p \\times q'},
      {'lb': 'Profit maximisation',
       'tex': '\\frac{d\\pi}{dq} = 0 \\iff MR = MC'},
      {'lb': 'Price elasticity of demand',
       'tex': 'E_d = \\frac{dq}{dp} \\times \\frac{p}{q}'},
    ]}},
    {'eg': {'t': 'Profit maximisation', 'q': [
      {'p': 'A firm faces the demand function $p = 200 - 5q$ and has total cost '
            '$TC = 500 + 20q$, where $q$ is output in units and $p$ is price in naira. '
            'Determine the output and price that maximise profit, and compute the maximum '
            'profit.'}],
      'a': [
      {'p': 'First build total revenue from the demand function:'},
      {'tex': 'TR = pq = (200 - 5q)q = 200q - 5q^2'},
      {'p': 'Differentiate both totals to get the marginals:'},
      {'tex': 'MR = \\frac{d(TR)}{dq} = 200 - 10q \\qquad MC = \\frac{d(TC)}{dq} = 20'},
      {'p': 'Profit is maximised where $MR = MC$:'},
      {'tex': '200 - 10q = 20 \\quad\\Rightarrow\\quad 10q = 180 \\quad\\Rightarrow\\quad '
              'q = 18 \\text{ units}'},
      {'tex': 'p = 200 - 5(18) = ₦110'},
      {'p': 'Confirm with the profit function directly:'},
      {'tex': '\\pi = TR - TC = (200q - 5q^2) - (500 + 20q) = -5q^2 + 180q - 500'},
      {'tex': '\\frac{d\\pi}{dq} = -10q + 180 = 0 \\quad\\Rightarrow\\quad q = 18 '
              '\\qquad \\frac{d^2\\pi}{dq^2} = -10 < 0 \\ \\text{(maximum)}'},
      {'tex': '\\pi_{\\max} = -5(18)^2 + 180(18) - 500 = -1{,}620 + 3{,}240 - 500 = ₦1{,}120'},
      {'note': 'Notice that $MR = 200 - 10q$ has twice the slope of the demand curve '
               '$p = 200 - 5q$. For any linear demand curve $p = a - bq$, marginal revenue is '
               '$a - 2bq$ — same intercept, twice the gradient. Quoting this saves a step.'}]}},

    {'eg': {'t': 'Minimising average cost', 'q': [
      {'p': 'A firm\'s total cost function is $TC = 2{,}000 + 10q + 0.05q^2$. Find the output '
            'at which average cost is a minimum, and the minimum average cost. Verify that '
            'marginal cost equals average cost at that output.'}],
      'a': [
      {'tex': 'AC = \\frac{TC}{q} = \\frac{2{,}000}{q} + 10 + 0.05q = 2{,}000q^{-1} + 10 '
              '+ 0.05q'},
      {'tex': '\\frac{d(AC)}{dq} = -2{,}000q^{-2} + 0.05 = 0'},
      {'tex': '\\frac{2{,}000}{q^2} = 0.05 \\quad\\Rightarrow\\quad q^2 = 40{,}000 '
              '\\quad\\Rightarrow\\quad q = 200 \\text{ units}'},
      {'p': 'Second derivative, to confirm a minimum:'},
      {'tex': '\\frac{d^2(AC)}{dq^2} = 4{,}000q^{-3} = \\frac{4{,}000}{200^3} > 0 '
              '\\ \\text{(minimum)}'},
      {'tex': 'AC_{\\min} = \\frac{2{,}000}{200} + 10 + 0.05(200) = 10 + 10 + 10 = ₦30'},
      {'p': 'Marginal cost at that output:'},
      {'tex': 'MC = \\frac{d(TC)}{dq} = 10 + 0.1q = 10 + 0.1(200) = ₦30'},
      {'key': 'Marginal cost equals average cost at the minimum of average cost, and this is '
              'always true. While $MC < AC$ each extra unit is cheaper than the running '
              'average and pulls it down; while $MC > AC$ it pushes the average up. The '
              'average therefore turns exactly where the two are equal — the same reason a '
              'batting average rises only while the latest score exceeds it.'}]}},
  ]},

  {'n': '13.4', 't': 'Integration', 'b': [
    {'p': 'Integration reverses differentiation. Where differentiation takes a total function '
          'to a marginal one, integration recovers the total from the marginal — with a '
          'constant that has to be identified from additional information, usually fixed cost.'},
    {'fbox': {'h': 'Standard integrals', 'rows': [
      {'lb': 'Power rule',
       'tex': '\\int x^n \\, dx = \\frac{x^{\\,n+1}}{n+1} + c, \\quad n \\ne -1'},
      {'lb': 'Constant', 'tex': '\\int k \\, dx = kx + c'},
      {'lb': 'Reciprocal',
       'tex': '\\int \\frac{1}{x} \\, dx = \\ln x + c'},
      {'lb': 'Exponential',
       'tex': '\\int e^{kx} \\, dx = \\frac{1}{k}e^{kx} + c'},
      {'lb': 'Definite integral',
       'tex': '\\int_{a}^{b} f(x)\\, dx = \\Big[F(x)\\Big]_{a}^{b} = F(b) - F(a)'},
    ]}},
    {'warn': 'The constant of integration $c$ must be written in every **indefinite** integral. '
             'In a business application it is not decoration: it is the fixed cost, the initial '
             'stock or the opening balance, and the question always supplies enough information '
             'to evaluate it.'},
    {'eg': {'t': 'Definite integral', 'q': [
      {'p': 'Evaluate $\\displaystyle\\int_{0}^{4} (2x + 3)\\, dx$.'}],
      'a': [
      {'tex': '\\int_{0}^{4} (2x+3)\\,dx = \\Big[x^2 + 3x\\Big]_{0}^{4}'},
      {'tex': '= \\big(4^2 + 3(4)\\big) - \\big(0 + 0\\big) = 16 + 12 = 28'},
      {'note': 'No constant is needed in a definite integral: it appears in both $F(b)$ and '
               '$F(a)$ and cancels in the subtraction.'}]}},
    {'eg': {'t': 'Recovering total cost from marginal cost', 'q': [
      {'p': 'The marginal cost function of a firm is $MC = 3q^2 - 4q + 10$ and fixed costs are '
            '₦100. Determine the total cost function and the total cost of producing 5 units.'}],
      'a': [
      {'tex': 'TC = \\int MC \\, dq = \\int (3q^2 - 4q + 10)\\, dq '
              '= q^3 - 2q^2 + 10q + c'},
      {'p': 'Fixed cost is the cost when output is zero, so $TC = 100$ at $q = 0$:'},
      {'tex': '100 = 0 - 0 + 0 + c \\quad\\Rightarrow\\quad c = 100'},
      {'tex': 'TC = q^3 - 2q^2 + 10q + 100'},
      {'tex': 'TC(5) = 125 - 50 + 50 + 100 = ₦225'}]}},
    {'eg': {'t': 'Consumer surplus', 'q': [
      {'p': 'The demand function for a product is $p = 100 - 2q$. If the market price is ₦60, '
            'compute the consumer surplus.'}],
      'a': [
      {'p': 'At $p = 60$: $60 = 100 - 2q$, so $q = 20$ units.'},
      {'p': 'Consumer surplus is the area under the demand curve above the price line — what '
            'consumers would have been willing to pay, less what they actually paid:'},
      {'tex': 'CS = \\int_{0}^{20} (100 - 2q)\\, dq - (60 \\times 20)'},
      {'tex': '= \\Big[100q - q^2\\Big]_{0}^{20} - 1{,}200 = (2{,}000 - 400) - 1{,}200'},
      {'tex': '= 1{,}600 - 1{,}200 = ₦400'},
      {'note': 'With a linear demand curve the surplus is a triangle, so the answer can be '
               'checked without calculus: $\\frac{1}{2} \\times 20 \\times (100 - 60) '
               '= \\frac{1}{2}(20)(40) = ₦400$ ✓'}]}},
  ]},

  {'n': '13.5', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§13.1 Rules of differentiation** — $dy/dx$ = instantaneous rate of change / gradient '
      'of the tangent = the *marginal* quantity in economics. Power rule '
      '$d(x^n)/dx=nx^{n-1}$; constant multiple, sum, product ($u\\,dv/dx+v\\,du/dx$), quotient '
      '($(v\\,du/dx-u\\,dv/dx)/v^2$) and chain ($dy/du\\times du/dx$) rules; '
      '$d(e^{kx})/dx=ke^{kx}$, $d(\\ln x)/dx=1/x$. Check a product-rule answer by expanding '
      'first where the expansion is easy.',
      '**§13.2 Maxima and minima** — differentiate, set $dy/dx=0$ to find stationary points, '
      'differentiate again; second derivative **negative** = maximum (frown shape), '
      '**positive** = minimum (smile shape), **zero** = inconclusive (possible inflexion). '
      'Always substitute the $x$ back into the *original* function to get the turning-point '
      'value.',
      '**§13.3 Marginal analysis** — $MC=d(TC)/dq$, $MR=d(TR)/dq$, $AC=TC/q$, '
      '$TR=p\\times q$; profit is maximised where $d\\pi/dq=0\\iff MR=MC$ (confirm with a '
      'negative second derivative); for any linear demand $p=a-bq$, $MR=a-2bq$ — same '
      'intercept, **twice** the gradient. **$MC=AC$ exactly at the minimum of AC** — while '
      '$MC<AC$ the average is still falling, while $MC>AC$ it is rising. Elasticity of demand '
      '$E_d=(dq/dp)\\times(p/q)$.',
      '**§13.4 Integration** — reverses differentiation; power rule '
      '$\\int x^n\\,dx=x^{n+1}/(n+1)+c$ ($n\\ne-1$), constant $\\int k\\,dx=kx+c$, reciprocal '
      '$\\int(1/x)dx=\\ln x+c$, exponential $\\int e^{kx}dx=(1/k)e^{kx}+c$; definite integral '
      '$\\int_a^b f(x)dx=F(b)-F(a)$ needs **no** constant (it cancels in the subtraction), but '
      'every **indefinite** integral must carry $c$ — in a business context $c$ is real data '
      '(fixed cost, opening stock/balance) recovered from information the question supplies.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Derivative $\\dfrac{dy}{dx}$ (or $f\'(x)$)** — the instantaneous rate of change of $y$ '
      'with respect to $x$; the gradient of the curve at a point.',
      '**Differentiation** — the process of finding the derivative.',
      '**Second derivative $\\dfrac{d^2y}{dx^2}$ (or $f\'\'(x)$)** — the derivative of the '
      'derivative; measures how the gradient is changing.',
      '**Turning (stationary) point** — where $\\dfrac{dy}{dx} = 0$: a **maximum**, a '
      '**minimum**, or a **point of inflexion**.',
      '**Marginal function** — the derivative of a total function: marginal cost, marginal '
      'revenue, marginal profit.',
      '**Elasticity** — the ratio of the proportionate change in one variable to the '
      'proportionate change in another.',
      '**Integration (anti-differentiation)** — the reverse of differentiation.',
      '**Indefinite integral** $\\int f(x)\\,dx$ — a family of functions differing by the '
      '**constant of integration $c$**.',
      '**Definite integral** $\\int_a^b f(x)\\,dx$ — a number; the (signed) area under the '
      'curve between $x = a$ and $x = b$.',
      '**Consumer surplus / producer surplus** — areas between the demand (or supply) curve '
      'and the market price.',
    ]},
    {'h3': 'A. Rules of differentiation'},
    {'fbox': {'h': 'Differentiation', 'rows': [
      {'lb': 'Constant', 'tex': '\\dfrac{d}{dx}(k) = 0'},
      {'lb': 'Power rule', 'tex': '\\dfrac{d}{dx}(x^{n}) = n x^{n-1}'},
      {'lb': 'Constant multiple', 'tex': '\\dfrac{d}{dx}(k\\,u) = k\\,\\dfrac{du}{dx}'},
      {'lb': 'Sum / difference',
       'tex': '\\dfrac{d}{dx}(u \\pm v) = \\dfrac{du}{dx} \\pm \\dfrac{dv}{dx}'},
      {'lb': 'Product rule', 'tex': '(uv)\' = u\'v + uv\''},
      {'lb': 'Quotient rule',
       'tex': '\\left(\\dfrac{u}{v}\\right)\' = \\dfrac{u\'v - uv\'}{v^{2}}'},
      {'lb': 'Chain rule',
       'tex': '\\dfrac{dy}{dx} = \\dfrac{dy}{du}\\cdot\\dfrac{du}{dx}'},
      {'lb': 'Exponential / log',
       'tex': '\\dfrac{d}{dx}(e^{x}) = e^{x}, \\qquad \\dfrac{d}{dx}(\\ln x) = \\dfrac{1}{x}'},
    ]}},
    {'h3': 'B. Maxima and minima'},
    {'fbox': {'h': 'Second-derivative test', 'rows': [
      {'lb': 'Step 1 — stationary points', 'tex': '\\dfrac{dy}{dx} = 0 \\ \\Rightarrow \\ x'},
      {'lb': 'Step 2 — classify',
       'tex': '\\dfrac{d^2y}{dx^2} < 0 \\Rightarrow \\text{maximum}; \\quad '
              '\\dfrac{d^2y}{dx^2} > 0 \\Rightarrow \\text{minimum}; \\quad '
              '= 0 \\Rightarrow \\text{test further (possible inflexion)}'},
    ]}},
    {'h3': 'C. Marginal analysis'},
    {'fbox': {'h': 'Marginals and optimisation', 'rows': [
      {'lb': 'Marginal cost', 'tex': 'MC = \\dfrac{d(TC)}{dq}'},
      {'lb': 'Marginal revenue', 'tex': 'MR = \\dfrac{d(TR)}{dq}'},
      {'lb': 'Marginal profit', 'tex': 'MP = \\dfrac{d(TP)}{dq} = MR - MC'},
      {'lb': 'Profit maximised when', 'tex': 'MR = MC \\ \\ (\\text{equivalently } MP = 0)'},
      {'lb': 'MR from a linear demand $p = a - bq$',
       'tex': 'TR = pq = aq - bq^{2}, \\quad MR = a - 2bq'},
      {'lb': 'Average cost', 'tex': 'AC = \\dfrac{TC}{q}'},
    ]}},
    {'h3': 'D. Elasticity'},
    {'fbox': {'h': 'Elasticity', 'rows': [
      {'lb': 'Point elasticity of $y = f(x)$',
       'tex': '\\varepsilon = \\dfrac{x}{y}\\cdot\\dfrac{dy}{dx}'},
      {'lb': 'Price elasticity of demand',
       'tex': '\\eta = -\\dfrac{p}{q}\\cdot\\dfrac{dq}{dp} '
              '= -\\dfrac{p}{q} \\div \\dfrac{dp}{dq}'},
      {'lb': 'Interpretation',
       'tex': '\\eta > 1 \\text{ elastic}, \\quad \\eta = 1 \\text{ unit elastic}, \\quad '
              '\\eta < 1 \\text{ inelastic}'},
    ]}},
    {'h3': 'E. Integration'},
    {'fbox': {'h': 'Integration', 'rows': [
      {'lb': 'Power rule',
       'tex': '\\int x^{n}\\,dx = \\dfrac{x^{n+1}}{n+1} + c \\quad (n \\neq -1)'},
      {'lb': 'Constant multiple / sum',
       'tex': '\\int (a\\,u \\pm b\\,v)\\,dx = a\\!\\int u\\,dx \\pm b\\!\\int v\\,dx'},
      {'lb': 'Constant', 'tex': '\\int a\\,dx = ax + c'},
      {'lb': 'Special cases',
       'tex': '\\int x^{-1}\\,dx = \\ln x + c, \\qquad \\int e^{x}\\,dx = e^{x} + c'},
      {'lb': 'Definite integral (Fundamental Theorem)',
       'tex': '\\int_a^b f(x)\\,dx = \\Big[F(x)\\Big]_a^b = F(b) - F(a)',
       'nt': 'The constant $c$ cancels, so it is omitted for a definite integral.'},
      {'lb': 'Total from a marginal',
       'tex': 'TC = \\int MC\\,dq + \\text{(fixed cost)}, \\qquad TR = \\int MR\\,dq'},
      {'lb': 'Consumer surplus',
       'tex': 'CS = \\int_0^{q_0} p_d(q)\\,dq - p_0 q_0'},
      {'lb': 'Producer surplus',
       'tex': 'PS = p_0 q_0 - \\int_0^{q_0} p_s(q)\\,dq'},
    ]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Power rule (differentiation)',
   'tex': '\\frac{d}{dx}(x^n) = nx^{n-1}'},
  {'lb': 'Product rule', 'tex': '(uv)\' = uv\' + vu\''},
  {'lb': 'Quotient rule',
   'tex': '\\left(\\frac{u}{v}\\right)\' = \\frac{vu\' - uv\'}{v^2}'},
  {'lb': 'Chain rule',
   'tex': '\\frac{dy}{dx} = \\frac{dy}{du}\\cdot\\frac{du}{dx}'},
  {'lb': 'Maximum / minimum test',
   'tex': '\\frac{dy}{dx}=0; \\ \\frac{d^2y}{dx^2}<0 \\text{ max}, \\ >0 \\text{ min}'},
  {'lb': 'Marginal cost', 'tex': 'MC = \\frac{d(TC)}{dq}'},
  {'lb': 'Marginal revenue', 'tex': 'MR = \\frac{d(TR)}{dq}'},
  {'lb': 'Marginal profit', 'tex': 'MP = \\frac{d(TP)}{dq} = MR - MC'},
  {'lb': 'Profit maximisation', 'tex': 'MR = MC \\ \\ (MP = 0)'},
  {'lb': 'MR from linear demand $p=a-bq$', 'tex': 'MR = a - 2bq'},
  {'lb': 'Point elasticity', 'tex': '\\varepsilon = \\frac{x}{y}\\cdot\\frac{dy}{dx}'},
  {'lb': 'Price elasticity of demand',
   'tex': '\\eta = -\\frac{p}{q}\\cdot\\frac{dq}{dp}'},
  {'lb': 'Power rule (integration)',
   'tex': '\\int x^n dx = \\frac{x^{n+1}}{n+1} + c \\ (n \\neq -1)'},
  {'lb': 'Integral of $x^{-1}$ and $e^x$',
   'tex': '\\int x^{-1}dx = \\ln x + c, \\ \\int e^x dx = e^x + c'},
  {'lb': 'Definite integral',
   'tex': '\\int_a^b f(x)dx = [F(x)]_a^b = F(b) - F(a)'},
  {'lb': 'Total from marginal',
   'tex': 'TC = \\int MC\\,dq + F, \\quad TR = \\int MR\\,dq'},
  {'lb': 'Consumer surplus',
   'tex': 'CS = \\int_0^{q_0} p_d(q)\\,dq - p_0 q_0'},
  {'lb': 'Producer surplus',
   'tex': 'PS = p_0 q_0 - \\int_0^{q_0} p_s(q)\\,dq'},
 ],
 'focus':
   'Two or three Section A marks on a straightforward derivative or the second-derivative test, '
   'and a Section B question in most diets on profit maximisation or minimum average cost. The '
   'examiner\'s report repeatedly notes that candidates differentiate correctly but never '
   'classify the stationary point or never substitute back to find the profit — both are '
   'explicit marks.',
 'errors': [
   'Forgetting the constant of integration in an indefinite integral.',
   'Stopping at $q$ without substituting back to find the price, profit or cost asked for.',
   'Omitting the second-derivative test, so a maximum is never distinguished from a minimum.',
   'Treating the demand function $p = a - bq$ as the revenue function; revenue is $pq$.',
   'Sign errors in the quotient rule — the numerator is $vu\' - uv\'$, in that order.',
   'Differentiating $2{,}000/q$ as if it were a constant; write it as $2{,}000q^{-1}$ first.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'If $y = 5x^3 - 2x^2 + 7$, then $\\dfrac{dy}{dx}$ is',
    'o': ['$15x^2 - 4x + 7$', '$15x^2 - 4x$', '$15x^3 - 4x^2$', '$5x^2 - 2x$', '$30x - 4$'],
    'a': 1,
    'w': 'Apply the power rule to each term; the derivative of the constant 7 is zero.',
    'calc': '\\frac{dy}{dx} = 15x^2 - 4x',
    'src': 'Chapter 13.1', 'sec': '13.1'},
   {'q': 'A stationary point of $y = f(x)$ is a maximum if, at that point,',
    'o': ['$\\frac{d^2y}{dx^2} > 0$', '$\\frac{d^2y}{dx^2} < 0$', '$\\frac{dy}{dx} > 0$',
          '$\\frac{dy}{dx} < 0$', '$\\frac{d^2y}{dx^2} = 0$'],
    'a': 1,
    'w': 'At a maximum the gradient is decreasing as $x$ increases, so the second derivative '
         'is negative.',
    'src': 'Chapter 13.2', 'sec': '13.2'},
   {'q': 'If $TC = 100 + 8q + q^2$, the marginal cost at $q = 10$ is',
    'o': ['₦18', '₦28', '₦280', '₦108', '₦8'],
    'a': 1,
    'w': 'Marginal cost is the derivative of total cost.',
    'calc': 'MC = 8 + 2q = 8 + 2(10) = ₦28',
    'src': 'Chapter 13.3', 'sec': '13.3'},
   {'q': '$\\displaystyle\\int (6x^2 + 4)\\, dx$ equals',
    'o': ['$12x + c$', '$2x^3 + 4x + c$', '$6x^3 + 4x + c$', '$2x^3 + 4 + c$', '$3x^3 + 4x$'],
    'a': 1,
    'w': 'Raise each power by one and divide by the new power, then add the constant.',
    'calc': '\\int (6x^2+4)dx = \\frac{6x^3}{3} + 4x + c = 2x^3 + 4x + c',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'Profit is maximised at the output where',
    'o': ['total revenue is maximised', 'marginal revenue equals marginal cost',
          'average cost is minimised', 'marginal cost is zero', 'total cost is minimised'],
    'a': 1,
    'w': 'Profit is $TR - TC$; setting its derivative to zero gives $MR - MC = 0$.',
    'src': 'Chapter 13.3', 'sec': '13.3'},
   {'q': '$\\displaystyle\\int_{1}^{3} 2x \\, dx$ equals',
    'o': ['4', '8', '9', '6', '10'],
    'a': 1,
    'w': 'Integrate to $x^2$ and evaluate between the limits.',
    'calc': '\\Big[x^2\\Big]_{1}^{3} = 9 - 1 = 8',
    'src': 'Chapter 13.4', 'sec': '13.4'},
  ],
  'theory': [
   {'q': 'A company\'s demand function is $p = 400 - 4q$ and its total cost function is '
         '$TC = 1{,}000 + 40q + 2q^2$, where $q$ is output in units and all money figures are '
         'in naira. (a) Derive the total revenue, marginal revenue and marginal cost functions. '
         '(b) Determine the output and price at which profit is maximised, verifying that it is '
         'a maximum. (c) Compute the maximum profit. (d) Determine the output at which total '
         'revenue is maximised, and explain why it differs from the profit-maximising output.',
    'marks': 15,
    'a': [
      {'h4': '(a) The functions'},
      {'tex': 'TR = pq = (400 - 4q)q = 400q - 4q^2'},
      {'tex': 'MR = \\frac{d(TR)}{dq} = 400 - 8q'},
      {'tex': 'MC = \\frac{d(TC)}{dq} = 40 + 4q'},
      {'h4': '(b) Profit-maximising output and price'},
      {'p': 'Set $MR = MC$:'},
      {'tex': '400 - 8q = 40 + 4q'},
      {'tex': '360 = 12q \\quad\\Rightarrow\\quad q = 30 \\text{ units}'},
      {'tex': 'p = 400 - 4(30) = ₦280'},
      {'p': 'Verification by the profit function:'},
      {'tex': '\\pi = TR - TC = (400q - 4q^2) - (1{,}000 + 40q + 2q^2) = -6q^2 + 360q - 1{,}000'},
      {'tex': '\\frac{d\\pi}{dq} = -12q + 360 = 0 \\quad\\Rightarrow\\quad q = 30'},
      {'tex': '\\frac{d^2\\pi}{dq^2} = -12 < 0'},
      {'p': 'The second derivative is negative, so $q = 30$ is a **maximum**, not a minimum.'},
      {'h4': '(c) Maximum profit'},
      {'tex': '\\pi_{\\max} = -6(30)^2 + 360(30) - 1{,}000 = -5{,}400 + 10{,}800 - 1{,}000 '
              '= ₦4{,}400'},
      {'p': 'Cross-check from the components: $TR = 400(30) - 4(900) = 12{,}000 - 3{,}600 '
            '= ₦8{,}400$ and $TC = 1{,}000 + 1{,}200 + 1{,}800 = ₦4{,}000$, giving a profit of '
            '₦4,400 ✓'},
      {'h4': '(d) Revenue-maximising output'},
      {'p': 'Total revenue is maximised where marginal revenue is zero:'},
      {'tex': 'MR = 400 - 8q = 0 \\quad\\Rightarrow\\quad q = 50 \\text{ units}'},
      {'tex': '\\frac{d^2(TR)}{dq^2} = -8 < 0 \\ \\text{(a maximum)}'},
      {'tex': 'TR_{\\max} = 400(50) - 4(50)^2 = 20{,}000 - 10{,}000 = ₦10{,}000'},
      {'h4': 'Why the two differ'},
      {'p': 'Revenue is maximised at 50 units but profit at only 30 units, because revenue '
            'maximisation ignores cost entirely. Between 30 and 50 units each additional unit '
            'still adds to revenue ($MR > 0$) but adds **more** to cost ($MC > MR$), so profit '
            'falls even while revenue rises.'},
      {'p': 'The figures make this concrete. At $q = 50$:'},
      {'tex': 'TC = 1{,}000 + 40(50) + 2(50)^2 = 1{,}000 + 2{,}000 + 5{,}000 = ₦8{,}000'},
      {'tex': '\\pi = 10{,}000 - 8{,}000 = ₦2{,}000'},
      {'p': 'Revenue is ₦1,600 higher than at the profit-maximising output, but profit is '
            '₦2,400 lower. Chasing turnover has cost the firm more than half its profit — the '
            'practical reason a sales-volume target is a poor substitute for a profit target.'},
      {'note': 'Note $MR = 400 - 8q$ against demand $p = 400 - 4q$: same intercept, twice the '
               'gradient. This holds for every linear demand curve and is a quick check that '
               'the revenue function was differentiated correctly.'}],
    'src': 'Chapter 13.3', 'sec': '13.3'},
  ]},
}
