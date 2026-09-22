CH = {
 'n': 1,
 't': 'Handling of Statistical Data',
 'brief': 'What statistical data is, how it is classified and collected, the sampling designs '
          'used to study a population, and the tables, charts and graphs used to present a '
          'distribution — including the study text\'s own worked examples for every chart.',
 'outcomes': [
   'Know the meaning of statistical data',
   'Know the types of data, and how to collect and classify them',
   'Understand the concept of data presentation in charts and graphs',
   'Understand the use of statistical packages for data presentation',
   'Understand the various methods of sampling',
 ],
 'secs': [
  {'n': '1.1', 't': 'Introduction', 'b': [
    {'p': 'Information is the key to the smooth running of an organisation or a country. A piece '
          'of information, or raw fact — numerical or non-numerical — that is collected, '
          'analysed and summarised for presentation and interpretation, is known as **data**, or '
          'statistical data.'},
    {'def': {'t': 'Statistics', 'd': 'a scientific method concerned with data collection, '
                  'presentation, analysis, interpretation and inference about data, where issues '
                  'of uncertainty are involved. Handling statistical data is itself sometimes '
                  'called statistics.'}},
    {'p': 'Statistics is useful in any area of human endeavour where decision-making matters — '
          'Accountancy, Engineering, Education, Business, the Social Sciences, Law, Agriculture, '
          'among others.'},
    {'p': 'Statistics is broadly classified into two:'},
    {'ul': [
      '**Descriptive statistics** — deals with data collection, and summarising and comparing '
      'numerical data; it is concerned with summarising a data set rather than using it to '
      'learn about the population.',
      '**Inferential statistics** — deals with techniques and tools for collecting data from a '
      'population, studying it through a **sample**, gaining knowledge of the population\'s '
      'characteristics and making vital decisions about the sampled population.',
    ]},
  ]},

  {'n': '1.2', 't': 'Broad classification of statistical data', 'b': [
    {'p': 'Statistical data is broadly classified into two: **numeric** and **non-numeric** '
          'data.'},
    {'h4': 'Numeric (quantitative) data'},
    {'p': 'Data whose values can be quantified — number of bank staff, number of candidates '
          'registered for an examination diet, ages, heights. Numeric data is classified '
          'further into:'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning'], 'rows': [
      ['**Discrete**', 'Values are integers — whole numbers, negative, zero or positive. No '
       'decimal or fractional value can occur — e.g. number of students in a class, number of '
       'typists in an organisation.'],
      ['**Continuous**', 'Values can be integer, fraction or decimal, negative, zero or '
       'positive — e.g. wages of workers, prices of goods and services, weights of employees, '
       'examination marks.'],
    ]}},
    {'h4': 'Non-numeric (qualitative) data'},
    {'p': 'Data whose values cannot be quantified — gender, marital status, state of origin, a '
          'boxer\'s weight class, income group, socio-economic status. Classified further into:'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning'], 'rows': [
      ['**Categorical (nominal)**', 'Cannot be put on an ordinal scale — facts collected by '
       'classification into groups or categories, e.g. gender, nationality, state of origin, '
       'type of religion, political affiliation.'],
      ['**Ordinal**', 'Can be put on an ordinal scale — using a particular yardstick or '
       'condition for group ranking, e.g. age group, rank of a soldier, socio-economic status.'],
    ]}},
    {'h4': 'Classification by collection process'},
    {'table': {'align': 'll', 'head': ['Type', 'Meaning'], 'rows': [
      ['**Primary data**', 'Obtained by direct collection from respondents/informants, or '
       'through one-on-one interaction — collected from a planned experiment relevant to the '
       'investigation, specifically for the purpose the investigation is carried out.'],
      ['**Secondary data**', 'Obtained, collected or extracted from already existing records or '
       'sources — published or unpublished records of government agencies, trade associations, '
       'research bureaus, magazines and individual research.'],
    ]}},
    {'p': 'Well-known secondary data collection agencies include the **National Bureau of '
          'Statistics (NBS)**, the **Central Bank of Nigeria (CBN)**, educational institutions, '
          'ministries, and commercial/private companies.'},
    {'table': {'align': 'lll', 'head': ['Type of data', 'Example', 'Source'], 'rows': [
      ['Financial', 'List of commercial banks; list of chartered accountants; exchange/interest '
       'rates', 'CBN; ICAN; commercial banks'],
      ['Health', 'List of public hospitals; list of medical doctors; number suffering from '
       'COVID-19', 'Federal/State Ministries of Health; WHO; NCDC'],
      ['Oil and gas', 'Number of refineries; registered petroleum marketers; crude-oil '
       'exporting countries', 'NNPC; Federal Ministry of Petroleum Resources; OPEC'],
      ['Security', 'Number of police personnel; correctional centres; military personnel',
       'Nigeria Police Force; Ministry of Defence; NDA; Federal Ministry of Interior'],
      ['Political', 'Number of political parties; registered voters; national lawmakers',
       'INEC; Federal Government; National/State Assemblies'],
    ]}},
  ]},

  {'n': '1.3', 't': 'Methods of collecting primary data', 'b': [
    {'h4': 'Mail (postal) questionnaire'},
    {'def': {'t': 'Questionnaire', 'd': 'a document consisting of a set of logically arranged '
                  'questions, to be filled by the respondent. Copies are sent by post for the '
                  'respondent to complete.'}},
    {'p': 'Questions are of two types: **close-ended (coded)**, where alternative answers are '
          'given for the respondent to pick from, and **open-ended (uncoded)**, where the '
          'respondent answers freely, without a restricted choice.'},
    {'p': 'A good questionnaire is:'},
    {'ol': [
      'well structured, so major sections are available — personal data first, then the '
      'questions relevant to the subject of investigation;',
      'clear in language, not ambiguous and not lengthy;',
      'free of leading questions;',
      'free of questions that require calculation;',
      'neither offensive nor resentful; and',
      'arranged in a logical order.',
    ]},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Wide area covered; cheap; saves a lot of time', 'Postal services are unreliable; '
       'non-response; unreliable answers may be given'],
    ]}},
    {'h4': 'Interview method'},
    {'p': 'Data is collected through conversation, by face-to-face contact or through a medium '
          'such as telephone.'},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Detailed, accurate information; the method and level of accuracy are known; reliable',
       'Time-consuming; expensive'],
    ]}},
    {'p': 'The interview method is accomplished by (a) **schedule**, (b) **telephone**, or '
          '(c) **group discussion**.'},
    {'table': {'align': 'lll', 'head': ['Sub-type', 'How it works', 'Advantages / disadvantages'],
      'rows': [
      ['**Interview schedule**', 'A schedule — a form of questions completed by the '
       '*interviewer* as he/she asks the respondent — is used.', '+ reliable/accurate; cuts '
       'non-response; questions can be reframed; difficult respondents can be persuaded. '
       '− time-consuming; expensive.'],
      ['**Telephone interview**', 'Questions are asked by telephone; both respondent and '
       'interviewer need access to one.', '+ fast; uncooperative respondents can be persuaded; '
       'faster call-backs; less non-response. − biased toward telephone owners; the '
       'telephone-less cannot be reached; data may be unreliable.'],
      ['**Group discussion**', 'The interview is conducted with more than one person, focused '
       'on a particular event.', '—'],
    ]}},
    {'key': 'A **schedule** is completed by the interviewer; a **questionnaire** is completed by '
            'the respondent. This exact distinction is the study text\'s own end-of-chapter '
            'question 2.'},
    {'h4': 'Observation method'},
    {'p': 'Enables data to be collected on the behaviour, skills, etc. of persons or objects that '
          'can be observed in their natural state. It is **controlled** when what is to be '
          'observed is predetermined by rules and procedures; otherwise it is **uncontrolled**.'},
  ]},

  {'n': '1.4', 't': 'Sampling', 'b': [
    {'p': 'Sampling is an important statistical method entailing the use of a fractional part of '
          'a population to study and make decisions about the characteristics of the whole '
          'population.'},
    {'h4': 'Definitions'},
    {'ul': [
      '**Population** — a collection or group of items satisfying a definite characteristic '
      '(human beings, animate objects such as cattle, inanimate objects such as chairs, or a '
      'given population such as ATS candidates). **Finite population** has a countable number '
      'of items (students in a college); **infinite population** has an uncountable number '
      '(sand particles on a beach).',
      '**Sample** — the fractional part of a population selected to observe or study it, for '
      'the purpose of making a scientific statement or decision about the population.',
      '**Census** — a complete enumeration of all units in the population, collecting vital '
      'information on each unit (e.g. Nigeria\'s year 2006 head count).',
      '**Sample survey** — a statistical method of collecting information using a fractional '
      'part of the population as a representative sample.',
      '**Sampling frame** — a list containing all the items or units in the target population, '
      'normally used as the basis for selecting a sample (e.g. a list of church members, a '
      'telephone directory).',
      '**Sampling unit** — any individual member of a population.',
    ]},
    {'fbox': {'h': 'Sampling notation', 'rows': [
      {'lb': 'Population and sample size', 'tex': 'N = \\text{population size}, \\quad '
        'n = \\text{sample size}'},
      {'lb': 'Sampling fraction', 'tex': 'f = \\frac{n}{N}'},
      {'lb': 'Expansion (raising) factor', 'tex': 'g = \\frac{N}{n}'},
    ]}},
    {'h4': 'Purpose of sampling'},
    {'p': 'Sampling is the act of selecting a representative sample from a target population to '
          'gather valuable data for planning and decision-making. It serves several purposes:'},
    {'ol': [
      'reduces the cost of collecting data — a sample costs much less than the whole population;',
      'the accuracy of the research result is greater with sampling than with the entire '
      'population;',
      'information is gathered at a faster speed;',
      'enough time is saved when a smaller unit is analysed; and',
      'analysing sampled data is less tedious than analysing the target population.',
    ]},
    {'h4': 'Probability sampling methods'},
    {'p': 'Involves **random selection**: each unit of the population is given a definite chance '
          '(probability) of being included.'},
    {'ul': [
      '**Simple random sampling (SRS)** — every member has an equal chance; needs a sampling '
      'frame; achieved by a table of random numbers, or a lottery/raffle draw. May be *with '
      'replacement* (a unit can be selected again) or *without replacement* (it cannot). '
      '+ fair, simple and straightforward, unbiased estimates. − not usable without a sampling '
      'frame; heavy drawing from one part of the population can defeat the fairness.',
      '**Systematic sampling (SS)** — needs a sampling frame with each unit numbered serially. '
      'The first sample is selected randomly within the first $k$, then every $k$-th unit is '
      'taken, where $k=N/n$, rounded down to a whole number (any decimal part is ignored). '
      '+ easy to handle; good representation if the frame is available. − not appropriate '
      'without a frame.',
      '**Stratified sampling (STS)** — used where the population is **heterogeneous**. '
      'Breaking a heterogeneous population into a number of homogeneous, non-overlapping groups '
      'is **stratification**; each group is a **stratum**. Common bases for stratifying are '
      'income level and employment status. Samples are then drawn from each stratum by simple '
      'random sampling. + pooling samples from the strata gives a more representative sample; '
      'more precise, accurate results. − difficulty deciding the basis for stratification; the '
      'problem of assigning weights to different strata.',
      '**Cluster sampling (CS)** — some populations exist in natural clusters (farm '
      'settlements, schools) or artificial clusters (faculties within an institution). '
      'Involves the random selection of some clusters from all the clusters in the population, '
      'which represent the sample.',
      '**Multi-stage sampling (MSS)** — involves two or more stages. The population is first '
      'broken into a set of distinct groups, and some are randomly selected — the list of '
      'selected groups is the **primary sampling units**. Each selected group is then broken '
      'down further and sampled again (a *second-stage sampling*, if the process stops there). '
      'Further stages may be added; the number of stages names the method (e.g. five-stage '
      'sampling). + simple if the sampling frame is available at every stage; low cost of '
      'implementation. − tedious if the frame is hard to obtain; complex variance estimation.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Systematic sampling interval', 'open': True, 'q': [
      {'p': 'In a population of $N=120$, 15 samples are needed. Determine the sampling interval '
            'and, if serial number 5 is the first one picked, the subsequent sample numbers.'}],
      'a': [
      {'tex': 'k = \\frac{N}{n} = \\frac{120}{15} = 8'},
      {'p': 'The first sample number lies between 1 and 8. If 5 is picked, the subsequent '
            'numbers are equidistant, an interval of 8 apart:'},
      {'tex': '5+8=13, \\quad 13+8=21, \\quad 21+8=29, \\quad 29+8=37, \\;\\dots'}]}},
    {'h4': 'Non-probability sampling'},
    {'p': 'Sampling techniques that are not probabilistic:'},
    {'ul': [
      '**Quota sampling (QS)** — the investigator aims at obtaining some balance among the '
      'different categories of units in the sample (e.g. quota selection of students to '
      'Federal Colleges in Nigeria). + fair representation of categories without a probability '
      'basis; no sampling frame needed. − sampling error cannot be estimated.',
      '**Judgemental sampling (JS)** — sample members are selected in conformity with some '
      'criterion of interest (e.g. interviewing only those with relevant job experience, or a '
      'company trialling a new product with its own employees first). + in-depth insight into '
      'the research topic; targets a group who can give valuable information. − subject to the '
      'researcher\'s bias; leads to a selective sample.',
      '**Convenience sampling (CS)** — units are selected without a prior known chance of '
      'selection, primarily on convenience or ease of access (e.g. a lecturer using her own '
      'students as a sample). + relatively easy selection; easy to collect information; time '
      'and cost efficient. − leads to inaccurate/biased data; introduces sampling bias.',
      '**Snowball sampling (SS)** — used where respondents are not easy to identify; selection '
      'is by recommendation or referral, picking a group who may or may not be in the sample '
      'and having them identify others with similar characteristics, until the required sample '
      'is gathered (e.g. a study of drug use among youths). + increases participation, since it '
      'is based on referral from a trusted member; useful for hard-to-reach populations. − the '
      'sample may not truly represent the population; leads to biased information.',
    ]},
  ]},

  {'n': '1.5', 't': 'Data presentation — text, tables and frequency distributions', 'b': [
    {'p': 'Statistical data is organised and classified into groups before being presented for '
          'analysis. Four important bases of classification:'},
    {'table': {'align': 'll', 'head': ['Basis', 'Meaning'], 'rows': [
      ['**Qualitative**', 'By type or quality of the items under consideration.'],
      ['**Quantitative**', 'By the range specified in quantities.'],
      ['**Chronological (time series)**', 'Monthly or yearly — analysis considers trend, '
       'cyclical, periodic and irregular movements.'],
      ['**Geographical**', 'By location.'],
    ]}},
    {'p': 'Classified data is then presented in one of three ways: **text presentation**, '
          '**tabular presentation** and **diagrammatic presentation** (charts and graphs).'},
    {'h4': 'Text presentation'},
    {'p': 'Texts and figures are combined in a procedure that emphasises the figures being '
          'discussed — for instance: "The populations of science and management students are '
          '3,000 and 5,000 respectively for year 2006 in a Polytechnic in Ghana."'},
    {'h4': 'Tabular presentation'},
    {'p': 'A table is more detailed than text, but brief and self-explanatory. Tables may be '
          '**simple** (one set of items against another, e.g. a dependent against an independent '
          'variable) or **complex** (several items, often showing sub-divisions). Essential '
          'features of a table: a **title** giving adequate information; **headings** '
          'identifying rows and columns; the **source**, i.e. the origin of the figures; and a '
          '**footnote** giving detail on particular figures.'},
    {'eg': {'tag': 'Study text', 't': 'Simple and complex tables', 'open': True, 'q': [
      {'p': 'Classification of 200 Polytechnic students by department (simple table), and the '
            'same 200 students split further by gender (complex table).'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['Department', 'No. of students'], 'rows': [
        ['Accountancy', '60'], ['Business Administration', '50'], ['Marketing', '40'],
        ['Banking/Finance', '50'], ['Total', '200', '@tot'],
      ]}},
      {'table': {'align': 'lrrr', 'head': ['Department', 'Male', 'Female', 'Total'], 'rows': [
        ['Accountancy', '40', '20', '60'], ['Business Administration', '36', '14', '50'],
        ['Marketing', '30', '10', '40'], ['Banking/Finance', '24', '26', '50'],
        ['Total', '130', '70', '200', '@tot'],
      ]}}]}},
    {'h4': 'The frequency table'},
    {'def': {'t': 'Frequency table', 'd': 'a table showing the number of times a value (figure), '
                  'or group of values, has occurred in a given set of data. It can be '
                  '**ungrouped** (each individual value against its frequency) or **grouped** '
                  '(a class interval against its frequency).'}},
    {'eg': {'tag': 'Study text', 't': 'Example 1.3 — an ungrouped frequency table', 'open': True,
      'q': [
      {'p': 'Marks scored by 20 candidates out of 10 in a quiz: 6, 7, 4, 5, 6, 4, 5, 8, 7, 6, 9, '
            '8, 4, 6, 5, 7, 6, 5, 8, 7. Obtain the frequency distribution.'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['Mark', 'No. of candidates'], 'rows': [
        ['4', '3'], ['5', '4'], ['6', '5'], ['7', '4'], ['8', '3'], ['9', '1'],
      ]}}]}},
    {'h4': 'Constructing a grouped frequency table'},
    {'p': 'Guidelines:'},
    {'ol': [
      'the number of classes should not be too few or too many — say 5 to 8;',
      'the class width should be 5, or a multiple of 5, for easy manipulation;',
      'classes should generally be the same width, except open (wider) end classes to '
      'accommodate extreme values;',
      'classes must not overlap — not "5–10, 10–15", which leaves 10 ambiguous — so every '
      'observation has a distinct class;',
      'class intervals could be of the form 1–5, 6–10, 11–20, …; or "10 but less than 20, 20 '
      'but less than 30, …";',
      'open-ended classes (e.g. "less than 20", "10 and above") are assumed to have the same '
      'width as the adjacent class.',
    ]},
    {'p': 'The **tally method** is usually used to construct a frequency table when there are '
          'many observations. A tally is a stroke ($\\vert$) for each occurrence; the fifth '
          'stroke is drawn across the first four ($\\rlap{\\hspace{2pt}\\vert\\vert\\vert\\vert}'
          '{/\\!\\!\\!}$), for easy counting. Its great advantage is that the data is gone '
          'through **only once**, avoiding confusion from re-counting.'},
    {'eg': {'tag': 'Study text', 't': 'Example 1.4 — a grouped frequency table by tally',
      'open': True, 'q': [
      {'p': 'Daily sales (₦\'000) of a supermarket over 40 days: 12, 33, 23, 48, 56, 18, 22, 55, '
            '57, 35, 45, 28, 36, 44, 17, 39, 58, 25, 31, 48, 26, 32, 45, 24, 35, 47, 56, 33, 27, '
            '31, 34, 19, 21, 35, 41, 32, 45, 37, 29, 49. Use classes 11–20, 21–30, … to construct '
            'a frequency table.'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['Class interval', 'Frequency'], 'rows': [
        ['11 – 20', '5'], ['21 – 30', '9'], ['31 – 40', '14'], ['41 – 50', '7'],
        ['51 – 60', '5'], ['Total', '40', '@tot'],
      ]}}]}},
    {'h4': 'Class limits, boundaries, size and mid-point'},
    {'ul': [
      '**Class limits** — the first number in a class is its **lower** limit, the second its '
      '**upper** limit (e.g. for the 3rd class, 31–40: lower limit 31, upper limit 40).',
      '**Class boundaries** — the lower class boundary is the sum of the *upper limit of the '
      'preceding class* and the *lower limit of this class*, divided by 2; the upper class '
      'boundary is the sum of *this class\'s upper limit* and the *lower limit of the '
      'succeeding class*, divided by 2. Consequently, a class\'s lower boundary equals the '
      'upper boundary of the class before it. Class boundaries are used to draw histograms and '
      'ogives.',
      '**Class size (width)** — the difference between a class\'s boundaries. The lower '
      'boundary of the first class and the upper boundary of the last class are obtained by '
      'logic (extending the pattern).',
      '**Class mid-point** — the sum of a class\'s limits, divided by 2. The mid-point of a '
      'class equals the mid-point of the preceding class plus the class width. Class marks '
      '(mid-points) represent class intervals in statistical calculations, and are used to '
      'draw the frequency polygon.',
      '**Cumulative frequency** — the sum of the frequencies of all classes before a particular '
      'class, plus the frequency of that class.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Example — class boundaries, size and mid-point',
      'open': True, 'q': [
      {'p': 'For the sales frequency table above (classes 11–20, 21–30, 31–40, 41–50, 51–60), '
            'find the boundaries of the 2nd class, the width of the 2nd class, and the '
            'mid-point of the 4th class.'}],
      'a': [
      {'p': 'Lower boundary of the 2nd class (21–30) $= \\dfrac{20+21}{2} = 20.5$. Upper '
            'boundary $= \\dfrac{30+31}{2} = 30.5$.'},
      {'p': 'Width of the 2nd class $= 30.5 - 20.5 = 10$.'},
      {'p': 'Mid-point of the 4th class (41–50) $= \\dfrac{41+50}{2} = 45.5$.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 1.5 — a cumulative frequency table', 'open': True,
      'q': [
      {'p': 'Obtain the cumulative frequency table for the sales classes above.'}],
      'a': [
      {'table': {'align': 'lrl', 'head': ['Class interval', 'Frequency', 'Cumulative frequency'],
        'rows': [
        ['11 – 20', '5', '5'], ['21 – 30', '9', '5+9=14'], ['31 – 40', '14', '14+14=28'],
        ['41 – 50', '7', '28+7=35'], ['51 – 60', '5', '35+5=40'],
      ]}}]}},
    {'warn': 'Class **boundaries** (not limits) are used for histograms and ogives; class '
             '**marks** (mid-points) are used for computing the mean and other statistical '
             'measures. Using limits instead of boundaries leaves gaps between histogram bars, '
             'which is wrong for continuous data.'},
  ]},

  {'n': '1.6', 't': 'Diagrammatic presentation — charts', 'b': [
    {'p': 'Diagrams reflect the relationship, trends and comparisons among variables shown on a '
          'table, in the form of **charts** and **graphs**.'},
    {'h4': 'Bar charts'},
    {'p': 'A bar chart represents information with rectangular bars of **equal width**, with '
          'height or length proportional to the value represented. Bars can be plotted '
          'vertically (usually) or horizontally, in four forms:'},
    {'ul': ['Simple bar chart;', 'Component bar chart;', 'Percentage component bar chart; and',
      'Multiple bar chart.']},
    {'eg': {'tag': 'Study text', 't': 'Example 1.6 — simple bar chart', 'open': True, 'q': [
      {'p': 'Draw a simple bar chart for the department table above (Accountancy 60, Business '
            'Administration 50, Marketing 40, Banking/Finance 50).'}],
      'a': [
      {'p': 'A series of bars of the same width, each bar\'s height showing its own '
            'department\'s number of students — 60, 50, 40, 50 — read straight off the y-axis '
            'against each department on the x-axis.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 1.7 — multiple bar chart', 'open': True, 'q': [
      {'p': 'Draw a multiple bar chart for the gender-split department table above.'}],
      'a': [
      {'p': 'Each department shows **two bars side by side** — Male and Female — rather than one '
            'combined bar: Accountancy (40, 20), Business Administration (36, 14), Marketing '
            '(30, 10), Banking/Finance (24, 26).'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 1.8 — component bar chart', 'open': True, 'q': [
      {'p': 'Draw a component bar chart for the same gender-split table.'}],
      'a': [
      {'p': 'Similar to a simple bar chart, but each department\'s single bar has its height '
            '**divided into component parts** — Male stacked on Female — so the total height '
            'still reads as 60, 50, 40, 50.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 1.9 — percentage component bar chart', 'open': True,
      'q': [
      {'p': 'For Accountancy (Male 40, Female 30) and Banking/Finance (Male 20, Female 10), '
            'draw the percentage component bar chart.'}],
      'a': [
      {'table': {'align': 'lrrrr',
        'head': ['', 'Accountancy', '%', 'Banking/Finance', '%'], 'rows': [
        ['Male', '40', '57%', '20', '67%'], ['Female', '30', '43%', '10', '33%'],
        ['Total', '70', '100%', '30', '100%', '@tot'],
      ]}},
      {'p': 'Every bar is drawn to the **same height (100%)**; each department\'s bar is split '
            'into the percentage each gender represents *within that department* — so the two '
            'bars are the same height even though the underlying totals (70 vs 30) differ.'}]}},
  ]},

  {'n': '1.7', 't': 'Diagrammatic presentation — the pie chart', 'b': [
    {'def': {'t': 'Pie chart', 'd': 'a circular chart divided into sectors, each sectorial angle '
                  'representing its part, in degrees.'}},
    {'tex': '\\theta = \\frac{\\text{component}}{\\text{total}} \\times 360^\\circ'},
    {'eg': {'tag': 'Study text', 't': 'Example 1.10 — pie chart angles', 'open': True, 'q': [
      {'p': 'Draw a pie chart for the department table (Accountancy 60, Business Administration '
            '50, Marketing 40, Banking/Finance 50; total 200 students).'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['Department', 'Angle'], 'rows': [
        ['Accountancy', '$60/200 \\times 360 = 108°$'],
        ['Business Administration', '$50/200 \\times 360 = 90°$'],
        ['Marketing', '$40/200 \\times 360 = 72°$'],
        ['Banking/Finance', '$50/200 \\times 360 = 90°$'],
        ['Check', '$108+90+72+90=360°$', '@tot'],
      ]}}]}},
  ]},

  {'n': '1.8', 't': 'Graphs — histogram, frequency polygon and ogive', 'b': [
    {'p': 'A graph shows the relationship between variables by a curve or straight line — for '
          'example, output against cost, or sales against time. The graphs typically used in '
          'business are the **histogram**, the **frequency polygon** and the cumulative '
          'frequency curve (**ogive**).'},
    {'h4': 'Histogram'},
    {'p': 'Rectangles drawn to represent a grouped frequency distribution — similar to a bar '
          'chart, but the rectangles **touch** each other (continuous), and the **frequency of a '
          'class is represented by the area** of its rectangle, not its height as in a bar '
          'chart. Since the rectangles must be continuous, class intervals are written using '
          'their **class boundaries**.'},
    {'p': 'If class sizes are unequal, adjust: choose the size common to most classes, then '
          'divide each other frequency by (its own class width $\\div$ the common width) — e.g. '
          'if a class is double the common width, its frequency is divided by 2.'},
    {'eg': {'tag': 'Study text', 't': 'Example 1.11 — histogram', 'open': True, 'q': [
      {'p': 'Draw the histogram for the sales frequency table (boundaries 10.5–20.5, 20.5–30.5, '
            '30.5–40.5, 40.5–50.5, 50.5–60.5; frequencies 5, 9, 14, 7, 5).'}],
      'a': [
      {'p': 'Five touching rectangles over the class boundaries, with heights (since the widths '
            'are all equal, height is proportional to frequency here) of 5, 9, 14, 7, 5 — the '
            'tallest rectangle, over 30.5–40.5, can be used to **estimate the modal value**.'}]}},
    {'h4': 'Frequency polygon'},
    {'p': 'The graph of frequencies against **class marks**. If the histogram has been drawn, '
          'the polygon is obtained by joining the mid-points of the top of each rectangle. It is '
          '**closed** by joining to the class mark of the (empty) class before the first, and '
          'after the last, both with zero frequency.'},
    {'eg': {'tag': 'Study text', 't': 'Example 1.12 — frequency polygon', 'open': True, 'q': [
      {'p': 'Draw the frequency polygon for the same sales table.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['Class interval', 'Class mark', 'Frequency'], 'rows': [
        ['1 – 10', '5.5', '0'], ['11 – 20', '15.5', '5'], ['21 – 30', '25.5', '9'],
        ['31 – 40', '35.5', '14'], ['41 – 50', '45.5', '7'], ['51 – 60', '55.5', '5'],
        ['61 – 70', '65.5', '0'],
      ]}},
      {'note': 'Joined with straight edges, then smoothed, the polygon becomes a **frequency '
               'curve**, showing the shape of the distribution.'}]}},
    {'h4': 'Ogive (cumulative frequency curve)'},
    {'p': 'A graph of cumulative frequency against **class boundaries** — either **"less than"** '
          'or **"more than"** type. "Or equal to" is understood and usually hidden, so only '
          '"less than" is written.'},
    {'eg': {'tag': 'Study text', 't': 'Example 1.13 — the "less than" ogive', 'open': True,
      'q': [
      {'p': 'Draw the "less than" ogive for the sales table.'}],
      'a': [
      {'table': {'align': 'lr', 'head': ['Less than (or equal to)', 'Cumulative frequency'],
        'rows': [
        ['10.5', '0'], ['20.5', '5'], ['30.5', '14'], ['40.5', '28'], ['50.5', '35'],
        ['60.5', '40'],
      ]}},
      {'note': 'No value is less than 10.5 (the upper boundary of the class before the first), '
               'hence cumulative frequency 0; no value exceeds 60.5, hence the cumulative '
               'frequency of 40 — the grand total. The ogive can be used to estimate the '
               '**median, quartiles, deciles and percentiles**.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 1.14 — the "more than" ogive', 'open': True,
      'q': [
      {'p': 'Using the same sales data, construct a "more than" ogive.'}],
      'a': [
      {'table': {'align': 'lrr', 'head': ['Class boundary', 'Frequency', 'Cumulative frequency'],
        'rows': [
        ['More than 10.5', '5', '40'], ['More than 20.5', '9', '35'],
        ['More than 30.5', '14', '26'], ['More than 40.5', '7', '12'],
        ['More than 50.5', '5', '5'],
      ]}},
      {'p': '"Less than" and "more than" cumulate from the top and bottom respectively; "less '
            'than" figures attach to **upper** class boundaries, "more than" figures attach to '
            '**lower** class boundaries.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 1.15 — where the two ogives cross', 'open': True,
      'q': [
      {'p': 'Marks of accounting students in Quantitative Analysis: classes 0–10 to 90–100 in '
            'tens, frequencies 5, 10, 15, 20, 25, 10, 5, 4, 3, 3 (total 100). Draw both ogives on '
            'one axis and comment.'}],
      'a': [
      {'p': 'Building "less than" (cumulating from 5 up to 100) and "more than" (cumulating '
            'from 100 down to 3) tables and plotting both on the same axes, the two curves '
            '**intersect at class boundary 40, cumulative frequency 50** — the intersection '
            'means the **median value is 40**.'}]}},
  ]},

  {'n': '1.9', 't': 'Statistical application packages', 'b': [
    {'p': 'Two statistical application packages are commonly used for data presentation and '
          'analysis: **Microsoft Excel** and the **Statistical Package for the Social Sciences '
          '(SPSS)**. Good knowledge of both statistics and computing is needed to interpret '
          'them; each uses the speed, efficiency and accuracy of the computer.'},
    {'h4': 'Microsoft Excel'},
    {'p': 'A spreadsheet developed by Microsoft, for Windows, Android, macOS and iOS — often '
          'called simply "Excel". It has graphic tools, pivot tables, calculation functions and '
          'Visual Basic for Applications (a programming language), and ships as part of '
          'Microsoft Office. It has built-in functions for engineering, statistical and '
          'financial questions, a data analysis tool pack, and displays data as tables, charts '
          'and graphics.'},
    {'h4': 'SPSS'},
    {'p': 'SPSS stands for **Statistical Package for the Social Sciences**, a set of programs for '
          'presenting, manipulating and analysing data sets. Originally developed by SPSS Inc. '
          'for social-science researchers (psychology, sociology), it is now owned by IBM and '
          'known as **IBM SPSS Statistics**, and its use has expanded to other fields. Unlike '
          'Excel, SPSS must be installed separately. It has four windows: **data editor** (with '
          '*data view* and *variable view*), **output**, **syntax** and **script** — the data '
          'editor and output windows matter most for data analysis. The data view shows the '
          'actual data and variables entered; the variable view holds each variable\'s '
          'definition/label; the output window shows the results of an analysis.'},
  ]},

  {'n': '1.10', 't': 'Worksheet summary — definitions and every formula', 'b': [
    {'p': 'Everything in this chapter, compressed for a last read-through.'},
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§1.1 Introduction** — data/statistical data is raw fact, numeric or non-numeric, '
      'collected/analysed/summarised. Statistics splits into **descriptive** (summarising a '
      'data set) and **inferential** (using a sample to learn about the population).',
      '**§1.2 Classification** — numeric (**discrete**: whole numbers only; **continuous**: '
      'any value) vs non-numeric (**categorical/nominal**: unordered groups; **ordinal**: '
      'ranked). Separately, **primary** (first-hand, for this enquiry) vs **secondary** '
      '(already collected by someone else) — with named secondary-data agencies (NBS, CBN, '
      'educational institutions, ministries, private companies).',
      '**§1.3 Collecting primary data** — the **mail questionnaire** (close/open-ended '
      'questions; the six qualities of a good one); the **interview method**, by schedule, '
      'telephone or group discussion (a schedule is filled by the *investigator*, a '
      'questionnaire by the *respondent*); and **observation** (controlled or uncontrolled).',
      '**§1.4 Sampling** — population/sample/census/sampling frame/sampling unit; notation '
      '$f=n/N$, $g=N/n$; five reasons to sample. **Probability** methods (known selection '
      'chance): simple random, systematic ($k=N/n$), stratified (homogeneous strata), cluster '
      '(whole natural/artificial clusters), multi-stage. **Non-probability** methods (unknown '
      'chance, error not estimable): quota, judgemental, convenience, snowball.',
      '**§1.5 Presenting data** — four classification bases (qualitative, quantitative, '
      'chronological, geographical); text/tabular/diagrammatic presentation; simple vs complex '
      'tables; ungrouped vs grouped frequency tables (5–8 classes, width a multiple of 5, no '
      'overlapping limits); the tally method; class limits vs the **averaging-based** class '
      'boundaries, class width, mid-point, and cumulative frequency.',
      '**§1.6–1.8 Charts and graphs** — four bar-chart forms (simple, multiple, component, '
      'percentage component); the pie chart (angle $=$ component/total $\\times 360°$); the '
      'histogram (touching bars over boundaries, **area** $=$ frequency, adjust for unequal '
      'widths); the frequency polygon (class marks, closed at zero-frequency ends); the ogive '
      '("less than" on upper boundaries, "more than" on lower boundaries — where they cross '
      'gives the **median**).',
      '**§1.9 Software** — Excel (built into Office, in-built functions, data analysis tool '
      'pack) and SPSS (installed separately; data editor/output/syntax/script windows; owned '
      'by IBM).',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Data / statistical data** — raw facts, numeric or non-numeric, collected, analysed and '
      'summarised for presentation and interpretation.',
      '**Statistics** — the scientific method of collecting, presenting, analysing and '
      'interpreting data, and making inferences under uncertainty.',
      '**Descriptive statistics** — summarises a data set. **Inferential statistics** — uses a '
      'sample to draw conclusions about a population.',
      '**Population** — items sharing a defined characteristic; **finite** (countable) or '
      '**infinite** (uncountable).',
      '**Sample** — a fractional part of a population, studied to make a statement about the '
      'whole. **Census** — complete enumeration of every unit. **Sample survey** — collecting '
      'information via a representative sample.',
      '**Sampling frame** — a list of all units in the target population. **Sampling unit** — '
      'any individual member.',
      '**Questionnaire** — filled by the *respondent*. **Schedule** — filled by the '
      '*investigator/interviewer*.',
      '**Class limits** — the numbers as written. **Class boundaries** — the true limits, from '
      'averaging adjacent class limits. **Class size/width** — the difference between the '
      'boundaries. **Class mid-point (mark)** — the average of a class\'s limits.',
      '**Frequency table** — how often each value (or class) occurs; **ungrouped** or '
      '**grouped**. **Cumulative frequency** — the running total up to and including a class.',
    ]},
    {'h3': 'A. Sampling formulae'},
    {'fbox': {'h': 'Sampling', 'rows': [
      {'lb': 'Sampling fraction', 'tex': 'f = \\dfrac{n}{N}'},
      {'lb': 'Expansion (raising) factor', 'tex': 'g = \\dfrac{N}{n}'},
      {'lb': 'Systematic sampling interval', 'tex': 'k = \\dfrac{N}{n}'},
    ]}},
    {'h3': 'B. Class-boundary and presentation formulae'},
    {'fbox': {'h': 'Frequency tables and charts', 'rows': [
      {'lb': 'Lower class boundary',
       'tex': '\\dfrac{\\text{upper limit of previous class} + \\text{lower limit of this '
              'class}}{2}'},
      {'lb': 'Upper class boundary',
       'tex': '\\dfrac{\\text{upper limit of this class} + \\text{lower limit of next class}}{2}'},
      {'lb': 'Class mid-point (mark)',
       'tex': 'x = \\dfrac{\\text{Lower limit} + \\text{Upper limit}}{2}'},
      {'lb': 'Frequency-density adjustment (unequal widths)',
       'tex': '\\text{Adjusted frequency} = \\text{frequency} \\times '
              '\\dfrac{\\text{common width}}{\\text{this class\'s width}}'},
      {'lb': 'Pie chart sector angle',
       'tex': '\\theta = \\dfrac{\\text{component}}{\\text{total}} \\times 360^\\circ'},
    ]}},
  ]},

  {'n': '1.11', 't': 'End-of-chapter questions (study text)', 'b': [
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
  {'lb': 'Sampling fraction', 'tex': 'f = \\frac{n}{N}'},
  {'lb': 'Expansion (raising) factor', 'tex': 'g = \\frac{N}{n}'},
  {'lb': 'Systematic sampling interval', 'tex': 'k = \\frac{N}{n}'},
  {'lb': 'Lower class boundary',
   'tex': '\\frac{\\text{upper limit of previous class} + \\text{lower limit of this class}}{2}'},
  {'lb': 'Class mid-point (mark)',
   'tex': 'x = \\frac{\\text{Lower limit} + \\text{Upper limit}}{2}'},
  {'lb': 'Frequency-density adjustment',
   'tex': '\\text{Adjusted frequency} = f \\times \\frac{\\text{common width}}{\\text{class width}}'},
  {'lb': 'Pie chart sector angle',
   'tex': '\\theta = \\frac{\\text{component}}{\\text{total}} \\times 360^\\circ'},
 ],
 'focus':
   'Two or three Section A marks every diet, on definitions rather than computation: which is a '
   'probability sampling design, what an ogive can and cannot estimate, what SPSS stands for, '
   'primary versus secondary data, and the schedule/questionnaire distinction. Learn the '
   'probability and non-probability sampling lists with one distinguishing sentence each. The '
   'grouped frequency table built here, with its class boundaries and marks, is the input to '
   'Chapters 2 and 3.',
 'errors': [
   'Using class limits instead of boundaries when drawing a histogram.',
   'Plotting an ogive against class marks instead of class boundaries.',
   'Calling quota sampling a probability (random) method.',
   'Forgetting the frequency-density adjustment when class widths are unequal.',
   'Trying to read the mode from an ogive — it comes from the histogram instead.',
   'Confusing a schedule (filled by the interviewer) with a questionnaire (filled by the '
   'respondent).',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A table showing the number of times a value or group of values occurs in a set of data '
         'is called a',
    'o': ['frequency table', 'contingency table', 'probability table', 'times table',
          'four-figure table'],
    'a': 0,
    'w': 'That is the definition of a frequency table or frequency distribution.',
    'src': 'Chapter 1.5', 'sec': '1.5'},
   {'q': 'The ogive can be used to estimate all of the following EXCEPT the',
    'o': ['median', 'quartiles', 'deciles', 'percentiles', 'mode'],
    'a': 4,
    'w': 'An ogive is a cumulative frequency curve, so it gives every measure of **position** — '
         'median, quartiles, deciles, percentiles. The mode is read from a histogram instead.',
    'src': 'Chapter 1.8', 'sec': '1.8'},
   {'q': 'SPSS stands for',
    'o': ['Standard Program for Statistical Sampling',
          'Statistical Package for the Social Sciences',
          'Systematic Procedure for Sample Selection',
          'Statistical Presentation and Sampling System',
          'Structured Package for Scientific Statistics'],
    'a': 1,
    'w': 'Statistical Package for the Social Sciences — now IBM SPSS Statistics.',
    'src': 'Chapter 1.9', 'sec': '1.9'},
   {'q': 'Which of the following is NOT a probability sampling method?',
    'o': ['Simple random sampling', 'Stratified sampling', 'Cluster sampling', 'Quota sampling',
          'Systematic sampling'],
    'a': 3,
    'w': 'In quota sampling the interviewer chooses whom to approach within each quota, so the '
         'probability of any individual being selected is unknown — that is what makes it '
         'non-probability sampling.',
    'src': 'Chapter 1.4', 'sec': '1.4'},
   {'q': 'For the class interval 21 – 30, immediately preceded by 11 – 20, the lower class '
         'boundary is',
    'o': ['21', '20.5', '20', '19.5', '30.5'],
    'a': 1,
    'w': 'Lower boundary $= \\dfrac{\\text{upper limit of previous class}+\\text{lower limit of '
         'this class}}{2} = \\dfrac{20+21}{2} = 20.5$.',
    'src': 'Chapter 1.5', 'sec': '1.5'},
   {'q': 'A population of 3,600 is to be sampled systematically with a sample size of 90. The '
         'sampling interval is',
    'o': ['30', '40', '45', '36', '90'],
    'a': 1,
    'w': 'The interval is population size divided by sample size.',
    'calc': 'k = \\frac{3600}{90} = 40',
    'src': 'Chapter 1.4', 'sec': '1.4'},
   {'q': 'The first and last points on a frequency polygon have',
    'o': ['zero frequencies', 'cumulative frequencies', 'high frequencies', 'low frequencies',
          'undefined frequencies'],
    'a': 0,
    'w': 'The polygon is closed by extending it to the class marks of the empty classes '
         'immediately before the first and after the last, where the frequency is zero.',
    'src': 'Chapter 1.8', 'sec': '1.8'},
   {'q': 'Breaking a heterogeneous population into a number of homogeneous, non-overlapping '
         'groups before sampling each by simple random sampling is called',
    'o': ['cluster sampling', 'stratification', 'quota sampling', 'systematic sampling',
          'multi-stage sampling'],
    'a': 1,
    'w': 'Each homogeneous group is a stratum; the technique is stratified sampling, and the '
         'act of forming the strata is stratification.',
    'src': 'Chapter 1.4', 'sec': '1.4'},
   {'q': 'In statistics, a schedule is a set of questions that is completed by the',
    'o': ['respondent, unaided', 'investigator or interviewer', 'supervisor after the interview',
          'data-entry clerk', 'head of the statistics office'],
    'a': 1,
    'w': 'A schedule is filled in by the investigator as they put the questions; a '
         'questionnaire is filled in by the respondent.',
    'src': 'Chapter 1.3', 'sec': '1.3'},
   {'q': 'A list containing every unit in the target population, used as the basis for selecting '
         'a sample, is called the',
    'o': ['sampling unit', 'sampling frame', 'sampling fraction', 'census', 'population'],
    'a': 1,
    'w': 'The sampling frame is the list; a sampling unit is one member of it; the sampling '
         'fraction is $n/N$.',
    'src': 'Chapter 1.4', 'sec': '1.4'},
  ],
  'theory': [
   {'q': 'Distinguish between primary and secondary data, and describe the THREE methods of '
         'collecting primary data set out in this chapter, giving one advantage and one '
         'disadvantage of each.',
    'marks': 10,
    'a': [
      {'p': '**Primary data** is obtained by direct collection from respondents or informants, '
            'specifically for the enquiry in hand. **Secondary data** is obtained, collected or '
            'extracted from already-existing records or sources, collected originally for '
            'another purpose.'},
      {'table': {'head': ['Method', 'Advantage', 'Disadvantage'], 'align': 'lll', 'rows': [
        ['**Mail questionnaire**', 'Wide area covered; cheap; saves time',
         'Postal services unreliable; non-response; unreliable answers'],
        ['**Interview** (schedule/telephone/group)', 'Detailed, accurate, reliable',
         'Time-consuming; expensive'],
        ['**Observation**', 'Records behaviour directly, free of respondent bias',
         'Limited to what can be observed; cannot capture reasons or attitudes'],
      ]}}],
    'src': 'Chapter 1.3', 'sec': '1.3'},
  ]},
}
