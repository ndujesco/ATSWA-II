CH = {
 'n': 7,
 't': 'Accounting Policies, Estimates and Errors (IAS 8)',
 'brief': 'When a change is a policy and when it is an estimate, and why that distinction '
          'decides whether prior years are restated.',
 'outcomes': [
   'Distinguish an accounting policy from an accounting estimate',
   'Apply the criteria for changing an accounting policy',
   'Account for a change in policy retrospectively',
   'Account for a change in estimate prospectively',
   'Correct a material prior period error and state the disclosures required',
 ],
 'secs': [
  {'n': '7.1', 't': 'The three things IAS 8 deals with', 'b': [
    {'table': {'head': ['', 'What it is', 'How it is applied', 'Prior years'],
     'align': 'llll', 'rows': [
      ['**Change of policy**', 'A change in the basis of recognition, measurement or presentation',
       'Retrospectively', 'Restated'],
      ['**Change of estimate**', 'A revision of a judgement about an uncertain amount',
       'Prospectively', 'Untouched'],
      ['**Prior period error**', 'An omission or misstatement in a previous period',
       'Retrospectively', 'Restated'],
    ]}},
    {'key': 'Two of the three are retrospective, one is not. If you remember only one thing from '
            'this chapter, remember that a change of **estimate is never backdated**.'},
  ]},

  {'n': '7.2', 't': 'The objectives of IAS 8', 'b': [
    {'p': '**IAS 8** deals with the selection of, and changes in, accounting policies, together '
          'with the disclosure of such changes. It also sets out the requirements and disclosure '
          'for changes in accounting estimates and the correction of errors. The standard states '
          'its own objectives explicitly:'},
    {'ol': [
      'to **enhance the relevance and reliability** of an entity\'s financial statements; and',
      'to **ensure comparability** of the financial statements of an entity over time, as well as '
      'with the financial statements of other entities.',
    ]},
    {'key': 'Every rule in the rest of this chapter — why a policy change is backdated, why an '
            'estimate is not, why an error is corrected quietly through opening equity rather than '
            'through this year\'s profit — exists in service of one or the other of those two '
            'objectives. If you are ever unsure how IAS 8 wants something treated, ask which of '
            'these two goals the treatment protects.'},
  ]},

  {'n': '7.3', 't': 'Accounting policies', 'b': [
    {'def': {'t': 'Accounting policies', 'd': 'the specific principles, bases, conventions, rules '
                  'and practices applied by an entity in preparing and presenting financial statements.'}},
    {'p': 'Accounting policies are important for a better understanding of the financial '
          'statements prepared by the management of an entity. Under IFRS, alternative treatments '
          'are often possible, which makes it all the more important for an entity to state '
          'clearly which accounting policy it has used in preparing its financial statements. '
          'Examples of accounting policies include:'},
    {'ul': [
      'valuation of inventory using FIFO, weighted average cost, or another suitable basis, as '
      'permitted by IAS 2 (Chapter 12); and',
      'the timing of recognition of assets, liabilities, expenses and income — for example, '
      'whether property, plant and equipment is subsequently measured on the cost basis or the '
      'revaluation basis.',
    ]},
    {'p': 'Where a standard applies to a transaction, the policy is dictated by that standard, so '
          'that the entity can identify trends in its own financial performance or position over '
          'time. Where **no standard presently exists** for the item, management must develop and '
          'apply a policy that is reliable and relevant to the decision-making needs of users.'},
    {'h3': 'What makes a policy "reliable"'},
    {'p': 'An accounting policy shall be considered reliable if it:'},
    {'ol': [
      'represents faithfully the financial position, the performance and the cash flows, and '
      'reflects the economic substance of transactions, other events and conditions — not merely '
      'their legal form;',
      'is **neutral** — free from bias;',
      'is **prudent** — exercises caution under uncertainty; and',
      'is **complete** in all material respects, comparable, and understandable.',
    ]},
    {'note': 'Notice this reliability test is really the Conceptual Framework\'s faithful '
             'representation criterion (Chapter 2 §2.3), applied specifically to the choice of an '
             'accounting policy rather than to a single figure. Where no standard directly '
             'addresses an item, an entity may also look to the most recent pronouncements of '
             'other similar standard-setting bodies, other accounting literature, and accepted '
             'industry practice, provided these do not conflict with an IFRS or the Conceptual '
             'Framework itself.'},
    {'h3': 'Consistency of accounting policies'},
    {'p': 'Entities are required to apply the accounting policies they select **consistently**, '
          'for similar transactions, events and conditions. Where a standard permits items to be '
          'categorised in more than one way — for example, into different classes of property, '
          'plant and equipment — an accounting policy must be selected and then used consistently '
          'for each category.'},
    {'h3': 'When may a policy be changed?'},
    {'ol': [
      'The change is **required by a standard or interpretation**; or',
      'The change results in financial statements providing **reliable and more relevant** '
      'information about the effects of transactions on the entity\'s position or performance.',
    ]},
    {'warn': 'Nothing else will do. A change made to smooth or improve reported profit fails both '
             'tests, and is a breach of both IAS 8 and the neutrality component of faithful '
             'representation.'},
    {'h3': 'Retrospective application'},
    {'steps': [
      'Adjust the **opening balance of retained earnings** of the earliest period presented, as '
      'if the new policy had always been applied.',
      'Restate the **comparative amounts** for each prior period presented.',
      'Present a **third statement of financial position** at the beginning of the earliest '
      'comparative period.',
    ]},
    {'p': 'Where it is impracticable to determine the effect for a particular prior period, the '
          'entity applies the new policy from the earliest period for which it is practicable and '
          'discloses that fact.'},
    {'h3': 'Examples of policy changes'},
    {'ul': [
      'Changing the inventory cost formula from FIFO to weighted average cost.',
      'Changing from the cost model to the revaluation model for property, plant and equipment '
      '(though IAS 16 requires this one to be applied prospectively as a revaluation).',
      'Changing the basis of presenting expenses from by-nature to by-function.',
    ]},
    {'eg': {'t': 'A change of policy', 'q': [
      {'p': 'Ekiti Ltd changed from FIFO to weighted average cost for inventory with effect from '
            '1 January 2024, because the new basis better reflects the physical flow. The effect '
            'was to reduce inventory at 31 December 2022 by ₦180,000 and at 31 December 2023 by '
            '₦260,000. Retained earnings at 1 January 2023 were ₦5,400,000 as previously reported '
            'and profit for 2023 was ₦1,900,000. How is this presented?'}],
      'a': [
      {'p': 'The change is retrospective. Restate as if weighted average had always applied.'},
      {'stmt': {'t': 'Statement of changes in equity extract', 'sub': 'retained earnings', 'rows': [
        ['Balance at 1 January 2023 as previously reported', 5400000],
        ['Effect of change in accounting policy', -180000],
        ['Balance at 1 January 2023 as restated', 5220000, '@t'],
        '@gap',
        ['Profit for 2023 as previously reported', 1900000],
        ['Effect on 2023 profit (260,000 − 180,000)', -80000],
        ['Profit for 2023 as restated', 1820000, '@t'],
        ['Balance at 31 December 2023 as restated', 7040000, '@tt'],
      ]}},
      {'note': 'The **cumulative** effect at the start of the earliest period presented adjusts '
               'opening retained earnings; the **incremental** effect of ₦80,000 restates that '
               'year\'s profit. Confusing the two is the standard error here — the ₦260,000 is '
               'never charged in full against a single year.'}]}},
  ]},

  {'n': '7.4', 't': 'Accounting estimates', 'b': [
    {'def': {'t': 'Accounting estimate', 'd': 'a monetary amount in the financial statements that '
                  'is subject to measurement uncertainty.'}},
    {'p': 'Estimates are not errors. They are the unavoidable consequence of reporting on '
          'incomplete information, and revising one as better information arrives is normal, '
          'proper practice — not a correction of anything.'},
    {'h3': 'Common estimates'},
    {'ul': [
      'Useful lives and residual values of non-current assets, and the depreciation method.',
      'The allowance for doubtful debts.',
      'The net realisable value of inventory.',
      'Provisions for warranty obligations and legal claims.',
      'Fair values where no quoted price exists.',
    ]},
    {'h3': 'Prospective application'},
    {'p': 'The effect of a change in estimate is recognised in the **period of the change**, and '
          'in future periods if the change affects them too. Prior periods are never restated.'},
    {'eg': {'t': 'Change in useful life', 'q': [
      {'p': 'A machine costing ₦12,000,000 with no residual value was being depreciated over ten '
            'years on the straight line basis. At the start of year 4, the remaining useful life '
            'was revised to four more years. Compute the depreciation charge for year 4.'}],
      'a': [
      {'p': 'Depreciation charged in years 1 to 3 was $12{,}000{,}000 \\div 10 = ₦1{,}200{,}000$ '
            'a year, so accumulated depreciation is ₦3,600,000.'},
      {'tex': '\\text{Carrying amount at start of year 4} = 12{,}000{,}000 - 3{,}600{,}000 '
              '= ₦8{,}400{,}000'},
      {'tex': '\\text{Revised annual charge} = \\frac{8{,}400{,}000}{4} = ₦2{,}100{,}000'},
      {'note': 'Years 1 to 3 are left exactly as reported. The unrecovered carrying amount is '
               'simply spread over the newly estimated remaining life. Restating the earlier '
               'years would be wrong — the earlier estimate was the best available at the time.'}]}},
    {'note': 'Where a change is genuinely hard to classify, IAS 8 says treat it as a **change in '
             'estimate**. That default is itself examinable.'},
  ]},

  {'n': '7.5', 't': 'Prior period errors', 'b': [
    {'def': {'t': 'Prior period error', 'd': 'an omission from, or misstatement in, the financial '
                  'statements of one or more prior periods arising from a failure to use, or '
                  'misuse of, reliable information that was available and could reasonably have '
                  'been expected to have been obtained.'}},
    {'p': 'The definition contains the test. If the information **was available** and was not '
          'used, it is an error. If it was not available, the figure was an estimate and its '
          'revision is a change of estimate.'},
    {'h3': 'Correcting a material error'},
    {'ol': [
      'Restate the comparative amounts for the prior period in which the error occurred; or',
      'If the error occurred before the earliest period presented, restate the opening balances '
      'of assets, liabilities and equity for that earliest period.',
    ]},
    {'p': 'The correction is **never** put through the profit or loss of the current period.'},
    {'h3': 'Disclosures required'},
    {'ul': [
      'The nature of the error.',
      'The amount of the correction for each prior period presented, and for each line item '
      'affected, with the effect on earnings per share where applicable.',
      'The amount of the correction at the beginning of the earliest period presented.',
      'If retrospective restatement is impracticable, the circumstances and how and from when the '
      'error has been corrected.',
    ]},
    {'eg': {'t': 'Error or estimate?', 'q': [
      {'ol': [
        'Closing inventory in 2023 was counted twice in one warehouse, overstating it by ₦900,000. '
        'Discovered in 2024.',
        'A machine\'s useful life is reduced from 8 years to 5 following an unexpected fall in '
        'demand for its output.',
        'A customer who owed ₦1,400,000 at 31 December 2023, and who was regarded as good, went '
        'into liquidation in March 2024.',
      ]}],
      'a': [{'ol': [
        '**Prior period error.** The correct inventory quantity was ascertainable in 2023; the '
        'information existed and was misused. Restate the 2023 comparatives: reduce inventory and '
        'cost of sales appropriately, and reduce opening retained earnings for 2024.',
        '**Change in estimate.** The original 8-year life was the best estimate at the time. '
        'Apply prospectively over the remaining life; do not restate.',
        '**Change in estimate**, not an error — provided the liquidation was not foreseeable at '
        'the reporting date. Note the further question of whether it is an adjusting event after '
        'the reporting period under IAS 10: if the liquidation provides evidence of a condition '
        'that existed at 31 December 2023, the 2023 receivable is adjusted.']}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Revised depreciation after a change in estimate',
   'tex': '\\text{New charge} = \\frac{\\text{Carrying amount} - \\text{Revised residual value}}'
          '{\\text{Revised remaining useful life}}',
   'nt': 'Prior years are never restated.'},
 ],
 'focus':
   'Short and reliably examined, almost always as a short-answer or a 4–5 mark part of a Section B '
   'question. The two questions that come up again and again: is this a policy or an estimate, and '
   'is the treatment retrospective or prospective. The revised-depreciation computation in §7.3 '
   'is the calculation to have at your fingertips.',
 'errors': [
   'Restating prior years for a change in estimate.',
   'Charging the whole cumulative effect of a policy change against the current year\'s profit.',
   'Changing a policy in order to improve reported results, and citing "more relevant information" '
   'without saying why it is more relevant.',
   'Confusing a change in the depreciation *method* (an estimate under IAS 16) with a change of policy.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A change in the estimated useful life of a non-current asset is accounted for',
    'o': ['retrospectively, by restating prior periods',
          'prospectively, over the remaining useful life',
          'by an adjustment to opening retained earnings',
          'as a prior period error', 'as a change in accounting policy'],
    'a': 1,
    'w': 'A revised useful life is a change in accounting estimate. IAS 8 requires prospective '
         'application: the remaining carrying amount is spread over the revised remaining life '
         'and prior years are untouched.',
    'src': 'Chapter 7.3'},
   {'q': 'An asset costing ₦20,000,000 with no residual value has been depreciated on the '
         'straight line basis over 20 years. After 8 years the remaining useful life is revised '
         'to 6 years. The charge for year 9 is',
    'o': ['₦1,000,000', '₦2,000,000', '₦2,400,000', '₦3,333,333', '₦2,666,667'],
    'a': 1,
    'w': 'Spread the unrecovered carrying amount over the revised remaining life.',
    'calc': '\\text{CA} = 20{,}000{,}000 - \\left(\\frac{20{,}000{,}000}{20}\\times 8\\right) '
            '= 12{,}000{,}000; \\quad \\frac{12{,}000{,}000}{6} = 2{,}000{,}000',
    'src': 'Chapter 7.3'},
   {'q': 'Under IAS 8, an accounting policy may be changed only if',
    'o': ['the directors consider the result more favourable',
          'the change is required by a standard, or gives reliable and more relevant information',
          'the auditors request it',
          'the previous policy has been used for more than five years',
          'the entity changes its financial year end'],
    'a': 1,
    'w': 'Those are the only two permitted grounds. Any other reason — most obviously a wish to '
         'report a better result — breaches the standard.',
    'src': 'Chapter 7.2'},
   {'q': 'Where it is unclear whether a change is a change of policy or a change of estimate, '
         'IAS 8 requires it to be treated as',
    'o': ['a change of policy', 'a change of estimate', 'a prior period error',
          'a contingent item', 'an extraordinary item'],
    'a': 1,
    'w': 'IAS 8 states the default explicitly: where a distinction is difficult, treat the change '
         'as a change in accounting estimate, which means prospective application.',
    'src': 'Chapter 7.3'},
   {'q': 'A material error in the 2023 financial statements is discovered in 2024. It should be '
         'corrected by',
    'o': ['charging it against 2024 profit',
          'restating the 2023 comparative figures and the opening retained earnings',
          'disclosing it in the notes without adjustment',
          'spreading it over 2024 and 2025',
          'transferring it to a suspense account'],
    'a': 1,
    'w': 'A material prior period error is corrected retrospectively. It never passes through '
         'current-period profit or loss.',
    'src': 'Chapter 7.4'},
  ],
  'theory': [
   {'q': 'Distinguish between a change in accounting policy and a change in accounting estimate, '
         'stating how each is accounted for and giving two examples of each.',
    'marks': 8,
    'a': [
      {'table': {'head': ['', 'Change of policy', 'Change of estimate'], 'align': 'lll', 'rows': [
        ['Nature', 'A change in the basis of recognition, measurement or presentation',
         'A revision of a judgement about an amount subject to measurement uncertainty'],
        ['Permitted when', 'Required by a standard, or gives reliable and more relevant information',
         'Whenever new information or developments warrant it'],
        ['Applied', 'Retrospectively', 'Prospectively'],
        ['Prior periods', 'Comparatives restated; opening retained earnings adjusted', 'Not restated'],
        ['Third statement of financial position', 'Required', 'Not required'],
      ]}},
      {'h4': 'Examples'},
      {'ul': [
        '**Policy** — moving from FIFO to weighted average cost for inventory; changing the '
        'presentation of expenses from by-nature to by-function.',
        '**Estimate** — revising the useful life or residual value of an asset; revising the '
        'allowance for doubtful debts; revising a warranty provision.']},
      {'note': 'Add the IAS 8 default for a mark: where the distinction is unclear, treat the '
               'change as a change in estimate.'}],
    'src': 'Chapter 7.2'},
  ]},
}
