CH = {
 'n': 6,
 't': 'Index Numbers',
 'brief': 'Measuring change over time: simple and weighted price and quantity indices, Laspeyres, '
          'Paasche and Fisher, and the consumer price index.',
 'outcomes': [
   'Explain the uses and problems of index numbers',
   'Compute simple price and quantity relatives and aggregate indices',
   'Compute Laspeyres, Paasche, Marshall-Edgeworth and Fisher indices',
   'Change the base of an index and deflate a money series',
 ],
 'secs': [
  {'n': '6.1', 't': 'What an index number is', 'b': [
    {'def': {'t': 'Index number', 'd': 'a statistical measure expressing the change in a variable, '
                  'or a group of variables, relative to a base period taken as 100.'}},
    {'h3': 'Uses'},
    {'ul': [
      'Measuring **inflation** through the consumer price index.',
      '**Deflating** a money series to obtain real values.',
      'Adjusting wages and pensions for changes in the cost of living.',
      'Comparing production, trade or prices between periods or regions.',
      'Providing a basis for economic policy and for business forecasting.',
    ]},
    {'h3': 'Problems in construction'},
    {'ol': [
      'Choice of the **base period** — it must be normal, not a boom or a slump, and not too remote.',
      'Selection of **items** to include — the basket must be representative and manageable.',
      'Choice of **weights** and how often to revise them.',
      'Choice of the **formula** — Laspeyres, Paasche and Fisher give different answers.',
      'Obtaining reliable and consistent **price data** across periods.',
      '**Quality changes** — a phone costing the same as last year is not the same phone.',
      'Handling items that **disappear** from the market or are newly introduced.',
    ]},
  ]},

  {'n': '6.2', 't': 'Unweighted indices', 'b': [
    {'fbox': {'h': 'Simple (unweighted) indices', 'rows': [
      {'lb': 'Price relative',
       'tex': 'P_{01} = \\frac{p_1}{p_0} \\times 100'},
      {'lb': 'Quantity relative',
       'tex': 'Q_{01} = \\frac{q_1}{q_0} \\times 100'},
      {'lb': 'Simple aggregate price index',
       'tex': 'P = \\frac{\\sum p_1}{\\sum p_0} \\times 100',
       'nt': 'Flawed: the answer depends on the units in which each item is quoted.'},
      {'lb': 'Simple average of price relatives',
       'tex': 'P = \\frac{1}{n}\\sum \\left(\\frac{p_1}{p_0} \\times 100\\right)',
       'nt': 'Free of the units problem, but still treats every item as equally important.'},
    ]}},
    {'warn': 'The simple aggregate index is unsound. If rice is quoted per bag and salt per gram, '
             'rice dominates the index for no reason but the choice of unit. Never use it where a '
             'weighted index is available.'},
  ]},

  {'n': '6.3', 't': 'Weighted indices', 'b': [
    {'p': 'Weighting solves both problems at once: items enter in proportion to how much is '
          'bought. The question is only **which period\'s quantities** to use as weights.'},
    {'fbox': {'h': 'Weighted price indices', 'rows': [
      {'lb': 'Laspeyres (base-year weights)',
       'tex': 'P_L = \\frac{\\sum p_1 q_0}{\\sum p_0 q_0} \\times 100',
       'nt': 'Weights fixed at the base. Easy to compute and to update, but overstates inflation '
             'because it ignores substitution away from items that have become dear.'},
      {'lb': 'Paasche (current-year weights)',
       'tex': 'P_P = \\frac{\\sum p_1 q_1}{\\sum p_0 q_1} \\times 100',
       'nt': 'Weights revised each period. More current, but expensive and understates inflation.'},
      {'lb': 'Marshall–Edgeworth',
       'tex': 'P_{ME} = \\frac{\\sum p_1 (q_0 + q_1)}{\\sum p_0 (q_0 + q_1)} \\times 100'},
      {'lb': "Fisher's ideal index",
       'tex': 'P_F = \\sqrt{P_L \\times P_P}',
       'nt': 'The geometric mean of the other two. Called *ideal* because it satisfies both the '
             'time reversal and factor reversal tests.'},
    ]}},
    {'p': 'The quantity indices are the mirror images, with $p$ and $q$ interchanged:'},
    {'tex': 'Q_L = \\frac{\\sum q_1 p_0}{\\sum q_0 p_0} \\times 100 \\qquad '
            'Q_P = \\frac{\\sum q_1 p_1}{\\sum q_0 p_1} \\times 100'},
    {'eg': {'t': 'Laspeyres, Paasche and Fisher', 'q': [
      {'p': 'Compute the three price indices for Year 1 with Year 0 as base.'},
      {'table': {'align': 'lrrrr',
        'head': ['Item', '$p_0$', '$q_0$', '$p_1$', '$q_1$'], 'rows': [
        ['Rice (bag)', '18,000', '40', '24,000', '35'],
        ['Beans (bag)', '25,000', '20', '32,000', '18'],
        ['Oil (litre)', '1,200', '150', '1,500', '160'],
        ['Salt (kg)', '400', '60', '450', '65'],
      ]}}],
      'a': [
      {'h4': 'The four products'},
      {'table': {'align': 'lrrrr',
        'head': ['Item', '$p_0q_0$', '$p_1q_0$', '$p_0q_1$', '$p_1q_1$'], 'rows': [
        ['Rice', '720,000', '960,000', '630,000', '840,000'],
        ['Beans', '500,000', '640,000', '450,000', '576,000'],
        ['Oil', '180,000', '225,000', '192,000', '240,000'],
        ['Salt', '24,000', '27,000', '26,000', '29,250'],
        ['Total', '1,424,000', '1,852,000', '1,298,000', '1,685,250', '@tot'],
      ]}},
      {'tex': 'P_L = \\frac{\\sum p_1 q_0}{\\sum p_0 q_0} \\times 100 '
              '= \\frac{1{,}852{,}000}{1{,}424{,}000} \\times 100 = 130.06'},
      {'tex': 'P_P = \\frac{\\sum p_1 q_1}{\\sum p_0 q_1} \\times 100 '
              '= \\frac{1{,}685{,}250}{1{,}298{,}000} \\times 100 = 129.84'},
      {'tex': 'P_F = \\sqrt{P_L \\times P_P} = \\sqrt{130.06 \\times 129.84} '
              '= \\sqrt{16{,}887.0} = 129.95'},
      {'p': 'Prices rose by about **30%** on all three measures. As theory predicts, Laspeyres '
            '(130.06) exceeds Paasche (129.84), with Fisher between them — consumers shifted '
            'away from rice and beans, whose prices rose most.'},
      {'note': 'Set the four product columns out as a single table. Every index is then just a '
               'ratio of two column totals, and one table answers all three parts of the question.'}]}},
  ]},

  {'n': '6.4', 't': 'Using an index', 'b': [
    {'h3': 'The consumer price index'},
    {'p': 'The CPI measures the change in the cost of a fixed basket of goods and services bought '
          'by a typical household. It is the standard measure of **inflation** and is a weighted '
          'price index, normally of Laspeyres form.'},
    {'tex': '\\text{Inflation rate} = \\frac{\\text{CPI}_1 - \\text{CPI}_0}{\\text{CPI}_0} '
            '\\times 100\\%', 'tag': '(6.1)'},
    {'h3': 'Deflating a money series'},
    {'p': 'A money (nominal) series is converted to a real series at base-year prices by dividing '
          'by the index:'},
    {'tex': '\\text{Real value} = \\frac{\\text{Money value}}{\\text{Price index}} \\times 100',
     'tag': '(6.2)'},
    {'eg': {'t': 'Real wages', 'q': [
      {'p': 'A worker\'s wage rose from ₦180,000 a month in 2020 to ₦300,000 in 2024. The CPI '
            'rose from 100 to 195 over the same period. Has the worker gained?'}],
      'a': [
      {'tex': '\\text{Real wage in 2024 at 2020 prices} = \\frac{300{,}000}{195} \\times 100 '
              '= ₦153{,}846'},
      {'p': 'In money terms the wage rose 66.7%; in real terms it **fell** from ₦180,000 to '
            '₦153,846, a decline of about **14.5%**. The worker is worse off.'},
      {'tex': '\\text{Real change} = \\frac{153{,}846 - 180{,}000}{180{,}000} \\times 100 '
              '= -14.5\\%'},
      {'note': 'This is the single most useful thing index numbers do, and the examiner returns '
               'to it regularly. The money figure went up; the answer is that the worker is worse '
               'off, and the deflation shows why.'}]}},
    {'h3': 'Changing the base'},
    {'tex': '\\text{New index} = \\frac{\\text{Old index}}{\\text{Old index of the new base year}} '
            '\\times 100', 'tag': '(6.3)'},
    {'p': 'This is called **splicing** where two series with different bases are joined. The '
          'assumption is that the relative movements within each series are correct even though '
          'the bases differ.'},
  ]},

  {'n': '6.5', 't': 'Worksheet summary — definitions and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§6.1 What an index number is** — measures change in a variable relative to a base '
      'period = 100. Uses: inflation (CPI), deflating money series, wage/pension adjustment, '
      'comparison across time/region, policy/forecasting. Construction problems: choosing a '
      'normal (not boom/slump, not too remote) base period; a representative, manageable item '
      'basket; the weights and how often to revise them; which formula (Laspeyres/Paasche/'
      'Fisher give different answers); reliable price data; quality changes; and items that '
      'disappear or are newly introduced.',
      '**§6.2 Unweighted indices** — price/quantity relative $=p_1/p_0\\times100$; the simple '
      '**aggregate** index $\\sum p_1/\\sum p_0\\times100$ is unsound (unit-dependent — never '
      'use it where a weighted index is available); the simple **average of relatives** fixes '
      'the unit problem but still weights every item equally.',
      '**§6.3 Weighted indices** — **Laspeyres** (base-year quantity weights, overstates '
      'inflation — ignores substitution); **Paasche** (current-year weights, understates '
      'inflation, costlier to compute); **Marshall-Edgeworth** ($q_0+q_1$ weights); '
      '**Fisher\'s ideal** $=\\sqrt{P_L\\times P_P}$ (satisfies time- and factor-reversal '
      'tests). Quantity indices mirror the price ones with $p$ and $q$ swapped. Laspeyres is '
      'always $\\ge$ Paasche when prices rise and consumers substitute away from dearer items.',
      '**§6.4 Using an index** — the **CPI** is normally a Laspeyres-form weighted price '
      'index measuring inflation; inflation rate $=(\\text{CPI}_1-\\text{CPI}_0)/'
      '\\text{CPI}_0\\times100$. **Deflating**: real value $=$ money value $\\div$ price index '
      '$\\times100$ — a money figure can rise while the real (deflated) figure falls, which is '
      'the chapter\'s most-examined idea. **Changing the base** (splicing): new index $=$ old '
      'index $\\div$ old index of the new base year $\\times100$, joining two differently-'
      'based series on the assumption their internal relative movements are correct.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Index number** — a statistical measure showing the change in a variable, or a group of '
      'variables, relative to time, geographical location or another characteristic (Spiegel).',
      '**Base year** — the reference period other periods are compared with; should be '
      'economically stable and not too distant. Its index is 100.',
      '**Price relative** — the ratio of a single commodity\'s current-year price to its '
      'base-year price, $\\times 100$.',
      '**Price index** — a measure of the change in the *general* price level of a group of '
      'commodities.',
      '**Weights** — the relative importance attached to each item.',
      '**Unweighted index** — equal importance to every item. **Weighted index** — items '
      'weighted by quantity (or value).',
      '**Deflating** — dividing a money value series by a price index to express it in real '
      '(constant-price) terms.',
      '**Splicing** — joining two index series that have different base years.',
    ]},
    {'h3': 'Uses of index numbers'},
    {'ul': [
      'deflate a value series into real / physical terms;',
      'act as a business / economic barometer;',
      'show the trend of business or the economy;',
      'forecast, from a series of indices;',
      'assess the purchasing power of money;',
      'compare the standard of living across areas or countries.',
    ]},
    {'h3': 'Problems in constructing an index number'},
    {'ul': [
      'defining the purpose of the index;',
      'selecting the commodities / items (type, quantity, quality);',
      'selecting a reliable source of data;',
      'choosing the method of collecting data;',
      'choosing the base year;',
      'choosing the method of combining the data (which dictates the formula);',
      'choosing the weights.',
    ]},
    {'h3': 'Notation'},
    {'p': '$p_0$, $q_0$ = base-year price and quantity; $p_1$ (or $p_i$, $p_t$), $q_1$ = '
          'current-year price and quantity; $n$ = number of commodities; $\\sum$ over the '
          'commodities.'},
    {'h3': 'A. Unweighted indices (type + formula)'},
    {'fbox': {'h': 'Unweighted price indices', 'rows': [
      {'lb': 'Simple price relative (SPRI)', 'tex': '\\dfrac{p_1}{p_0} \\times 100'},
      {'lb': 'Simple aggregate price index (SAPI)',
       'tex': '\\dfrac{\\sum p_1}{\\sum p_0} \\times 100'},
      {'lb': 'Simple average of relatives (SARPI)',
       'tex': '\\dfrac{\\sum \\left(\\dfrac{p_1}{p_0} \\times 100\\right)}{n}'},
    ]}},
    {'h3': 'B. Weighted aggregative indices (type + formula)'},
    {'fbox': {'h': 'Weighted price indices', 'rows': [
      {'lb': 'Laspeyres (base-year quantities; upward bias)',
       'tex': 'P_L = \\dfrac{\\sum p_1 q_0}{\\sum p_0 q_0} \\times 100'},
      {'lb': 'Paasche (current-year quantities; downward bias)',
       'tex': 'P_P = \\dfrac{\\sum p_1 q_1}{\\sum p_0 q_1} \\times 100'},
      {'lb': "Fisher's ideal (geometric mean of L and P)",
       'tex': 'P_F = \\sqrt{P_L \\times P_P} = \\sqrt{\\dfrac{\\sum p_1 q_0}{\\sum p_0 q_0} '
              '\\times \\dfrac{\\sum p_1 q_1}{\\sum p_0 q_1}} \\times 100'},
      {'lb': 'Marshall–Edgeworth (average of base & current quantities)',
       'tex': 'P_{ME} = \\dfrac{\\sum p_1(q_0 + q_1)}{\\sum p_0(q_0 + q_1)} \\times 100 '
              '= \\dfrac{\\sum p_1 q_0 + \\sum p_1 q_1}{\\sum p_0 q_0 + \\sum p_0 q_1} '
              '\\times 100'},
    ]}},
    {'note': 'The column set for a weighted-index question: $p_0, q_0, p_1, q_1, \\; p_0 q_0, '
             '\\; p_1 q_0, \\; p_1 q_1, \\; p_0 q_1$. Every weighted index above is a ratio of '
             'two of those column totals.'},
    {'h3': 'C. A quantity index'},
    {'p': 'Swap the roles of $p$ and $q$: e.g. Laspeyres quantity index '
          '$= \\dfrac{\\sum q_1 p_0}{\\sum q_0 p_0} \\times 100$.'},
    {'h3': 'D. Using an index'},
    {'fbox': {'h': 'Deflation and base change', 'rows': [
      {'lb': 'Real (deflated) value',
       'tex': '\\text{Real} = \\dfrac{\\text{Money value}}{\\text{Price index}} \\times 100'},
      {'lb': 'Purchasing power of the naira',
       'tex': '\\text{PP} = \\dfrac{100}{\\text{Price index}}'},
      {'lb': 'Change of base / splicing',
       'tex': '\\text{New index} = \\dfrac{\\text{Old index}}'
              '{\\text{Old index of the new base year}} \\times 100'},
    ]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Simple price relative (SPRI)', 'tex': '\\frac{p_1}{p_0} \\times 100'},
  {'lb': 'Simple aggregate price index (SAPI)',
   'tex': '\\frac{\\sum p_1}{\\sum p_0} \\times 100'},
  {'lb': 'Simple average of relatives (SARPI)',
   'tex': '\\frac{\\sum \\left(\\frac{p_1}{p_0}\\times 100\\right)}{n}'},
  {'lb': 'Laspeyres price index (base-year quantities)',
   'tex': 'P_L = \\frac{\\sum p_1 q_0}{\\sum p_0 q_0} \\times 100'},
  {'lb': 'Paasche price index (current-year quantities)',
   'tex': 'P_P = \\frac{\\sum p_1 q_1}{\\sum p_0 q_1} \\times 100'},
  {'lb': "Fisher's ideal index", 'tex': 'P_F = \\sqrt{P_L \\times P_P}'},
  {'lb': 'Marshall–Edgeworth index',
   'tex': 'P_{ME} = \\frac{\\sum p_1(q_0 + q_1)}{\\sum p_0(q_0 + q_1)} \\times 100'},
  {'lb': 'Laspeyres quantity index',
   'tex': '\\frac{\\sum q_1 p_0}{\\sum q_0 p_0} \\times 100'},
  {'lb': 'Deflating a money series',
   'tex': '\\text{Real} = \\frac{\\text{Money}}{\\text{Price index}} \\times 100'},
  {'lb': 'Purchasing power of money',
   'tex': '\\text{PP} = \\frac{100}{\\text{Price index}}'},
  {'lb': 'Changing the base / splicing',
   'tex': '\\text{New} = \\frac{\\text{Old index}}{\\text{Old index at new base}} \\times 100'},
 ],
 'focus':
   'A dependable Section B question: a table of prices and quantities for four or five items and '
   'a request for Laspeyres, Paasche and Fisher. Build the four product columns once and read all '
   'three indices off the totals. Section A tests which index uses which weights, and the '
   'deflation calculation. Remember Laspeyres uses **base**-year quantities — the mnemonic is '
   'that L comes before P in the alphabet as the base comes before the current period.',
 'errors': [
   'Swapping the weights of Laspeyres and Paasche.',
   'Taking the arithmetic mean instead of the geometric mean for Fisher\'s index.',
   'Multiplying by the index instead of dividing when deflating a money series.',
   'Using the simple aggregate index where quantities are given.',
   'Forgetting to multiply by 100, giving an index of 1.30 instead of 130.',
 ],
 'quiz': {
  'mcq': [
   {'q': "Laspeyres' price index uses quantities of the",
    'o': ['current year', 'base year', 'average of both years', 'preceding year',
          'year with the highest output'],
    'a': 1,
    'w': 'Laspeyres holds the basket fixed at base-year quantities, which is why it is cheap to '
         'maintain but overstates inflation by ignoring substitution.',
    'src': 'Chapter 6.3', 'sec': '6.3'},
   {'q': "If Laspeyres' index is 121 and Paasche's is 116, Fisher's ideal index is",
    'o': ['118.5', '118.47', '237.0', '116.0', '121.0'],
    'a': 1,
    'w': "Fisher's index is the geometric mean of the other two.",
    'calc': 'P_F = \\sqrt{121 \\times 116} = \\sqrt{14{,}036} = 118.47',
    'src': 'Chapter 6.3', 'sec': '6.3'},
   {'q': 'A salary of ₦450,000 is earned when the price index is 180 (base 100). Its real value '
         'at base-year prices is',
    'o': ['₦810,000', '₦250,000', '₦270,000', '₦450,000', '₦2,500'],
    'a': 1,
    'w': 'Deflate by dividing the money value by the index and multiplying by 100.',
    'calc': '\\frac{450{,}000}{180} \\times 100 = 250{,}000',
    'src': 'Chapter 6.4', 'sec': '6.4'},
   {'q': 'The main defect of the simple aggregate price index is that',
    'o': ['it is difficult to compute', 'it requires quantity data',
          'its value depends on the units in which the items are quoted',
          'it cannot be expressed as a percentage', 'it always exceeds 100'],
    'a': 2,
    'w': 'Adding prices quoted in different units lets the item with the largest unit dominate '
         'the index for reasons unconnected with its importance. Weighting removes the problem.',
    'src': 'Chapter 6.2', 'sec': '6.2'},
   {'q': 'The CPI rose from 148 to 172 over a year. The rate of inflation was',
    'o': ['24%', '16.22%', '13.95%', '86%', '116.22%'],
    'a': 1,
    'w': 'Express the increase as a percentage of the earlier index.',
    'calc': '\\frac{172 - 148}{148} \\times 100 = \\frac{24}{148} \\times 100 = 16.22\\%',
    'src': 'Chapter 6.4', 'sec': '6.4'},
  ],
  'theory': [
   {'q': "Distinguish between Laspeyres' and Paasche's price indices, stating one advantage and "
         "one disadvantage of each, and explain why Fisher's index is described as ideal.",
    'marks': 8,
    'a': [
      {'tex': 'P_L = \\frac{\\sum p_1 q_0}{\\sum p_0 q_0} \\times 100 \\qquad '
              'P_P = \\frac{\\sum p_1 q_1}{\\sum p_0 q_1} \\times 100'},
      {'table': {'head': ['', 'Laspeyres', 'Paasche'], 'align': 'lll', 'rows': [
        ['Weights', 'Base-year quantities $q_0$', 'Current-year quantities $q_1$'],
        ['Basket', 'Fixed', 'Revised every period'],
        ['Advantage', 'Cheap: quantities are collected once, so the series is easily extended '
         'and directly comparable over time',
         'Reflects the current pattern of consumption, so it is more representative of what '
         'people actually buy now'],
        ['Disadvantage', 'Overstates the rise in prices, because it ignores substitution away '
         'from goods whose prices have risen',
         'Expensive, since quantities must be re-surveyed each period; and it understates the '
         'rise, because the current basket already reflects substitution. Earlier years are not '
         'directly comparable'],
      ]}},
      {'h4': "Fisher's ideal index"},
      {'tex': 'P_F = \\sqrt{P_L \\times P_P}'},
      {'p': 'It is the geometric mean of the two, so it lies between them and splits the '
            'difference between the upward bias of Laspeyres and the downward bias of Paasche. '
            'It is called **ideal** because it satisfies two formal tests that neither of the '
            'others satisfies:'},
      {'ul': [
        'the **time reversal test** — the index for period 1 on base 0, multiplied by the index '
        'for period 0 on base 1, equals unity; and',
        'the **factor reversal test** — the price index multiplied by the corresponding quantity '
        'index equals the change in total value.']},
      {'p': 'Its practical drawback is that it requires both sets of quantities, so it costs as '
            'much to compute as Paasche and is less easily interpreted.'}],
    'src': 'Chapter 6.3', 'sec': '6.3'},
  ]},
}
