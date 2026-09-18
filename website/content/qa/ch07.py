CH = {
 'n': 7,
 't': 'Probability',
 'brief': 'Sample spaces and events, the addition and multiplication laws, conditional '
          'probability, permutations and combinations, and expected value.',
 'outcomes': [
   'Define probability and identify a sample space',
   'Distinguish mutually exclusive from independent events',
   'Apply the addition and multiplication laws',
   'Compute conditional probabilities',
   'Use permutations and combinations to count outcomes',
   'Compute an expected value and use it to choose between alternatives',
 ],
 'secs': [
  {'n': '7.1', 't': 'Basic terms', 'b': [
    {'ul': [
      '**Experiment** — a process with an uncertain outcome.',
      '**Sample space $S$** — the set of all possible outcomes.',
      '**Event** — a subset of the sample space.',
      '**Mutually exclusive** events cannot occur together: $P(A \\cap B) = 0$.',
      '**Exhaustive** events cover the whole sample space.',
      '**Independent** events: the occurrence of one does not affect the probability of the '
      'other, so $P(A \\cap B) = P(A)P(B)$.',
      '**Complement** $A\'$: everything not in $A$, so $P(A\') = 1 - P(A)$.',
    ]},
    {'tex': 'P(A) = \\frac{\\text{Number of favourable outcomes}}'
            '{\\text{Total number of equally likely outcomes}}, \\qquad 0 \\le P(A) \\le 1',
     'tag': '(7.1)'},
    {'warn': '**Mutually exclusive is not the same as independent.** Two mutually exclusive events '
             'with non-zero probability are in fact strongly *dependent*: if one occurs, the other '
             'certainly does not. Confusing the two is the commonest conceptual error in this '
             'chapter.'},
  ]},

  {'n': '7.2', 't': 'The laws of probability', 'b': [
    {'fbox': {'h': 'Addition and multiplication', 'rows': [
      {'lb': 'Addition law, general',
       'tex': 'P(A \\cup B) = P(A) + P(B) - P(A \\cap B)'},
      {'lb': 'Addition law, mutually exclusive events',
       'tex': 'P(A \\cup B) = P(A) + P(B)'},
      {'lb': 'Multiplication law, general',
       'tex': 'P(A \\cap B) = P(A) \\times P(B \\mid A)'},
      {'lb': 'Multiplication law, independent events',
       'tex': 'P(A \\cap B) = P(A) \\times P(B)'},
      {'lb': 'Conditional probability',
       'tex': 'P(B \\mid A) = \\frac{P(A \\cap B)}{P(A)}'},
      {'lb': 'Complement', 'tex': "P(A') = 1 - P(A)"},
    ]}},
    {'key': 'In words: **"or" means add, "and" means multiply.** Subtract the overlap when adding '
            'unless the events are mutually exclusive, and use the conditional probability when '
            'multiplying unless the events are independent.'},
    {'eg': {'t': 'Addition and conditional probability', 'q': [
      {'p': 'Of 200 staff, 120 have a degree, 80 are in the accounts department, and 50 are in '
            'accounts and have a degree. One member of staff is chosen at random. Find the '
            'probability that the person (a) has a degree or is in accounts; (b) is in accounts '
            'given that they have a degree; (c) has neither a degree nor works in accounts.'}],
      'a': [
      {'p': 'Let $D$ = has a degree, $A$ = in accounts. Then $P(D) = 120/200 = 0.6$, '
            '$P(A) = 80/200 = 0.4$, $P(D \\cap A) = 50/200 = 0.25$.'},
      {'p': '**(a)**'},
      {'tex': 'P(D \\cup A) = P(D) + P(A) - P(D \\cap A) = 0.6 + 0.4 - 0.25 = 0.75'},
      {'p': '**(b)**'},
      {'tex': 'P(A \\mid D) = \\frac{P(A \\cap D)}{P(D)} = \\frac{0.25}{0.6} = 0.4167'},
      {'p': '**(c)** Neither is the complement of "either":'},
      {'tex': "P(D' \\cap A') = 1 - P(D \\cup A) = 1 - 0.75 = 0.25"},
      {'note': 'Check the independence question while you are here: $P(A)P(D) = 0.4 \\times 0.6 '
               '= 0.24 \\ne 0.25 = P(A \\cap D)$, so having a degree and working in accounts are '
               '**not quite independent** — graduates are very slightly over-represented in '
               'accounts.'}]}},
  ]},

  {'n': '7.3', 't': 'Counting: permutations and combinations', 'b': [
    {'fbox': {'h': 'Counting rules', 'rows': [
      {'lb': 'Permutation (order matters)',
       'tex': '{}^nP_r = \\frac{n!}{(n-r)!}'},
      {'lb': 'Combination (order does not matter)',
       'tex': '{}^nC_r = \\binom{n}{r} = \\frac{n!}{r!\\,(n-r)!}'},
      {'lb': 'Relationship', 'tex': '{}^nP_r = {}^nC_r \\times r!'},
    ]}},
    {'p': 'The test is simple: if rearranging the same items gives a **different** result, it is a '
          'permutation; if not, a combination. A committee of three from ten is a combination; '
          'chairman, secretary and treasurer from ten is a permutation.'},
    {'eg': {'t': 'Combinations in a probability', 'q': [
      {'p': 'A box holds 7 good and 3 defective components. Three are drawn at random without '
            'replacement. Find the probability that exactly one is defective.'}],
      'a': [
      {'p': 'Total ways of choosing 3 from 10:'},
      {'tex': '{}^{10}C_3 = \\frac{10!}{3!\\,7!} = \\frac{10 \\times 9 \\times 8}{3 \\times 2 '
              '\\times 1} = 120'},
      {'p': 'Ways of choosing exactly 1 defective from 3 and 2 good from 7:'},
      {'tex': '{}^{3}C_1 \\times {}^{7}C_2 = 3 \\times \\frac{7 \\times 6}{2} = 3 \\times 21 = 63'},
      {'tex': 'P(\\text{exactly one defective}) = \\frac{63}{120} = 0.525'}]}},
  ]},

  {'n': '7.4', 't': 'Expected value', 'b': [
    {'tex': 'E(X) = \\sum x_i \\, p_i', 'tag': '(7.2)'},
    {'p': 'The expected value is the long-run average outcome — a weighted mean of the possible '
          'values, weighted by their probabilities. It need not be an attainable value.'},
    {'eg': {'t': 'Expected value of a die', 'q': [
      {'p': 'Calculate the expected value of rolling a fair six-sided die.'}],
      'a': [
      {'tex': 'E(X) = \\sum x p = (1 + 2 + 3 + 4 + 5 + 6) \\times \\frac{1}{6} '
              '= \\frac{21}{6} = 3.5'},
      {'note': 'A die can never show 3.5. The expected value is the average over many throws, not '
               'a prediction of any single one.'}]}},
    {'eg': {'t': 'Choosing between projects', 'q': [
      {'p': 'A company must choose between two projects. Returns depend on demand:'},
      {'table': {'align': 'lrrr',
        'head': ['Demand', 'Probability', 'Project A (₦m)', 'Project B (₦m)'], 'rows': [
        ['Low', '0.25', '20', '(10)'],
        ['Medium', '0.45', '50', '60'],
        ['High', '0.30', '70', '110'],
      ]}},
      {'p': 'Which should be chosen on expected value, and what else should be considered?'}],
      'a': [
      {'tex': 'E(A) = 0.25(20) + 0.45(50) + 0.30(70) = 5 + 22.5 + 21 = ₦48.5\\text{m}'},
      {'tex': 'E(B) = 0.25(-10) + 0.45(60) + 0.30(110) = -2.5 + 27 + 33 = ₦57.5\\text{m}'},
      {'p': '**Project B** has the higher expected value and would be chosen on that criterion.'},
      {'h4': 'What else matters'},
      {'ul': [
        '**Risk.** B\'s outcomes range from a loss of ₦10m to a gain of ₦110m; A\'s range only '
        'from ₦20m to ₦70m. B is far more variable, and a risk-averse decision-maker might still '
        'prefer A.',
        '**Downside.** B can lose money; A cannot. If the company could not survive a ₦10m loss, '
        'expected value is the wrong criterion entirely.',
        '**Repetition.** Expected value is a long-run average and is most appropriate where the '
        'decision will be repeated many times. For a single, once-only decision it is a weaker '
        'guide.',
        '**Quality of the probabilities.** They are estimates; a sensitivity analysis on them is '
        'worth more than another decimal place on the expected value.']},
      {'note': 'A question that gives you two projects and asks which to choose almost always '
               'wants the expected values **and** a comment on risk. The comment is where the '
               'discriminating marks are.'}]}},
  ]},

  {'n': '7.5', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§7.1 Basic terms** — experiment, sample space $S$ (all outcomes), event (a subset of '
      '$S$), mutually exclusive ($P(A\\cap B)=0$), exhaustive (covers all of $S$), independent '
      '($P(A\\cap B)=P(A)P(B)$), complement ($P(A\')=1-P(A)$); $P(A)=$ favourable ÷ total '
      'equally-likely outcomes, $0\\le P(A)\\le1$. **Mutually exclusive is not independent** — '
      'in fact two such events (with non-zero probability) are strongly *dependent*, since one '
      'occurring guarantees the other does not.',
      '**§7.2 The laws of probability** — "or" means **add** (subtract the overlap unless '
      'mutually exclusive: $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$); "and" means **multiply** (use '
      'the conditional probability unless independent: $P(A\\cap B)=P(A)P(B|A)$); conditional '
      '$P(B|A)=P(A\\cap B)/P(A)$. Always check independence by comparing $P(A)P(B)$ against '
      'the actual $P(A\\cap B)$ rather than assuming it.',
      '**§7.3 Counting: permutations and combinations** — permutation ${}^nP_r=n!/(n-r)!$ when '
      'order matters (chairman/secretary/treasurer); combination ${}^nC_r=n!/(r!(n-r)!)$ when '
      'it does not (a 3-person committee); ${}^nP_r={}^nC_r\\times r!$. Combinations feed '
      'directly into probability-without-replacement questions (favourable-selection '
      'combinations ÷ total-selection combinations).',
      '**§7.4 Expected value** — $E(X)=\\sum x_ip_i$, the long-run probability-weighted '
      'average outcome — it need **not** be an attainable value (e.g. 3.5 on a die). When '
      'choosing between options, the higher $E(X)$ is only one criterion: also weigh risk/'
      'variability of outcomes, whether there is a downside the decision-maker could not '
      'survive, whether the decision repeats (EV suits repeated decisions more than one-off '
      'ones), and the reliability of the probability estimates themselves.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Probability** — a measure, between 0 and 1, of the likelihood that an event occurs. '
      '$P(E) = 0$ → certain not to happen; $P(E) = 1$ → certain to happen; $0 \\le P(E) \\le 1$.',
      '**(Random) experiment** — an act with an unpredictable outcome (tossing a coin, throwing '
      'a die).',
      '**Outcome** — one possible result of a single trial of an experiment.',
      '**Sample space $S$** — the set of all possible outcomes. **Sample point** — one element '
      'of $S$.',
      '**Event** — a subset of the sample space; a collection of sample points with a common '
      'characteristic.',
      '**$n(A)$** — the number of sample points in event $A$; **$n(S)$** — the number in the '
      'sample space.',
      '**Equally likely outcomes** — outcomes with the same probability.',
      '**Classical (a priori) probability** — computed by counting equally likely outcomes '
      'before any trial.',
      '**Frequency (a posteriori / empirical) probability** — the relative frequency $r/n$ '
      'observed after $n$ (large) repetitions.',
      '**Axiomatic probability** — probability defined by three axioms (below), based on set '
      'theory.',
      '**Complement $E\'$ (or $\\bar{E}$)** — the event that $E$ does **not** occur; '
      '$P(E\') = 1 - P(E)$.',
      '**Mutually exclusive events** — events that cannot occur together; '
      '$P(A \\cap B) = 0$.',
      '**Exhaustive events** — events whose union is the whole sample space; their '
      'probabilities sum to 1.',
      '**Independent events** — the occurrence of one does not affect the probability of the '
      'other; $P(B \\mid A) = P(B)$.',
      '**Dependent events** — the occurrence of one *does* affect the probability of the other.',
      '**Conditional probability $P(B \\mid A)$** — the probability of $B$ given that $A$ has '
      'occurred; "$\\mid$" (or "/") reads "given".',
      '**Union $A \\cup B$** — "$A$ **or** $B$" (or both).',
      '**Intersection $A \\cap B$** — "$A$ **and** $B$".',
      '**Random variable $X$** — a variable whose value is a numerical outcome of a random '
      'experiment; discrete or continuous.',
      '**Probability distribution** — the possible values of $X$ with their probabilities '
      '$p_i$, where $\\sum p_i = 1$.',
      '**Expected value / mathematical expectation $E(X)$** — the long-run average value of '
      '$X$; the mean of its distribution.',
      '**With replacement** — the item is returned before the next draw (draws independent). '
      '**Without replacement** — it is not (draws dependent).',
    ]},
    {'h3': 'Axioms of probability'},
    {'ol': [
      '$0 \\le P(A) \\le 1$ for every event $A$.',
      '$P(S) = 1$.',
      'If $A_1, A_2, \\dots, A_k$ are mutually exclusive, then '
      '$P(A_1 \\cup A_2 \\cup \\dots \\cup A_k) = P(A_1) + P(A_2) + \\dots + P(A_k)$.',
    ]},
    {'h3': 'A. Basic probability'},
    {'fbox': {'h': 'Definitions of probability', 'rows': [
      {'lb': 'Classical', 'tex': 'P(E) = \\dfrac{n(E)}{n(S)} = \\dfrac{r}{n} '
              '= \\dfrac{\\text{favourable outcomes}}{\\text{total equally likely outcomes}}'},
      {'lb': 'Frequency / empirical', 'tex': 'P(E) = \\dfrac{r}{n} \\ \\ (n \\text{ large})'},
      {'lb': 'Complement', 'tex': "P(E') = 1 - P(E)"},
      {'lb': 'Certain / impossible', 'tex': 'P(S) = 1, \\qquad P(\\varnothing) = 0'},
    ]}},
    {'h3': 'B. The addition law ("or", $\\cup$)'},
    {'fbox': {'h': 'Addition law', 'rows': [
      {'lb': 'Any two events',
       'tex': 'P(A \\cup B) = P(A) + P(B) - P(A \\cap B)'},
      {'lb': 'Mutually exclusive events',
       'tex': 'P(A \\cup B) = P(A) + P(B)'},
      {'lb': 'Three events',
       'tex': 'P(A \\cup B \\cup C) = P(A) + P(B) + P(C) - P(A \\cap B) - P(A \\cap C) '
              '- P(B \\cap C) + P(A \\cap B \\cap C)'},
    ]}},
    {'h3': 'C. The multiplication law ("and", $\\cap$)'},
    {'fbox': {'h': 'Multiplication law', 'rows': [
      {'lb': 'Any two events',
       'tex': 'P(A \\cap B) = P(A)\\,P(B \\mid A) = P(B)\\,P(A \\mid B)'},
      {'lb': 'Independent events',
       'tex': 'P(A \\cap B) = P(A)\\,P(B)'},
      {'lb': 'Several independent events',
       'tex': 'P(E_1 \\cap E_2 \\cap \\dots \\cap E_k) = P(E_1)P(E_2)\\cdots P(E_k)'},
      {'lb': 'Conditional probability',
       'tex': 'P(B \\mid A) = \\dfrac{P(A \\cap B)}{P(A)}, \\quad P(A) \\neq 0'},
      {'lb': 'Test for independence',
       'tex': 'A, B \\text{ independent} \\iff P(A \\cap B) = P(A)P(B) '
              '\\iff P(B \\mid A) = P(B)'},
    ]}},
    {'h3': 'D. Counting (from §7.3)'},
    {'fbox': {'h': 'Counting rules', 'rows': [
      {'lb': 'Multiplication principle',
       'tex': '\\text{ways} = m_1 \\times m_2 \\times \\dots \\times m_k'},
      {'lb': 'Factorial', 'tex': 'n! = n(n-1)(n-2)\\cdots 2 \\cdot 1, \\quad 0! = 1'},
      {'lb': 'Permutations (order matters)',
       'tex': '{}^{n}P_r = \\dfrac{n!}{(n-r)!}'},
      {'lb': 'Combinations (order does not matter)',
       'tex': '{}^{n}C_r = \\dfrac{n!}{r!\\,(n-r)!}'},
    ]}},
    {'h3': 'E. Expected value of a discrete random variable'},
    {'fbox': {'h': 'Expectation', 'rows': [
      {'lb': 'Mean', 'tex': 'E(X) = \\mu = \\sum x_i\\,p_i = \\dfrac{\\sum x f(x)}{\\sum f}'},
      {'lb': 'Second moment', 'tex': 'E(X^2) = \\sum x_i^2\\,p_i'},
      {'lb': 'Variance', 'tex': '\\operatorname{Var}(X) = E(X^2) - [E(X)]^2'},
      {'lb': 'Standard deviation', 'tex': '\\sigma_X = \\sqrt{\\operatorname{Var}(X)}'},
      {'lb': 'Equal probabilities → arithmetic mean',
       'tex': 'E(X) = \\dfrac{x_1 + x_2 + \\dots + x_n}{n}'},
    ]}},
    {'fbox': {'h': 'Properties of expectation', 'rows': [
      {'lb': 'Constant $c$', 'tex': 'E(c) = c, \\qquad E(cX) = c\\,E(X)'},
      {'lb': 'Sum', 'tex': 'E(X + Y) = E(X) + E(Y)'},
      {'lb': 'Independent $X, Y$', 'tex': 'E(XY) = E(X)\\,E(Y)'},
    ]}},
    {'note': 'A game / lottery is **fair** when $E(\\text{gain}) = 0$, i.e. the fair price of a '
             'ticket equals the expected winnings.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Classical probability', 'tex': 'P(A) = \\frac{n(A)}{n(S)} = \\frac{r}{n}'},
  {'lb': 'Empirical (frequency) probability', 'tex': 'P(A) = \\frac{r}{n} \\ (n \\text{ large})'},
  {'lb': 'Complement', 'tex': "P(A') = 1 - P(A)"},
  {'lb': 'Addition law (any two events)',
   'tex': 'P(A \\cup B) = P(A) + P(B) - P(A \\cap B)'},
  {'lb': 'Addition law (mutually exclusive)',
   'tex': 'P(A \\cup B) = P(A) + P(B)'},
  {'lb': 'Addition law (three events)',
   'tex': 'P(A\\cup B\\cup C) = P(A)+P(B)+P(C) - P(A\\cap B) - P(A\\cap C) - P(B\\cap C) '
          '+ P(A\\cap B\\cap C)'},
  {'lb': 'Multiplication law (any two events)',
   'tex': 'P(A \\cap B) = P(A)\\,P(B \\mid A) = P(B)\\,P(A \\mid B)'},
  {'lb': 'Multiplication law (independent)', 'tex': 'P(A \\cap B) = P(A)\\,P(B)'},
  {'lb': 'Conditional probability',
   'tex': 'P(B \\mid A) = \\frac{P(A \\cap B)}{P(A)}'},
  {'lb': 'Multiplication principle',
   'tex': '\\text{ways} = m_1 \\times m_2 \\times \\dots \\times m_k'},
  {'lb': 'Factorial', 'tex': 'n! = n(n-1)\\cdots 2\\cdot 1, \\ \\ 0! = 1'},
  {'lb': 'Permutations', 'tex': '{}^nP_r = \\frac{n!}{(n-r)!}'},
  {'lb': 'Combinations', 'tex': '{}^nC_r = \\frac{n!}{r!(n-r)!}'},
  {'lb': 'Expected value (mean)', 'tex': 'E(X) = \\mu = \\sum x_i p_i'},
  {'lb': 'Second moment', 'tex': 'E(X^2) = \\sum x_i^2 p_i'},
  {'lb': 'Variance of X', 'tex': '\\operatorname{Var}(X) = E(X^2) - [E(X)]^2'},
  {'lb': 'Expectation properties',
   'tex': 'E(cX) = cE(X), \\ E(X+Y) = E(X)+E(Y), \\ E(XY) = E(X)E(Y) \\text{ (indep.)}'},
 ],
 'focus':
   'Two or three Section A marks every diet — an addition or multiplication law applied to a small '
   'problem, or an expected value. Section B usually pairs expected value with a decision, where '
   'the commentary on risk carries as many marks as the arithmetic. Learn the distinction between '
   'mutually exclusive and independent well enough to state it in one sentence.',
 'errors': [
   'Adding probabilities of events that are not mutually exclusive without subtracting the overlap.',
   'Multiplying probabilities of dependent events as though they were independent.',
   'Treating mutually exclusive events as independent.',
   'Using permutations where order does not matter.',
   'Reporting an expected value without commenting on the spread of outcomes when a decision is asked for.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Calculate the expected value of rolling a fair six-sided die.',
    'o': ['3', '3.5', '4', '6', '21'],
    'a': 1,
    'w': 'Each face has probability 1/6, so the expected value is the mean of 1 to 6.',
    'calc': 'E(X) = \\frac{1+2+3+4+5+6}{6} = \\frac{21}{6} = 3.5',
    'src': 'Chapter 7.4', 'sec': '7.4'},
   {'q': 'If $P(A) = 0.5$, $P(B) = 0.4$ and $P(A \\cap B) = 0.2$, then $P(A \\cup B)$ is',
    'o': ['0.9', '0.7', '0.2', '1.1', '0.3'],
    'a': 1,
    'w': 'Apply the general addition law, subtracting the overlap so it is not counted twice.',
    'calc': 'P(A \\cup B) = 0.5 + 0.4 - 0.2 = 0.7',
    'src': 'Chapter 7.2', 'sec': '7.2'},
   {'q': 'Two events are mutually exclusive if',
    'o': ['the occurrence of one does not affect the other',
          'they cannot occur at the same time',
          'their probabilities sum to one',
          'they are equally likely',
          'they together cover the sample space'],
    'a': 1,
    'w': 'Mutually exclusive means the events cannot occur together, so $P(A \\cap B) = 0$. '
         'Option A describes independence, which is a different idea.',
    'src': 'Chapter 7.1', 'sec': '7.1'},
   {'q': 'A committee of 3 is to be chosen from 8 people. The number of possible committees is',
    'o': ['24', '56', '336', '512', '120'],
    'a': 1,
    'w': 'Order does not matter in a committee, so this is a combination.',
    'calc': '{}^{8}C_3 = \\frac{8 \\times 7 \\times 6}{3 \\times 2 \\times 1} = 56',
    'src': 'Chapter 7.3', 'sec': '7.3'},
   {'q': 'A bag has 5 red and 3 blue balls. Two are drawn without replacement. The probability '
         'that both are red is',
    'o': ['25/64', '5/14', '15/56', '10/28', '1/2'],
    'a': 1,
    'w': 'Without replacement the second draw is conditional on the first.',
    'calc': 'P = \\frac{5}{8} \\times \\frac{4}{7} = \\frac{20}{56} = \\frac{5}{14}',
    'src': 'Chapter 7.2', 'sec': '7.2'},
   {'q': 'If $P(A) = 0.3$ and $A$ and $B$ are independent with $P(B) = 0.6$, then '
         '$P(A \\cap B)$ is',
    'o': ['0.9', '0.3', '0.18', '0.5', '0'],
    'a': 2,
    'w': 'For independent events the joint probability is the product of the individual '
         'probabilities.',
    'calc': 'P(A \\cap B) = 0.3 \\times 0.6 = 0.18',
    'src': 'Chapter 7.2', 'sec': '7.2'},
  ],
  'theory': [
   {'q': 'Distinguish between mutually exclusive events and independent events, and state the '
         'addition and multiplication laws for each case.',
    'marks': 6,
    'a': [
      {'p': '**Mutually exclusive events** cannot occur at the same time. The occurrence of one '
            'rules out the other, so their intersection is empty:'},
      {'tex': 'P(A \\cap B) = 0'},
      {'p': '**Independent events** are events where the occurrence of one has no effect on the '
            'probability of the other:'},
      {'tex': 'P(B \\mid A) = P(B) \\quad\\text{and so}\\quad P(A \\cap B) = P(A) \\, P(B)'},
      {'h4': 'The laws'},
      {'table': {'head': ['', 'General case', 'Special case'], 'align': 'lll', 'rows': [
        ['Addition ("or")', '$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$',
         'Mutually exclusive: $P(A \\cup B) = P(A) + P(B)$'],
        ['Multiplication ("and")', '$P(A \\cap B) = P(A) \\, P(B \\mid A)$',
         'Independent: $P(A \\cap B) = P(A) \\, P(B)$'],
      ]}},
      {'p': 'The two concepts are often confused but are almost opposites. Two mutually exclusive '
            'events with non-zero probabilities are necessarily **dependent**: knowing that $A$ '
            'has occurred tells you that $B$ certainly has not, so $P(B \\mid A) = 0 \\ne P(B)$.'}],
    'src': 'Chapter 7.1', 'sec': '7.1'},
  ]},
}
