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
    {'p': '**SPSS** stands for **Statistical Package for the Social Sciences** (now IBM SPSS '
          'Statistics). It, along with **Microsoft Excel**, R and Stata, is used for data entry, '
          'presentation and analysis. Excel ships with Microsoft Office and has built-in '
          'statistical functions and a data-analysis tool pack; SPSS must be installed '
          'separately and has four windows — **data editor** (with *data view* and *variable '
          'view*), **output**, **syntax** and **script** — of which the data editor and output '
          'windows matter most. This has been asked directly as a multiple-choice question.'},
  ]},

  {'n': '1.5', 't': 'Full revision summary (listed)', 'b': [
    {'p': 'Everything in this chapter, compressed to lists for a last read-through. Nothing here '
          'is new — it is §§1.1–1.4 in recall form, mapped below so you can check off every '
          'section as you go.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§1.1 Types of data** — covered in **A–C** below: what data/statistics are, the '
      'primary/secondary, qualitative/quantitative, discrete/continuous and nominal/ordinal/'
      'interval/ratio classifications, and the six methods of collecting primary data with '
      'their trade-offs (compiling from published sources is **secondary**, not primary — a '
      'standard trap).',
      '**§1.2 Sampling** — covered in **D–E**: census vs sample; probability sampling (simple '
      'random, systematic, stratified, cluster, multi-stage) where selection probability is '
      '**known**, vs non-probability sampling (quota, judgemental, convenience, snowball) '
      'where it is not — that distinction is the whole difference and is what makes sampling '
      'error estimable only for probability designs.',
      '**§1.3 The frequency distribution** — covered in **G–H**: what a frequency table is; '
      'Sturges\' rule $k=1+3.322\\log_{10}N$ for the number of classes; class limits vs '
      '**boundaries** vs width vs mid-point/mark, with the boundary formula and the warning '
      'that boundaries feed histograms/ogives/median/mode while marks feed the mean.',
      '**§1.4 Presenting data** — covered in **F, I–J**: text/tabular/diagrammatic '
      'presentation; bar charts (simple, multiple, component, percentage component); pie '
      'charts (sector angle $=f/\\sum f\\times360°$); histograms (area, not height, '
      'proportional to frequency — use frequency density for unequal widths); frequency '
      'polygons (closed at zero-frequency class marks either end); ogives (less-than vs '
      'more-than, gives every positional measure except the mode); and the software — Excel '
      'and SPSS (data editor, output, syntax, script windows).',
    ]},
    {'h3': 'A. Data and statistics'},
    {'ul': [
      '**Data / statistical data** — raw facts, numeric or non-numeric, collected, analysed and '
      'summarised for presentation and interpretation.',
      '**Statistics** — the scientific method of collecting, presenting, analysing and '
      'interpreting data, and of making inferences under uncertainty.',
      '**Descriptive statistics** — summarises a data set (collection, summarising, comparison).',
      '**Inferential statistics** — uses a sample to draw conclusions about the population.',
    ]},
    {'h3': 'B. Classification of data'},
    {'ul': [
      '**By value** — *Numeric (quantitative)*: **discrete** (whole numbers only — number of '
      'students, number of typists) and **continuous** (any value including fractions — wages, '
      'prices, weights, exam marks). *Non-numeric (qualitative)*: **categorical / nominal** '
      '(groups with no order — gender, nationality, religion, political affiliation) and '
      '**ordinal** (ranked on a scale — age group, rank of a soldier, socio-economic status).',
      '**By collection process** — *Primary*: collected first-hand for the specific enquiry. '
      '*Secondary*: taken from records already collected by others.',
      '**Secondary-data agencies** — National Bureau of Statistics (NBS), Central Bank of '
      'Nigeria (CBN), educational institutions, ministries, private companies. (Financial data → '
      'CBN, ICAN, banks; health data → Federal/State Ministries of Health, WHO, NCDC; oil & gas '
      '→ NNPC, Ministry of Petroleum Resources, OPEC; security → Nigeria Police, Ministry of '
      'Defence; political → INEC, the Assemblies.)',
    ]},
    {'h3': 'C. Methods of collecting primary data'},
    {'ul': [
      '**Mail (postal) questionnaire** — a set of logically arranged questions filled by the '
      'respondent; posted out. *Question types*: **close-ended / coded** (pick from given '
      'answers) and **open-ended / uncoded** (respondent writes freely). *Good questionnaire*: '
      'well structured into sections (personal data first); clear, unambiguous, not lengthy; no '
      'leading questions; no calculations required; not offensive; logical order. '
      '*Advantages*: wide coverage, cheap, saves time. *Disadvantages*: unreliable postal '
      'service, non-response, unreliable answers.',
      '**Interview** — face-to-face or by a medium such as telephone. *Advantages*: detailed, '
      'accurate, reliable; method and accuracy known. *Disadvantages*: time-consuming, '
      'expensive. Sub-types: **interview schedule** (a form the *interviewer* completes while '
      'asking questions — reliable, cuts non-response, questions can be reframed, difficult '
      'respondents persuaded); **telephone interview** (fast, faster call-backs, less '
      'non-response — but biased toward telephone owners); **group discussion** (several people, '
      'one focus event).',
      '**Observation** — recording behaviour, skills, objects in their natural state. '
      '**Controlled** (predetermined rules and procedures) or **uncontrolled**.',
    ]},
    {'note': 'A **schedule** is completed by the *investigator/interviewer*; a **questionnaire** '
             'is completed by the *respondent* — study text MCQ 2 turns on exactly this.'},
    {'h3': 'D. Sampling — terms'},
    {'ul': [
      '**Population** — every item with a defined characteristic (people, animals, objects, or '
      'a defined group such as "ATS candidates"). **Finite** = countable (students in a '
      'college); **infinite** = uncountable (sand particles on a beach).',
      '**Sample** — a fractional part of a population studied to make a statement about the '
      'whole.',
      '**Census** — complete enumeration of every unit (2006 head count).',
      '**Sample survey** — collecting information using a representative sample.',
      '**Sampling frame** — a list of all units in the target population, used as the basis for '
      'selection (church-member list, telephone directory).',
      '**Sampling unit** — any individual member of the population.',
      '**Notation** — $N$ = population size, $n$ = sample size; **sampling fraction** '
      '$f = n/N$; **expansion (raising) factor** $g = N/n$.',
    ]},
    {'p': '**Purposes of sampling**: cuts the cost of data collection; greater accuracy than '
          'covering the whole population; faster; saves time; analysis is less tedious.'},
    {'h3': 'E. Sampling methods'},
    {'ul': [
      '**Probability (random) sampling** — every unit has a definite, known chance of '
      'selection; sampling error can be estimated.',
      '  · **Simple random sampling (SRS)** — equal chance for every member; needs a sampling '
      'frame; by random-number table or lottery/raffle; *with* or *without* replacement. '
      '+ fair, simple, unbiased estimates.  − useless without a frame; heavy drawing from one '
      'part defeats fairness.',
      '  · **Systematic sampling** — needs a serially numbered frame; pick a random start '
      'within the first $k$, then every $k$-th unit, where $k = N/n$ rounded **down** to a '
      'whole number (e.g. $N=120$, $n=15$ → $k=8$; start 5 → 5, 13, 21, 29, …). + easy, good '
      'representation.  − no frame, no method; biased if the list is periodic.',
      '  · **Stratified sampling** — for a *heterogeneous* population: split into '
      '**homogeneous, non-overlapping strata** (by income level, employment status, …), then '
      'SRS within each. + more representative, more precise.  − hard to choose the basis for '
      'stratification; problem of weighting the strata.',
      '  · **Cluster sampling** — units occur in natural clusters (farm settlements, schools) '
      'or artificial ones (faculties); randomly select whole clusters and take all their units.',
      '  · **Multi-stage sampling** — sampling in two or more stages (institutions → faculties '
      '→ departments); the first-stage list is the *primary sampling units*; the number of '
      'stages names it (five-stage = five stages). + simple and cheap if frames exist at each '
      'stage.  − tedious without frames; complex variance estimation.',
      '**Non-probability sampling** — chance of selection is unknown; sampling error cannot be '
      'estimated.',
      '  · **Quota sampling** — the investigator fills preset category quotas (quota admission '
      'to Federal Colleges). + fair spread without a frame, no frame needed.  − sampling error '
      'not estimable.',
      '  · **Judgemental (purposive) sampling** — units chosen to fit a criterion of interest '
      '(interviewing only those with on-the-job experience). + in-depth insight, targets the '
      'right group.  − researcher bias, selective sample.',
      '  · **Convenience sampling** — whoever is easiest to reach (a lecturer using her own '
      'students). + easy, quick, cheap.  − inaccurate, biased, unrepresentative.',
      '  · **Snowball sampling** — respondents refer further respondents, rolling on until the '
      'sample is complete (drug use among youths). + raises participation, reaches '
      'hard-to-find populations.  − unrepresentative, biased.',
    ]},
    {'h3': 'F. Data presentation'},
    {'ul': [
      '**Bases of classification** — qualitative (by type/quality), quantitative (by range), '
      'chronological (time series — trend, cyclical, periodic, irregular), geographical (by '
      'location).',
      '**Three methods** — *text* (words + figures, emphasis on the figures), *tabular*, '
      '*diagrammatic* (charts and graphs).',
      '**Table** — more detailed than text; brief and self-explanatory. *Simple* table (one '
      'variable against one other) vs *complex* table (several items, sub-divisions). '
      '*Essential features*: title; row/column headings; source; footnote.',
    ]},
    {'h3': 'G. Frequency tables'},
    {'ul': [
      '**Frequency table** — how many times each value / group of values occurs. *Ungrouped* '
      '(value against its frequency) or *grouped* (class intervals against frequency).',
      '**Grouped-table guidelines** — 5 to 8 classes; class width 5 or a multiple of 5; equal '
      'widths (except wider open ends for extreme values); every observation in exactly one '
      'class; **avoid overlapping limits** like 5–10, 10–15 (where does 10 go?); open-ended '
      'classes ("less than 20", "10 and above") are assumed the same width as their neighbours.',
      '**Tally method** — one stroke per occurrence, the fifth struck across the first four; '
      'go through the data **once**.',
    ]},
    {'h3': 'H. Class limits, boundaries, width, mid-point'},
    {'ul': [
      '**Class limits** — the numbers as written. For class 31 – 40: lower limit 31, upper '
      'limit 40.',
      '**Class boundaries** — the *true* limits. Lower boundary $= \\dfrac{\\text{upper limit '
      'of the previous class} + \\text{lower limit of this class}}{2}$; upper boundary $= '
      '\\dfrac{\\text{upper limit of this class} + \\text{lower limit of the next class}}{2}$. '
      'The lower boundary of a class equals the upper boundary of the class before it. '
      'For 21 – 30: lower boundary $(20+21)/2 = 20.5$, upper boundary $(30+31)/2 = 30.5$.',
      '**Class size / width** — difference between the boundaries, e.g. $30.5 - 20.5 = 10$. The '
      'first lower boundary and last upper boundary are obtained by logic.',
      '**Class mid-point / class mark** — $\\dfrac{\\text{lower limit} + \\text{upper limit}}'
      '{2}$, e.g. $(41+50)/2 = 45.5$. Successive mid-points differ by the class width. Class '
      'marks represent the class in calculations (mean, standard deviation) and are the '
      'x-values of a frequency polygon.',
      '**Cumulative frequency** — running total of the frequencies up to and including each '
      'class.',
    ]},
    {'warn': 'Boundaries — not limits — are used for **histograms** and **ogives**, and for the '
             '**median and mode formulas** in Chapter 2. Class **marks** (limits averaged) are '
             'used for the **mean**. Where classes are written continuously (0–10, 10–20) the '
             'lower limit already *is* the lower boundary; where there is a gap (1–10, 11–20) it '
             'is not — see Chapter 2 §2.5.'},
    {'h3': 'I. Charts and graphs'},
    {'ul': [
      '**Bar chart** — equal-width bars, *height* proportional to value, gaps between bars, '
      'usually vertical. Forms: *simple*, *multiple* (groups side by side), *component / '
      'stacked* (each bar split into parts), *percentage component* (all bars 100% tall, split '
      'by percentage share).',
      '**Pie chart** — a circle split into sectors; sector angle $= \\dfrac{\\text{component}}'
      '{\\text{total}} \\times 360^\\circ$; angles must sum to 360°.',
      '**Histogram** — adjacent (touching) rectangles over **class boundaries**; **area** (not '
      'height) is proportional to frequency. Unequal widths → adjust: pick the common width and '
      'multiply each frequency by (common width ÷ its width) — i.e. use frequency density. Used '
      'to estimate the **mode**.',
      '**Frequency polygon** — frequencies plotted against **class marks** and joined by '
      'straight lines; closed by joining to the class marks of the empty classes before the '
      'first and after the last (zero frequency). Smoothed, it becomes the **frequency curve**, '
      'showing the shape of the distribution.',
      '**Ogive (cumulative frequency curve)** — cumulative frequency against **class '
      'boundaries**. *Less-than* type: cumulate from the top; plot against **upper** '
      'boundaries. *More-than* type: cumulate from the bottom; plot against **lower** '
      'boundaries. Used to estimate the **median, quartiles, deciles and percentiles** — but '
      '**not the mode**. Where both ogives are drawn together, they cross at the **median**.',
    ]},
    {'h3': 'J. Software'},
    {'ul': [
      '**Microsoft Excel** — spreadsheet; comes with Microsoft Office; graphic tools, pivot '
      'tables, built-in statistical/financial functions, data-analysis tool pack.',
      '**SPSS** — Statistical Package for the Social Sciences (now IBM SPSS Statistics); '
      'installed separately; windows: data editor (data view + variable view), output, syntax, '
      'script.',
    ]},
  ]},

  {'n': '1.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following is a non-numeric ordinal data? (A) Income  (B) Price of a '
        'commodity  (C) Occupation  (D) Rating in a beauty contest  (E) Students\' numbers in a '
        'class',
        'A schedule in statistics refers to (A) an examination timetable  (B) a set of '
        'questions filled by the respondent  (C) a set of questions filled by the investigator '
        'him/herself  (D) a set of past examination questions  (E) paper used by bankers for '
        'investigation',
        'Which sampling method does not need a sampling frame? (A) simple random  (B) purposive  '
        '(C) systematic  (D) cluster  (E) stratified',
        'The following are qualities of a good questionnaire **except** (A) each question is '
        'precise and unambiguous  (B) leading questions are avoided  (C) it must be lengthy to '
        'accommodate many questions  (D) it is well structured into related sections  '
        '(E) double-barrelled questions are avoided',
        'In sampling, a list of all units in a target population is known as a …',
        'A small or fractional part of a population selected to meet some objective is a …',
        'A spreadsheet with built-in functions for engineering, statistical and financial '
        'questions is …',
        'A report combining text and figures is known as … presentation',
        'A histogram is similar to a bar chart except that its bars … each other',
        'The age of an employee is an example of … type of data',
      ]}],
      'a': [
      {'ol': [
        '**D — rating in a beauty contest** (ranked, non-numeric).',
        '**C** — a schedule is completed by the *investigator*.',
        '**B — purposive (judgemental)** sampling needs no frame. (Quota, convenience and '
        'snowball also need none; of the options listed, purposive is the answer.)',
        '**C** — a good questionnaire must **not** be lengthy.',
        '**Sampling frame.**',
        '**Sample.**',
        '**Microsoft Excel.**',
        '**Text** presentation.',
        '**Touch** (the bars are continuous / adjacent).',
        '**Continuous numeric** (quantitative continuous) data.'],
      }]}},
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
  {'lb': 'Class boundary (lower)',
   'tex': '\\text{Lower boundary} = \\frac{\\text{upper limit of previous class} + '
          '\\text{lower limit of this class}}{2}',
   'nt': 'The upper boundary of a class is the lower boundary of the class after it.'},
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
    'src': 'Chapter 1.3', 'sec': '1.3'},
   {'q': 'The ogive can be used to estimate all of the following EXCEPT the',
    'o': ['median', 'quartiles', 'deciles', 'percentiles', 'mode'],
    'a': 4,
    'w': 'An ogive is a cumulative frequency curve, so it gives every measure of **position** — '
         'median, quartiles, deciles, percentiles. The mode is the most frequent value and is '
         'read from a histogram instead.',
    'src': 'Chapter 1.4', 'sec': '1.4'},
   {'q': 'SPSS stands for',
    'o': ['Standard Program for Statistical Sampling',
          'Statistical Package for the Social Sciences',
          'Systematic Procedure for Sample Selection',
          'Statistical Presentation and Sampling System',
          'Structured Package for Scientific Statistics'],
    'a': 1,
    'w': 'Statistical Package for the Social Sciences — one of the standard tools for data entry, '
         'presentation and analysis.',
    'src': 'Chapter 1.4', 'sec': '1.4'},
   {'q': 'Which of the following is NOT a probability sampling method?',
    'o': ['Simple random sampling', 'Stratified sampling', 'Cluster sampling', 'Quota sampling',
          'Systematic sampling'],
    'a': 3,
    'w': 'In quota sampling the interviewer chooses whom to approach within each quota, so the '
         'probability of any individual being selected is unknown. That is what makes it '
         'non-probability sampling.',
    'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'For the class interval 30 – 39, the class boundaries are',
    'o': ['30 and 39', '29.5 and 39.5', '30.5 and 38.5', '29 and 40', '34.5 only'],
    'a': 1,
    'w': 'Class boundaries extend half a unit beyond the stated limits so that adjacent classes '
         'touch, which is what continuous data requires.',
    'src': 'Chapter 1.3', 'sec': '1.3'},
   {'q': 'A population of 3,600 is to be sampled systematically with a sample size of 90. The '
         'sampling interval is',
    'o': ['30', '40', '45', '36', '90'],
    'a': 1,
    'w': 'The interval is population size divided by sample size.',
    'calc': 'k = \\frac{3600}{90} = 40',
    'src': 'Chapter 1.2', 'sec': '1.2'},
   {'q': 'The first and last points on a frequency polygon have',
    'o': ['zero frequencies', 'cumulative frequencies', 'high frequencies', 'low frequencies',
          'undefined frequencies'],
    'a': 0,
    'w': 'The polygon is closed by extending it to the class marks of the empty classes '
         'immediately below the first and above the last, where the frequency is zero. This makes '
         'the area under the polygon equal the area of the histogram.',
    'src': 'Chapter 1.4', 'sec': '1.4'},
   {'q': 'Which of the following is non-numeric ordinal data?',
    'o': ['Monthly income', 'Price of a commodity', 'Occupation',
          'Rating in a beauty contest', 'Number of students in a class'],
    'a': 3,
    'w': 'A beauty-contest rating puts entrants in rank order but the "values" are not '
         'measurements — non-numeric and ordinal. Occupation is non-numeric but only nominal; '
         'the rest are numeric.',
    'src': 'Chapter 1.6 (study text Q1)', 'sec': '1.6'},
   {'q': 'In statistics, a schedule is a set of questions that is completed by the',
    'o': ['respondent, unaided', 'investigator or interviewer', 'supervisor after the interview',
          'data-entry clerk', 'head of the statistics office'],
    'a': 1,
    'w': 'A schedule is filled in by the investigator as they put the questions; a '
         'questionnaire is filled in by the respondent. That is the whole distinction.',
    'src': 'Chapter 1.6 (study text Q2)', 'sec': '1.6'},
   {'q': 'A list containing every unit in the target population, used as the basis for selecting '
         'a sample, is called the',
    'o': ['sampling unit', 'sampling frame', 'sampling fraction', 'census', 'population'],
    'a': 1,
    'w': 'The sampling frame is the list; a sampling unit is one member of it; the sampling '
         'fraction is $n/N$.',
    'src': 'Chapter 1.6 (study text Q5)', 'sec': '1.6'},
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
    'src': 'Chapter 1.1', 'sec': '1.1'},
  ]},
}
