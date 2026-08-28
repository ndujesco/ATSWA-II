CH = {
 'n': 19,
 't': 'Transportation and Assignment',
 'brief': 'The transportation problem and the three methods of finding an initial feasible '
          'solution — north-west corner, least cost and Vogel\'s approximation — together with '
          'the assignment problem and the Hungarian method.',
 'outcomes': [
   'Set up a transportation tableau and check whether it is balanced',
   'Find an initial feasible solution by the north-west corner rule',
   'Find an initial feasible solution by the least-cost method',
   'Apply Vogel\'s approximation method and explain why it is superior',
   'Handle unbalanced problems with a dummy row or column',
   'Solve an assignment problem by the Hungarian method',
 ],
 'secs': [
  {'n': '19.1', 't': 'The transportation problem', 'b': [
    {'p': 'A commodity is available at several **sources** (factories, warehouses) in known '
          'quantities and required at several **destinations** (depots, customers) in known '
          'quantities. The cost of moving one unit from each source to each destination is '
          'known. The problem is to determine the schedule that satisfies all requirements at '
          'least total cost.'},
    {'ul': [
      'A problem is **balanced** when total supply equals total demand. Only a balanced problem '
      'can be solved directly.',
      'If supply exceeds demand, add a **dummy destination** with a requirement equal to the '
      'excess and zero transport costs; the amount allocated to it is the quantity left in '
      'store.',
      'If demand exceeds supply, add a **dummy source** with zero costs; allocations from it '
      'represent unsatisfied demand.',
      'A solution is **non-degenerate** when the number of occupied cells equals '
      '$m + n - 1$, where $m$ is the number of sources and $n$ the number of destinations. '
      'Fewer occupied cells means the solution is **degenerate** and cannot be tested for '
      'optimality without inserting a nominal zero allocation.',
    ]},
    {'note': 'Every method in this chapter produces an **initial feasible solution**. Testing '
             'it for optimality requires a further step (the stepping-stone or MODI method), '
             'which is outside the Part II syllabus. What is examined is the construction of '
             'the initial solution and the comparison of the three methods.'},
  ]},

  {'n': '19.2', 't': 'Finding an initial solution', 'b': [
    {'p': 'The three methods are applied to the same problem below. In each, an allocation '
          'exhausts either a row or a column, which is then closed and ignored thereafter.'},
    {'h4': 'The data'},
    {'table': {'align': 'lrrrr',
      'head': ['From \\ To', 'X', 'Y', 'Z', 'Supply'], 'rows': [
      ['A', '8', '6', '10', '30'],
      ['B', '9', '12', '13', '40'],
      ['C', '14', '9', '16', '30'],
      ['Demand', '35', '25', '40', '100'],
    ]}},
    {'p': 'Total supply (100) equals total demand (100), so the problem is balanced. Costs are '
          'in naira per unit.'},

    {'h4': '19.2.1  North-west corner rule'},
    {'p': 'Begin at the top-left cell and allocate as much as possible; move right if the row '
          'is exhausted, down if the column is exhausted. The rule ignores costs entirely, so '
          'it is quick but usually poor.'},
    {'table': {'align': 'llrr',
      'head': ['Step', 'Cell', 'Units', 'Cost (₦)'], 'rows': [
      ['1', 'A–X', '30', '240'],
      ['2', 'B–X', '5', '45'],
      ['3', 'B–Y', '25', '300'],
      ['4', 'B–Z', '10', '130'],
      ['5', 'C–Z', '30', '480'],
      ['**Total**', '', '**100**', '**1,195**'],
    ]}},

    {'h4': '19.2.2  Least-cost method'},
    {'p': 'Allocate as much as possible to the cheapest cell available, then to the next '
          'cheapest, and so on. It uses cost information but only one cell at a time.'},
    {'table': {'align': 'llrrl',
      'head': ['Step', 'Cell', 'Unit cost (₦)', 'Units', 'Cost (₦)'], 'rows': [
      ['1', 'A–Y', '6', '25', '150'],
      ['2', 'A–X', '8', '5', '40'],
      ['3', 'B–X', '9', '30', '270'],
      ['4', 'B–Z', '13', '10', '130'],
      ['5', 'C–Z', '16', '30', '480'],
      ['**Total**', '', '', '**100**', '**1,070**'],
    ]}},
    {'p': 'Better than the north-west corner rule by ₦125, because it takes the cheap A–Y route '
          'first.'},

    {'h4': "19.2.3  Vogel's approximation method (VAM)"},
    {'p': 'For each row and column compute a **penalty**: the difference between the two '
          'cheapest costs still available in it. This is the extra cost incurred if the '
          'cheapest route is *not* used. Allocate to the cheapest cell in the row or column '
          'with the **largest** penalty, then recompute.'},
    {'steps': [
      'Compute the penalty for every row and column.',
      'Select the row or column with the largest penalty (break ties arbitrarily, or by the '
      'lower cost).',
      'Allocate as much as possible to the lowest-cost cell in that row or column.',
      'Delete the row or column that is now exhausted and recompute the penalties for what '
      'remains.',
      'Repeat until all supplies and demands are met.',
    ]},
    {'table': {'align': 'llll',
      'head': ['Iteration', 'Penalties', 'Largest', 'Allocation'], 'rows': [
      ['1', 'Rows A 2, B 3, C 5; Columns X 1, Y 3, Z 3', 'Row C (5)',
       'Cheapest in C is Y at 9 → allocate 25; Y is exhausted'],
      ['2', 'Rows A 2, B 4, C 2; Columns X 1, Z 3', 'Row B (4)',
       'Cheapest in B is X at 9 → allocate 35; X is exhausted'],
      ['3', 'Only Z remains', '—', 'A 30, B 5, C 5 to Z'],
    ]}},
    {'table': {'align': 'llrrl',
      'head': ['', 'Cell', 'Unit cost (₦)', 'Units', 'Cost (₦)'], 'rows': [
      ['', 'C–Y', '9', '25', '225'],
      ['', 'B–X', '9', '35', '315'],
      ['', 'A–Z', '10', '30', '300'],
      ['', 'B–Z', '13', '5', '65'],
      ['', 'C–Z', '16', '5', '80'],
      ['**Total**', '', '', '**100**', '**985**'],
    ]}},
    {'key': 'VAM gives ₦985 against ₦1,070 for least cost and ₦1,195 for the north-west corner '
            'rule — a saving of 18% on the worst method. VAM is superior because the penalty '
            'looks ahead: it asks not "which cell is cheapest?" but "which route, if missed, '
            'would cost us most?". Its solution is frequently optimal or very close to it, and '
            'it is the method to use unless a question specifies otherwise.'},
    {'warn': 'A penalty is the difference between the two cheapest **remaining** costs in that '
             'row or column. Once a row or column is deleted, penalties must be recomputed from '
             'what is left — carrying forward the original penalties is the standard error.'},
  ]},

  {'n': '19.3', 't': 'The assignment problem', 'b': [
    {'p': 'The assignment problem is a special transportation problem in which every supply and '
          'every demand equals one: $n$ jobs are to be allocated to $n$ workers, one job to '
          'each worker, so as to minimise total cost or time. It is solved by the **Hungarian '
          'method**.'},
    {'steps': [
      '**Row reduction.** Subtract the smallest element in each row from every element of that '
      'row.',
      '**Column reduction.** In the resulting matrix, subtract the smallest element in each '
      'column from every element of that column. Every row and column now contains at least one '
      'zero.',
      '**Cover the zeros** with the minimum possible number of horizontal and vertical lines.',
      'If the number of lines equals the number of rows, an optimal assignment exists — go to '
      'step 6. Otherwise continue.',
      '**Revise the matrix.** Find the smallest uncovered element; subtract it from every '
      'uncovered element and add it to every element covered twice (at a line intersection). '
      'Return to step 3.',
      '**Make the assignment.** Select zeros so that exactly one is chosen in each row and each '
      'column, starting with any row or column containing only one zero. Read the total cost '
      'from the original matrix.',
    ]},
    {'ul': [
      'For a **maximisation** problem (profit, output), convert to minimisation first by '
      'subtracting every element from the largest element in the matrix, then proceed normally.',
      'An **unbalanced** problem (more jobs than workers, or the reverse) requires a dummy row '
      'or column of zeros.',
      'A **prohibited** assignment is given a very large cost, conventionally $M$, so that the '
      'algorithm never selects it.',
    ]},
    {'eg': {'t': 'Hungarian method', 'q': [
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
      {'p': 'The uncovered elements are rows W1–W3 in columns J3 and J4: 1, 7, 7, 1, 3, 6. The '
            'smallest is **1**. Subtract 1 from every uncovered element and add 1 to the two '
            'elements covered twice (row W4 in columns J1 and J2):'},
      {'table': {'align': 'lrrrr', 'head': ['', 'J1', 'J2', 'J3', 'J4'], 'rows': [
        ['W1', '0', '5', '0', '6'],
        ['W2', '0', '3', '6', '0'],
        ['W3', '2', '0', '2', '5'],
        ['W4', '3', '1', '0', '0'],
      ]}},
      {'p': 'Four lines are now required to cover all the zeros, so an optimal assignment '
            'exists.'},
      {'h4': 'Step 5 — assign'},
      {'p': 'W3 has only one zero, at J2, so **W3 → J2**. Column J2 is now closed, which leaves '
            'W1 with zeros at J1 and J3, W2 at J1 and J4, and W4 at J3 and J4. Taking '
            '**W1 → J3** forces **W4 → J4** and hence **W2 → J1**.'},
      {'table': {'align': 'llr', 'head': ['Worker', 'Job', 'Cost (₦\'000)'], 'rows': [
        ['W1', 'J3', '22'],
        ['W2', 'J1', '15'],
        ['W3', 'J2', '17'],
        ['W4', 'J4', '24'],
        ['**Total**', '', '**78**'],
      ]}},
      {'p': 'The minimum total cost is **₦78,000**.'},
      {'note': 'There is a second optimal assignment at the same cost: W1 → J1 (20), '
               'W2 → J4 (17), W3 → J2 (17), W4 → J3 (24), also ₦78,000. Alternative optima are '
               'common in assignment problems and are a legitimate answer — say so, and let '
               'non-cost factors such as skill or preference decide between them.'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Balanced condition',
   'tex': '\\sum_{i} a_i = \\sum_{j} b_j'},
  {'lb': 'Total transportation cost',
   'tex': 'Z = \\sum_{i}\\sum_{j} c_{ij}\\, x_{ij}'},
  {'lb': 'Non-degeneracy condition',
   'tex': '\\text{Occupied cells} = m + n - 1'},
  {'lb': 'Vogel penalty',
   'tex': '\\text{Penalty} = c_{(2)} - c_{(1)}'},
  {'lb': 'Assignment: conversion to minimisation',
   'tex': "c'_{ij} = c_{\\max} - c_{ij}"},
 ],
 'focus':
   'Transportation appears in Section B in roughly one diet in three, almost always asking for '
   'an initial solution by one or two named methods and a comparison of them. Assignment by the '
   'Hungarian method appears rather less often. Both are procedural: the marks go to the '
   'tableau at each stage, so show every intermediate table rather than only the final answer.',
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
   'Forgetting to convert a maximisation assignment problem to a minimisation one first.',
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
    'src': 'Chapter 19.1'},
   {'q': 'In a transportation problem with 4 sources and 5 destinations, a non-degenerate '
         'solution has',
    'o': ['9 occupied cells', '8 occupied cells', '20 occupied cells', '5 occupied cells',
          '4 occupied cells'],
    'a': 1,
    'w': 'The condition is $m + n - 1$ occupied cells.',
    'calc': 'm + n - 1 = 4 + 5 - 1 = 8',
    'src': 'Chapter 19.1'},
   {'q': "In Vogel's approximation method, the penalty for a row is",
    'o': ['the smallest cost in the row',
          'the difference between the two smallest costs in the row',
          'the difference between the largest and smallest costs in the row',
          'the average cost in the row', 'the sum of the costs in the row'],
    'a': 1,
    'w': 'The penalty measures the extra cost that would be incurred if the cheapest route in '
         'that row were not used.',
    'src': 'Chapter 19.2'},
   {'q': 'The north-west corner rule',
    'o': ['always produces the optimal solution',
          'ignores the transportation costs entirely',
          'requires the problem to be unbalanced',
          'is used only for assignment problems',
          'produces the same answer as Vogel\'s method'],
    'a': 1,
    'w': 'It allocates purely by position in the tableau, which is why it is quick to apply but '
         'generally gives the most expensive of the three initial solutions.',
    'src': 'Chapter 19.2'},
   {'q': 'In the Hungarian method, an optimal assignment has been reached when the minimum '
         'number of lines needed to cover all the zeros',
    'o': ['is less than the number of rows', 'equals the number of rows',
          'exceeds the number of rows', 'is zero', 'equals the number of zeros'],
    'a': 1,
    'w': 'When the covering lines equal the order of the matrix, an independent zero can be '
         'chosen in every row and column.',
    'src': 'Chapter 19.3'},
   {'q': 'An assignment problem in which the objective is to maximise profit is solved by',
    'o': ['maximising each row in turn',
          'subtracting every element from the largest element and then minimising',
          'adding the largest element to every cell',
          'reversing the sign of each element and applying the north-west corner rule',
          'using the transportation method instead'],
    'a': 1,
    'w': 'Converting to a regret or opportunity-loss matrix turns the problem into a standard '
         'minimisation, which the Hungarian method then solves.',
    'src': 'Chapter 19.3'},
  ],
  'theory': [
   {'q': 'Distinguish between the transportation problem and the assignment problem. Explain '
         'the north-west corner rule, the least-cost method and Vogel\'s approximation method '
         'for obtaining an initial feasible solution to a transportation problem, and state '
         'which is to be preferred and why.',
    'marks': 12,
    'a': [
      {'h4': 'Transportation and assignment compared'},
      {'p': 'Both allocate resources at least cost, and the assignment problem is in fact a '
            'special case of the transportation problem. They differ as follows.'},
      {'table': {'align': 'lll', 'head': ['', 'Transportation', 'Assignment'], 'rows': [
        ['Purpose', 'Ship a commodity from sources to destinations at least cost',
         'Allocate $n$ jobs to $n$ workers, one each, at least cost'],
        ['Supplies and demands', 'Any quantities, subject to balance',
         'Every supply and every demand equals one'],
        ['Matrix', 'May be rectangular ($m \\times n$)', 'Must be square; a dummy row or column '
         'is added if it is not'],
        ['Allocation', 'A cell may take any quantity up to the row or column limit',
         'A cell takes either 0 or 1'],
        ['Solution method', 'Initial solution by NWC, least cost or VAM, then optimality test',
         'Hungarian method'],
        ['Degeneracy', 'Requires $m + n - 1$ occupied cells',
         'Always degenerate in transportation terms, which is why a separate method is used'],
      ]}},
      {'h4': 'North-west corner rule'},
      {'p': 'Start at the top-left ("north-west") cell of the tableau and allocate the largest '
            'quantity the row supply and column demand allow. If the row is exhausted, move '
            'down; if the column is exhausted, move right; if both, move diagonally. Continue '
            'until all supplies and demands are met.'},
      {'p': '*Advantage:* extremely simple and quick, and it always yields a feasible solution '
            'with the correct number of occupied cells. *Disadvantage:* it takes no account '
            'whatever of the transportation costs, so the solution is usually far from optimal '
            'and requires the most subsequent iterations to improve.'},
      {'h4': 'Least-cost method'},
      {'p': 'Identify the cell with the lowest unit cost anywhere in the tableau and allocate '
            'as much as possible to it. Delete the exhausted row or column, then repeat with '
            'the lowest remaining cost, until the allocation is complete.'},
      {'p': '*Advantage:* it uses cost information, so it generally gives a much better '
            'starting solution than the north-west corner rule. *Disadvantage:* it is '
            'short-sighted. By taking the cheapest cell available at each step it can leave a '
            'source or destination with only expensive routes remaining, and the penalty for '
            'that is paid at the end.'},
      {'h4': "Vogel's approximation method"},
      {'p': 'For each row and each column, compute the **penalty** — the difference between the '
            'two lowest costs still available in it. This is the additional cost per unit that '
            'would be incurred if the cheapest route in that row or column were not used. '
            'Select the row or column with the **largest** penalty and allocate as much as '
            'possible to its cheapest cell. Delete the exhausted row or column, recompute all '
            'penalties from the costs that remain, and repeat.'},
      {'p': '*Advantage:* the penalty is a look-ahead measure of regret, so VAM avoids the trap '
            'that catches the least-cost method. It attends first to the row or column with '
            'most to lose. *Disadvantage:* it takes appreciably longer to apply, since '
            'penalties must be recomputed after every allocation.'},
      {'h4': 'Which is preferable'},
      {'p': '**Vogel\'s approximation method** is to be preferred. It consistently produces the '
            'lowest-cost initial solution of the three, and that solution is frequently optimal '
            'or within one iteration of optimality, so the additional effort at the start is '
            'more than repaid by the reduction in optimality iterations afterwards. The '
            'north-west corner rule is justified only where a feasible starting point is wanted '
            'quickly and the improvement routine will do the work; the least-cost method is a '
            'reasonable compromise where time is short.'},
      {'note': 'On a typical three-by-three problem the difference is substantial. Applied to '
               'the illustration in §19.2, the three methods give ₦1,195, ₦1,070 and ₦985 '
               'respectively — Vogel\'s solution is 18% cheaper than the north-west corner '
               'rule\'s. Quoting a worked comparison of this kind, if the question supplies '
               'data, earns the discussion marks convincingly.'}],
    'src': 'Chapter 19.1–19.3'},
  ]},
}
