CH = {
 'n': 15,
 't': 'Linear Programming',
 'brief': 'Formulating a linear programme, solving a two-variable problem graphically, the '
          'simplex method with slack variables, and the interpretation of slack and shadow '
          'prices.',
 'outcomes': [
   'Formulate a business problem as a linear programme',
   'Plot constraints and identify the feasible region',
   'Find the optimal solution by evaluating the corner points',
   'Convert a maximisation problem to standard form with slack variables',
   'Carry out the simplex algorithm and read the final tableau',
   'Interpret slack variables and shadow prices',
 ],
 'secs': [
  {'n': '15.1', 't': 'Formulation', 'b': [
    {'p': 'Every linear programme has three parts. Formulating them correctly carries as many '
          'marks as the solution, and is where most candidates lose them.'},
    {'ol': [
      '**Decision variables** — what the manager chooses. Define them precisely, with units: '
      '"let $x$ be the number of units of product A produced per week".',
      '**Objective function** — a linear expression in the decision variables to be maximised '
      '(contribution, profit) or minimised (cost, time).',
      '**Constraints** — linear inequalities expressing the limits on resources, plus the '
      'non-negativity conditions $x, y \\ge 0$.',
    ]},
    {'warn': 'The objective in a production problem is to maximise **contribution**, not '
             'profit. Fixed costs do not vary with the decision, so including them changes '
             'nothing except the arithmetic — and if they are apportioned per unit they will '
             'give the wrong answer.'},
    {'h4': 'Assumptions of the model'},
    {'ul': [
      '**Linearity** — the objective and every constraint are proportional; doubling output '
      'doubles both contribution and resource usage.',
      '**Certainty** — all coefficients are known constants.',
      '**Divisibility** — fractional solutions are allowed. Where they are not (aircraft, '
      'staff), integer programming is required.',
      '**Non-negativity** — the variables cannot be negative.',
      '**Additivity** — the total is the sum of the parts; there are no interaction effects.',
    ]},
  ]},

  {'n': '15.2', 't': 'The graphical method', 'b': [
    {'steps': [
      'Formulate the problem.',
      'Convert each inequality to an equation and plot it by finding the two intercepts '
      '(set $x = 0$, then $y = 0$).',
      'Shade the side of each line that satisfies the inequality; the region satisfying all '
      'of them simultaneously is the **feasible region**.',
      'Identify the coordinates of every corner (vertex) of the feasible region, solving '
      'simultaneous equations where two constraints intersect.',
      'Evaluate the objective function at each corner and select the best.',
    ]},
    {'key': 'The optimum of a linear programme always lies at a **corner** of the feasible '
            'region. This is the whole basis of the method — and of the simplex algorithm, '
            'which simply moves from corner to corner in the direction of improvement.'},
    {'eg': {'t': 'Graphical solution', 'q': [
      {'p': 'Adeleke Manufacturing produces two products, A and B, with contributions of ₦30 '
            'and ₦20 per unit respectively. Each unit of A requires 2 machine hours and 1 '
            'labour hour; each unit of B requires 1 machine hour and 1 labour hour. Only 100 '
            'machine hours and 80 labour hours are available each week, and no more than 40 '
            'units of A can be sold. Determine the weekly production plan that maximises '
            'contribution.'}],
      'a': [
      {'h4': 'Formulation'},
      {'p': 'Let $a$ = units of A and $b$ = units of B produced per week.'},
      {'tex': '\\text{Maximise } Z = 30a + 20b'},
      {'tex': '\\text{subject to } \\quad 2a + b \\le 100 \\quad \\text{(machine hours)}'},
      {'tex': 'a + b \\le 80 \\quad \\text{(labour hours)}'},
      {'tex': 'a \\le 40 \\quad \\text{(sales limit)}'},
      {'tex': 'a, b \\ge 0'},
      {'h4': 'Plotting'},
      {'table': {'align': 'lll', 'head': ['Constraint', 'Intercept on $a$', 'Intercept on $b$'],
        'rows': [
        ['$2a + b = 100$', '$(50, 0)$', '$(0, 100)$'],
        ['$a + b = 80$', '$(80, 0)$', '$(0, 80)$'],
        ['$a = 40$', 'vertical line', '—'],
      ]}},
      {'h4': 'Corner points'},
      {'p': 'The intersection of the two resource constraints is found by simultaneous '
            'equations. Subtracting $a + b = 80$ from $2a + b = 100$:'},
      {'tex': 'a = 20 \\quad\\Rightarrow\\quad b = 80 - 20 = 60'},
      {'p': 'The intersection of $a = 40$ with $2a + b = 100$ gives $b = 20$. Evaluating the '
            'objective at each vertex:'},
      {'table': {'align': 'lrr', 'head': ['Corner $(a, b)$', 'Working', 'Contribution $Z$ (₦)'],
        'rows': [
        ['(0, 0)', '—', '0'],
        ['(0, 80)', '$30(0)+20(80)$', '1,600'],
        ['(20, 60)', '$30(20)+20(60)$', '**1,800**'],
        ['(40, 20)', '$30(40)+20(20)$', '1,600'],
        ['(40, 0)', '$30(40)+20(0)$', '1,200'],
      ]}},
      {'h4': 'Solution'},
      {'p': 'The maximum contribution of **₦1,800 per week** is obtained by producing **20 '
            'units of A and 60 units of B**.'},
      {'p': 'Resource usage at the optimum:'},
      {'ul': [
        'Machine hours: $2(20) + 60 = 100$ — **fully used**, no slack.',
        'Labour hours: $20 + 60 = 80$ — **fully used**, no slack.',
        'Sales limit on A: 20 units against a limit of 40 — **20 units of slack**, so this '
        'constraint is not binding and does not affect the solution.',
      ]},
      {'note': 'Only binding constraints matter. Relaxing the sales limit on A would change '
               'nothing, because the plan does not reach it. Relaxing either resource '
               'constraint would increase contribution — by how much is the shadow price, '
               'computed in §15.4.'}]}},
  ]},

  {'n': '15.3', 't': 'The simplex method', 'b': [
    {'p': 'The graphical method fails beyond two variables. The **simplex method** solves any '
          'size of problem by moving from one corner of the feasible region to an adjacent, '
          'better one, until no improvement is possible.'},
    {'h4': 'Standard form'},
    {'ul': [
      'A "$\\le$" constraint is made an equation by adding a **slack variable**, which measures '
      'the unused resource: $2a + b + s_1 = 100$.',
      'A "$\\ge$" constraint requires a **surplus variable** to be subtracted and an '
      '**artificial variable** added, so that an initial feasible solution exists.',
      'An "$=$" constraint requires an artificial variable only.',
      'The objective is written with all terms on the left: $Z - 30a - 20b = 0$.',
    ]},
    {'steps': [
      'Set up the initial tableau with the slack variables in the basis (all decision variables '
      'zero — the origin).',
      '**Entering variable:** choose the column with the most negative coefficient in the $Z$ '
      'row. If none is negative, the current solution is optimal.',
      '**Leaving variable:** divide each right-hand-side value by the corresponding positive '
      'coefficient in the pivot column; the smallest non-negative ratio identifies the pivot '
      'row. Ignore zero and negative pivot-column entries.',
      'Divide the pivot row by the pivot element so that it becomes 1.',
      'Add multiples of the new pivot row to every other row (including the $Z$ row) so that '
      'the rest of the pivot column becomes zero.',
      'Repeat from step 2.',
    ]},
    {'eg': {'t': 'Simplex solution of the same problem', 'q': [
      {'p': 'Solve the Adeleke Manufacturing problem of §15.2 by the simplex method and '
            'interpret the final tableau.'}],
      'a': [
      {'p': 'Introduce slack variables $s_1$ (machine hours), $s_2$ (labour hours) and $s_3$ '
            '(sales limit):'},
      {'tex': '2a + b + s_1 = 100, \\quad a + b + s_2 = 80, \\quad a + s_3 = 40'},
      {'tex': 'Z - 30a - 20b = 0'},
      {'h4': 'Initial tableau'},
      {'table': {'align': 'lrrrrrr',
        'head': ['Basis', '$a$', '$b$', '$s_1$', '$s_2$', '$s_3$', 'RHS'], 'rows': [
        ['$s_1$', '2', '1', '1', '0', '0', '100'],
        ['$s_2$', '1', '1', '0', '1', '0', '80'],
        ['$s_3$', '1', '0', '0', '0', '1', '40'],
        ['$Z$', '−30', '−20', '0', '0', '0', '0'],
      ]}},
      {'p': 'Most negative in the $Z$ row is $-30$, so **$a$ enters**. Ratios: $100/2 = 50$, '
            '$80/1 = 80$, $40/1 = 40$. The smallest is 40, so **$s_3$ leaves** and the pivot '
            'element is the 1 in row $s_3$, column $a$.'},
      {'h4': 'Second tableau'},
      {'table': {'align': 'lrrrrrr',
        'head': ['Basis', '$a$', '$b$', '$s_1$', '$s_2$', '$s_3$', 'RHS'], 'rows': [
        ['$s_1$', '0', '1', '1', '0', '−2', '20'],
        ['$s_2$', '0', '1', '0', '1', '−1', '40'],
        ['$a$', '1', '0', '0', '0', '1', '40'],
        ['$Z$', '0', '−20', '0', '0', '30', '1,200'],
      ]}},
      {'p': 'Now $-20$ is the most negative, so **$b$ enters**. Ratios: $20/1 = 20$ and '
            '$40/1 = 40$ (row $a$ has a zero in the $b$ column and is skipped). **$s_1$ '
            'leaves**.'},
      {'h4': 'Third tableau'},
      {'table': {'align': 'lrrrrrr',
        'head': ['Basis', '$a$', '$b$', '$s_1$', '$s_2$', '$s_3$', 'RHS'], 'rows': [
        ['$b$', '0', '1', '1', '0', '−2', '20'],
        ['$s_2$', '0', '0', '−1', '1', '1', '20'],
        ['$a$', '1', '0', '0', '0', '1', '40'],
        ['$Z$', '0', '0', '20', '0', '−10', '1,600'],
      ]}},
      {'p': '$-10$ remains, so **$s_3$ enters**. Ratios use only positive entries in the $s_3$ '
            'column: $20/1 = 20$ in row $s_2$ and $40/1 = 40$ in row $a$ (row $b$ has $-2$ and '
            'is skipped). **$s_2$ leaves**.'},
      {'h4': 'Final tableau'},
      {'table': {'align': 'lrrrrrr',
        'head': ['Basis', '$a$', '$b$', '$s_1$', '$s_2$', '$s_3$', 'RHS'], 'rows': [
        ['$b$', '0', '1', '−1', '2', '0', '60'],
        ['$s_3$', '0', '0', '−1', '1', '1', '20'],
        ['$a$', '1', '0', '1', '−1', '0', '20'],
        ['$Z$', '0', '0', '10', '10', '0', '1,800'],
      ]}},
      {'p': 'No negative coefficient remains in the $Z$ row, so the solution is **optimal**.'},
      {'note': 'Reading the tableau: the basis column gives the variables that are non-zero, '
               'and the RHS gives their values. So $a = 20$, $b = 60$, $s_3 = 20$, with '
               '$s_1 = s_2 = 0$ (they are not in the basis). Contribution $Z = ₦1{,}800$ — '
               'exactly the graphical answer.'}]}},
  ]},

  {'n': '15.4', 't': 'Slack and shadow prices', 'b': [
    {'def': {'t': 'Slack variable',
             'd': 'The unused quantity of a resource at the optimum. A slack of zero means the '
                  'resource is fully used and the constraint is **binding**; a positive slack '
                  'means the resource is not scarce.'}},
    {'def': {'t': 'Shadow price (dual value)',
             'd': 'The increase in the objective function that would result from one additional '
                  'unit of a scarce resource. It is read from the $Z$ row of the final tableau '
                  'under the corresponding slack column. A non-binding resource has a shadow '
                  'price of zero.'}},
    {'p': 'From the final tableau above, the $Z$-row entries under $s_1$ and $s_2$ are both 10. '
          'So the shadow price of a machine hour is **₦10** and of a labour hour also **₦10**, '
          'while the sales limit on A, being non-binding, has a shadow price of zero.'},
    {'eg': {'t': 'Using the shadow price', 'q': [
      {'p': 'Adeleke can hire additional machine time at ₦6 per hour or additional labour at '
            '₦12 per hour. Advise the company.'}],
      'a': [
      {'ul': [
        '**Machine time.** The shadow price is ₦10 and the marginal cost ₦6, so each extra hour '
        'adds ₦4 of net contribution. **Hire it.**',
        '**Labour.** The shadow price is ₦10 but the marginal cost ₦12, so each extra hour '
        'would cost ₦2 more than it earns. **Do not hire it.**',
      ]},
      {'warn': 'A shadow price holds only over a limited range. As machine hours are added the '
               'optimum eventually shifts to a different corner, another constraint becomes '
               'binding, and the shadow price changes. Never extrapolate it indefinitely — '
               'state the range over which it is valid, or note that it applies only to small '
               'changes.'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Standard form of an LP',
   'tex': '\\text{Max } Z = c_1x_1 + c_2x_2 \\ \\text{ s.t. } \\ a_{ij}x_j \\le b_i, \\ x_j \\ge 0'},
  {'lb': 'Slack variable ($\\le$ constraint)',
   'tex': 'a_{i1}x_1 + a_{i2}x_2 + s_i = b_i'},
  {'lb': 'Surplus variable ($\\ge$ constraint)',
   'tex': 'a_{i1}x_1 + a_{i2}x_2 - s_i + A_i = b_i'},
  {'lb': 'Simplex ratio test',
   'tex': '\\theta = \\min\\left\\{\\frac{b_i}{a_{ik}} : a_{ik} > 0\\right\\}'},
  {'lb': 'Shadow price',
   'tex': '\\text{Shadow price} = \\frac{\\Delta Z}{\\Delta b_i}'},
 ],
 'focus':
   'A frequent Section B question, and reliably the highest-scoring one for a prepared '
   'candidate. Most diets ask for formulation plus a graphical solution; the simplex appears '
   'less often but the *interpretation* of a given final tableau appears regularly and is quick '
   'marks. Always evaluate every corner point and tabulate the results — examiners award marks '
   'for the table even when the final selection is wrong.',
 'errors': [
   'Failing to define the decision variables in words, with units.',
   'Maximising profit after deducting apportioned fixed costs instead of maximising '
   'contribution.',
   'Omitting the non-negativity constraints.',
   'Reading corner coordinates off the graph by eye instead of solving the simultaneous '
   'equations.',
   'Testing only one or two corners rather than all of them.',
   'In the simplex ratio test, dividing by a negative or zero coefficient.',
   'Treating a shadow price as valid for any size of increase in the resource.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In a linear programming problem, the optimal solution always occurs',
    'o': ['at the centre of the feasible region', 'at a corner point of the feasible region',
          'where all constraints are binding', 'at the origin',
          'where the objective function is zero'],
    'a': 1,
    'w': 'A linear objective attains its extreme value at a vertex of a convex feasible region; '
         'this is the basis of both the graphical and the simplex methods.',
    'src': 'Chapter 15.2'},
   {'q': 'A slack variable is added to a constraint of the form',
    'o': ['$\\ge$', '$\\le$', '$=$', '$<$', '$\\ne$'],
    'a': 1,
    'w': 'A $\\le$ constraint has unused capacity, which the slack variable measures. A $\\ge$ '
         'constraint needs a surplus variable subtracted.',
    'src': 'Chapter 15.3'},
   {'q': 'The shadow price of a resource that is not fully utilised at the optimum is',
    'o': ['equal to its market price', 'zero', 'negative', 'equal to the contribution per unit',
          'undefined'],
    'a': 1,
    'w': 'If a resource is already in surplus, an additional unit adds nothing to the '
         'objective.',
    'src': 'Chapter 15.4'},
   {'q': 'Maximise $Z = 5x + 4y$ subject to $x + y \\le 10$, $x \\le 6$, $x, y \\ge 0$. The '
         'maximum value of $Z$ is',
    'o': ['40', '46', '50', '54', '30'],
    'a': 1,
    'w': 'Test the corners $(0,0)$, $(0,10)$, $(6,4)$ and $(6,0)$. Since $x$ carries the higher '
         'contribution, push $x$ to its limit of 6 and fill the rest with $y$.',
    'calc': 'Z(6,4) = 5(6) + 4(4) = 30 + 16 = 46 \\quad\\text{against}\\quad Z(0,10) = 40',
    'src': 'Chapter 15.2'},
   {'q': 'In the simplex method, the variable chosen to enter the basis is the one with',
    'o': ['the largest right-hand-side value', 'the most negative coefficient in the $Z$ row',
          'the smallest ratio in the ratio test', 'the largest positive coefficient in the $Z$ row',
          'the smallest coefficient in the pivot row'],
    'a': 1,
    'w': 'For a maximisation problem the most negative $Z$-row coefficient identifies the '
         'variable that improves the objective fastest. The ratio test identifies the '
         '*leaving* variable.',
    'src': 'Chapter 15.3'},
   {'q': 'Which of the following is NOT an assumption of linear programming?',
    'o': ['Linearity', 'Divisibility', 'Certainty', 'Independence of the decision variables',
          'Additivity'],
    'a': 3,
    'w': 'Linear programming does not require the decision variables to be independent — they '
         'are linked precisely through the shared constraints. The other four are standard '
         'assumptions of the model.',
    'src': 'Chapter 15.1'},
  ],
  'theory': [
   {'q': 'Kuforiji Limited manufactures two products, X and Y, which yield contributions of '
         '₦40 and ₦50 per unit respectively. Each unit of X requires 4 hours of machining and '
         '2 hours of finishing; each unit of Y requires 2 hours of machining and 5 hours of '
         'finishing. In the coming month 400 machining hours and 500 finishing hours are '
         'available. (a) Formulate the problem as a linear programme. (b) Determine the '
         'production plan that maximises contribution, using the graphical method. (c) State '
         'the slack on each resource. (d) State three assumptions underlying your model.',
    'marks': 15,
    'a': [
      {'h4': '(a) Formulation'},
      {'p': 'Let $x$ = number of units of product X manufactured in the month, and $y$ = number '
            'of units of product Y.'},
      {'tex': '\\text{Maximise } Z = 40x + 50y \\quad \\text{(contribution in ₦)}'},
      {'p': 'Subject to:'},
      {'tex': '4x + 2y \\le 400 \\quad \\text{(machining hours)}'},
      {'tex': '2x + 5y \\le 500 \\quad \\text{(finishing hours)}'},
      {'tex': 'x \\ge 0, \\quad y \\ge 0 \\quad \\text{(non-negativity)}'},
      {'h4': '(b) Solution'},
      {'p': 'Find the intercepts of each constraint:'},
      {'table': {'align': 'lll', 'head': ['Constraint', 'When $x=0$', 'When $y=0$'], 'rows': [
        ['$4x + 2y = 400$', '$y = 200$', '$x = 100$'],
        ['$2x + 5y = 500$', '$y = 100$', '$x = 250$'],
      ]}},
      {'p': 'The two constraints intersect where both hold as equations. Multiply the second by '
            '2 and subtract:'},
      {'tex': '4x + 10y = 1{,}000'},
      {'tex': '4x + 2y = 400'},
      {'tex': '8y = 600 \\quad\\Rightarrow\\quad y = 75'},
      {'tex': '4x + 2(75) = 400 \\quad\\Rightarrow\\quad 4x = 250 \\quad\\Rightarrow\\quad '
              'x = 62.5'},
      {'p': 'Evaluate the objective function at every corner of the feasible region:'},
      {'table': {'align': 'lrr', 'head': ['Corner $(x, y)$', 'Working', 'Contribution (₦)'],
        'rows': [
        ['(0, 0)', '—', '0'],
        ['(100, 0)', '$40(100) + 50(0)$', '4,000'],
        ['(62.5, 75)', '$40(62.5) + 50(75)$', '**6,250**'],
        ['(0, 100)', '$40(0) + 50(100)$', '5,000'],
      ]}},
      {'p': 'The optimal plan is to make **62.5 units of X and 75 units of Y**, giving a maximum '
            'contribution of **₦6,250** for the month.'},
      {'p': 'Since half a unit of X may not be practicable, the company would either carry the '
            'part-finished unit into the next month as work in progress, or produce 62 units of '
            'X. At $x = 62$ the machining constraint permits $y = (400 - 248)/2 = 76$, and the '
            'finishing constraint permits $y = (500 - 124)/5 = 75.2$, so $y = 75$; contribution '
            'is then $40(62) + 50(75) = ₦6{,}230$ — ₦20 less. A strictly integer answer requires '
            'integer programming.'},
      {'h4': '(c) Slack'},
      {'p': 'At the optimum $(62.5,\\ 75)$:'},
      {'ul': [
        'Machining: $4(62.5) + 2(75) = 250 + 150 = 400$ hours used against 400 available — '
        '**nil slack**, the constraint is binding.',
        'Finishing: $2(62.5) + 5(75) = 125 + 375 = 500$ hours used against 500 available — '
        '**nil slack**, the constraint is binding.',
      ]},
      {'p': 'Both resources are fully utilised, which is characteristic of an optimum lying at '
            'the intersection of two constraints. Both therefore carry positive shadow prices, '
            'and the company would benefit from additional capacity in either — up to the point '
            'at which the optimum moves to a different vertex.'},
      {'h4': '(d) Assumptions'},
      {'ol': [
        '**Linearity.** Contribution per unit and resource usage per unit are constant '
        'regardless of volume. In practice bulk discounts, learning effects and overtime '
        'premiums all break this.',
        '**Certainty.** The contributions of ₦40 and ₦50 and the hours per unit are known '
        'exactly, and the 400 and 500 hours are firm. In reality they are estimates.',
        '**Divisibility.** Fractional units are permitted, which produced the 62.5 units of X '
        'above. Where output must be whole units this assumption fails.',
        '**Additivity and independence of the objective.** Total contribution is the sum of the '
        'contributions of the two products, with no joint effects, and the whole of production '
        'can be sold at the assumed prices.',
      ]}],
    'src': 'Chapter 15.1–15.4'},
  ]},
}
