CH = {
 'n': 9,
 't': 'Accounting for Non-Current Assets',
 'brief': 'IAS 16 and IAS 38: what goes into cost, how depreciation is computed under each '
          'method, revaluation, disposal and the non-current asset schedule.',
 'outcomes': [
   'Determine the cost of an item of property, plant and equipment',
   'Compute depreciation by the straight line, reducing balance and other methods',
   'Account for the revaluation of an asset and the treatment of the surplus',
   'Compute the profit or loss on disposal',
   'Prepare a non-current asset schedule and the related ledger accounts',
   'Distinguish capital from revenue expenditure and state the effect of misclassification',
 ],
 'secs': [
  {'n': '9.1', 't': 'What goes into cost', 'b': [
    {'p': 'IAS 16 says cost comprises the purchase price plus **any costs directly attributable '
          'to bringing the asset to the location and condition necessary for it to operate in '
          'the manner intended by management**, plus the estimated cost of dismantling and '
          'restoring the site where an obligation exists.'},
    {'table': {'head': ['Include in cost', 'Exclude — expense as incurred'], 'align': 'll',
     'rows': [
      ['Purchase price net of trade discount and rebates', 'Recoverable VAT'],
      ['Import duties and non-refundable purchase taxes', 'Administration and general overheads'],
      ['Site preparation, delivery and handling', 'Staff training on the new asset'],
      ['Installation, assembly and testing', 'Costs of introducing a new product'],
      ['Professional fees (architects, engineers)', 'Operating losses in the start-up period'],
      ['Initial dismantling and restoration obligation', 'Costs of relocating the asset later'],
      ['Borrowing costs on a qualifying asset (IAS 23)', 'Repairs and maintenance'],
    ]}},
    {'eg': {'t': 'Determining cost', 'q': [
      {'p': 'A company acquired a machine. The invoice showed: list price ₦16,000,000; trade '
            'discount 10%; delivery ₦340,000; installation ₦620,000; testing ₦180,000; a '
            'twelve-month maintenance contract ₦450,000; staff training ₦210,000. The company '
            'also expects to dismantle the machine in ten years at a present-value cost of '
            '₦900,000. Compute the cost to be capitalised.'}],
      'a': [
      {'stmt': {'t': 'Cost of the machine', 'rows': [
        ['List price', 16000000],
        ['Less trade discount at 10%', -1600000],
        ['Net purchase price', 14400000, '@t'],
        ['Delivery', 340000],
        ['Installation', 620000],
        ['Testing', 180000],
        ['Present value of dismantling obligation', 900000],
        ['Capitalised cost', 16440000, '@tt'],
      ]}},
      {'p': 'The maintenance contract (₦450,000) and staff training (₦210,000) are **expensed**. '
            'Neither brings the asset to working condition — maintenance keeps it there '
            'afterwards, and training benefits the staff, whom the entity does not control.'},
      {'note': 'Trade discount is always deducted; a **settlement** (cash) discount is not part '
               'of the cost calculation at all — it is a financing item recognised when taken.'}]}},
  ]},

  {'n': '9.2', 't': 'Depreciation', 'b': [
    {'def': {'t': 'Depreciation', 'd': 'the systematic allocation of the depreciable amount of an '
                  'asset over its useful life. The **depreciable amount** is cost less residual value.'}},
    {'key': 'Depreciation is **allocation of cost**, not valuation and not a fund for replacement. '
            'That distinction is a recurring short-answer question, and the second half — that it '
            'is not a cash fund — is where the second mark lives.'},
    {'h3': 'Straight line'},
    {'tex': '\\text{Annual charge} = \\frac{\\text{Cost} - \\text{Residual value}}'
            '{\\text{Useful life}} \\qquad\\text{or}\\qquad \\text{rate}\\% \\times '
            '(\\text{Cost} - \\text{RV})', 'tag': '(9.1)'},
    {'p': 'Equal charge each year. Appropriate where the benefit is consumed evenly — buildings, '
          'fixtures, leases.'},
    {'h3': 'Reducing (diminishing) balance'},
    {'tex': '\\text{Charge}_t = r \\times \\text{Carrying amount at start of year } t', 'tag': '(9.2)'},
    {'p': 'A high charge early and a low charge late, which matches assets that lose value fastest '
          'when new and need more repairs when old — motor vehicles, computers. The combined '
          'charge for depreciation plus repairs is therefore more even than under straight line.'},
    {'p': 'Where the rate is not given, it can be derived from the residual value:'},
    {'tex': 'r = 1 - \\sqrt[n]{\\dfrac{\\text{Residual value}}{\\text{Cost}}}', 'tag': '(9.3)'},
    {'h3': 'Other methods'},
    {'ul': [
      '**Sum of the digits** — charge for year $t$ of an $n$-year life is $\\dfrac{n-t+1}{n(n+1)/2}$ '
      'of the depreciable amount. Another accelerated method.',
      '**Units of production (machine hour)** — charge is $\\dfrac{\\text{Depreciable amount}}'
      '{\\text{Total expected output}} \\times \\text{output for the year}$. Best where wear '
      'depends on use rather than time.',
      '**Revaluation method** — used for many small items such as loose tools: charge is opening '
      'valuation plus purchases less closing valuation.',
    ]},
    {'eg': {'t': 'Straight line against reducing balance', 'q': [
      {'p': 'A vehicle costs ₦7,500,000 with an estimated residual value of ₦1,500,000 and a '
            'four-year life. Compute the charge and carrying amount for each year under (a) the '
            'straight line method and (b) the reducing balance method at 30% a year.'}],
      'a': [
      {'p': '**(a) Straight line.** $\\dfrac{7{,}500{,}000 - 1{,}500{,}000}{4} = ₦1{,}500{,}000$ '
            'a year.'},
      {'table': {'cap': 'Straight line', 'align': 'lrrr',
        'head': ['Year', 'Opening CA (₦)', 'Charge (₦)', 'Closing CA (₦)'], 'rows': [
        ['1', '7,500,000', '1,500,000', '6,000,000'],
        ['2', '6,000,000', '1,500,000', '4,500,000'],
        ['3', '4,500,000', '1,500,000', '3,000,000'],
        ['4', '3,000,000', '1,500,000', '1,500,000'],
      ]}},
      {'p': '**(b) Reducing balance at 30%.** The residual value is not deducted first — the rate '
            'is applied to the carrying amount.'},
      {'table': {'cap': 'Reducing balance at 30%', 'align': 'lrrr',
        'head': ['Year', 'Opening CA (₦)', 'Charge (₦)', 'Closing CA (₦)'], 'rows': [
        ['1', '7,500,000', '2,250,000', '5,250,000'],
        ['2', '5,250,000', '1,575,000', '3,675,000'],
        ['3', '3,675,000', '1,102,500', '2,572,500'],
        ['4', '2,572,500', '771,750', '1,800,750'],
      ]}},
      {'note': 'Reducing balance never reaches zero, which is why it suits assets with a residual '
               'value. Note also that the two methods charge the same **total** over the life of '
               'the asset if it is held to the end — only the timing differs. That point is worth '
               'a mark whenever a question asks you to compare them.'},
      {'p': 'Had the question instead asked for the rate that reduces ₦7,500,000 to ₦1,500,000 '
            'over four years:'},
      {'tex': 'r = 1 - \\sqrt[4]{\\frac{1{,}500{,}000}{7{,}500{,}000}} = 1 - \\sqrt[4]{0.2} '
              '= 1 - 0.6687 = 33.13\\%'}]}},
    {'h3': 'Part-year charges'},
    {'p': 'Read the policy in the question. The three you will meet are: charge in proportion to '
          'the **months owned**; a **full year in the year of purchase and none in the year of '
          'sale**; or a full year in both. They give materially different answers, and the marks '
          'are for following the stated policy, not for choosing the one you prefer.'},
  ]},

  {'n': '9.3', 't': 'Disposal', 'b': [
    {'tex': '\\text{Profit or loss on disposal} = \\text{Net proceeds} - \\text{Carrying amount '
            'at date of disposal}', 'tag': '(9.4)'},
    {'p': 'Where the carrying amount is cost less accumulated depreciation to the date of sale. '
          'The three ledger entries are always the same:'},
    {'steps': [
      'Transfer the cost: **Dr** Disposal, **Cr** Asset at cost.',
      'Transfer the accumulated depreciation: **Dr** Accumulated depreciation, **Cr** Disposal.',
      'Record the proceeds: **Dr** Cash or receivable, **Cr** Disposal.',
    ]},
    {'p': 'The balance on the disposal account is the profit (credit balance) or loss (debit '
          'balance), taken to profit or loss.'},
    {'eg': {'t': 'Disposal with a part-exchange', 'q': [
      {'p': 'A machine bought on 1 April 2021 for ₦4,800,000 was traded in on 30 September 2024 '
            'against a new machine costing ₦7,200,000. A part-exchange allowance of ₦1,150,000 '
            'was given and the balance paid by cheque. Depreciation is 20% a year on cost, '
            'charged monthly. Show the disposal account.'}],
      'a': [
      {'p': 'Annual charge $= 0.20 \\times 4{,}800{,}000 = ₦960{,}000$, or ₦80,000 a month. The '
            'machine was held from 1 April 2021 to 30 September 2024 = 42 months.'},
      {'tex': '\\text{Accumulated depreciation} = 80{,}000 \\times 42 = ₦3{,}360{,}000'},
      {'tex': '\\text{Carrying amount} = 4{,}800{,}000 - 3{,}360{,}000 = ₦1{,}440{,}000'},
      {'tacc': {'t': 'Disposal of machine', 'dr': [
          ['Machine at cost', 4800000], ['', 4800000, '@tot']],
        'cr': [['Accumulated depreciation', 3360000], ['Part-exchange allowance', 1150000],
               ['Loss on disposal to P/L', 290000], ['', 4800000, '@tot']]}},
      {'tex': '\\text{Loss} = 1{,}150{,}000 - 1{,}440{,}000 = -₦290{,}000'},
      {'note': 'The part-exchange allowance is the **proceeds**. The new machine is recorded at '
               'its full cost of ₦7,200,000, financed by ₦1,150,000 of allowance and ₦6,050,000 '
               'of cash. Netting the allowance off the new cost is a common error and understates '
               'both the asset and the loss.'}]}},
  ]},

  {'n': '9.4', 't': 'Revaluation', 'b': [
    {'p': 'IAS 16 permits either the **cost model** (cost less accumulated depreciation and '
          'impairment) or the **revaluation model** (fair value at the date of revaluation less '
          'subsequent depreciation and impairment). Once chosen, the model applies to the whole '
          '**class** of assets, not to a single item.'},
    {'h3': 'Accounting for a surplus'},
    {'ul': [
      'The increase is credited to **other comprehensive income** and accumulated in equity as a '
      '**revaluation surplus** — it never passes through profit or loss.',
      'Unless it reverses a decrease previously recognised in profit or loss for the same asset, '
      'in which case that much is credited to profit or loss first.',
      'Accumulated depreciation at the date of revaluation is eliminated against the gross '
      'carrying amount, and the asset is restated at the revalued amount.',
      'Depreciation thereafter is based on the **revalued amount over the remaining useful life**, '
      'so the charge increases.',
      'The entity may transfer the excess depreciation from the revaluation surplus to retained '
      'earnings each year; this is a reserve movement, not income.',
    ]},
    {'p': 'A **decrease** on revaluation is recognised in profit or loss, except to the extent it '
          'reverses a surplus already held for that asset, which is debited to other comprehensive '
          'income first.'},
    {'eg': {'t': 'Revaluation and the surplus', 'q': [
      {'p': 'A building costing ₦40,000,000 on 1 January 2019 was being depreciated over 40 years '
            'with no residual value. On 1 January 2024 it was revalued to ₦54,000,000, with the '
            'remaining useful life unchanged at 35 years. Show the revaluation and the '
            'depreciation charge for 2024.'}],
      'a': [
      {'p': 'Annual charge to 2023 $= 40{,}000{,}000 \\div 40 = ₦1{,}000{,}000$; five years '
            'elapsed, so accumulated depreciation is ₦5,000,000.'},
      {'stmt': {'t': 'Revaluation at 1 January 2024', 'rows': [
        ['Cost', 40000000],
        ['Accumulated depreciation (5 years)', -5000000],
        ['Carrying amount', 35000000, '@t'],
        ['Revalued amount', 54000000],
        ['Revaluation surplus to other comprehensive income', 19000000, '@tt'],
      ]}},
      {'p': 'Entry: **Dr** Building (to restate to ₦54,000,000), **Dr** Accumulated depreciation '
            '₦5,000,000, **Cr** Revaluation surplus ₦19,000,000.'},
      {'tex': '\\text{Depreciation for 2024} = \\frac{54{,}000{,}000}{35} = ₦1{,}542{,}857'},
      {'p': 'The extra charge of $1{,}542{,}857 - 1{,}000{,}000 = ₦542{,}857$ may be transferred '
            'annually from the revaluation surplus to retained earnings, so that distributable '
            'reserves are not depleted by the revaluation.'},
      {'warn': 'The surplus goes to **other comprehensive income**, never to profit or loss. '
               'Crediting ₦19,000,000 to profit is the single largest error available in this '
               'chapter, and examiners plant the opportunity deliberately.'}]}},
  ]},

  {'n': '9.5', 't': 'Intangible assets and the asset schedule', 'b': [
    {'p': 'IAS 38 recognises an intangible asset only if it is **identifiable** (separable or '
          'arising from contractual rights), **controlled**, and expected to generate future '
          'economic benefits, and its cost can be measured reliably.'},
    {'ul': [
      '**Purchased goodwill** is recognised only in a business combination; **internally '
      'generated goodwill is never recognised**.',
      '**Research** expenditure is always expensed. **Development** expenditure is capitalised '
      'only if all six PIRATE conditions are met: **P**robable future benefits, **I**ntention to '
      'complete, **R**esources adequate, **A**bility to use or sell, **T**echnical feasibility, '
      '**E**xpenditure measurable.',
      'Finite-life intangibles are **amortised**; indefinite-life intangibles are not amortised '
      'but are tested for impairment annually.',
    ]},
    {'h3': 'The non-current asset schedule'},
    {'p': 'A published-accounts note that Section B questions ask for regularly. Its shape is '
          'fixed: cost across the top block, accumulated depreciation across the bottom, carrying '
          'amount as the difference.'},
    {'table': {'cap': 'Property, plant and equipment (₦\'000)', 'align': 'lrrrr',
      'head': ['', 'Land & buildings', 'Plant', 'Vehicles', 'Total'], 'rows': [
      ['**Cost**', '', '', '', ''],
      ['At 1 January 2024', '175,000', '131,250', '78,750', '385,000'],
      ['Additions', '—', '17,500', '10,500', '28,000'],
      ['Disposals', '—', '(12,000)', '(9,400)', '(21,400)'],
      ['At 31 December 2024', '175,000', '136,750', '79,850', '391,600', '@tot'],
      ['**Accumulated depreciation**', '', '', '', ''],
      ['At 1 January 2024', '—', '50,575', '45,500', '96,075'],
      ['Charge for the year', '—', '13,675', '15,970', '29,645'],
      ['On disposals', '—', '(8,300)', '(7,100)', '(15,400)'],
      ['At 31 December 2024', '—', '55,950', '54,370', '110,320', '@tot'],
      ['**Carrying amount**', '', '', '', ''],
      ['At 31 December 2024', '175,000', '80,800', '25,480', '281,280', '@tot'],
      ['At 31 December 2023', '175,000', '80,675', '33,250', '288,925'],
    ]}},
    {'key': 'Every column must cross-cast and every block must down-cast. Building the schedule '
            'first and reading the statement of financial position off it is faster and safer '
            'than doing it the other way round.'},
  ]},

  {'n': '9.6', 't': 'Capital and revenue expenditure', 'b': [
    {'table': {'head': ['', 'Capital expenditure', 'Revenue expenditure'], 'align': 'lll',
     'rows': [
      ['Purpose', 'Acquire or improve a non-current asset', 'Maintain earning capacity'],
      ['Benefit', 'Extends beyond the current period', 'Consumed within the period'],
      ['Charged to', 'Statement of financial position', 'Statement of profit or loss'],
      ['Examples', 'Purchase of machinery, extension to a building, legal fees on buying property',
       'Repairs, repainting, insurance, wages'],
    ]}},
    {'warn': 'The effect of misclassification compounds. Treating a repair of ₦120,000 as capital '
             'overstates this year\'s profit by ₦120,000 **and** overstates assets, and then '
             'overstates profit again in every later year by the depreciation that should never '
             'have been charged. Questions frequently ask for the effect on profit and on net '
             'assets separately — answer both.'},
  ]},

  {'n': '9.7', 't': 'Cost of an asset — the study text\'s worked illustrations', 'b': [
    {'p': 'The two illustrations the study text uses for the cost computation. The question in '
          'each is reproduced as printed; the solution follows the text.'},
    {'eg': {'tag': 'Illustration 9.1', 't': 'Mensa (Ghana) Ltd — equipment on instalment terms',
      'open': True, 'q': [
      {'p': 'Mensa (Ghana) Ltd orders equipment from a Nigerian tools company at an invoice price '
            'of ₵300,000,000. Payment will be made in 50 monthly instalments of ₵7,200,000 which '
            'include ₵60,000,000 of interest charges. Value added tax of ₵35,000,000 must be paid, '
            'as well as freight charges of ₵30,850,000. Installation and other start-up costs '
            'amount to ₵14,000,000. **Determine the cost of the equipment.**'}],
      'a': [
      {'stmt': {'t': 'Cost of the equipment', 'rows': [
        ['Invoice price', 300000000],
        ['Value added tax', 35000000],
        ['Freight charges', 30850000],
        ['Installation and start-up costs', 14000000],
        ['Cost of the equipment', 379850000, '@tt'],
      ]}},
      {'note': 'The ₵60,000,000 interest built into the instalments is **not** capitalised. It is '
               'a financing charge, recognised as interest expense over the 50 months of payments. '
               'Cost is the cash-equivalent price plus directly attributable costs. The VAT is '
               'included here because the study text treats it as non-refundable; recoverable VAT '
               'would be excluded (see §9.1).'}]}},
    {'eg': {'tag': 'Illustration 9.2', 't': 'Gbenga Nigeria Plc — a manufacturing plant',
      'open': True, 'q': [
      {'p': 'The following cost information relates to a large manufacturing plant acquired by '
            'Gbenga Nigeria Plc:'},
      {'table': {'align': 'lr', 'head': ['', '₦'], 'rows': [
        ['List price of the machinery', '25,000,000'],
        ['Trade discount received', '500,000'],
        ['Delivery cost', '2,250,000'],
        ['Installation cost', '3,450,000'],
        ['Cost of site preparation', '5,200,000'],
        ['Architect\'s fees', '300,000'],
        ['Administration expense', '2,500,000'],
        ['Test-run cost', '1,400,000'],
      ]}},
      {'p': 'The test run was to ensure the asset was installed and working correctly. Items of '
            'inventory produced during the test run had a sale value of ₦200,000. A state '
            'government licensing condition requires Gbenga Plc to remove the asset and restore '
            'the site to its former condition at the end of the asset\'s life; the company has '
            'recognised a liability of ₦3,600,000 for the expected clearance cost. **State the '
            'cost to be capitalised.**'}],
      'a': [
      {'stmt': {'t': 'Cost of the machinery', 'rows': [
        ['Purchase price (25,000,000 − 500,000 trade discount)', 24500000],
        ['Delivery cost', 2250000],
        ['Installation cost', 3450000],
        ['Cost of site preparation', 5200000],
        ['Architect\'s fees', 300000],
        ['Decommissioning / site restoration provision', 3600000],
        ['Test-run cost (1,400,000 − 200,000 proceeds)', 1200000],
        ['Capitalised cost', 40500000, '@tt'],
      ]}},
      {'ul': [
        '**Administration expense ₦2,500,000** is a general overhead — excluded by IAS 16.',
        '**Trade discount** is deducted from the list price; a settlement discount would not be.',
        '**Test-run proceeds** of ₦200,000 are netted against the testing cost in the edition of '
        'IAS 16 the study text follows. Under the 2020 amendment to IAS 16 (effective 2022) such '
        'proceeds are taken to profit or loss instead and the full ₦1,400,000 is capitalised — '
        'but ATSWA answers follow the study text.',
        'Cost recognition **ceases when the asset is ready for use** — in the location and '
        'condition management intended.']}]}},
  ]},

  {'n': '9.8', 't': 'Computing depreciation — the study text\'s worked illustrations', 'b': [
    {'eg': {'tag': 'Illustration 9.3', 't': 'Babatunde and Mensah — straight line', 'open': True,
      'q': [
      {'p': 'Babatunde and Mensah purchased an industrial machine costing ₦415,800,000. The '
            'machine has an economic useful life of ten years. It is estimated that the machine '
            'can be sold at the end of the ninth year for ₦83,097,000. Calculate (a) the annual '
            'depreciation charge, (b) the accumulated depreciation and (c) the carrying amount for '
            'each of the first five years.'}],
      'a': [
      {'p': 'Depreciable amount $= 415{,}800{,}000 - 83{,}097{,}000 = ₦332{,}703{,}000$.'},
      {'tex': '\\text{Annual charge} = \\frac{332{,}703{,}000}{9} = ₦36{,}967{,}000'},
      {'table': {'cap': 'First five years (₦\'000)', 'align': 'lrrr',
        'head': ['Year', 'Charge', 'Accumulated depreciation', 'Carrying amount'], 'rows': [
        ['1', '36,967', '36,967', '378,833'],
        ['2', '36,967', '73,934', '341,866'],
        ['3', '36,967', '110,901', '304,899'],
        ['4', '36,967', '147,868', '267,932'],
        ['5', '36,967', '184,835', '230,965'],
      ]}},
      {'p': 'As a percentage of cost: $\\dfrac{36{,}967{,}000}{415{,}800{,}000}\\times 100 = 8.89\\%$.'},
      {'note': 'The study text divides the depreciable amount by **9**, not 10 — it spreads the '
               'cost over the period to the expected disposal (end of year 9), because that is the '
               'asset\'s useful life *to this entity*. Where a question tells you the asset will be '
               'sold before the end of its physical life, depreciate over the shorter period.'}]}},
    {'eg': {'tag': 'Illustration 9.4', 't': 'Bosco Holdings Plc — depreciate the full cost',
      'open': True, 'q': [
      {'p': 'Bosco Holdings Plc acquired a plant at a cash cost of ₦24,000,000. It paid transport '
            'and other handling charges of ₦1,200,000, installation expenses of ₦650,000 and '
            'pre-usage services of ₦580,000. The asset is to be depreciated at 20% per annum on '
            'the straight line basis. Calculate the annual depreciation charge.'}],
      'a': [
      {'stmt': {'t': 'Cost of the plant', 'rows': [
        ['Cash cost', 24000000],
        ['Handling charges', 1200000],
        ['Installation expenses', 650000],
        ['Pre-usage services', 580000],
        ['Capitalised cost', 26430000, '@tt'],
      ]}},
      {'tex': '\\text{Annual charge} = 20\\% \\times 26{,}430{,}000 = ₦5{,}286{,}000'},
      {'key': 'Depreciation is computed on the **full capitalised cost** — the invoice price plus '
              'every directly attributable pre-use cost — not on the purchase price alone.'}]}},
    {'eg': {'tag': 'Illustration 9.5', 't': 'Kwame Company — reducing balance, rate from residual '
      'value', 'open': True, 'q': [
      {'p': 'Kwame Company acquired a tractor for use in agricultural production at a cost of '
            '₦225,000,000. The residual value of the tractor after five years is estimated at '
            '₦38,000,000. Show (a) the depreciation charge, (b) the accumulated depreciation and '
            '(c) the carrying amount for the first four years, using the reducing balance method.'}],
      'a': [
      {'tex': 'r = 1 - \\sqrt[5]{\\frac{38{,}000{,}000}{225{,}000{,}000}} = 1 - \\sqrt[5]{0.16889} '
              '= 1 - 0.701 = 29.9\\% \\approx 30\\%'},
      {'table': {'cap': 'Reducing balance at 30% (₦\'000)', 'align': 'lrrrr',
        'head': ['Year', 'Opening CA', 'Charge (30%)', 'Accumulated depn', 'Closing CA'], 'rows': [
        ['1', '225,000', '67,500', '67,500', '157,500'],
        ['2', '157,500', '47,250', '114,750', '110,250'],
        ['3', '110,250', '33,075', '147,825', '77,175'],
        ['4', '77,175', '23,153', '170,978', '54,022'],
      ]}},
      {'note': 'The study text\'s printed table shows the year-2 charge as 47,500; $157{,}500 '
               '\\times 30\\% = 47{,}250$, and its own accumulated figure of 114,750 confirms '
               '47,250. Treat 47,500 as a misprint. The residual value is **not** deducted before '
               'applying the rate — reducing balance always applies the rate to the carrying '
               'amount.'}]}},
    {'eg': {'tag': 'Illustration 9.6', 't': 'Kwame Company — sum-of-the-years\'-digits', 'open': True,
      'q': [
      {'p': 'Using the figures of Illustration 9.5 (cost ₦225,000,000; residual value ₦38,000,000; '
            'five-year life), calculate the depreciation charge for all five years using the '
            'sum-of-the-years\'-digits method.'}],
      'a': [
      {'p': 'Sum of the digits $= 1+2+3+4+5 = 15$. Depreciable amount $= 225{,}000 - 38{,}000 = '
            '₦187{,}000$ (₦\'000). The digits are applied in reverse — $\\tfrac{5}{15}$ in year 1, '
            'down to $\\tfrac{1}{15}$ in year 5.'},
      {'table': {'cap': 'Sum-of-the-digits (₦\'000)', 'align': 'lrrrr',
        'head': ['Year', 'Fraction', 'Charge', 'Accumulated depn', 'Carrying amount'], 'rows': [
        ['1', '5/15', '62,333', '62,333', '162,667'],
        ['2', '4/15', '49,867', '112,200', '112,800'],
        ['3', '3/15', '37,400', '149,600', '75,400'],
        ['4', '2/15', '24,933', '174,533', '50,467'],
        ['5', '1/15', '12,467', '187,000', '38,000'],
      ]}},
      {'note': 'The study text\'s printed table shows year-5 accumulated depreciation as 167.00 '
               '(in ₦millions); it must be 187.00 so the carrying amount falls exactly to the '
               '₦38,000 (₦\'000) residual value. Like reducing balance, this method front-loads '
               'the charge; unlike reducing balance, it lands the carrying amount precisely on the '
               'residual value.'}]}},
  ]},

  {'n': '9.9', 't': 'Recording depreciation and disposals — the study text\'s worked illustrations',
    'b': [
    {'eg': {'tag': 'Illustration 9.7', 't': 'Damusa & Son — the allowance (provision) method',
      'open': True, 'q': [
      {'p': 'Damusa & Son Manufacturing Company acquired office equipment at a cost of ₦4,800,000 '
            'on 1 January 2021. The equipment is depreciated at 20% per annum on the reducing '
            'balance method. Show, for the first three years: (a) the office equipment account, '
            '(b) the allowance for depreciation account, (c) the statement of profit or loss '
            'extract and (d) the statement of financial position extract.'}],
      'a': [
      {'p': 'Charges: 2021 $= 20\\% \\times 4{,}800{,}000 = 960{,}000$; 2022 $= 20\\% \\times '
            '3{,}840{,}000 = 768{,}000$; 2023 $= 20\\% \\times 3{,}072{,}000 = 614{,}400$.'},
      {'tacc': {'t': 'Office equipment account', 'dr': [
          ['2021 Jan 1  Bank', 4800000], ['', 4800000, '@tot']],
        'cr': [['2021 Dec 31  Balance c/d', 4800000], ['', 4800000, '@tot']]}},
      {'p': 'The asset account simply carries the cost forward — ₦4,800,000 balance b/d at the '
            'start of 2022, 2023 and 2024.'},
      {'tacc': {'t': 'Allowance for depreciation account', 'dr': [
          ['2021 Dec 31  Balance c/d', 960000],
          ['2022 Dec 31  Balance c/d', 1728000],
          ['2023 Dec 31  Balance c/d', 2342400]],
        'cr': [['2021 Dec 31  Profit or loss', 960000],
               ['2022 Jan 1  Balance b/d', 960000],
               ['2022 Dec 31  Profit or loss', 768000],
               ['2023 Jan 1  Balance b/d', 1728000],
               ['2023 Dec 31  Profit or loss', 614400]]}},
      {'stmt': {'t': 'Statement of financial position extracts', 'rows': [
        ['2021: Office equipment at cost', 4800000],
        ['       Less accumulated depreciation', -960000],
        ['       Carrying amount', 3840000, '@t'],
        '@gap',
        ['2022: Office equipment at cost', 4800000],
        ['       Less accumulated depreciation', -1728000],
        ['       Carrying amount', 3072000, '@t'],
        '@gap',
        ['2023: Office equipment at cost', 4800000],
        ['       Less accumulated depreciation', -2342400],
        ['       Carrying amount', 2457600, '@t'],
      ]}},
      {'note': 'This is the **allowance (provision) method**, preferred by IFRS: the asset stays '
               'at cost and a separate accumulated-depreciation account builds up, so the '
               'statement of financial position can show cost, accumulated depreciation and '
               'carrying amount side by side. Writing depreciation straight off the asset account '
               'hides the original cost.'}]}},
    {'eg': {'tag': 'Illustration 9.8', 't': 'Adanna Nigeria Ltd — straight line, then reducing '
      'balance', 'open': True, 'q': [
      {'p': 'Adanna Nigeria Ltd purchased machinery on 1 January 2020 for ₦58,600,000. The '
            'machinery will be used for ten years and sold at the end of the tenth year for an '
            'estimated ₦5,400,000. The year end is 31 December. Using the straight line method, '
            'show for the first five years the asset account, the allowance for depreciation '
            'account and extracts of the statements of profit or loss and financial position. '
            'Then show how the figures change if the reducing balance method at 10% is used '
            'instead.'}],
      'a': [
      {'h4': 'Straight line'},
      {'tex': '\\text{Annual charge} = \\frac{58{,}600{,}000 - 5{,}400{,}000}{10} = ₦5{,}320{,}000'},
      {'table': {'cap': 'Straight line (₦\'000)', 'align': 'lrrr',
        'head': ['Year', 'Charge', 'Accumulated depreciation', 'Carrying amount'], 'rows': [
        ['2020', '5,320', '5,320', '53,280'],
        ['2021', '5,320', '10,640', '47,960'],
        ['2022', '5,320', '15,960', '42,640'],
        ['2023', '5,320', '21,280', '37,320'],
        ['2024', '5,320', '26,600', '32,000'],
      ]}},
      {'p': 'The machinery account carries ₦58,600,000 forward unchanged; each year the allowance '
            'account is credited with ₦5,320,000 from profit or loss.'},
      {'h4': 'Reducing balance at 10%'},
      {'table': {'cap': 'Reducing balance at 10% (₦\'000)', 'align': 'lrrr',
        'head': ['Year', 'Charge (10% of opening CA)', 'Accumulated depreciation', 'Carrying amount'],
        'rows': [
        ['2020', '5,860.00', '5,860.00', '52,740.00'],
        ['2021', '5,274.00', '11,134.00', '47,466.00'],
        ['2022', '4,746.60', '15,880.60', '42,719.40'],
        ['2023', '4,271.94', '20,152.54', '38,447.46'],
        ['2024', '3,844.75', '23,997.29', '34,602.71'],
      ]}},
      {'warn': 'Under straight line the machine reaches its ₦5,400,000 residual value exactly at '
               'the end of year 10. Under reducing balance at 10% it **never** reaches the '
               'residual value, and the residual value is ignored in the calculation. Reducing '
               'balance is the wrong method where a definite residual value is expected at a '
               'definite date — the study text shows both only to contrast the pattern of '
               'charges. Some figures in the printed solution\'s profit-or-loss extract are '
               'mis-scanned (e.g. the 2020 charge shown as 5,274 rather than 5,860).'}]}},
    {'eg': {'tag': 'Illustration 9.9', 't': 'Dan Musa Ltd — several assets, part-year charges and '
      'disposals', 'open': True, 'q': [
      {'p': 'The following balances, all at cost, relate to assets acquired by Dan Musa Ltd on '
            '1 April 20-5: Plant & Machinery ₦360,000,000; Motor Vehicles ₦298,000,000; Equipment '
            '₦105,000,000.'},
      {'p': 'In the year to 31 December 20-8, additions were paid for by cheque: on 1 July, two '
            'delivery vans at ₦300,000,000 each and plant & machinery costing ₦250,000,000. On '
            '1 January 20-9 the plant & machinery bought on 1 April 20-5 and the motor vehicles '
            'bought on 1 April 20-5 were sold for ₦220,000,000 and ₦148,000,000 respectively.'},
      {'p': 'Depreciation is straight line: Plant & Machinery 10%, Motor Vehicles 20%, Equipment '
            '15%. Prepare, to 31 December 20-9: the Equipment account, the Plant & Machinery '
            'account, the Motor Vehicles account, and the provision for depreciation accounts for '
            'plant & machinery and for motor vehicles.'}],
      'a': [
      {'h4': 'W1 — depreciation charge each year (₦\'000)'},
      {'ul': [
        '**20-5** (9 months, 1 Apr–31 Dec): P&M $10\\%\\times360{,}000\\times\\tfrac{9}{12}=27{,}000$; '
        'MV $20\\%\\times298{,}000\\times\\tfrac{9}{12}=44{,}700$; Equipment '
        '$15\\%\\times105{,}000\\times\\tfrac{9}{12}=11{,}813$.',
        '**20-6 and 20-7** (full year on the original assets): P&M 36,000; MV 59,600; '
        'Equipment 15,750.',
        '**20-8**: originals — P&M 36,000, MV 59,600; plus a half-year on the 1 July additions — '
        'P&M $10\\%\\times250{,}000\\times\\tfrac{6}{12}=12{,}500$; MV '
        '$20\\%\\times600{,}000\\times\\tfrac{6}{12}=60{,}000$. Totals: P&M 48,500; MV 119,600.',
        '**20-9**: the original P&M and MV are sold on 1 January, so no charge on them. Charge '
        'only on assets still held — P&M addition $10\\%\\times250{,}000=25{,}000$; MV vans '
        '$20\\%\\times600{,}000=120{,}000$; Equipment 15,750.']},
      {'h4': 'W2 — accumulated depreciation on the assets sold (to 31 Dec 20-8)'},
      {'ul': [
        'Plant & Machinery: $27{,}000+36{,}000+36{,}000+36{,}000 = ₦135{,}000$ (₦\'000).',
        'Motor Vehicles: $44{,}700+59{,}600+59{,}600+59{,}600 = ₦223{,}500$ (₦\'000).']},
      {'h4': 'Plant & Machinery account (₦\'000)'},
      {'tacc': {'t': 'Plant & Machinery', 'dr': [
          ['20-8 Jan 1  Balance b/d', 360000],
          ['20-8 Jul 1  Bank', 250000],
          ['20-9 Jan 1  Balance b/d', 610000]],
        'cr': [['20-8 Dec 31  Balance c/d', 610000],
               ['20-9 Jan 1  Disposal account', 360000],
               ['20-9 Dec 31  Balance c/d', 250000]]}},
      {'h4': 'Motor Vehicles account (₦\'000)'},
      {'tacc': {'t': 'Motor Vehicles', 'dr': [
          ['20-8 Jan 1  Balance b/d', 298000],
          ['20-8 Jul 1  Bank', 600000],
          ['20-9 Jan 1  Balance b/d', 898000]],
        'cr': [['20-8 Dec 31  Balance c/d', 898000],
               ['20-9 Jan 1  Disposal account', 298000],
               ['20-9 Dec 31  Balance c/d', 600000]]}},
      {'h4': 'Equipment account (₦\'000)'},
      {'p': 'No additions or disposals — the account carries ₦105,000 forward from 1 April 20-5 '
            'to 31 December 20-9.'},
      {'h4': 'Provision for depreciation — Plant & Machinery (20-9 year, ₦\'000)'},
      {'p': 'The account builds up over 20-5 to 20-8 to a balance of ₦147,500 (27,000 + 36,000 + '
            '36,000 + 48,500). The final year:'},
      {'tacc': {'t': 'Provision for depreciation — P&M', 'dr': [
          ['20-9 Jan 1  Disposal account', 135000],
          ['20-9 Dec 31  Balance c/d', 37500],
          ['', 172500, '@tot']],
        'cr': [['20-9 Jan 1  Balance b/d', 147500],
               ['20-9 Dec 31  Profit or loss', 25000],
               ['', 172500, '@tot']]}},
      {'h4': 'Provision for depreciation — Motor Vehicles (20-9 year, ₦\'000)'},
      {'p': 'The account builds up over 20-5 to 20-8 to a balance of ₦283,500 (44,700 + 59,600 + '
            '59,600 + 119,600). The final year:'},
      {'tacc': {'t': 'Provision for depreciation — MV', 'dr': [
          ['20-9 Jan 1  Disposal account', 223500],
          ['20-9 Dec 31  Balance c/d', 180000],
          ['', 403500, '@tot']],
        'cr': [['20-9 Jan 1  Balance b/d', 283500],
               ['20-9 Dec 31  Profit or loss', 120000],
               ['', 403500, '@tot']]}},
      {'h4': 'Disposal accounts (₦\'000)'},
      {'tacc': {'t': 'Plant & Machinery disposal', 'dr': [
          ['Plant & Machinery at cost', 360000], ['', 360000, '@tot']],
        'cr': [['Provision for depreciation', 135000], ['Bank (proceeds)', 220000],
               ['Loss on disposal to P/L', 5000], ['', 360000, '@tot']]}},
      {'tacc': {'t': 'Motor Vehicles disposal', 'dr': [
          ['Motor Vehicles at cost', 298000], ['Profit on disposal to P/L', 73500],
          ['', 371500, '@tot']],
        'cr': [['Provision for depreciation', 223500], ['Bank (proceeds)', 148000],
               ['', 371500, '@tot']]}},
      {'warn': 'The plant & machinery is sold at a **loss of ₦5m** (carrying amount 225 − proceeds '
               '220); the motor vehicles at a **profit of ₦73.5m** (proceeds 148 − carrying amount '
               '74.5). The study text\'s printed disposal accounts are badly corrupted in the '
               'scan (they show a ₦145,000 provision transfer and figures that do not cross-cast); '
               'the workings above are internally consistent — follow the method.'}]}},
  ]},

  {'n': '9.10', 't': 'End-of-chapter questions (study text)', 'b': [
    {'p': 'Every question from the study text\'s own end-of-chapter set, with its answer key. '
          'The multiple-choice and short-answer questions first, then the three examination-type '
          'questions with worked solutions.'},
    {'h3': 'Multiple-choice and short-answer questions'},
    {'eg': {'tag': 'Study text Q1–Q10', 't': 'Questions with the study text\'s answers', 'open': True,
      'q': [
      {'ol': [
        'A non-current asset to one company may be a current asset to another company. '
        '(a) True  (b) False',
        'Expenditure which brings short-term benefit to a business entity will normally be '
        'classified as … (a) Revenue expenditure  (b) Tangible assets  (c) Capital expenditure',
        'Which among these is a tangible non-current asset? (a) Goodwill  (b) Copyright  '
        '(c) Plant  (d) Brand',
        'Depreciation of an asset with a fixed period of legal life is often referred to as? '
        '(a) Obsolescence  (b) Amortization  (c) Diminishing balance  (d) Depletion',
        'An increase in the value of a non-current asset over and above its original cost is '
        'termed? (a) Depreciation  (b) Appreciation  (c) Inflation  (d) Residual value',
        'The main reason for depreciating an asset is to provide funds for the replacement of '
        'the asset at the end of its useful life. (a) True  (b) False',
        'Depreciable amount of a non-current asset is … (a) Carrying amount  (b) Cost less '
        'residual value  (c) Residual value plus carrying amount  (d) Residual value less '
        'carrying amount',
        'State three basic methods of calculating depreciation.',
        'What are the causes of depreciation?',
        'In the first year of use of a non-current asset, the depreciation charge will be the '
        'same for both the straight line and the reducing balance method. (a) True  (b) False',
      ]}],
      'a': [
      {'ol': [
        '**(a) True.** A vehicle is a non-current asset to a haulier but trading inventory to a '
        'car dealer — classification depends on the holder\'s intended use.',
        '**(a) Revenue expenditure.** Short-term benefit, consumed within the period.',
        '**(c) Plant.** The other three are intangible.',
        '**(b) Amortization** — the term used for writing off intangibles and assets with a '
        'fixed legal life such as a lease or patent.',
        '**(b) Appreciation.**',
        '**(b) False.** Depreciation allocates cost to the periods that benefit; it sets aside no '
        'cash and creates no replacement fund.',
        '**(b) Cost less residual value.**',
        'Straight line; reducing (diminishing) balance; sum-of-the-years\'-digits.',
        'Wear and tear from usage; passage of time (effluxion of time); environmental / physical '
        'factors; obsolescence; exhaustion (depletion of a wasting asset).',
        '**(a) True**, per the study text\'s answer key — the reasoning is that in year 1 both '
        'methods apply their percentage to the same base (cost), so if the *same rate* is used '
        'the charge is identical. In general, though, the two methods use different rates and '
        'the year-1 charges differ; take the study text\'s answer as reflecting its own stated '
        'assumption.'],
      }]}},
    {'h3': 'Examination-type question 1 — Baba Mensa'},
    {'eg': {'tag': 'Study text', 't': 'Baba Mensa — motor vehicles with two disposals', 'open': True,
      'q': [
      {'p': 'Baba Mensa has been in business for several years. The following balances were '
            'extracted from his books on 31 December 20-5: Motor vehicle at cost ₦10,000,000; '
            'Provision for depreciation on motor vehicle ₦4,500,000. During the years 20-5 to '
            '20-8 the following took place:'},
      {'ol': [
        'On 30 April 20-6 a motor vehicle which cost ₦3,800,000 (purchased on 1 January 20-4) '
        'was sold for ₦1,260,000.',
        'On 1 January 20-8 an additional motor vehicle was bought for ₦5,200,000.',
        'On 1 September 20-8 a motor vehicle which was bought on 1 January 20-6 for ₦4,200,000 '
        'was sold for ₦2,950,000.',
      ]},
      {'p': 'Depreciation is charged at 20% per annum on cost; no depreciation is charged in the '
            'year of disposal. Write up, for all the relevant years: (a) the Motor Vehicle '
            'account, (b) the Provision for Depreciation account, (c) the Motor Vehicle Disposal '
            'accounts.'}],
      'a': [
      {'warn': 'The question as printed is internally inconsistent — item (iii) dates the '
               '₦4,200,000 vehicle to 1 January 20-6, but the study text\'s own answer treats it '
               'as part of the opening ₦10,000,000 balance and depreciates it for only two years '
               '(20-6 and 20-7). The study text\'s answer is reproduced below; follow its method.'},
      {'h4': 'Workings (₦\'000)'},
      {'ul': [
        '20-6 charge $= 20\\% \\times (10{,}000 - 3{,}800) = 1{,}240$.',
        '20-7 charge $= 20\\% \\times 6{,}200 = 1{,}240$.',
        '20-8 charge $= 20\\% \\times (6{,}200 + 5{,}200 - 4{,}200) = 1{,}440$.',
        'Accumulated depreciation on the 20-6 disposal $= 20\\% \\times 3{,}800 \\times 2 '
        '\\text{ years (20-4, 20-5)} = 1{,}520$.',
        'Accumulated depreciation on the 20-8 disposal $= 20\\% \\times 4{,}200 \\times 2 '
        '\\text{ years (20-6, 20-7)} = 1{,}680$.']},
      {'tacc': {'t': 'Motor Vehicle account (₦\'000)', 'dr': [
          ['20-6 Jan 1  Balance b/d', 10000],
          ['20-8 Jan 1  Bank', 5200]],
        'cr': [['20-6 Apr 30  Disposal', 3800],
               ['20-8 Sep 1  Disposal', 4200],
               ['20-8 Dec 31  Balance c/d', 7200]]}},
      {'tacc': {'t': 'Provision for depreciation account (₦\'000)', 'dr': [
          ['20-6 Apr 30  Disposal', 1520],
          ['20-7 Dec 31  Balance c/d', 4220],
          ['20-8 Sep 1  Disposal', 1680],
          ['20-8 Dec 31  Balance c/d', 5220]],
        'cr': [['20-6 Jan 1  Balance b/d', 4500],
               ['20-6 Dec 31  Profit or loss', 1240],
               ['20-7 Jan 1  Balance b/d', 4220],
               ['20-7 Dec 31  Profit or loss', 1240],
               ['20-8 Jan 1  Balance b/d', 5460],
               ['20-8 Dec 31  Profit or loss', 1440]]}},
      {'tacc': {'t': '20-6 Disposal account (₦\'000)', 'dr': [
          ['Motor vehicle at cost', 3800], ['', 3800, '@tot']],
        'cr': [['Provision for depreciation', 1520], ['Bank (proceeds)', 1260],
               ['Loss on disposal to P/L', 1020], ['', 3800, '@tot']]}},
      {'tacc': {'t': '20-8 Disposal account (₦\'000)', 'dr': [
          ['Motor vehicle at cost', 4200], ['Profit on disposal to P/L', 430],
          ['', 4630, '@tot']],
        'cr': [['Provision for depreciation', 1680], ['Bank (proceeds)', 2950],
               ['', 4630, '@tot']]}}]}},
    {'h3': 'Examination-type question 2 — Emeka Kofi Enterprise'},
    {'eg': {'tag': 'Study text', 't': 'Emeka Kofi Enterprise — reducing balance with a disposal',
      'open': True, 'q': [
      {'p': 'An extract from the books of Emeka Kofi Enterprise as at 31 December 20-6: Equipment '
            'at cost ₦250,000,000; Carrying amount at 31/12/20-6 ₦156,978,000. Depreciation is '
            'provided on equipment at 15% per annum on the reducing balance basis, calculated on '
            'assets in use at the end of the year. In 20-7: (i) equipment which cost ₦43,750,000 '
            'and had been used for four years was sold for ₦30,000,000; (ii) new equipment '
            'costing ₦50,000,000 was purchased on 1 January 20-7. Prepare, for 20-7: (a) the '
            'Equipment account, (b) the Provision for Depreciation account, (c) the Equipment '
            'Disposal account.'}],
      'a': [
      {'h4': 'Workings (₦\'000)'},
      {'ul': [
        'Accumulated depreciation at 31/12/20-6 $= 250{,}000 - 156{,}978 = 93{,}022$.',
        'Carrying amount of the equipment sold — reduce ₦43,750 by 15% for four years: '
        '43,750 → 37,188 → 31,609 → 26,868 → **22,838**. Accumulated depreciation on it '
        '$= 43{,}750 - 22{,}838 = 20{,}912$.',
        '20-7 charge $= 15\\% \\times \\big[(156{,}978 - 22{,}838) + 50{,}000\\big] = 15\\% \\times '
        '184{,}140 = 27{,}621$.']},
      {'tacc': {'t': 'Equipment account (₦\'000)', 'dr': [
          ['20-7 Jan 1  Balance b/d', 250000],
          ['20-7 Jan 1  Bank', 50000],
          ['', 300000, '@tot']],
        'cr': [['20-7 Dec 31  Disposal account', 43750],
               ['20-7 Dec 31  Balance c/d', 256250],
               ['', 300000, '@tot']]}},
      {'tacc': {'t': 'Provision for depreciation account (₦\'000)', 'dr': [
          ['20-7 Dec 31  Disposal account', 20912],
          ['20-7 Dec 31  Balance c/d', 99731],
          ['', 120643, '@tot']],
        'cr': [['20-7 Jan 1  Balance b/d', 93022],
               ['20-7 Dec 31  Profit or loss', 27621],
               ['', 120643, '@tot']]}},
      {'tacc': {'t': 'Equipment disposal account (₦\'000)', 'dr': [
          ['Equipment at cost', 43750], ['Profit on disposal to P/L', 7162],
          ['', 50912, '@tot']],
        'cr': [['Provision for depreciation', 20912], ['Bank (proceeds)', 30000],
               ['', 50912, '@tot']]}},
      {'note': 'The study text\'s printed Equipment account does not cross-cast (it shows a '
               'balance c/d of 206,250 against a debit side of 300,000). The balance carried down '
               'is ₦256,250 (₦\'000): 250,000 + 50,000 − 43,750.'}]}},
    {'h3': 'Examination-type question 3 — Tunde Kwame'},
    {'eg': {'tag': 'Study text', 't': 'Tunde Kwame — two asset classes, additions and disposals',
      'open': True, 'q': [
      {'p': 'The following were extracted from the books of Tunde Kwame as at 31 December 20-4: '
            'Plant & Machinery at cost ₦180,000,000; Motor Vehicle at cost ₦156,000,000; '
            'Provision for depreciation — Plant & Machinery ₦10,000,000, Motor Vehicles '
            '₦6,000,000. Additions were acquired by cheque:'},
      {'ol': [
        'On 31 March 20-5, two delivery trucks at ₦4,000,000 each and a plant for ₦10,000,000.',
        'On 1 April 20-6, one saloon car at ₦5,000,000 and four machines at ₦5,000,000 each.',
        'On 30 June 20-6, two machines purchased on 1 January 20-2 at ₦3,000,000 each were sold '
        'for ₦1,700,000 and ₦1,300,000 respectively; and one saloon car purchased on 1 January '
        '20-3 for ₦4,000,000 was auctioned for ₦3,000,000.',
      ]},
      {'p': 'Tunde Kwame depreciates motor vehicles at 15% and plant & machinery at 10% per '
            'annum on the straight line method. Write up, to 31 December 20-7: (a) the Plant & '
            'Machinery account, (b) the Motor Vehicles account, (c) the provision for '
            'depreciation accounts, (d) the disposal accounts.'}],
      'a': [
      {'h4': 'Workings — depreciation charge (₦\'000)'},
      {'ul': [
        '20-5: P&M $= 10\\%\\times180{,}000 + 10\\%\\times10{,}000\\times\\tfrac{9}{12} = 18{,}750$; '
        'MV $= 15\\%\\times156{,}000 + 15\\%\\times8{,}000\\times\\tfrac{9}{12} = 24{,}300$.',
        '20-6: P&M $= 10\\%\\times(190{,}000 - 6{,}000) + 10\\%\\times20{,}000\\times\\tfrac{9}{12} '
        '= 19{,}900$; MV $= 15\\%\\times(164{,}000 - 4{,}000) + 15\\%\\times5{,}000\\times'
        '\\tfrac{9}{12} = 24{,}563$.',
        '20-7: P&M $= 10\\%\\times204{,}000 = 20{,}400$; MV $= 15\\%\\times165{,}000 = 24{,}750$.',
        'Accumulated depreciation on disposals: P&M $= 10\\%\\times6{,}000\\times4 '
        '\\text{ years} = 2{,}400$; MV $= 15\\%\\times4{,}000\\times3\\text{ years} = 1{,}800$.']},
      {'tacc': {'t': 'Plant & Machinery account (₦\'000)', 'dr': [
          ['20-6 Jan 1  Balance b/d', 190000],
          ['20-6 Apr 1  Bank', 20000],
          ['20-7 Jan 1  Balance b/d', 204000]],
        'cr': [['20-6 Jun 30  Disposal account', 6000],
               ['20-6 Dec 31  Balance c/d', 204000],
               ['20-7 Dec 31  Balance c/d', 204000]]}},
      {'tacc': {'t': 'Motor Vehicles account (₦\'000)', 'dr': [
          ['20-6 Jan 1  Balance b/d', 164000],
          ['20-6 Apr 1  Bank', 5000],
          ['20-7 Jan 1  Balance b/d', 165000]],
        'cr': [['20-6 Jun 30  Disposal account', 4000],
               ['20-6 Dec 31  Balance c/d', 165000],
               ['20-7 Dec 31  Balance c/d', 165000]]}},
      {'tacc': {'t': 'Provision for depreciation — Plant & Machinery (₦\'000)', 'dr': [
          ['20-6 Jun 30  Disposal account', 2400],
          ['20-6 Dec 31  Balance c/d', 46250],
          ['20-7 Dec 31  Balance c/d', 66650]],
        'cr': [['20-5 Dec 31  Balance c/d then b/d', 28750],
               ['20-6 Dec 31  Profit or loss', 19900],
               ['20-7 Jan 1  Balance b/d', 46250],
               ['20-7 Dec 31  Profit or loss', 20400]]}},
      {'tacc': {'t': 'Provision for depreciation — Motor Vehicles (₦\'000)', 'dr': [
          ['20-6 Jun 30  Disposal account', 1800],
          ['20-6 Dec 31  Balance c/d', 53063],
          ['20-7 Dec 31  Balance c/d', 77813]],
        'cr': [['20-5 Dec 31  Balance c/d then b/d', 30300],
               ['20-6 Dec 31  Profit or loss', 24563],
               ['20-7 Jan 1  Balance b/d', 53063],
               ['20-7 Dec 31  Profit or loss', 24750]]}},
      {'tacc': {'t': 'Plant & Machinery disposal (₦\'000)', 'dr': [
          ['Plant & Machinery at cost', 6000], ['', 6000, '@tot']],
        'cr': [['Provision for depreciation', 2400], ['Bank (1,700 + 1,300)', 3000],
               ['Loss on disposal to P/L', 600], ['', 6000, '@tot']]}},
      {'tacc': {'t': 'Motor Vehicle disposal (₦\'000)', 'dr': [
          ['Motor Vehicle at cost', 4000], ['Profit on disposal to P/L', 800],
          ['', 4800, '@tot']],
        'cr': [['Provision for depreciation', 1800], ['Bank (proceeds)', 3000],
               ['', 4800, '@tot']]}},
      {'p': 'The ₦10,000,000 opening balance b/d on the P&M provision account and the ₦6,000,000 '
            'on the MV provision account are added to the 20-5 charge to give the 20-5 closing '
            'balances of ₦28,750 and ₦30,300 (₦\'000) shown above.'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Straight line depreciation',
   'tex': '\\text{Charge} = \\frac{\\text{Cost} - \\text{Residual value}}{\\text{Useful life}}'},
  {'lb': 'Reducing balance depreciation',
   'tex': '\\text{Charge}_t = r \\times \\text{Carrying amount}_{t-1}'},
  {'lb': 'Reducing balance rate from residual value',
   'tex': 'r = 1 - \\sqrt[n]{\\frac{\\text{Residual value}}{\\text{Cost}}}'},
  {'lb': 'Sum of the digits',
   'tex': '\\text{Charge}_t = \\frac{n - t + 1}{\\tfrac{n(n+1)}{2}} \\times '
          '(\\text{Cost} - \\text{RV})'},
  {'lb': 'Units of production',
   'tex': '\\text{Charge} = \\frac{\\text{Cost} - \\text{RV}}{\\text{Total expected output}} '
          '\\times \\text{Output for the year}'},
  {'lb': 'Profit or loss on disposal',
   'tex': '\\text{Profit} = \\text{Net proceeds} - (\\text{Cost} - \\text{Accumulated depreciation})'},
 ],
 'focus':
   'The most heavily examined chapter in the paper. It appears in Section B almost every diet, '
   'usually as a non-current asset schedule with additions, disposals and a depreciation policy, '
   'and often with a revaluation attached. Section A tests single computations: a part-year '
   'charge, a loss on disposal, what to include in cost. Master the asset schedule layout — it '
   'carries presentation marks even when an arithmetic figure is wrong.',
 'errors': [
   'Deducting residual value before applying a reducing balance rate. Reducing balance applies to '
   'the carrying amount.',
   'Ignoring the stated part-year policy and pro-rating anyway (or vice versa).',
   'Crediting a revaluation surplus to profit or loss instead of other comprehensive income.',
   'Netting a part-exchange allowance against the cost of the new asset.',
   'Capitalising staff training, maintenance contracts or relocation costs.',
   'Forgetting to remove the accumulated depreciation on a disposed asset from the schedule.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A machine cost ₦9,000,000 with a residual value of ₦1,000,000 and a useful life of 5 '
         'years. Using the straight line method, the annual charge is',
    'o': ['₦1,800,000', '₦1,600,000', '₦2,000,000', '₦1,500,000', '₦1,700,000'],
    'a': 1,
    'w': 'The depreciable amount is cost less residual value, spread evenly over the life.',
    'calc': '\\frac{9{,}000{,}000 - 1{,}000{,}000}{5} = 1{,}600{,}000',
    'src': 'Chapter 9.2'},
   {'q': 'An asset with a carrying amount of ₦2,600,000 was sold for ₦2,150,000. The result is',
    'o': ['a profit of ₦450,000', 'a loss of ₦450,000', 'a profit of ₦2,150,000',
          'a loss of ₦2,600,000', 'no gain or loss'],
    'a': 1,
    'w': 'Proceeds below carrying amount give a loss on disposal, charged to profit or loss.',
    'calc': '2{,}150{,}000 - 2{,}600{,}000 = -450{,}000',
    'src': 'Chapter 9.3'},
   {'q': 'A building with a carrying amount of ₦28,000,000 is revalued to ₦41,000,000. The '
         'surplus of ₦13,000,000 is',
    'o': ['credited to profit or loss',
          'credited to other comprehensive income and held in a revaluation surplus',
          'credited to retained earnings directly',
          'ignored until the building is sold',
          'credited to share premium'],
    'a': 1,
    'w': 'IAS 16 requires an upward revaluation to go to other comprehensive income and accumulate '
         'in equity as a revaluation surplus. It reaches profit or loss only where it reverses an '
         'earlier decrease charged there.',
    'src': 'Chapter 9.4'},
   {'q': 'Which of the following should NOT be capitalised as part of the cost of a machine?',
    'o': ['Delivery charges', 'Installation and testing costs',
          'Staff training on how to operate it', 'Site preparation costs',
          'Non-refundable import duty'],
    'a': 2,
    'w': 'Training benefits the staff, whom the entity does not control, so it fails the '
         'definition of an asset. The other four are directly attributable to bringing the '
         'machine to working condition.',
    'src': 'Chapter 9.1'},
   {'q': 'A vehicle costing ₦5,000,000 is depreciated at 25% on the reducing balance. Its '
         'carrying amount at the end of year 3 is',
    'o': ['₦1,250,000', '₦2,109,375', '₦2,812,500', '₦1,875,000', '₦3,750,000'],
    'a': 1,
    'w': 'Apply 25% to the carrying amount each year, or use the factor directly.',
    'calc': '5{,}000{,}000 \\times (1 - 0.25)^3 = 5{,}000{,}000 \\times 0.421875 = 2{,}109{,}375',
    'src': 'Chapter 9.2'},
   {'q': 'Treating the cost of repairing a delivery van as capital expenditure will',
    'o': ['understate profit and understate assets', 'overstate profit and overstate assets',
          'overstate profit and understate assets', 'understate profit and overstate assets',
          'have no effect on profit'],
    'a': 1,
    'w': 'The repair should have been an expense. Capitalising it removes the expense (overstating '
         'profit) and adds a non-existent asset (overstating assets). It is an error of principle.',
    'src': 'Chapter 9.6'},
   {'q': 'Research expenditure under IAS 38 is',
    'o': ['always capitalised', 'always written off as incurred',
          'capitalised if the six conditions are met', 'capitalised and amortised over five years',
          'charged to other comprehensive income'],
    'a': 1,
    'w': 'Research is always expensed because future benefits cannot be demonstrated. Only '
         '**development** expenditure meeting all six conditions may be capitalised.',
    'src': 'Chapter 9.5'},
   {'q': 'Depreciation of an asset that has a fixed period of legal life (a lease or a patent) '
         'is referred to as',
    'o': ['obsolescence', 'amortization', 'diminishing balance', 'depletion', 'appreciation'],
    'a': 1,
    'w': 'Amortization is the term used for writing off an intangible asset or an asset with a '
         'fixed legal life. Depletion is the equivalent for a wasting asset such as a mine.',
    'src': 'Chapter 9.10 (study text Q4)'},
   {'q': 'An increase in the value of a non-current asset over and above its original cost is '
         'termed',
    'o': ['depreciation', 'appreciation', 'inflation', 'residual value', 'revaluation surplus'],
    'a': 1,
    'w': 'Appreciation is a rise in value above cost. (A formal upward revaluation recognised '
         'under IAS 16 produces a revaluation *surplus*, but the general term the study text '
         'wants here is appreciation.)',
    'src': 'Chapter 9.10 (study text Q5)'},
   {'q': 'The depreciable amount of a non-current asset is',
    'o': ['the carrying amount', 'cost less residual value',
          'residual value plus carrying amount', 'residual value less carrying amount',
          'cost less accumulated depreciation'],
    'a': 1,
    'w': 'Depreciable amount is cost (or revalued amount) less residual value — the total to be '
         'spread over the useful life.',
    'src': 'Chapter 9.10 (study text Q7)'},
   {'q': 'An asset that cost ₦43,750,000 has been depreciated at 15% per annum on the reducing '
         'balance for four years. Its carrying amount is approximately',
    'o': ['₦17,500,000', '₦22,838,000', '₦26,868,000', '₦19,688,000', '₦37,188,000'],
    'a': 1,
    'w': 'Reduce by 15% four times: 43,750 → 37,188 → 31,609 → 26,868 → 22,838 (₦\'000).',
    'calc': '43{,}750{,}000 \\times (1 - 0.15)^4 = 43{,}750{,}000 \\times 0.52200625 \\approx '
            '22{,}838{,}000',
    'src': 'Chapter 9.10 (examination-type Q2)'},
  ],
  'theory': [
   {'q': 'Explain what is meant by depreciation, state FOUR causes of depreciation, and explain '
         'why depreciation is not a source of funds for replacing the asset.',
    'marks': 8,
    'a': [
      {'p': '**Depreciation** is the systematic allocation of the depreciable amount of an asset '
            'over its useful life, the depreciable amount being cost (or revalued amount) less '
            'residual value. It applies the accruals concept: the cost of a non-current asset is '
            'matched against the periods that benefit from its use.'},
      {'h4': 'Causes'},
      {'ol': [
        '**Physical wear and tear** through use.',
        '**Passage of time**, which matters for assets held under a lease or a fixed-term right.',
        '**Obsolescence** — a newer technology makes the asset uneconomic even though it still works.',
        '**Depletion** — extraction reduces a wasting asset such as a mine or quarry.',
        '**Inadequacy** — the asset is no longer large enough for the scale of operations.']},
      {'h4': 'Why it is not a fund'},
      {'p': 'The entries are **Dr** depreciation expense and **Cr** accumulated depreciation. '
            'Neither is a cash account, so no money is set aside. Depreciation reduces reported '
            'profit and therefore reduces the amount legally available for distribution, which '
            'may indirectly leave more cash in the business; but it creates no fund, and unless '
            'management separately invests that cash there will be nothing available when the '
            'asset must be replaced. Replacement also costs current prices, not historical cost, '
            'so accumulated depreciation would in any case be insufficient.'}],
    'src': 'Chapter 9.2'},
   {'q': 'Distinguish between capital and revenue expenditure, and state the effect on the '
         'financial statements of treating revenue expenditure as capital expenditure.',
    'marks': 6,
    'a': [
      {'table': {'head': ['', 'Capital expenditure', 'Revenue expenditure'], 'align': 'lll',
        'rows': [
        ['Purpose', 'To acquire, improve or extend a non-current asset',
         'To maintain the existing earning capacity'],
        ['Benefit period', 'More than one accounting period', 'The current period only'],
        ['Where charged', 'Capitalised in the statement of financial position',
         'Expensed in the statement of profit or loss'],
        ['Recovered through', 'Depreciation over the useful life', 'Immediately, in full'],
        ['Examples', 'Purchase of plant, building extension, legal fees on acquiring land',
         'Repairs, insurance, wages, repainting'],
      ]}},
      {'h4': 'Effect of misclassification'},
      {'ol': [
        'Profit for the current year is **overstated**, because the expense has been removed from '
        'profit or loss.',
        'Non-current assets and therefore net assets and equity are **overstated**.',
        'Depreciation is charged in later years on an amount that should never have been '
        'capitalised, so profit in each of those years is **understated** — the error unwinds '
        'slowly rather than correcting itself.',
        'It is an **error of principle**, so the trial balance still agrees and the error will not '
        'be found by checking the arithmetic.']}],
    'src': 'Chapter 9.6'},
  ]},
}
