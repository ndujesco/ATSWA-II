CH = {
 'n': 11,
 't': 'Functional Relationships',
 'brief': 'What a function is and its types (linear, quadratic, exponential, logarithmic); '
          'solving linear, simultaneous and quadratic equations; business applications (cost, '
          'revenue, profit, break-even, demand/supply and market equilibrium); and simple linear '
          'inequalities.',
 'outcomes': [
   'Understand the concept of functions',
   'Identify different types of functions',
   'Understand equations',
   'Solve different types of equations by algebraic and graphical methods',
   'Understand the concept of linear inequalities and their solutions',
   'Apply all the concepts above to business and economic problems',
 ],
 'secs': [
  {'n': '11.1', 't': 'Introduction — definition of a function', 'b': [
    {'def': {'t': 'Function', 'd': 'a mathematical way of describing a relationship between two '
                  'or more variables — a mathematical expression involving one or more '
                  'variables. Functions connect fragments of business information together.'}},
    {'p': 'A function of $x$ is written $f(x)$, read "$f$ of $x$" — e.g. $f(x) = 4x + 3$. '
          '$y$ is often used to represent $f(x)$, in which case $y$ is said to be a function '
          'of $x$.'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.1 — evaluating a function', 'open': True,
      'q': [
      {'p': '(a) If $f(x) = 4x + 3$, find (i) $f(0)$, (ii) $f(1)$, (iii) $f(14)$.'},
      {'p': '(b) If $f(x) = 2x^2 + 5x + 7$, find (i) $f(0)$, (ii) $f(2)$, (iii) $f(15)$.'}],
      'a': [
      {'tex': '\\text{(a)}\\quad f(0)=3,\\quad f(1)=7,\\quad f(14)=4(14)+3=59'},
      {'tex': '\\text{(b)}\\quad f(0)=7,\\quad f(2)=2(2)^2+5(2)+7=25,\\quad '
              'f(15)=2(15)^2+5(15)+7=532'}]}},
  ]},

  {'n': '11.2', 't': 'Types of functions', 'b': [
    {'p': 'A function can be **explicit** (one variable directly expressed in terms of the '
          'other(s), e.g. $y=5x+9$, $y=3x^2+8$) or **implicit** (the relationship is one '
          'equation involving all the variables, e.g. $2x^2+3xy+3y^2+10=0$).'},
    {'h4': 'Linear functions'},
    {'p': 'A linear function has the variable at first degree: $f(x) = a+bx$ or $y=a+bx$, where '
          '$a$ and $b$ are constants. Its graph is a straight line; $a$ is the intercept on the '
          '$y$-axis (value of $y$ when $x=0$) and $b$ is the **gradient (slope)**, the increase '
          'in $y$ for a unit increase in $x$ — unique to that line, positive or negative.'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.2 — drawing a linear function', 'open': True,
      'q': [{'p': 'Draw the graph of (a) $y=3x+12$, (b) $y=46-5x$.'}],
      'a': [{'p': 'Any two points fix a straight line — usually the $y$-intercept ($x=0$) and '
                  'the $x$-intercept ($y=0$).'},
        {'tex': '\\text{(a)}\\ y=3x+12:\\ (0,12)\\text{ and }(-4,0)'},
        {'tex': '\\text{(b)}\\ y=46-5x:\\ (0,46)\\text{ and }(9.2,0)'}]}},
    {'h4': 'Quadratic functions'},
    {'p': 'A quadratic function has $x$ at second degree: $y=ax^2+bx+c$, where $a,b,c$ are '
          'constants and $a\\ne0$. Its graph is cup-shaped ($\\cup$) when $a$ is positive, and '
          'cap-shaped ($\\cap$) when $a$ is negative.'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.3 — drawing a quadratic function', 'open': True,
      'q': [{'p': 'For $-4 \\le x \\le 3$, draw the graph of (a) $y=x^2+2x-1$; (b) '
                  '$y=5-2x-3x^2$.'}],
      'a': [{'p': 'Substitute each value of $x$ in the given range to build a table of values, '
                  'then plot the points and join them. E.g. for (a): $x=-4 \\Rightarrow y=7$; '
                  '$x=0 \\Rightarrow y=-1$; $x=3 \\Rightarrow y=14$.'}]}},
    {'h4': 'Exponential functions'},
    {'p': 'An exponential function has a constant base and a variable exponent: if $y=a^x$, $y$ '
          'is an exponential function of $x$, with base $a$ and exponent $x$. It is '
          '**non-linear**. If $a>1$ there is exponential **growth**; if $a<1$, exponential '
          '**decay**. Most exponential functions in economic theory use base $e$ (i.e. '
          '$y=e^x$).'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.4 — plotting exponential functions', 'open': True,
      'q': [{'p': 'For $-2 \\le x \\le 2$, plot (a) $y=2^x$; (b) $y=(1/3)^x$; (c) '
                  '$y=3e^{x/2}$.'}],
      'a': [{'table': {'align': 'lrrrrr', 'head': ['$x$', '−2', '−1', '0', '1', '2'], 'rows': [
        ['$y=2^x$', '0.25', '0.5', '1', '2', '4'],
        ['$y=(1/3)^x$', '9', '3', '1', '0.33', '0.11'],
        ['$y=3e^{x/2}$', '1.10', '1.82', '3', '4.95', '8.15'],
      ]}}]}},
    {'h4': 'Logarithmic function'},
    {'p': 'The study text presents the **logarithmic function** in the form $y=ax^b$. Taking '
          'logarithms of both sides gives $\\log y = \\log a + b\\log x$ — so $y$ is said to be '
          'a logarithmic function of $x$. Its graph cannot easily be drawn directly, but plotting '
          '$\\log y$ against $\\log x$ gives a **straight line**, even where the underlying '
          'relationship $y=ax^b$ is itself non-linear (e.g. quadratic).'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.5 — the logarithmic graph of $y=2x^2$',
      'open': True, 'q': [{'p': 'If $y=2x^2$, plot the logarithmic graph for $1\\le x\\le5$.'}],
      'a': [{'table': {'align': 'lrrrrr', 'head': ['$x$', '1', '2', '3', '4', '5'], 'rows': [
        ['$y$', '2', '8', '18', '32', '50'],
        ['$\\log x$', '0', '0.30', '0.48', '0.60', '0.70'],
        ['$\\log y$', '0.30', '0.90', '1.26', '1.51', '1.70'],
      ]}},
      {'note': '$y=2x^2$ is itself a quadratic function, but its **logarithmic graph** '
               '($\\log y$ against $\\log x$) is a straight line.'}]}},
  ]},

  {'n': '11.3', 't': 'Concept of functional relationships — equations', 'b': [
    {'def': {'t': 'Equation / relationship', 'd': 'a mathematical expression of two equal '
                  'quantities, consisting of **variables** (unknowns) and **constants** '
                  '(numbers) — e.g. $x+5=2$; $2x+15=x+8$; $x^2+6x+9=0$.'}},
    {'h4': 'Rules for handling equations'},
    {'ol': [
      'An equation is unchanged if the same number/expression is added to (or subtracted from) '
      'each side, or if each side is multiplied (or divided) by the same number/expression.',
      'The sign of an expression or number **changes** when it crosses the equality sign.',
    ]},
    {'h4': 'Linear equations'},
    {'p': 'A linear equation in one variable contains one unknown of the first degree, and is '
          'solved by applying the rules above.'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.6 — solving linear equations', 'open': True,
      'q': [{'p': 'Solve (a) $2x+3=5$; (b) $8a+5=3a+30$; (c) $\\frac13(y+7)=2(y-1)$; (d) '
                  '$\\frac{2x}{5}-\\frac{3}{14}=\\frac{x}{14}+\\frac{2x}{7}$.'}],
      'a': [
      {'tex': '\\text{(a)}\\ 2x=2 \\Rightarrow x=1'},
      {'tex': '\\text{(b)}\\ 8a-3a=30-5 \\Rightarrow 5a=25 \\Rightarrow a=5'},
      {'p': '(c) Multiply each side by 3: $y+7=6(y-1) \\Rightarrow y+7=6y-6 \\Rightarrow '
            '-5y=-13 \\Rightarrow y=2.6$.'},
      {'p': '(d) Multiply each side by 70 (the LCM of the denominators): $28x-15=7x+20x '
            '\\Rightarrow x=15$.'}]}},
    {'h4': 'Simultaneous equations (two unknowns)'},
    {'p': 'If the solution to equations containing two unknowns can be found at the same time, '
          'the equations are **simultaneous equations**; the number of equations must equal the '
          'number of unknowns. There are four methods of solving them: **substitution**, '
          '**elimination**, **graphical**, and **matrix** — the study text covers the first '
          'three.'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.7 — the three methods', 'open': True, 'q': [
      {'p': '(a) Solve $2x+3y=13$ and $3x+2y=32$ by substitution.'},
      {'p': '(b) Solve $5x-4y=-6$ and $6x+2y=20$ by (i) elimination and (ii) graphically.'}],
      'a': [
      {'p': '(a) From the first equation, $x=\\frac12(13-3y)$. Substitute into the second: '
            '$\\frac32(13-3y)+2y=32 \\Rightarrow 39-9y+4y=64 \\Rightarrow -5y=25 \\Rightarrow '
            'y=-5$, then $x=\\frac12(13+15)=14$. **$x=14$, $y=-5$.**'},
      {'p': '(b)(i) $(ii)\\times2$: $12x+4y=40$; add to (i) $5x-4y=-6$: $17x=34 \\Rightarrow '
            'x=2$; substitute back: $6(2)+2y=20 \\Rightarrow y=4$. **$x=2$, $y=4$.**'},
      {'p': '(ii) Rewrite both as $y=$: $y=1.25x+1.5$ and $y=-3x+10$; the lines cross at the '
            'same point, $(2,4)$, confirming the algebraic answer. Graphical solutions are '
            'estimates and may differ slightly from the algebraic ones due to plotting '
            'approximation.'}]}},
    {'h4': 'Quadratic equations'},
    {'p': 'A one-variable, second-degree equation: $ax^2+bx+c=0$, $a\\ne0$. Three methods of '
          'solution: **factorisation**, **formula**, and **graphical**.'},
    {'fbox': {'h': 'Solving a quadratic equation', 'rows': [
      {'lb': 'Formula method',
       'tex': 'x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 11.8 — the three methods', 'open': True, 'q': [
      {'p': 'Solve (a) $x^2+6x+8=0$ by factorisation; (b) $2x^2+13x-16=0$ by formula; (c) '
            '$x^2+3x-7=0$ by graphical method.'}],
      'a': [
      {'p': '(a) Find two numbers with sum 6 and product 8 — 2 and 4: $x(x+2)+4(x+2)=0 '
            '\\Rightarrow (x+2)(x+4)=0 \\Rightarrow x=-2$ or $-4$. (Not applicable if the '
            'quadratic will not factorise.)'},
      {'p': '(b) $a=2,b=13,c=-16$:'},
      {'tex': 'x = \\frac{-13 \\pm \\sqrt{169+128}}{4} = \\frac{-13\\pm17.23}{4} = -7.56 '
              '\\text{ or } 1.0'},
      {'p': '(This method works whether or not the equation factorises.)'},
      {'p': '(c) Tabulate $y=x^2+3x-7$ for $x=-5,\\dots,3$ and plot; the curve crosses the '
            '$x$-axis at $x\\approx-4.5$ or $1.5$ — the roots. (Works for any quadratic.)'}]}},
  ]},

  {'n': '11.4', 't': 'Applications of the concept of functional relationships', 'b': [
    {'h4': 'Cost, revenue and profit functions'},
    {'p': 'Total cost has two parts: **fixed cost** (machinery, infrastructure — the "set-up '
          'cost," always constant) and **variable cost** (materials, labour, utilities — '
          'depends on the number of units). If $x$ is the number of units, the **cost '
          'function** $C(x)$ is:'},
    {'fbox': {'h': 'Cost, revenue and profit', 'rows': [
      {'lb': 'Linear cost function', 'tex': 'C(x) = a + bx',
       'nt': '$a$ = fixed cost, $b$ = price per unit of $x$ (variable cost).'},
      {'lb': 'Quadratic cost function', 'tex': 'C(x) = ax^2 + bx + c',
       'nt': '$a\\ne0$; $c$ (independent of $x$) is the fixed cost.'},
      {'lb': 'Revenue function', 'tex': 'R(x) = px',
       'nt': '$p$ = sales price per item. There is no such thing as fixed revenue.'},
      {'lb': 'Profit function', 'tex': 'P(x) = R(x) - C(x)',
       'nt': '$P(x)>0$ gain; $P(x)<0$ loss; $P(x)=0$ break-even.'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Examples 11.9–11.11 — cost, revenue and target profit',
      'open': True, 'q': [
      {'p': '11.9 A shop costs ₦120,000/year to rent, plus ₦25,000 to renovate. Find the total '
            'cost to equip it with 480 items at ₦75 each.'},
      {'p': '11.10 If 2,500 items are sold at ₦120 each, find the revenue.'},
      {'p': '11.11 A businessman spends ₦1.5m to set up a workshop; each item costs ₦450 to '
            'produce and sells for ₦1,450. Find the minimum quantity to sell for a profit of at '
            'least ₦800,000.'}],
      'a': [
      {'tex': '11.9:\\ C(x)=145{,}000+75x,\\ x=480 \\Rightarrow C=\\text{\\textnaira}181{,}000'},
      {'tex': '11.10:\\ R(x)=120x=120(2{,}500)=\\text{\\textnaira}300{,}000'},
      {'p': '11.11 $C(x)=1{,}500{,}000+450x$; $R(x)=1{,}450x$; '
            '$P(x)=1{,}000x-1{,}500{,}000$. For $P(x)\\ge800{,}000$:'},
      {'tex': '1{,}000x-1{,}500{,}000\\ge800{,}000 \\Rightarrow x\\ge2{,}300'},
      {'p': 'At least **2,300 items** must be produced and sold.'}]}},
    {'h4': 'Break-even analysis'},
    {'p': 'A business **breaks even** when $R(x)=C(x)$, i.e. $P(x)=0$ — profit is zero (no '
          'profit, no loss). On a break-even graph, the **loss area** is where the revenue line '
          'is below the cost line, and the **profit area** is where it is above.'},
    {'eg': {'tag': 'Study text', 't': 'Examples 11.12–11.13, 11.15 — break-even quantity',
      'open': True, 'q': [
      {'p': '11.12 Find the break-even quantity for Example 11.11.'},
      {'p': '11.13 $C(x)=400+4x$, $R(x)=24x$. Find the break-even quantity graphically.'},
      {'p': '11.15 Sale function $S(x)=800x-250$ (so $R(x)=x\\cdot S(x)$); cost function '
            '$C(x)=50{,}000+200x^2-500x$. Find the break-even quantity.'}],
      'a': [
      {'tex': '11.12:\\ 1{,}450x=1{,}500{,}000+450x \\Rightarrow x=1{,}500\\text{ units}'},
      {'p': 'Below 1,500 units is a loss; above is a profit.'},
      {'p': '11.13 Plot $C(x)=400+4x$ through $(0,400)$ and $(-100,0)$, and $R(x)=24x$ through '
            '$(0,0)$ and $(25,600)$. The lines cross at the break-even quantity, **20 units**.'},
      {'p': '11.15 $R(x)=x(800x-250)=800x^2-250x$. Setting $R(x)=C(x)$: $600x^2+350x-50{,}000=0 '
            '\\Rightarrow 12x^2+7x-1{,}000=0$. By the quadratic formula, $x=8.84$ or $-9.43$; '
            'since $x$ cannot be negative, the break-even quantity is approximately **9**.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 11.14 — simultaneous equations from a costing '
      'problem', 'open': True, 'q': [
      {'p': 'A firm uses 8 hours of labour and 10 units of material for a total cost of ₦2,100; '
            'using 12 hours of labour and 6 units of material costs ₦2,700. Find the cost per '
            'unit of labour and of material.'}],
      'a': [
      {'p': 'Let $x$ = cost per labour-hour, $y$ = cost per material unit: '
            '$8x+10y=2{,}100$ and $12x+6y=2{,}700$. Solving simultaneously (eliminate $y$): '
            '$72x=14{,}400 \\Rightarrow x=200$; then $y=50$.'},
      {'p': 'Labour costs **₦200/hour**, material costs **₦50/unit**.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 11.16 — exponential cost/revenue functions',
      'open': True, 'q': [
      {'p': '(a) Monthly revenue (Leone) $R=200{,}000(0.5)^{0.6x}$, where $x$ (Le\'000) is '
            'overhead spend. Find (i) the maximum revenue and (ii) revenue if Le5,000 is spent '
            'on overheads.'},
      {'p': '(b) Production cost $C(x)=200-80e^{-0.02x}$, $x$ = units produced. Find (i) fixed '
            'costs, (ii) the cost of producing 250 items, (iii) the fixed-cost percentage of '
            '(ii).'}],
      'a': [
      {'p': '(a)(i) Maximum revenue is at $x=0$ (no overhead spend): $R=200{,}000(0.5)^0=$ '
            '**Le200,000**.'},
      {'p': '(ii) $x=5{,}000\\div1{,}000=5$: $R=200{,}000(0.5)^{3}=$ **Le25,000**.'},
      {'p': '(b)(i) Fixed cost is at $x=0$: $C=200-80e^0=120$, i.e. **₦120,000**.'},
      {'p': '(ii) $x=250$: $C=200-80e^{-5}=199.461$, i.e. **₦199,461**.'},
      {'tex': '\\text{(iii)}\\ \\frac{120{,}000}{199{,}461}\\times100 = 60.16\\%'}]}},
    {'h4': 'Demand and supply equations; market equilibrium'},
    {'p': 'Demand and supply are usually approximated by linear equations of the form '
          '$y=a+bx$ (price $y$, quantity $x$).'},
    {'ul': [
      '**Demand** — inversely related to price (quantity falls as price rises); the demand '
      'curve has a **negative** slope. A zero slope means constant price regardless of demand; '
      'an undefined slope means constant demand regardless of price.',
      '**Supply** — directly related to price (quantity rises as price rises); the supply curve '
      'has a **positive** slope.',
      '**Market equilibrium** — where quantity demanded equals quantity supplied; found by '
      'solving the demand and supply equations simultaneously, or graphically as the point '
      'where the two curves intersect. It is only meaningful in the first quadrant ($x,y>0$).',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Examples 11.17–11.19 — demand, supply and equilibrium',
      'open': True, 'q': [
      {'p': '11.17 500 watches sell at ₦2,400 each; 800 sell at ₦2,000 each. (a) Find the demand '
            'equation. (b) How many sell at ₦3,000? (c) What is the highest price a watch could '
            'command?'},
      {'p': '11.18 2,000 printers are supplied at ₦15,000; 3,200 at ₦21,000. (a) Find the supply '
            'equation. (b) How many at ₦30,000? (c) What price if 8,000 are supplied? (d) '
            'Lowest possible price?'},
      {'p': '11.19 Demand: $20y+3x=335$. Supply: $15y-2x=60$. Find the equilibrium price and '
            'quantity (a) simultaneously, (b) graphically.'}],
      'a': [
      {'p': '11.17 (a) $y=a+bx$ through $(500,2400)$ and $(800,2000)$: $b=-\\frac43$, '
            '$a=\\frac{9200}{3}$, so $3y=9{,}200-4x$. (b) $y=3{,}000 \\Rightarrow x=50$ '
            'watches. (c) Highest price is where demand is zero ($x=0$): $y\\approx'
            '\\text{\\textnaira}3{,}066.67$.'},
      {'p': '11.18 (a) $y=a+bx$ through $(2000,15000)$ and $(3200,21000)$: $b=5$, $a=5{,}000$, '
            'so $y=5{,}000+5x$. (b) $y=30{,}000 \\Rightarrow x=5{,}000$ printers. (c) $x=8{,}000 '
            '\\Rightarrow y=\\text{\\textnaira}45{,}000$. (d) Lowest price at $x=0$: '
            '$y=\\text{\\textnaira}5{,}000$.'},
      {'p': '11.19 (a) Solving simultaneously: $y=10$, $x=45$ — equilibrium price 10, quantity '
            '45. (b) Graphically the lines meet at approximately the same point (graphical '
            'solutions are estimates, so a small difference from the algebraic answer is '
            'normal).'}]}},
  ]},

  {'n': '11.5', 't': 'Simple linear inequalities as applied to operations research', 'b': [
    {'p': 'When two quantities are not equal, one is greater or less than the other — an '
          '**inequality**. Symbols: $<$ less than; $\\le$ less than or equal to; $>$ greater '
          'than; $\\ge$ greater than or equal to.'},
    {'h4': 'Rules for handling inequalities'},
    {'ol': [
      'The symbol is **unchanged** if a number/expression is added to (or subtracted from) both '
      'sides, or if both sides are multiplied (or divided) by a **positive** number.',
      'The symbol **reverses** if both sides are multiplied (or divided) by a **negative** '
      'number.',
      'The sign of a number/expression changes when it crosses the inequality symbol.',
    ]},
    {'p': 'A solution to an inequality is a **range of values**, not a single point value as '
          'with an equation.'},
    {'eg': {'tag': 'Study text', 't': 'Example 11.20 — solving and graphing inequalities',
      'open': True, 'q': [
      {'p': 'Indicate the region satisfying: (a) $2x+5<x+8$; (b) $4x+7\\ge2x+15$; (c) '
            '$3x+10\\le5x-2$; and graph (d)–(k), including $x\\ge0,\\,y\\ge0$; $x+2y\\le6$; '
            '$3x-2y\\ge12$; and the simultaneous systems $2x+3y\\le9,\\,5x+2y\\le10$ and '
            '$2x+y\\le18,\\,1.5x+2y\\ge15,\\,x\\ge0,\\,y\\ge0$.'}],
      'a': [
      {'tex': '\\text{(a)}\\ x<3 \\qquad \\text{(b)}\\ x\\ge4 \\qquad \\text{(c)}\\ '
              '-2x\\le-12 \\Rightarrow x\\ge6\\ (\\text{sign reverses — divided by }-2)'},
      {'p': 'For a two-variable inequality like $x+2y\\le6$, draw the line $x+2y=6$ (through '
            '$(0,3)$ and $(6,0)$); it splits the plane in two. Test the origin $(0,0)$ in the '
            'inequality: $0\\le6$ is true, so the region containing the origin is the answer. '
            'If the test point makes the inequality false (as for $3x-2y\\ge12$, since '
            '$0\\ge12$ is false), the required region is the **other** side, away from the '
            'origin.'},
      {'p': 'For two or more simultaneous inequalities (e.g. $2x+3y\\le9$ and $5x+2y\\le10$), '
            'draw all the boundary lines on the same axes; the required region is where '
            '**every** inequality is satisfied at once — the overlap of all the individual '
            'regions, including $x\\ge0,\\,y\\ge0$ where those are also required.'}]}},
  ]},

  {'n': '11.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'If $f(x)=3x^3-4x^2+2x+555$, then $f(-5)$ is (A) 820 (B) 290 (C) 270 (D) 70 (E) 90',
        'The condition for $ax^2+bx+c$ to be a quadratic expression is (A) $b\\ne0$ (B) '
        '$a\\ne0\\,\\&\\,b\\ne0$ (C) $b\\ne0\\,\\&\\,c\\ne0$ (D) $c\\ne0$ (E) $a\\ne0$',
        'A company\'s cost function is $C(x)=500+2x^2+5x$ and revenue function is '
        '$R(x)=3x^2-10x$, $x$ = items produced and sold. The profit from 500 items is (A) '
        '24,200 (B) 242,000 (C) 124,000 (D) 224,000 (E) 257,000',
        'If demand and supply are given by $30y+7x=800$ and $14y-5x=-40$, the equilibrium '
        'point is (A) (15, 50) (B) (50, 20) (C) (50, 15) (D) (20, 50) (E) (25, 25)',
        'On the graph of $y=a+bx$, $a$ is the …………… on the $y$-axis while $b$ is the ……………',
        'An exponential function is a function which has a …………… base and a …………… exponent',
        'The sign of a variable or constant in an equation changes when it crosses the …………',
        'When two expressions are not equal, then one has to be …………… or …………… than the other',
        'If for a business, $R(x)-C(x)<0$, then the business is said to be running at a ……………',
        'The demand for a commodity is …………… proportional while supply is …………… proportional '
        'to the price of the commodity',
      ]}],
      'a': [
      {'ol': [
        '**D — 70.** $f(-5)=3(-5)^3-4(-5)^2+2(-5)+555=-375-100-10+555=70$.',
        '**E — $a\\ne0$** (if $a=0$ the quadratic term vanishes).',
        '**B — 242,000.** Profit $=R(x)-C(x)=x^2-15x-500$; at $x=500$: '
        '$(500)^2-15(500)-500=242{,}000$.',
        '**C — (50, 15).** Solving simultaneously gives $y=15$, $x=50$.',
        '**Intercept; slope of the line** (in that order).',
        '**Constant; variable** (in that order).',
        '**Equality sign.**',
        '**Less; greater** (or vice versa).',
        '**Loss.**',
        '**Inversely; directly** (in that order).',
      ]}]}},
  ]},

  {'n': '11.7', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§11.1 Functions** — a mathematical expression describing a relationship between two '
      'or more variables; written $f(x)$; $y$ often stands for $f(x)$.',
      '**§11.2 Types of functions** — explicit ($y$ alone on one side) vs implicit (all '
      'variables mixed in one equation); **linear** $y=a+bx$ (straight line, intercept $a$, '
      'gradient $b$); **quadratic** $y=ax^2+bx+c$, $a\\ne0$ (cup-shaped if $a>0$, cap-shaped if '
      '$a<0$); **exponential** $y=a^x$ (constant base, variable exponent; $a>1$ growth, $a<1$ '
      'decay; often base $e$); **logarithmic** (in this text) $y=ax^b$, whose log–log plot '
      '$\\log y=\\log a+b\\log x$ is a straight line even when the underlying relation is '
      'non-linear.',
      '**§11.3 Equations** — an equation is unchanged by adding/subtracting/multiplying/'
      'dividing both sides by the same thing; signs flip crossing "="; linear equations solved '
      'directly; simultaneous equations (as many equations as unknowns) by substitution, '
      'elimination or graphically; quadratic equations by factorisation, formula '
      '$x=(-b\\pm\\sqrt{b^2-4ac})/2a$, or graphically.',
      '**§11.4 Business applications** — cost $C(x)=a+bx$ (or quadratic); revenue $R(x)=px$ (no '
      'fixed revenue); profit $P(x)=R(x)-C(x)$; break-even where $R(x)=C(x)$, i.e. $P(x)=0$. '
      'Demand ($y=a+bx$, negative slope) and supply (positive slope) equations; market '
      'equilibrium where $Q_d=Q_s$, solved simultaneously or graphically, meaningful only where '
      'both price and quantity are positive.',
      '**§11.5 Linear inequalities** — symbols $<,\\le,>,\\ge$; unchanged by adding/subtracting '
      'or multiplying/dividing by a positive number; **reversed** by multiplying/dividing by a '
      'negative number; solution is a range, not a point. A two-variable inequality is solved '
      'by drawing its boundary line and testing the origin (or another convenient point) to see '
      'which side satisfies it; several simultaneous inequalities are solved together as the '
      'overlap of all their individual regions.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Function** — a mathematical expression describing a relationship between two or more '
      'variables.',
      '**Explicit function** — one variable expressed directly in terms of the other(s). '
      '**Implicit function** — all the variables appear together in one equation.',
      '**Linear function** — $y=a+bx$; $a$ = $y$-intercept, $b$ = gradient (slope).',
      '**Quadratic function** — $y=ax^2+bx+c$, $a\\ne0$; graph is a parabola.',
      '**Exponential function** — constant base, variable exponent, $y=a^x$.',
      '**Logarithmic function (this text)** — $y=ax^b$; becomes linear in $\\log x,\\log y$.',
      '**Equation** — an expression of two equal quantities, made of variables and constants.',
      '**Simultaneous equations** — equations solved together; need as many equations as '
      'unknowns.',
      '**Inequality** — an expression of two quantities that are not equal, using $<,\\le,>,\\ge$.',
      '**Cost function $C(x)$** — fixed cost + variable cost.',
      '**Revenue function $R(x)=px$** — no fixed component.',
      '**Profit function $P(x)=R(x)-C(x)$.**',
      '**Break-even point** — where $P(x)=0$, i.e. $R(x)=C(x)$.',
      '**Market equilibrium** — where quantity demanded equals quantity supplied.',
    ]},
    {'h3': 'Formula reference'},
    {'fbox': {'h': 'Every formula in the chapter', 'rows': [
      {'lb': 'Linear function', 'tex': 'y = a + bx'},
      {'lb': 'Quadratic formula', 'tex': 'x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}'},
      {'lb': 'Cost function (linear)', 'tex': 'C(x) = a + bx'},
      {'lb': 'Cost function (quadratic)', 'tex': 'C(x) = ax^2+bx+c'},
      {'lb': 'Revenue function', 'tex': 'R(x) = px'},
      {'lb': 'Profit function', 'tex': 'P(x) = R(x) - C(x)'},
      {'lb': 'Break-even condition', 'tex': 'R(x) = C(x) \\iff P(x) = 0'},
      {'lb': 'Demand/supply equation', 'tex': 'y = a + bx \\quad (y=\\text{price},\\ '
              'x=\\text{quantity})'},
    ]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Linear function', 'tex': 'y = a + bx'},
  {'lb': 'Quadratic formula', 'tex': 'x = \\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}'},
  {'lb': 'Cost function', 'tex': 'C(x) = a + bx \\ \\text{ or } \\ ax^2+bx+c'},
  {'lb': 'Revenue function', 'tex': 'R(x) = px'},
  {'lb': 'Profit function', 'tex': 'P(x) = R(x) - C(x)'},
  {'lb': 'Break-even condition', 'tex': 'R(x) = C(x)'},
 ],
 'focus':
   'Section A tests the definitions verbatim (intercept vs gradient, growth vs decay base, '
   'inversely/directly proportional demand/supply) and small formula evaluations ($f(-5)$-style '
   'questions, discriminant sign). Section B is reliably a cost/revenue/profit or a demand/'
   'supply-and-equilibrium question, solved by simultaneous equations exactly as in the worked '
   'examples above — set up the two equations carefully, then it is routine algebra.',
 'errors': [
   'Sign errors substituting into the quadratic formula, especially when $b$ is itself negative.',
   'Assuming a fixed revenue term — there is none; $R(x)=px$ always passes through the origin.',
   'Forgetting the inequality symbol reverses when multiplying/dividing by a negative number.',
   'Testing the wrong point (not the origin, or a point actually ON the boundary line) when '
   'shading a two-variable inequality.',
   'Mixing up which of demand/supply has the negative slope — demand is inversely related to '
   'price.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The gradient of the line joining $(1, 4)$ and $(3, 10)$ is',
    'o': ['2', '3', '6', '7', '½'],
    'a': 1,
    'w': 'Gradient is the change in $y$ divided by the change in $x$.',
    'calc': 'b = \\frac{10-4}{3-1} = \\frac{6}{2} = 3',
    'src': 'Chapter 11.2', 'sec': '11.2'},
   {'q': 'The roots of $x^2 - 5x + 6 = 0$ are',
    'o': ['1 and 6', '2 and 3', '−2 and −3', '5 and 6', '1 and 5'],
    'a': 1,
    'w': 'Factorise: two numbers whose sum is 5 and product is 6.',
    'calc': '(x-2)(x-3) = 0 \\Rightarrow  x = 2 \\text{ or } 3',
    'src': 'Chapter 11.3', 'sec': '11.3'},
   {'q': 'Fixed costs are ₦300,000; selling price ₦80/unit, variable cost ₦50/unit. The '
         'break-even output is',
    'o': ['3,750 units', '10,000 units', '6,000 units', '5,000 units', '3,000 units'],
    'a': 1,
    'w': 'Break-even is where $R(x)=C(x)$: $80x = 300{,}000+50x$.',
    'calc': '80x=300{,}000+50x \\Rightarrow 30x=300{,}000 \\Rightarrow x=10{,}000',
    'src': 'Chapter 11.4', 'sec': '11.4'},
   {'q': 'If $b^2 - 4ac < 0$ in the quadratic formula, the equation has',
    'o': ['two distinct real roots', 'no real roots', 'one repeated root',
          'roots that sum to zero', 'infinitely many roots'],
    'a': 1,
    'w': 'A negative value under the square root has no real square root, so the formula '
         'yields no real solution.',
    'src': 'Chapter 11.3', 'sec': '11.3'},
   {'q': 'Given $Q_d = 60 - 4P$ and $Q_s = 10 + P$, the equilibrium price is',
    'o': ['₦8', '₦10', '₦12', '₦14', '₦20'],
    'a': 1,
    'w': 'Set demand equal to supply and solve for $P$.',
    'calc': '60 - 4P = 10 + P \\Rightarrow  50 = 5P \\Rightarrow  P = 10',
    'src': 'Chapter 11.4', 'sec': '11.4'},
   {'q': 'Dividing both sides of $-3x \\le 12$ by $-3$ gives',
    'o': ['$x \\le -4$', '$x \\ge -4$', '$x \\le 4$', '$x \\ge 4$', '$x = -4$'],
    'a': 1,
    'w': 'Dividing an inequality by a negative number reverses the symbol.',
    'src': 'Chapter 11.5', 'sec': '11.5'},
  ],
  'theory': [
   {'q': 'A manufacturer sells a product at ₦400 per unit; variable cost is ₦240 per unit and '
         'fixed costs are ₦960,000 per period. (a) State the cost, revenue and profit functions. '
         '(b) Find the break-even output and sales value. (c) Find the output needed for a '
         '₦320,000 profit.',
    'marks': 10,
    'a': [
      {'p': 'Let $x$ be the number of units produced and sold.'},
      {'tex': 'C(x) = 960{,}000+240x \\qquad R(x)=400x \\qquad '
              'P(x)=R(x)-C(x)=160x-960{,}000'},
      {'p': '**Break-even**, where $P(x)=0$:'},
      {'tex': '160x=960{,}000 \\Rightarrow x^{*}=6{,}000\\text{ units}, \\quad '
              '\\text{sales value}=6{,}000\\times400=\\text{\\textnaira}2{,}400{,}000'},
      {'p': '**Target profit** of ₦320,000: $P(x)=320{,}000$:'},
      {'tex': '160x-960{,}000=320{,}000 \\Rightarrow x=\\frac{1{,}280{,}000}{160}=8{,}000'
              '\\text{ units}'}],
    'src': 'Chapter 11.4', 'sec': '11.4'},
  ]},
}
