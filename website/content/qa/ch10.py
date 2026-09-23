CH = {
 'n': 10,
 't': 'Set Theory as Applied to Business',
 'brief': 'Sets, their elements and the roster/property methods of specifying them; the types of '
          'sets and the basic operations (union, intersection, complement); and solving '
          'business-oriented problems — for two and three overlapping groups — using Euler-Venn '
          'diagrams.',
 'outcomes': [
   'Understand the concept of set theory',
   'Understand the relevant terms in set theory',
   'Solve business-oriented problems based on set theory using Euler-Venn diagrams',
 ],
 'secs': [
  {'n': '10.1', 't': 'Introduction', 'b': [
    {'p': 'In real life, arranging and collecting objects or people according to their common '
          'properties or characteristics is part of day-to-day activity — for example, the '
          'arrangement of chartered accountants in an accounting firm\'s register by their '
          'membership number, or the types of animals kept in a zoo. Each such collection is '
          'known as a **set**, and the objects in the set are called **elements** or **members**.'},
  ]},

  {'n': '10.2', 't': 'Relevant terms in set theory', 'b': [
    {'def': {'t': 'Set', 'd': 'a collection of well-defined objects, things or units. The '
                  'objects — called members or elements — must be well defined, so that it can '
                  'be determined whether a particular object belongs to the set or not.'}},
    {'p': 'Examples of a set: the set of all integer numbers; the set of accountancy students in '
          'a university; the set of ATS candidates in Ghana.'},
    {'p': 'By convention, a set is denoted by a **capital letter**, and an element by a **small '
          'letter**. The symbols used are:'},
    {'ul': [
      '$\\{ \\dots \\}$ to represent a set;',
      '$b \\in B$ means "$b$ belongs to $B$"; and',
      '$b \\notin B$ means "$b$ does not belong to $B$".',
    ]},
    {'p': 'A set is completely specified in one of two ways:'},
    {'ol': [
      'By actually **listing** all its elements — the **roster method**, e.g. '
      '$A = \\{1,2,3,4,5,6\\}$, $B = \\{a,b,c,d\\}$; or',
      'By **describing a property** held by all elements in the set — the **property method**, '
      'e.g. $A = \\{x : x \\text{ is an integer}\\}$.',
    ]},
    {'note': 'The curly bracket $\\{\\ \\}$ is always used to represent a set.'},
    {'h4': 'Types of sets'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning'], 'rows': [
      ['**Finite / infinite**', 'A set is finite if its number of elements is countable; '
       'otherwise it is infinite. $A=\\{\\text{odd numbers between 0 and 12}\\}$ is finite; '
       '$B=\\{1,2,3,\\dots\\}$ is infinite.'],
      ['**Cardinality (number of elements)**', 'For a finite set $A$, the number of elements is '
       'denoted $n(A)$. If $A=\\{1,4,7,8,5,6\\}$, then $n(A)=6$.'],
      ['**Empty / null set**', 'A set with no element, denoted $\\{\\ \\}$. E.g. the set of '
       'integers that are both odd and even is empty.'],
      ['**Universal set**', 'The collection of all conceivable objects under consideration, '
       'denoted $U$. E.g. $U=\\{\\text{all English alphabets}\\}$; '
       '$U=\\{\\text{all candidates writing a particular diet of ATS examination}\\}$.'],
      ['**Subset**', 'If every element of $A$ is contained in $B$, $A$ is a subset of $B$: '
       '$A \\subseteq B$ (or $B \\supseteq A$, read "$B$ is a superset of $A$"). If every '
       'element of $A$ is also an element of $B$ **and** vice versa, $A$ and $B$ are equal '
       'sets.'],
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Subsets and equal sets', 'open': True, 'q': [
      {'p': '(i) $A=\\{1,2,3\\}$ and $B=\\{3,2,1\\}$. (ii) $D=\\{a,b,c\\}$ and $F=\\{a,e,c,b\\}$. '
            'Describe the relationship in each case.'}],
      'a': [
      {'p': '(i) $A = B$ — every element of each is in the other.'},
      {'p': '(ii) $D$ is a subset of $F$: $D \\subseteq F$.'}]}},
    {'h4': 'Basic set operations'},
    {'ul': [
      '**Union ($A \\cup B$)** — the set of all elements belonging to either $A$ or $B$ or '
      'both.',
      '**Intersection ($A \\cap B$)** — the set of all elements belonging to both $A$ and $B$.',
      '**Complement ($A\'$ or $A^c$)** — the set of all elements in the universal set $U$ but '
      'not in $A$.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 10.1 — listing the elements of a set',
      'open': True, 'q': [
      {'p': 'List the elements of each of the following sets: (a) '
            '$X=\\{\\text{odd numbers between 0 and 10}\\}$; (b) '
            '$Y=\\{\\text{odd numbers less than 20}\\}$; (c) '
            '$Z=\\{\\text{even numbers between 9 and 31}\\}$.'}],
      'a': [
      {'p': '(a) $X = \\{1,3,5,7,9\\}$'},
      {'p': '(b) $Y = \\{1,3,5,7,9,11,13,15,17,19\\}$'},
      {'p': '(c) $Z = \\{10,12,14,16,18,20,22,24,26,28,30\\}$'}]}},
  ]},

  {'n': '10.3', 't': 'Applications to business-oriented problems using Euler-Venn diagrams', 'b': [
    {'p': 'The Euler-Venn diagram was developed by both Euler and John Venn. It is a '
          'pictorial/diagrammatical representation of sets, and provides a relationship between '
          'or among sets, especially when set operations are involved. By convention, the '
          'universal set $U$ is represented by the set of points inside a **rectangle**, and '
          'other subsets by sets of points inside **circles**.'},
    {'eg': {'tag': 'Study text', 't': 'Example 10.2 — a two-set trader problem', 'open': True,
      'q': [
      {'p': 'In a market of 50 traders, 25 sell either Tubers of yam ($T$) or Onions ($O$). Of '
            'these, 4 sell both, and 6 traders sell onions. Using (a) set notation and (b) an '
            'Euler-Venn diagram, find how many traders sell (i) tubers of yam; (ii) tubers of '
            'yam but not onions; and (iii) neither tubers of yam nor onions.'}],
      'a': [
      {'p': 'Let $U$ stand for all the traders: $n(U)=50$, $n(O)=6$, $n(T \\cap O)=4$, '
            '$n(T \\cup O)=25$.'},
      {'h4': '(a) By set notation'},
      {'tex': 'n(T \\cup O) = n(T) + n(O) - n(T \\cap O) \\;\\Rightarrow\\; 25 = n(T) + 6 - 4 '
              '\\;\\Rightarrow\\; n(T) = 23'},
      {'tex': '(ii)\\ n(T \\text{ only}) = n(T) - n(T \\cap O) = 23 - 4 = 19'},
      {'tex': '(iii)\\ n(\\text{neither}) = n(U) - n(T \\cup O) = 50 - 25 = 25'},
      {'h4': '(b) By Euler-Venn diagram'},
      {'p': 'Filling the diagram: onions only $= n(O) - n(T \\cap O) = 6 - 4 = 2$; tubers only '
            '$= 19$; both $= 4$; outside both circles $= 50 - (19+4+2) = 25$. This gives '
            '(i) $n(T) = 19+4 = 23$; (ii) tubers only $=19$; (iii) neither $=25$ — matching (a) '
            'exactly.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 10.3 — a two-set bank-account problem, solved '
      'algebraically', 'open': True, 'q': [
      {'p': 'Each of 40 staff at a company operates no account, or at least one account, at FAO '
            'Microfinance Bank. 15 operate savings account only, 9 operate current account only, '
            'and 5 operate neither. (a) Draw the Euler-Venn diagram. (b) Calculate the number of '
            'staff that operate (i) both types of account; (ii) savings account; (iii) current '
            'account; (iv) at least one type of account.'}],
      'a': [
      {'p': 'Let $S$ = savings account, $C$ = current account. $n(U)=40$, '
            '$n(S \\cap C\')=15$ (savings only), $n(S\' \\cap C)=9$ (current only), '
            '$n(S\' \\cap C\')=5$ (neither). Let $n(S \\cap C) = x$ (both, unknown).'},
      {'tex': 'n(U) = 15 + x + 9 + 5 \\;\\Rightarrow\\; 40 = 29 + x \\;\\Rightarrow\\; x = 11'},
      {'p': '(i) **11 staff operate both accounts.**'},
      {'tex': '(ii)\\ n(S) = 15 + 11 = 26 \\qquad (iii)\\ n(C) = 11 + 9 = 20'},
      {'tex': '(iv)\\ n(S \\cup C) = 15 + 11 + 9 = 35 \\text{ (at least one account)}'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 10.4 — a three-set insurance problem, solved '
      'algebraically', 'open': True, 'q': [
      {'p': 'A company has 120 employees, each of whom has bought no policy or at least one of '
            'three insurance policies: health ($H$), vehicle ($V$) and life ($L$), from WAFAO '
            'Insurance. 45 bought health, 49 bought vehicle, 54 bought life; 15 bought health '
            'and vehicle, 18 bought health and life, 12 bought vehicle and life; 10 bought none '
            'of the three. Determine the number who bought (i) all three policies; (ii) health '
            'policy only; (iii) health and life policies only.'}],
      'a': [
      {'p': '$n(U)=120$, $n(H)=45$, $n(V)=49$, $n(L)=54$, $n(H \\cap V)=15$, $n(H \\cap L)=18$, '
            '$n(V \\cap L)=12$, $n(\\text{none})=10$. Let $n(H \\cap V \\cap L) = x$.'},
      {'p': 'Each pairwise-only region is the pairwise total less $x$: health-and-vehicle only '
            '$=15-x$; health-and-life only $=18-x$; vehicle-and-life only $=12-x$.'},
      {'p': 'Each single-only region is the total less its two pairwise overlaps, with $x$ added '
            'back (since it was subtracted twice):'},
      {'tex': 'H \\text{ only} = 45 - (15-x) - (18-x) - x = 12 + x'},
      {'tex': 'V \\text{ only} = 49 - (15-x) - (12-x) - x = 22 + x'},
      {'tex': 'L \\text{ only} = 54 - (18-x) - (12-x) - x = 24 + x'},
      {'p': 'All eight regions (including "none") sum to $n(U)$:'},
      {'tex': '120 = (12+x) + (22+x) + (24+x) + (15-x) + (18-x) + (12-x) + x + 10'},
      {'tex': '120 = 113 + x \\;\\Rightarrow\\; x = 7'},
      {'p': '(i) **7 employees bought all three policies.**'},
      {'tex': '(ii)\\ H \\text{ only} = 12 + 7 = 19 \\qquad '
              '(iii)\\ H \\text{ and } L \\text{ only} = 18 - 7 = 11'}]}},
  ]},

  {'n': '10.4', 't': 'Worksheet summary — every term and every worked method', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§10.1–10.2 Terms** — a set is a collection of well-defined objects/elements/members; '
      'denoted by a capital letter, elements by small letters; $\\in$ / $\\notin$. Specified by '
      'the **roster method** (listing) or the **property method** (a common rule). Types: '
      'finite/infinite; cardinality $n(A)$; empty/null set; universal set $U$; subset '
      '$A \\subseteq B$/superset/equal sets. Operations: union (in $A$ or $B$ or both), '
      'intersection (in both), complement (in $U$, not in $A$).',
      '**§10.3 Euler-Venn diagrams** — developed by Euler and John Venn; $U$ is a rectangle, '
      'subsets are circles. For a **two-set** problem, apply '
      '$n(A \\cup B)=n(A)+n(B)-n(A \\cap B)$ directly (Example 10.2), or let the unknown overlap '
      'be $x$ and solve $n(U)=$ (only-$A$) $+x+$ (only-$B$) $+$ (neither) (Example 10.3). For a '
      '**three-set** problem, let the triple overlap be $x$, express every pairwise-only region '
      'as (pairwise total $-x$) and every single-only region as (single total $-$ its two '
      'pairwise overlaps $+x$), then solve for $x$ from $n(U) = \\sum$(all regions) (Example '
      '10.4).',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Set** — a collection of well-defined objects, things or units (capital letter).',
      '**Element / member** — an object in a set (small letter). $b \\in B$ = "belongs to"; '
      '$b \\notin B$ = "does not belong to".',
      '**Roster method** — specifying a set by listing its elements.',
      '**Property method** — specifying a set by a common property/rule.',
      '**Finite set** — countable number of elements. **Infinite set** — uncountable.',
      '**Cardinality $n(A)$** — the number of elements in $A$.',
      '**Empty / null set** — a set with no elements, $\\{\\ \\}$.',
      '**Universal set $U$** — the collection of all objects under consideration; a rectangle '
      'on the Euler-Venn diagram.',
      '**Subset $A \\subseteq B$** — every element of $A$ is in $B$. **Superset $B \\supseteq '
      'A$**. **Equal sets** — each is a subset of the other.',
      '**Union $A \\cup B$** — in $A$ or $B$ or both.',
      '**Intersection $A \\cap B$** — in both $A$ and $B$.',
      '**Complement $A\'$ or $A^c$** — in $U$ but not in $A$.',
      '**Euler-Venn diagram** — a pictorial representation of sets: circles inside a rectangle.',
    ]},
    {'h3': 'The two-set counting formula'},
    {'tex': 'n(A \\cup B) = n(A) + n(B) - n(A \\cap B)'},
    {'h3': 'The three-set method'},
    {'p': 'Let $x = n(A \\cap B \\cap C)$. Each single-only region $= n(\\text{that set}) - '
          '(\\text{its two pairwise totals}) + x$; each pairwise-only region $= '
          '(\\text{that pairwise total}) - x$. All regions, plus those outside every set, sum '
          'to $n(U)$ — solve that equation for $x$.'},
  ]},

  {'n': '10.5', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following does NOT constitute a set? (A) An aggregate of books in a '
        'library (B) A collection of tools in a carpentry shop (C) A collection of historical '
        'artifacts in a museum (D) A collection of undefined items (E) A group of all vowels '
        'in the English alphabet',
        'Which of the following sets is infinite? '
        '(A) $D=\\{\\text{all the days in a week}\\}$ '
        '(B) $S=\\{\\text{all the ICAN students in a Tuition house}\\}$ '
        '(C) $T=\\{\\text{all the letters of the alphabet}\\}$ '
        '(D) $V=\\{\\text{all even numbers}\\}$ (E) $P=\\{x: 1 \\le x \\le 7\\}$',
        'From enrolment records for Principles of Accounting ($A$) and Quantitative Analysis '
        '($Q$): $n(A)=120$, $n(A \\cap Q)=40$ and $n(A \\cup Q)=240$. Calculate $n(Q)$. '
        '(A) 80  (B) 160  (C) 200  (D) 280  (E) 400',
        'A survey of bank accounts operated by staff showed 35 operate savings and current '
        'accounts, 45 operate savings account, 20 operate current account only, while 5 '
        'operate neither. Determine the number of staff in the company. '
        '(A) 60  (B) 65  (C) 70  (D) 80  (E) 105',
        'Withdrawals (in ₦\'000) at two paying points: $A=\\{3,5,10,15,17,21\\}$ and '
        '$B=\\{11,15,20,21,30\\}$. Then $n(A \\cup B)$ is (A) 7  (B) 8  (C) 9  (D) 10  (E) 11',
        'Any given set is a subset of the universal set; the set of points not in the given '
        'set is known as ……………………',
        'In an Euler-Venn diagram, the circle represents a …………… while the rectangle represents '
        'a ……………',
        'Given $n(X)=33$, $n(Y)=40$ and $n(X \\cap Y)=40$, then $n(X \\cup Y)$ is …………',
        'The set that contains all the elements of set $E$ or set $F$ or both sets is called '
        'the …………… of set $E$ and set $F$',
        'A set with countable members is known as …………… while a set with uncountable members '
        'is known as ……………',
      ]}],
      'a': [
      {'ol': [
        '**D** — a collection must be well-defined to be a set.',
        '**D** — even numbers have no upper bound and so are infinite.',
        '**B — 160.** $n(A \\cup Q) = n(A)+n(Q)-n(A \\cap Q) \\Rightarrow 240 = 120+n(Q)-40 '
        '\\Rightarrow n(Q)=160$.',
        '**C — 70.** $35 + (45-35) + 20 + 5 = 35+10+20+5=70$.',
        '**C — 9.** $A \\cup B=\\{3,5,10,11,15,17,20,21,30\\}$, 9 elements.',
        '**Complement.**',
        '**Any set** (a subset), **universal set** — in that order.',
        '**Flagged.** Applying the formula to the numbers as printed gives '
        '$n(X \\cup Y)=33+40-40=33$ — and $n(X \\cap Y)=40$ cannot exceed $n(X)=33$ in the '
        'first place, since an intersection can never be larger than either of its sets. One '
        'of the three figures in the study text\'s own question is very likely a misprint; the '
        'text\'s own printed answer is **49**, which would require $n(X \\cap Y)=24$, not 40. '
        'Verify with your tutor if this exact question appears on a past paper.',
        '**Union.**',
        '**Finite set**, **infinite set** — in that order.',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Cardinality (complement)', 'tex': "n(A') = n(U) - n(A)"},
  {'lb': 'Union of two sets',
   'tex': 'n(A \\cup B) = n(A) + n(B) - n(A \\cap B)'},
  {'lb': '"A only"', 'tex': "n(A \\text{ only}) = n(A) - n(A \\cap B)"},
  {'lb': 'Neither of two sets', 'tex': "n(\\text{neither}) = n(U) - n(A \\cup B)"},
 ],
 'focus':
   'One Section A mark most diets, usually a two-set counting problem solved directly from '
   '$n(A \\cup B)=n(A)+n(B)-n(A \\cap B)$, or a fill-in-the-blank on set vocabulary (universal '
   'set, complement, subset). A three-set business problem (insurance, scheme membership, '
   'subject combinations) is a dependable Section B question — set the triple overlap as $x$ '
   'and build every other region from it, exactly as the study text\'s own worked examples do.',
 'errors': [
   'Reading "15 operate savings and current accounts" as "15 operate only those two" when it '
   'means both, including anyone also elsewhere.',
   'Filling a three-set Venn diagram from the outside in rather than starting from the (unknown, '
   'often algebraic) centre.',
   'Forgetting the "neither/none" region when the universal set total is given.',
   'Confusing the empty set $\\{\\ \\}$ with a set containing zero, $\\{0\\}$.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'If $n(A) = 20$, $n(B) = 15$ and $n(A \\cap B) = 5$, then $n(A \\cup B)$ is',
    'o': ['40', '30', '35', '25', '10'],
    'a': 1,
    'w': 'Add the two sets and subtract the overlap, which would otherwise be counted twice.',
    'calc': 'n(A \\cup B) = 20 + 15 - 5 = 30',
    'src': 'Chapter 10.3', 'sec': '10.3'},
   {'q': 'The set of all elements in the universal set that are not in $A$ is called the',
    'o': ['subset of $A$', 'complement of $A$', 'union of $A$', 'intersection of $A$',
          'superset of $A$'],
    'a': 1,
    'w': 'The complement, $A\'$ or $A^c$, is everything in $U$ that is not in $A$.',
    'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'In a class of 40, 25 study French and 18 study German. If 5 study neither, the number '
         'studying both is',
    'o': ['13', '8', '7', '12', '10'],
    'a': 1,
    'w': 'Those studying at least one language number $40 - 5 = 35$; substitute in the '
         'union formula and solve for the overlap.',
    'calc': '35 = 25 + 18 - n(F \\cap G) \\Rightarrow  n(F \\cap G) = 43 - 35 = 8',
    'src': 'Chapter 10.3', 'sec': '10.3'},
   {'q': 'A set is specified by writing out $A = \\{2, 4, 6, 8\\}$. This is an example of the',
    'o': ['property method', 'roster method', 'universal method', 'Euler-Venn method',
          'complement method'],
    'a': 1,
    'w': 'Listing the elements directly is the roster method; describing a shared rule (e.g. '
         '"$x$ is even") would be the property method.',
    'src': 'Chapter 10.2', 'sec': '10.2'},
   {'q': 'In an Euler-Venn diagram, the universal set $U$ is conventionally represented by a',
    'o': ['circle', 'rectangle', 'triangle', 'straight line', 'point'],
    'a': 1,
    'w': 'By convention $U$ is the rectangle; the other subsets are drawn as circles inside it.',
    'src': 'Chapter 10.3', 'sec': '10.3'},
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
      {'p': 'Following the same centre-outwards method as Example 10.4: remove both pairwise '
            'overlaps from each single total, then add the triple back once, since it was '
            'removed twice:'},
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
      {'note': 'Marks are given for the diagram as well as the arithmetic. Draw three '
               'overlapping circles, write 12 in the central region first, then the three '
               'pairwise regions, then the three "only" regions, and finally the 19 outside the '
               'circles but inside the rectangle representing $U$ — the same left-to-centre '
               'method as the study text\'s own Example 10.4.'}],
    'src': 'Chapter 10.3', 'sec': '10.3'},
  ]},
}
