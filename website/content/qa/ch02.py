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
      {'warn': 'Use the lower **boundary** (29.5), not the lower limit (30). Here the classes '
               'have a 1-unit gap (10–19, 20–29, …) so the boundary is half a unit below the '
               'limit; if the classes had been written 10–20, 20–30, … the limit *would* be the '
               'boundary. §2.5 sets out exactly when the two differ.'}]}},
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

  {'n': '2.5', 't': 'Class limits vs class boundaries — get this right for the median and mode',
    'b': [
    {'p': 'The median, mode and quantile formulas for grouped data all begin with **$L$ = the '
          'lower class *boundary*** of the relevant class, and use **$c$ = the class *width* '
          'measured between boundaries**. Nearly every lost mark on these formulas comes from '
          'putting the **stated lower limit** in for $L$, or the **apparent width** in for $c$. '
          'The two look interchangeable in some questions and are not in others — here is why, '
          'and how to be safe every time.'},
    {'fbox': {'h': 'The rule', 'rows': [
      {'lb': 'In the median / mode / $Q$ / $D$ / $P$ formula',
       'tex': 'L = \\text{lower class \\textbf{boundary}}, \\qquad c = \\text{upper boundary} '
              '- \\text{lower boundary}'},
      {'lb': 'Lower boundary of a class',
       'tex': 'L = \\frac{\\text{lower limit of this class} + \\text{upper limit of the '
              'previous class}}{2}',
       'nt': 'Equivalently: lower limit − ½(gap to the previous class). The lower boundary of a '
             'class is the upper boundary of the class before it.'},
    ]}},
    {'h3': 'Why it seems "interchangeable"'},
    {'table': {'cap': 'Same frequencies, two ways of writing the classes', 'align': 'llll',
      'head': ['Classes as written', 'Gap between classes', 'Lower boundary of "the third class"',
               'Does $L$ = lower limit?'], 'rows': [
      ['**Continuous:** 0–10, 10–20, 20–30, …', 'none', '20 (same as the lower limit)',
       '**Yes** — safe to use the limit'],
      ['**Continuous:** 2–4, 4–6, 6–8, …', 'none', '6 (same as the lower limit)',
       '**Yes** — safe to use the limit'],
      ['**Gapped:** 1–10, 11–20, 21–30, …', '1 unit', '$(10+11)/2 = 20.5$',
       '**No** — limit 21 is wrong; use 20.5'],
      ['**Gapped:** 2–4, 5–7, 8–10, …', '1 unit', '$(7+8)/2 = 7.5$',
       '**No** — limit 8 is wrong; use 7.5'],
    ]}},
    {'key': 'When classes are written **continuously** (no gap — 0–10, 10–20 or 2–4, 4–6), the '
            'lower **limit already equals** the lower boundary, so students who "use the limit" '
            'still get the right answer and never notice the distinction. The moment the classes '
            'have a **gap** (1–10, 11–20 or 2–4, 5–7), the boundary sits **halfway across the '
            'gap** and using the stated limit throws every answer out by **half the gap** '
            '(0.5 for the usual 1-unit gap). The class **width $c$** is affected too: for gapped '
            'classes like 5–7, 8–10 the width is $10.5 - 7.5 = 3$, **not** $10 - 8 = 2$.'},
    {'note': 'The **mean is not affected** by this at all. The class mark it uses is '
             '$\\frac{\\text{lower limit} + \\text{upper limit}}{2}$, which is identical to '
             '$\\frac{\\text{lower boundary} + \\text{upper boundary}}{2}$ — the two half-unit '
             'shifts cancel. So limits-vs-boundaries only ever bites on the **median, mode and '
             'quantiles**.'},
    {'h3': 'Worked contrast'},
    {'eg': {'t': 'The same data, continuous vs gapped', 'open': True, 'q': [
      {'p': 'A distribution has frequencies **3, 4, 6, 7, 2** across five equal classes. Find '
            'the mode by formula when the classes are written (a) continuously as 2–4, 4–6, 6–8, '
            '8–10, 10–12, and (b) with a 1-unit gap as 2–4, 5–7, 8–10, 11–13, 14–16.'}],
      'a': [
      {'p': 'Modal class is the fourth one either way ($f = 7$). $\\Delta_1 = 7 - 6 = 1$, '
            '$\\Delta_2 = 7 - 2 = 5$.'},
      {'h4': '(a) Continuous — lower limit = lower boundary'},
      {'p': '$L = 8$, $c = 2$ (both boundary-to-boundary):'},
      {'tex': '\\text{Mode} = 8 + \\left(\\frac{1}{1+5}\\right)(2) = 8 + 0.33 = 8.33'},
      {'h4': '(b) Gapped — lower boundary is 7.5, not 8'},
      {'p': 'Boundaries of the fourth class (8–10) are $7.5$ and $10.5$, so $L = 7.5$ and '
            '$c = 10.5 - 7.5 = 3$:'},
      {'tex': '\\text{Mode} = 7.5 + \\left(\\frac{1}{1+5}\\right)(3) = 7.5 + 0.5 = 8.0'},
      {'note': 'Different class *labels* for the same data legitimately give slightly different '
               'formula answers, because the interval is genuinely 2 wide in (a) and 3 wide in '
               '(b). What is **not** allowed is mixing them — using $L = 8$ with $c = 3$, or '
               '$L = 8.5$ with anything.'}]}},
    {'h3': 'Notes on the study text\'s worked examples'},
    {'ul': [
      '**Examples 2.5–2.9 (mean)** use continuous classes (0–10, 10–20, …) so class mark = '
      'lower limit + 5; boundaries never arise. Example 2.6 uses gapped classes (1–10, 11–20, '
      '…) and correctly takes the class mark as $(1+10)/2 = 5.5$, $(11+20)/2 = 15.5$, … — '
      'limits averaged, which is right for the mean.',
      '**Example 2.17 (mode & median by formula, continuous classes 2–4, 4–6, 6–8, 8–10, '
      '10–12)** — correctly uses $L_{mo} = 8$, $L_{me} = 6$, $c = 2$, giving Mode = 8.33 and '
      'Median = 7.33. Correct, because the classes touch.',
      '**Example 2.18 (gapped classes)** — the study text writes the modal/median class as '
      '"8–10" and then uses **$L = 8.5$**. That is wrong: the lower boundary of the class 8–10 '
      '(neighbours 5–7 and 11–13) is **$7.5$**. With the correct $L = 7.5$ and $c = 3$: '
      'Mode $= 7.5 + (2/6)\\times 3 = 8.5$ and Median $= 7.5 + \\frac{10-7}{6}\\times 3 = 9.0$ '
      '— which agree with the graphical answers the study text itself gets for the same-shaped '
      'data ($\\approx 8.5$ and $\\approx 9.0$). The printed formula answers (Mode 9.5, Median '
      '10) are each **exactly 1.0 too high**, the size of the mistake in $L$ ($8.5 - 7.5$).',
      '**Example 2.19 (quartiles etc., gapped classes 0–2, 3–5, 6–8, 9–11, 12–14)** — this one '
      'is done **correctly**: $L_1 = 2.5$ for class 3–5, $L_7 = 5.5$ for class 6–8, '
      '$L_{20} = 2.5$, all proper lower boundaries, with $c = 3$. Use this example as your '
      'model, not Example 2.18.',
    ]},
  ]},

  {'n': '2.6', 't': 'Easy-to-miss points, and end-of-chapter questions', 'b': [
    {'h3': 'Points that quietly lose marks'},
    {'ul': [
      '**Locating the median/quantile class** — scan the **cumulative** frequency column for '
      'the first value that reaches $N/2$ (or $kN/4$, $kN/10$, $kN/100$). Do **not** pick the '
      'class with the largest frequency — that is the *modal* class.',
      '**Position formula differs by data type** — ungrouped median position is '
      '$\\frac{n+1}{2}$; grouped median position is $\\frac{N}{2}$ (no "+1"). Quartiles/'
      'deciles/percentiles for grouped data use $\\frac{kN}{4}$, $\\frac{kN}{10}$, '
      '$\\frac{kN}{100}$ — using $\\frac{N}{2}$ to find a quartile is a common slip.',
      '**$\\Delta_1$ and $\\Delta_2$ are *differences*** — modal frequency minus the '
      'frequency before, and minus the frequency after — not the neighbouring frequencies '
      'themselves.',
      '**$\\sum f_{me}$ in the median formula is the cumulative frequency of all classes '
      '*before* the median class**, not including it.',
      '**Multiply the whole bracket by $c$** — in the step-deviation mean and in every '
      'median/mode/quantile formula, $c$ multiplies the entire correction term, not just part '
      'of it.',
      '**Assumed-mean and step-deviation methods are exact**, not approximations — they give '
      'the identical answer to the direct method (Examples 2.7–2.9 all return 8.9 bags / 21.75 '
      'years).',
      '**Units** — the mean, median and mode carry the **same unit as the data** (bags, litres, '
      'years, kg).',
      '**A mean can be an "impossible" value** — Example 2.3 gives 2.6061 students. That is a '
      'recognised shortcoming of the mean, not an error.',
      '**Even $n$, ungrouped median** — average the two middle values (Example 2.12: 6.5th '
      'position → mean of the 6th and 7th values $= (3+4)/2 = 3.5$).',
      '**Empirical (skewness) relationship** — $\\text{Mean} - \\text{Mode} = 3(\\text{Mean} - '
      '\\text{Median})$, i.e. $\\text{Mode} = 3\\,\\text{Median} - 2\\,\\text{Mean}$. Holds '
      'approximately for a moderately skewed distribution.',
      '**Skew direction** — right- (positively) skewed: $\\text{Mean} > \\text{Median} > '
      '\\text{Mode}$; left- (negatively) skewed: $\\text{Mean} < \\text{Median} < '
      '\\text{Mode}$; symmetrical/normal: all three coincide.',
      '**Which graph gives which** — the **mode** is estimated from a **histogram** (diagonals '
      'across the modal bar); the **median, quartiles, deciles and percentiles** are estimated '
      'from an **ogive**. An ogive cannot give the mode.',
      '**$Q_2 = D_5 = P_{50} = $ the median**; $Q_1 = P_{25}$, $Q_3 = P_{75}$, $D_k = P_{10k}$.',
      '**$HM < GM < \\bar{x}$** for positive values that are not all equal; equal only when '
      'every value is the same.',
      '**"Measures of location" = "measures of central tendency" = "measures of centre"**, and '
      'the study text also lumps the **measures of partition** (quantiles) under the same '
      'heading even though a quartile is not a measure of *central* tendency.',
    ]},
    {'h3': 'End-of-chapter questions (study text)'},
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'The mean of 2, 4, 6, 8, 10 is (A) 4  (B) 5  (C) 6  (D) 7  (E) 8',
        'Which of the following is **not** a measure of central tendency? (A) mean  (B) mode  '
        '(C) median  (D) decile  (E) 2nd quartile',
        'Which of the following is **not** a measure of partition? (A) median  (B) mode  '
        '(C) percentile  (D) quantiles  (E) deciles',
        'Which formula is used to compute a quartile? '
        '(A) $L_1 + \\frac{\\frac{N}{2} - \\sum f_1}{f_1}\\,c$  '
        '(B) $L_1 + \\frac{\\frac{3N}{4} - \\sum f_1}{f_1}\\,c$  '
        '(C) $L_1 + \\frac{\\frac{N}{4} - \\sum f_1}{f_1}\\,c$  '
        '(D) $L_1 + \\frac{\\frac{N}{10} - \\sum f_1}{f_1}\\,c$  '
        '(E) $L_1 + \\frac{\\frac{N}{100} - \\sum f_1}{f_1}\\,c$',
        'In the graphical method of obtaining the quartiles, which diagram is used? (A) bar '
        'chart  (B) histogram  (C) pie chart  (D) ogive  (E) component bar chart',
        'For the data 6, 3, 8, 8, 5 — calculate the arithmetic mean.',
        'For the same data, determine the median.',
        'For the same data, determine the mode.',
        'Find the sum of the mode and the mean.',
        'Find the difference between the median and the mean.',
      ]}],
      'a': [
      {'ol': [
        '**C — 6.** $\\frac{2+4+6+8+10}{5} = \\frac{30}{5} = 6$.',
        '**D — decile.** A decile is a measure of *partition*, not of central tendency. (The '
        '2nd quartile is the median, which *is* a central measure.)',
        '**B — mode.** The mode is a measure of central tendency; the quartiles, deciles and '
        'percentiles (collectively *quantiles*) are the measures of partition. The median is '
        'both.',
        '**C** — a quartile uses $\\frac{kN}{4}$ in the numerator; here $Q_1$ uses '
        '$\\frac{N}{4}$.',
        '**D — ogive.** Quartiles, like the median, are read from the cumulative frequency '
        'curve.',
        '**Mean = 6.** $\\frac{6+3+8+8+5}{5} = \\frac{30}{5} = 6$.',
        '**Median = 6.** Ordered: 3, 5, **6**, 8, 8.',
        '**Mode = 8** (occurs twice).',
        '**14.** Mode 8 + Mean 6.',
        '**0.** Median 6 − Mean 6.'],
      }]}},
  ]},

  {'n': '2.7', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§2.1 The arithmetic mean** — ungrouped $\\bar{x}=\\sum x/n$; grouped $\\sum fx/\\sum '
      'f$; assumed-mean $\\bar{x}=A+\\sum fd/\\sum f$ ($d=x-A$); step-deviation '
      '$\\bar{x}=A+(\\sum fu/\\sum f)c$ ($u=(x-A)/c$) — all three give the identical answer, '
      'step-deviation just keeps the arithmetic in small integers. Other means: geometric '
      '$GM=\\sqrt[n]{\\prod x_i}$ (growth rates, index numbers), harmonic $HM=n/\\sum(1/x_i)$ '
      '(rates like speed); for positive unequal values $HM<GM<\\bar{x}$.',
      '**§2.2 The median** — the middle value; ungrouped odd-$n$ position $(n+1)/2$, even-$n$ '
      'average the two middle values; grouped $L+((N/2-CF)/f_m)\\,c$ using the lower '
      '**boundary** and the cumulative frequency **before** the median class. Unaffected by '
      'extreme values, unlike the mean.',
      '**§2.3 The mode** — the most frequent value; grouped '
      '$L+(\\Delta_1/(\\Delta_1+\\Delta_2))\\,c$ where $\\Delta_1,\\Delta_2$ are the modal '
      'frequency\'s **excess** over the classes before/after (not the neighbouring frequencies '
      'themselves). Empirical relationship: $\\text{Mean}-\\text{Mode}='
      '3(\\text{Mean}-\\text{Median})$, used to find any one of the three from the other two '
      'in a moderately skewed distribution. Mean is best for further algebra but distorted by '
      'extremes; median survives extremes and open-ended classes; mode suits qualitative data '
      'but may not exist or be unique.',
      '**§2.4 Measures of partition** — one formula family for quartiles/deciles/percentiles, '
      'only the fraction of $N$ changes ($kN/4$, $kN/10$, $kN/100$); identities '
      '$Q_2=D_5=P_{50}=$ median, $Q_1=P_{25}$, $Q_3=P_{75}$, $D_k=P_{10k}$. Read from an '
      '**ogive** by tracing the required cumulative frequency across to the curve then down — '
      'an ogive gives every positional measure **except the mode**.',
      '**§2.5 Class limits vs boundaries** — the median/mode/quantile formulas always need $L$ '
      '= the lower class **boundary** and $c$ = boundary-to-boundary width, never the stated '
      'limit or apparent width. For **continuous** classes (0–10, 10–20, …) the limit already '
      'equals the boundary so the distinction is invisible; for **gapped** classes (1–10, '
      '11–20, …) the boundary sits half the gap above the limit and using the limit throws the '
      'answer out. The **mean** is never affected (its class mark cancels the shift). The '
      'study text\'s own Example 2.18 gets this wrong (uses $L=8.5$ instead of the correct '
      '$7.5$); Examples 2.17 and 2.19 get it right and are the ones to model.',
      '**§2.6 Easy-to-miss points** — locate the median/quantile class from the **cumulative** '
      'column, not the largest frequency (that finds the modal class instead); grouped median '
      'position is $N/2$ with **no** "+1"; $c$ multiplies the **whole** correction bracket; '
      'assumed-mean/step-deviation are exact, not approximations; a mean may be a value that '
      'cannot literally occur (e.g. 2.6 students) — that is a known shortcoming, not an error.',
    ]},
    {'h3': 'Definitions'},
    {'ul': [
      '**Measures of location (central tendency)** — a single value taken as representative '
      'of a whole set of data: the **mean**, **median** and **mode**.',
      '**Arithmetic mean** — the sum of all the values divided by how many there are.',
      '**Geometric mean** — the $n$th root of the product of $n$ values; used for average '
      'rates of growth and for index numbers.',
      '**Harmonic mean** — the number of values divided by the sum of their reciprocals; '
      'used for averaging rates such as speed over equal distances.',
      '**Median** — the value of the middle item when the data is arranged in order of '
      'magnitude; unaffected by extreme values.',
      '**Mode** — the most frequently occurring value; a distribution may have no mode '
      '(non-modal), one (unimodal), two (bimodal) or more.',
      '**Measures of partition** — values that divide an ordered distribution into equal '
      'parts: **quartiles** (four parts), **deciles** (ten parts), **percentiles** (a '
      'hundred parts). The study text groups these under "measures of location" too, even '
      'though a quartile is not itself a measure of *central* tendency.',
      '**Class boundary** — the true limit of a class, halfway between its stated limit and '
      'the stated limit of the neighbouring class; equal to the stated limit only when '
      'classes are written continuously (no gap), e.g. 0–10, 10–20.',
      '**Empirical relationship** — an approximate link between the mean, median and mode '
      'for a moderately skewed distribution.',
    ]},
    {'h3': 'The arithmetic mean'},
    {'fbox': {'h': 'Arithmetic mean', 'rows': [
      {'lb': 'Ungrouped data', 'tex': '\\bar{x} = \\frac{\\sum x}{n}'},
      {'lb': 'Grouped or weighted data',
       'tex': '\\bar{x} = \\frac{\\sum fx}{\\sum f}',
       'nt': '$x$ is the class mark (mid-point) for grouped data.'},
      {'lb': 'Assumed mean (coding) method — step 1: choose $A$, form $d$',
       'tex': 'd = x - A'},
      {'lb': 'Assumed mean method — step 2: the mean',
       'tex': '\\bar{x} = A + \\frac{\\sum fd}{\\sum f}'},
      {'lb': 'Step deviation method — step 1: choose $A$ and $c$, form $u$',
       'tex': 'u = \\frac{x - A}{c}'},
      {'lb': 'Step deviation method — step 2: the mean',
       'tex': '\\bar{x} = A + \\left(\\frac{\\sum fu}{\\sum f}\\right) c',
       'nt': '$c$ is the common class width; all three methods give the identical answer.'},
    ]}},
    {'h3': 'Other means'},
    {'fbox': {'h': 'Geometric and harmonic means', 'rows': [
      {'lb': 'Geometric mean',
       'tex': 'GM = \\sqrt[n]{x_1 x_2 \\cdots x_n} = \\left(\\prod_{i=1}^{n} x_i\\right)^{1/n}'},
      {'lb': 'Harmonic mean', 'tex': 'HM = \\frac{n}{\\sum \\frac{1}{x_i}}'},
    ]}},
    {'key': 'For any set of positive numbers not all equal: $HM < GM < \\bar{x}$.'},
    {'h3': 'The median'},
    {'fbox': {'h': 'Median', 'rows': [
      {'lb': 'Ungrouped, $n$ odd', 'tex': '\\text{Median} = x_{\\left(\\frac{n+1}{2}\\right)}'},
      {'lb': 'Ungrouped, $n$ even',
       'tex': '\\text{Median} = \\frac{x_{(n/2)} + x_{(n/2 + 1)}}{2}'},
      {'lb': 'Grouped data — step 1: locate the median class',
       'tex': '\\text{first class where cumulative } f \\ge \\frac{N}{2}'},
      {'lb': 'Grouped data — step 2: the median',
       'tex': '\\text{Median} = L + \\left(\\frac{\\frac{N}{2} - CF}{f_m}\\right) c',
       'nt': '$L$ = lower **boundary** of the median class; $CF$ = cumulative frequency '
             'before it; $f_m$ = its frequency; $c$ = its width; $N = \\sum f$.'},
    ]}},
    {'h3': 'The mode'},
    {'fbox': {'h': 'Mode', 'rows': [
      {'lb': 'Step 1: locate the modal class', 'tex': '\\text{the class with the highest } f'},
      {'lb': 'Step 2: form the differences',
       'tex': '\\Delta_1 = f_{mo} - f_{\\text{before}}, \\qquad '
              '\\Delta_2 = f_{mo} - f_{\\text{after}}'},
      {'lb': 'Step 3: the mode',
       'tex': '\\text{Mode} = L + \\left(\\frac{\\Delta_1}{\\Delta_1 + \\Delta_2}\\right) c',
       'nt': '$L$ = lower **boundary** of the modal class; $c$ = its width.'},
    ]}},
    {'h3': 'The empirical relationship'},
    {'fbox': {'h': 'Mean, median and mode', 'rows': [
      {'lb': 'Stated as a difference',
       'tex': '\\text{Mean} - \\text{Mode} = 3(\\text{Mean} - \\text{Median})'},
      {'lb': 'Rearranged for the mode',
       'tex': '\\text{Mode} = 3\\,\\text{Median} - 2\\,\\text{Mean}'},
    ]}},
    {'h3': 'Measures of partition — quartiles, deciles, percentiles'},
    {'fbox': {'h': 'Quantiles for grouped data — one formula, three fractions of $N$', 'rows': [
      {'lb': 'Quartile $k$ ($k = 1, 2, 3$)',
       'tex': 'Q_k = L + \\left(\\frac{\\frac{kN}{4} - CF}{f_q}\\right) c'},
      {'lb': 'Decile $k$ ($k = 1, \\ldots, 9$)',
       'tex': 'D_k = L + \\left(\\frac{\\frac{kN}{10} - CF}{f_d}\\right) c'},
      {'lb': 'Percentile $k$ ($k = 1, \\ldots, 99$)',
       'tex': 'P_k = L + \\left(\\frac{\\frac{kN}{100} - CF}{f_p}\\right) c'},
    ]}},
    {'key': 'Identities worth memorising: $Q_2 = D_5 = P_{50} = $ the median; $Q_1 = P_{25}$; '
            '$Q_3 = P_{75}$; $D_k = P_{10k}$.'},
    {'h3': 'Class boundary — the rule for $L$ and $c$'},
    {'fbox': {'h': 'Only matters for the median, mode and quantiles — never the mean', 'rows': [
      {'lb': 'In every median / mode / $Q$ / $D$ / $P$ formula',
       'tex': 'L = \\text{lower class \\textbf{boundary}}, \\qquad '
              'c = \\text{upper boundary} - \\text{lower boundary}'},
      {'lb': 'Lower boundary of a class',
       'tex': 'L = \\frac{\\text{lower limit of this class} + \\text{upper limit of the '
              'previous class}}{2}'},
    ]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Arithmetic mean, ungrouped', 'tex': '\\bar{x} = \\frac{\\sum x}{n}'},
  {'lb': 'Arithmetic mean, grouped', 'tex': '\\bar{x} = \\frac{\\sum fx}{\\sum f}'},
  {'lb': 'Assumed mean method',
   'tex': '\\bar{x} = A + \\frac{\\sum fd}{\\sum f}, \\quad d = x - A'},
  {'lb': 'Step deviation method',
   'tex': '\\bar{x} = A + \\left(\\frac{\\sum fu}{\\sum f}\\right) c, '
          '\\quad u = \\frac{x - A}{c}'},
  {'lb': 'Geometric mean', 'tex': 'GM = \\sqrt[n]{x_1 x_2 \\cdots x_n}'},
  {'lb': 'Harmonic mean', 'tex': 'HM = \\frac{n}{\\sum \\frac{1}{x}}'},
  {'lb': 'Median, ungrouped ($n$ odd)',
   'tex': '\\text{Median} = x_{\\left(\\frac{n+1}{2}\\right)}'},
  {'lb': 'Median, ungrouped ($n$ even)',
   'tex': '\\text{Median} = \\frac{x_{(n/2)} + x_{(n/2 + 1)}}{2}'},
  {'lb': 'Median, grouped',
   'tex': '\\text{Median} = L + \\left(\\frac{\\frac{N}{2} - CF}{f_m}\\right) c'},
  {'lb': 'Mode, grouped',
   'tex': '\\text{Mode} = L + \\left(\\frac{\\Delta_1}{\\Delta_1 + \\Delta_2}\\right) c'},
  {'lb': 'Empirical relationship',
   'tex': '\\text{Mode} = 3\\,\\text{Median} - 2\\,\\text{Mean}'},
  {'lb': 'Quartile $k$', 'tex': 'Q_k = L + \\left(\\frac{\\frac{kN}{4} - CF}{f_q}\\right) c'},
  {'lb': 'Decile $k$', 'tex': 'D_k = L + \\left(\\frac{\\frac{kN}{10} - CF}{f_d}\\right) c'},
  {'lb': 'Percentile $k$',
   'tex': 'P_k = L + \\left(\\frac{\\frac{kN}{100} - CF}{f_p}\\right) c'},
  {'lb': 'Lower class boundary',
   'tex': 'L = \\frac{\\text{lower limit of this class} + \\text{upper limit of the '
          'previous class}}{2}'},
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
    'src': 'Chapter 2.1', 'sec': '2.1'},
   {'q': 'A distribution has a mean of 48 and a median of 45. Using the empirical relationship, '
         'the mode is approximately',
    'o': ['39', '42', '46.5', '51', '54'],
    'a': 0,
    'w': 'Apply Mode = 3 Median − 2 Mean.',
    'calc': '\\text{Mode} = 3(45) - 2(48) = 135 - 96 = 39',
    'src': 'Chapter 2.3', 'sec': '2.3'},
   {'q': 'For a distribution with total frequency 50, the cumulative frequency traced on the ogive '
         'to give the 70th percentile is',
    'o': ['70', '50', '35', '25', '15'],
    'a': 2,
    'w': 'The 70th percentile is the value below which 70% of the observations fall.',
    'calc': 'P_{70} \\text{ at } \\frac{70}{100} \\times 50 = 35',
    'src': 'Chapter 2.4', 'sec': '2.4'},
   {'q': 'In a grouped distribution the median class is 40 – 49 with frequency 12. The cumulative '
         'frequency up to 39 is 28 and $N = 80$. The median is',
    'o': ['45.5', '49.5', '49.0', '39.5', '48.5'],
    'a': 2,
    'w': 'Apply the grouped median formula with $L = 39.5$, $N/2 = 40$, $CF = 28$, $f_m = 12$, '
         '$c = 10$.',
    'calc': '39.5 + \\left(\\frac{40 - 28}{12}\\right)(10) = 39.5 + 10 = 49.5',
    'src': 'Chapter 2.2', 'sec': '2.2'},
   {'q': 'Which measure of location is most affected by extreme values?',
    'o': ['Mode', 'Median', 'Arithmetic mean', 'Lower quartile', 'Upper quartile'],
    'a': 2,
    'w': 'The arithmetic mean uses every observation, so a single very large or very small value '
         'pulls it. The median and mode are positional and are unaffected.',
    'src': 'Chapter 2.3', 'sec': '2.3'},
   {'q': 'For any set of positive numbers that are not all equal, the correct ordering is',
    'o': ['$\\bar{x} < GM < HM$', '$HM < GM < \\bar{x}$', '$GM < HM < \\bar{x}$',
          '$\\bar{x} < HM < GM$', 'they are always equal'],
    'a': 1,
    'w': 'The harmonic mean is smallest, the arithmetic mean largest, with the geometric mean '
         'between them. Equality holds only when every value is the same.',
    'src': 'Chapter 2.1', 'sec': '2.1'},
   {'q': 'A grouped distribution has classes 5 – 9, 10 – 14, 15 – 19, … The lower class '
         'boundary of the class 15 – 19, for use in the median and mode formulas, is',
    'o': ['15', '14.5', '15.5', '14', '17'],
    'a': 1,
    'w': 'The classes have a 1-unit gap (9 to 10, 14 to 15), so the boundary is half a unit '
         'below the stated lower limit: $(14 + 15)/2 = 14.5$. The class width $c$ is '
         '$19.5 - 14.5 = 5$.',
    'src': 'Chapter 2.5', 'sec': '2.5'},
   {'q': 'Which of the following is NOT a measure of partition?',
    'o': ['Median', 'Mode', 'Quartile', 'Decile', 'Percentile'],
    'a': 1,
    'w': 'The measures of partition (quantiles) are the quartiles, deciles and percentiles; the '
         'median is the middle quantile. The mode is a measure of central tendency only.',
    'src': 'Chapter 2.6 (study text Q3)', 'sec': '2.6'},
   {'q': 'The quartiles of a grouped distribution are estimated graphically from a(n)',
    'o': ['histogram', 'bar chart', 'ogive', 'pie chart', 'frequency polygon'],
    'a': 2,
    'w': 'The ogive (cumulative frequency curve) gives the median and all quantiles. The '
         'histogram gives the mode.',
    'src': 'Chapter 2.6 (study text Q5)', 'sec': '2.6'},
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
    'src': 'Chapter 2.3', 'sec': '2.3'},
  ]},
}
