CH = {
 'n': 18,
 't': 'Replacement Analysis',
 'brief': 'When to replace an asset whose running costs rise and resale value falls, and '
          'whether to replace items that fail suddenly individually or in groups.',
 'outcomes': [
   'Distinguish gradual deterioration from sudden failure',
   'Compute the average annual cost of ownership for each possible replacement age',
   'Identify the optimal replacement period for an item that deteriorates',
   'Build a mortality table and project failures period by period',
   'Compare individual and group replacement policies on a cost-per-period basis',
 ],
 'secs': [
  {'n': '18.1', 't': 'The two replacement problems', 'b': [
    {'table': {'align': 'lll', 'head': ['', 'Gradual deterioration', 'Sudden failure'], 'rows': [
      ['Nature', 'Efficiency declines steadily; running costs rise and resale value falls',
       'The item works perfectly, then fails without warning'],
      ['Examples', 'Vehicles, plant, machinery, computers',
       'Light bulbs, fuses, small electronic components, bearings'],
      ['Decision', 'At what **age** to replace the single asset',
       'Whether to replace items **individually on failure** or **all together** at intervals'],
      ['Method', 'Minimise average annual cost of ownership',
       'Compare cost per period of the two policies'],
    ]}},
    {'p': 'In both cases the underlying trade-off is the same: replacing too soon wastes '
          'remaining useful life, and replacing too late incurs excessive running or failure '
          'costs. The optimum is where the total cost per period of use is least.'},
  ]},

  {'n': '18.2', 't': 'Items that deteriorate', 'b': [
    {'fbox': {'h': 'Average annual cost of ownership', 'rows': [
      {'lb': 'Capital cost over $n$ years',
       'tex': 'C - S_n'},
      {'lb': 'Total cost of owning for $n$ years',
       'tex': 'TC_n = (C - S_n) + \\sum_{t=1}^{n} R_t'},
      {'lb': 'Average annual cost',
       'tex': 'AAC_n = \\frac{(C - S_n) + \\sum_{t=1}^{n} R_t}{n}'},
    ]}},
    {'p': 'where $C$ is the purchase cost, $S_n$ the resale (scrap) value at the end of year '
          '$n$, and $R_t$ the running cost in year $t$. Replace at the age $n$ that minimises '
          '$AAC_n$.'},
    {'key': 'Capital cost per year **falls** as the asset is kept longer, because the initial '
            'outlay is spread over more years. Running cost per year **rises**. The average '
            'annual cost is therefore U-shaped, and the optimum is the bottom of the U.'},
    {'eg': {'t': 'Optimal replacement age', 'q': [
      {'p': 'A machine costs ₦100,000. Its running costs and resale values are:'},
      {'table': {'align': 'lrr',
        'head': ['Year', 'Running cost (₦)', 'Resale value at end of year (₦)'], 'rows': [
        ['1', '30,000', '60,000'],
        ['2', '35,000', '40,000'],
        ['3', '42,000', '25,000'],
        ['4', '52,000', '15,000'],
        ['5', '65,000', '10,000'],
      ]}},
      {'p': 'Determine when the machine should be replaced.'}],
      'a': [
      {'p': 'For each possible replacement age, add the capital cost (purchase price less '
            'resale value at that age) to the cumulative running costs, and divide by the '
            'number of years of use.'},
      {'table': {'align': 'lrrrrr',
        'head': ['Replace at end of year', 'Cumulative running cost (₦)',
                 'Capital cost $100{,}000 - S_n$ (₦)', 'Total cost (₦)',
                 'Years', 'Average annual cost (₦)'], 'rows': [
        ['1', '30,000', '40,000', '70,000', '1', '70,000'],
        ['2', '65,000', '60,000', '125,000', '2', '62,500'],
        ['3', '107,000', '75,000', '182,000', '3', '**60,667**'],
        ['4', '159,000', '85,000', '244,000', '4', '61,000'],
        ['5', '224,000', '90,000', '314,000', '5', '62,800'],
      ]}},
      {'p': 'The average annual cost is lowest at the end of **year 3**, at ₦60,667. The '
            'machine should therefore be replaced every **three years**.'},
      {'note': 'Notice how flat the bottom of the curve is: years 3, 4 and 5 differ by only '
               '₦2,133 a year on an outlay of ₦100,000. Where the optimum is this flat, a '
               'decision to keep the machine an extra year for operational reasons costs '
               'little, and the answer should say so. What the table does establish firmly is '
               'that replacing after one or two years is expensive.'},
      {'warn': 'The basic model ignores the time value of money. Where the asset\'s life is '
               'long or interest rates are high, the correct approach is to discount each '
               'year\'s cash flows and compare the **equivalent annual cost** — the net present '
               'value of one replacement cycle divided by the annuity factor for that number '
               'of years. Say so if the question mentions a cost of capital.'}]}},
  ]},

  {'n': '18.3', 't': 'Items that fail suddenly', 'b': [
    {'p': 'Where items fail without warning, two policies are possible. Under **individual '
          'replacement** each item is replaced as it fails. Under **group replacement** all '
          'items are replaced at fixed intervals, with individual replacement of any that fail '
          'in between. Group replacement is cheaper per item — the labour of a single organised '
          'operation is far less than that of many separate call-outs — but wastes the '
          'remaining life of items that had not yet failed.'},
    {'fbox': {'h': 'Group replacement', 'rows': [
      {'lb': 'Failures in period $t$',
       'tex': 'N_t = \\sum_{k=1}^{t} N_{t-k}\\, p_k'},
      {'lb': 'Mean life of an item',
       'tex': '\\bar{L} = \\sum t \\, p_t'},
      {'lb': 'Steady-state failures per period (individual policy)',
       'tex': '\\frac{N}{\\bar{L}}'},
      {'lb': 'Cost per period, group replacement at $n$',
       'tex': '\\frac{N C_g + C_i \\sum_{t=1}^{n} N_t}{n}'},
    ]}},
    {'p': 'where $N$ is the number of items installed, $p_t$ the probability that an item fails '
          'in period $t$ of its life, $C_g$ the group replacement cost per item and $C_i$ the '
          'individual replacement cost per item.'},
    {'eg': {'t': 'Individual against group replacement', 'q': [
      {'p': 'A factory has 1,000 electric bulbs in use. The probability of a bulb failing in '
            'each week of its life is: week 1, 0.10; week 2, 0.25; week 3, 0.40; week 4, 0.25. '
            'Replacing a bulb individually as it fails costs ₦60; replacing all bulbs together '
            'costs ₦20 per bulb. Determine the optimal policy.'}],
      'a': [
      {'h4': 'Step 1 — project the failures'},
      {'p': 'Bulbs that replace failed bulbs are themselves subject to the same failure '
            'pattern, so failures in later weeks include failures among the replacements:'},
      {'tex': 'N_1 = 1{,}000(0.10) = 100'},
      {'tex': 'N_2 = 1{,}000(0.25) + 100(0.10) = 250 + 10 = 260'},
      {'tex': 'N_3 = 1{,}000(0.40) + 100(0.25) + 260(0.10) = 400 + 25 + 26 = 451'},
      {'tex': 'N_4 = 1{,}000(0.25) + 100(0.40) + 260(0.25) + 451(0.10) = 250 + 40 + 65 + 45 '
              '= 400'},
      {'h4': 'Step 2 — cost of the individual policy'},
      {'p': 'In the long run the number of failures per week settles down to the number of '
            'bulbs divided by their mean life:'},
      {'tex': '\\bar{L} = 1(0.10) + 2(0.25) + 3(0.40) + 4(0.25) = 0.10 + 0.50 + 1.20 + 1.00 '
              '= 2.80 \\text{ weeks}'},
      {'tex': '\\text{Failures per week} = \\frac{1{,}000}{2.80} = 357.14'},
      {'tex': '\\text{Cost per week} = 357.14 \\times ₦60 = ₦21{,}428.57'},
      {'h4': 'Step 3 — cost of group replacement at various intervals'},
      {'p': 'The group operation costs $1{,}000 \\times ₦20 = ₦20{,}000$, and any bulbs failing '
            'within the interval are replaced individually at ₦60:'},
      {'table': {'align': 'lrrrrr',
        'head': ['Replace all at end of week', 'Cumulative individual failures',
                 'Individual cost at ₦60 (₦)', 'Group cost (₦)', 'Total (₦)',
                 'Cost per week (₦)'], 'rows': [
        ['1', '100', '6,000', '20,000', '26,000', '26,000'],
        ['2', '360', '21,600', '20,000', '41,600', '**20,800**'],
        ['3', '811', '48,660', '20,000', '68,660', '22,887'],
        ['4', '1,211', '72,660', '20,000', '92,660', '23,165'],
      ]}},
      {'h4': 'Decision'},
      {'p': 'The cheapest group interval is **every two weeks**, at ₦20,800 per week. This is '
            'below the individual-replacement cost of ₦21,428.57 per week, so the factory '
            'should **replace all 1,000 bulbs every two weeks**, replacing individual failures '
            'as they occur in the meantime. The saving is about ₦628 a week, or roughly '
            '₦32,700 a year.'},
      {'note': 'The saving is small — under 3% — so the non-financial factors matter here. '
               'Group replacement can be scheduled outside working hours and gives more '
               'predictable lighting, which favours it; against that it consumes bulbs with '
               'life remaining. Where the margin is this thin, say so rather than presenting '
               'the arithmetic as decisive.'},
      {'warn': 'Two arithmetic traps. First, the failure projection must include failures '
               '**among the replacements** — omitting them understates $N_3$ and $N_4$ badly. '
               'Second, the mean life is a weighted average using the failure probabilities, '
               'not the simple average of 1, 2, 3 and 4.'}]}},
  ]},

  {'n': '18.4', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'All the terms'},
    {'ul': [
      '**Replacement analysis** — deciding *when* to replace equipment to minimise total '
      'cost.',
      '**Items that deteriorate** — efficiency falls and running / maintenance cost rises '
      'gradually with age (a vehicle, a machine); replaced *individually*.',
      '**Items that fail suddenly** — work at full efficiency then fail without warning '
      '(bulbs, tubes); replaced *individually on failure* or by *group replacement*.',
      '**Capital / purchase cost $C$** — the cost of a new item.',
      '**Scrap / salvage / resale value $S_n$** — what the old item fetches after $n$ years.',
      '**Running / maintenance cost $R_t$** — cost of operating the item in year $t$; an '
      'increasing function of age.',
      '**Average annual cost (AAC / ATC)** — total cost of ownership over $n$ years divided '
      'by $n$; replace at the $n$ that minimises it.',
      '**Time value of money** — where the interest rate is not zero, costs are discounted; '
      'otherwise ignored.',
      '**Discount factor** — $d = \\dfrac{1}{1 + r}$ (or $(1+r)^{-t}$).',
      '**Mortality (survival) table** — the probability $p_t$ that an item fails in period '
      '$t$.',
      '**Individual replacement policy** — replace each item as it fails, at cost $C_i$ each.',
      '**Group replacement policy** — replace *all* items every $n$ periods at low unit cost '
      '$C_g$, plus replace failures individually in between.',
    ]},
    {'h3': 'A. Items that deteriorate — no discounting'},
    {'fbox': {'h': 'Optimal replacement age', 'rows': [
      {'lb': 'Total cost of owning for $n$ years',
       'tex': 'TC(n) = (C - S_n) + \\sum_{t=1}^{n} R_t'},
      {'lb': 'Average annual cost',
       'tex': 'AAC(n) = \\dfrac{(C - S_n) + \\sum_{t=1}^{n} R_t}{n}'},
      {'lb': 'Rule', 'tex': '\\text{replace at the } n \\text{ that minimises } AAC(n)'},
    ]}},
    {'h3': 'B. Items that deteriorate — with discounting'},
    {'fbox': {'h': 'Discounted cost', 'rows': [
      {'lb': 'Discount factor', 'tex': 'd = \\dfrac{1}{1 + r}'},
      {'lb': 'Present value of the cost pattern over $n$ years',
       'tex': 'PV(n) = C + \\sum_{t=1}^{n} R_t\\,d^{\\,t} - S_n\\,d^{\\,n}'},
      {'lb': 'Equivalent annual cost',
       'tex': 'EAC = \\dfrac{PV \\text{ of one replacement cycle}}{\\text{annuity factor for } '
              'n \\text{ years}}'},
      {'lb': 'Rule', 'tex': '\\text{choose the machine / age with the lowest EAC}'},
    ]}},
    {'h3': 'C. Items that fail suddenly'},
    {'fbox': {'h': 'Failure projection and group replacement', 'rows': [
      {'lb': 'Mean life', 'tex': '\\bar{L} = \\sum_{t} t\\,p_t'},
      {'lb': 'Steady-state failures per period', 'tex': '\\dfrac{N}{\\bar{L}}'},
      {'lb': 'Failures in period $t$ (include failures among replacements)',
       'tex': 'N_t = \\sum_{k=1}^{t} N_{t-k}\\,p_k \\qquad (N_0 = N)'},
      {'lb': 'Cost per period — individual replacement only',
       'tex': '\\dfrac{N}{\\bar{L}} \\times C_i'},
      {'lb': 'Cost per period — group replacement every $n$ periods',
       'tex': '\\dfrac{N\\,C_g + C_i \\sum_{t=1}^{n-1} N_t}{n}'},
      {'lb': 'Rule',
       'tex': '\\text{group-replace at the } n \\text{ giving the lowest cost per period, if '
              'below the individual-only cost}'},
    ]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Total cost of ownership over $n$ years',
   'tex': 'TC(n) = (C - S_n) + \\sum_{t=1}^{n} R_t'},
  {'lb': 'Average annual cost of ownership',
   'tex': 'AAC_n = \\frac{(C - S_n) + \\sum_{t=1}^{n} R_t}{n}'},
  {'lb': 'Discount factor', 'tex': 'd = \\frac{1}{1 + r}'},
  {'lb': 'PV of a replacement cycle',
   'tex': 'PV(n) = C + \\sum_{t=1}^{n} R_t\\,d^{\\,t} - S_n\\,d^{\\,n}'},
  {'lb': 'Mean life from a failure distribution',
   'tex': '\\bar{L} = \\sum t\\,p_t'},
  {'lb': 'Cost per period, individual replacement only',
   'tex': '\\frac{N}{\\bar{L}}\\,C_i'},
  {'lb': 'Steady-state failures per period',
   'tex': '\\frac{N}{\\bar{L}}'},
  {'lb': 'Failures in period $t$',
   'tex': 'N_t = \\sum_{k=1}^{t} N_{t-k}\\,p_k'},
  {'lb': 'Cost per period, group replacement at $n$',
   'tex': '\\frac{N C_g + C_i \\sum N_t}{n}'},
  {'lb': 'Equivalent annual cost (with discounting)',
   'tex': 'EAC = \\frac{NPV \\text{ of one cycle}}{\\text{Annuity factor}}'},
 ],
 'focus':
   'Appears in Section B in perhaps one diet in three, and almost always as the deterioration '
   'model, which is a straightforward table. The group replacement question is harder and less '
   'common, but the failure-projection recursion is the only real difficulty in it. Set the '
   'work out as a table with a column for each element of cost — examiners award marks column '
   'by column.',
 'errors': [
   'Dividing total cost by the wrong number of years.',
   'Deducting resale value from running costs instead of from purchase cost.',
   'Using the running cost of the final year alone instead of the cumulative running cost.',
   'Omitting failures among replacement items when projecting sudden failures.',
   'Taking the simple average of the periods as the mean life instead of the '
   'probability-weighted average.',
   'Comparing a group policy total cost with an individual policy cost per week — both must be '
   'expressed per period.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'An asset should be replaced at the age at which',
    'o': ['its resale value is highest', 'its average annual cost of ownership is lowest',
          'its running cost first exceeds its resale value',
          'it is fully depreciated in the accounts', 'its running cost is lowest'],
    'a': 1,
    'w': 'The criterion is the total cost per year of use, combining falling capital cost per '
         'year with rising running cost. Accounting depreciation is irrelevant to the '
         'decision.',
    'src': 'Chapter 18.2'},
   {'q': 'A machine costs ₦80,000 and has a resale value of ₦30,000 after 2 years. Running '
         'costs are ₦20,000 in year 1 and ₦26,000 in year 2. The average annual cost of '
         'replacing after 2 years is',
    'o': ['₦38,000', '₦48,000', '₦53,000', '₦96,000', '₦23,000'],
    'a': 1,
    'w': 'Capital cost is $80{,}000 - 30{,}000 = ₦50{,}000$; cumulative running cost is '
         '₦46,000; divide the total by 2 years.',
    'calc': 'AAC_2 = \\frac{50{,}000 + 46{,}000}{2} = \\frac{96{,}000}{2} = ₦48{,}000',
    'src': 'Chapter 18.2'},
   {'q': 'If items fail with probabilities 0.2, 0.3 and 0.5 in the first, second and third '
         'months of life, the mean life of an item is',
    'o': ['2.00 months', '2.30 months', '2.50 months', '3.00 months', '1.00 month'],
    'a': 1,
    'w': 'Weight each period by its probability of failure.',
    'calc': '\\bar{L} = 1(0.2) + 2(0.3) + 3(0.5) = 0.2 + 0.6 + 1.5 = 2.3',
    'src': 'Chapter 18.3'},
   {'q': 'Group replacement is likely to be preferred to individual replacement when',
    'o': ['items are expensive to buy', 'the cost of replacing an item individually greatly '
          'exceeds the cost of replacing it as part of a group',
          'items fail gradually rather than suddenly', 'there are very few items',
          'failure probabilities are unknown'],
    'a': 1,
    'w': 'The saving comes from the labour and disruption avoided by doing the work once. If '
         'the two unit costs were similar there would be nothing to gain, since group '
         'replacement discards unexpired life.',
    'src': 'Chapter 18.3'},
   {'q': 'In the replacement model for a deteriorating asset, capital cost per year of '
         'ownership',
    'o': ['rises as the asset is kept longer', 'falls as the asset is kept longer',
          'remains constant', 'equals the annual depreciation charge', 'is always zero'],
    'a': 1,
    'w': 'The net capital outlay is spread over more years, so although the total capital cost '
         'rises as resale value falls, the amount per year falls.',
    'src': 'Chapter 18.2'},
  ],
  'theory': [
   {'q': 'A transport company is considering its policy for replacing its delivery vans. A new '
         'van costs ₦4,000,000. Estimated running costs and resale values are:\n\nYear 1: '
         'running ₦800,000, resale ₦2,800,000. Year 2: running ₦1,000,000, resale ₦2,000,000. '
         'Year 3: running ₦1,400,000, resale ₦1,400,000. Year 4: running ₦2,000,000, resale '
         '₦900,000. Year 5: running ₦2,800,000, resale ₦500,000.\n\n(a) Determine the optimal '
         'replacement period, ignoring the time value of money. (b) Explain the reasoning '
         'behind the method. (c) State three limitations of the analysis.',
    'marks': 15,
    'a': [
      {'h4': '(a) Computation'},
      {'p': 'For each possible replacement age, capital cost is the purchase price less the '
            'resale value at that age, to which cumulative running costs are added. The total '
            'is then divided by the number of years of use. All figures in ₦\'000:'},
      {'table': {'align': 'lrrrrr',
        'head': ['Replace at end of year', 'Cumulative running cost',
                 'Capital cost $4{,}000 - S_n$', 'Total cost', 'Years',
                 'Average annual cost'], 'rows': [
        ['1', '800', '1,200', '2,000', '1', '2,000'],
        ['2', '1,800', '2,000', '3,800', '2', '1,900'],
        ['3', '3,200', '2,600', '5,800', '3', '1,933'],
        ['4', '5,200', '3,100', '8,300', '4', '2,075'],
        ['5', '8,000', '3,500', '11,500', '5', '2,300'],
      ]}},
      {'p': 'The average annual cost is minimised at **₦1,900,000**, which occurs when the van '
            'is replaced at the end of **year 2**.'},
      {'p': 'The company should therefore operate a two-year replacement cycle. Note, however, '
            'that year 3 costs ₦1,933,000 — only ₦33,000 a year more, or 1.7%. The two options '
            'are for practical purposes equivalent, and factors outside the model (the '
            'reliability of the second-hand market, the disruption of changing vehicles, the '
            'availability of capital) could reasonably decide between them. Beyond year 3 the '
            'position deteriorates sharply, and a five-year cycle would cost 21% more per year '
            'than the optimum.'},
      {'h4': '(b) The reasoning'},
      {'p': 'Two costs of ownership move in opposite directions as the asset is kept longer.'},
      {'ul': [
        '**Capital cost per year falls.** The net outlay — purchase price less what the van '
        'eventually fetches — is spread over an increasing number of years. Here it falls from '
        '₦1,200,000 for one year of use to ₦700,000 a year over five years.',
        '**Running cost per year rises.** As the vehicle ages, fuel consumption, maintenance '
        'and repairs increase, and downtime grows. Here average running cost rises from '
        '₦800,000 in year 1 to ₦1,600,000 a year over five years.',
      ]},
      {'p': 'The sum of the two is therefore U-shaped: high at short lives because the capital '
            'cost is barely spread, high at long lives because running costs dominate. The '
            'optimum is the bottom of the U — the age at which the total cost of a year of '
            'motoring is least. Equivalently, the asset should be kept while the incremental '
            'cost of one more year is below the current average, and replaced once it exceeds '
            'it.'},
      {'h4': '(c) Limitations'},
      {'ol': [
        '**The time value of money is ignored.** Costs in year 5 are treated as equal to costs '
        'in year 1, which they are not. With a positive cost of capital, later running costs '
        'are worth less in present-value terms, which tends to favour keeping the asset longer. '
        'The correct treatment is to discount the cash flows of one replacement cycle and '
        'compare the **equivalent annual cost**, $NPV \\div$ annuity factor, across the '
        'possible lives.',
        '**All figures are estimates.** Running costs four and five years ahead and resale '
        'values in a second-hand market that may not exist as forecast are both uncertain. '
        'Since the difference between a two-year and a three-year cycle is only 1.7%, an error '
        'well within the margin of estimation would reverse the recommendation. Sensitivity '
        'analysis is essential.',
        '**Technology and prices are assumed static.** The model assumes the replacement van '
        'costs the same ₦4,000,000 and has the same cost profile. Inflation, exchange-rate '
        'movements on imported vehicles, and improvements in fuel efficiency all break that '
        'assumption.',
        '**Non-financial factors are excluded.** Vehicle reliability affects customer service '
        'and the company\'s reputation; the age of a fleet affects the image presented to '
        'customers, driver morale, and increasingly regulatory compliance on emissions. None of '
        'these enters the cost table.',
        '**Capital availability and taxation are ignored.** A shorter cycle requires cash '
        'sooner and more often, which a company under financing constraints may not have. '
        'Capital allowances and the tax treatment of disposals also affect the real cost of '
        'each policy.',
      ]}],
    'src': 'Chapter 18.2'},
  ]},
}
