CH = {
 'n': 19,
 't': 'Transportation and Assignment Models',
 'brief': 'The transportation problem — balanced vs unbalanced, and the three methods of '
          'finding an initial feasible solution (north-west corner, least cost, Vogel\'s '
          'approximation) — together with the assignment problem and the Hungarian method.',
 'outcomes': [
   'Know that the transportation problem is a special class of linear programming problem',
   'Understand the concept of balanced and unbalanced transportation models',
   'Obtain the initial basic feasible solution using the north-west corner rule, least cost '
   'method and Vogel\'s approximation method',
   'Apply the Hungarian method to solve assignment problems',
 ],
 'secs': [
  {'n': '19.1', 't': 'Introduction and the nature of the transportation model', 'b': [
    {'p': 'The **transportation problem** is a special class of linear programming problem in '
          'which the objective is to transport or distribute a single commodity from various '
          'sources/origins to different destinations at minimum total cost. Solving it involves '
          'identifying an **initial basic feasible solution** — the three methods for setting '
          'one up, plus the Hungarian method for the related assignment problem, are the subject '
          'of this chapter.'},
    {'table': {'align': 'lrrrrr', 'head': ['Origin', '1', '2', '3', '4', 'Supply'], 'rows': [
      ['1', '22', '19', '26', '22', '85'],
      ['2', '30', '27', '22', '28', '60'],
      ['3', '25', '23', '37', '24', '48'],
      ['Demand', '51', '72', '36', '34', '193'],
    ]}},
    {'note': 'A tableau like this — sources as rows, destinations as columns, unit cost in each '
             'cell, supply and demand in the margins — is the standard layout for every '
             'transportation problem in this chapter.'},
  ]},

  {'n': '19.2', 't': 'Balanced and unbalanced problems, involving a dummy', 'b': [
    {'p': 'A transportation problem is **balanced** if total quantity demanded at the '
          'destinations equals total quantity available at the origins; otherwise it is '
          '**unbalanced**. When it is not balanced, a **dummy** origin (row) or destination '
          '(column) is created, with **zero cost**, to absorb the difference between total '
          'supply and total demand and so create the balance.'},
    {'table': {'align': 'lrrrrr', 'head': ['Origin', '1', '2', '3', '4', 'Supply'], 'rows': [
      ['1', '18', '16', '20', '21', '40'],
      ['2', '16', '14', '16', '20', '60'],
      ['3', '20', '23', '21', '22', '40'],
      ['Dummy', '0', '0', '0', '0', '30'],
      ['Demand', '40', '80', '30', '20', '170'],
    ]}},
    {'p': 'Here, given total supply is 140 while total demand is 170, so a dummy row is created '
          'for the difference of 30 (as supply) at zero cost to balance the table. Solving a '
          'transportation problem means choosing a shipping programme that satisfies the '
          'destination and supply requirements at minimum total cost.'},
  ]},

  {'n': '19.3', 't': 'The three methods for the initial basic feasible solution', 'b': [
    {'p': 'The solution to a transportation problem has two phases: obtaining the **initial '
          'basic feasible solution** (this chapter\'s focus) and then obtaining the optimal '
          'solution. Three methods give the initial solution: the **North-West Corner Rule**, '
          'the **Least Cost Method** and **Vogel\'s Approximation (Penalty) Method**.'},
    {'p': 'Any of the three methods must satisfy two conditions to produce a valid initial basic '
          'feasible solution:'},
    {'ol': [
      'the problem must be balanced (as above); and',
      'the number of cells allocated must equal $m+n-1$, where $m$ and $n$ are the number of '
      'rows and columns respectively.',
    ]},
    {'def': {'t': 'Non-degenerate / degenerate solution', 'd': 'a solution satisfying both '
             'conditions above is a **non-degenerate initial basic feasible solution**; '
             'otherwise it is a **degenerate solution**.'}},
    {'h4': 'North-West Corner Rule (NWCR)'},
    {'p': 'The simplest but least efficient method — it has the highest total transportation '
          'cost of all the methods, because it never considers the cost of any route.'},
    {'ol': [
      'Allocate to the North-West (top-left) cell of the tableau the allowable minimum of the '
      'supply and demand capacities of that cell.',
      'If the allocation exhausts the supply (demand) of the first row (column), cross out that '
      'exhausted row (column) so no further allocation is made to it; move to the next cell and '
      'repeat step 1.',
      'Continue until exactly one row or column is left uncrossed; make the allowable allocation '
      'to it and stop.',
    ]},
    {'h4': 'Least Cost Method (LCM)'},
    {'p': 'A better method than NWCR because it does account for cost.'},
    {'ol': [
      'Assign as much as possible to the cell with the smallest unit cost (ties broken '
      'arbitrarily), subject to the allowable minimum of supply and demand.',
      'Cross out the exhausted row or column and adjust supply/demand; if both are exhausted at '
      'once, cross out only one, to avoid a degenerate solution.',
      'Look for the smallest cost among the remaining uncrossed cells and allocate; repeat until '
      'exactly one uncrossed row or column remains.',
    ]},
    {'h4': "Vogel's Approximation Method (VAM)"},
    {'p': 'Also called the Penalty method — an improvement on LCM using the **opportunity cost '
          '(penalty)** principle to minimise the cost of a poor allocation choice.'},
    {'ol': [
      'For each row (column), compute its **penalty**: the smallest unit cost subtracted from '
      'the next-smallest unit cost in that row (column).',
      'Select the row or column with the **highest** penalty, and allocate as much as possible '
      'to the cell of least cost within it (ties broken arbitrarily).',
      'Adjust supply/demand and cross out the exhausted row or column; if both are exhausted at '
      'once, cross out only one and assign zero supply (demand) to the other.',
      'Recompute penalties for the remaining uncrossed rows/columns and repeat from step 2.',
      'When exactly one row (column) remains uncrossed, allocate the leftover and stop.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 19.1 — all three methods on the same problem',
      'open': True, 'q': [
      {'p': 'SAO company has 3 plants (A, B, C) with monthly production capacity of 50, 60 and '
            '50 units respectively, to be distributed to 4 consumption points (X, Y, W, Z) with '
            'monthly demand of 50, 70, 30 and 10 respectively. Transportation cost (₦) per unit '
            'is:'},
      {'table': {'align': 'lrrrr', 'head': ['Plant', 'X', 'Y', 'W', 'Z'], 'rows': [
        ['A', '21', '18', '27', '22'], ['B', '19', '18', '24', '20'], ['C', '24', '25', '28', '25'],
      ]}},
      {'p': 'Obtain the initial basic feasible solution by (a) NWCR, (b) LCM, (c) VAM.'}],
      'a': [
      {'p': '**(a) NWCR.** Allocate A–X 50 (row A and column X exhausted); B–Y 60 (row B '
            'exhausted); C–Y 10 (column Y exhausted); C–W 30 (column W exhausted); C–Z 10.'},
      {'table': {'align': 'lrr', 'head': ['Cell', 'Units', 'Cost (₦)'], 'rows': [
        ['A–X', '50', '1,050'], ['B–Y', '60', '1,080'], ['C–Y', '10', '250'],
        ['C–W', '30', '840'], ['C–Z', '10', '250'],
        ['**Total**', '**160**', '**3,470**'],
      ]}},
      {'p': '**(b) LCM.** Lowest cost is A–Y (18): allocate 50 (row A exhausted, column Y '
            'balance 20). Next lowest among uncrossed is B–Y (18): allocate 20 (column Y '
            'exhausted, row B balance 40). Next is B–X (19): allocate 40 (row B exhausted, '
            'column X balance 10). Next is C–X (24): allocate 10 (column X exhausted). Left: '
            'C–W and C–Z, allocated 30 and 10.'},
      {'table': {'align': 'lrr', 'head': ['Cell', 'Units', 'Cost (₦)'], 'rows': [
        ['A–Y', '50', '900'], ['B–Y', '20', '360'], ['B–X', '40', '760'],
        ['C–X', '10', '240'], ['C–W', '30', '840'], ['C–Z', '10', '250'],
        ['**Total**', '**160**', '**3,350**'],
      ]}},
      {'p': '**(c) VAM.** Working through the penalty iterations gives the same allocation as '
            'LCM here: XA=50, XB=20, XB(further)=40, XC=10, XW=30, ZC=10.'},
      {'p': 'Total cost $=50(18)+40(19)+20(18)+10(24)+30(28)+10(25)=$ **₦3,350** — the same as '
            'LCM in this particular problem, both cheaper than NWCR\'s ₦3,470.'}]}},
    {'h4': 'Profit-maximisation problems in transportation'},
    {'p': 'If a **profit** table is given instead of a cost table, either of two approaches '
          'applies:'},
    {'ol': [
      'convert the profit table to a cost table by multiplying every entry by $-1$, apply all '
      'the usual steps, then multiply the resulting total by $-1$ to recover the total profit; '
      'or',
      'work directly on the profit table, allocating to the **highest**-profit cell each time '
      '(the mirror image of the least-cost method).',
    ]},
    {'p': 'Both the Least Cost and Vogel\'s Approximation methods are applicable either way.'},
  ]},

  {'n': '19.4', 't': 'Nature of the assignment model', 'b': [
    {'def': {'t': 'Assignment problem', 'd': 'a mathematical optimisation problem that deals '
             'with assigning tasks, projects, activities, resources or agents to specific '
             'jobs.'}},
    {'p': 'Its three main features:'},
    {'ol': [
      'its goal is to optimise an objective — minimising cost, or maximising profit/efficiency/'
      'performance;',
      'it recognises that the resources available for assignment are limited; and',
      'it recognises that a job is normally assigned to only one agent or resource.',
    ]},
    {'p': 'The assignment model is a **special case of the transportation problem** in which '
          'every source and destination capacity is equated to one; sources and destinations '
          'represent, respectively, jobs and tasks. Its mathematical form is:'},
    {'tex': '\\text{Min } Z = \\sum_{j=1}^{m}\\sum_{i=1}^{n} C_{ij}X_{ij}'},
    {'p': 'subject to:'},
    {'tex': '\\sum_{j} X_{ij} = 1, \\; i=1,2,\\ldots,n; \\qquad '
            '\\sum_{i} X_{ij} = 1, \\; j=1,2,\\ldots,n; \\qquad X_{ij}=0 \\text{ or } 1'},
    {'p': 'Application areas include: assigning various jobs to various machines; assigning '
          'tractors in different locations to trailers in different locations, to pick them up '
          'to a centralised depot; and matching operations in production for optimality.'},
  ]},

  {'n': '19.5', 't': 'The Hungarian method', 'b': [
    {'p': 'Assignment problems are usually solved by the **Hungarian Method**, also called the '
          '**Reduced Matrix Method**.'},
    {'ol': [
      'Ensure the cost table is **balanced** (rows $=$ columns); if not, add a dummy row or '
      'column of zero cost.',
      'Determine the **opportunity cost table**: subtract the lowest entry in each row from '
      'every entry in that row, then subtract the lowest entry in each resulting column from '
      'every entry in that column.',
      'Check for an optimal assignment: draw the minimum number of horizontal/vertical lines '
      'needed to cover every zero. If that number equals the number of rows (or columns), an '
      'optimal assignment exists and the process stops.',
      'If not optimal, modify the table: subtract the smallest uncovered number from every '
      'uncovered number, and add it to every number lying at the intersection of two lines.',
      'Return to step 3.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 19.3 — assigning programmers to packages',
      'open': True, 'q': [
      {'p': 'An organisation has 3 programmers to develop 3 application packages. Estimated '
            'computer time (hours) required is:'},
      {'table': {'align': 'lrrr', 'head': ['Package', 'A', 'B', 'C'], 'rows': [
        ['1', '110', '90', '70'], ['2', '70', '80', '100'], ['3', '100', '130', '110'],
      ]}},
      {'p': 'Obtain the optimal assignment minimising total time.'}],
      'a': [
      {'p': 'Row minima are 70, 70, 100; column reduction of that table then gives:'},
      {'table': {'align': 'lrrr', 'head': ['', 'A', 'B', 'C'], 'rows': [
        ['1', '40', '10', '0'], ['2', '0', '0', '30'], ['3', '0', '20', '10'],
      ]}},
      {'p': 'Only 3 lines are needed to cover every zero, so this is already optimal: '
            '**Package 1 → C, Package 2 → B, Package 3 → A**.'},
      {'tex': '\\text{Total time} = 70 + 80 + 100 = 250 \\text{ hours}'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 19.4 — assigning jobs to machines', 'open': True,
      'q': [
      {'p': 'Obtain the optimal assignment for the following cost table (₦\'000):'},
      {'table': {'align': 'lrrr', 'head': ['Job', 'X', 'Y', 'Z'], 'rows': [
        ['A', '40', '46', '50'], ['B', '30', '35', '39'], ['C', '37', '34', '32'],
      ]}}],
      'a': [
      {'p': 'Row reduction (minima 40, 30, 32), then column reduction gives:'},
      {'table': {'align': 'lrrr', 'head': ['Job', 'X', 'Y', 'Z'], 'rows': [
        ['A', '0', '4', '10'], ['B', '0', '3', '9'], ['C', '5', '0', '0'],
      ]}},
      {'p': 'Job A → X, Job B → Y, Job C → Z (3 lines cover all zeros — already optimal).'},
      {'tex': '\\text{Total cost} = 40 + 35 + 32 = ₦107,000'}]}},
    {'note': 'For a **profit** matrix, multiply every entry by $-1$ to convert it to a cost '
             'matrix, then apply all the steps above as normal.'},
    {'eg': {'t': 'The Hungarian method with a revision step', 'q': [
      {'p': 'Four workers are to be assigned to four jobs. The cost in ₦\'000 of each worker '
            'doing each job is:'},
      {'table': {'align': 'lrrrr',
        'head': ['Worker', 'J1', 'J2', 'J3', 'J4'], 'rows': [
        ['W1', '20', '25', '22', '28'],
        ['W2', '15', '18', '23', '17'],
        ['W3', '19', '17', '21', '24'],
        ['W4', '25', '23', '24', '24'],
      ]}},
      {'p': 'Determine the assignment that minimises total cost.'}],
      'a': [
      {'h4': 'Step 1 — row reduction'},
      {'p': 'Row minima are 20, 15, 17 and 23:'},
      {'table': {'align': 'lrrrr', 'head': ['', 'J1', 'J2', 'J3', 'J4'], 'rows': [
        ['W1', '0', '5', '2', '8'],
        ['W2', '0', '3', '8', '2'],
        ['W3', '2', '0', '4', '7'],
        ['W4', '2', '0', '1', '1'],
      ]}},
      {'h4': 'Step 2 — column reduction'},
      {'p': 'Column minima are 0, 0, 1 and 1:'},
      {'table': {'align': 'lrrrr', 'head': ['', 'J1', 'J2', 'J3', 'J4'], 'rows': [
        ['W1', '0', '5', '1', '7'],
        ['W2', '0', '3', '7', '1'],
        ['W3', '2', '0', '3', '6'],
        ['W4', '2', '0', '0', '0'],
      ]}},
      {'h4': 'Step 3 — cover the zeros'},
      {'p': 'The zeros can be covered by three lines: column J1, column J2, and row W4. Three '
            'lines is fewer than four rows, so the solution is not yet optimal.'},
      {'h4': 'Step 4 — revise'},
      {'p': 'The uncovered elements are rows W1–W3 in columns J3 and J4. The smallest is '
            '**1**. Subtract 1 from every uncovered element and add 1 to the two elements at '
            'line intersections (row W4, columns J1 and J2):'},
      {'table': {'align': 'lrrrr', 'head': ['', 'J1', 'J2', 'J3', 'J4'], 'rows': [
        ['W1', '0', '5', '0', '6'],
        ['W2', '0', '3', '6', '0'],
        ['W3', '2', '0', '2', '5'],
        ['W4', '3', '1', '0', '0'],
      ]}},
      {'p': 'Four lines are now required to cover all the zeros, so an optimal assignment '
            'exists.'},
      {'h4': 'Step 5 — assign'},
      {'p': 'W3 has only one zero, at J2, so **W3 → J2**. This leaves W1 with zeros at J1 and '
            'J3, W2 at J1 and J4, W4 at J3 and J4. Taking **W1 → J3** forces **W4 → J4** and '
            'hence **W2 → J1**.'},
      {'table': {'align': 'llr', 'head': ['Worker', 'Job', 'Cost (₦\'000)'], 'rows': [
        ['W1', 'J3', '22'], ['W2', 'J1', '15'], ['W3', 'J2', '17'], ['W4', 'J4', '24'],
        ['**Total**', '', '**78**'],
      ]}},
      {'note': 'There is a second optimal assignment at the same cost: W1→J1 (20), W2→J4 (17), '
               'W3→J2 (17), W4→J3 (24), also ₦78,000 — alternative optima are common in '
               'assignment problems and are a legitimate answer.'}]}},
  ]},

  {'n': '19.6', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§19.1–19.2 The model** — ship a single commodity from sources to destinations at '
      'least cost; **balanced** when total supply $=$ total demand, otherwise add a zero-cost '
      'dummy row/column for the difference.',
      '**§19.3 Initial basic feasible solution** — needs a balanced table and $m+n-1$ occupied '
      'cells (**non-degenerate**; fewer is **degenerate**). **NWCR**: top-left cell first, '
      'ignores cost, worst of the three. **LCM**: cheapest cell each time, better but '
      'short-sighted. **VAM**: allocate to the cheapest cell in the row/column with the '
      '**largest penalty** (difference between the two lowest remaining costs there); '
      'penalties are recomputed after every deletion. For a **profit** table, convert by '
      '$\\times(-1)$ then minimise (or allocate to the highest profit directly).',
      '**§19.4 Assignment model** — a special transportation problem with every supply/demand '
      '$=1$; solved by the **Hungarian method**.',
      '**§19.5 Hungarian method** — balance the table; row-reduce, then column-reduce; cover '
      'all zeros with the minimum number of lines; if lines $=$ rows, optimal — assign on the '
      'zeros; otherwise subtract the smallest uncovered value from uncovered cells and add it '
      'at line intersections, then recheck. A profit matrix is converted by $\\times(-1)$ '
      'first.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Balanced problem** — total supply $=$ total demand.',
      '**Dummy row/column** — a zero-cost row or column added to balance an unbalanced problem.',
      '**Non-degenerate solution** — occupied cells $=m+n-1$; fewer is **degenerate**.',
      '**Initial basic feasible solution** — a starting allocation from NWCR, LCM or VAM.',
      '**Penalty (VAM)** — the difference between the two lowest costs still available in a '
      'row/column.',
      '**Assignment problem** — a special transportation problem: $n$ jobs to $n$ agents, one '
      'each.',
      '**Hungarian (Reduced Matrix) Method** — row/column reduction, line-covering and revision '
      'to reach an optimal assignment.',
    ]},
    {'h3': 'Formulas'},
    {'fbox': {'h': 'Transportation and assignment', 'rows': [
      {'lb': 'Balanced condition', 'tex': '\\sum_i a_i = \\sum_j b_j'},
      {'lb': 'Non-degeneracy', 'tex': '\\text{occupied cells} = m+n-1'},
      {'lb': 'VAM penalty', 'tex': '\\text{penalty} = c_{(2)} - c_{(1)}'},
      {'lb': 'Assignment objective',
       'tex': '\\text{Min } Z = \\sum_{j=1}^{m}\\sum_{i=1}^{n} C_{ij}X_{ij}'},
      {'lb': 'Assignment constraints',
       'tex': '\\sum_j X_{ij}=1, \\ \\sum_i X_{ij}=1, \\ X_{ij}\\in\\{0,1\\}'},
      {'lb': 'Profit → cost conversion', 'tex': "C'_{ij} = -C_{ij}"},
    ]}},
  ]},

  {'n': '19.7', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'The main objective of a transportation problem is to (A) Transport goods to the '
        'supply points (B) Allocate goods to people (C) Distribute a single good from various '
        'sources to different destinations at minimum total cost (D) Sell goods to consumers '
        '(E) Bring goods nearer to the people',
        'Which of the following is NOT a method of obtaining the initial feasible solution of '
        'a transportation problem? (A) NWCR (B) Least Cost Method (C) Vogel\'s Approximation '
        'Method (D) Inventory control (E) Simplex Method',
        'Least Cost Method is better than NWCR because it is (A) Faster in computation and '
        'allocation (B) Concerned with handling of computation and allocation (C) Straight '
        'forward for allocation and computation (D) Needed for cost for allocation and '
        'computation (E) Having fewer iterations',
        'The "real condition" in a transportation problem (A) Is the addition of a dummy to '
        'destination or source (B) Means total demand equals total supply (C) Means shipment '
        'to a dummy source represents surplus (D) Means all of the above (E) Is the absence of '
        'a dummy',
        'Supply capacities $a_1=120,a_2=70,a_3=60,a_4=80$; demand capacities '
        '$b_1=120,b_2=70,b_3=90,b_4=110$. Determine the dummy capacity to add. (A) 60 dummy '
        'for supply (B) 60 dummy for demand (C) 70 dummy for supply (D) 70 dummy for demand '
        '(E) 50 dummy for supply',
      ]},
      {'p': 'Short answer:'},
      {'ol': [
        'The major difference between LCM and VAM is that VAM uses ……… costs.',
        'If $m$ and $n$ are numbers of origins and destinations, cell allocations not equal to '
        '$m+n-1$ leads to a ……… solution.',
        'The necessary condition for a transportation problem to be solvable is that it must '
        'be ……….',
        'Solution to a typical transportation problem involves ……… phases.',
      ]}],
      'a': [
      {'ol': [
        '**C.**', '**D.**', '**D.**', '**B.**',
        '**A** — total supply $=120+70+60+80=330$; total demand $=120+70+90+110=390$; demand '
        'exceeds supply by 60, so a dummy of 60 is added for **supply (source)**.',
      ]},
      {'ol': [
        '**Penalty or opportunity** costs.',
        '**Degenerate.**',
        '**Balanced.**',
        '**Two.**',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Balanced condition', 'tex': '\\sum_{i} a_i = \\sum_{j} b_j'},
  {'lb': 'Non-degeneracy condition', 'tex': '\\text{Occupied cells} = m + n - 1'},
  {'lb': 'Vogel penalty', 'tex': '\\text{Penalty} = c_{(2)} - c_{(1)}'},
  {'lb': 'Assignment: objective', 'tex': '\\text{Min } Z = \\sum_{j}\\sum_{i} C_{ij}X_{ij}'},
  {'lb': 'Assignment: constraints',
   'tex': '\\sum_j X_{ij}=1, \\ \\sum_i X_{ij}=1, \\ X_{ij}\\in\\{0,1\\}'},
  {'lb': 'Assignment: profit to cost conversion', 'tex': "C'_{ij} = -C_{ij}"},
 ],
 'focus':
   'Transportation appears in Section B fairly often, almost always asking for an initial '
   'solution by one or more named methods. Assignment by the Hungarian method appears rather '
   'less often. Both are procedural: the marks go to the tableau at each stage, so show every '
   'intermediate table rather than only the final answer. Note that the study text stops at the '
   'initial solution — optimality-testing methods beyond that are not part of this syllabus.',
 'errors': [
   'Failing to check whether the problem is balanced, and omitting the dummy row or column.',
   'Carrying forward Vogel penalties instead of recomputing them after each deletion.',
   'In VAM, allocating to the cell with the largest penalty rather than to the cheapest cell in '
   'the row or column with the largest penalty.',
   'Deleting both the row and the column when an allocation exhausts only one of them.',
   'In the Hungarian method, revising the matrix before checking whether the minimum number of '
   'covering lines already equals the number of rows.',
   'Adding the reduced-matrix values to obtain the total cost instead of reading the original '
   'costs.',
   'Forgetting to convert a maximisation (profit) problem before applying the standard steps.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A transportation problem is said to be balanced when',
    'o': ['the number of sources equals the number of destinations',
          'total supply equals total demand',
          'all transportation costs are equal',
          'the number of occupied cells equals $m + n - 1$',
          'no dummy row or column is required'],
    'a': 1,
    'w': 'Balance concerns quantities, not the size of the matrix. An unbalanced problem is '
         'made balanced by adding a dummy row or column at zero cost.',
    'src': 'Chapter 19.2', 'sec': '19.2'},
   {'q': 'In a transportation problem with 4 sources and 5 destinations, a non-degenerate '
         'solution has',
    'o': ['9 occupied cells', '8 occupied cells', '20 occupied cells', '5 occupied cells',
          '4 occupied cells'],
    'a': 1,
    'w': 'The condition is $m + n - 1$ occupied cells.',
    'calc': 'm + n - 1 = 4 + 5 - 1 = 8',
    'src': 'Chapter 19.3', 'sec': '19.3'},
   {'q': "In Vogel's approximation method, the penalty for a row is",
    'o': ['the smallest cost in the row',
          'the difference between the two smallest costs in the row',
          'the difference between the largest and smallest costs in the row',
          'the average cost in the row', 'the sum of the costs in the row'],
    'a': 1,
    'w': 'The penalty measures the extra cost that would be incurred if the cheapest route in '
         'that row were not used.',
    'src': 'Chapter 19.3', 'sec': '19.3'},
   {'q': 'The north-west corner rule',
    'o': ['always produces the optimal solution',
          'ignores the transportation costs entirely',
          'requires the problem to be unbalanced',
          'is used only for assignment problems',
          "produces the same answer as Vogel's method"],
    'a': 1,
    'w': 'It allocates purely by position in the tableau, which is why it is quick to apply but '
         'generally gives the most expensive of the three initial solutions.',
    'src': 'Chapter 19.3', 'sec': '19.3'},
   {'q': 'In the Hungarian method, an optimal assignment has been reached when the minimum '
         'number of lines needed to cover all the zeros',
    'o': ['is less than the number of rows', 'equals the number of rows',
          'exceeds the number of rows', 'is zero', 'equals the number of zeros'],
    'a': 1,
    'w': 'When the covering lines equal the order of the matrix, an independent zero can be '
         'chosen in every row and column.',
    'src': 'Chapter 19.5', 'sec': '19.5'},
   {'q': 'An assignment problem in which the objective is to maximise profit is solved by',
    'o': ['maximising each row in turn',
          'multiplying every element by $-1$ and then minimising',
          'adding the largest element to every cell',
          'reversing the sign of each element and applying the north-west corner rule',
          'using the transportation method instead'],
    'a': 1,
    'w': 'Converting the profit matrix to a cost matrix by multiplying by $-1$ turns the '
         'problem into a standard minimisation, which the Hungarian method then solves.',
    'src': 'Chapter 19.5', 'sec': '19.5'},
  ],
  'theory': [
   {'q': 'Distinguish between the transportation problem and the assignment problem. Explain '
         'the north-west corner rule, the least-cost method and Vogel\'s approximation method '
         'for obtaining an initial feasible solution to a transportation problem.',
    'marks': 12,
    'a': [
      {'h4': 'Transportation and assignment compared'},
      {'p': 'The assignment problem is a special case of the transportation problem, in which '
            'every source and destination capacity is equated to one.'},
      {'table': {'align': 'lll', 'head': ['', 'Transportation', 'Assignment'], 'rows': [
        ['Purpose', 'Ship a commodity from sources to destinations at least cost',
         'Allocate $n$ jobs to $n$ agents, one each, at least cost'],
        ['Supplies and demands', 'Any quantities, subject to balance',
         'Every supply and every demand equals one'],
        ['Solution method', 'NWCR, LCM or VAM for the initial solution', 'Hungarian method'],
      ]}},
      {'h4': 'North-West Corner Rule'},
      {'p': 'Allocate to the top-left cell the allowable minimum of supply and demand; cross '
            'out the exhausted row or column; move to the next cell and repeat, until one row '
            'or column remains. It ignores cost entirely, so it is quick but usually gives the '
            'most expensive initial solution of the three.'},
      {'h4': 'Least Cost Method'},
      {'p': 'Allocate as much as possible to the cell of smallest unit cost each time, crossing '
            'out the exhausted row/column and repeating. It uses cost information, so it is '
            'generally better than NWCR, but it is short-sighted since it never looks beyond '
            'the immediate cheapest cell.'},
      {'h4': "Vogel's Approximation Method"},
      {'p': 'For each row/column, compute the penalty (the difference between the two lowest '
            'costs available in it); allocate to the cheapest cell in the row/column with the '
            'largest penalty; recompute penalties and repeat. VAM is generally the best of the '
            'three, since the penalty is a look-ahead measure of the cost of not using the '
            'cheapest route.'}],
    'src': 'Chapter 19.2–19.3', 'sec': '19.3'},
  ]},
}
