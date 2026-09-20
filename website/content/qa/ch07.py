CH = {
 'n': 7,
 't': 'Probability',
 'brief': 'Sample spaces and events, the classical/frequency/axiomatic approaches to '
          'probability, the addition and multiplication laws, conditional probability, '
          'permutations and combinations, and expected value.',
 'outcomes': [
   'Define probability and identify a sample space',
   'Explain the classical, frequency and axiomatic approaches to estimating a probability',
   'Distinguish mutually exclusive from independent events',
   'Apply the addition and multiplication laws',
   'Compute conditional probabilities',
   'Use permutations and combinations to count outcomes',
   'Compute an expected value and use it to choose between alternatives',
 ],
 'secs': [
  {'n': '7.1', 't': 'Introduction and basic terms', 'b': [
    {'p': 'As various activities of business and life in general depend on chance and risk, the '
          'study of probability theory is an essential tool for making correct decisions. '
          'Probability theory is concerned with chance and calculated risk in the face of '
          'uncertainty, built as a mathematical concept from the study of samples of a '
          'theoretical or imaginary population.'},
    {'h4': 'Uses of probability'},
    {'ul': [
      'Quantitative analysis of problems arising in business and other areas.',
      'The basis of **statistical inference**.',
      'A vital role in **insurance** and **statistical quality control**.',
    ]},
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
    {'h4': 'Two schools of thought on estimating a probability'},
    {'p': 'The study text is explicit that there are **two schools of thought** about the '
          'procedure for getting an estimate of the probability of an event:'},
    {'ol': [
      '**Classical, or *a priori*, approach.** All $n$ trials of the experiment are assumed '
      '**equally likely**, and the possible outcomes **mutually exclusive**. If event $E$ can '
      'occur in $r$ of the $n$ possible ways, $P(E) = r/n$ — computed *before* any trial is run, '
      'from the structure of the experiment itself.',
      '**Frequency, or *a posteriori* (empirical), approach.** After $n$ repetitions of the '
      'experiment, where $n$ is very large, event $E$ is observed to occur in $r$ of them, so '
      '$P(E) = r/n$ — computed *after* the trials, from what was actually observed.',
    ]},
    {'note': 'Both approaches share the same formula ($r/n$) but differ in **when** and **how** '
             'the count is obtained — before any trial (classical) or after many trials '
             '(frequency). A classic exam trap is to be given a scenario and asked which of the '
             'two was used: if the answer counts favourable *possibilities*, it is classical; if '
             'it counts favourable *observed occurrences* over many repetitions, it is frequency.'},
    {'warn': 'Both the classical and frequency approaches run into difficulty because "**equally '
             'likely**" and "**very large**" are vague, relative terms — what counts as large '
             'enough, or as truly equally likely, differs from one person to another. This '
             'difficulty is exactly why a **third**, more rigorous approach — the **axiomatic '
             'approach**, built on set theory — was developed: it defines probability by the '
             'three axioms below instead of appealing to either "equally likely" outcomes or a '
             '"large" number of trials.'},
    {'h4': 'The axiomatic definition'},
    {'p': 'For a sample space $S$ and any event $A$ in it, a real value $P(A)$ exists satisfying '
          'three axioms:'},
    {'ol': [
      '$0 \\le P(A) \\le 1$ for every event $A$.',
      '$P(S) = 1$.',
      'If $A_1, A_2, \\dots, A_k$ are mutually exclusive, $P(A_1 \\cup A_2 \\cup \\dots \\cup A_k) '
      '= P(A_1) + P(A_2) + \\dots + P(A_k)$ — i.e. $P(A)$ is the sum of the probabilities of the '
      'simple events making up $A$.',
    ]},
    {'h4': 'Sample spaces of compound experiments'},
    {'p': 'The sample space of an experiment with more than one step is built up systematically. '
          'A few standard ones, worth recognising on sight:'},
    {'table': {'align': 'll', 'head': ['Experiment', 'Sample space'], 'rows': [
      ['A coin tossed once', '$S = \\{H, T\\}$ — 2 sample points'],
      ['A die tossed once', '$S = \\{1,2,3,4,5,6\\}$ — 6 sample points'],
      ['A coin and a die tossed together',
       'Every (face, coin-result) pairing — $2 \\times 6 = 12$ sample points'],
      ['Two coins and a die tossed together',
       'Every (coin, coin, face) combination — $2 \\times 2 \\times 6 = 24$ sample points'],
      ['Two dice tossed together',
       'Every ordered pair $(i,j)$, $i,j \\in \\{1,\\dots,6\\}$ — $6 \\times 6 = 36$ sample points'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Examples 7.1–7.3 — outcomes, sample space and a first '
      'probability', 'open': True, 'q': [
      {'p': '**7.1** State the outcomes of (i) a fair coin and (ii) an unbiased die. '
            '**7.2** If a fair coin is tossed once, what is the probability of obtaining a Head? '
            '**7.3** If a fair die is rolled once, what is the probability of obtaining an even '
            'number?'}],
      'a': [
      {'p': '**7.1** (i) Coin: $\\{H, T\\}$. (ii) Die: $\\{1,2,3,4,5,6\\}$ — the sample space is '
            'the die\'s own set of outcomes, and (say) 3 is one *sample point* within it.'},
      {'p': '**7.2** $n(E) = 1$ (Head), $n(S) = 2$, so $P(E) = 1/2 = 0.5$.'},
      {'p': '**7.3** $S = \\{1,2,3,4,5,6\\}$, even numbers $E = \\{2,4,6\\}$, so '
            '$P(E) = 3/6 = 0.5$.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 7.4 — the frequency (empirical) approach', 'open': True, 'q': [
      {'p': 'SAO Bank Plc gave out loans to 50 customers and later found that only 10 repaid as '
            'scheduled. Determine the probability of repayment of a loan in that bank.'}],
      'a': [
      {'tex': 'P(\\text{repayment}) = \\frac{\\text{number that repaid}}{\\text{total that took '
              'a loan}} = \\frac{10}{50} = 0.2'},
      {'note': 'This is a **frequency-approach** probability, not classical: the 10-out-of-50 is '
               'an observed outcome after the fact, not a count of equally-likely possibilities '
               'before it.'}]}},
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
    {'h4': 'Recognising independent and dependent events'},
    {'table': {'align': 'll', 'head': ['Independent (occurrence of one leaves the other unaffected)',
      'Dependent (occurrence of one changes the other\'s probability)'], 'rows': [
      ['Obtaining a Head, then a Tail, on two tosses of a coin',
       'Weather conditions and the sales of mineral (soft) drinks'],
      ['A candidate passing QA and passing Economics in the same ATSWA sitting',
       'The drug taken and the rate of recovery from an illness'],
    ]}},
    {'p': 'For independent events, applying independence to the conditional-probability formula '
          'gives $P(E_2 \\mid E_1) = P(E_2)$ — knowing $E_1$ happened tells you nothing new about '
          '$E_2$ — so $P(E_1 \\cap E_2) = P(E_1)\\,P(E_2)$, extending to any number of independent '
          'events: $P(E_1 \\cap E_2 \\cap \\dots \\cap E_k) = P(E_1)P(E_2)\\cdots P(E_k)$.'},
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
    {'eg': {'tag': 'Study text', 't': 'Example 7.10 — replacement changes independence',
      'open': True, 'q': [
      {'p': 'A box contains 6 black and 8 yellow balls. Two successive draws of one ball are made. '
            'Find $P(\\text{first black, second yellow})$ if (a) the first ball is replaced before '
            'the second draw; (b) it is not replaced.'}],
      'a': [
      {'p': '**(a) With replacement — independent events.**'},
      {'tex': "P(B) = \\frac{6}{14} = \\frac{3}{7}, \\quad P(Y) = \\frac{8}{14} = \\frac{4}{7}"},
      {'tex': "P(BY) = P(B)\\times P(Y) = \\frac{3}{7}\\times\\frac{4}{7} = \\frac{12}{49}"},
      {'p': '**(b) Without replacement — the second draw is conditional on the first.**'},
      {'tex': "P(B) = \\frac{6}{14} = \\frac{3}{7}, \\quad P(Y \\mid B) = \\frac{8}{13}"},
      {'tex': "P(BY) = P(B) \\times P(Y \\mid B) = \\frac{3}{7}\\times\\frac{8}{13} = "
              "\\frac{24}{91}"},
      {'note': 'Same balls, same question — but a different answer once replacement is removed, '
               'because removing the first ball changes the total (and, here, the yellow count) '
               'available for the second draw. This is *the* example to reach for when asked to '
               'explain why "with replacement" gives independence and "without" does not.'}]}},
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
          'values, weighted by their probabilities. It need not be an attainable value. For a '
          'continuous random variable with density $f(x)$, $E(X) = \\int_{-\\infty}^{\\infty} '
          'xf(x)\\,dx$. A special case: when every outcome is equally likely, $E(X)$ collapses '
          'to the plain arithmetic mean $(x_1+x_2+\\cdots+x_n)/n$.'},
    {'h4': 'Properties of expectation'},
    {'ol': [
      '$E(cX) = c\\,E(X)$ for any constant $c$.',
      '$E(X+Y) = E(X) + E(Y)$ for any random variables $X, Y$.',
      '$E(XY) = E(X)\\,E(Y)$ if $X$ and $Y$ are **independent**.',
    ]},
    {'eg': {'t': 'Expected value of a die', 'q': [
      {'p': 'Calculate the expected value of rolling a fair six-sided die.'}],
      'a': [
      {'tex': 'E(X) = \\sum x p = (1 + 2 + 3 + 4 + 5 + 6) \\times \\frac{1}{6} '
              '= \\frac{21}{6} = 3.5'},
      {'note': 'A die can never show 3.5. The expected value is the average over many throws, not '
               'a prediction of any single one.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 7.13 — $E(X)$, $E(X^2)$ and standard deviation from '
      'a distribution', 'open': True, 'q': [
      {'table': {'align': 'lrrrrr', 'head': ['$X$', '6', '10', '14', '18', '22'],
        'rows': [['$P(X)$', '1/6', '5/36', '1/4', '1/3', '1/9']]}},
      {'p': 'Find (a) $E(X)$, (b) $E(X^2)$, (c) the standard deviation of $X$.'}],
      'a': [
      {'p': '**(a)**'},
      {'tex': "E(X) = \\textstyle\\sum xP(x) = 6(\\frac16) + 10(\\frac{5}{36}) + 14(\\frac14) "
              "+ 18(\\frac13) + 22(\\frac19) = 1 + 1.389 + 3.5 + 6 + 2.444 = 14.333"},
      {'p': '**(b)**'},
      {'tex': "E(X^2) = \\textstyle\\sum x^2P(x) = 36(\\frac16) + 100(\\frac{5}{36}) + "
              "196(\\frac14) + 324(\\frac13) + 484(\\frac19) = 6 + 13.889 + 49 + 108 + 53.778 "
              "= 230.667"},
      {'p': '**(c)**'},
      {'tex': "\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 230.667 - 14.333^2 = 230.667 - "
              "205.444 = 25.22"},
      {'tex': "\\sigma_X = \\sqrt{25.22} = 5.02"}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 7.14 — the fair price of a lottery ticket',
      'open': True, 'q': [
      {'p': 'A company runs a lottery with 200 prizes of ₦50, 20 prizes of ₦250 and 5 prizes of '
            '₦1,000, out of 10,000 tickets issued. Determine the fair price of a ticket.'}],
      'a': [
      {'p': 'The probability of each outcome is its count of tickets over the 10,000 issued, with '
            'the remaining $10{,}000-225=9{,}775$ tickets winning nothing:'},
      {'table': {'align': 'lrrrr', 'head': ['Prize $X$ (₦)', '50', '250', '1,000', '0'],
        'rows': [['$P(X)$', '0.02', '0.002', '0.0005', '0.9775']]}},
      {'tex': "\\text{Fair price} = E(X) = 50(0.02) + 250(0.002) + 1000(0.0005) + 0(0.9775) = "
              "1 + 0.5 + 0.5 + 0 = \\text{\\textnaira}2"},
      {'note': 'A "fair" price is exactly $E(X)$ — the price at which neither the ticket-buyer '
               'nor the company gains on average. See the fair-game note at the end of this '
               'chapter.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 7.15 — expected value of the sum of two dice',
      'open': True, 'q': [
      {'p': 'Determine the expected value of the sum of points shown when a pair of fair dice is '
            'tossed.'}],
      'a': [
      {'p': '**Direct method** — the sum $X$ ranges from 2 to 12 with these probabilities (out of '
            '36 equally likely pairs):'},
      {'table': {'align': 'r'*11,
        'head': ['2','3','4','5','6','7','8','9','10','11','12'],
        'rows': [['1/36','2/36','3/36','4/36','5/36','6/36','5/36','4/36','3/36','2/36','1/36']]}},
      {'tex': "E(X) = \\textstyle\\sum xP(x) = 2(\\frac1{36}) + 3(\\frac2{36}) + \\cdots + "
              "12(\\frac1{36}) = 7"},
      {'p': '**Shortcut, using the sum property.** Let $X, Y$ be the two dice separately, each '
            'with $E(X) = E(Y) = 1(\\frac16)+2(\\frac16)+\\cdots+6(\\frac16) = 3.5$. Since the '
            'sum of the points is $X + Y$:'},
      {'tex': "E(X+Y) = E(X) + E(Y) = 3.5 + 3.5 = 7"},
      {'note': 'The shortcut uses property (b) of expectation — $E(X+Y)=E(X)+E(Y)$ — and needs '
               'no joint distribution at all, however many dice are involved.'}]}},
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
      '**§7.1 Introduction and basic terms** — probability theory\'s uses (quantitative '
      'analysis, basis of statistical inference, insurance/quality control); the **two schools '
      'of thought** on estimating a probability — classical/*a priori* (equally-likely outcomes '
      'counted *before* any trial) and frequency/*a posteriori* (observed rate *after* many '
      'trials) — and why their shared reliance on the vague terms "equally likely"/"very large" '
      'led to a third, **axiomatic** approach built on the three axioms instead; experiment, '
      'sample space $S$ (all outcomes), event (a subset of $S$), mutually exclusive '
      '($P(A\\cap B)=0$), exhaustive (covers all of $S$), independent ($P(A\\cap B)=P(A)P(B)$), '
      'complement ($P(A\')=1-P(A)$); $P(A)=$ favourable ÷ total equally-likely outcomes, '
      '$0\\le P(A)\\le1$; standard compound sample spaces (coin+die = 12 points, two dice = 36). '
      '**Mutually exclusive is not independent** — in fact two such events (with non-zero '
      'probability) are strongly *dependent*, since one occurring guarantees the other does not.',
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
      '**§7.6 End-of-chapter questions (study text)** — the study text\'s own 10-item MCQ/'
      'short-answer bank with the official answers, on classical probability from a listed set, '
      'lottery-prize probabilities, and probabilities from a mixed-colour box of balls.',
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

  {'n': '7.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'p': 'Questions 1–3 use the set $S = \\{2, 4, 7, 10, 13, 16, 22, 27, 81, 102\\}$. If a '
            'number is picked at random, determine the probability that it is:'},
      {'ol': [
        'even (A) 0.4  (B) 0.2  (C) 0.6  (D) 0.8  (E) 0.9',
        'odd (A) 0.4  (B) 0.8  (C) 0.2  (D) 0.9  (E) 0.6',
        'prime (A) 0.2  (B) 0.5  (C) 0.3  (D) 0.6  (E) 0.4',
      ]},
      {'p': 'Questions 4–5: a lottery issues 2,000 tickets, with 5 major and 50 minor prizes to '
            'be won. If a ticket is bought, the probability that it wins:'},
      {'ol': [
        'a major prize (A) 0.25  (B) 0.025  (C) 0.0025  (D) 0.5  (E) 0.05',
        'a minor prize (A) 0.25  (B) 0.025  (C) 0.0025  (D) 0.5  (E) 0.05',
      ]},
      {'ol': [
        'Using the items in question 4 and 5, the probability of winning **a** prize in the '
        'lottery game is …',
        'The list of all possible outcomes in a random experiment is called its …',
      ]},
      {'p': 'Questions 8–10: a ball is selected at random from a box containing 6 white, 4 blue '
            'and 5 red balls. Obtain the probability that:'},
      {'ol': [
        'a white ball is selected',
        'a ball that is **not** white is selected',
        'a blue **or** a red ball is selected',
      ]},
      ],
      'a': [
      {'ol': [
        '**C — 0.6.** 6 of the 10 numbers (2, 4, 10, 16, 22, 102) are even.',
        '**A — 0.4.** 4 of the 10 (7, 13, 27, 81) are odd.',
        '**C — 0.3.** 3 of the 10 (2, 7, 13) are prime.',
        '**C — 0.0025** — $5/2000$.',
        '**B — 0.025** — $50/2000$.',
        '**0.0275** — $5/2000 + 50/2000 = 55/2000 = 0.0275$.',
        '**Sample space.**',
        '**0.4** — $\\Pr(\\text{white}) = 6/15$.',
        '**0.6** — $1 - \\Pr(\\text{white}) = 1 - 0.4$.',
        '**0.6** — $\\Pr(\\text{blue or red}) = 4/15 + 5/15 = 9/15$.',
      ]}]}},
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
   {'q': 'The two schools of thought on the procedure for estimating the probability of an '
         'event are the classical (a priori) approach and the',
    'o': ['subjective approach', 'axiomatic approach', 'frequency (a posteriori) approach',
          'Bayesian approach', 'combinatorial approach'],
    'a': 2,
    'w': 'Classical/a priori counts equally-likely outcomes before any trial; frequency/a '
         'posteriori counts observed occurrences after many repetitions. The axiomatic '
         'approach is a later, third approach, developed because both of these rely on the '
         'vague terms "equally likely" and "very large".',
    'src': 'Chapter 7.1', 'sec': '7.1'},
   {'q': 'The axiomatic approach to probability was developed mainly because the classical '
         'and frequency approaches both rely on',
    'o': ['expensive computer software', 'the vague terms "equally likely" and "very large"',
          'continuous random variables only', 'permutations rather than combinations',
          'sample spaces with a single outcome'],
    'a': 1,
    'w': '"Equally likely" and "very large" are relative, vague terms — the axiomatic approach '
         'avoids them by defining probability through three axioms built on set theory instead.',
    'src': 'Chapter 7.1', 'sec': '7.1'},
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
