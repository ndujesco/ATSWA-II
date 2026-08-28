CH = {
 'n': 10,
 't': 'Set Theory',
 'brief': 'Set notation and operations, Venn diagrams, De Morgan\'s laws, and the counting '
          'formulae for two and three overlapping sets.',
 'outcomes': [
   'Use set notation and describe sets by listing or by rule',
   'Perform union, intersection, difference and complement',
   'Represent a problem on a Venn diagram',
   'Apply the inclusion–exclusion formula for two and three sets',
   'State and use De Morgan\'s laws',
 ],
 'secs': [
  {'n': '10.1', 't': 'Notation and basic operations', 'b': [
    {'ul': [
      '**Set** — a well-defined collection of distinct objects, written '
      '$A = \\{1, 2, 3\\}$ or by rule $A = \\{x : x \\text{ is even}\\}$.',
      '**Element**: $x \\in A$ means $x$ belongs to $A$; $x \\notin A$ means it does not.',
      '**Universal set $U$** — all elements under consideration in the problem.',
      '**Empty (null) set $\\varnothing$** — the set with no elements. Note '
      '$\\varnothing \\ne \\{0\\}$ and $\\varnothing \\ne \\{\\varnothing\\}$.',
      '**Subset**: $A \\subseteq B$ if every element of $A$ is in $B$. Proper subset '
      '$A \\subset B$ additionally requires $A \\ne B$.',
      '**Cardinality $n(A)$** — the number of elements in $A$.',
      '**Disjoint** sets have no element in common: $A \\cap B = \\varnothing$.',
    ]},
    {'fbox': {'h': 'Operations', 'rows': [
      {'lb': 'Union — in $A$ or $B$ or both',
       'tex': 'A \\cup B = \\{x : x \\in A \\text{ or } x \\in B\\}'},
      {'lb': 'Intersection — in both',
       'tex': 'A \\cap B = \\{x : x \\in A \\text{ and } x \\in B\\}'},
      {'lb': 'Complement — in $U$ but not in $A$',
       'tex': "A' = \\{x \\in U : x \\notin A\\}"},
      {'lb': 'Difference — in $A$ but not in $B$',
       'tex': "A - B = A \\cap B'"},
      {'lb': 'Number of subsets of a set of $n$ elements',
       'tex': '2^{n}'},
    ]}},
    {'eg': {'t': 'Operations on small sets', 'q': [
      {'p': 'Given $U = \\{1,2,3,4,5,6,7,8,9,10\\}$, $A = \\{1,2,3,4,5\\}$ and '
            '$B = \\{4,5,6,7\\}$, find $A \\cup B$, $A \\cap B$, $A - B$, $A\'$ and '
            '$n(A \\cup B)$.'}],
      'a': [
      {'tex': 'A \\cup B = \\{1,2,3,4,5,6,7\\}'},
      {'tex': 'A \\cap B = \\{4,5\\}'},
      {'tex': 'A - B = \\{1,2,3\\}'},
      {'tex': "A' = \\{6,7,8,9,10\\}"},
      {'p': 'By counting, $n(A \\cup B) = 7$. By formula:'},
      {'tex': 'n(A \\cup B) = n(A) + n(B) - n(A \\cap B) = 5 + 4 - 2 = 7'}]}},
  ]},

  {'n': '10.2', 't': 'Laws of set algebra', 'b': [
    {'table': {'align': 'll', 'head': ['Law', 'Statement'], 'rows': [
      ['Commutative', '$A \\cup B = B \\cup A$;  $A \\cap B = B \\cap A$'],
      ['Associative', '$(A \\cup B) \\cup C = A \\cup (B \\cup C)$'],
      ['Distributive', '$A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C)$'],
      ['Identity', '$A \\cup \\varnothing = A$;  $A \\cap U = A$'],
      ['Complement', '$A \\cup A\' = U$;  $A \\cap A\' = \\varnothing$'],
      ['Idempotent', '$A \\cup A = A$;  $A \\cap A = A$'],
      ['De Morgan', '$(A \\cup B)\' = A\' \\cap B\'$;  $(A \\cap B)\' = A\' \\cup B\''],
    ]}},
    {'key': '**De Morgan\'s laws** are the ones examiners ask for by name. In words: the '
            'complement of a union is the intersection of the complements, and the complement '
            'of an intersection is the union of the complements. "Not (A or B)" means "not A '
            'and not B".'},
  ]},

  {'n': '10.3', 't': 'Counting with Venn diagrams', 'b': [
    {'fbox': {'h': 'Inclusion–exclusion', 'rows': [
      {'lb': 'Two sets',
       'tex': 'n(A \\cup B) = n(A) + n(B) - n(A \\cap B)'},
      {'lb': 'Three sets',
       'tex': 'n(A \\cup B \\cup C) = n(A) + n(B) + n(C) - n(A \\cap B) - n(A \\cap C) '
              '- n(B \\cap C) + n(A \\cap B \\cap C)'},
      {'lb': 'Neither / none',
       'tex': "n\\big((A \\cup B)'\\big) = n(U) - n(A \\cup B)"},
    ]}},
    {'p': 'The pattern is alternating: add the singles, subtract the pairs, add the triple. '
          'Elements in two sets have been counted twice and must be removed once; elements in '
          'all three were counted three times and removed three times, so one addition restores '
          'them.'},
    {'eg': {'t': 'Two sets', 'q': [
      {'p': 'In a survey of 100 households, 70 read *The Guardian*, 55 read *The Punch*, and 10 '
            'read neither. How many read both papers?'}],
      'a': [
      {'p': 'Those who read at least one paper:'},
      {'tex': 'n(G \\cup P) = 100 - 10 = 90'},
      {'p': 'Substitute into the two-set formula and solve for the overlap:'},
      {'tex': '90 = 70 + 55 - n(G \\cap P)'},
      {'tex': 'n(G \\cap P) = 125 - 90 = 35'},
      {'p': '**35 households read both papers.** As a check, *Guardian* only $= 70 - 35 = 35$, '
            '*Punch* only $= 55 - 35 = 20$, both $= 35$, neither $= 10$; total '
            '$35 + 20 + 35 + 10 = 100$. ✓'}]}},

    {'eg': {'t': 'Three sets', 'q': [
      {'p': 'Of 100 students, 60 offer Mathematics, 45 offer Accounting and 30 offer Economics. '
            '25 offer Mathematics and Accounting, 20 offer Mathematics and Economics, 15 offer '
            'Accounting and Economics, and 10 offer all three. Find the number who offer '
            '(a) at least one subject; (b) none of the three; (c) exactly one subject; '
            '(d) exactly two subjects.'}],
      'a': [
      {'p': '**(a)** Apply inclusion–exclusion:'},
      {'tex': 'n(M \\cup A \\cup E) = 60 + 45 + 30 - 25 - 20 - 15 + 10 = 85'},
      {'p': '**(b)** None of the three:'},
      {'tex': '100 - 85 = 15'},
      {'p': '**(c)** Work outwards from the centre. Each "only" region is the set less the two '
            'pairwise overlaps, plus the triple back (it was removed twice):'},
      {'tex': '\\text{Maths only} = 60 - 25 - 20 + 10 = 25'},
      {'tex': '\\text{Accounting only} = 45 - 25 - 15 + 10 = 15'},
      {'tex': '\\text{Economics only} = 30 - 20 - 15 + 10 = 5'},
      {'tex': '\\text{Exactly one} = 25 + 15 + 5 = 45'},
      {'p': '**(d)** Each pairwise region excluding the centre:'},
      {'tex': '(25 - 10) + (20 - 10) + (15 - 10) = 15 + 10 + 5 = 30'},
      {'p': 'Final check — the seven regions plus "none" must total the universal set:'},
      {'table': {'align': 'lr', 'head': ['Region', 'Number'], 'rows': [
        ['Mathematics only', '25'],
        ['Accounting only', '15'],
        ['Economics only', '5'],
        ['Mathematics and Accounting only', '15'],
        ['Mathematics and Economics only', '10'],
        ['Accounting and Economics only', '5'],
        ['All three', '10'],
        ['None', '15'],
        ['Total', '100'],
      ]}},
      {'note': 'Always fill a three-set Venn diagram **from the centre outwards**. Writing the '
               '10 in the middle first, then reducing each pairwise figure by 10, then each '
               'single figure by the three numbers already placed, removes every chance of '
               'double counting.'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Union of two sets',
   'tex': 'n(A \\cup B) = n(A) + n(B) - n(A \\cap B)'},
  {'lb': 'Union of three sets',
   'tex': 'n(A\\cup B\\cup C) = \\sum n(A) - \\sum n(A\\cap B) + n(A\\cap B\\cap C)'},
  {'lb': 'Complement', 'tex': "n(A') = n(U) - n(A)"},
  {'lb': "De Morgan (union)", 'tex': "(A \\cup B)' = A' \\cap B'"},
  {'lb': "De Morgan (intersection)", 'tex': "(A \\cap B)' = A' \\cup B'"},
  {'lb': 'Number of subsets', 'tex': '2^n'},
 ],
 'focus':
   'One Section A mark most diets — a two-set counting problem, the number of subsets, or the '
   'statement of De Morgan\'s laws. Three-set Venn problems appear in Section B from time to '
   'time and are pure marks if the diagram is filled from the centre outwards.',
 'errors': [
   'Reading "25 offer Mathematics and Accounting" as "25 offer only those two" — it includes '
   'those who also offer the third subject.',
   'Forgetting to add back the triple intersection in the three-set formula.',
   'Confusing $\\varnothing$ with $\\{0\\}$; the latter has one element.',
   'Filling a Venn diagram from the outside in, which double counts the overlaps.',
   'Omitting the "neither" region when the universal set total is given.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'If $n(A) = 20$, $n(B) = 15$ and $n(A \\cap B) = 5$, then $n(A \\cup B)$ is',
    'o': ['40', '30', '35', '25', '10'],
    'a': 1,
    'w': 'Add the two sets and subtract the overlap, which would otherwise be counted twice.',
    'calc': 'n(A \\cup B) = 20 + 15 - 5 = 30',
    'src': 'Chapter 10.3'},
   {'q': 'The number of subsets of a set containing 5 elements is',
    'o': ['10', '32', '25', '5', '120'],
    'a': 1,
    'w': 'Each element is either in or out of a subset, giving $2^5$ possibilities.',
    'calc': '2^{5} = 32',
    'src': 'Chapter 10.1'},
   {'q': 'De Morgan\'s law states that $(A \\cup B)\'$ equals',
    'o': ["$A' \\cup B'$", "$A' \\cap B'$", "$A \\cap B$", "$A' - B'$", "$U - A$"],
    'a': 1,
    'w': 'The complement of a union is the intersection of the complements: "not (A or B)" is '
         '"not A and not B".',
    'src': 'Chapter 10.2'},
   {'q': 'In a class of 40, 25 study French and 18 study German. If 5 study neither, the number '
         'studying both is',
    'o': ['13', '8', '7', '12', '10'],
    'a': 1,
    'w': 'Those studying at least one language number $40 - 5 = 35$; substitute in the '
         'inclusion–exclusion formula.',
    'calc': '35 = 25 + 18 - n(F \\cap G) \\Rightarrow  n(F \\cap G) = 43 - 35 = 8',
    'src': 'Chapter 10.3'},
   {'q': 'Two sets with no element in common are said to be',
    'o': ['equal', 'disjoint', 'universal', 'equivalent', 'complementary'],
    'a': 1,
    'w': 'Disjoint sets satisfy $A \\cap B = \\varnothing$.',
    'src': 'Chapter 10.1'},
  ],
  'theory': [
   {'q': 'In a survey of 120 employees, 62 belong to the pension scheme, 55 to the medical '
         'scheme and 40 to the housing scheme. 28 belong to both the pension and medical '
         'schemes, 22 to the pension and housing schemes, 18 to the medical and housing '
         'schemes, and 12 belong to all three. Determine the number of employees who belong to '
         '(a) at least one scheme, (b) no scheme, (c) exactly one scheme, and (d) exactly two '
         'schemes.',
    'marks': 12,
    'a': [
      {'p': 'Let $P$, $M$ and $H$ denote membership of the pension, medical and housing schemes '
            'respectively. The data are:'},
      {'tex': 'n(U) = 120, \\quad n(P) = 62, \\quad n(M) = 55, \\quad n(H) = 40'},
      {'tex': 'n(P \\cap M) = 28, \\quad n(P \\cap H) = 22, \\quad n(M \\cap H) = 18, '
              '\\quad n(P \\cap M \\cap H) = 12'},
      {'h4': '(a) At least one scheme'},
      {'tex': 'n(P \\cup M \\cup H) = n(P) + n(M) + n(H) - n(P\\cap M) - n(P\\cap H) '
              '- n(M\\cap H) + n(P\\cap M\\cap H)'},
      {'tex': '= 62 + 55 + 40 - 28 - 22 - 18 + 12 = 101'},
      {'p': '**101 employees belong to at least one scheme.**'},
      {'h4': '(b) No scheme'},
      {'tex': '120 - 101 = 19'},
      {'h4': '(c) Exactly one scheme'},
      {'p': 'Build each region from the centre outwards. For "pension only", remove both '
            'pairwise overlaps and add the triple back, since it was removed twice:'},
      {'tex': '\\text{Pension only} = 62 - 28 - 22 + 12 = 24'},
      {'tex': '\\text{Medical only} = 55 - 28 - 18 + 12 = 21'},
      {'tex': '\\text{Housing only} = 40 - 22 - 18 + 12 = 12'},
      {'tex': '\\text{Exactly one} = 24 + 21 + 12 = 57'},
      {'h4': '(d) Exactly two schemes'},
      {'p': 'Each pairwise figure includes those in all three, so deduct 12 from each:'},
      {'tex': '(28 - 12) + (22 - 12) + (18 - 12) = 16 + 10 + 6 = 32'},
      {'h4': 'Check'},
      {'table': {'align': 'lr', 'head': ['Region', 'Employees'], 'rows': [
        ['Pension only', '24'],
        ['Medical only', '21'],
        ['Housing only', '12'],
        ['Pension and medical only', '16'],
        ['Pension and housing only', '10'],
        ['Medical and housing only', '6'],
        ['All three schemes', '12'],
        ['No scheme', '19'],
        ['Total', '120'],
      ]}},
      {'p': 'The eight mutually exclusive regions sum to 120, confirming the working. Note also '
            'that exactly one (57) plus exactly two (32) plus all three (12) gives 101, which '
            'agrees with part (a).'},
      {'note': 'Marks in this question are given for the diagram as well as the arithmetic. '
               'Draw three overlapping circles, write 12 in the central region first, then the '
               'three pairwise regions, then the three "only" regions, and finally the 19 '
               'outside the circles but inside the rectangle representing $U$.'}],
    'src': 'Chapter 10.3'},
  ]},
}
