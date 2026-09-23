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
    {'p': 'There are generally two methods of simulation: the **Monte Carlo method** and '
          '**system (computer) simulation**. Only the Monte Carlo method is developed in this '
          'study text.'},
    {'eg': {'tag': 'Study text', 't': 'Example 20.1 — simulating daily demand (inventory)',
      'open': True, 'q': [
      {'p': 'A company\'s daily demand pattern for a product, with probabilities, is:'},
      {'table': {'align': 'lrrrrr', 'head': ['Demand', '0', '10', '20', '30', '40'], 'rows': [
        ['Probability', '0.01', '0.20', '0.15', '0.50', '0.14'],
      ]}},
      {'p': '(a) Using the random numbers 40, 19, 87, 83, 73, 84, 29, 09, 02, 20, simulate '
            'demand for 10 days. (b) Estimate the daily average demand from the simulated '
            'data.'}],
      'a': [
      {'table': {'align': 'lrrl', 'head': ['Demand', 'Probability', 'Cumulative', 'Random '
        'number interval'], 'rows': [
        ['0', '0.01', '0.01', '—'], ['10', '0.20', '0.21', '00–20'],
        ['20', '0.15', '0.36', '21–35'], ['30', '0.50', '0.86', '36–85'],
        ['40', '0.14', '1.00', '86–99'],
      ]}},
      {'table': {'align': 'lrr', 'head': ['Day', 'Random number', 'Demand'], 'rows': [
        ['1', '40', '30'], ['2', '19', '10'], ['3', '87', '40'], ['4', '83', '30'],
        ['5', '73', '30'], ['6', '84', '30'], ['7', '29', '20'], ['8', '09', '10'],
        ['9', '02', '10'], ['10', '20', '10'], ['**Total**', '', '**220**'],
      ]}},
      {'tex': '\\text{(b) Expected average} = \\frac{220}{10} = 22 \\text{ units}'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 20.2 — simulating a queuing system',
      'open': True, 'q': [
      {'p': 'Inter-arrival and service-time distributions for a queuing system:'},
      {'table': {'align': 'lrr', 'head': ['Inter-arrival (min)', 'Probability', ''], 'rows': [
        ['2', '0.15', ''], ['4', '0.23', ''], ['6', '0.35', ''], ['8', '0.17', ''],
        ['10', '0.10', ''],
      ]}},
      {'table': {'align': 'lrr', 'head': ['Service time (min)', 'Probability', ''], 'rows': [
        ['1', '0.10', ''], ['3', '0.22', ''], ['5', '0.33', ''], ['7', '0.23', ''],
        ['9', '0.10', ''],
      ]}},
      {'p': 'Using arrival random numbers 93, 14, 72, 10, 21, 81, 87, 90, 38 and service random '
            'numbers 71, 63, 14, 53, 64, 42, 07, 54, 66, simulate the queue for 60 minutes '
            '(service starting 10:00am) and estimate (i) average queue length, (ii) average '
            'customer waiting time, (iii) average service idle time, (iv) average service time, '
            '(v) average time a customer spends in the system.'}],
      'a': [
      {'p': 'Running the simulation worksheet (arrival time, service start, random number, '
            'service time, service ends, attendant/customer waiting, queue length) for all 9 '
            'customers gives totals: inter-arrival 56 min, service time 41 min, attendant '
            'waiting (idle) 20 min, customer waiting 23 min, queue length total 5.'},
      {'ol': [
        'Average queue length $= 5/9 \\approx 0.56 \\approx 1$ customer.',
        'Average customer waiting time $= 23/9 = 2.56$ minutes.',
        'Average service idle time $= 20/9 = 2.22$ minutes.',
        'Average service time $= 41/9 = 4.56$ minutes.',
        'Time a customer spends in the system $= 4.56 + 2.56 = 7.12$ minutes.',
      ]}]}},
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

  {'n': '20.4', 't': 'Advantages and disadvantages', 'b': [
    {'h4': 'Advantages (study text)'},
    {'ol': [
      'Simulation is suitable for analysing large and complex real-life problems which may not '
      'be solved by the usual quantitative methods.',
      'Simulation can also be used for sensitivity analysis on complex systems.',
      'It makes the decision-maker note and study the interactive system, and effect changes '
      'where possible.',
      'Simulation experiments make use of a **model**, not the system itself.',
      'It can be used as a pre-test service for situations where new products or policies are '
      'to be introduced.',
    ]},
    {'h4': 'Disadvantages (study text)'},
    {'ol': [
      'Simulation may sometimes be very expensive and even take a long time to develop.',
      'Simulation is a trial-and-error approach, and that is the reason for having different '
      'solutions.',
      'Simulation applications usually result in outcomes that are, at least to some extent, '
      'ad hoc.',
    ]},
    {'note': 'The standard examination point is that **simulation is a descriptive/trial-and-'
             'error technique, not an optimising one** — there is no mathematical model leading '
             'directly to an optimal solution, so the result is always an approximation.'},
  ]},

  {'n': '20.5', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§20.1 What simulation is** — models a real system over time using random numbers to '
      'generate values for the uncertain variables, without experimenting on the real system. '
      '**Descriptive, not optimising** — it shows what a given policy would do; alternative '
      'policies must be simulated separately and compared. **Monte Carlo** simulation samples '
      'probability distributions with random numbers. Used when the system is too complex '
      'analytically, when an analytical model\'s assumptions don\'t hold, when real-world '
      'experiments would be too costly/slow/dangerous, or when the **whole distribution** of '
      'outcomes (not just the expected value) is wanted.',
      '**§20.2 Assigning random number ranges** — list values and probabilities, cumulate the '
      'probabilities, assign a **contiguous, non-overlapping** block of random numbers to each '
      'value in proportion to its probability (using the cumulative column as the upper '
      'boundary), then read off values against drawn random numbers. With two-digit numbers '
      '(00–99), a probability of 0.30 gets 30 numbers; check that each block\'s count equals '
      '100 × its probability and that all blocks together span 00–99 with no gaps.',
      '**§20.3 Running a simulation** — build a table of random number → simulated value per '
      'trial. A small number of trials will **not** match the theoretical expected value '
      'exactly — convergence needs many iterations, so a short exam simulation is an '
      'illustration of *method*, not a reliable estimate (say so for marks). When comparing '
      'policies (e.g. order quantities), **every policy must be tested against the same '
      'stream of random numbers**, or the policy comparison is confounded with differences in '
      'the random demand stream itself.',
      '**§20.4 Advantages and disadvantages** — advantages: suitable for large/complex '
      'problems the usual quantitative methods cannot solve; useful for sensitivity analysis; '
      'lets the decision-maker study the interactive system and effect changes; uses a model, '
      'not the real system; and can pre-test new products/policies. Disadvantages: can be '
      'expensive and slow to develop; is trial-and-error (so different runs give different '
      'solutions); results are, to some extent, ad hoc.',
    ]},
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
    {'h3': 'C. Advantages and disadvantages'},
    {'ul': [
      '**Advantages** — suitable for large/complex problems beyond the usual quantitative '
      'methods; useful for sensitivity analysis; lets the decision-maker study the system and '
      'effect changes; uses a model rather than the real system; can pre-test new products or '
      'policies.',
      '**Disadvantages** — can be expensive and slow to develop; is a trial-and-error approach '
      '(different runs give different solutions); results are, at least to some extent, ad hoc.',
    ]},
  ]},

  {'n': '20.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'By utilising simulation, the result that emanates from it is (A) Exact  (B) '
        'Unrealistic  (C) An approximation  (D) Simplified  (E) Uncertain',
        'A large complex simulation model will be most appropriate when (A) it is difficult to '
        'create appropriate events  (B) it is expensive to write and use it as an experimental '
        'device  (C) the average costs may not be well defined  (D) the certain decision '
        'variable(s) cannot be clearly identified  (E) the time to be taken is short and '
        'unpredictable',
        'In the Monte Carlo simulation method, assigning random numbers means it is necessary '
        'to (A) assign particular and appropriate random numbers  (B) not assign particular and '
        'appropriate random numbers  (C) develop a cumulative probability distribution  (D) not '
        'assign the exact range of random number interval as the probability  (E) have the '
        'total frequency for assigning the random numbers',
        'Before simulation is carried out, there is need to consider the analytical results in '
        'order to (A) identify suitable values of decision variables for specific choices of '
        'system parameters  (B) determine the optimal decision  (C) identify suitable values of '
        'the system parameters  (D) compute the optimal values  (E) determine the variables '
        'that are irrelevant',
        'A method of simulation that utilises samples from a real population, and does not '
        'assume a theoretical counterpart of the actual population, is known as the '
        '.......................... method.',
        'A simulation method that does not lend itself to analysis by a mathematical model, and '
        'which draws samples from a table of random numbers, is called the '
        '.......................... method.',
        'An application of simulation to situations such as cash-flow analysis, price '
        'determination, stock and commodity analysis, consumer behaviour, budgeting or '
        'investment can be seen as .......................... and .......................... '
        'applications.',
        'The disadvantage of simulation over optimisation is that several options of measure of '
        'performance cannot be examined. TRUE or FALSE?',
      ]}],
      'a': [
      {'ol': [
        '**C — an approximation.**', '**B.**', '**C — develop a cumulative probability '
        'distribution.**', '**A.**', '**System simulation.**', '**Monte Carlo.**',
        '**Business and Economic** applications.', '**False.**',
      ]}]}},
    {'note': 'The study text\'s own end-of-chapter answer key stops at question 8 — questions 9 '
             'and 10 (and their answers) are missing/garbled in the printed source itself, not '
             'omitted here.'},
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
    'src': 'Chapter 20.2', 'sec': '20.2'},
   {'q': 'If an outcome has a probability of 0.25, how many two-digit random numbers should be '
         'assigned to it?',
    'o': ['4', '25', '20', '75', '2'],
    'a': 1,
    'w': 'Out of the one hundred numbers 00–99, a probability of 0.25 takes 25 of them.',
    'src': 'Chapter 20.2', 'sec': '20.2'},
   {'q': 'Simulation is best described as a technique that is',
    'o': ['optimising', 'descriptive', 'deterministic', 'analytical', 'graphical'],
    'a': 1,
    'w': 'Simulation shows what would happen under a specified policy. It does not compute the '
         'best policy, so alternatives must be tested and compared.',
    'src': 'Chapter 20.1', 'sec': '20.1'},
   {'q': 'Demand has probabilities 0.2, 0.5 and 0.3 for 10, 20 and 30 units. Using the '
         'convention that intervals begin at 00, the random number range assigned to a demand '
         'of 20 units is',
    'o': ['00 – 19', '20 – 69', '20 – 49', '50 – 69', '21 – 70'],
    'a': 1,
    'w': 'A demand of 10 takes 00–19. A demand of 20 has probability 0.5, so it takes the next '
         'fifty numbers, 20 to 69.',
    'src': 'Chapter 20.2', 'sec': '20.2'},
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
    'src': 'Chapter 20.3', 'sec': '20.3'},
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
    'src': 'Chapter 20.1–20.4', 'sec': '20.1'},
  ]},
}
