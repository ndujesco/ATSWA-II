CH = {
 'n': 15,
 't': 'Linear Programming',
 'brief': 'Formulating a linear programme and solving it by the graphical method (two decision '
          'variables only), plus the concept of dual/shadow costs.',
 'outcomes': [
   'Understand the basic concepts of linear programming',
   'Know the meaning of objective function and constraints in linear programming',
   'Understand the concept of optimal solution to a linear programming problem',
   'Know the assumptions underlying linear programming',
   'Formulate linear programming problems',
   'Solve linear programming problems using the graphical method only',
   'Solve duality problems in LP',
 ],
 'secs': [
  {'n': '15.1', 't': 'Introduction and the nature of LP', 'b': [
    {'p': 'Linear programming is concerned with the use of scarce resources among various '
          'competing activities, in such a way as to maximise (or minimise) an outcome expressed '
          'as a given objective. It is concerned with optimising an objective function (e.g. to '
          'maximise profit or minimise cost) given constraints (e.g. machine hours, labour '
          'hours, quantity of materials). A linear programming problem therefore consists of an '
          'objective function and certain constraints based on limited resources.'},
    {'p': 'The allocation of scarce resources — machines, materials, men and money (the "4 '
          'M\'s"), or a combination of them — to competing activities is a decision managers and '
          'executive directors must take from time to time. The main objective is to use the '
          'limited resources to best advantage, which the linear programming model helps '
          'achieve.'},
  ]},

  {'n': '15.2', 't': 'Underlying assumptions', 'b': [
    {'p': 'There are **two** major assumptions:'},
    {'ol': [
      '**Linearity** of the objective function and the constraints. This guarantees the '
      '**additivity** and **divisibility** of the functions involved.',
      '**Non-negativity** of the decision variables — negative quantities of an activity are '
      'not possible.',
    ]},
    {'note': 'Linear programming consists of two words: the **linear** part, as above, and the '
             '**programming** part, which is the solution method.'},
  ]},

  {'n': '15.3', 't': 'Formulating and solving an LP problem', 'b': [
    {'h4': 'The processes of problem formulation'},
    {'ol': [
      'Define all variables and their units.',
      'Determine the objective of the problem — either to maximise or minimise the objective '
      'function.',
      'Express the objective function mathematically.',
      'Express each constraint mathematically, including the non-negativity constraints (the '
      'same for every LP problem). Constraints are always expressed as inequalities.',
    ]},
    {'h4': 'Methods of solving LP problems'},
    {'p': 'There are, generally, two methods: **graphical** and **simplex**. The graphical '
          'method applies only when a problem has **two decision variables**; the simplex method '
          'applies to two or more decision variables.'},
    {'warn': 'The simplex method is **beyond the scope of this study pack** — the syllabus '
             'examines the graphical method only, for problems in exactly two decision '
             'variables.'},
  ]},

  {'n': '15.4', 't': 'The graphical method', 'b': [
    {'steps': [
      'Turn the inequalities into equalities.',
      'Draw the lines representing the equations on the same axes.',
      'Identify the region where each constraint is satisfied.',
      'Identify the region where all the constraints are simultaneously satisfied — the '
      '**feasible region**.',
      'Find or read off the coordinates of the corner points of the boundary of the feasible '
      'region.',
      'Calculate the value of the objective function at each of those points, by substituting '
      'each pair of coordinates into it.',
      'Determine the optimal solution — the corner with the **highest** value of the objective '
      'function for a maximisation problem, or the **lowest** for a minimisation problem.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 15.1 — a first maximisation problem', 'open': True,
      'q': [
      {'p': 'Maximise $800x + 600y$ subject to $2x+y \\le 100$, $x+2y \\le 120$, $x,y \\ge 0$.'}],
      'a': [
      {'p': 'For $2x+y=100$: points $(0,100)$ and $(50,0)$. For $x+2y=120$: points $(0,60)$ '
            'and $(120,0)$.'},
      {'p': 'From the graph, the corner points of the feasible region are $A(0,60)$, '
            '$B(26,47)$, $C(50,0)$.'},
      {'table': {'align': 'lrr', 'head': ['Corner', 'Working', 'Value of $800x+600y$'], 'rows': [
        ['A(0, 60)', '800(0) + 600(60)', '36,000'],
        ['B(26, 47)', '800(26) + 600(47)', '**49,000**'],
        ['C(50, 0)', '800(50) + 600(0)', '40,000'],
      ]}},
      {'p': 'Corner $B(26,47)$ gives the highest value, so the optimal combination is $x=26$, '
            '$y=47$.'},
      {'note': 'Corner $B$ is the point of intersection of the two constraint lines and usually '
               'gives the optimal solution. Solved exactly (simultaneously), $l_1$ and $l_2$ '
               'intersect at $x=26\\tfrac23$, $y=46\\tfrac23$ — the whole-number corner read '
               'from the graph is a close approximation.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 15.2 — a production (maximisation) problem',
      'open': True, 'q': [
      {'p': 'AWOSOYE furniture produces executive and ordinary chairs on two machines MI and '
            'MII, with 100 and 120 hours available per week respectively. An executive chair '
            'needs 4 hours on MI and 3 on MII; an ordinary chair needs 1.25 hours on MI and 2 '
            'on MII. There is a standing order for 15 ordinary chairs a week. Contribution is '
            '¢2,500 per executive chair and ¢1,000 per ordinary chair. (a) Formulate the '
            'problem. (b) Solve it graphically.'}],
      'a': [
      {'p': 'Let $x$ = executive chairs, $y$ = ordinary chairs made per week; $P$ = total '
            'contribution.'},
      {'tex': '\\text{Maximise } P = 2500x + 1000y'},
      {'tex': '\\text{Subject to } 4x+1.25y\\le100 \\text{ (MI)}, \\quad 3x+2y\\le120 \\text{ '
              '(MII)}, \\quad y\\ge15 \\text{ (standing order)}, \\quad x\\ge0'},
      {'p': 'For $4x+1.25y=100$: $(0,80)$ and $(25,0)$. For $3x+2y=120$: $(0,60)$ and $(40,0)$. '
            'The feasible region has corners $A(0,60)$, $B(11.75,42.5)$, $C(20.25,15)$, '
            '$D(0,15)$.'},
      {'table': {'align': 'lrr', 'head': ['Corner', 'Working', 'Value of $2500x+1000y$'],
        'rows': [
        ['A(0, 60)', '2500(0) + 1000(60)', '60,000'],
        ['B(11.75, 42.5)', '2500(11.75) + 1000(42.5)', '**71,875**'],
        ['C(20.25, 15)', '2500(20.25) + 1000(15)', '65,625'],
        ['D(0, 15)', '2500(0) + 1000(15)', '15,000'],
      ]}},
      {'p': 'Corner $B$ gives the highest contribution, ¢71,875 — so the optimal plan is '
            'approximately **12 executive chairs and 43 ordinary chairs**.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 15.3 — a minimisation (mix) problem', 'open': True,
      'q': [
      {'p': 'A poultry farmer mixes feed ingredients F1 (₦200/kg: 200 units N1, 400 units N2, '
            '100 units N3) and F2 (₦250/kg: 200 units N1, 250 units N2, 200 units N3). Minimum '
            'daily needs are 14,000 units N1, 20,000 units N2, 10,000 units N3. (a) Formulate. '
            '(b) Solve graphically.'}],
      'a': [
      {'p': 'Let $x$ kg of F1, $y$ kg of F2 per day; $C$ = total daily cost.'},
      {'tex': '\\text{Minimise } C = 200x + 250y'},
      {'tex': '\\text{Subject to } 200x+200y\\ge14{,}000, \\quad 400x+250y\\ge20{,}000, \\quad '
              '100x+200y\\ge10{,}000, \\quad x,y\\ge0'},
      {'p': 'The feasible region has corners $A(0,80)$, $B(16,53)$, $C(38,31)$, $D(100,0)$.'},
      {'table': {'align': 'lrr', 'head': ['Corner', 'Working', 'Value of $200x+250y$'], 'rows': [
        ['A(0, 80)', '200(0) + 250(80)', '20,000'],
        ['B(16, 53)', '200(16) + 250(53)', '16,450'],
        ['C(38, 31)', '200(38) + 250(31)', '**15,350**'],
        ['D(100, 0)', '200(100) + 250(0)', '20,000'],
      ]}},
      {'p': 'Corner $C$ gives the lowest cost, so the optimal mix is **38 kg of F1 and 31 kg of '
            'F2**, at ₦15,350 per day.'}]}},
  ]},

  {'n': '15.5', 't': 'The concept of dual/shadow costs', 'b': [
    {'def': {'t': 'Shadow cost (shadow price, dual price)', 'd': 'the amount by which the '
             'objective function decreases (or increases) as a result of one unit less (or '
             'more) of a scarce resource being available. Only **binding constraints** — the '
             'two constraints that intersect at the optimal solution point — have shadow costs.'}},
    {'p': 'The solutions to the **dual** problem of the primal problem give the shadow costs '
          '(prices) — hence the alternative name **dual costs (prices)**. They help management '
          'carry out sensitivity analysis on the availability of scarce resources; indeed, '
          '**solving the dual problem is the same as carrying out sensitivity analysis.**'},
    {'h4': 'How to find a shadow cost (this study text\'s method)'},
    {'ol': [
      'Increase the right-hand side of the binding constraint by 1 unit, holding the other '
      'binding constraint unchanged.',
      'Solve the resulting pair of simultaneous equations for the new $x$ and $y$.',
      'Substitute the new $x, y$ into the objective function and compare with the original '
      'optimal value — the difference is the shadow cost of that resource.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 15.4 — formulating, solving and finding shadow '
      'costs', 'open': True, 'q': [
      {'p': 'ROYEJAS Sewing Institute produces shirts and blouses. A shirt contributes ₦800 and '
            'needs 2 units of materials and 1 hour of labour; a blouse contributes ₦600 and '
            'needs 1 unit of materials and 2 hours of labour. 100 units of materials and 120 '
            'labour hours are available weekly. (a) Formulate and solve. (b) Find the shadow '
            'cost of (i) a unit of materials, (ii) a labour hour. (c) Advise the Institute.'}],
      'a': [
      {'p': 'Let $x$ = shirts, $y$ = blouses per week.'},
      {'tex': '\\text{Maximise } 800x+600y \\text{ subject to } 2x+y\\le100 \\text{ (materials)}, '
              '\\quad x+2y\\le120 \\text{ (labour)}'},
      {'p': 'This is the same problem as Example 15.1, with optimal solution $(26,47)$ giving '
            'the highest contribution of **₦49,000** — i.e. 26 shirts and 47 blouses weekly.'},
      {'h4': '(b)(i) Shadow cost of a unit of materials'},
      {'p': 'Increase materials by 1, labour unchanged: $2x+y=101$, $x+2y=120$. Solving gives '
            '$x=27.33$, $y=46.34$.'},
      {'tex': '800(27.33) + 600(46.34) = 49{,}668'},
      {'p': 'Difference from the original ₦49,000 $=$ **₦668** — the shadow cost per unit of '
            'materials.'},
      {'h4': '(b)(ii) Shadow cost of a labour hour'},
      {'p': 'Increase labour by 1, materials unchanged: $2x+y=100$, $x+2y=121$. Solving gives '
            '$x=26.33$, $y=47.33$.'},
      {'tex': '800(26.33) + 600(47.33) = 49{,}466.67'},
      {'p': 'Difference from ₦49,000 $=$ **₦466.67** — the shadow cost per labour hour.'},
      {'h4': '(c) Advice'},
      {'p': 'The Institute should increase the units of materials rather than the hours of '
            'labour, since the resulting increase in contribution (₦668) is bigger than that '
            'from labour (₦466.67).'}]}},
  ]},

  {'n': '15.6', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§15.1–15.2** — LP allocates scarce resources among competing activities to optimise '
      'an objective. Two assumptions only: **linearity** (guarantees additivity and '
      'divisibility) and **non-negativity**.',
      '**§15.3** — formulation steps: define variables/units; decide maximise or minimise; '
      'express the objective mathematically; express constraints (with non-negativity) as '
      'inequalities. Two solution methods: **graphical** (2 variables only, examinable) and '
      '**simplex** (2+ variables, **beyond the scope of this study pack**).',
      '**§15.4 Graphical method** — plot each constraint as a line, shade the feasible side, '
      'find the feasible region, evaluate the objective at every corner, pick the best '
      '(highest for maximise, lowest for minimise).',
      '**§15.5 Dual/shadow costs** — only **binding** constraints have shadow costs. Found by '
      'increasing a binding constraint\'s RHS by 1, re-solving the simultaneous equations, and '
      'comparing the new optimum with the original — the difference is the shadow cost. Solving '
      'the dual problem = sensitivity analysis.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Linear programming** — allocating scarce resources among competing activities to '
      'maximise or minimise an objective.',
      '**Objective function** — the linear expression (e.g. profit, cost) being maximised or '
      'minimised.',
      '**Constraint** — a linear inequality expressing a limit on resources.',
      '**Non-negativity constraint** — $x,y\\ge0$; the same for every LP problem.',
      '**Feasible region** — where all constraints are simultaneously satisfied.',
      '**Optimal solution** — the corner point of the feasible region with the best objective '
      'value.',
      '**Binding constraint** — one of the (two) constraints intersecting at the optimal '
      'solution point.',
      '**Shadow cost (shadow/dual price)** — the change in the objective function from one '
      'more/fewer unit of a scarce (binding) resource.',
      '**Dual problem** — the companion LP problem whose solution gives the shadow costs of '
      'the (primal) original problem; a minimising primal has a maximising dual, and vice '
      'versa.',
    ]},
    {'h3': 'Graphical method, step by step'},
    {'ol': [
      'Turn each inequality into an equation and plot it.',
      'Shade the region satisfying each constraint.',
      'Identify the feasible region (all constraints satisfied together).',
      'Read off, or solve for, each corner point.',
      'Evaluate the objective function at every corner.',
      'Select the best value — highest (maximise) or lowest (minimise).',
    ]},
  ]},

  {'n': '15.7', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'The objective function for a minimisation LP problem is $500x+700y$, and the corner '
        'points of the feasible region are $(0,40)$, $(30,50)$ and $(60,0)$. The optimal '
        'solution is (A) 28,000  (B) 30,000  (C) $(60,0)$  (D) $(0,40)$  (E) $(30,50)$',
        'Linear programming can be applied only if the objective function and/or constraints '
        'are (A) Linear  (B) Non-linear  (C) Complex  (D) Independent functions  '
        '(E) Dependent functions',
        'Find $z$: Minimise $z=50x+60y$ subject to $2x+4y\\ge80$, $x+y\\ge30$, $x,y\\ge0$. '
        '(A) 2000  (B) 1600  (C) 1800  (D) 1400  (E) 1200',
        'If the original LP problem is a minimising one, what do we call the maximising one? '
        '(A) Shadow occurrence  (B) Dual formulation  (C) Simplex method  (D) Objective '
        'function  (E) Inequality constraint',
        'The region where all the constraints are simultaneously satisfied is called the '
        '(A) Equilibrium region  (B) Maximum profit region  (C) Feasible region  (D) Minimum '
        'profit region  (E) Break-even region',
        'Linear programming is concerned with the allocation of …………… to ……………….',
        'The solution to a linear programming problem is always at the ................ point '
        'of the boundary of the ............ region.',
        'Linear programming cannot be applied when there are more than two decision variables. '
        'Yes or No?',
        'If the primal problem of a linear programming is a minimising one, the dual problem '
        'will be a ……………',
        'The two major assumptions in linear programming are ..........of the objective '
        'function and ................of the decision variables.',
      ]}],
      'a': [
      {'p': '**1. D — (0, 40).** $500(0)+700(40)=28{,}000$; $500(30)+700(50)=50{,}000$; '
            '$500(60)+700(0)=30{,}000$. 28,000 is the least (minimisation).'},
      {'ol': [
        '**A — Linear.**',
        '**B — 1600.** Solving $2x+4y=80$ and $x+y=30$ simultaneously gives $x=20$, $y=10$, so '
        '$z=50(20)+60(10)=1{,}600$.',
        '**B — Dual formulation.**',
        '**C — Feasible region.**',
        '**Scarce resources, competing activities** (in that order).',
        '**Corner, feasible** (in that order).',
        '**No.**',
        '**Maximizing one.**',
        '**Linearity, non-negativity** (in that order).',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Objective function (maximise or minimise)',
   'tex': 'Z = c_1x_1 + c_2x_2'},
  {'lb': 'Constraint (general form)',
   'tex': 'a_1x_1 + a_2x_2 \\ \\{\\le, \\ge, =\\}\\ b'},
  {'lb': 'Non-negativity', 'tex': 'x_1, x_2 \\ge 0'},
  {'lb': 'Shadow cost of a binding resource',
   'tex': '\\text{Shadow cost} = Z^{*}_{\\text{new (RHS}+1)} - Z^{*}_{\\text{original}}'},
 ],
 'focus':
   'A frequent Section B question: formulate the problem, solve it graphically by evaluating '
   'every corner, then find one or two shadow costs by re-solving the binding constraints with '
   'the resource increased by one unit. The simplex method is explicitly outside this syllabus '
   '— only two-variable problems, solved graphically, are examined.',
 'errors': [
   'Failing to define the decision variables in words, with units.',
   'Omitting the non-negativity constraints.',
   'Reading corner coordinates off the graph by eye instead of solving the simultaneous '
   'equations.',
   'Testing only one or two corners rather than all of them.',
   'Trying to apply the simplex method — it is outside this syllabus; use the graphical method '
   'for a two-variable problem.',
   'Finding a shadow cost by any method other than re-solving the binding constraints with the '
   'RHS increased by one unit and comparing objective values.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In a linear programming problem, the optimal solution always occurs',
    'o': ['at the centre of the feasible region', 'at a corner point of the feasible region',
          'where all constraints are binding', 'at the origin',
          'where the objective function is zero'],
    'a': 1,
    'w': 'A linear objective attains its extreme value at a vertex of the feasible region; this '
         'is the whole basis of the graphical method.',
    'src': 'Chapter 15.4', 'sec': '15.4'},
   {'q': 'The graphical method of solving a linear programming problem is applicable only when '
         'the problem has',
    'o': ['one decision variable', 'two decision variables',
          'three or more decision variables', 'no constraints', 'only equality constraints'],
    'a': 1,
    'w': 'Beyond two decision variables, the (non-examinable) simplex method is required '
         'instead.',
    'src': 'Chapter 15.3', 'sec': '15.3'},
   {'q': 'Maximise $Z = 5x + 4y$ subject to $x + y \\le 10$, $x \\le 6$, $x, y \\ge 0$. The '
         'maximum value of $Z$ is',
    'o': ['40', '46', '50', '54', '30'],
    'a': 1,
    'w': 'Test the corners $(0,0)$, $(0,10)$, $(6,4)$ and $(6,0)$.',
    'calc': 'Z(6,4) = 5(6) + 4(4) = 30 + 16 = 46 \\quad\\text{against}\\quad Z(0,10) = 40',
    'src': 'Chapter 15.4', 'sec': '15.4'},
   {'q': 'Only the constraints that intersect at the optimal solution point have',
    'o': ['non-negativity', 'shadow costs', 'slack', 'a feasible region', 'integer solutions'],
    'a': 1,
    'w': 'These are the binding constraints, and only binding constraints carry a shadow cost.',
    'src': 'Chapter 15.5', 'sec': '15.5'},
   {'q': 'Which of the following is one of the two assumptions underlying linear programming, '
         'per the study text?',
    'o': ['Certainty of demand', 'Non-negativity of the decision variables',
          'Independence of the constraints', 'Integer solutions only',
          'A single binding constraint'],
    'a': 1,
    'w': 'The study text names exactly two assumptions: linearity of the objective/constraints '
         '(which itself guarantees additivity and divisibility), and non-negativity of the '
         'decision variables.',
    'src': 'Chapter 15.2', 'sec': '15.2'},
  ],
  'theory': [
   {'q': 'A firm produces two products, X and Y, with contributions of ₦800 and ₦600 per unit. '
         'X requires 2 units of a scarce material and 1 hour of labour; Y requires 1 unit of '
         'material and 2 hours of labour. 100 units of material and 120 labour hours are '
         'available weekly. (a) Formulate and solve the problem graphically. (b) Find the '
         'shadow cost of one extra unit of material.',
    'marks': 12,
    'a': [
      {'h4': '(a) Formulation and solution'},
      {'p': 'Let $x$ = units of X, $y$ = units of Y produced weekly.'},
      {'tex': '\\text{Maximise } 800x+600y \\text{ subject to } 2x+y\\le100, \\quad x+2y\\le120, '
              '\\quad x,y\\ge0'},
      {'p': 'The two constraints intersect at $x=26$, $y=47$ (approximately), which gives the '
            'highest contribution of the feasible corners:'},
      {'table': {'align': 'lrr', 'head': ['Corner', 'Working', 'Value'], 'rows': [
        ['(0, 60)', '800(0)+600(60)', '36,000'],
        ['(26, 47)', '800(26)+600(47)', '**49,000**'],
        ['(50, 0)', '800(50)+600(0)', '40,000'],
      ]}},
      {'p': 'Optimal plan: **26 units of X, 47 units of Y**, contribution **₦49,000**.'},
      {'h4': '(b) Shadow cost of material'},
      {'p': 'Increase the material constraint to 101 (labour unchanged): $2x+y=101$, '
            '$x+2y=120$, giving $x=27.33$, $y=46.34$.'},
      {'tex': '800(27.33)+600(46.34) = 49{,}668'},
      {'p': 'Shadow cost $= 49{,}668 - 49{,}000 = \\textbf{₦668}$ per extra unit of material.'}],
    'src': 'Chapter 15.4–15.5', 'sec': '15.4'},
  ]},
}
