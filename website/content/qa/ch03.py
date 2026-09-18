CH = {
 'n': 3,
 't': 'Measures of Variation',
 'brief': 'Range, mean deviation, variance, standard deviation and quartile deviation, and the '
          'coefficients of variation and skewness that make them comparable.',
 'outcomes': [
   'Compute the range and the quartile deviation',
   'Compute the mean deviation for grouped and ungrouped data',
   'Compute the variance and standard deviation by both the definition and the working formula',
   'Compute and interpret the coefficient of variation',
   'Compute Pearson\'s and Bowley\'s coefficients of skewness',
 ],
 'secs': [
  {'n': '3.1', 't': 'Why variation matters', 'b': [
    {'p': 'Two distributions can share a mean and be entirely different. A measure of location '
          'without a measure of spread describes almost nothing.'},
    {'eg': {'t': 'Same mean, different risk', 'q': [
      {'p': 'Two salesmen average ₦50,000 a day. A\'s daily figures are 48, 51, 49, 52, 50; B\'s '
            'are 10, 90, 20, 80, 50. Which would you rather employ?'}],
      'a': [
      {'p': 'Both means are ₦50,000. But A\'s figures cluster tightly and B\'s swing wildly. The '
            'range for A is $52 - 48 = 4$; for B it is $90 - 10 = 80$, twenty times as wide.'},
      {'p': 'A is predictable and can be planned around; B is a gamble. That difference is '
            'entirely invisible in the mean, and quantifying it is what this chapter is for.'}]}},
  ]},

  {'n': '3.2', 't': 'Range and quartile deviation', 'b': [
    {'fbox': {'h': 'Range and quartile deviation', 'rows': [
      {'lb': 'Range, ungrouped', 'tex': 'R = \\text{Largest} - \\text{Smallest}'},
      {'lb': 'Range, grouped',
       'tex': 'R = \\text{Upper boundary of last class} - \\text{Lower boundary of first class}'},
      {'lb': 'Quartile deviation (semi-interquartile range)',
       'tex': 'QD = \\frac{Q_3 - Q_1}{2}'},
      {'lb': 'Coefficient of quartile deviation',
       'tex': '\\frac{Q_3 - Q_1}{Q_3 + Q_1} \\times 100\\%'},
    ]}},
    {'p': 'The range uses only two observations and is destroyed by a single outlier. The quartile '
          'deviation ignores the extreme quarter at each end, so it is far more stable, but it '
          'still ignores the magnitude of most of the data.'},
  ]},

  {'n': '3.3', 't': 'Mean deviation', 'b': [
    {'p': 'The average of the **absolute** deviations from the mean. Absolute values are essential '
          '— the signed deviations from the mean always sum to zero.'},
    {'fbox': {'h': 'Mean deviation', 'rows': [
      {'lb': 'Ungrouped', 'tex': 'MD = \\frac{\\sum |x_i - \\bar{x}|}{n}'},
      {'lb': 'Grouped', 'tex': 'MD = \\frac{\\sum f|x - \\bar{x}|}{\\sum f}'},
    ]}},
    {'eg': {'t': 'Mean deviation', 'q': [
      {'p': 'Compute the mean deviation of the daily ATM withdrawals (₦m): 1, 2, 5, 7, 10.'}],
      'a': [
      {'tex': '\\bar{x} = \\frac{1 + 2 + 5 + 7 + 10}{5} = \\frac{25}{5} = 5'},
      {'table': {'align': 'rrr', 'head': ['$x$', '$x - \\bar{x}$', '$|x - \\bar{x}|$'], 'rows': [
        ['1', '−4', '4'], ['2', '−3', '3'], ['5', '0', '0'], ['7', '2', '2'], ['10', '5', '5'],
        ['25', '0', '14', '@tot'],
      ]}},
      {'tex': 'MD = \\frac{\\sum |x - \\bar{x}|}{n} = \\frac{14}{5} = 2.8'},
      {'note': 'The middle column sums to zero, which is the check that you have the right mean. '
               'If it does not, the mean is wrong.'}]}},
  ]},

  {'n': '3.4', 't': 'Variance and standard deviation', 'b': [
    {'p': 'Squaring the deviations, rather than taking absolute values, gives a measure that is '
          'algebraically well behaved and is the foundation of almost all further statistics.'},
    {'fbox': {'h': 'Variance and standard deviation', 'rows': [
      {'lb': 'Variance, ungrouped (definition)',
       'tex': '\\sigma^2 = \\frac{\\sum (x - \\bar{x})^2}{n}'},
      {'lb': 'Variance, ungrouped (working formula)',
       'tex': '\\sigma^2 = \\frac{\\sum x^2}{n} - \\left(\\frac{\\sum x}{n}\\right)^2',
       'nt': 'Much faster: no need to compute each deviation.'},
      {'lb': 'Variance, grouped',
       'tex': '\\sigma^2 = \\frac{\\sum f x^2}{\\sum f} - '
              '\\left(\\frac{\\sum f x}{\\sum f}\\right)^2'},
      {'lb': 'Standard deviation', 'tex': '\\sigma = \\sqrt{\\sigma^2}'},
      {'lb': 'Sample variance (unbiased)',
       'tex': 's^2 = \\frac{\\sum (x - \\bar{x})^2}{n - 1}',
       'nt': 'Divide by $n-1$ when the data is a sample and the population variance is being estimated.'},
    ]}},
    {'eg': {'t': 'Standard deviation, both ways', 'q': [
      {'p': 'Compute the standard deviation of 1, 2, 5, 7, 10.'}],
      'a': [
      {'h4': 'By definition'},
      {'table': {'align': 'rrr', 'head': ['$x$', '$x - \\bar{x}$', '$(x - \\bar{x})^2$'], 'rows': [
        ['1', '−4', '16'], ['2', '−3', '9'], ['5', '0', '0'], ['7', '2', '4'], ['10', '5', '25'],
        ['25', '0', '54', '@tot'],
      ]}},
      {'tex': '\\sigma^2 = \\frac{54}{5} = 10.8 \\qquad \\sigma = \\sqrt{10.8} = 3.286'},
      {'h4': 'By the working formula'},
      {'p': '$\\sum x = 25$, $\\sum x^2 = 1 + 4 + 25 + 49 + 100 = 179$.'},
      {'tex': '\\sigma^2 = \\frac{179}{5} - \\left(\\frac{25}{5}\\right)^2 = 35.8 - 25 = 10.8'},
      {'tex': '\\sigma = \\sqrt{10.8} = 3.286'},
      {'note': 'Identical, as they must be. In an exam use the working formula: it needs only '
               '$\\sum x$ and $\\sum x^2$, both of which you accumulate in one pass.'}]}},
    {'eg': {'t': 'Standard deviation of a grouped distribution', 'q': [
      {'p': 'Compute the standard deviation of the distribution from Chapter 2.'},
      {'table': {'align': 'lr', 'head': ['Class', '$f$'], 'rows': [
        ['10 – 19', '4'], ['20 – 29', '9'], ['30 – 39', '15'], ['40 – 49', '12'],
        ['50 – 59', '7'], ['60 – 69', '3'],
      ]}}],
      'a': [
      {'table': {'align': 'lrrrr', 'head': ['Class', '$f$', '$x$', '$fx$', '$fx^2$'], 'rows': [
        ['10 – 19', '4', '14.5', '58.0', '841.00'],
        ['20 – 29', '9', '24.5', '220.5', '5,402.25'],
        ['30 – 39', '15', '34.5', '517.5', '17,853.75'],
        ['40 – 49', '12', '44.5', '534.0', '23,763.00'],
        ['50 – 59', '7', '54.5', '381.5', '20,791.75'],
        ['60 – 69', '3', '64.5', '193.5', '12,480.75'],
        ['Total', '50', '', '1,905.0', '81,132.50', '@tot'],
      ]}},
      {'tex': '\\bar{x} = \\frac{1905}{50} = 38.1'},
      {'tex': '\\sigma^2 = \\frac{81{,}132.5}{50} - (38.1)^2 = 1622.65 - 1451.61 = 171.04'},
      {'tex': '\\sigma = \\sqrt{171.04} = 13.08'},
      {'warn': 'Note that $fx^2$ means $f \\times x^2$, not $(fx)^2$. For the first class that is '
               '$4 \\times 14.5^2 = 4 \\times 210.25 = 841$, not $58^2 = 3364$. Squaring $fx$ '
               'instead of $x$ is the commonest error in this computation.'}]}},
  ]},

  {'n': '3.5', 't': 'Coefficient of variation', 'b': [
    {'p': 'The standard deviation is in the units of the data, so it cannot compare a distribution '
          'of salaries with one of ages. The coefficient of variation is dimensionless and can.'},
    {'tex': 'CV = \\frac{\\sigma}{\\bar{x}} \\times 100\\%', 'tag': '(3.1)'},
    {'eg': {'t': 'Comparing consistency', 'q': [
      {'p': 'Branch A has mean daily sales of ₦840,000 with a standard deviation of ₦126,000. '
            'Branch B has mean daily sales of ₦2,400,000 with a standard deviation of ₦288,000. '
            'Which branch is more consistent?'}],
      'a': [
      {'tex': 'CV_A = \\frac{126{,}000}{840{,}000} \\times 100 = 15.0\\%'},
      {'tex': 'CV_B = \\frac{288{,}000}{2{,}400{,}000} \\times 100 = 12.0\\%'},
      {'p': '**Branch B is more consistent**, even though its standard deviation is more than '
            'twice as large in absolute terms. Relative to the size of its sales, its variation '
            'is smaller.'},
      {'note': 'A lower coefficient of variation means greater consistency, uniformity and '
               'stability — and lower risk. This interpretation, not the arithmetic, is where the '
               'marks are.'}]}},
  ]},

  {'n': '3.6', 't': 'Skewness', 'b': [
    {'p': 'Skewness measures the asymmetry of a distribution.'},
    {'table': {'head': ['Shape', 'Relationship', 'Coefficient'], 'align': 'lll', 'rows': [
      ['Symmetrical', '$\\text{Mean} = \\text{Median} = \\text{Mode}$', 'Zero'],
      ['Positively skewed (right tail)', '$\\text{Mean} > \\text{Median} > \\text{Mode}$', 'Positive'],
      ['Negatively skewed (left tail)', '$\\text{Mean} < \\text{Median} < \\text{Mode}$', 'Negative'],
    ]}},
    {'fbox': {'h': 'Coefficients of skewness', 'rows': [
      {'lb': "Pearson's first coefficient",
       'tex': 'SK_1 = \\frac{\\bar{x} - \\text{Mode}}{\\sigma}'},
      {'lb': "Pearson's second coefficient",
       'tex': 'SK_2 = \\frac{3(\\bar{x} - \\text{Median})}{\\sigma}',
       'nt': 'Used when the mode is ill-defined; follows from the empirical relationship.'},
      {'lb': "Bowley's (quartile) coefficient",
       'tex': 'SK_B = \\frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}',
       'nt': 'Bounded between −1 and +1.'},
    ]}},
    {'eg': {'t': 'Measuring skewness', 'q': [
      {'p': 'For the grouped distribution above: mean 38.1, median 37.5, mode 36.17, standard '
            'deviation 13.08, $Q_1 = 28.94$, $Q_3 = 47.42$. Compute Pearson\'s two coefficients '
            'and Bowley\'s coefficient, and comment.'}],
      'a': [
      {'tex': 'SK_1 = \\frac{38.1 - 36.17}{13.08} = \\frac{1.93}{13.08} = 0.148'},
      {'tex': 'SK_2 = \\frac{3(38.1 - 37.5)}{13.08} = \\frac{1.8}{13.08} = 0.138'},
      {'tex': 'SK_B = \\frac{47.42 + 28.94 - 2(37.5)}{47.42 - 28.94} = \\frac{1.36}{18.48} '
              '= 0.074'},
      {'p': 'All three are small and **positive**, so the distribution is mildly **positively '
            'skewed** — it has a slightly longer tail to the right, consistent with mean > median '
            '> mode.'},
      {'note': 'The three coefficients need not agree closely because they measure different '
               'things: the Pearson coefficients use the whole distribution through $\\sigma$, '
               'while Bowley\'s uses only the middle half. The **sign** is what matters, and here '
               'they all agree.'}]}},
  ]},

  {'n': '3.7', 't': 'Worksheet summary — definitions and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§3.1 Why variation matters** — two data sets can share a mean and differ entirely in '
      'spread; a measure of location alone describes almost nothing.',
      '**§3.2 Range and quartile deviation** — range = largest − smallest (grouped: upper '
      'boundary of the last class − lower boundary of the first); it uses only two values and '
      'one outlier destroys it. Quartile deviation $= (Q_3-Q_1)/2$ ignores the extreme quarter '
      'at each end and is more stable, but still ignores most of the data.',
      '**§3.3 Mean deviation** — the average of the *absolute* deviations from the mean '
      '($MD = \\sum|x-\\bar{x}|/n$, grouped $\\sum f|x-\\bar{x}|/\\sum f$); absolute values are '
      'needed because signed deviations always sum to zero — that sum-to-zero check confirms '
      'the mean used is correct.',
      '**§3.4 Variance and standard deviation** — definitional formula '
      '$\\sigma^2=\\sum(x-\\bar{x})^2/n$ and the faster working formula '
      '$\\sigma^2=\\sum x^2/n-(\\sum x/n)^2$ give identical answers; grouped uses $fx^2$ meaning '
      '$f\\times x^2$, **not** $(fx)^2$ — the commonest error in the chapter. Sample variance '
      'divides by $n-1$, not $n$, when estimating a population variance from a sample.',
      '**§3.5 Coefficient of variation** — $CV=\\sigma/\\bar{x}\\times100\\%$, dimensionless, so '
      'it can compare the spread of two *differently scaled* data sets; the **lower** CV is the '
      'more consistent/lower-risk series, even if its absolute standard deviation is larger.',
      '**§3.6 Skewness** — symmetrical: mean = median = mode, coefficient zero; positively '
      'skewed: mean > median > mode, coefficient positive; negatively skewed: the reverse. '
      'Three coefficients: Pearson\'s first $(\\bar{x}-\\text{Mode})/\\sigma$, Pearson\'s second '
      '$3(\\bar{x}-\\text{Median})/\\sigma$ (used when the mode is ill-defined), and Bowley\'s '
      '$(Q_3+Q_1-2Q_2)/(Q_3-Q_1)$ (bounded −1 to +1, uses only the middle half of the data). '
      'They needn\'t agree closely in size — only the **sign** matters for the shape verdict.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Measure of variation / dispersion / spread** — the degree to which numerical data '
      'spread about an average value.',
      '**Range** — highest value minus lowest value.',
      '**Mean deviation** — arithmetic mean of the *absolute* deviations from the mean.',
      '**Variance** — mean of the squared deviations from the mean.',
      '**Standard deviation** — the (positive) square root of the variance; same units as the '
      'data.',
      '**Quartile deviation / semi-interquartile range (SIR)** — half the interquartile range '
      '$Q_3 - Q_1$.',
      '**Coefficient of variation (CV)** — standard deviation as a percentage of the mean; '
      'dimensionless; used to compare the spread of two data sets. *Smaller CV → higher '
      'precision / better reliability.*',
      '**Skewness** — the degree of asymmetry of a frequency curve. Zero for a symmetrical / '
      'normal distribution; positive → mean > median > mode; negative → mean < median < mode.',
      '**Population** measures use $\\mu$ and divide by $N$; **sample** measures use $\\bar{x}$ '
      'and (in the study text) divide by $n$.',
    ]},
    {'h3': 'Range'},
    {'fbox': {'h': 'Range', 'rows': [
      {'lb': 'Ungrouped', 'tex': 'R = x_{\\max} - x_{\\min}'},
      {'lb': 'Grouped', 'tex': 'R = (\\text{upper boundary of last class}) - '
              '(\\text{lower boundary of first class})',
       'nt': 'The study text also accepts (upper limit of last class) − (lower limit of first '
             'class).'},
    ]}},
    {'h3': 'Mean deviation'},
    {'fbox': {'h': 'Mean deviation', 'rows': [
      {'lb': 'Ungrouped', 'tex': 'MD = \\frac{\\sum |x_i - \\bar{x}|}{n} = \\frac{\\sum |d_i|}{n}'},
      {'lb': 'Grouped', 'tex': 'MD = \\frac{\\sum f|x - \\bar{x}|}{\\sum f} '
              '= \\frac{\\sum f|d|}{\\sum f}',
       'nt': '$d_i = x_i - \\bar{x}$; $x$ is the class mark for grouped data.'},
    ]}},
    {'h3': 'Variance and standard deviation'},
    {'fbox': {'h': 'Definitional formulae', 'rows': [
      {'lb': 'Population SD, ungrouped',
       'tex': '\\sigma = \\sqrt{\\dfrac{\\sum (x - \\mu)^2}{N}}, \\qquad \\mu = \\frac{\\sum x}{N}'},
      {'lb': 'Sample SD, ungrouped',
       'tex': 's = \\sqrt{\\dfrac{\\sum (x - \\bar{x})^2}{n}}, \\qquad \\bar{x} = \\frac{\\sum x}{n}'},
      {'lb': 'Population SD, grouped',
       'tex': '\\sigma = \\sqrt{\\dfrac{\\sum f(x - \\mu)^2}{\\sum f}}'},
      {'lb': 'Sample SD, grouped',
       'tex': 's = \\sqrt{\\dfrac{\\sum f(x - \\bar{x})^2}{\\sum f}}'},
    ]}},
    {'fbox': {'h': 'Short-cut (working) formulae — ungrouped', 'rows': [
      {'lb': 'Form 1', 'tex': 's^2 = \\dfrac{\\sum (x - \\bar{x})^2}{n}'},
      {'lb': 'Form 2', 'tex': 's^2 = \\dfrac{\\sum x^2 - n\\bar{x}^2}{n}'},
      {'lb': 'Form 3',
       'tex': 's^2 = \\dfrac{\\sum x^2 - \\dfrac{(\\sum x)^2}{n}}{n} '
              '= \\dfrac{\\sum x^2}{n} - \\left(\\dfrac{\\sum x}{n}\\right)^2'},
    ]}},
    {'fbox': {'h': 'Short-cut (working) formulae — grouped', 'rows': [
      {'lb': 'Form 1', 'tex': 's^2 = \\dfrac{\\sum f(x - \\bar{x})^2}{\\sum f}'},
      {'lb': 'Form 2', 'tex': 's^2 = \\dfrac{\\sum fx^2 - (\\sum f)\\bar{x}^2}{\\sum f}'},
      {'lb': 'Form 3',
       'tex': 's^2 = \\dfrac{\\sum fx^2 - \\dfrac{(\\sum fx)^2}{\\sum f}}{\\sum f} '
              '= \\dfrac{\\sum fx^2}{\\sum f} - \\left(\\dfrac{\\sum fx}{\\sum f}\\right)^2'},
      {'lb': 'then', 'tex': 's = \\sqrt{s^2}'},
    ]}},
    {'note': 'The column set for a grouped SD question is $f$, $x$ (class mark), $fx$, $x^2$, '
             '$fx^2$ (and $cf$ if quartiles are also wanted). Compute $\\bar{x} = \\sum fx / '
             '\\sum f$ first.'},
    {'h3': 'Quartile deviation'},
    {'fbox': {'h': 'Semi-interquartile range', 'rows': [
      {'lb': 'Interquartile range', 'tex': 'IQR = Q_3 - Q_1'},
      {'lb': 'Quartile deviation (SIR)', 'tex': 'QD = \\dfrac{Q_3 - Q_1}{2}'},
      {'lb': 'Quartile (grouped), from Chapter 2',
       'tex': 'Q_i = L + \\left(\\dfrac{\\frac{iN}{4} - \\sum f_b}{f_Q}\\right) c',
       'nt': '$L$ = lower **boundary** of the $Q_i$ class; $\\sum f_b$ = cumulative frequency '
             'before it; $f_Q$ = its frequency; $c$ = its width.'},
    ]}},
    {'h3': 'Coefficient of variation'},
    {'tex': 'CV = \\dfrac{\\text{SD}}{\\text{Mean}} \\times 100\\% '
            '= \\dfrac{s}{\\bar{x}} \\times 100\\%'},
    {'h3': 'Coefficient of skewness'},
    {'fbox': {'h': 'Skewness', 'rows': [
      {'lb': 'Pearson, first coefficient',
       'tex': 'SK = \\dfrac{\\bar{x} - \\text{Mode}}{s}'},
      {'lb': 'Pearson, second coefficient',
       'tex': 'SK = \\dfrac{3(\\bar{x} - \\text{Median})}{s}'},
      {'lb': 'Bowley (quartile) coefficient',
       'tex': 'SK_B = \\dfrac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}',
       'nt': '$Q_2$ = median. Lies between −1 and +1.'},
    ]}},
    {'note': 'Comparing two distributions: the one with the **larger absolute** coefficient of '
             'skewness is "more skewed"; the one with the **smaller CV** is more '
             'consistent / reliable.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Range (ungrouped)', 'tex': 'R = x_{\\max} - x_{\\min}'},
  {'lb': 'Range (grouped)',
   'tex': 'R = \\text{upper boundary of last class} - \\text{lower boundary of first class}'},
  {'lb': 'Mean deviation (ungrouped)',
   'tex': 'MD = \\frac{\\sum |x - \\bar{x}|}{n}'},
  {'lb': 'Mean deviation (grouped)', 'tex': 'MD = \\frac{\\sum f|x - \\bar{x}|}{\\sum f}'},
  {'lb': 'Variance — definition (ungrouped)',
   'tex': '\\sigma^2 = \\frac{\\sum (x - \\mu)^2}{N}'},
  {'lb': 'Variance — short cut (ungrouped)',
   'tex': 's^2 = \\frac{\\sum x^2}{n} - \\left(\\frac{\\sum x}{n}\\right)^2 '
          '= \\frac{\\sum x^2 - n\\bar{x}^2}{n}'},
  {'lb': 'Variance — definition (grouped)',
   'tex': '\\sigma^2 = \\frac{\\sum f(x - \\mu)^2}{\\sum f}'},
  {'lb': 'Variance — short cut (grouped)',
   'tex': 's^2 = \\frac{\\sum fx^2}{\\sum f} - \\left(\\frac{\\sum fx}{\\sum f}\\right)^2'},
  {'lb': 'Standard deviation', 'tex': 's = \\sqrt{s^2}'},
  {'lb': 'Interquartile range', 'tex': 'IQR = Q_3 - Q_1'},
  {'lb': 'Quartile deviation / semi-interquartile range',
   'tex': 'QD = \\frac{Q_3 - Q_1}{2}'},
  {'lb': 'Quartile of a grouped distribution',
   'tex': 'Q_i = L + \\left(\\frac{\\frac{iN}{4} - \\sum f_b}{f_Q}\\right) c'},
  {'lb': 'Coefficient of variation',
   'tex': 'CV = \\frac{s}{\\bar{x}} \\times 100\\%'},
  {'lb': "Pearson's coefficient of skewness (1st)",
   'tex': 'SK = \\frac{\\bar{x} - \\text{Mode}}{s}'},
  {'lb': "Pearson's coefficient of skewness (2nd)",
   'tex': 'SK = \\frac{3(\\bar{x} - \\text{Median})}{s}'},
  {'lb': "Bowley's coefficient of skewness",
   'tex': 'SK_B = \\frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}'},
 ],
 'focus':
   'Appears in Section A every diet and often as half a Section B question, usually paired with '
   'Chapter 2 on the same data table. Build one table with columns $f$, $x$, $fx$, $fx^2$ and '
   'cumulative $f$, and it will answer every part of both chapters. The coefficient of variation '
   'and its interpretation are the highest-yield items — the examiner wants the conclusion, not '
   'just the percentage.',
 'errors': [
   'Computing $(fx)^2$ instead of $f x^2$.',
   'Omitting the absolute value in the mean deviation, giving zero.',
   'Comparing standard deviations of series with different means instead of using the coefficient '
   'of variation.',
   'Dividing by $n-1$ when the data is the whole population, or by $n$ when it is a sample and an '
   'estimate is required.',
   'Forgetting the factor of 3 in Pearson\'s second coefficient.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The mean deviation of 1, 2, 5, 7 and 10 is',
    'o': ['2.8', '3.286', '5.0', '2.0', '14.0'],
    'a': 0,
    'w': 'The mean is 5; the absolute deviations are 4, 3, 0, 2, 5, summing to 14.',
    'calc': 'MD = \\frac{|1-5| + |2-5| + |5-5| + |7-5| + |10-5|}{5} = \\frac{14}{5} = 2.8',
    'src': 'Chapter 3.3', 'sec': '3.3'},
   {'q': 'A distribution has $\\sum x = 60$, $\\sum x^2 = 800$ and $n = 6$. The variance is',
    'o': ['33.33', '133.33', '23.33', '100.00', '10.00'],
    'a': 2,
    'w': 'Apply the working formula: mean square minus square of the mean.',
    'calc': '\\sigma^2 = \\frac{800}{6} - \\left(\\frac{60}{6}\\right)^2 = 133.33 - 100 = 33.33',
    'src': 'Chapter 3.4', 'sec': '3.4'},
   {'q': 'A distribution has a mean of 250 and a standard deviation of 40. Its coefficient of '
         'variation is',
    'o': ['6.25%', '16%', '625%', '10%', '62.5%'],
    'a': 1,
    'w': 'The coefficient of variation expresses the standard deviation as a percentage of the '
         'mean, making distributions with different units comparable.',
    'calc': 'CV = \\frac{40}{250} \\times 100 = 16\\%',
    'src': 'Chapter 3.5', 'sec': '3.5'},
   {'q': 'If $Q_1 = 65.8$ and $Q_3 = 98.3$, the semi-interquartile range is',
    'o': ['32.5', '16.25', '82.05', '164.1', '8.125'],
    'a': 1,
    'w': 'The semi-interquartile range, or quartile deviation, is half the interquartile range.',
    'calc': 'QD = \\frac{98.3 - 65.8}{2} = \\frac{32.5}{2} = 16.25',
    'src': 'Chapter 3.2', 'sec': '3.2'},
   {'q': 'In a positively skewed distribution',
    'o': ['mean = median = mode', 'mean > median > mode', 'mean < median < mode',
          'median > mean > mode', 'mode > mean > median'],
    'a': 1,
    'w': 'A long right tail pulls the mean furthest, then the median, leaving the mode at the '
         'peak. Hence mean > median > mode and a positive coefficient of skewness.',
    'src': 'Chapter 3.6', 'sec': '3.6'},
   {'q': 'Which measure of dispersion uses every observation and is expressed in the same units '
         'as the data?',
    'o': ['Range', 'Variance', 'Standard deviation', 'Coefficient of variation',
          'Quartile deviation'],
    'a': 2,
    'w': 'The variance uses every observation but is in squared units. Taking the square root '
         'returns it to the original units, which is exactly why the standard deviation is '
         'preferred for reporting.',
    'src': 'Chapter 3.4', 'sec': '3.4'},
  ],
  'theory': [
   {'q': 'Explain what is meant by the coefficient of variation, state why it is used in '
         'preference to the standard deviation for comparing two distributions, and compute it '
         'for two branches: Branch X, mean ₦640,000, standard deviation ₦96,000; Branch Y, mean '
         '₦1,500,000, standard deviation ₦195,000. State which branch is more consistent.',
    'marks': 6,
    'a': [
      {'p': 'The **coefficient of variation** expresses the standard deviation as a percentage of '
            'the mean:'},
      {'tex': 'CV = \\frac{\\sigma}{\\bar{x}} \\times 100\\%'},
      {'p': 'The standard deviation is measured in the **units of the data**, so it cannot be '
            'compared between two distributions measured in different units, or between two '
            'distributions of very different magnitude in the same units. A standard deviation of '
            '₦100,000 is enormous relative to a mean of ₦200,000 and trivial relative to a mean '
            'of ₦50 million. Dividing by the mean removes the units and the scale, leaving a pure '
            'number that measures **relative** variability.'},
      {'tex': 'CV_X = \\frac{96{,}000}{640{,}000} \\times 100 = 15.0\\%'},
      {'tex': 'CV_Y = \\frac{195{,}000}{1{,}500{,}000} \\times 100 = 13.0\\%'},
      {'p': '**Branch Y is the more consistent**, since a lower coefficient of variation means '
            'less variability relative to the average. This is so even though Y\'s absolute '
            'standard deviation is more than twice X\'s — which is precisely the comparison the '
            'standard deviation alone would get wrong.'}],
    'src': 'Chapter 3.5', 'sec': '3.5'},
  ]},
}
