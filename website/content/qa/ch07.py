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
 ],
 'formulas': [
  {'lb': 'Classical probability',
   'tex': 'P(A) = \\frac{n(A)}{n(S)}'},
  {'lb': 'Addition law',
   'tex': 'P(A \\cup B) = P(A) + P(B) - P(A \\cap B)'},
  {'lb': 'Multiplication law',
   'tex': 'P(A \\cap B) = P(A) \\, P(B \\mid A)'},
  {'lb': 'Independence', 'tex': 'P(A \\cap B) = P(A) P(B)'},
  {'lb': 'Conditional probability',
   'tex': 'P(B \\mid A) = \\frac{P(A \\cap B)}{P(A)}'},
  {'lb': 'Permutations', 'tex': '{}^nP_r = \\frac{n!}{(n-r)!}'},
  {'lb': 'Combinations', 'tex': '{}^nC_r = \\frac{n!}{r!(n-r)!}'},
  {'lb': 'Expected value', 'tex': 'E(X) = \\sum x_i p_i'},
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
    'src': 'Chapter 7.4'},
   {'q': 'If $P(A) = 0.5$, $P(B) = 0.4$ and $P(A \\cap B) = 0.2$, then $P(A \\cup B)$ is',
    'o': ['0.9', '0.7', '0.2', '1.1', '0.3'],
    'a': 1,
    'w': 'Apply the general addition law, subtracting the overlap so it is not counted twice.',
    'calc': 'P(A \\cup B) = 0.5 + 0.4 - 0.2 = 0.7',
    'src': 'Chapter 7.2'},
   {'q': 'Two events are mutually exclusive if',
    'o': ['the occurrence of one does not affect the other',
          'they cannot occur at the same time',
          'their probabilities sum to one',
          'they are equally likely',
          'they together cover the sample space'],
    'a': 1,
    'w': 'Mutually exclusive means the events cannot occur together, so $P(A \\cap B) = 0$. '
         'Option A describes independence, which is a different idea.',
    'src': 'Chapter 7.1'},
   {'q': 'A committee of 3 is to be chosen from 8 people. The number of possible committees is',
    'o': ['24', '56', '336', '512', '120'],
    'a': 1,
    'w': 'Order does not matter in a committee, so this is a combination.',
    'calc': '{}^{8}C_3 = \\frac{8 \\times 7 \\times 6}{3 \\times 2 \\times 1} = 56',
    'src': 'Chapter 7.3'},
   {'q': 'A bag has 5 red and 3 blue balls. Two are drawn without replacement. The probability '
         'that both are red is',
    'o': ['25/64', '5/14', '15/56', '10/28', '1/2'],
    'a': 1,
    'w': 'Without replacement the second draw is conditional on the first.',
    'calc': 'P = \\frac{5}{8} \\times \\frac{4}{7} = \\frac{20}{56} = \\frac{5}{14}',
    'src': 'Chapter 7.2'},
   {'q': 'If $P(A) = 0.3$ and $A$ and $B$ are independent with $P(B) = 0.6$, then '
         '$P(A \\cap B)$ is',
    'o': ['0.9', '0.3', '0.18', '0.5', '0'],
    'a': 2,
    'w': 'For independent events the joint probability is the product of the individual '
         'probabilities.',
    'calc': 'P(A \\cap B) = 0.3 \\times 0.6 = 0.18',
    'src': 'Chapter 7.2'},
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
    'src': 'Chapter 7.1'},
  ]},
}
