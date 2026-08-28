CH = {
 'n': 2,
 't': 'Measures of Location',
 'brief': 'Mean, median and mode for grouped and ungrouped data, the assumed-mean shortcut, and '
          'the measures of partition — quartiles, deciles and percentiles.',
 'outcomes': [
   'Compute the arithmetic, geometric and harmonic means',
   'Compute the mean of a grouped distribution, including by the assumed mean method',
   'Compute the median and mode of grouped and ungrouped data',
   'Apply the empirical relationship between mean, median and mode',
   'Compute quartiles, deciles and percentiles',
 ],
 'secs': [
  {'n': '2.1', 't': 'The arithmetic mean', 'b': [
    {'fbox': {'h': 'Arithmetic mean', 'rows': [
      {'lb': 'Ungrouped data', 'tex': '\\bar{x} = \\frac{\\sum x}{n}'},
      {'lb': 'Grouped or weighted data',
       'tex': '\\bar{x} = \\frac{\\sum fx}{\\sum f}',
       'nt': '$x$ is the class mark for grouped data.'},
      {'lb': 'Assumed mean (coding) method',
       'tex': '\\bar{x} = A + \\frac{\\sum fd}{\\sum f} \\quad\\text{where } d = x - A'},
      {'lb': 'Step deviation method',
       'tex': '\\bar{x} = A + \\left(\\frac{\\sum fu}{\\sum f}\\right) c '
              '\\quad\\text{where } u = \\frac{x - A}{c}',
       'nt': '$c$ is the common class width; this reduces the arithmetic to small integers.'},
    ]}},
    {'eg': {'t': 'Mean of a grouped distribution, three ways', 'q': [
      {'p': 'Compute the mean of the following distribution.'},
      {'table': {'align': 'lr', 'head': ['Class', 'Frequency'], 'rows': [
        ['10 – 19', '4'], ['20 – 29', '9'], ['30 – 39', '15'], ['40 – 49', '12'],
        ['50 – 59', '7'], ['60 – 69', '3'],
      ]}}],
      'a': [
      {'h4': 'Method 1 — direct'},
      {'table': {'align': 'lrrrrr',
        'head': ['Class', '$f$', '$x$', '$fx$', '$d = x - 34.5$', '$fd$'], 'rows': [
        ['10 – 19', '4', '14.5', '58.0', '−20', '−80'],
        ['20 – 29', '9', '24.5', '220.5', '−10', '−90'],
        ['30 – 39', '15', '34.5', '517.5', '0', '0'],
        ['40 – 49', '12', '44.5', '534.0', '10', '120'],
        ['50 – 59', '7', '54.5', '381.5', '20', '140'],
        ['60 – 69', '3', '64.5', '193.5', '30', '90'],
        ['Total', '50', '', '1,905.0', '', '180', '@tot'],
      ]}},
      {'tex': '\\bar{x} = \\frac{\\sum fx}{\\sum f} = \\frac{1905}{50} = 38.1'},
      {'h4': 'Method 2 — assumed mean, $A = 34.5$'},
      {'tex': '\\bar{x} = A + \\frac{\\sum fd}{\\sum f} = 34.5 + \\frac{180}{50} '
              '= 34.5 + 3.6 = 38.1'},
      {'h4': 'Method 3 — step deviation, $A = 34.5$, $c = 10$'},
      {'p': 'Here $u = d/10$ takes the values $-2, -1, 0, 1, 2, 3$ and $\\sum fu = 18$:'},
      {'tex': '\\bar{x} = 34.5 + \\left(\\frac{18}{50}\\right)(10) = 34.5 + 3.6 = 38.1'},
      {'note': 'All three give 38.1, as they must. The step deviation method turns five-figure '
               'multiplications into single-digit ones, which is worth knowing when you have no '
               'calculator memory to spare.'}]}},
    {'h3': 'Other means'},
    {'fbox': {'h': 'Geometric and harmonic means', 'rows': [
      {'lb': 'Geometric mean',
       'tex': 'GM = \\sqrt[n]{x_1 x_2 \\cdots x_n} = \\left(\\prod_{i=1}^{n} x_i\\right)^{1/n}',
       'nt': 'Used for average rates of growth and for index numbers.'},
      {'lb': 'Harmonic mean',
       'tex': 'HM = \\frac{n}{\\sum \\frac{1}{x_i}}',
       'nt': 'Used for averaging rates such as speed over equal distances.'},
    ]}},
    {'p': 'For any set of positive numbers not all equal, $HM < GM < \\bar{x}$.'},
  ]},

  {'n': '2.2', 't': 'The median', 'b': [
    {'p': 'The median is the value of the middle item when the data is arranged in order. It is '
          'unaffected by extreme values, which is why it is preferred for income and house-price '
          'data.'},
    {'fbox': {'h': 'Median', 'rows': [
      {'lb': 'Ungrouped, $n$ odd', 'tex': '\\text{Median} = x_{\\left(\\frac{n+1}{2}\\right)}'},
      {'lb': 'Ungrouped, $n$ even',
       'tex': '\\text{Median} = \\frac{x_{(n/2)} + x_{(n/2 + 1)}}{2}'},
      {'lb': 'Grouped data',
       'tex': '\\text{Median} = L + \\left(\\frac{\\frac{N}{2} - CF}{f_m}\\right) c',
       'nt': '$L$ = lower boundary of the median class; $CF$ = cumulative frequency before it; '
             '$f_m$ = its frequency; $c$ = its width; $N = \\sum f$.'},
    ]}},
    {'eg': {'t': 'Median of a grouped distribution', 'q': [
      {'p': 'Using the distribution in §2.1, compute the median.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['Class', '$f$', 'Cumulative $f$'], 'rows': [
        ['10 – 19', '4', '4'], ['20 – 29', '9', '13'], ['30 – 39', '15', '28'],
        ['40 – 49', '12', '40'], ['50 – 59', '7', '47'], ['60 – 69', '3', '50'],
      ]}},
      {'p': '$N/2 = 25$, which first exceeds a cumulative frequency at the class 30 – 39. So '
            '$L = 29.5$, $CF = 13$, $f_m = 15$, $c = 10$.'},
      {'tex': '\\text{Median} = 29.5 + \\left(\\frac{25 - 13}{15}\\right)(10) '
              '= 29.5 + \\frac{120}{15} = 29.5 + 8 = 37.5'},
      {'warn': 'Use the lower **boundary** (29.5), not the lower limit (30). Using 30 shifts every '
               'answer by half a unit, and the marker will spot it immediately.'}]}},
  ]},

  {'n': '2.3', 't': 'The mode', 'b': [
    {'p': 'The mode is the most frequently occurring value. A distribution may have no mode, one '
          '(unimodal), two (bimodal) or more.'},
    {'tex': '\\text{Mode} = L + \\left(\\frac{\\Delta_1}{\\Delta_1 + \\Delta_2}\\right) c',
     'tag': '(2.1)'},
    {'p': 'where $\\Delta_1$ is the excess of the modal class frequency over the class before it, '
          'and $\\Delta_2$ the excess over the class after it.'},
    {'eg': {'t': 'Mode of a grouped distribution', 'q': [
      {'p': 'Using the same distribution, compute the mode.'}],
      'a': [
      {'p': 'The modal class is 30 – 39 with $f = 15$. So $L = 29.5$, $\\Delta_1 = 15 - 9 = 6$, '
            '$\\Delta_2 = 15 - 12 = 3$, $c = 10$.'},
      {'tex': '\\text{Mode} = 29.5 + \\left(\\frac{6}{6 + 3}\\right)(10) = 29.5 + '
              '\\frac{60}{9} = 29.5 + 6.67 = 36.17'}]}},
    {'h3': 'The empirical relationship'},
    {'tex': '\\text{Mean} - \\text{Mode} = 3(\\text{Mean} - \\text{Median})', 'tag': '(2.2)'},
    {'p': 'or equivalently $\\text{Mode} = 3\\,\\text{Median} - 2\\,\\text{Mean}$. It holds '
          'approximately for a moderately skewed distribution, and questions use it to find a '
          'third measure when two are given.'},
    {'p': 'Check it here: $3(37.5) - 2(38.1) = 112.5 - 76.2 = 36.3$, against the computed mode of '
          '36.17 — close, as expected for a mildly skewed distribution.'},
    {'table': {'cap': 'Choosing a measure', 'head': ['Measure', 'Advantages', 'Disadvantages'],
     'align': 'lll', 'rows': [
      ['Mean', 'Uses all the data; suited to further algebra; unique',
       'Distorted by extreme values; may not be an actual value; cannot be found for open-ended classes'],
      ['Median', 'Not affected by extremes; can be found for open-ended distributions',
       'Ignores the magnitude of most observations; awkward algebraically'],
      ['Mode', 'The most typical value; unaffected by extremes; applies to qualitative data',
       'May not exist or may not be unique; ignores most of the data'],
    ]}},
  ]},

  {'n': '2.4', 't': 'Measures of partition', 'b': [
    {'p': 'Quartiles cut the distribution into four, deciles into ten, percentiles into a hundred. '
          'One formula covers all three — only the fraction of $N$ changes.'},
    {'fbox': {'h': 'Quantiles for grouped data', 'rows': [
      {'lb': 'Quartile $k$ (k = 1, 2, 3)',
       'tex': 'Q_k = L + \\left(\\frac{\\frac{kN}{4} - CF}{f_q}\\right) c'},
      {'lb': 'Decile $k$',
       'tex': 'D_k = L + \\left(\\frac{\\frac{kN}{10} - CF}{f_d}\\right) c'},
      {'lb': 'Percentile $k$',
       'tex': 'P_k = L + \\left(\\frac{\\frac{kN}{100} - CF}{f_p}\\right) c'},
    ]}},
    {'note': 'Note the identities: $Q_2 = D_5 = P_{50} = $ the median, and $Q_1 = P_{25}$, '
             '$Q_3 = P_{75}$, $D_k = P_{10k}$.'},
    {'eg': {'t': 'Quartiles', 'q': [
      {'p': 'Using the same distribution ($N = 50$), compute $Q_1$ and $Q_3$.'}],
      'a': [
      {'p': '**$Q_1$:** $\\dfrac{N}{4} = 12.5$, which falls in class 20 – 29 (cumulative 13). '
            '$L = 19.5$, $CF = 4$, $f = 9$, $c = 10$.'},
      {'tex': 'Q_1 = 19.5 + \\left(\\frac{12.5 - 4}{9}\\right)(10) = 19.5 + \\frac{85}{9} '
              '= 19.5 + 9.44 = 28.94'},
      {'p': '**$Q_3$:** $\\dfrac{3N}{4} = 37.5$, which falls in class 40 – 49 (cumulative 40). '
            '$L = 39.5$, $CF = 28$, $f = 12$, $c = 10$.'},
      {'tex': 'Q_3 = 39.5 + \\left(\\frac{37.5 - 28}{12}\\right)(10) = 39.5 + \\frac{95}{12} '
              '= 39.5 + 7.92 = 47.42'},
      {'note': 'These two feed straight into Chapter 3: the quartile deviation is '
               '$(Q_3 - Q_1)/2 = (47.42 - 28.94)/2 = 9.24$.'}]}},
    {'h3': 'Reading a quantile from the ogive'},
    {'p': 'On a cumulative frequency curve, go up the vertical axis to the required cumulative '
          'frequency ($N/2$ for the median, $N/4$ for $Q_1$, $70N/100$ for $P_{70}$), across to '
          'the curve, then down to the horizontal axis.'},
    {'eg': {'t': 'Which cumulative frequency to trace', 'q': [
      {'p': 'A distribution has a total frequency of 50. What cumulative frequency is traced on '
            'the ogive to give the 70th percentile?'}],
      'a': [
      {'tex': '\\frac{70}{100} \\times 50 = 35'},
      {'p': 'Trace across from a cumulative frequency of **35**.'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Arithmetic mean, ungrouped', 'tex': '\\bar{x} = \\frac{\\sum x}{n}'},
  {'lb': 'Arithmetic mean, grouped', 'tex': '\\bar{x} = \\frac{\\sum fx}{\\sum f}'},
  {'lb': 'Assumed mean method',
   'tex': '\\bar{x} = A + \\frac{\\sum fd}{\\sum f}, \\quad d = x - A'},
  {'lb': 'Geometric mean', 'tex': 'GM = \\sqrt[n]{x_1 x_2 \\cdots x_n}'},
  {'lb': 'Harmonic mean', 'tex': 'HM = \\frac{n}{\\sum \\frac{1}{x}}'},
  {'lb': 'Median, grouped',
   'tex': '\\text{Median} = L + \\left(\\frac{\\frac{N}{2} - CF}{f_m}\\right) c'},
  {'lb': 'Mode, grouped',
   'tex': '\\text{Mode} = L + \\left(\\frac{\\Delta_1}{\\Delta_1 + \\Delta_2}\\right) c'},
  {'lb': 'Empirical relationship',
   'tex': '\\text{Mode} = 3\\,\\text{Median} - 2\\,\\text{Mean}'},
  {'lb': 'Quantiles',
   'tex': 'Q_k = L + \\left(\\frac{\\frac{kN}{4} - CF}{f}\\right) c'},
 ],
 'focus':
   'Guaranteed marks in both sections. Section A asks for a mean, median or mode from a small '
   'grouped table, or applies the empirical relationship. Section B often asks for a full set of '
   'measures from one distribution and then for the standard deviation from the same table, so '
   'set the table up once with columns for $f$, $x$, $fx$, $fx^2$ and cumulative $f$ and use it '
   'throughout. The single most common error is using class limits where boundaries are required.',
 'errors': [
   'Using the lower class limit instead of the lower class boundary in the median and mode formulas.',
   'Identifying the median class from the frequency column instead of the cumulative frequency column.',
   'Taking $\\Delta_1$ and $\\Delta_2$ as the neighbouring frequencies rather than the differences.',
   'Forgetting that $c$ in the step deviation method must multiply the whole correction term.',
   'Using $N/2$ to locate a quartile.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The mean of 15, 17, 14, 16 and 18 is',
    'o': ['15', '16', '17', '18', '80'],
    'a': 1,
    'w': 'Sum the values and divide by how many there are.',
    'calc': '\\bar{x} = \\frac{15 + 17 + 14 + 16 + 18}{5} = \\frac{80}{5} = 16',
    'src': 'Chapter 2.1'},
   {'q': 'A distribution has a mean of 48 and a median of 45. Using the empirical relationship, '
         'the mode is approximately',
    'o': ['39', '42', '46.5', '51', '54'],
    'a': 0,
    'w': 'Apply Mode = 3 Median − 2 Mean.',
    'calc': '\\text{Mode} = 3(45) - 2(48) = 135 - 96 = 39',
    'src': 'Chapter 2.3'},
   {'q': 'For a distribution with total frequency 50, the cumulative frequency traced on the ogive '
         'to give the 70th percentile is',
    'o': ['70', '50', '35', '25', '15'],
    'a': 2,
    'w': 'The 70th percentile is the value below which 70% of the observations fall.',
    'calc': 'P_{70} \\text{ at } \\frac{70}{100} \\times 50 = 35',
    'src': 'Chapter 2.4'},
   {'q': 'In a grouped distribution the median class is 40 – 49 with frequency 12. The cumulative '
         'frequency up to 39 is 28 and $N = 80$. The median is',
    'o': ['45.5', '49.5', '49.0', '39.5', '48.5'],
    'a': 2,
    'w': 'Apply the grouped median formula with $L = 39.5$, $N/2 = 40$, $CF = 28$, $f_m = 12$, '
         '$c = 10$.',
    'calc': '39.5 + \\left(\\frac{40 - 28}{12}\\right)(10) = 39.5 + 10 = 49.5',
    'src': 'Chapter 2.2'},
   {'q': 'Which measure of location is most affected by extreme values?',
    'o': ['Mode', 'Median', 'Arithmetic mean', 'Lower quartile', 'Upper quartile'],
    'a': 2,
    'w': 'The arithmetic mean uses every observation, so a single very large or very small value '
         'pulls it. The median and mode are positional and are unaffected.',
    'src': 'Chapter 2.3'},
   {'q': 'For any set of positive numbers that are not all equal, the correct ordering is',
    'o': ['$\\bar{x} < GM < HM$', '$HM < GM < \\bar{x}$', '$GM < HM < \\bar{x}$',
          '$\\bar{x} < HM < GM$', 'they are always equal'],
    'a': 1,
    'w': 'The harmonic mean is smallest, the arithmetic mean largest, with the geometric mean '
         'between them. Equality holds only when every value is the same.',
    'src': 'Chapter 2.1'},
  ],
  'theory': [
   {'q': 'State THREE advantages and THREE disadvantages of the arithmetic mean as a measure of '
         'location, and explain when the median would be preferred.',
    'marks': 8,
    'a': [
      {'h4': 'Advantages of the arithmetic mean'},
      {'ol': ['It uses **every observation**, so no information is discarded.',
              'It is **uniquely defined** for any set of data.',
              'It is **algebraically tractable** — it can be combined across groups and is the '
              'basis of the variance, regression and most further analysis.',
              'It is **easily understood** and widely used.']},
      {'h4': 'Disadvantages'},
      {'ol': ['It is **distorted by extreme values**: one very large observation pulls it away '
              'from the bulk of the data.',
              'It **may not be an attainable value** — 2.4 children.',
              'It **cannot be computed** where the distribution has open-ended classes, unless an '
              'arbitrary limit is assumed.',
              'It can be **misleading for a skewed distribution**, where it lies away from the '
              'typical value.']},
      {'h4': 'When the median is preferred'},
      {'p': 'The median is preferred where the distribution is **markedly skewed** or contains '
            '**extreme values** — incomes, house prices, waiting times — because it is positional '
            'and is unaffected by the size of the extremes. It is also the only one of the two '
            'that can be computed where the distribution has **open-ended classes**, since only '
            'the position of the middle observation is needed, not the value of every one.'}],
    'src': 'Chapter 2.3'},
  ]},
}
