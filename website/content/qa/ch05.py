CH = {
 'n': 5,
 't': 'Time Series',
 'brief': 'Decomposing a series into trend, seasonal, cyclical and irregular components; fitting a '
          'trend by moving averages, least squares or exponential smoothening; and computing '
          'seasonal indices to forecast.',
 'outcomes': [
   'Know the meaning of a time series',
   'Know the basic components of a time series',
   'Estimate the trend by the use of moving averages and least squares methods',
   'Estimate seasonal indices',
   'Determine the adjusted seasonal variation',
 ],
 'secs': [
  {'n': '5.1', 't': 'Introduction', 'b': [
    {'def': {'t': 'Time series', 'd': 'a set of data successively collected at regular intervals '
                  'of time — daily, weekly, monthly, quarterly or yearly.'}},
    {'p': 'Examples of time series data include:'},
    {'ul': [
      'monthly production of a company;', 'daily sales at a medical store;',
      'amount of annual rainfall over a period of time; and',
      'money deposited in a bank on various working days.',
    ]},
    {'p': 'Analysing a time series has the following benefits:'},
    {'ol': [
      'understanding the **past behaviour** of a variable, so as to determine the direction of '
      'periodic fluctuations and predict its future tendencies;',
      'determining the **impact of the various forces** influencing different variables, which '
      'facilitates their comparison; and',
      'knowing the **behaviour of the variables**, in order to iron out intra-year variations as '
      'control events.',
    ]},
  ]},

  {'n': '5.2', 't': "Time series and its applications", 'b': [
    {'p': 'Through time series analysis, organisations predict future trends, optimise their '
          'operations and generally make informed decisions. Application areas include:'},
    {'ol': [
      '**Sales and marketing** — forecasting demand, analysing customer behaviour, predicting '
      'sales.',
      '**Quality control** — detecting abnormalities, product-quality monitoring and prediction.',
      '**Transportation and traffic** — transportation planning, and prediction/optimisation of '
      'route and traffic flow.',
      '**Climate and weather** — climate modelling and weather forecasting.',
      '**Health care** — hospital-admission forecasting, disease-outbreak prediction and '
      'patient-outcome analysis.',
    ]},
  ]},

  {'n': '5.3', 't': 'Basic components of a time series', 'b': [
    {'p': 'The fluctuations observed in a time series from time to time are caused by four '
          'composite forces, constantly at work:'},
    {'table': {'head': ['Component', 'Symbol', 'Nature'], 'align': 'lll', 'rows': [
      ['**Secular Trend** (Secular Variation)', '$T$', 'The pattern of the series over time, '
       'which may be **linear** (values concentrated along a straight line on the time-plot) or '
       'non-linear'],
      ['**Seasonal Fluctuations** (Variation)', '$S$', 'A variation that repeatedly occurs '
       'during a corresponding month or period of successive years — an annual recurring event, '
       'e.g. the rainy season or Christmas sales'],
      ['**Cyclical Variation**', '$C$', 'A long-term oscillation or wave-like fluctuation about '
       'the trend line, similar to seasonal variation but recurring over **more than one year** '
       '— called business cycles (prosperity, recession/depression, recovery). Length varies '
       'between **4 and 7 years**, and is less predictable than the seasonal component'],
      ['**Irregular / Random Variation**', '$I$', 'Caused by sporadic, unpredictable events — '
       'floods, strikes, disasters, wars. It is the residual variation left after Trend, '
       'Seasonal and Cyclical variation are accounted for'],
    ]}},
    {'def': {'t': 'Time-plot (historigram)', 'd': 'the graph of time series values against '
                  'different time points — the first step in a time series analysis, showing the '
                  'pattern of the series\' movement.'}},
  ]},

  {'n': '5.4', 't': 'Time series models', 'b': [
    {'p': 'Analysing and interpreting time series data — investigating its components — is at '
          'times referred to as **decomposition** of a time series. Letting $Y$ represent the '
          'series and $T, S, C, I$ the components, there are two models:'},
    {'fbox': {'h': 'The two models', 'rows': [
      {'lb': 'Additive model', 'tex': 'Y = T + S + C + I', 'nt': 'Equation 5.1.'},
      {'lb': 'Multiplicative model', 'tex': 'Y = TSCI', 'nt': 'Equation 5.2.'},
    ]}},
    {'p': 'Most of the time, the data available can be used to estimate only the trend and the '
          'seasonal variation.'},
  ]},

  {'n': '5.5', 't': 'Methods of constructing the trend line', 'b': [
    {'p': 'This study text considers three methods of estimating the trend:'},
    {'ol': ['Moving Average method;', 'Least Squares method; and', 'Exponential Smoothening '
      '(exponential trend).']},

    {'h3': '(a) Moving Average method'},
    {'p': 'The trend is obtained by smoothing out the fluctuations. For a given time series '
          '$Y_1, Y_2, Y_3, \\ldots, Y_n$, moving averages of order $n$ are given by:'},
    {'tex': '\\frac{Y_1+Y_2+\\cdots+Y_n}{n}, \\ \\frac{Y_2+Y_3+\\cdots+Y_{n+1}}{n}, \\ '
            '\\frac{Y_3+Y_4+\\cdots+Y_{n+2}}{n}, \\ \\text{etc.}', 'tag': '(5.3)'},
    {'p': 'Each moving average is written against the **middle** item of the values considered; '
          'the numerators above are called the **moving totals**.'},
    {'steps': [
      'Determine the order to be used — odd or even.',
      'If **odd**, apply equation 5.3 directly to get the moving average.',
      'If **even**, first obtain the moving totals of order $n$, then obtain a **2-combined-n** '
      'moving total (pair consecutive $n$-totals) of those totals; divide by $2n$ to give the '
      'moving average. This is needed because, by convention, an M.A. must sit against the '
      '**middle** item of the values considered, and only pairing two totals achieves that when '
      'the order is even.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 5.2 — moving averages of order 3 and 4',
      'open': True, 'q': [
      {'p': 'Use the following table to determine (a) the moving average of order 3, and (b) '
            'the moving average of order 4.'},
      {'table': {'align': 'rrrrrrrrrrrr', 'head': ['Month', '1','2','3','4','5','6','7','8','9',
        '10','11','12'], 'rows': [['Sales', '14','24','42','19','29','38','43','58','48','43',
        '64','74']]}}],
      'a': [
      {'h4': '(a) 3-month moving average'},
      {'table': {'align': 'rrr', 'head': ['Month', 'Sales', '3-month M.A.'], 'rows': [
        ['1', '14', ''], ['2', '24', '26.67'], ['3', '42', '28.33'], ['4', '19', '30.00'],
        ['5', '29', '28.67'], ['6', '38', '36.67'], ['7', '43', '46.33'], ['8', '58', '49.67'],
        ['9', '48', '51.67'], ['10', '43', '60.33'], ['11', '64', ''], ['12', '74', ''],
      ]}},
      {'h4': '(b) 4-month moving average (centred)'},
      {'table': {'align': 'rrrr', 'head': ['Month', 'Sales', '2-of-4-month total', '4-month M.A. ($\\div 8$)'],
        'rows': [
        ['3', '42', '213', '26.63'], ['4', '19', '242', '30.25'], ['5', '29', '257', '31.13'],
        ['6', '38', '297', '37.13'], ['7', '43', '355', '44.38'], ['8', '58', '379', '47.38'],
        ['9', '48', '405', '50.63'], ['10', '43', '442', '55.25'],
      ]}}]}},
    {'h4': 'Merits and demerits of the Moving Average method'},
    {'ul': [
      '**Merit:** simple compared with the least squares method.',
      '**Merit:** the effect of cyclical fluctuations is completely removed if the period of the '
      'moving average equals the average period of the cycles.',
      '**Merit:** good for a time series that reveals a linear trend.',
      '**Demerit:** extreme values are always lost.',
      '**Demerit:** not suitable for forecasting.',
      '**Demerit:** not good for a non-linear trend.',
    ]},

    {'h3': '(b) Least Squares Method (L.S.M.)'},
    {'p': 'Fitting a linear regression of $y$ on $x$ gives $y = a + bx$. This extends to time '
          'series by taking the time period $t$ as $x$ and the series value as $y$:'},
    {'fbox': {'h': 'Trend line by L.S.M. — direct', 'rows': [
      {'lb': 'Trend', 'tex': 'y = a + bx', 'nt': 'Equation 5.4.'},
      {'lb': 'Slope', 'tex': 'b = \\frac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2}',
       'nt': 'Equation 5.5.'},
      {'lb': 'Intercept', 'tex': 'a = \\bar{y} - b\\bar{x}', 'nt': 'Equation 5.6.'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 5.3 — trend by L.S.M. (direct)', 'open': True,
      'q': [
      {'p': 'Fit the trend to the same twelve-month sales series by the least squares approach.'}],
      'a': [
      {'p': '$\\sum x=78$, $\\sum y=607$, $\\sum x^2=650$, $\\sum xy=3{,}693$, $n=12$.'},
      {'tex': 'b = \\frac{12(3{,}693) - 78(607)}{12(650) - 78^2} = '
              '\\frac{44{,}316 - 47{,}346}{7{,}800 - 6{,}084} = \\frac{-3{,}030}{1{,}716} '
              '= -1.7657'},
      {'tex': '\\bar{y} = \\frac{607}{12} = 50.5833, \\quad \\bar{x} = \\frac{78}{12} = 6.5'},
      {'tex': 'a = 50.5833 - (-1.7657)(6.5) = 62.0604'},
      {'p': 'Trend: $\\hat{Y} = 62.0604 - 1.7657x$.'}]}},
    {'p': 'Because a time series typically has many periods, the L.S.M. computation is usually '
          'reduced by **coding** the time variable. Let $t_i = x_i - x_m$, where $x_m$ is the '
          'median of $x_i$; this makes $\\sum t = 0$, and the normal equations collapse to:'},
    {'fbox': {'h': 'Trend line by L.S.M. — coded ($\\sum t = 0$)', 'rows': [
      {'lb': 'Slope', 'tex': 'b = \\frac{\\sum y_it_i}{\\sum t_i^2}', 'nt': 'Equation 5.7.'},
      {'lb': 'Intercept', 'tex': 'a = \\frac{\\sum y_i}{n} = \\bar{Y}', 'nt': 'Equation 5.8.'},
      {'lb': 'Trend', 'tex': 'T = a + bt'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 5.4 — trend by L.S.M. with coding', 'open': True,
      'q': [
      {'p': 'Use the Least Squares Method with coding to fit the trend to the quarterly data '
            'below.'},
      {'table': {'align': 'lrrrr', 'head': ['Year', 'Q1', 'Q2', 'Q3', 'Q4'], 'rows': [
        ['2000', '20', '40', '25', '45'], ['2001', '30', '50', '37', '60'],
        ['2002', '42', '60', '45', '65'],
      ]}}],
      'a': [
      {'p': 'With $x=0,\\ldots,11$ across the 12 quarters, the mean of $x$ is 5.5, so $t=x-5.5$. '
            '$\\sum y = 519$, $\\sum t^2 = 143$, $\\sum ty = 428.5$, $n = 12$.'},
      {'tex': 'b = \\frac{428.5}{143} = 2.9965, \\qquad \\bar{y} = \\frac{519}{12} = 43.25'},
      {'tex': 'a = \\bar{y} - bt \\cdot \\bar{t}\\big|_{\\bar t = 5.5\\text{(uncoded mean)}}'
              ' = 43.25 - 2.9965(5.5) = 26.7692'},
      {'p': 'So $y = 26.7692 + 2.9965(x-5.5) = 10.2884 + 2.9965x$.'}]}},
    {'h4': 'Merits and demerits of the Least Squares method'},
    {'ul': [
      '**Merit:** no extreme values are lost, unlike the moving average method.',
      '**Merit:** free from subjective error.',
      '**Merit:** can be used for forecasting.',
      '**Demerit:** requires more time for computation.',
    ]},

    {'h3': '(c) Exponential Trend (Exponential Smoothening)'},
    {'p': 'Where the trend shows an exponential function — $x$ and $y$ in arithmetic and '
          'geometric progressions respectively — the trend is fitted as:'},
    {'fbox': {'h': 'Fitting $Y = ab^x$', 'rows': [
      {'lb': 'Exponential trend', 'tex': 'Y = ab^x', 'nt': 'Equation 5.9.'},
      {'lb': 'Linearised (take logs)', 'tex': '\\log Y = \\log a + x\\log b', 'nt': 'Equation 5.10.'},
      {'lb': 'Let $z=\\log Y$, $A=\\log a$, $B=\\log b$', 'tex': 'z = A + Bx', 'nt': 'Equation 5.11.'},
      {'lb': 'Normal equations',
       'tex': '\\sum z = nA + B\\sum x, \\qquad \\sum zx = A\\sum x + B\\sum x^2',
       'nt': 'Equations 5.12–5.13. Solve for $A$, $B$; recover $a=\\text{antilog}(A)$, '
             '$b=\\text{antilog}(B)$.'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 5.5 — fitting an exponential trend', 'open': True,
      'q': [
      {'p': 'Fit an exponential trend $Y=ab^x$ to a country\'s census population (millions), '
            'using coded years $u=(x-1970)/10$.'},
      {'table': {'align': 'rrrrr', 'head': ['Year', '1950', '1960', '1970', '1980', '1990'],
        'rows': [['Population', '25.0', '26.1', '27.9', '31.9', '36.1']]}}],
      'a': [
      {'p': 'Let $v = \\log y$. With $u=(x-1970)/10$: $u=-2,-1,0,1,2$; '
            '$v=1.3979,1.4166,1.4456,1.5038,1.5575$; $\\sum u=0$, $\\sum v=7.3214$, '
            '$\\sum u^2=10$, $\\sum uv=0.4064$.'},
      {'tex': 'A = \\frac{\\sum v}{n} = \\frac{7.3214}{5} = 1.4643 \\Rightarrow '
              'a = \\text{antilog}(A) = 29.1259'},
      {'tex': 'B = \\frac{\\sum uv}{\\sum u^2} = \\frac{0.4064}{10} = 0.04064 \\Rightarrow '
              'b = \\text{antilog}(B) = 1.0981'},
      {'p': 'So $Y = 29.1259(1.0981)^{u}$, or equivalently $v = 1.4643 + 0.04064u$ gives the '
            'trend values for any $x$.'}]}},
  ]},

  {'n': '5.6', 't': 'Evaluation of seasonal indices and the adjusted seasonal variation', 'b': [
    {'p': 'Seasonal indices identify patterns that repeat in daily, weekly or yearly cycles. '
          'Estimating them uses the original series and the trend already obtained; the approach '
          'depends on which model (additive or multiplicative) is assumed.'},
    {'h4': 'Additive model — steps'},
    {'ol': [
      'Arrange the original time series $Y$ in a column.',
      'Place the trend $T$ in the next column.',
      'Obtain the seasonal variation $S$ in another column: $S = Y - T$ (assuming $C+I=0$).',
      'Obtain the average seasonal variation for each period/season across the years available '
      '— this is the **seasonal index (S.I.)**.',
      'Check whether the S.I. is **balanced** by summing them: the total should be zero.',
      'If not balanced, divide the difference (from zero) by the number of periods/seasons, and '
      'add to or subtract from each S.I. as the sign of the difference dictates, so the total '
      'becomes zero.',
    ]},
    {'h4': 'Multiplicative model — steps'},
    {'p': 'Steps (a) and (b) are the same as the additive model. Then:'},
    {'ol': [
      'Obtain $S$ in another column by **dividing** $Y$ by $T$ (assuming $CI=1$): $S = Y/T$.',
      'Average by season, as in the additive model, to get the S.I.',
      'Check balance: the total of the indices should equal the **number of periods/seasons** '
      '(4 for quarterly, 2 for half-yearly — or 400/200 if expressed as percentages).',
      'If not balanced, adjust as in the additive model, but against a target of 4 or 2 (or 400 '
      'or 200) instead of zero.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example 5.6 — trend and seasonal variation', 'open': True,
      'q': [
      {'p': 'A company secretary invests quarterly (₦\'000) over four years. Estimate the trend '
            'by least squares, then compute the seasonal variation (multiplicative model).'},
      {'table': {'align': 'lrrrr', 'head': ['Year', 'Q1', 'Q2', 'Q3', 'Q4'], 'rows': [
        ['2000', '15', '35', '40', '20'], ['2001', '25', '45', '55', '30'],
        ['2002', '37', '55', '60', '40'], ['2003', '47', '62', '72', '58'],
      ]}}],
      'a': [
      {'p': 'Coding $x = 0, 1, \\ldots, 15$ across the 16 quarters: $n=16$, $\\sum x=120$, '
            '$\\sum y=696$, $\\sum x^2=1{,}240$, $\\sum xy=6{,}119$.'},
      {'tex': 'b = \\frac{16(6{,}119) - 120(696)}{16(1{,}240) - 120^2} = '
              '\\frac{97{,}904 - 83{,}520}{19{,}840 - 14{,}400} = \\frac{14{,}384}{5{,}440} '
              '= 2.6441'},
      {'tex': '\\bar{y} = \\frac{696}{16} = 43.5, \\quad \\bar{x} = \\frac{120}{16} = 7.5 '
              '\\Rightarrow a = 43.5 - 2.6441(7.5) = 23.6692'},
      {'p': 'Trend: $T = 23.6692 + 2.6441x$. Seasonal variation $S = Y/T$ for each quarter is '
            'then averaged by season and adjusted to sum to 4:'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Q1', 'Q2', 'Q3', 'Q4'], 'rows': [
        ['Average S over 4 years', '0.7663', '1.2038', '1.2987', '0.7595'],
        ['Total = 4.0283, adjustment', '−0.007075', '−0.007075', '−0.007075', '−0.007075'],
        ['Adjusted seasonal index', '0.7592', '1.1967', '1.2916', '0.7524'],
      ]}}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 5.7 — forecasting with the adjusted index',
      'open': True, 'q': [
      {'p': 'Use the result of Example 5.6 to forecast the investment in the 3rd quarter of '
            '2004.'}],
      'a': [
      {'p': 'The 3rd quarter of 2004 is $x=18$ on the same coding.'},
      {'tex': 'T = 23.67 + 2.64(18) = 71.19'},
      {'p': 'The adjusted seasonal index for Q3 is 1.29.'},
      {'tex': 'Forecast = 71.19 \\times 1.29 = 91.84'}]}},
    {'p': 'Forecasting by the least squares line is done exactly as in regression analysis, '
          'except that the forecast figure is then adjusted using the appropriate seasonal '
          'index.'},
  ]},

  {'n': '5.7', 't': 'Worksheet summary — definitions and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§5.1–5.2 Introduction and applications** — a time series is data collected at regular '
      'intervals; analysing it reveals past behaviour, the impact of underlying forces, and '
      'supports control decisions. Applied in sales/marketing, quality control, transport, '
      'climate/weather and health care.',
      '**§5.3 Components** — trend $T$ (linear/non-linear long-run movement), seasonal $S$ '
      '(recurs within a year or less), cyclical $C$ (recurs over **4–7 years**, business '
      'cycles, less predictable), irregular $I$ (sporadic, unpredictable residual).',
      '**§5.4 Models** — additive $Y=T+S+C+I$; multiplicative $Y=TSCI$.',
      '**§5.5 Trend methods** — (a) **Moving average**: order $n$ = cycle length; odd order '
      'applies the formula directly, even order needs a 2-combined-$n$ total divided by $2n$ '
      'to centre it on a real period. (b) **Least squares**: $y=a+bx$, with time coded as '
      '$t=x-x_m$ (median) to make $\\sum t=0$ and simplify $b=\\sum ty/\\sum t^2$, '
      '$a=\\bar Y$. (c) **Exponential smoothening**: for $Y=ab^x$, linearise by taking logs, '
      'fit $z=A+Bx$ by least squares, then recover $a,b$ by antilog.',
      '**§5.6 Seasonal indices** — additive: $S=Y-T$, averaged by season, adjusted to sum to '
      'zero. Multiplicative: $S=Y/T$, averaged by season, adjusted to sum to the number of '
      'seasons (4 quarterly, 2 half-yearly, or 400/200 as percentages). Forecast by projecting '
      'the trend, then applying the adjusted seasonal index.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Time series** — data collected successively at regular intervals (daily, weekly, '
      'monthly, quarterly, yearly).',
      '**Time-plot (historigram)** — the graph of time series values against time.',
      '**Secular trend (T)** — the long-term underlying movement; linear or non-linear.',
      '**Seasonal variation (S)** — a pattern recurring within a year or less.',
      '**Cyclical variation (C)** — a wave-like fluctuation about the trend recurring over more '
      'than one year (4–7 years); a business cycle.',
      '**Irregular / random variation (I)** — residual variation from sporadic, unpredictable '
      'events.',
      '**Decomposition** — analysing/interpreting a time series into its T, S, C, I components.',
      '**Moving average / moving total** — a trend estimate from averaging (the numerator of '
      'which is the moving total), written against the middle item.',
    ]},
  ]},

  {'n': '5.8', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following is NOT a time series data? (A) Monthly production of a '
        'company  (B) Daily sales at a medicine store  (C) Expenditure at home  (D) Daily '
        'deposits in a bank  (E) Annual rainfall',
        'For monthly time series data, the order of the moving average is (A) 2  (B) 4  (C) 6  '
        '(D) 10  (E) 12',
        'Using the conventional symbol of time series components, which of the following is '
        'the additive model? (A) $P=T+C+I+S$  (B) $Y=T+S+C+I$  (C) $Y=TSCI$  (D) $P=TSCI$  '
        '(E) $Y=ab^x$',
        'Which of the following is NOT true of the moving average method? (A) The method is '
        'simple compared with Least Squares Method  (B) The effect of cyclical fluctuations is '
        'completely removed by the method  (C) The extreme values are always lost  (D) The '
        'method is suitable for forecasting  (E) It is not good for non-linear trend',
      ]},
      {'p': 'Use the following table (moving average of order 3) to answer questions 5–8.'},
      {'table': {'align': 'rrr', 'head': ['Time $t$', 'Value $Y$', 'M.A. of order 3'], 'rows': [
        ['1', '24', ''], ['2', '30', '$a$'], ['3', '25', '$b$'], ['4', '35', '$c$'],
        ['5', '33', '$d$'], ['6', '38', ''],
      ]}},
      {'ol': ['Find $a$.', 'Find $b$.', 'Find $c$.', 'Find $d$.']},
      {'p': 'Use the following (Trend by L.S.M. $Y=30+3t$, additive model) to answer 9 and 10.'},
      {'table': {'align': 'rrr', 'head': ['$t$', '$Y$', 'Seasonal variation'], 'rows': [
        ['1', '30', '$p$'], ['2', '32', ''], ['3', '37', '$q$'],
      ]}},
      {'ol': ['Find $p$.', 'Find $q$.']}],
      'a': [
      {'ol': [
        '**C** — expenditure at home is not a regular, collected time series.',
        '**E** — 12, since there are 12 months in a cycle.',
        '**B** — $Y=T+S+C+I$.',
        '**D** — the method is **not** suitable for forecasting (it loses the extreme values '
        'needed to project forward).',
      ]},
      {'tex': 'a = \\frac{24+30+25}{3} = 26.33 \\qquad b = \\frac{30+25+35}{3} = 30'},
      {'tex': 'c = \\frac{25+35+33}{3} = 31 \\qquad d = \\frac{35+33+38}{3} = 35.33'},
      {'tex': 'p = 30 - [30+3(1)] = -3 \\qquad q = 37 - [30+3(3)] = -2'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Additive model', 'tex': 'Y = T + S + C + I'},
  {'lb': 'Multiplicative model', 'tex': 'Y = TSCI'},
  {'lb': 'Moving average, order $n$', 'tex': '\\frac{Y_1+Y_2+\\cdots+Y_n}{n}'},
  {'lb': 'Centred (even-order) moving average',
   'tex': 'T = \\frac{(\\text{1st } n\\text{-total}) + (\\text{2nd } n\\text{-total})}{2n}'},
  {'lb': 'Trend by L.S.M. — direct',
   'tex': 'b = \\frac{n\\sum xy - \\sum x\\sum y}{n\\sum x^2 - (\\sum x)^2}, \\quad '
          'a = \\bar{y} - b\\bar{x}'},
  {'lb': 'Trend by L.S.M. — coded ($\\sum t = 0$)',
   'tex': 't = x - x_m, \\quad b = \\frac{\\sum ty}{\\sum t^2}, \\quad a = \\bar{Y}'},
  {'lb': 'Exponential trend', 'tex': 'Y = ab^x, \\quad \\log Y = \\log a + x\\log b'},
  {'lb': 'Seasonal variation — additive', 'tex': 'S = Y - T'},
  {'lb': 'Seasonal variation — multiplicative', 'tex': 'S = \\frac{Y}{T}'},
 ],
 'focus':
   'A very frequent Section B question — a moving-average or least-squares trend, then seasonal '
   'variation, then a forecast — worth full marks because every step is mechanical once the '
   'method is known. Section A tests single moving-average values from a small table, which model '
   'is which, and the merits/demerits of each trend method. The two places marks are lost: '
   'forgetting to **centre** an even-order moving average, and forgetting to **adjust** the '
   'seasonal indices so they sum correctly before forecasting.',
 'errors': [
   'Failing to centre a four-quarter or twelve-month moving average.',
   'Using the unadjusted seasonal indices in a forecast.',
   'Confusing the additive adjustment target (zero) with the multiplicative one (number of '
   'seasons, or 400/200 as a percentage).',
   'Treating the cyclical component as having a fixed period — only the seasonal component does.',
   'Believing the moving average method is suitable for forecasting — it is not; least squares '
   'is.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'For the series 14, 24, 42, 19, 29, the three-month moving average centred on the '
         'second value is',
    'o': ['26.67', '24.00', '28.33', '19.00', '30.00'],
    'a': 0,
    'w': 'Average the first three values; the result is centred on the middle one.',
    'calc': '\\frac{14+24+42}{3} = \\frac{80}{3} = 26.67',
    'src': 'Chapter 5.5', 'sec': '5.5'},
   {'q': 'The Moving Average method is unsuitable for forecasting mainly because',
    'o': ['it always overstates the trend', 'extreme values are lost in the smoothing process',
          'it cannot handle monthly data', 'it requires logarithms',
          'it needs the cyclical component to be known in advance'],
    'a': 1,
    'w': 'Averaging discards the extreme values that would be needed to extrapolate the series '
         'forward — the study text\'s own listed demerit.',
    'src': 'Chapter 5.5', 'sec': '5.5'},
   {'q': 'Under the multiplicative model, the seasonal indices for four quarters must sum to',
    'o': ['zero', '1', '4', '100', 'the value of the trend'],
    'a': 2,
    'w': 'Multiplicative indices are ratios averaging to 1 each, so four of them must sum to 4 '
         '(or 400 if expressed as percentages).',
    'src': 'Chapter 5.6', 'sec': '5.6'},
   {'q': 'A four-quarter moving average must be centred because', 'sec': '5.5',
    'o': ['the data is seasonal',
          'the average of an even number of periods falls between two actual periods',
          'the trend is exponential', 'the seasonal indices do not sum to zero',
          'the irregular component is large'],
    'a': 1,
    'w': 'With an even order the raw average corresponds to a point midway between two actual '
         'periods; pairing two consecutive n-totals and dividing by $2n$ shifts it onto a real '
         'period.',
    'src': 'Chapter 5.5'},
   {'q': 'Coding the time variable in the Least Squares Method, so that $\\sum t = 0$, is done '
         'by subtracting from each period its',
    'o': ['mean', 'median', 'mode', 'range', 'standard deviation'],
    'a': 1,
    'w': 'The study text codes $t_i = x_i - x_m$, where $x_m$ is the **median** of the time '
         'periods, which collapses the normal equations to $b=\\sum ty/\\sum t^2$.',
    'src': 'Chapter 5.5', 'sec': '5.5'},
  ],
  'theory': [
   {'q': 'Identify the FOUR components of a time series and explain the difference between the '
         'additive and multiplicative models.',
    'marks': 8,
    'a': [
      {'h4': 'The components'},
      {'ol': [
        '**Secular trend ($T$)** — the long-term underlying movement, linear or non-linear.',
        '**Seasonal variation ($S$)** — a pattern that repeats within a year or less, such as '
        'Christmas sales or the rainy season.',
        '**Cyclical variation ($C$)** — a wave-like fluctuation about the trend, similar to the '
        'seasonal component but recurring over more than one year (4–7 years); associated with '
        'business cycles of prosperity, recession and recovery. Less predictable than $S$.',
        '**Irregular / random variation ($I$)** — the residual: caused by sporadic events such '
        'as floods, strikes, disasters or wars, and not explained by $T$, $S$ or $C$.']},
      {'h4': 'The two models'},
      {'tex': '\\text{Additive: } Y = T + S + C + I \\qquad \\text{Multiplicative: } Y = TSCI'},
      {'p': 'Under the additive model the components combine by addition and the seasonal '
            'variations, being expressed in the units of the data, must sum to zero over a '
            'complete cycle. Under the multiplicative model the components combine by '
            'multiplication and the seasonal indices, being ratios, must average to 1 — so 4 '
            'quarterly indices sum to 4 (or 400 as percentages).'}],
    'src': 'Chapter 5.3', 'sec': '5.3'},
  ]},
}
