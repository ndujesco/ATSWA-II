CH = {
 'n': 5,
 't': 'Time Series',
 'brief': 'Decomposing a series into trend, seasonal, cyclical and irregular components, fitting '
          'a trend by moving averages or least squares, and forecasting.',
 'outcomes': [
   'Identify the four components of a time series',
   'Distinguish the additive from the multiplicative model',
   'Compute a moving average trend, including a centred moving average',
   'Fit a trend line by the method of least squares and by semi-averages',
   'Compute and adjust seasonal indices and use them to forecast',
 ],
 'secs': [
  {'n': '5.1', 't': 'The four components', 'b': [
    {'table': {'head': ['Component', 'Symbol', 'Nature'], 'align': 'lll', 'rows': [
      ['**Trend** (secular)', '$T$', 'The long-term underlying direction of the series'],
      ['**Seasonal**', '$S$', 'Regular fluctuations within a year, of fixed period'],
      ['**Cyclical**', '$C$', 'Longer swings around the trend, typically 3–10 years, of no fixed period'],
      ['**Irregular** (random)', '$I$', 'Unpredictable, non-recurring — a strike, a flood, a policy shock'],
    ]}},
    {'fbox': {'h': 'The two models', 'rows': [
      {'lb': 'Additive model', 'tex': 'Y = T + S + C + I',
       'nt': 'Use where the seasonal swing is roughly constant in absolute size.'},
      {'lb': 'Multiplicative model', 'tex': 'Y = T \\times S \\times C \\times I',
       'nt': 'Use where the seasonal swing grows in proportion to the trend.'},
    ]}},
    {'key': 'Under the **additive** model seasonal variations are in the units of the data and '
            'must sum to **zero** over a full cycle. Under the **multiplicative** model they are '
            'ratios or index numbers and must average to **1** (or sum to 400 for four quarters, '
            '1,200 for twelve months).'},
    {'h3': 'Uses of time series analysis'},
    {'ul': [
      'To understand past behaviour and identify the underlying trend.',
      'To forecast future values for budgeting and planning.',
      'To compare the performance of one period against another after removing seasonal effects.',
      'To evaluate current performance against what the trend would have predicted.',
    ]},
  ]},

  {'n': '5.2', 't': 'The moving average trend', 'b': [
    {'p': 'A moving average smooths the series by averaging successive groups of observations. '
          'The **order** of the average is the number of periods in one full cycle: 4 for '
          'quarterly data, 12 for monthly, 7 for daily.'},
    {'tex': '\\text{MA}_k = \\frac{Y_1 + Y_2 + \\cdots + Y_k}{k}', 'tag': '(5.1)'},
    {'warn': 'Where the order is **even** (4 or 12), the average falls between two periods and '
             'must be **centred** by taking a further two-point average, so that the trend value '
             'lines up with an actual period. Where the order is **odd** (3, 5, 7), no centring '
             'is needed.'},
    {'eg': {'t': 'Three-point moving average', 'q': [
      {'p': 'Complete the moving average column.'},
      {'table': {'align': 'rrr',
        'head': ['Time $t$', 'Value $Y$', 'Moving average of order 3'], 'rows': [
        ['1', '15', ''], ['2', '20', '$p$'], ['3', '25', '$q$'], ['4', '36', ''],
        ['5', '42', '$r$'], ['6', '48', '$s$'],
      ]}}],
      'a': [
      {'p': 'A three-point moving average is centred on the middle of each group of three.'},
      {'tex': 'p = \\frac{15 + 20 + 25}{3} = \\frac{60}{3} = 20'},
      {'tex': 'q = \\frac{20 + 25 + 36}{3} = \\frac{81}{3} = 27'},
      {'tex': 'r = \\frac{25 + 36 + 42}{3} = \\frac{103}{3} = 34.33'},
      {'p': 'The next group would be centred at $t = 5$: $\\dfrac{36 + 42 + 48}{3} = 42$, so the '
            'value shown against $t=5$ is $r$ if the table is offset, and $s$ takes the value at '
            '$t=5$. Read the alignment of the table carefully — questions of this shape depend '
            'entirely on which row each average sits against.'},
      {'note': 'With an odd order the first and last $\\frac{k-1}{2}$ periods have no trend value. '
               'That is unavoidable and is one reason moving averages cannot forecast beyond the '
               'end of the data without further assumption.'}]}},
    {'eg': {'t': 'Centred four-quarter moving average', 'q': [
      {'p': 'Compute the centred moving average trend for the quarterly sales: '
            'Q1 80, Q2 95, Q3 130, Q4 105, Q1 88, Q2 104, Q3 142, Q4 114.'}],
      'a': [
      {'table': {'align': 'lrrr',
        'head': ['Quarter', 'Sales', '4-quarter total', 'Centred MA (trend)'], 'rows': [
        ['Y1 Q1', '80', '', ''],
        ['Y1 Q2', '95', '410', ''],
        ['Y1 Q3', '130', '418', '103.50'],
        ['Y1 Q4', '105', '427', '105.63'],
        ['Y2 Q1', '88', '439', '108.25'],
        ['Y2 Q2', '104', '448', '110.88'],
        ['Y2 Q3', '142', '', ''],
        ['Y2 Q4', '114', '', ''],
      ]}},
      {'p': 'Four-quarter totals: $80+95+130+105 = 410$; $95+130+105+88 = 418$; '
            '$130+105+88+104 = 427$; $105+88+104+142 = 439$; $88+104+142+114 = 448$.'},
      {'tex': '\\text{Centred MA at Y1 Q3} = \\frac{410 + 418}{2 \\times 4} = \\frac{828}{8} '
              '= 103.50'},
      {'tex': '\\text{Centred MA at Y1 Q4} = \\frac{418 + 427}{8} = \\frac{845}{8} = 105.63'},
      {'note': 'Dividing the sum of two four-quarter **totals** by 8 does the averaging and the '
               'centring in one step, which is faster and less error-prone than averaging then '
               'centring separately.'}]}},
  ]},

  {'n': '5.3', 't': 'Fitting a trend line', 'b': [
    {'h3': 'Method of least squares'},
    {'p': 'Fit $T = a + bt$ where $t$ is time coded as $1, 2, 3, \\ldots$ The formulas are exactly '
          'those of Chapter 4 with $t$ in place of $x$:'},
    {'tex': 'b = \\frac{n\\sum ty - \\sum t \\sum y}{n\\sum t^2 - (\\sum t)^2}, \\qquad '
            'a = \\bar{y} - b\\bar{t}'},
    {'note': 'Coding $t$ symmetrically about zero (…, −2, −1, 0, 1, 2, … for an odd number of '
             'periods, or …, −3, −1, 1, 3, … for an even number) makes $\\sum t = 0$, which '
             'collapses the formulas to $b = \\dfrac{\\sum ty}{\\sum t^2}$ and $a = \\bar{y}$. '
             'This saves a great deal of arithmetic.'},
    {'h3': 'Method of semi-averages'},
    {'steps': [
      'Split the series into two equal halves (dropping the middle value if the count is odd).',
      'Compute the mean of each half.',
      'Plot each mean against the mid-point of its half and join the two points.',
    ]},
    {'p': 'Quick but crude: it uses only two summary points and is distorted by extremes.'},
  ]},

  {'n': '5.4', 't': 'Seasonal variation and forecasting', 'b': [
    {'steps': [
      'Compute the trend $T$ (usually by centred moving average).',
      'Compute the deviation of each actual value from its trend: $Y - T$ for the additive model, '
      '$Y/T$ for the multiplicative model.',
      'Average those deviations for each season across all the years available.',
      '**Adjust** the averages so that they sum to zero (additive) or to the number of seasons '
      '(multiplicative), by spreading the discrepancy equally.',
      'Forecast: project the trend forward, then apply the seasonal factor.',
    ]},
    {'fbox': {'h': 'Deseasonalising and forecasting', 'rows': [
      {'lb': 'Seasonal variation, additive', 'tex': 'S = Y - T'},
      {'lb': 'Seasonal index, multiplicative', 'tex': 'S = \\frac{Y}{T} \\times 100'},
      {'lb': 'Deseasonalised (seasonally adjusted) value',
       'tex': 'Y_{\\text{adj}} = Y - S \\quad\\text{or}\\quad Y_{\\text{adj}} '
              '= \\frac{Y}{S} \\times 100'},
      {'lb': 'Forecast', 'tex': 'F = T + S \\quad\\text{or}\\quad F = T \\times \\frac{S}{100}'},
    ]}},
    {'eg': {'t': 'Adjusting seasonal variations and forecasting', 'q': [
      {'p': 'Unadjusted average seasonal variations under the additive model are: Q1 $-18$, '
            'Q2 $+4$, Q3 $+31$, Q4 $-13$. The trend line is $T = 96 + 3.2t$ with $t = 1$ at the '
            'first quarter of Year 1. Forecast sales for Q3 of Year 4.'}],
      'a': [
      {'h4': 'Step 1 — adjust the seasonals'},
      {'p': 'They currently sum to $-18 + 4 + 31 - 13 = +4$, but must sum to zero. Spread the '
            'excess of 4 equally, deducting $4 \\div 4 = 1$ from each:'},
      {'table': {'align': 'lrrr', 'head': ['Quarter', 'Unadjusted', 'Adjustment', 'Adjusted'],
        'rows': [
        ['Q1', '−18', '−1', '−19'], ['Q2', '+4', '−1', '+3'],
        ['Q3', '+31', '−1', '+30'], ['Q4', '−13', '−1', '−14'],
        ['Total', '+4', '−4', '0', '@tot'],
      ]}},
      {'h4': 'Step 2 — project the trend'},
      {'p': 'Q3 of Year 4 is the $(4-1)\\times 4 + 3 = 15$th quarter, so $t = 15$:'},
      {'tex': 'T = 96 + 3.2(15) = 96 + 48 = 144'},
      {'h4': 'Step 3 — apply the seasonal'},
      {'tex': 'F = T + S = 144 + 30 = 174'},
      {'p': 'The forecast for Q3 Year 4 is **174 units**.'},
      {'warn': 'Two things are examined here more than the arithmetic: the seasonals must be '
               '**adjusted to sum to zero** before use, and $t$ must be counted from the same '
               'origin the trend line was fitted from. Getting $t$ wrong by one quarter shifts '
               'the forecast by the whole value of $b$.'}]}},
    {'h3': 'Why deseasonalise?'},
    {'p': 'A seasonally adjusted series answers the question "is business really improving, or is '
          'it just December?" It strips out the regular seasonal pattern so that consecutive '
          'periods can be compared directly.'},
  ]},

  {'n': '5.5', 't': 'Worksheet summary — definitions and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§5.1 The four components** — trend $T$ (long-term direction), seasonal $S$ (fixed-'
      'period, within a year), cyclical $C$ (3–10-year swings, no fixed period), irregular $I$ '
      '(one-off shocks). **Additive** $Y=T+S+C+I$ for a roughly constant seasonal swing '
      '(seasonals sum to zero); **multiplicative** $Y=T\\times S\\times C\\times I$ for a '
      'swing that grows with the trend (seasonal indices average to 1, or sum to 400 for '
      'quarterly/1,200 for monthly data).',
      '**§5.2 The moving average trend** — order = periods in one cycle (4 quarterly, 12 '
      'monthly, 7 daily); **odd** order needs no centring, **even** order must be **centred** '
      'by a further two-point average (or, faster, by summing two consecutive n-period totals '
      'and dividing by $2n$) so the trend value lines up with a real period.',
      '**§5.3 Fitting a trend line** — **least squares** $T=a+bt$ uses the Chapter 4 formulas '
      'with $t$ in place of $x$; coding $t$ symmetrically about zero makes $\\sum t=0$ and '
      'collapses them to $b=\\sum ty/\\sum t^2$, $a=\\bar{y}$. **Semi-averages** (split the '
      'series in half, plot each half\'s mean against its mid-point, join them) is quick but '
      'crude, using only two summary points.',
      '**§5.4 Seasonal variation and forecasting** — find $T$ (usually centred MA), compute '
      'each period\'s deviation ($Y-T$ additive, $Y/T$ multiplicative), average by season '
      'across years, then **adjust** so the averages sum to zero (additive) or to the number '
      'of seasons (multiplicative) by spreading the discrepancy equally — this adjustment is '
      'compulsory before forecasting. Forecast = project the trend from the **same origin** '
      'the line was fitted from, then apply the adjusted seasonal factor. Deseasonalising '
      'strips the seasonal pattern out so consecutive periods can be compared directly.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Time series** — data collected successively at regular intervals (daily, weekly, '
      'monthly, quarterly, yearly).',
      '**Time-plot (historigram)** — graph of the series values against time.',
      '**Secular trend (T)** — the long-term underlying movement (upward, downward or flat); '
      'may be linear or non-linear.',
      '**Seasonal variation (S)** — a pattern that repeats within a period of **one year or '
      'less** (months, quarters).',
      '**Cyclical variation (C)** — a wave-like fluctuation about the trend recurring over '
      '**more than one year** (business cycles, typically 4–7 years); less predictable.',
      '**Irregular / random variation (I)** — residual variation from sporadic, unpredictable '
      'events (floods, strikes, wars); what is left after T, S and C.',
      '**Moving average** — a trend estimate obtained by averaging successive overlapping '
      'groups of values (smoothing).',
      '**Moving total** — the numerator of a moving average, written against the middle item.',
      '**Deseasonalised (seasonally adjusted) series** — the series with the seasonal component '
      'removed.',
    ]},
    {'h3': 'Time series models (name + formula)'},
    {'ul': [
      'Additive model — $Y = T + S + C + I$',
      'Multiplicative model — $Y = T \\times S \\times C \\times I$',
      'Exponential trend — $Y = ab^{x}$',
    ]},
    {'h3': 'A. Trend by moving average'},
    {'fbox': {'h': 'Moving average of order n', 'rows': [
      {'lb': 'General term',
       'tex': '\\text{MA}_k = \\dfrac{Y_k + Y_{k+1} + \\dots + Y_{k+n-1}}{n}',
       'nt': 'Written against the **middle** item of the n values.'},
      {'lb': 'Even order — centre with a second (2-point) moving total',
       'tex': 'T = \\dfrac{\\text{(1st } n\\text{-total)} + \\text{(2nd } n\\text{-total)}}{2n}',
       'nt': 'e.g. a 4-quarter series: pair consecutive 4-quarter totals, then divide by 8.'},
    ]}},
    {'note': 'Odd order (3, 5, 7): apply the general term directly. Even order (4, 12): take '
             'n-period moving totals, add them in overlapping pairs, then divide by $2n$ so the '
             'value sits against a real time point. Monthly data → order 12; quarterly → order 4.'},
    {'h3': 'B. Trend by least squares'},
    {'p': 'Take $x$ (or $t$) = the time period and $y$ = the series value, and fit $y = a + bx$.'},
    {'fbox': {'h': 'Least squares trend — direct', 'rows': [
      {'lb': 'Normal equations',
       'tex': '\\sum y = an + b\\sum x, \\qquad \\sum xy = a\\sum x + b\\sum x^2'},
      {'lb': 'Slope',
       'tex': 'b = \\dfrac{n\\sum xy - \\sum x \\sum y}{n\\sum x^2 - (\\sum x)^2}'},
      {'lb': 'Intercept', 'tex': 'a = \\bar{y} - b\\bar{x}'},
    ]}},
    {'fbox': {'h': 'Least squares trend — coded time (\\(\\sum t = 0\\))', 'rows': [
      {'lb': 'Coding', 'tex': 't_i = x_i - x_m',
       'nt': '$x_m$ = median of the time periods. Then $\\sum t = 0$.'},
      {'lb': 'Slope', 'tex': 'b = \\dfrac{\\sum ty}{\\sum t^2}'},
      {'lb': 'Intercept', 'tex': 'a = \\dfrac{\\sum y}{n} = \\bar{Y}'},
      {'lb': 'Trend', 'tex': 'T = a + bt'},
    ]}},
    {'h3': 'C. Exponential trend by least squares'},
    {'fbox': {'h': 'Fitting Y = ab^x', 'rows': [
      {'lb': 'Linearise', 'tex': '\\log Y = \\log a + x\\log b'},
      {'lb': 'Let $z = \\log Y$, $A = \\log a$, $B = \\log b$', 'tex': 'z = A + Bx'},
      {'lb': 'Normal equations',
       'tex': '\\sum z = nA + B\\sum x, \\qquad \\sum zx = A\\sum x + B\\sum x^2'},
      {'lb': 'Recover constants', 'tex': 'a = \\operatorname{antilog}(A), \\quad '
              'b = \\operatorname{antilog}(B)'},
    ]}},
    {'h3': 'D. Seasonal variation and seasonal index'},
    {'fbox': {'h': 'Seasonal component', 'rows': [
      {'lb': 'Additive model', 'tex': 'S = Y - T \\quad (\\text{assuming } C + I = 0)'},
      {'lb': 'Multiplicative model', 'tex': 'S = \\dfrac{Y}{T} \\quad (\\text{assuming } '
              'C \\times I = 1)'},
      {'lb': 'Seasonal index (S.I.)',
       'tex': '\\text{S.I. for a season} = \\text{average of that season\'s } S \\text{ values}'},
    ]}},
    {'fbox': {'h': 'Adjusting the seasonal indices', 'rows': [
      {'lb': 'Additive — indices must sum to 0',
       'tex': '\\text{adjustment} = \\dfrac{0 - \\sum \\text{S.I.}}{\\text{number of seasons}}, '
              '\\quad \\text{add to each S.I.}'},
      {'lb': 'Multiplicative — indices must sum to the number of seasons',
       'tex': '\\text{adjustment} = \\dfrac{k - \\sum \\text{S.I.}}{k}, \\quad '
              'k = \\text{number of seasons (4 quarterly, 2 half-yearly)}',
       'nt': 'If expressed as percentages the target sum is $100k$ (400 quarterly, 200 '
             'half-yearly).'},
    ]}},
    {'h3': 'E. Forecasting'},
    {'fbox': {'h': 'Forecast', 'rows': [
      {'lb': 'Additive', 'tex': 'F = T + S'},
      {'lb': 'Multiplicative', 'tex': 'F = T \\times S \\quad \\text{or} \\quad '
              'F = T \\times \\dfrac{\\text{S.I.}\\%}{100}'},
    ]}},
    {'note': 'Project the trend $T$ for the required future period using the fitted line (with '
             '$x$/$t$ counted from the same origin), then apply the **adjusted** seasonal index '
             'for that season.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Additive model', 'tex': 'Y = T + S + C + I'},
  {'lb': 'Multiplicative model', 'tex': 'Y = T \\times S \\times C \\times I'},
  {'lb': 'Exponential trend', 'tex': 'Y = ab^{x}'},
  {'lb': 'Moving average of order $n$',
   'tex': '\\text{MA} = \\frac{Y_k + Y_{k+1} + \\dots + Y_{k+n-1}}{n}'},
  {'lb': 'Centred even-order moving average',
   'tex': 'T = \\frac{(\\text{1st } n\\text{-total}) + (\\text{2nd } n\\text{-total})}{2n}'},
  {'lb': 'Trend by least squares — normal equations',
   'tex': '\\sum y = an + b\\sum x, \\quad \\sum xy = a\\sum x + b\\sum x^2'},
  {'lb': 'Trend by least squares — solved',
   'tex': 'b = \\frac{n\\sum xy - \\sum x\\sum y}{n\\sum x^2 - (\\sum x)^2}, \\quad '
          'a = \\bar{y} - b\\bar{x}'},
  {'lb': 'Trend by least squares — coded time ($\\sum t = 0$)',
   'tex': 't = x - x_m, \\quad b = \\frac{\\sum ty}{\\sum t^2}, \\quad a = \\bar{y}'},
  {'lb': 'Exponential trend — linearised',
   'tex': '\\log Y = \\log a + x\\log b; \\ \\ a = \\operatorname{antilog}A, \\ '
          'b = \\operatorname{antilog}B'},
  {'lb': 'Seasonal variation — additive', 'tex': 'S = Y - T'},
  {'lb': 'Seasonal variation — multiplicative', 'tex': 'S = \\frac{Y}{T}'},
  {'lb': 'Seasonal index adjustment — additive',
   'tex': '\\text{adj} = \\frac{0 - \\sum \\text{S.I.}}{k}'},
  {'lb': 'Seasonal index adjustment — multiplicative',
   'tex': '\\text{adj} = \\frac{k - \\sum \\text{S.I.}}{k}'},
  {'lb': 'Forecast', 'tex': 'F = T + S \\quad\\text{or}\\quad F = T \\times \\frac{\\text{S.I.}\\%}{100}'},
 ],
 'focus':
   'A very frequent Section B question — usually a centred four-quarter moving average, then '
   'seasonal variations, then a forecast — and worth the full marks because every step is '
   'mechanical. Section A tests single moving average values from a small table and asks which '
   'model is which. The two places marks are lost: forgetting to **centre** an even-order average, '
   'and forgetting to **adjust** the seasonals to sum to zero.',
 'errors': [
   'Failing to centre a four-quarter or twelve-month moving average.',
   'Using the unadjusted seasonal variations in a forecast.',
   'Counting $t$ from the wrong origin when projecting the trend.',
   'Applying an additive seasonal to a multiplicative model, or the reverse.',
   'Treating the cyclical component as having a fixed period. Only the seasonal component does.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'For the series 15, 20, 25, 36, 42, 48, the three-point moving average centred on the '
         'second value is',
    'o': ['20', '15', '27', '25', '18'],
    'a': 0,
    'w': 'Average the first three values; the result is centred on the middle one.',
    'calc': '\\frac{15 + 20 + 25}{3} = \\frac{60}{3} = 20',
    'src': 'Chapter 5.2', 'sec': '5.2'},
   {'q': 'For the same series, the three-point moving average centred on the third value is',
    'o': ['43', '36', '27', '14', '12'],
    'a': 2,
    'w': 'Average the second, third and fourth values.',
    'calc': '\\frac{20 + 25 + 36}{3} = \\frac{81}{3} = 27',
    'src': 'Chapter 5.2', 'sec': '5.2'},
   {'q': 'Under the additive model, the seasonal variations for four quarters must sum to',
    'o': ['zero', '100', '400', '1', 'the value of the trend'],
    'a': 0,
    'w': 'Additive seasonals are measured in the units of the data as deviations from trend, and '
         'over a complete cycle the deviations must cancel. Multiplicative indices sum to 400 for '
         'four quarters.',
    'src': 'Chapter 5.1', 'sec': '5.1'},
   {'q': 'A four-quarter moving average must be centred because',
    'o': ['the data is seasonal',
          'the average of an even number of periods falls between two periods',
          'the trend is non-linear', 'the seasonal indices do not sum to zero',
          'the irregular component is large'],
    'a': 1,
    'w': 'With an even order the average corresponds to a point midway between two actual '
         'periods. A further two-point average shifts it onto an actual period so that $Y-T$ can '
         'be computed.',
    'src': 'Chapter 5.2', 'sec': '5.2'},
   {'q': 'The trend line is $T = 96 + 3.2t$ and the adjusted seasonal for Q3 is $+30$. The '
         'forecast for $t = 15$ under the additive model is',
    'o': ['144', '174', '114', '4,320', '126'],
    'a': 1,
    'w': 'Project the trend, then add the adjusted seasonal variation.',
    'calc': 'T = 96 + 3.2(15) = 144; \\quad F = 144 + 30 = 174',
    'src': 'Chapter 5.4', 'sec': '5.4'},
   {'q': 'Which component of a time series has no fixed period?',
    'o': ['Trend', 'Seasonal', 'Cyclical', 'Irregular', 'Both cyclical and irregular'],
    'a': 4,
    'w': 'The seasonal component repeats over a fixed period, usually a year. Cyclical swings '
         'recur but at irregular intervals of several years, and the irregular component is by '
         'definition unpredictable.',
    'src': 'Chapter 5.1', 'sec': '5.1'},
  ],
  'theory': [
   {'q': 'Identify the FOUR components of a time series, and explain the difference between the '
         'additive and multiplicative models, stating when each is appropriate.',
    'marks': 8,
    'a': [
      {'h4': 'The components'},
      {'ol': [
        '**Trend ($T$)** — the long-term underlying movement of the series, upward, downward or '
        'flat, over a period of years.',
        '**Seasonal variation ($S$)** — regular, repeating fluctuations within a fixed period, '
        'usually a year: higher sales in December, lower output in the rainy season.',
        '**Cyclical variation ($C$)** — longer swings about the trend associated with the trade '
        'cycle, typically lasting several years and of no fixed length.',
        '**Irregular or random variation ($I$)** — the residual: unpredictable, non-recurring '
        'movements caused by strikes, floods, policy changes or one-off events.']},
      {'h4': 'The two models'},
      {'tex': '\\text{Additive: } Y = T + S + C + I \\qquad '
              '\\text{Multiplicative: } Y = T \\times S \\times C \\times I'},
      {'p': 'Under the **additive** model the components are measured in the units of the data '
            'and the seasonal effect is a fixed absolute amount — sales are always ₦2m above '
            'trend in December. The seasonal variations must sum to zero over a full cycle.'},
      {'p': 'Under the **multiplicative** model the components are ratios or index numbers and '
            'the seasonal effect is a fixed proportion — December sales are always 130% of trend. '
            'The seasonal indices must average to 1, or sum to 400 for four quarters.'},
      {'h4': 'Which to use'},
      {'p': 'Plot the data. If the seasonal swings stay roughly **constant in absolute size** as '
            'the trend rises, use the additive model. If they **grow in proportion** to the '
            'trend — the peaks getting taller as the series climbs — use the multiplicative '
            'model, which is the more usual case for a growing business.'}],
    'src': 'Chapter 5.1', 'sec': '5.1'},
  ]},
}
