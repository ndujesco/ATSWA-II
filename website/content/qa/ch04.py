CH = {
 'n': 4,
 't': 'Measures of Relationship: Correlation and Regression',
 'brief': 'Measuring how two variables move together, and fitting the line that predicts one from '
          'the other.',
 'outcomes': [
   'Draw and interpret a scatter diagram',
   "Compute Pearson's product moment correlation coefficient",
   "Compute Spearman's rank correlation coefficient, including with tied ranks",
   'Interpret the coefficient of determination',
   'Fit a least squares regression line and use it to predict',
 ],
 'secs': [
  {'n': '4.1', 't': 'Correlation', 'b': [
    {'p': 'Correlation measures the **strength and direction** of the linear relationship between '
          'two variables. It ranges from $-1$ to $+1$.'},
    {'table': {'head': ['Value of $r$', 'Interpretation'], 'align': 'll', 'rows': [
      ['$+1$', 'Perfect positive linear relationship'],
      ['$+0.7$ to $+0.99$', 'Strong positive'],
      ['$+0.4$ to $+0.69$', 'Moderate positive'],
      ['$0$', 'No linear relationship'],
      ['$-0.4$ to $-0.69$', 'Moderate negative'],
      ['$-1$', 'Perfect negative linear relationship'],
    ]}},
    {'warn': '**Correlation is not causation.** A high $r$ between two series may reflect a causal '
             'link either way, a common third cause, or pure coincidence (a spurious correlation). '
             'Saying so is worth a mark whenever an interpretation is asked for.'},
    {'fbox': {'h': 'Correlation coefficients', 'rows': [
      {'lb': "Pearson's product moment correlation coefficient",
       'tex': 'r = \\frac{n\\sum xy - \\sum x \\sum y}'
              '{\\sqrt{\\left[n\\sum x^2 - (\\sum x)^2\\right]\\left[n\\sum y^2 - '
              '(\\sum y)^2\\right]}}',
       'nt': 'For measured (interval or ratio) data.'},
      {'lb': "Spearman's rank correlation coefficient",
       'tex': 'r_s = 1 - \\frac{6\\sum d^2}{n(n^2 - 1)}',
       'nt': '$d$ is the difference between the two ranks of the same item. For ranked or '
             'ordinal data.'},
      {'lb': 'Coefficient of determination',
       'tex': 'r^2',
       'nt': 'The proportion of the variation in $y$ explained by the variation in $x$.'},
    ]}},
    {'eg': {'t': "Pearson's correlation coefficient", 'q': [
      {'p': 'Compute $r$ for the following data.'},
      {'table': {'align': 'lrrrrr', 'head': ['', '', '', '', '', ''], 'rows': [
        ['$x$', '1', '2', '3', '4', '5'],
        ['$y$', '2', '5', '4', '8', '11'],
      ]}}],
      'a': [
      {'table': {'align': 'rrrrr', 'head': ['$x$', '$y$', '$xy$', '$x^2$', '$y^2$'], 'rows': [
        ['1', '2', '2', '1', '4'],
        ['2', '5', '10', '4', '25'],
        ['3', '4', '12', '9', '16'],
        ['4', '8', '32', '16', '64'],
        ['5', '11', '55', '25', '121'],
        ['15', '30', '111', '55', '230', '@tot'],
      ]}},
      {'tex': 'r = \\frac{5(111) - (15)(30)}{\\sqrt{[5(55) - 15^2][5(230) - 30^2]}}'},
      {'tex': '= \\frac{555 - 450}{\\sqrt{(275 - 225)(1150 - 900)}} '
              '= \\frac{105}{\\sqrt{50 \\times 250}} = \\frac{105}{\\sqrt{12500}}'},
      {'tex': '= \\frac{105}{111.803} = 0.939'},
      {'p': 'A **strong positive** linear relationship. The coefficient of determination is '
            '$r^2 = 0.882$, so about **88%** of the variation in $y$ is explained by the '
            'variation in $x$.'}]}},
    {'eg': {'t': "Spearman's rank correlation", 'q': [
      {'p': 'Two judges ranked five contestants as follows. Compute the rank correlation.'},
      {'table': {'align': 'lrrrrr',
        'head': ['Contestant', 'X1', 'X2', 'X3', 'X4', 'X5'], 'rows': [
        ['Rank by A', '4', '5', '1', '3', '2'],
        ['Rank by B', '3', '2', '1', '5', '4'],
      ]}}],
      'a': [
      {'table': {'align': 'lrrrr',
        'head': ['Contestant', '$R_A$', '$R_B$', '$d$', '$d^2$'], 'rows': [
        ['X1', '4', '3', '1', '1'],
        ['X2', '5', '2', '3', '9'],
        ['X3', '1', '1', '0', '0'],
        ['X4', '3', '5', '−2', '4'],
        ['X5', '2', '4', '−2', '4'],
        ['', '', '', '0', '18', '@tot'],
      ]}},
      {'tex': 'r_s = 1 - \\frac{6\\sum d^2}{n(n^2 - 1)} = 1 - \\frac{6(18)}{5(5^2 - 1)} '
              '= 1 - \\frac{108}{5(24)} = 1 - \\frac{108}{120}'},
      {'tex': '= 1 - 0.9 = 0.1'},
      {'p': 'A rank correlation of **0.1** — almost no agreement between the judges.'},
      {'note': 'The $d$ column must sum to zero. If it does not, a rank has been copied wrongly. '
               'Where ranks are **tied**, assign each tied item the average of the ranks they '
               'would have occupied: two items tied for 3rd and 4th both get 3.5, and the next '
               'is 5th.'}]}},
  ]},

  {'n': '4.2', 't': 'Regression', 'b': [
    {'p': 'Regression fits the straight line $y = a + bx$ that minimises the sum of the squared '
          'vertical distances from the points to the line — the **least squares** line.'},
    {'fbox': {'h': 'Least squares regression of $y$ on $x$', 'rows': [
      {'lb': 'Slope (regression coefficient)',
       'tex': 'b = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2}'},
      {'lb': 'Intercept',
       'tex': 'a = \\bar{y} - b\\bar{x} = \\frac{\\sum y - b\\sum x}{n}'},
      {'lb': 'The fitted line', 'tex': 'y = a + bx'},
      {'lb': 'Relationship with correlation',
       'tex': 'r = \\pm\\sqrt{b_{yx} \\cdot b_{xy}}',
       'nt': '$r$ and $b$ always carry the same sign.'},
    ]}},
    {'p': 'In $y = a + bx$, $y$ is the **dependent** variable (the one being predicted) and $x$ '
          'the **independent** or explanatory variable. The line always passes through the point '
          '$(\\bar{x}, \\bar{y})$, which is a useful check.'},
    {'eg': {'t': 'Fitting a regression line', 'q': [
      {'p': 'Fit the line $y = a + bx$ to the data:'},
      {'table': {'align': 'lrrr', 'head': ['', '', '', ''], 'rows': [
        ['$x$', '1', '2', '3'],
        ['$y$', '9', '5', '7'],
      ]}},
      {'p': 'and find the values of $a$ and $b$.'}],
      'a': [
      {'table': {'align': 'rrrr', 'head': ['$x$', '$y$', '$xy$', '$x^2$'], 'rows': [
        ['1', '9', '9', '1'], ['2', '5', '10', '4'], ['3', '7', '21', '9'],
        ['6', '21', '40', '14', '@tot'],
      ]}},
      {'tex': 'b = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2} '
              '= \\frac{3(40) - (6)(21)}{3(14) - 6^2} = \\frac{120 - 126}{42 - 36} '
              '= \\frac{-6}{6} = -1'},
      {'tex': 'a = \\bar{y} - b\\bar{x} = \\frac{21}{3} - (-1)\\left(\\frac{6}{3}\\right) '
              '= 7 + 2 = 9'},
      {'p': 'The fitted line is $y = 9 - x$.'},
      {'p': 'Check: at $\\bar{x} = 2$, $y = 9 - 2 = 7 = \\bar{y}$. ✓'},
      {'note': 'A **negative** $b$ means the line slopes downward: as $x$ rises, $y$ falls. The '
               'magnitude of $b$ is the change in $y$ for a one-unit change in $x$ — a steep '
               'upward line has a large positive gradient.'}]}},
    {'h3': 'Prediction and its limits'},
    {'ul': [
      '**Interpolation** — predicting within the range of the observed $x$ values. Reasonably safe.',
      '**Extrapolation** — predicting outside that range. Unreliable, because there is no evidence '
      'the relationship continues to hold.',
      'The line of $y$ on $x$ is **not** the same as the line of $x$ on $y$; use the one that '
      'predicts the variable the question asks for.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': "Pearson's correlation coefficient",
   'tex': 'r = \\frac{n\\sum xy - \\sum x \\sum y}{\\sqrt{[n\\sum x^2 - (\\sum x)^2]'
          '[n\\sum y^2 - (\\sum y)^2]}}'},
  {'lb': "Spearman's rank correlation",
   'tex': 'r_s = 1 - \\frac{6\\sum d^2}{n(n^2 - 1)}'},
  {'lb': 'Coefficient of determination', 'tex': 'r^2'},
  {'lb': 'Regression slope',
   'tex': 'b = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2}'},
  {'lb': 'Regression intercept', 'tex': 'a = \\bar{y} - b\\bar{x}'},
 ],
 'focus':
   'One of the most reliably examined chapters, in both sections. Section A asks for $b$, for $a$, '
   'or for $r_s$ from a small table; Section B asks for the full correlation and regression '
   'analysis of six or eight pairs, then for a prediction and a comment. Set out the columns '
   '$x, y, xy, x^2, y^2$ every time — the same table serves both $r$ and $b$. Always end with an '
   'interpretation sentence: a bare number rarely earns the last mark.',
 'errors': [
   'Mixing up which variable is dependent. $y$ is what is being predicted.',
   'Squaring the sums instead of summing the squares: $\\sum x^2 \\ne (\\sum x)^2$.',
   'Forgetting the 6 in Spearman\'s formula, or using $n^2$ instead of $n(n^2-1)$.',
   'Reporting $r^2$ when $r$ was asked for, or vice versa.',
   'Extrapolating far beyond the data and treating the prediction as reliable.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'For the data $x$: 1, 2, 3 and $y$: 9, 5, 7, the value of $b$ in the regression line '
         '$y = a + bx$ is',
    'o': ['−1', '−2', '−3', '−4', '−5'],
    'a': 0,
    'w': 'Compute the sums and apply the slope formula.',
    'calc': 'b = \\frac{3(40) - (6)(21)}{3(14) - 36} = \\frac{-6}{6} = -1',
    'src': 'Chapter 4.2'},
   {'q': 'For the same data, the value of $a$ is',
    'o': ['6', '7', '8', '9', '10'],
    'a': 3,
    'w': 'The intercept is the mean of $y$ less $b$ times the mean of $x$.',
    'calc': 'a = 7 - (-1)(2) = 9',
    'src': 'Chapter 4.2'},
   {'q': 'In the regression line $y = a + bx$, $y$ is a/an ……… variable while $x$ is a/an ……… '
         'variable.',
    'o': ['constant, dependent', 'constant, independent', 'dependent, independent',
          'independent, dependent', 'dependent, constant'],
    'a': 2,
    'w': '$y$ is the variable being explained or predicted, so it is dependent; $x$ is the '
         'explanatory variable, so it is independent.',
    'src': 'Chapter 4.2'},
   {'q': 'Five items are ranked by two judges and $\\sum d^2 = 18$. Spearman\'s rank correlation '
         'coefficient is',
    'o': ['0.9', '0.1', '−0.1', '0.5', '0.82'],
    'a': 1,
    'w': 'Apply the rank correlation formula with $n = 5$.',
    'calc': 'r_s = 1 - \\frac{6(18)}{5(25-1)} = 1 - \\frac{108}{120} = 1 - 0.9 = 0.1',
    'src': 'Chapter 4.1'},
   {'q': 'A correlation coefficient of $-0.92$ indicates',
    'o': ['a weak relationship', 'no relationship',
          'a strong relationship in which $y$ falls as $x$ rises',
          'a strong relationship in which $y$ rises as $x$ rises',
          'that $x$ causes $y$ to fall'],
    'a': 2,
    'w': 'The magnitude 0.92 shows the relationship is strong; the negative sign shows it is '
         'inverse. It shows association only — it does not establish that $x$ causes anything.',
    'src': 'Chapter 4.1'},
   {'q': 'If $r = 0.8$, the percentage of the variation in $y$ explained by the variation in $x$ is',
    'o': ['80%', '64%', '89%', '20%', '36%'],
    'a': 1,
    'w': 'The coefficient of determination is $r^2$.',
    'calc': 'r^2 = 0.8^2 = 0.64 = 64\\%',
    'src': 'Chapter 4.1'},
   {'q': 'Which of the following indicates a very steep and upward sloping regression line?',
    'o': ['A gradient of 0.05', 'A gradient of −4.5', 'A gradient of 4.5', 'A gradient of 0',
          'A gradient of −0.05'],
    'a': 2,
    'w': 'Upward sloping means a positive gradient; steep means a large magnitude. A gradient of '
         '4.5 is both.',
    'src': 'Chapter 4.2'},
  ],
  'theory': [
   {'q': 'Distinguish between correlation and regression, and explain why a high correlation '
         'coefficient does not establish that one variable causes the other.',
    'marks': 6,
    'a': [
      {'table': {'head': ['', 'Correlation', 'Regression'], 'align': 'lll', 'rows': [
        ['Purpose', 'Measures the strength and direction of a relationship',
         'Establishes the form of the relationship as an equation'],
        ['Output', 'A single coefficient between −1 and +1', 'A line $y = a + bx$'],
        ['Symmetry', 'Symmetric: $r_{xy} = r_{yx}$',
         'Not symmetric: the line of $y$ on $x$ differs from that of $x$ on $y$'],
        ['Use', 'To describe association', 'To predict a value of the dependent variable'],
        ['Units', 'Dimensionless', 'In the units of the variables'],
      ]}},
      {'h4': 'Why correlation is not causation'},
      {'p': 'A correlation coefficient measures only how closely two series move together. A high '
            'value may arise for any of four reasons:'},
      {'ol': [
        '$x$ genuinely causes $y$.',
        '$y$ genuinely causes $x$ — the direction is the reverse of the one assumed.',
        'A **third variable** causes both. Ice cream sales and drowning deaths correlate strongly '
        'because both rise with temperature.',
        '**Coincidence** — a spurious correlation, which becomes increasingly likely as more pairs '
        'of series are tested.']},
      {'p': 'Establishing causation requires a plausible mechanism, correct time ordering, and '
            'ideally controlled experiment — none of which a correlation coefficient supplies.'}],
    'src': 'Chapter 4.1'},
  ]},
}
