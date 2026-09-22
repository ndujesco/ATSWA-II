CH = {
 'n': 6,
 't': 'Index Numbers',
 'brief': 'Measuring change over time: unweighted price relatives and aggregates, and the four '
          'weighted indices — Laspeyre, Paasche, Fisher and Marshall–Edgeworth.',
 'outcomes': [
   'Understand the concept of index numbers',
   'Differentiate between price indices and price relatives',
   'Know the differences between unweighted and weighted index numbers',
   'Compute and handle problems on index numbers using Laspeyre, Paasche, Fisher and '
   'Marshall–Edgeworth methods',
 ],
 'secs': [
  {'n': '6.1', 't': 'Introduction', 'b': [
    {'def': {'t': 'Index number (Spiegel)', 'd': 'a statistical measure designed to show changes '
                  'in a variable or a group of variables with respect to time, geographical '
                  'location or other characteristics.'}},
    {'p': 'It is usual practice in business, the economy and other areas of life to find the '
          'average change in the price, quantity or value of a related group of items over a '
          'period of time, or across geographical locations. The index number is the statistical '
          'device used to measure that change.'},
    {'p': 'By the principle of index numbers, the statistical device measures:'},
    {'ol': [
      'the differences in the general level of a group of related variables;',
      'the differences that may have to do with the **price** of commodities; and',
      'the **physical quantity** of goods produced, marketed or consumed, in order to make a '
      'comparison between periods of time, schools, places, etc.',
    ]},
    {'p': 'Based on this principle, index numbers are broadly categorised by the variable they '
          'measure into **Price Index Numbers** — consisting of retail price indices and the '
          'like — which is the type this chapter develops in full.'},
  ]},

  {'n': '6.2', 't': 'Index numbers and their uses', 'b': [
    {'p': 'It is important to state the following uses of index numbers:'},
    {'ol': [
      'to deflate a value series in order to convert it into physical terms;',
      'to keep abreast of current business conditions — it acts as a business or economic '
      'barometer;',
      'to give the trend movement in business or the economy;',
      'to forecast, by using a series of the indices;',
      'to assess the worth of the purchasing power of money;',
      'to compare the standard of living in various areas/countries or geographical locations; '
      'and',
      'to compare readers\' intelligence in various schools or countries.',
    ]},
  ]},

  {'n': '6.3', 't': 'Problems in constructing an index number', 'b': [
    {'p': 'The following are among the problems usually encountered in constructing an index '
          'number:'},
    {'ol': [
      'definition of the **purpose** for which the index number is being compiled or '
      'constructed;',
      'selection of **commodities/items** to include — what type, quantity and quality are to '
      'be selected;',
      'selection of the **source of data** — it must be reliable, so utmost care is needed;',
      '**method of collecting data** — once the source is settled, an efficient and effective '
      'collection method must be decided, depending on whether the data is primary or '
      'secondary;',
      'selection of the **base year** — the reference period against which other data is '
      'compared. It should be economically stable and free from abnormalities such as '
      'inflation, depression, famine or boom, and should not be too far from the current '
      'period;',
      '**method of combining the data** — the appropriate method depends on the purpose of the '
      'index and the data available, and it dictates which formula is used; and',
      'choice of **weight** — the relative importance attached to the various items must be '
      'taken into account for a fair, accurate index.',
    ]},
    {'h4': 'Construction methods of price index numbers'},
    {'p': 'The Price Index number measures the change in the general level of prices for a given '
          'number or group of commodities — it could be a wholesale price index, a retail price '
          'index, or an index of the prices of manufactured products. The construction methods '
          'fall broadly into two:'},
    {'ul': ['the use of **unweighted** price index numbers; and', 'the use of **weighted** price '
      'index numbers.']},
  ]},

  {'n': '6.4', 't': 'Unweighted index numbers and their calculation', 'b': [
    {'p': 'In an unweighted index number, equal importance is attached to every item in the '
          'index. Three unweighted indices are considered:'},
    {'ul': ['Simple Price Relative Index Number (SPRI);', 'Simple Aggregate Price Index (SAPI); '
      'and', 'Simple Average of Relative Price Index (SARPI).']},
    {'fbox': {'h': 'Unweighted price indices', 'rows': [
      {'lb': 'Simple Price Relative Index (SPRI)',
       'tex': 'SPRI = \\frac{p_{ti}}{p_{0i}} \\times 100',
       'nt': 'The simplest of all index numbers: the ratio of a single commodity\'s current-year '
             'price $p_{ti}$ to its base-year price $p_{0i}$.'},
      {'lb': 'Simple Aggregate Price Index (SAPI)',
       'tex': 'SAPI = \\frac{\\sum p_{ti}}{\\sum p_{0i}} \\times 100',
       'nt': 'Uses only the arithmetic mean, ignoring the relative importance of the '
             'commodities: total prices at the current period as a percentage of total prices '
             'at the base period.'},
      {'lb': 'Simple Average of Relative Price Index (SARPI)',
       'tex': 'SARPI = \\frac{\\sum \\left(\\frac{p_{ti}}{p_{0i}} \\times 100\\right)}{n}',
       'nt': 'Removes the unit-dependence of SAPI: the average of the individual price '
             'relatives, where $n$ is the number of items.'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 6.1 — SPRI, SAPI and SARPI', 'open': True, 'q': [
      {'p': 'Determine the SPRI, SAPI and SARPI for the following table, using 2004 as the base '
            'year.'},
      {'table': {'align': 'lrrr', 'head': ['Item', '2004 (₦/₵)', '2005', '2006'], 'rows': [
        ['A', '20', '30', '60'], ['B', '30', '42', '55'],
        ['C', '10', '15', '20'], ['D', '6', '8', '15'],
      ]}}],
      'a': [
      {'h4': '(i) SPRI'},
      {'table': {'align': 'lrrrr',
        'head': ['Item', '$p_0$ (2004)', '$p_1$ (2005)', '$p_2$ (2006)', 'SPRI 2005 / 2006 (%)'],
        'rows': [
        ['A', '20', '30', '60', '150 / 300'],
        ['B', '30', '42', '55', '140 / 183'],
        ['C', '10', '15', '20', '150 / 200'],
        ['D', '6', '8', '15', '130 / 250'],
      ]}},
      {'h4': '(ii) SAPI, using 2004 as base ($\\sum p_0 = 66$)'},
      {'p': '$\\sum p_1 = 95$ (2005), $\\sum p_2 = 150$ (2006).'},
      {'tex': 'SAPI_{2005} = \\frac{95}{66} \\times 100 = 143.94 \\approx 144\\% \\qquad '
              'SAPI_{2006} = \\frac{150}{66} \\times 100 = 227.27 \\approx 227\\%'},
      {'h4': '(iii) SARPI'},
      {'table': {'align': 'lrrrr', 'head': ['Item', '$p_0$', '$p_1/p_0$', '$p_2/p_0$', ''],
        'rows': [
        ['A', '20', '1.50', '3.00', ''], ['B', '30', '1.40', '1.83', ''],
        ['C', '10', '1.50', '2.00', ''], ['D', '6', '1.30', '2.50', ''],
        ['Total', '', '5.70', '9.33', '@tot'],
      ]}},
      {'tex': 'SARPI_{2005} = \\frac{5.70 \\times 100}{4} = 142.5 \\approx 143\\% \\qquad '
              'SARPI_{2006} = \\frac{9.33 \\times 100}{4} = 233.25 \\approx 233\\%'}]}},
  ]},

  {'n': '6.5', 't': 'Weighted index numbers and their calculation', 'b': [
    {'p': 'In a weighted index, weights are attached to each item on the assumption that they '
          'denote the item\'s relative importance. Weighted indices fall into two broad groups: '
          '**Weighted Aggregative Indices** and **Weighted Average of Relative Indices**. Four '
          'weighted aggregative methods, each using a different weighting technique, are '
          'considered: Laspeyre, Paasche, Fisher and Marshall–Edgeworth.'},
    {'fbox': {'h': 'Weighted price indices', 'rows': [
      {'lb': "Laspeyre's index (1864)",
       'tex': 'I_L = \\frac{\\sum p_i q_0}{\\sum p_0 q_0} \\times 100',
       'nt': 'Uses base-year quantities $q_0$ as weights. Easy and widely used, since it is '
             'based on fixed base-year weights, but it has an **upward bias**.'},
      {'lb': "Paasche's index (1874)",
       'tex': 'I_P = \\frac{\\sum p_i q_i}{\\sum p_0 q_i} \\times 100',
       'nt': 'Introduced by the German statistician Paasche. Uses current/given-year quantities '
             '$q_i$ as weights. Tedious to compute and has a **downward bias**.'},
      {'lb': "Fisher's Ideal index",
       'tex': 'I_F = \\sqrt{I_L \\times I_P}',
       'nt': 'The geometric mean of Laspeyre and Paasche. Theoretically better than the other '
             'methods because it overcomes their shortcomings.'},
      {'lb': 'Marshall–Edgeworth index',
       'tex': 'I_M = \\frac{\\sum p_i \\left(\\frac{q_0+q_i}{2}\\right)}'
              '{\\sum p_0 \\left(\\frac{q_0+q_i}{2}\\right)} \\times 100 = '
              '\\frac{\\sum p_i q_0 + \\sum p_i q_i}{\\sum p_0 q_0 + \\sum p_0 q_i} \\times 100',
       'nt': 'Uses the **average of base and current-year quantities** as weights.'},
    ]}},
    {'note': 'Notation throughout: $p_0$ = base-year price, $q_0$ = base-year quantity; $p_i$ = '
             'current/given-year price, $q_i$ = current/given-year quantity.'},
    {'eg': {'tag': 'Study text', 't': 'Example 6.2 — all four weighted indices', 'open': True,
      'q': [
      {'p': 'Use the table below to calculate the price index for 2016, taking 2011 as base '
            'year, by (a) Laspeyre, (b) Paasche, (c) Fisher, and (d) Marshall–Edgeworth.'},
      {'table': {'align': 'lrrrr', 'head': ['Item', '2011 price', '2011 qty', '2016 price', '2016 qty'],
        'rows': [
        ['A', '14', '45', '20', '35'], ['B', '13', '15', '19', '20'],
        ['C', '12', '10', '14', '10'], ['D', '10', '5', '12', '8'],
      ]}}],
      'a': [
      {'table': {'align': 'lrrrr', 'head': ['Item', '$p_0q_0$', '$p_iq_0$', '$p_iq_i$', '$p_0q_i$'],
        'rows': [
        ['A', '630', '900', '700', '490'], ['B', '195', '285', '380', '300'],
        ['C', '120', '140', '140', '100'], ['D', '50', '60', '96', '40'],
        ['Total', '995', '1,385', '1,316', '930', '@tot'],
      ]}},
      {'tex': 'I_L = \\frac{1{,}385}{995} \\times 100 = 139.20\\% \\qquad '
              'I_P = \\frac{1{,}316}{930} \\times 100 = 141.51\\%'},
      {'tex': 'I_F = \\sqrt{139.20 \\times 141.51} = \\sqrt{19{,}696.6} = 140.34\\%'},
      {'p': 'For Marshall–Edgeworth, sum $p_iq_0+p_iq_i$ and $p_0q_0+p_0q_i$ item by item: '
            '$1{,}385+1{,}316=2{,}701$ and $995+930=1{,}925$.'},
      {'tex': 'I_M = \\frac{2{,}701}{1{,}925} \\times 100 = 140.31\\%'},
      {'note': 'All four methods put the rise in prices at roughly **139–141%** — as expected, '
               'Laspeyre and Paasche bracket the true movement, with Fisher and '
               'Marshall–Edgeworth falling between them.'}]}},
  ]},

  {'n': '6.6', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§6.1 Introduction** — Spiegel\'s definition; the principle measures (a) differences in '
      'the level of related variables, (b) differences in commodity price, (c) physical '
      'quantity comparisons. Classified by the study text into Price Index Numbers, which this '
      'chapter develops.',
      '**§6.2 Uses** — deflate a value series; act as a business/economic barometer; show '
      'trend movement; forecast from a series of indices; assess the purchasing power of '
      'money; compare standards of living across areas/countries; compare intelligence across '
      'schools/countries.',
      '**§6.3 Problems in construction** — purpose; selection of commodities/items; selection '
      'of the source of data; method of collecting data; selection of the base year; method of '
      'combining data (dictates the formula); choice of weight. Construction methods split into '
      'unweighted and weighted price index numbers.',
      '**§6.4 Unweighted indices** — SPRI $=p_{ti}/p_{0i}\\times100$ (single commodity); SAPI '
      '$=\\sum p_{ti}/\\sum p_{0i}\\times100$ (ignores relative importance); SARPI $=\\sum('
      'p_{ti}/p_{0i}\\times100)/n$ (average of the relatives).',
      '**§6.5 Weighted indices** — Laspeyre $I_L=\\sum p_iq_0/\\sum p_0q_0\\times100$ '
      '(base-year weights, **upward** bias); Paasche $I_P=\\sum p_iq_i/\\sum p_0q_i\\times100$ '
      '(current-year weights, **downward** bias); Fisher $I_F=\\sqrt{I_L\\times I_P}$ '
      '(geometric mean, theoretically the best of the four); Marshall–Edgeworth (average of '
      'base and current quantities as weights).',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Index number** — a statistical measure designed to show changes in a variable or a '
      'group of variables with respect to time, geographical location or other '
      'characteristics (Spiegel).',
      '**Base year** — the reference period against which other periods are compared; should '
      'be economically stable and not too remote.',
      '**Weight** — the relative importance attached to an item in the index.',
      '**Unweighted index** — equal importance given to every item. **Weighted index** — items '
      'weighted by quantity.',
    ]},
  ]},

  {'n': '6.7', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following is NOT one of the uses of an index number? (A) To deflate a '
        'value series in order to convert it into real physical terms  (B) To compare '
        'students’ intelligence in various schools or countries  (C) To select the '
        'commodities sources  (D) To forecast by using series of the indices  (E) To assess '
        'the worth of purchasing power of money',
        'Which of the following is NOT a problem in the construction of an index number? '
        '(A) Selection of sources of data  (B) Definition of the purpose for which index is '
        'needed  (C) Method of collecting data for index  (D) Method of combining the data  '
        '(E) Unweighted average price index',
        'Which of the following is NOT a weighted price index number? (A) Laspeyre Index  '
        '(B) Simple Aggregate Price Index  (C) Fisher Ideal Index  (D) Marshall-Edgeworth '
        'Index  (E) Paasche Index',
        'The Weighted Aggregative Index with a downward bias is _________ (A) Laspeyre Index  '
        '(B) Simple Aggregate Price Index  (C) Fisher Ideal Index  (D) Marshall-Edgeworth '
        'Index  (E) Paasche Index',
        'Which of the following is the formula for the Unweighted Price Index? '
        '(A) $\\sum q_{ti}/\\sum q_{0i} \\times 100$  '
        '(B) $q_{ti}/q_{0i} \\times 100$  '
        '(C) $\\sum p_iq_0/\\sum p_0q_0 \\times 100$  '
        '(D) $\\sum p_{ti}/\\sum p_{0i} \\times 100$  '
        '(E) $\\sum p_i(q_0+q_i)/2 \\div \\sum p_0(q_0+q_i)/2 \\times 100$',
      ]},
      {'p': 'Use the following table (2000 as base year) to answer questions 6 and 7.'},
      {'table': {'align': 'lrr', 'head': ['Item', '2000 price', '2005 price'], 'rows': [
        ['A', '50', '80'], ['B', '70', '100'], ['C', '90', '100'], ['D', '100', '120'],
      ]}},
      {'ol': [
        'F. The Simple Aggregate Price Index of the above table, using 2000 as base year, is …',
        'G. The Simple Average of Relative Price Index, with 2000 as base year, is …',
      ]},
      {'p': 'Use the following table (2001 as base year) to answer questions 8 to 10.'},
      {'table': {'align': 'lrrrr', 'head': ['Item', '2001 price', '2001 qty', '2006 price', '2006 qty'],
        'rows': [
        ['A', '80', '50', '100', '60'], ['B', '90', '60', '100', '70'],
        ['C', '100', '70', '120', '90'],
      ]}},
      {'ol': [
        'H. Using 2001 as base year, the Laspeyre price index for 2006 is …',
        'I. Using 2001 as base year, the Paasche price index for 2006 is …',
        'J. Fisher’s Ideal price index of the above table is …',
      ]}],
      'a': [
      {'ol': [
        '**C** — selecting commodity sources is not listed among the construction problems.',
        '**E** — the unweighted average price index is itself one of the unweighted methods, '
        'not a listed *problem*.',
        '**B** — Simple Aggregate Price Index is **unweighted**.',
        '**E** — Paasche has the downward bias (Laspeyre has the upward bias).',
        '**D** — $\\sum p_{ti}/\\sum p_{0i}\\times100$ is the (unweighted) simple aggregate '
        'price index formula.',
      ]},
      {'p': '$\\sum p_0 = 310$, $\\sum p_1 = 400$.'},
      {'tex': 'F.\\; SAPI = \\frac{400}{310} \\times 100 = 129.03\\%'},
      {'p': 'Price relatives: $80/50=1.6$, $100/70=1.429$, $100/90=1.111$, $120/100=1.2$; sum '
            '$=5.340$.'},
      {'tex': 'G.\\; SARPI = \\frac{5.340}{4} \\times 100 = 133.50\\%'},
      {'p': '$\\sum p_0q_0 = 16{,}400$, $\\sum p_iq_0 = 14{,}400$, $\\sum p_0q_i = 20{,}100$, '
            '$\\sum p_iq_i = 23{,}800$.'},
      {'tex': 'H.\\; I_L = \\frac{14{,}400}{16{,}400} \\times 100 = 118.29\\% \\qquad '
              'I.\\; I_P = \\frac{23{,}800}{20{,}100} \\times 100 = 118.41\\%'},
      {'tex': 'J.\\; I_F = \\sqrt{118.29 \\times 118.41} = 118.35\\%'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Simple Price Relative Index (SPRI)', 'tex': '\\frac{p_{ti}}{p_{0i}} \\times 100'},
  {'lb': 'Simple Aggregate Price Index (SAPI)',
   'tex': '\\frac{\\sum p_{ti}}{\\sum p_{0i}} \\times 100'},
  {'lb': 'Simple Average of Relative Price Index (SARPI)',
   'tex': '\\frac{\\sum \\left(\\frac{p_{ti}}{p_{0i}}\\times 100\\right)}{n}'},
  {'lb': "Laspeyre's price index (base-year quantities, upward bias)",
   'tex': 'I_L = \\frac{\\sum p_i q_0}{\\sum p_0 q_0} \\times 100'},
  {'lb': "Paasche's price index (current-year quantities, downward bias)",
   'tex': 'I_P = \\frac{\\sum p_i q_i}{\\sum p_0 q_i} \\times 100'},
  {'lb': "Fisher's Ideal index", 'tex': 'I_F = \\sqrt{I_L \\times I_P}'},
  {'lb': 'Marshall–Edgeworth index',
   'tex': 'I_M = \\frac{\\sum p_i q_0 + \\sum p_i q_i}{\\sum p_0 q_0 + \\sum p_0 q_i} \\times 100'},
 ],
 'focus':
   'A dependable Section B question: a table of prices and quantities for four or five items and '
   'a request for two or more of Laspeyre, Paasche, Fisher and Marshall–Edgeworth. Build the four '
   'product columns ($p_0q_0$, $p_iq_0$, $p_iq_i$, $p_0q_i$) once and read every index off the '
   'column totals. Section A tests which index uses which weights and bias, and the list of uses '
   'and construction problems verbatim.',
 'errors': [
   'Swapping the weights (and the bias direction) of Laspeyre and Paasche.',
   'Taking the arithmetic mean instead of the geometric mean for Fisher\'s index.',
   'Using the simple aggregate index where quantities are actually given (a weighted index is '
   'available and should be preferred).',
   'Forgetting to multiply by 100, giving an index of 1.40 instead of 140.',
   'Treating Simple Aggregate Price Index as a weighted method — it is unweighted.',
 ],
 'quiz': {
  'mcq': [
   {'q': "Laspeyre's price index uses the quantities of the",
    'o': ['current year', 'base year', 'average of both years', 'preceding year',
          'year with the highest output'],
    'a': 1,
    'w': 'Laspeyre holds the basket fixed at base-year quantities $q_0$, which is cheap to '
         'maintain but gives the index an upward bias.',
    'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': "If Laspeyre's index is 121 and Paasche's is 116, Fisher's Ideal index is",
    'o': ['118.5', '118.47', '237.0', '116.0', '121.0'],
    'a': 1,
    'w': "Fisher's index is the geometric mean of the other two.",
    'calc': 'I_F = \\sqrt{121 \\times 116} = \\sqrt{14{,}036} = 118.47',
    'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': 'The main defect of the Simple Aggregate Price Index is that',
    'o': ['it is difficult to compute', 'it requires quantity data',
          'its value depends on the units in which the items are quoted',
          'it cannot be expressed as a percentage', 'it always exceeds 100'],
    'a': 2,
    'w': 'Adding prices quoted in different units lets the item with the largest unit dominate '
         'the index for reasons unconnected with its true importance — it ignores relative '
         'importance altogether.',
    'src': 'Chapter 6.4', 'sec': '6.4'},
   {'q': 'Which weighted index uses the average of base-year and current-year quantities as '
         'its weights?',
    'o': ["Laspeyre's index", "Paasche's index", "Fisher's Ideal index",
          'Marshall–Edgeworth index', 'Simple Average of Relatives'],
    'a': 3,
    'w': 'Marshall–Edgeworth weights each item by $(q_0+q_i)/2$, splitting the difference '
         'between the base and current baskets.',
    'src': 'Chapter 6.5', 'sec': '6.5'},
   {'q': 'Given $\\sum p_0=200$, $\\sum p_1=260$ for four items of equal importance, the Simple '
         'Aggregate Price Index for the current year is',
    'o': ['76.92', '130.00', '60.00', '13.00', '200.00'],
    'a': 1,
    'w': 'SAPI is the ratio of the two price totals, expressed as a percentage.',
    'calc': 'SAPI = \\frac{260}{200} \\times 100 = 130.00',
    'src': 'Chapter 6.4', 'sec': '6.4'},
  ],
  'theory': [
   {'q': "Distinguish between Laspeyre's and Paasche's price indices, stating the bias of each, "
         "and explain how Fisher's index is derived from them.",
    'marks': 8,
    'a': [
      {'tex': 'I_L = \\frac{\\sum p_i q_0}{\\sum p_0 q_0} \\times 100 \\qquad '
              'I_P = \\frac{\\sum p_i q_i}{\\sum p_0 q_i} \\times 100'},
      {'table': {'head': ['', "Laspeyre's index", "Paasche's index"], 'align': 'lll', 'rows': [
        ['Weights', 'Base-year quantities $q_0$', 'Current-year quantities $q_i$'],
        ['Introduced by', 'Laspeyre, 1864', 'Paasche (German statistician), 1874'],
        ['Ease of computation', 'Easy — fixed base-year weights collected once',
         'Tedious — quantities must be re-collected every period'],
        ['Bias', '**Upward**', '**Downward**'],
      ]}},
      {'h4': "Fisher's Ideal index"},
      {'tex': 'I_F = \\sqrt{I_L \\times I_P}'},
      {'p': 'It is the geometric mean of Laspeyre and Paasche, so it lies between the two and is '
            'theoretically better than either because it overcomes their individual '
            'shortcomings — the upward bias of one offsetting the downward bias of the other.'}],
    'src': 'Chapter 6.5', 'sec': '6.5'},
  ]},
}
