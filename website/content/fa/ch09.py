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
