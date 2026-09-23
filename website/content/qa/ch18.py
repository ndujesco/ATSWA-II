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
      {'warn': 'This basic model ignores the time value of money — see §18.2\'s discounting '
               'method below for how the study text treats a case where interest rates matter.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 18.1 — replacement age of a grinding machine '
      '(no discounting)', 'open': True, 'q': [
      {'p': 'An owner of a grinding machine estimates that operating cost per year is: Year 1 '
            '₦250, Year 2 ₦550, Year 3 ₦850, Year 4 ₦1,250, Year 5 ₦1,850, Year 6 ₦2,550, Year '
            '7 ₦3,250, Year 8 ₦4,050. The cost price is ₦12,300 and the scrap value is ₦250. '
            'When should the machine be replaced?'}],
      'a': [
      {'table': {'align': 'lrrrrr', 'head': ['Year $n$', 'Running cost', 'Cumulative running '
        'cost', 'Depreciation ($C-S$)', 'Total cost', 'Average cost'], 'rows': [
        ['1', '250', '250', '12,050', '12,300', '12,300'],
        ['2', '550', '800', '12,050', '12,850', '6,425'],
        ['3', '850', '1,650', '12,050', '13,700', '4,566.67'],
        ['4', '1,250', '2,900', '12,050', '14,950', '3,737.50'],
        ['5', '1,850', '4,750', '12,050', '16,800', '3,360'],
        ['6', '2,550', '7,300', '12,050', '19,350', '**3,225**'],
        ['7', '3,250', '10,550', '12,050', '22,600', '3,228.57'],
        ['8', '4,050', '14,600', '12,050', '26,650', '3,331.25'],
      ]}},
      {'p': 'Average annual cost is lowest in year 6, so the machine should be replaced at the '
            'end of the **sixth year** of use.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 18.2 — replacement with maintenance cost and '
      'resale value tables', 'open': True, 'q': [
      {'p': 'A machine costing ₦70,000 has maintenance cost and resale value per year:'},
      {'table': {'align': 'lrr', 'head': ['Year', 'Maintenance cost', 'Resale value'], 'rows': [
        ['1', '9,000', '40,000'], ['2', '12,000', '20,000'], ['3', '16,000', '12,000'],
        ['4', '21,000', '6,000'], ['5', '28,000', '5,000'], ['6', '37,000', '4,000'],
        ['7', '47,000', '4,000'], ['8', '59,000', '4,000'],
      ]}},
      {'p': 'When should the machine be replaced?'}],
      'a': [
      {'table': {'align': 'lrrrrr', 'head': ['Year $n$', 'Capital cost ($C-S$)',
        'Annual maintenance', 'Cumulative maintenance', 'Total cost', 'Average cost'], 'rows': [
        ['1', '30,000', '9,000', '9,000', '39,000', '39,000'],
        ['2', '50,000', '12,000', '21,000', '71,000', '35,500'],
        ['3', '58,000', '16,000', '37,000', '95,000', '31,666.67'],
        ['4', '64,000', '21,000', '58,000', '122,000', '30,500'],
        ['5', '65,000', '28,000', '86,000', '151,000', '**30,200**'],
        ['6', '66,000', '37,000', '123,000', '189,000', '31,500'],
        ['7', '66,000', '47,000', '170,000', '236,000', '33,714'],
        ['8', '66,000', '59,000', '229,000', '295,000', '36,875'],
      ]}},
      {'p': 'Average cost is minimum in year 5, so the machine should be replaced by the end of '
            'the **fifth year**.'}]}},
    {'h4': 'When the value of money changes with time'},
    {'p': 'Where maintenance cost rises with time **and** the value of money is also changing, '
          'the replacement decision is based on the equivalent (discounted) cost. The present '
          'value (worth) of ₦100 spent after $n$ years, where the interest rate is $r$ per cent '
          'a year, is'},
    {'tex': 'D = \\frac{100}{(100+r)^n}', 'tag': '(18.1)'},
    {'p': 'where $D$ is the discount rate/factor. Each year\'s cost is multiplied by the '
          'discount factor for that year, and the machine with the **lower total discounted '
          'cost** is preferred.'},
    {'eg': {'tag': 'Study text', 't': 'Example 18.3 — comparing two machines with discounting',
      'open': True, 'q': [
      {'p': 'The yearly costs of two machines, money value neglected, are:'},
      {'table': {'align': 'lrrr', 'head': ['Year', '1', '2', '3'], 'rows': [
        ['Machine A (₦)', '1,400', '800', '1,000'],
        ['Machine B (₦)', '24,000', '300', '1,100'],
      ]}},
      {'p': 'If the money value is 12% per year, find the discounted cost pattern of each '
            'machine and determine which is more economical.'}],
      'a': [
      {'tex': 'd = \\frac{1}{1+0.12} = 0.89'},
      {'table': {'align': 'lrrrr', 'head': ['', 'Year 1', 'Year 2 ($\\times 0.89$)',
        'Year 3 ($\\times 0.89^2$)', 'Total'], 'rows': [
        ['Machine A', '1,400', '712', '792.1', '**2,904.1**'],
        ['Machine B', '24,000', '267', '871.31', '**25,138.3**'],
      ]}},
      {'p': '**Machine A is more economical**, since its total discounted cost is much lower.'}]}},
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
    {'eg': {'tag': 'Study text', 't': 'Example 18.4 — individual replacement (resistors)',
      'open': True, 'q': [
      {'p': 'Resistors used in a company\'s computers have a life span of five months, with '
            'failure rates: month 1, 10%; month 2, 30%; month 3, 35%; month 4, 20%; month 5, '
            '5%. 798 resistors are fixed for use at a time. Each resistor costs ₦14 if replaced '
            'as part of a group, or ₦60 if replaced individually. Determine the cost of '
            'individual monthly replacement.'}],
      'a': [
      {'p': 'Average life span $t = \\sum P_iX_i = 1(0.10)+2(0.30)+3(0.35)+4(0.20)+5(0.05) '
            '= 0.10+0.60+1.05+0.80+0.25 = 2.80$ months.'},
      {'tex': 'R = \\frac{N}{t} = \\frac{798}{2.80} = 285 \\text{ (average monthly replacements)}'},
      {'tex': 'C = RK = 285 \\times 60 = ₦17{,}100 \\text{ (individual replacement cost)}'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 18.5 — group replacement (resistors, continued)',
      'open': True, 'q': [
      {'p': 'Using the data in Example 18.4, determine (a) the best interval between group '
            'replacements, and (b) the cost of group replacement.'}],
      'a': [
      {'p': 'Let $N_i$ be the number of items replaced at the end of month $i$, with $N_0=798$. '
            'Projecting forward using the monthly failure probabilities $P_1$–$P_5$ (0.10, '
            '0.30, 0.35, 0.20, 0.05):'},
      {'table': {'align': 'lr', 'head': ['Month', 'Failures ($N_i$)'], 'rows': [
        ['1', '80'], ['2', '247'], ['3', '328'], ['4', '295'], ['5', '270'], ['6', '284'],
      ]}},
      {'note': 'The number of failures each month rises to month 3, falls, then rises again '
               'from month 6 — it oscillates continuously until the system reaches a steady '
               'state.'},
      {'p': 'Total cost of group replacement at the end of each month '
            '$=$ (number replaced as a group $\\times$ ₦14) $+$ (cumulative individual '
            'failures replaced $\\times$ ₦60):'},
      {'table': {'align': 'lrr', 'head': ['End of month', 'Total cost (₦)', 'Average cost per '
        'month (₦)'], 'rows': [
        ['1', '15,972', '15,972'],
        ['2', '30,792', '**15,396**'],
        ['3', '50,472', '16,824'],
        ['4', '68,172', '17,043'],
        ['5', '84,372', '16,874'],
      ]}},
      {'p': '**(a)** The average cost per month is lowest at the end of month 2, so group '
            'replacement should occur **every two months**. **(b)** The cost of the group '
            'replacement is **₦15,396** — cheaper than the ₦17,100 individual-only cost found '
            'in Example 18.4.'}]}},
  ]},

  {'n': '18.4', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§18.1 The two replacement problems** — **gradual deterioration** (running cost rises, '
      'resale falls steadily — vehicles, machinery): decide the *age* to replace a single '
      'asset by minimising average annual cost. **Sudden failure** (works perfectly then fails '
      'without warning — bulbs, fuses, small components): decide **individual** replacement '
      '(on failure) vs **group** replacement (all together at intervals, individual '
      'replacement of any that fail in between) by comparing cost per period.',
      '**§18.2 Items that deteriorate** — average annual cost $AAC_n=[(C-S_n)+\\sum R_t]/n$ '
      '($C$ = purchase cost, $S_n$ = resale value at year $n$, $R_t$ = running cost in year '
      '$t$); capital cost per year **falls** with longer ownership, running cost per year '
      '**rises**, so $AAC$ is U-shaped — replace at the age that minimises it. The bottom of '
      'the U is usually flat, so a small departure from the exact optimum costs little. Where '
      'the value of money is also changing with time, discount each year\'s cost by '
      '$D=100/(100+r)^n$ and compare **total discounted cost** across options instead.',
      '**§18.3 Items that fail suddenly** — project period failures $N_t$ **including failures '
      'among the replacements themselves** (a common omission that understates later periods); '
      'mean life $\\bar{L}=\\sum t\\,p_t$ (a probability-weighted average, not a simple one); '
      'steady-state individual-policy failures per period $=N/\\bar{L}$; group-replacement '
      'cost per period at interval $n$ $=[NC_g+C_i\\sum_{t=1}^n N_t]/n$. Compare the individual '
      'policy\'s steady-state cost per period against the cheapest group interval\'s cost per '
      'period and pick the lower — and comment on non-financial factors when the financial '
      'margin between them is thin.',
    ]},
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
    {'h3': 'B. Items that deteriorate — with the value of money changing'},
    {'fbox': {'h': 'Discounted cost comparison', 'rows': [
      {'lb': 'Discount rate/factor for year $n$',
       'tex': 'D = \\dfrac{100}{(100+r)^{n}}'},
      {'lb': 'Discounted cost in year $t$', 'tex': '\\text{Cost}_t \\times d^{\\,t-1}'},
      {'lb': 'Rule',
       'tex': '\\text{sum each option\'s discounted yearly costs; choose the lower total}'},
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

  {'n': '18.5', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Which of the following is the reason for the study of replacement theory? (A) To '
        'ensure efficient functioning of the equipment  (B) To know when and how best the '
        'equipment can be replaced  (C) To minimize the costs of maintenance  (D) (A) and (B) '
        'only  (E) (A), (B) and (C)',
        'Which of the following is a policy in the replacement of equipment or items that fail '
        'suddenly? (A) Gradual replacement policy  (B) Individual replacement policy  '
        '(C) Group replacement policy  (D) (B) and (C) only  (E) (A) and (B) only',
        'Which of the following is NOT a resulting effect of gradual failure or deterioration '
        'of items? (A) The output of the equipment  (B) Its production capacity  (C) The '
        'maintenance and operating costs  (D) The value of the re-sale price of the item  '
        '(E) The efficiency of the equipment',
      ]},
      {'p': 'A certain item has monthly failure probabilities 0.05, 0.08, 0.12, 0.18, 0.25, '
            '0.20, 0.08, 0.04 for months 1–8 respectively (cumulative: 0.05, 0.13, 0.25, 0.43, '
            '0.68, 0.88, 0.96, 1.00). The total number of items is 1,000; individual and group '
            'replacement cost ₦2.25 and 60 kobo per item respectively. Use this to answer '
            'questions 4–6.'},
      {'ol': [
        'The average number of failures per month is approximately …',
        'The average cost of individual replacement is …',
        'The best interval between group replacements is …',
        'At the old age of an operating machine, state the reason why it will definitely '
        'require higher operating costs and more maintenance costs.',
        'The two common replacement policies are replacement of equipment/items that: '
        '(i) … (ii) …',
        'State any TWO consequences of equipment/items that deteriorate with time having their '
        'efficiency get low.',
        'State two characterising features of the policy that governs an equipment that is '
        'replaced immediately it fails.',
      ]}],
      'a': [
      {'ol': [
        '**E** — all three (A, B and C) are reasons for the study.',
        '**D** — individual and group replacement are both sudden-failure policies.',
        '**B**, per the study text\'s own printed key — though §18.2 lists "a decrease in the '
        'equipment production capacity" as one of the three effects of gradual failure, which '
        'sits awkwardly with this answer. Treat this one with caution; verify with your tutor.',
        'Expected value $=(1\\times0.05)+(2\\times0.08)+\\dots+(8\\times0.04)=4.62$. Average '
        'number of failures per month $=1{,}000/4.62 \\approx$ **216**.',
        'Average cost of individual replacement $=216 \\times 2.25 = $ **₦486**.',
        'Minimum cost of group replacement per month occurs in the **3rd month**.',
        'The reason is due to repairing and replacement of some parts.',
        '(i) equipment/items that deteriorate or wear out gradually; and (ii) equipment/items '
        'that fail suddenly.',
        '(i) a decrease in production capacity; (ii) increasing maintenance and operating '
        'costs; (iii) a decrease in the re-sale (salvage) value of the item — any two.',
        '(i) the item\'s life span is uncertain; (ii) failure is assumed to occur only at the '
        'end of its life span.',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Total cost of ownership over $n$ years',
   'tex': 'TC(n) = (C - S_n) + \\sum_{t=1}^{n} R_t'},
  {'lb': 'Average annual cost of ownership',
   'tex': 'AAC_n = \\frac{(C - S_n) + \\sum_{t=1}^{n} R_t}{n}'},
  {'lb': 'Discount rate/factor for year $n$', 'tex': 'D = \\frac{100}{(100+r)^{n}}'},
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
    'src': 'Chapter 18.2', 'sec': '18.2'},
   {'q': 'A machine costs ₦80,000 and has a resale value of ₦30,000 after 2 years. Running '
         'costs are ₦20,000 in year 1 and ₦26,000 in year 2. The average annual cost of '
         'replacing after 2 years is',
    'o': ['₦38,000', '₦48,000', '₦53,000', '₦96,000', '₦23,000'],
    'a': 1,
    'w': 'Capital cost is $80{,}000 - 30{,}000 = ₦50{,}000$; cumulative running cost is '
         '₦46,000; divide the total by 2 years.',
    'calc': 'AAC_2 = \\frac{50{,}000 + 46{,}000}{2} = \\frac{96{,}000}{2} = ₦48{,}000',
    'src': 'Chapter 18.2', 'sec': '18.2'},
   {'q': 'If items fail with probabilities 0.2, 0.3 and 0.5 in the first, second and third '
         'months of life, the mean life of an item is',
    'o': ['2.00 months', '2.30 months', '2.50 months', '3.00 months', '1.00 month'],
    'a': 1,
    'w': 'Weight each period by its probability of failure.',
    'calc': '\\bar{L} = 1(0.2) + 2(0.3) + 3(0.5) = 0.2 + 0.6 + 1.5 = 2.3',
    'src': 'Chapter 18.3', 'sec': '18.3'},
   {'q': 'Group replacement is likely to be preferred to individual replacement when',
    'o': ['items are expensive to buy', 'the cost of replacing an item individually greatly '
          'exceeds the cost of replacing it as part of a group',
          'items fail gradually rather than suddenly', 'there are very few items',
          'failure probabilities are unknown'],
    'a': 1,
    'w': 'The saving comes from the labour and disruption avoided by doing the work once. If '
         'the two unit costs were similar there would be nothing to gain, since group '
         'replacement discards unexpired life.',
    'src': 'Chapter 18.3', 'sec': '18.3'},
   {'q': 'In the replacement model for a deteriorating asset, capital cost per year of '
         'ownership',
    'o': ['rises as the asset is kept longer', 'falls as the asset is kept longer',
          'remains constant', 'equals the annual depreciation charge', 'is always zero'],
    'a': 1,
    'w': 'The net capital outlay is spread over more years, so although the total capital cost '
         'rises as resale value falls, the amount per year falls.',
    'src': 'Chapter 18.2', 'sec': '18.2'},
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
        'The correct treatment discounts each year\'s cost by $D=100/(100+r)^n$ and compares '
        'the **total discounted cost** of each option, as in §18.2\'s machine-A-vs-B example.',
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
    'src': 'Chapter 18.2', 'sec': '18.2'},
  ]},
}
