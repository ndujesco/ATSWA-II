CH = {
 'n': 1,
 't': 'Handling Statistical Data',
 'brief': 'Types of data, methods of collection, sampling designs, and the tables and charts used '
          'to present a distribution.',
 'outcomes': [
   'Distinguish primary from secondary data and qualitative from quantitative data',
   'Describe the methods of collecting primary data and their merits',
   'Distinguish the probability sampling designs from the non-probability ones',
   'Construct a grouped frequency distribution and identify class boundaries and limits',
   'Draw and interpret a histogram, frequency polygon, ogive and pie chart',
 ],
 'secs': [
  {'n': '1.1', 't': 'Types of data', 'b': [
    {'table': {'head': ['Basis', 'Types'], 'align': 'll', 'rows': [
      ['Source', '**Primary** — collected first-hand for the purpose at hand. '
       '**Secondary** — already collected by someone else for another purpose.'],
      ['Nature', '**Qualitative (attribute)** — described, not measured (colour, gender). '
       '**Quantitative (variable)** — measured or counted.'],
      ['Continuity', '**Discrete** — takes only whole values (number of cars). '
       '**Continuous** — takes any value in a range (weight, time).'],
      ['Measurement scale', '**Nominal**, **ordinal**, **interval**, **ratio**.'],
    ]}},
    {'table': {'head': ['', 'Primary data', 'Secondary data'], 'align': 'lll', 'rows': [
      ['Cost', 'Expensive', 'Cheap or free'],
      ['Time', 'Slow to obtain', 'Immediately available'],
      ['Fit to purpose', 'Exactly what is needed', 'May not fit the definition required'],
      ['Reliability', 'Known, because you collected it', 'Depends on the original collector'],
      ['Currency', 'Up to date', 'May be out of date'],
    ]}},
    {'h3': 'Methods of collecting primary data'},
    {'ul': [
      '**Direct personal interview** — the investigator meets the respondent. Accurate and allows '
      'clarification, but costly and prone to interviewer bias.',
      '**Indirect oral investigation** — witnesses or third parties are questioned; used where '
      'respondents are unwilling.',
      '**Questionnaire by post or online** — cheap and wide-reaching, but suffers low and '
      'possibly biased response rates.',
      '**Questionnaire through enumerators** — enumerators help respondents complete the form; '
      'better response, higher cost.',
      '**Observation** — recording behaviour directly, avoiding respondent bias entirely.',
      '**Telephone interview** — quick and cheap, but limited to those with telephones and to '
      'short interviews.',
    ]},
    {'note': 'Compiling from published sources is a method of collecting **secondary** data, not '
             'primary. That distinction is a standard multiple-choice trap.'},
  ]},

  {'n': '1.2', 't': 'Sampling', 'b': [
    {'p': 'A **census** examines every member of the population; a **sample** examines a part '
          'chosen to represent the whole. Sampling is used because a census is usually too '
          'costly, too slow, or destructive of the item tested.'},
    {'h3': 'Probability (random) sampling'},
    {'p': 'Every member of the population has a known, non-zero chance of selection, so sampling '
          'error can be measured.'},
    {'ul': [
      '**Simple random** — every member equally likely; drawn by lot or by random numbers. '
      'Requires a complete sampling frame.',
      '**Systematic** — take every $k$-th item after a random start, where $k = N/n$. Simple, but '
      'biased if the list has a periodic pattern.',
      '**Stratified** — the population is divided into homogeneous strata and a random sample '
      'drawn from each, usually in proportion to size. Gives the greatest precision where the '
      'strata differ from one another.',
      '**Cluster** — the population is divided into clusters, whole clusters are chosen at random '
      'and all members within them examined. Cheap where the population is geographically spread.',
      '**Multi-stage** — sampling in successive stages: states, then local governments, then '
      'households.',
    ]},
    {'h3': 'Non-probability sampling'},
    {'ul': [
      '**Quota** — interviewers fill preset quotas by category; cheap and fast, but the choice '
      'within a quota is not random.',
      '**Judgemental (purposive)** — the investigator selects those believed representative.',
      '**Convenience** — whoever is easiest to reach.',
      '**Snowball** — respondents recruit further respondents; used for hard-to-reach populations.',
    ]},
    {'key': 'The dividing line is whether the probability of selection is **known**. It is in '
            'every probability design and in none of the others, which is why sampling error can '
            'only be estimated for probability samples.'},
    {'eg': {'t': 'Systematic sampling', 'q': [
      {'p': 'A firm has 4,800 employees and wishes to draw a systematic sample of 120. Determine '
            'the sampling interval and describe the procedure.'}],
      'a': [
      {'tex': 'k = \\frac{N}{n} = \\frac{4800}{120} = 40'},
      {'p': 'Choose a random starting point between 1 and 40 — say 17 — then select employees '
            'numbered 17, 57, 97, 137, and so on, taking every 40th name until 120 are chosen.'},
      {'note': 'The risk is periodicity. If the list is ordered by department in groups of 40, '
               'every selection would come from the same position in each department and the '
               'sample would be systematically unrepresentative.'}]}},
  ]},

  {'n': '1.3', 't': 'The frequency distribution', 'b': [
    {'p': 'A **frequency distribution** is a table showing how often each value or group of '
          'values occurs. For continuous data the values are grouped into **classes**.'},
    {'table': {'head': ['Term', 'Meaning', 'For the class 20 – 29'], 'align': 'lll', 'rows': [
      ['Class limits', 'The values as written', '20 and 29'],
      ['Class boundaries', 'The true limits, half a unit beyond', '19.5 and 29.5'],
      ['Class width', 'Upper boundary − lower boundary', '$29.5 - 19.5 = 10$'],
      ['Class mark (mid-point)', 'The average of the two limits', '$(20 + 29)/2 = 24.5$'],
    ]}},
    {'warn': 'Class **boundaries** are used for histograms and ogives; class **marks** are used '
             'for computing means and standard deviations. Using limits instead of boundaries '
             'leaves gaps between the bars of a histogram, which is wrong for continuous data.'},
    {'p': 'Where the number of classes is not given, Sturges\' rule gives a reasonable starting '
          'point:'},
    {'tex': 'k = 1 + 3.322 \\log_{10} N', 'tag': '(1.1)'},
    {'tex': '\\text{Class width} \\approx \\frac{\\text{Range}}{k} '
            '= \\frac{\\text{Largest} - \\text{Smallest}}{k}', 'tag': '(1.2)'},
    {'eg': {'t': 'Building a grouped distribution', 'q': [
      {'p': 'Forty daily sales figures range from ₦12,000 to ₦91,000. Suggest a suitable number '
            'of classes and class width.'}],
      'a': [
      {'tex': 'k = 1 + 3.322 \\log_{10} 40 = 1 + 3.322(1.6021) = 1 + 5.32 = 6.32 \\approx 6'},
      {'tex': '\\text{Width} = \\frac{91{,}000 - 12{,}000}{6} = \\frac{79{,}000}{6} '
              '= 13{,}167 \\approx ₦15{,}000'},
      {'p': 'Six classes of width ₦15,000 starting at ₦10,000: 10,000–24,999; 25,000–39,999; and '
            'so on to 85,000–99,999. Round the width **up** to a convenient number so that the '
            'classes cover the whole range.'}]}},
  ]},

  {'n': '1.4', 't': 'Presenting data', 'b': [
    {'table': {'head': ['Chart', 'Shows', 'Built from'], 'align': 'lll', 'rows': [
      ['**Histogram**', 'The shape of a distribution', 'Adjacent bars over class boundaries; '
       'area proportional to frequency'],
      ['**Frequency polygon**', 'The shape, for comparison between distributions',
       'Class marks joined by straight lines'],
      ['**Ogive (cumulative frequency curve)**', 'How many fall below a value',
       'Cumulative frequency plotted against the **upper class boundary**'],
      ['**Bar chart**', 'Comparison between discrete categories', 'Separated bars; height only'],
      ['**Pie chart**', 'Composition of a whole', 'Sectors, angle $= \\frac{f}{\\sum f} \\times 360°$'],
      ['**Scatter diagram**', 'Relationship between two variables', 'Paired points'],
    ]}},
    {'key': 'The **ogive** is the workhorse. Read the median off it at $N/2$, the quartiles at '
            '$N/4$ and $3N/4$, deciles at $kN/10$ and percentiles at $kN/100$. It gives every '
            'measure of position except the **mode**, which is read from a histogram — that '
            'exception is examined nearly every diet.'},
    {'p': 'Where classes have **unequal widths**, the histogram must use frequency **density** so '
          'that area, not height, represents frequency:'},
    {'tex': '\\text{Frequency density} = \\frac{\\text{Frequency}}{\\text{Class width}}', 'tag': '(1.3)'},
    {'eg': {'t': 'Pie chart angles', 'q': [
      {'p': 'A company\'s costs are: materials ₦4,500,000; labour ₦3,000,000; overheads '
            '₦2,100,000; distribution ₦900,000. Compute the sector angles.'}],
      'a': [
      {'p': 'Total $= ₦10{,}500{,}000$.'},
      {'table': {'align': 'lrrl', 'head': ['Item', 'Amount (₦)', 'Angle', 'Working'], 'rows': [
        ['Materials', '4,500,000', '154.3°', '4.5/10.5 × 360'],
        ['Labour', '3,000,000', '102.9°', '3.0/10.5 × 360'],
        ['Overheads', '2,100,000', '72.0°', '2.1/10.5 × 360'],
        ['Distribution', '900,000', '30.9°', '0.9/10.5 × 360'],
        ['', '10,500,000', '360.0°', '', '@tot'],
      ]}},
      {'note': 'The angles must sum to 360°. Rounding each to one decimal and checking the total '
               'is a fast way to catch an arithmetic slip.'}]}},
    {'h3': 'SPSS and analytical software'},
    {'p': '**SPSS** stands for **Statistical Package for the Social Sciences**. It, along with '
          'Excel, R and Stata, is used for data entry, presentation and analysis. This has been '
          'asked directly as a multiple-choice question.'},
  ]},
 ],
 'formulas': [
  {'lb': "Sturges' rule for the number of classes", 'tex': 'k = 1 + 3.322 \\log_{10} N'},
  {'lb': 'Class width', 'tex': '\\text{Width} = \\frac{\\text{Range}}{k}'},
  {'lb': 'Class mark',
   'tex': 'x = \\frac{\\text{Lower limit} + \\text{Upper limit}}{2}'},
  {'lb': 'Frequency density',
   'tex': '\\text{Density} = \\frac{f}{\\text{class width}}',
   'nt': 'Needed whenever class widths are unequal.'},
  {'lb': 'Pie chart sector angle',
   'tex': '\\theta = \\frac{f}{\\sum f} \\times 360^\\circ'},
  {'lb': 'Systematic sampling interval', 'tex': 'k = \\frac{N}{n}'},
 ],
 'focus':
   'Two or three Section A marks every diet, on the definitions rather than on computation: which '
   'is a probability sampling design, what an ogive can and cannot estimate, what SPSS stands for, '
   'primary versus secondary data. Learn the list of sampling methods with one distinguishing '
   'sentence each. The grouped frequency table you build here is the input to Chapters 2 and 3, '
   'so get class boundaries and class marks right now.',
 'errors': [
   'Using class limits instead of boundaries when drawing a histogram.',
   'Plotting an ogive against class marks instead of upper class boundaries.',
   'Calling quota sampling a random method.',
   'Forgetting frequency density when class widths are unequal.',
   'Trying to read the mode from an ogive.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A table showing the number of times a value or group of values occurs in a set of data '
         'is called a',
    'o': ['frequency table', 'contingency table', 'probability table', 'times table',
          'four-figure table'],
    'a': 0,
    'w': 'That is the definition of a frequency table or frequency distribution. A contingency '
         'table cross-classifies two attributes; a probability table gives probabilities.',
    'src': 'Chapter 1.3'},
   {'q': 'The ogive can be used to estimate all of the following EXCEPT the',
    'o': ['median', 'quartiles', 'deciles', 'percentiles', 'mode'],
    'a': 4,
    'w': 'An ogive is a cumulative frequency curve, so it gives every measure of **position** — '
         'median, quartiles, deciles, percentiles. The mode is the most frequent value and is '
         'read from a histogram instead.',
    'src': 'Chapter 1.4'},
   {'q': 'SPSS stands for',
    'o': ['Standard Program for Statistical Sampling',
          'Statistical Package for the Social Sciences',
          'Systematic Procedure for Sample Selection',
          'Statistical Presentation and Sampling System',
          'Structured Package for Scientific Statistics'],
    'a': 1,
    'w': 'Statistical Package for the Social Sciences — one of the standard tools for data entry, '
         'presentation and analysis.',
    'src': 'Chapter 1.4'},
   {'q': 'Which of the following is NOT a probability sampling method?',
    'o': ['Simple random sampling', 'Stratified sampling', 'Cluster sampling', 'Quota sampling',
          'Systematic sampling'],
    'a': 3,
    'w': 'In quota sampling the interviewer chooses whom to approach within each quota, so the '
         'probability of any individual being selected is unknown. That is what makes it '
         'non-probability sampling.',
    'src': 'Chapter 1.2'},
   {'q': 'For the class interval 30 – 39, the class boundaries are',
    'o': ['30 and 39', '29.5 and 39.5', '30.5 and 38.5', '29 and 40', '34.5 only'],
    'a': 1,
    'w': 'Class boundaries extend half a unit beyond the stated limits so that adjacent classes '
         'touch, which is what continuous data requires.',
    'src': 'Chapter 1.3'},
   {'q': 'A population of 3,600 is to be sampled systematically with a sample size of 90. The '
         'sampling interval is',
    'o': ['30', '40', '45', '36', '90'],
    'a': 1,
    'w': 'The interval is population size divided by sample size.',
    'calc': 'k = \\frac{3600}{90} = 40',
    'src': 'Chapter 1.2'},
   {'q': 'The first and last points on a frequency polygon have',
    'o': ['zero frequencies', 'cumulative frequencies', 'high frequencies', 'low frequencies',
          'undefined frequencies'],
    'a': 0,
    'w': 'The polygon is closed by extending it to the class marks of the empty classes '
         'immediately below the first and above the last, where the frequency is zero. This makes '
         'the area under the polygon equal the area of the histogram.',
    'src': 'Chapter 1.4'},
  ],
  'theory': [
   {'q': 'Distinguish between primary and secondary data, and describe FOUR methods of collecting '
         'primary data, giving one advantage and one disadvantage of each.',
    'marks': 10,
    'a': [
      {'p': '**Primary data** is collected at first hand by or for the investigator, specifically '
            'for the enquiry in hand. **Secondary data** has already been collected by someone '
            'else, usually for a different purpose, and is used second-hand.'},
      {'table': {'head': ['Method', 'Advantage', 'Disadvantage'], 'align': 'lll', 'rows': [
        ['**Direct personal interview**', 'High accuracy; the investigator can probe and clarify',
         'Expensive and slow; risk of interviewer bias'],
        ['**Postal or online questionnaire**', 'Cheap; reaches a wide and dispersed population',
         'Low response rate, and non-respondents may differ systematically from respondents'],
        ['**Questionnaire through enumerators**',
         'Higher response rate; the enumerator resolves misunderstandings',
         'Costly, and enumerators must be trained and supervised'],
        ['**Observation**', 'Free of respondent bias, since behaviour is recorded directly',
         'Cannot capture attitudes or reasons; may be slow and intrusive'],
        ['**Telephone interview**', 'Very quick and inexpensive',
         'Restricted to telephone owners and to short interviews'],
        ['**Indirect oral investigation**', 'Reaches information respondents will not give directly',
         'Depends on the reliability and memory of third parties'],
      ]}}],
    'src': 'Chapter 1.1'},
  ]},
}
