CH = {
 'n': 4,
 't': 'Measures of Relationship: Correlation and Regression',
 'brief': 'Measuring how two variables move together, and fitting the line that predicts one from '
          'the other.',
 'outcomes': [
   'Draw and interpret a scatter diagram',
   "Compute Pearson's product moment correlation coefficient",
   "Compute Spearman's rank correlation coefficient, including with tied ranks",
   'Fit a simple linear regression line by the graphical method and by the algebraic '
   '(least squares) method, and use it to predict',
 ],
 'secs': [
  {'n': '4.1', 't': 'Correlation', 'b': [
    {'p': 'Two variables are **correlated** or related when a change in one results in a change '
          'in the other. Correlation measures the **degree of association** between them. The '
          'degree of correlation $r$ is a real number between $-1$ and $+1$ inclusive.'},
    {'ul': [
      'Positive correlation — $0 < r < 1$ (the two variables move in the same direction, e.g. '
      'income and expenditure of a family).',
      'Perfect positive correlation — $r = 1$.',
      'Negative correlation — $-1 < r < 0$ (the variables move in opposite directions — e.g. '
      'number of labourers and time to complete a job; demand and price of a commodity).',
      'Perfect negative correlation — $r = -1$.',
      'Zero correlation — $r = 0$ (no fixed pattern between the two variables).',
    ]},
    {'note': 'Interpretation, by how close $r$ is to $\\pm 1$: $r=+0.92$ is good/strong positive '
             'correlation; $r=-0.96$ is good/strong negative correlation; $r=-0.12$ or $r=+0.26$ '
             'is poor or non-existent correlation; $r=0$ is no correlation at all. The same scale '
             'is used to read Spearman\'s $R$.'},
    {'fbox': {'h': 'Correlation coefficients', 'rows': [
      {'lb': "Pearson's product moment correlation coefficient",
       'tex': 'r = \\frac{n\\sum xy - \\sum x \\sum y}'
              '{\\sqrt{\\left[n\\sum x^2 - (\\sum x)^2\\right]\\left[n\\sum y^2 - '
              '(\\sum y)^2\\right]}}',
       'nt': 'For measured (interval or ratio) data. Also written as covariance$(x,y)$ over '
             '$\\sqrt{\\text{Var}(x)\\,\\text{Var}(y)}$.'},
      {'lb': "Spearman's rank correlation coefficient",
       'tex': 'r_s = 1 - \\frac{6\\sum d^2}{n(n^2 - 1)}',
       'nt': '$d$ is the difference between the two ranks of the same item. For ranked or '
             'ordinal data.'},
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
      {'p': 'Since $r=0.939$ is close to $+1$, this is a **good, strong positive correlation** '
            'between $x$ and $y$.'}]}},
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
    {'p': 'Where correlation measures the *degree* of association, regression looks at the '
          '*nature* of the relationship between $x$ and $y$ — expressed as a mathematical model '
          'called the **regression equation**, $y = a + bx$, where $a$ is the intercept on the '
          '$y$-axis and $b$ (the regression coefficient) is the slope, indicating the type of '
          'correlation between the variables. Unlike correlation, regression **requires** the '
          'independent and dependent variables to be distinguished.'},
    {'h3': 'Two methods of fitting the line'},
    {'h4': '(a) Graphical method'},
    {'ol': [
      'draw the scatter diagram for the data;',
      'draw a straight line through two points on the diagram — one of the points should be '
      '$(\\bar{x}, \\bar{y})$;',
      'read the constants $a$ and $b$ off the graph, where $a$ is the intercept on the $y$-axis '
      'and $b = \\dfrac{\\text{vertical length}}{\\text{horizontal length}}$ of the line drawn;',
      'state the regression line $y = a + bx$.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 4.8/4.9 — graphical and algebraic methods agree',
      'open': True, 'q': [
      {'p': 'Find the relationship between $y$ and $x$: $x=1,2,3,4,5$; $y=3,5,7,9,11$ — first '
            'graphically, then algebraically.'}],
      'a': [
      {'p': 'Graphically, a line through the points has intercept $a=1$ and slope '
            '$b=\\dfrac{11-5}{5-2}=\\dfrac{6}{3}=2$, giving $y=1+2x$.'},
      {'table': {'align': 'rrrr', 'head': ['$x$', '$y$', '$xy$', '$x^2$'], 'rows': [
        ['1', '3', '3', '1'], ['2', '5', '10', '4'], ['3', '7', '21', '9'],
        ['4', '9', '36', '16'], ['5', '11', '55', '25'],
        ['15', '35', '125', '55', '@tot'],
      ]}},
      {'tex': 'b = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2} = '
              '\\frac{5(125) - (15)(35)}{5(55) - 15^2} = \\frac{625-525}{275-225} = '
              '\\frac{100}{50} = 2'},
      {'tex': 'a = \\bar{y} - b\\bar{x} = \\frac{35}{5} - 2\\left(\\frac{15}{5}\\right) = 7 - 6 = 1'},
      {'note': 'Both methods give $y = 1 + 2x$ — as they must, since they fit the same data.'}]}},
    {'h4': '(b) Algebraic (least squares) method'},
    {'p': 'The normal equations, derived by the method of least squares, are:'},
    {'tex': 'an + b\\sum x = \\sum y \\qquad\\text{and}\\qquad a\\sum x + b\\sum x^2 = \\sum xy'},
    {'p': 'Solving these simultaneously for the line of $y$ on $x$:'},
    {'fbox': {'h': 'Least squares regression of $y$ on $x$', 'rows': [
      {'lb': 'Slope (regression coefficient)',
       'tex': 'b = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2}'},
      {'lb': 'Intercept',
       'tex': 'a = \\bar{y} - b\\bar{x} = \\frac{\\sum y - b\\sum x}{n}'},
      {'lb': 'The fitted line', 'tex': 'y = a + bx'},
    ]}},
    {'p': 'In $y = a + bx$, $y$ is the **dependent** variable (the one being predicted) and $x$ '
          'the **independent** or explanatory variable. It is important to distinguish these — '
          'this is not necessary for correlation.'},
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
    {'h3': 'Regression of $x$ on $y$'},
    {'p': 'Sections above fit $y$ on $x$ (predicting $y$ from a given $x$). Sometimes the '
          'reverse is wanted: $x = a\' + b\'y$, treating $y$ as independent and $x$ as '
          'dependent.'},
    {'fbox': {'h': 'Least squares regression of $x$ on $y$', 'rows': [
      {'lb': "Slope", 'tex': "b' = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum y^2 - (\\sum y)^2}"},
      {'lb': 'Intercept', 'tex': "a' = \\bar{x} - b'\\bar{y}"},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 4.10/4.11 — regression of $y$ on $x$ AND of $x$ '
      'on $y$, from the same data', 'open': True, 'q': [
      {'p': 'A trader\'s income ($x$, ₦\'000) and expenditure ($y$, ₦\'000) over 10 months:'},
      {'table': {'align': 'lrrrrrrrrrr', 'head': ['', '1', '2', '3', '4', '5', '6', '7', '8',
        '9', '10'], 'rows': [
        ['$x$', '8', '18', '52', '38', '26', '60', '40', '50', '82', '75'],
        ['$y$', '2', '4', '5', '7', '9', '11', '13', '15', '20', '23'],
      ]}},
      {'p': 'Fit (a) the regression line of $y$ on $x$, and (b) the regression line of $x$ on '
            '$y$.'}],
      'a': [
      {'p': 'From the raw data: $n=10$, $\\sum x=449$, $\\sum y=109$, $\\sum xy=6143$, '
            '$\\sum x^2=25{,}261$, $\\sum y^2=1{,}619$.'},
      {'h4': '(a) $y$ on $x$'},
      {'tex': 'b = \\frac{10(6143) - (449)(109)}{10(25{,}261) - 449^2} = '
              '\\frac{61{,}430 - 48{,}941}{252{,}610 - 201{,}601} = \\frac{12{,}489}{51{,}009} '
              '= 0.2448'},
      {'tex': '\\bar{x} = 44.9, \\quad \\bar{y} = 10.9 \\quad\\Rightarrow\\quad '
              'a = 10.9 - 0.2448(44.9) = 10.9 - 10.9915 = -0.0915'},
      {'p': 'Regression line of $y$ on $x$: $\\;y = -0.0915 + 0.2448x$.'},
      {'h4': '(b) $x$ on $y$'},
      {'tex': "b' = \\frac{10(6143) - (449)(109)}{10(1{,}619) - 109^2} = "
              "\\frac{12{,}489}{16{,}190 - 11{,}881} = \\frac{12{,}489}{4{,}309} = 2.898"},
      {'tex': "a' = 44.9 - 2.898(10.9) = 44.9 - 31.59 = 13.31"},
      {'p': 'Regression line of $x$ on $y$: $\\;x = 13.31 + 2.898y$.'},
      {'warn': 'Comparing the two lines shows they have **nothing in common** — regression of '
               '$y$ on $x$ is definitely different from regression of $x$ on $y$; one is not '
               'simply a rearrangement of the other.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 4.13 — predicting from a fitted line',
      'open': True, 'q': [
      {'p': 'Using $y = -0.09 + 0.2448x$ from the example above, estimate expenditure when '
            'income is ₦29,000.'}],
      'a': [
      {'tex': 'y = -0.09 + 0.2448(29) = -0.09 + 7.10 = 7.01'},
      {'p': 'Estimated expenditure $\\approx$ **₦7,010**.'}]}},
  ]},

  {'n': '4.3', 't': 'Worksheet summary — definitions and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§4.1 Correlation** — strength/direction of a *linear* relationship, $-1\\le r\\le1$; '
      'Pearson\'s $r$ (measured data) and Spearman\'s $r_s=1-6\\sum d^2/n(n^2-1)$ (ranked '
      'data, tied items share the average of the positions they occupy) with the $d$-column '
      'always summing to zero as a check; $r^2$ is the proportion of $y$\'s variation '
      'explained by $x$. **Correlation is not causation** — a high $r$ may reflect a genuine '
      'causal link either way, a common third cause, or coincidence.',
      '**§4.2 Regression** — fits $y=a+bx$ by least squares (minimises squared vertical '
      'distances); $b=(n\\sum xy-\\sum x\\sum y)/(n\\sum x^2-(\\sum x)^2)$, then '
      '$a=\\bar{y}-b\\bar{x}$; $r$ and $b$ always share the same sign; the line always passes '
      'through $(\\bar{x},\\bar{y})$ — use that as a check. The line of $y$ on $x$ is **not** '
      'the line of $x$ on $y$ — use whichever the question asks you to predict. '
      '**Interpolation** (within the data range) is safe; **extrapolation** (beyond it) is '
      'not, since there is no evidence the relationship continues.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Univariate** data — one variable. **Bivariate** data — two variables, written as '
      'points $(x, y)$.',
      '**Independent (explanatory) variable** $x$; **dependent (response) variable** $y$. The '
      'distinction matters for regression, **not** for correlation.',
      '**Scatter diagram** — bivariate data plotted on rectangular axes to reveal the '
      'relationship.',
      '**Correlation** — the *degree of association* between two variables. Coefficient $r$ '
      'lies in $-1 \\le r \\le 1$.',
      '**Regression** — the *pattern / nature* of the relationship, expressed as an equation.',
      '**Coefficient of determination** $r^2$ — the proportion of the variation in $y$ '
      'explained by $x$.',
      '**Rank correlation** — correlation computed from ranks (ordinal data) rather than actual '
      'values.',
    ]},
    {'h3': 'Types of correlation (name + condition)'},
    {'ul': [
      'Positive correlation — $0 < r < 1$',
      'Perfect positive correlation — $r = 1$',
      'Negative correlation — $-1 < r < 0$',
      'Perfect negative correlation — $r = -1$',
      'Zero (no) correlation — $r = 0$',
    ]},
    {'note': 'Interpretation: $|r|$ close to 1 → strong correlation; close to 0 → poor / '
             'non-existent. The same scale applies to Spearman\'s $R$.'},
    {'h3': 'A. Pearson\'s product-moment correlation coefficient'},
    {'p': 'Build the columns $x$, $y$, $xy$, $x^2$, $y^2$ and total each; $n$ = number of pairs.'},
    {'fbox': {'h': 'Pearson r — equivalent forms', 'rows': [
      {'lb': 'Deviation form',
       'tex': 'r = \\dfrac{\\sum (x - \\bar{x})(y - \\bar{y})}'
              '{\\sqrt{\\sum (x - \\bar{x})^2 \\; \\sum (y - \\bar{y})^2}}, \\quad '
              '\\bar{x} = \\tfrac{\\sum x}{n}, \\; \\bar{y} = \\tfrac{\\sum y}{n}'},
      {'lb': 'Covariance / variance form',
       'tex': 'r = \\dfrac{\\operatorname{Cov}(x, y)}{\\sqrt{\\operatorname{Var}(x)\\,'
              '\\operatorname{Var}(y)}}'},
      {'lb': 'Working (machine) form',
       'tex': 'r = \\dfrac{n\\sum xy - \\sum x \\sum y}'
              '{\\sqrt{\\left[n\\sum x^2 - (\\sum x)^2\\right]\\left[n\\sum y^2 - '
              '(\\sum y)^2\\right]}}'},
    ]}},
    {'note': 'Numerator $= n\\sum xy - \\sum x\\sum y$ is $n^2 \\times$ the covariance; each '
             'bracket in the denominator is $n^2 \\times$ a variance.'},
    {'h3': 'B. Spearman\'s rank correlation coefficient'},
    {'fbox': {'h': 'Spearman R', 'rows': [
      {'lb': 'Formula', 'tex': 'R = 1 - \\dfrac{6\\sum d^2}{n(n^2 - 1)}',
       'nt': '$d$ = difference in each pair of ranks $R_x - R_y$; $n$ = number of items ranked. '
             '$-1 \\le R \\le 1$.'},
      {'lb': 'Tied ranks', 'tex': '\\text{shared rank} = \\dfrac{\\text{sum of the positions '
              'the tied items occupy}}{\\text{number tied}}',
       'nt': 'e.g. two items in 2nd place each get $(2+3)/2 = 2.5$; three items in 6th place '
             'each get $(6+7+8)/3 = 7$.'},
    ]}},
    {'note': 'Rank in ascending **or** descending order — but use the *same* order for both '
             'variables. Spearman is easier to compute but less accurate than Pearson.'},
    {'h3': 'C. Simple linear regression — line of y on x'},
    {'p': 'Model: $\\;y = a + bx\\;$ where $a$ = intercept on the $y$-axis, $b$ = regression '
          'coefficient = slope / gradient.'},
    {'fbox': {'h': 'Least-squares regression of y on x', 'rows': [
      {'lb': 'Normal equations (from least squares)',
       'tex': '\\sum y = an + b\\sum x \\qquad\\text{and}\\qquad '
              '\\sum xy = a\\sum x + b\\sum x^2'},
      {'lb': 'Solve for the slope',
       'tex': 'b = \\dfrac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2}'},
      {'lb': 'then the intercept',
       'tex': 'a = \\dfrac{\\sum y}{n} - b\\,\\dfrac{\\sum x}{n} = \\bar{y} - b\\bar{x}'},
      {'lb': 'Graphical slope',
       'tex': 'b = \\dfrac{\\text{vertical length}}{\\text{horizontal length}} '
              '= \\dfrac{y_2 - y_1}{x_2 - x_1}',
       'nt': 'The fitted line always passes through $(\\bar{x}, \\bar{y})$.'},
    ]}},
    {'h3': 'D. Regression line of x on y'},
    {'p': 'Model: $\\;x = a\' + b\'y\\;$ (now $y$ is independent). **Different line** from y on '
          'x — not a rearrangement.'},
    {'fbox': {'h': 'Least-squares regression of x on y', 'rows': [
      {'lb': 'Slope',
       'tex': "b' = \\dfrac{n\\sum xy - \\sum x \\sum y}{n\\sum y^2 - (\\sum y)^2}"},
      {'lb': 'Intercept', 'tex': "a' = \\dfrac{\\sum x}{n} - b'\\,\\dfrac{\\sum y}{n} "
              "= \\bar{x} - b'\\bar{y}"},
    ]}},
    {'h3': 'E. Prediction and interpretation'},
    {'ul': [
      '**Predict $y$** from a given $x$: substitute $x$ into $y = a + bx$. Predict $x$ from $y$ '
      'using $x = a\' + b\'y$.',
      '$b = 0$ → line parallel to the $x$-axis (no linear relationship).',
      '$b > 0$ and large → steep, upward-sloping line.',
      '$b < 0$ → downward-sloping line.',
      '$r^2$ (or $R^2$) — square the correlation coefficient to get the proportion of variation '
      'explained.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': "Pearson's r — deviation form",
   'tex': 'r = \\frac{\\sum (x-\\bar{x})(y-\\bar{y})}{\\sqrt{\\sum (x-\\bar{x})^2 \\sum '
          '(y-\\bar{y})^2}}'},
  {'lb': "Pearson's r — covariance form",
   'tex': 'r = \\frac{\\operatorname{Cov}(x,y)}{\\sqrt{\\operatorname{Var}(x)\\operatorname{Var}(y)}}'},
  {'lb': "Pearson's r — working form",
   'tex': 'r = \\frac{n\\sum xy - \\sum x \\sum y}{\\sqrt{[n\\sum x^2 - (\\sum x)^2]'
          '[n\\sum y^2 - (\\sum y)^2]}}'},
  {'lb': "Spearman's rank correlation",
   'tex': 'R = 1 - \\frac{6\\sum d^2}{n(n^2 - 1)}, \\quad d = R_x - R_y'},
  {'lb': 'Tied rank', 'tex': '\\text{shared rank} = \\frac{\\text{sum of tied positions}}'
          '{\\text{number tied}}'},
  {'lb': 'Coefficient of determination', 'tex': 'r^2 \\text{ (or } R^2\\text{)}'},
  {'lb': 'Regression y on x — normal equations',
   'tex': '\\sum y = an + b\\sum x, \\qquad \\sum xy = a\\sum x + b\\sum x^2'},
  {'lb': 'Regression y on x — slope',
   'tex': 'b = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2}'},
  {'lb': 'Regression y on x — intercept',
   'tex': 'a = \\bar{y} - b\\bar{x} = \\frac{\\sum y}{n} - b\\frac{\\sum x}{n}'},
  {'lb': 'Regression x on y — slope',
   'tex': "b' = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum y^2 - (\\sum y)^2}"},
  {'lb': 'Regression x on y — intercept', 'tex': "a' = \\bar{x} - b'\\bar{y}"},
  {'lb': 'Graphical slope',
   'tex': 'b = \\frac{\\text{vertical length}}{\\text{horizontal length}} = '
          '\\frac{y_2 - y_1}{x_2 - x_1}'},
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
    'src': 'Chapter 4.2', 'sec': '4.2'},
   {'q': 'For the same data, the value of $a$ is',
    'o': ['6', '7', '8', '9', '10'],
    'a': 3,
    'w': 'The intercept is the mean of $y$ less $b$ times the mean of $x$.',
    'calc': 'a = 7 - (-1)(2) = 9',
    'src': 'Chapter 4.2', 'sec': '4.2'},
   {'q': 'In the regression line $y = a + bx$, $y$ is a/an ……… variable while $x$ is a/an ……… '
         'variable.',
    'o': ['constant, dependent', 'constant, independent', 'dependent, independent',
          'independent, dependent', 'dependent, constant'],
    'a': 2,
    'w': '$y$ is the variable being explained or predicted, so it is dependent; $x$ is the '
         'explanatory variable, so it is independent.',
    'src': 'Chapter 4.2', 'sec': '4.2'},
   {'q': 'Five items are ranked by two judges and $\\sum d^2 = 18$. Spearman\'s rank correlation '
         'coefficient is',
    'o': ['0.9', '0.1', '−0.1', '0.5', '0.82'],
    'a': 1,
    'w': 'Apply the rank correlation formula with $n = 5$.',
    'calc': 'r_s = 1 - \\frac{6(18)}{5(25-1)} = 1 - \\frac{108}{120} = 1 - 0.9 = 0.1',
    'src': 'Chapter 4.1', 'sec': '4.1'},
   {'q': 'A correlation coefficient of $-0.92$ indicates',
    'o': ['a weak relationship', 'no relationship',
          'a strong relationship in which $y$ falls as $x$ rises',
          'a strong relationship in which $y$ rises as $x$ rises',
          'that $x$ causes $y$ to fall'],
    'a': 2,
    'w': 'The magnitude 0.92 shows the relationship is strong; the negative sign shows it is '
         'inverse. It shows association only — it does not establish that $x$ causes anything.',
    'src': 'Chapter 4.1', 'sec': '4.1'},
   {'q': 'If $r = 0.8$, the percentage of the variation in $y$ explained by the variation in $x$ is',
    'o': ['80%', '64%', '89%', '20%', '36%'],
    'a': 1,
    'w': 'The coefficient of determination is $r^2$.',
    'calc': 'r^2 = 0.8^2 = 0.64 = 64\\%',
    'src': 'Chapter 4.1', 'sec': '4.1'},
   {'q': 'Which of the following indicates a very steep and upward sloping regression line?',
    'o': ['A gradient of 0.05', 'A gradient of −4.5', 'A gradient of 4.5', 'A gradient of 0',
          'A gradient of −0.05'],
    'a': 2,
    'w': 'Upward sloping means a positive gradient; steep means a large magnitude. A gradient of '
         '4.5 is both.',
    'src': 'Chapter 4.2', 'sec': '4.2'},
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
    'src': 'Chapter 4.1', 'sec': '4.1'},
  ]},
}
