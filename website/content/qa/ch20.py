CH = {
 'n': 20,
 't': 'Simulation',
 'brief': 'Monte Carlo simulation: assigning random number ranges to a probability '
          'distribution, running a simulation table, and using the results to evaluate a '
          'decision. Advantages and limitations of the technique.',
 'outcomes': [
   'Explain what simulation is and when it is appropriate',
   'Assign random number intervals from a probability distribution',
   'Construct and run a simulation table',
   'Use simulated results to compare alternative policies',
   'Discuss the advantages and limitations of simulation',
 ],
 'secs': [
  {'n': '20.1', 't': 'What simulation is', 'b': [
    {'def': {'t': 'Simulation',
             'd': 'A technique in which a model of a real system is operated over time, using '
                  'random numbers to generate values of the uncertain variables, so that the '
                  'behaviour of the system can be observed without experimenting on the system '
                  'itself.'}},
    {'p': 'Simulation is **descriptive**, not optimising. It tells you what would happen under '
          'a given policy; it does not compute the best policy directly. Alternative policies '
          'are therefore simulated in turn and compared. **Monte Carlo** simulation is the '
          'variety used where the uncertainty is represented by probability distributions and '
          'sampled with random numbers.'},
    {'h4': 'When to use it'},
    {'ul': [
      'The system is too complex for an analytical solution — several interacting random '
      'variables, or queues feeding into queues.',
      'The mathematical assumptions of an analytical model (constant demand, exponential '
      'service times) do not hold.',
      'Experimenting on the real system would be too costly, too slow or too dangerous.',
      'Management wants to see the **distribution** of outcomes, not just an expected value — '
      'the worst case matters as much as the average.',
    ]},
    {'p': 'Typical applications are inventory policy under uncertain demand and lead time, '
          'queueing at bank counters or toll gates, machine breakdown and maintenance '
          'scheduling, project completion times, and cash flow forecasting.'},
  ]},

  {'n': '20.2', 't': 'Assigning random number ranges', 'b': [
    {'steps': [
      'List the possible values of the variable and their probabilities.',
      'Compute the **cumulative** probability for each value.',
      'Assign a block of random numbers to each value, in proportion to its probability, using '
      'the cumulative column as the upper boundary.',
      'Draw random numbers from a table or a generator and read off the corresponding value.',
    ]},
    {'key': 'With two-digit random numbers (00–99) a probability of 0.30 receives 30 numbers. '
            'The intervals must be **contiguous and non-overlapping**, and together must use '
            'all one hundred numbers. Starting at 00 rather than 01 is the usual convention '
            'and keeps the arithmetic simple: the interval for a value ends at (cumulative '
            'probability × 100) − 1.'},
    {'table': {'align': 'lrrl',
      'head': ['Daily demand', 'Probability', 'Cumulative', 'Random numbers'], 'rows': [
      ['0', '0.05', '0.05', '00 – 04'],
      ['1', '0.15', '0.20', '05 – 19'],
      ['2', '0.30', '0.50', '20 – 49'],
      ['3', '0.25', '0.75', '50 – 74'],
      ['4', '0.15', '0.90', '75 – 89'],
      ['5', '0.10', '1.00', '90 – 99'],
    ]}},
    {'note': 'Check the assignment before using it: the count of numbers in each block must '
             'equal 100 times the probability (5, 15, 30, 25, 15, 10 here), and the blocks must '
             'run continuously from 00 to 99. An error here corrupts every row of the '
             'simulation that follows.'},
  ]},

  {'n': '20.3', 't': 'Running a simulation', 'b': [
    {'eg': {'t': 'Simulating demand', 'q': [
      {'p': 'Using the demand distribution above and the random numbers 58, 12, 90, 33, 71, '
            '06, 84, 47, 25, 03, simulate demand for ten days and compute the average daily '
            'demand. Compare it with the expected value of the distribution.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['Day', 'Random number', 'Demand'], 'rows': [
        ['1', '58', '3'],
        ['2', '12', '1'],
        ['3', '90', '5'],
        ['4', '33', '2'],
        ['5', '71', '3'],
        ['6', '06', '1'],
        ['7', '84', '4'],
        ['8', '47', '2'],
        ['9', '25', '2'],
        ['10', '03', '0'],
        ['**Total**', '', '**23**'],
      ]}},
      {'tex': '\\text{Simulated average} = \\frac{23}{10} = 2.3 \\text{ units per day}'},
      {'p': 'The theoretical expected value is:'},
      {'tex': 'E(X) = 0(0.05) + 1(0.15) + 2(0.30) + 3(0.25) + 4(0.15) + 5(0.10) = 2.6'},
      {'key': 'The simulated average of 2.3 differs from the theoretical 2.6 because ten trials '
              'is a very small sample. Simulated results converge on the theoretical value only '
              'as the number of trials grows — this is why real simulations run thousands of '
              'iterations. An examination question run over ten days is an illustration of '
              'method, not a reliable estimate, and a sentence saying so earns marks.'}]}},

    {'eg': {'t': 'Using a simulation to choose a policy', 'q': [
      {'p': 'A vendor buys newspapers at ₦150 each and sells them at ₦250. Unsold copies are '
            'returned to the publisher for ₦50. Using the ten days of simulated demand above, '
            'determine which of the order quantities 1, 2, 3 or 4 copies a day is most '
            'profitable.'}],
      'a': [
      {'p': 'For each order quantity $Q$, sales are $\\min(\\text{demand}, Q)$ and unsold '
            'copies are $Q - \\text{sales}$. Take $Q = 3$ as an illustration:'},
      {'table': {'align': 'lrrrr',
        'head': ['Day', 'Demand', 'Sales', 'Unsold', 'Contribution (₦)'], 'rows': [
        ['1', '3', '3', '0', '300'],
        ['2', '1', '1', '2', '−50'],
        ['3', '5', '3', '0', '300'],
        ['4', '2', '2', '1', '100'],
        ['5', '3', '3', '0', '300'],
        ['6', '1', '1', '2', '−50'],
        ['7', '4', '3', '0', '300'],
        ['8', '2', '2', '1', '100'],
        ['9', '2', '2', '1', '100'],
        ['10', '0', '0', '3', '−300'],
        ['**Total**', '**23**', '**20**', '**10**', '**1,000**'],
      ]}},
      {'p': 'Daily contribution is $250 \\times \\text{sales} + 50 \\times \\text{unsold} '
            '- 150 \\times 3$. On day 1 this is $750 + 0 - 450 = ₦300$; on day 10, '
            '$0 + 150 - 450 = -₦300$. Repeating the exercise for each order quantity over the '
            'same ten days of demand:'},
      {'table': {'align': 'lrrrr',
        'head': ['Order quantity', 'Total sales', 'Total unsold', 'Total cost (₦)',
                 'Profit over 10 days (₦)'], 'rows': [
        ['1', '9', '1', '1,500', '800'],
        ['2', '16', '4', '3,000', '**1,200**'],
        ['3', '20', '10', '4,500', '1,000'],
        ['4', '22', '18', '6,000', '400'],
      ]}},
      {'p': 'Profit is highest at an order quantity of **2 copies a day**, giving ₦1,200 over '
            'the ten days, or ₦120 a day.'},
      {'p': 'The economics are worth stating. Each copy sold earns $250 - 150 = ₦100$; each '
            'copy unsold loses $150 - 50 = ₦100$. Gain and loss are equal, so the vendor should '
            'stock up to the point where the probability of selling the next copy is above 0.5. '
            'From the cumulative column, $P(\\text{demand} \\ge 2) = 0.80$ but '
            '$P(\\text{demand} \\ge 3) = 0.50$ — exactly on the boundary. The simulation\'s '
            'answer of 2 is consistent with that, and the closeness of 2 and 3 in the table '
            '(₦1,200 against ₦1,000) is precisely what the theory predicts.'},
      {'warn': 'Every order quantity must be tested against the **same** stream of random '
               'numbers. Using fresh random numbers for each policy confounds the difference '
               'between the policies with the difference between the demand streams, and the '
               'comparison becomes meaningless.'}]}},
  ]},

  {'n': '20.4', 't': 'Advantages and limitations', 'b': [
    {'h4': 'Advantages'},
    {'ul': [
      '**Handles complexity.** Systems with several interacting random variables can be '
      'modelled where no analytical solution exists.',
      '**Avoids restrictive assumptions.** Any empirical distribution can be sampled, not only '
      'the mathematically convenient ones.',
      '**Safe and cheap experimentation.** Policies can be tested on the model rather than on '
      'the real operation.',
      '**Compresses time.** Years of operation can be simulated in seconds, and rare events '
      'observed often enough to be studied.',
      '**Shows the whole distribution of outcomes**, including the worst case, rather than a '
      'single expected value.',
      '**Comprehensible to management.** The logic of "if this happened, then that would '
      'follow" is transparent in a way that a closed-form solution often is not.',
    ]},
    {'h4': 'Limitations'},
    {'ul': [
      '**It does not optimise.** Simulation evaluates the policies you choose to test. A better '
      'policy that was not tested will not be discovered.',
      '**Results are estimates subject to sampling error.** Two runs with different random '
      'numbers give different answers, and a short run may mislead badly — as the 2.3 against '
      '2.6 above illustrates.',
      '**Requires many trials** to produce reliable results, and hence computing resources for '
      'any realistic problem.',
      '**Depends on the input distributions.** If the assumed probabilities are wrong, the '
      'simulation reproduces the error faithfully and with an air of authority.',
      '**Model building is expensive** in skilled time, and the model must be validated before '
      'it is trusted.',
    ]},
    {'note': 'The standard examination point is the first limitation: **simulation is a '
             'descriptive technique, not an optimising one**. Contrast it with linear '
             'programming, which computes the optimum directly. Making that contrast explicitly '
             'is usually worth a mark on its own.'},
  ]},

  {'n': '20.5', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'All the terms'},
    {'ul': [
      '**Simulation** — imitating the behaviour of a real system over time by a numerical '
      'model, to study it without experimenting on the real thing.',
      '**Monte Carlo simulation** — simulation driven by **random numbers** to reproduce a '
      'probability distribution.',
      '**Random numbers** — digits with each value equally likely; from tables, a calculator '
      'or software; used to sample from a distribution.',
      '**Probability distribution** — the possible values of a variable (demand, lead time, '
      'arrivals) with their probabilities $p(x)$.',
      '**Cumulative probability $F(x)$** — the running total of $p(x)$; used to set the random '
      '-number ranges.',
      '**Random-number interval (tag)** — the block of random numbers assigned to each value, '
      'in proportion to its probability.',
      '**Run / trial / iteration** — one pass through the simulation table (e.g. one '
      'simulated day).',
      '**Simulation is descriptive, not optimising** — it evaluates given policies; it does '
      'not find the best one directly.',
    ]},
    {'h3': 'A. Setting up the model'},
    {'fbox': {'h': 'Random-number assignment', 'rows': [
      {'lb': 'Cumulative probability',
       'tex': 'F(x_i) = \\sum_{t \\le x_i} p(t)'},
      {'lb': 'Two-digit random-number range for value $x_i$',
       'tex': '\\big[\\,100\\,F(x_{i-1}), \\ \\ 100\\,F(x_i) - 1\\,\\big]',
       'nt': 'e.g. $p = 0.10, 0.25, 0.40, 0.25 \\Rightarrow$ tags 00–09, 10–34, 35–74, 75–99.'},
      {'lb': 'One-digit version', 'tex': '\\big[\\,10\\,F(x_{i-1}), \\ 10\\,F(x_i) - 1\\,\\big]'},
    ]}},
    {'h3': 'B. Running and evaluating'},
    {'ol': [
      'Build the distribution table with $p(x)$, $F(x)$ and the random-number tags.',
      'For each trial, draw a random number, read off the corresponding value of the variable.',
      'Carry the value through the system logic (e.g. update stock, queue, cash).',
      'Repeat for the required number of trials and total / average the results.',
    ]},
    {'fbox': {'h': 'Results', 'rows': [
      {'lb': 'Simulated mean',
       'tex': '\\bar{x} = \\dfrac{\\sum x_i}{n} \\quad (n = \\text{number of trials})'},
      {'lb': 'Theoretical expected value (for comparison)',
       'tex': 'E(X) = \\sum x\\,p(x)'},
      {'lb': 'Simulated cost / profit per period',
       'tex': '= \\dfrac{\\text{total simulated cost / profit}}{\\text{number of periods '
              'simulated}}'},
    ]}},
    {'note': 'The simulated mean approaches $E(X)$ as the number of trials increases; a large '
             'gap after few trials just reflects sampling variation.'},
    {'h3': 'C. Advantages and limitations'},
    {'ul': [
      '**Advantages** — handles complex, stochastic systems that defy analytic solution; no '
      'disruption to the real system; "what-if" testing of policies; relatively easy to '
      'understand.',
      '**Limitations** — descriptive not optimising; results depend on the quality of the '
      'input distributions and the random numbers; many trials needed for reliable estimates; '
      'can be time-consuming / costly to build; each run gives only an estimate.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': 'Cumulative probability',
   'tex': 'F(x) = \\sum_{t \\le x} p(t)'},
  {'lb': 'Random number interval (two digits)',
   'tex': '\\big[100\\,F(x_{i-1}),\\ 100\\,F(x_i) - 1\\big]'},
  {'lb': 'Simulated mean',
   'tex': '\\bar{x} = \\frac{\\sum x_i}{n}'},
  {'lb': 'Expected value (for comparison)',
   'tex': 'E(X) = \\sum x\\,p(x)'},
 ],
 'focus':
   'One or two Section A marks on the assignment of random number ranges or on the nature of '
   'simulation. In Section B it appears in perhaps one diet in four, always as a table: assign '
   'the ranges, run ten or fifteen trials, compute an average or a profit, and comment. The '
   'comment — that the run is short, that simulation does not optimise — is where the last two '
   'or three marks sit, and it is the part most often omitted.',
 'errors': [
   'Overlapping or non-contiguous random number intervals, or intervals that do not total 100 '
   'numbers.',
   'Assigning intervals from the individual probabilities rather than the cumulative ones.',
   'Using different random numbers when comparing alternative policies.',
   'Presenting a ten-trial average as though it were a reliable estimate.',
   'Describing simulation as producing an optimal solution.',
   'Forgetting to carry forward closing stock, or a queue, from one period to the next in a '
   'multi-period simulation.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In a Monte Carlo simulation, random number intervals are assigned in proportion to',
    'o': ['the values of the variable', 'the probabilities of the outcomes',
          'the number of trials', 'the expected value', 'the standard deviation'],
    'a': 1,
    'w': 'Each outcome receives a block of random numbers proportional to its probability, so '
         'that it is selected with that relative frequency.',
    'src': 'Chapter 20.2'},
   {'q': 'If an outcome has a probability of 0.25, how many two-digit random numbers should be '
         'assigned to it?',
    'o': ['4', '25', '20', '75', '2'],
    'a': 1,
    'w': 'Out of the one hundred numbers 00–99, a probability of 0.25 takes 25 of them.',
    'src': 'Chapter 20.2'},
   {'q': 'Simulation is best described as a technique that is',
    'o': ['optimising', 'descriptive', 'deterministic', 'analytical', 'graphical'],
    'a': 1,
    'w': 'Simulation shows what would happen under a specified policy. It does not compute the '
         'best policy, so alternatives must be tested and compared.',
    'src': 'Chapter 20.1'},
   {'q': 'Demand has probabilities 0.2, 0.5 and 0.3 for 10, 20 and 30 units. Using the '
         'convention that intervals begin at 00, the random number range assigned to a demand '
         'of 20 units is',
    'o': ['00 – 19', '20 – 69', '20 – 49', '50 – 69', '21 – 70'],
    'a': 1,
    'w': 'A demand of 10 takes 00–19. A demand of 20 has probability 0.5, so it takes the next '
         'fifty numbers, 20 to 69.',
    'src': 'Chapter 20.2'},
   {'q': 'A principal reason why a simulation should be run for a large number of trials is '
         'that',
    'o': ['random numbers are eventually exhausted',
          'results converge on the theoretical values only as the number of trials increases',
          'the model becomes optimal after many trials',
          'the probabilities change over time',
          'short runs are impossible to compute'],
    'a': 1,
    'w': 'A simulated average is a sample statistic subject to sampling error. Only a large '
         'number of trials makes it a reliable estimate.',
    'src': 'Chapter 20.3'},
  ],
  'theory': [
   {'q': 'The daily demand for a perishable product at a retail outlet follows the '
         'distribution: 0 units 0.10; 1 unit 0.20; 2 units 0.40; 3 units 0.20; 4 units 0.10. '
         '(a) Assign two-digit random number intervals to each level of demand. (b) Using the '
         'random numbers 27, 03, 65, 88, 41, 92, 16, 55, 34, 71, simulate demand for ten days '
         'and compute the average daily demand. (c) Compare your result with the expected value '
         'of the distribution and explain any difference. (d) State three advantages and three '
         'limitations of simulation as a technique.',
    'marks': 15,
    'a': [
      {'h4': '(a) Random number intervals'},
      {'table': {'align': 'lrrl',
        'head': ['Demand', 'Probability', 'Cumulative probability', 'Random numbers'], 'rows': [
        ['0', '0.10', '0.10', '00 – 09'],
        ['1', '0.20', '0.30', '10 – 29'],
        ['2', '0.40', '0.70', '30 – 69'],
        ['3', '0.20', '0.90', '70 – 89'],
        ['4', '0.10', '1.00', '90 – 99'],
      ]}},
      {'p': 'The blocks contain 10, 20, 40, 20 and 10 numbers respectively — a total of 100, '
            'running continuously from 00 to 99, as required.'},
      {'h4': '(b) The simulation'},
      {'table': {'align': 'lrr', 'head': ['Day', 'Random number', 'Demand (units)'], 'rows': [
        ['1', '27', '1'],
        ['2', '03', '0'],
        ['3', '65', '2'],
        ['4', '88', '3'],
        ['5', '41', '2'],
        ['6', '92', '4'],
        ['7', '16', '1'],
        ['8', '55', '2'],
        ['9', '34', '2'],
        ['10', '71', '3'],
        ['**Total**', '', '**20**'],
      ]}},
      {'tex': '\\text{Average daily demand} = \\frac{20}{10} = 2.0 \\text{ units}'},
      {'h4': '(c) Comparison with the expected value'},
      {'tex': 'E(X) = 0(0.10) + 1(0.20) + 2(0.40) + 3(0.20) + 4(0.10)'},
      {'tex': '= 0 + 0.20 + 0.80 + 0.60 + 0.40 = 2.0 \\text{ units}'},
      {'p': 'The simulated average of 2.0 units happens to equal the theoretical expected value '
            'exactly. This is a **coincidence of this particular sample**, not a property of '
            'the method, and should not be presented as confirmation that the simulation is '
            'correct.'},
      {'p': 'A simulated average is a sample mean drawn from the underlying distribution, and '
            'is therefore subject to sampling error. With only ten trials that error can be '
            'substantial: had the random number 92 been 12 instead, day 6 would have shown a '
            'demand of 1 rather than 4 and the average would have fallen to 1.7 — a 15% '
            'difference from one number in ten. The agreement observed here would not '
            'necessarily be repeated with a different set of random numbers.'},
      {'p': 'The general principle is that the simulated mean converges on the expected value '
            'only as the number of trials increases, in accordance with the law of large '
            'numbers. Practical simulations therefore run thousands of iterations, and often '
            'several independent replications, before their results are relied on.'},
      {'h4': '(d) Advantages and limitations'},
      {'p': '**Advantages**'},
      {'ol': [
        '**It handles complexity that defeats analytical methods.** Where several random '
        'variables interact — demand, lead time and machine availability together — no '
        'closed-form solution exists, but each can be sampled independently in a simulation.',
        '**It avoids restrictive assumptions.** Any empirical distribution observed in the '
        'business can be used directly, rather than forcing the data into a standard '
        'distribution chosen for mathematical convenience.',
        '**It permits safe and inexpensive experimentation.** Alternative stock policies, '
        'staffing levels or layouts can be tested on the model without disrupting the real '
        'operation, and years of trading can be compressed into seconds of computing.',
        '**It reveals the whole distribution of outcomes**, so management can see how bad the '
        'worst case is and how often it occurs, rather than only an average.',
      ]},
      {'p': '**Limitations**'},
      {'ol': [
        '**It is descriptive, not optimising.** Simulation evaluates the policies presented to '
        'it; it does not search for the best one. A superior policy that is never tested will '
        'never be found. This is the fundamental contrast with linear programming, which '
        'computes the optimum directly.',
        '**The results are estimates subject to sampling error.** Different random numbers '
        'produce different answers, and short runs — such as the ten days above — may be '
        'seriously unrepresentative.',
        '**It is only as good as its inputs.** If the assumed probability distribution does not '
        'reflect actual demand, the simulation will reproduce that error faithfully while '
        'lending it an appearance of rigour.',
        '**Model building and validation are costly**, requiring skilled analysts, reliable '
        'historical data and computing resources that may not be justified for a small or '
        'one-off decision.',
      ]}],
    'src': 'Chapter 20.1–20.4'},
  ]},
}
