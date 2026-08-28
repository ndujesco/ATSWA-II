CH = {
 'n': 5,
 't': 'IPSAS 39 — Employee Benefits',
 'brief': 'The four categories of employee benefit, recognition and measurement of short-term '
          'benefits, the distinction between defined contribution and defined benefit '
          'post-employment plans, and the accounting entries for each.',
 'outcomes': [
   'State the objective and scope of IPSAS 39',
   'Classify a benefit into one of the four categories',
   'Account for short-term benefits including compensated absences and bonuses',
   'Account for a defined contribution plan',
   'Explain the components of defined benefit cost and where each is recognised',
   'State the disclosures required',
 ],
 'secs': [
  {'n': '5.1', 't': 'Objective and scope', 'b': [
    {'p': '**IPSAS 39, Employee Benefits**, replaced IPSAS 25 for periods beginning on or after '
          '1 January 2018. Its objective is to prescribe the accounting and disclosure for '
          'employee benefits, requiring an entity to recognise:'},
    {'ul': [
      'a **liability** when an employee has rendered service in exchange for benefits to be '
      'paid in the future; and',
      'an **expense** when the entity consumes the economic benefit or service potential '
      'arising from the service rendered.',
    ]},
    {'def': {'t': 'Employee benefits',
             'd': 'All forms of consideration given by an entity in exchange for service '
                  'rendered by employees or for the termination of employment. They include '
                  'benefits provided to employees or their dependants, and may be settled by '
                  'payment in cash or in goods and services, and directly to employees, to '
                  'their spouses, children or other dependants, or to others such as insurance '
                  'companies.'}},
    {'p': 'The standard applies to all employee benefits **except** share-based transactions '
          '(dealt with by the relevant standard) and benefits arising from an employer\'s '
          'reporting on retirement benefit plans, which is a separate matter.'},
  ]},

  {'n': '5.2', 't': 'The four categories', 'b': [
    {'table': {'align': 'lll', 'head': ['Category', 'Definition', 'Examples'], 'rows': [
      ['**Short-term employee benefits**',
       'Benefits (other than termination benefits) expected to be settled wholly **within '
       'twelve months** after the end of the annual reporting period in which the service was '
       'rendered',
       'Wages, salaries and social security contributions; paid annual leave and paid sick '
       'leave; profit-sharing and bonuses payable within twelve months; non-monetary benefits '
       'such as medical care, housing, cars and subsidised goods'],
      ['**Post-employment benefits**',
       'Benefits (other than termination benefits) payable **after the completion of '
       'employment**',
       'Retirement benefits such as pensions and lump-sum payments; post-employment life '
       'insurance and medical care'],
      ['**Other long-term employee benefits**',
       'Benefits **not expected to be settled wholly within twelve months** after the end of '
       'the period in which the service was rendered, and which are not post-employment or '
       'termination benefits',
       'Long-service leave or sabbatical leave; jubilee or other long-service benefits; '
       'long-term disability benefits; deferred bonuses'],
      ['**Termination benefits**',
       'Benefits payable as a result of either the entity\'s decision to terminate employment '
       'before normal retirement date, or the employee\'s decision to accept voluntary '
       'redundancy in exchange for those benefits',
       'Severance pay; redundancy payments; enhanced pension on early retirement'],
    ]}},
    {'key': 'Classification turns on **when the benefit is expected to be settled**, not on how '
            'it is described. A bonus payable fifteen months after the year in which it was '
            'earned is an *other long-term* benefit, not a short-term one, and must be '
            'discounted.'},
  ]},

  {'n': '5.3', 't': 'Short-term employee benefits', 'b': [
    {'p': 'These are the simplest: no actuarial assumptions are required, the obligation is '
          '**not discounted**, and there are no remeasurement gains or losses. The entity '
          'recognises the undiscounted amount as a liability (accrued expense) after deducting '
          'any amount already paid, and as an expense, unless another standard requires or '
          'permits it to be included in the cost of an asset such as inventory or '
          'self-constructed property.'},
    {'h4': 'Compensated absences'},
    {'ul': [
      '**Accumulating** absences are carried forward and can be used in future periods if not '
      'used in full in the current period. The expected cost is recognised **as the employees '
      'render the service that increases their entitlement**.',
      '  — *Vesting*: the employee is entitled to a cash payment for unused entitlement on '
      'leaving. The whole accumulated entitlement is provided for.',
      '  — *Non-vesting*: no payment on leaving. Provide only for the amount expected to be '
      'used, taking account of the possibility that employees may leave.',
      '**Non-accumulating** absences (such as sick leave that lapses, or maternity leave) do '
      'not carry forward. The cost is recognised **when the absence occurs**, not before.',
    ]},
    {'h4': 'Bonus and profit-sharing plans'},
    {'p': 'The expected cost is recognised when, and only when, the entity has a **present legal '
          'or constructive obligation** to make the payment as a result of past events, and a '
          '**reliable estimate** of the obligation can be made. A constructive obligation exists '
          'where past practice has created a valid expectation on the part of employees.'},
    {'eg': {'t': 'Accumulating vesting leave', 'q': [
      {'p': 'A government agency employs 120 staff, each entitled to 20 working days of paid '
            'annual leave. Unused leave may be carried forward for one year, and any balance '
            'unused on leaving is paid in cash. At 31 December 2025 the average unused '
            'entitlement is 4 days per employee, and the average daily rate of pay is ₦12,500. '
            'Determine the amount to be recognised.'}],
      'a': [
      {'p': 'The entitlement is **accumulating and vesting**, so the full accumulated balance '
            'must be provided for regardless of whether the employees are expected to use it: '
            'it will be paid out in cash if it is not taken as leave.'},
      {'tex': '\\text{Liability} = 120 \\text{ employees} \\times 4 \\text{ days} \\times '
              '₦12{,}500 = ₦6{,}000{,}000'},
      {'p': 'The entries at 31 December 2025 are:'},
      {'table': {'align': 'lrr', 'head': ['', 'Dr (₦)', 'Cr (₦)'], 'rows': [
        ['Employee benefits expense', '6,000,000', ''],
        ['Accrued leave liability', '', '6,000,000'],
      ]}},
      {'note': 'Had the leave been **non-vesting** — lapsing unpaid on departure — the agency '
               'would provide only for the days expected actually to be taken. If, say, 15% of '
               'accumulated days were historically forfeited, the liability would be '
               '$₦6{,}000{,}000 \\times 0.85 = ₦5{,}100{,}000$.'}]}},
  ]},

  {'n': '5.4', 't': 'Post-employment benefits', 'b': [
    {'p': 'The accounting depends entirely on the classification of the plan, and the '
          'classification depends on **where the risk lies**.'},
    {'table': {'align': 'lll', 'head': ['', 'Defined contribution plan', 'Defined benefit plan'],
      'rows': [
      ['Obligation of the entity',
       'Limited to the agreed contributions. Once paid, the entity has no further obligation',
       'To provide the agreed benefits, whatever the fund earns'],
      ['Actuarial and investment risk', 'Falls on the **employee**', 'Falls on the **entity**'],
      ['Measurement', 'Undiscounted contributions payable (discounted if not due within twelve '
       'months)', 'Present value of the defined benefit obligation, less the fair value of plan '
       'assets'],
      ['Actuary required?', 'No', 'Yes — the projected unit credit method'],
      ['Nigerian example', 'The Contributory Pension Scheme under the Pension Reform Act 2014',
       'The pre-2004 public service pension scheme; some gratuity schemes'],
    ]}},
    {'h4': 'Defined contribution plans'},
    {'p': 'Recognise the contribution payable in exchange for service rendered during the period '
          'as a liability, after deducting any contribution already paid, and as an expense. If '
          'the contribution already paid exceeds the amount due, recognise the excess as an '
          'asset (a prepayment) to the extent that it will lead to a refund or a reduction in '
          'future payments.'},
    {'eg': {'t': 'Defined contribution entries', 'q': [
      {'p': 'A ministry\'s pensionable emoluments for the year are ₦480,000,000. The employer '
            'contributes 10% and the employee 8%. By the year end ₦44,000,000 of the employer '
            'contribution had been remitted. Show the amounts to be recognised.'}],
      'a': [
      {'tex': '\\text{Employer contribution} = 10\\% \\times 480{,}000{,}000 = ₦48{,}000{,}000'},
      {'tex': '\\text{Employee contribution} = 8\\% \\times 480{,}000{,}000 = ₦38{,}400{,}000'},
      {'p': 'The employer contribution is an expense of the period; the employee contribution '
            'is a deduction from gross pay and is not an additional expense — it is already '
            'inside the ₦480,000,000 salary cost.'},
      {'table': {'align': 'lrr', 'head': ['', 'Dr (₦)', 'Cr (₦)'], 'rows': [
        ['Pension contribution expense', '48,000,000', ''],
        ['Cash (remitted)', '', '44,000,000'],
        ['Accrued pension contribution (liability)', '', '4,000,000'],
      ]}},
      {'p': 'The unremitted ₦4,000,000 is a liability at the reporting date, and if the '
            'seven-working-day limit has passed it also attracts the statutory penalty of not '
            'less than 2% per month, which is an additional expense.'}]}},
    {'h4': 'Defined benefit plans'},
    {'p': 'These require the **projected unit credit method**: each period of service gives rise '
          'to an additional unit of benefit entitlement, and each unit is measured separately '
          'and discounted to build up the final obligation. The net liability recognised is:'},
    {'tex': '\\text{Net defined benefit liability} = \\text{PV of the defined benefit '
            'obligation} - \\text{Fair value of plan assets}'},
    {'table': {'align': 'lll',
      'head': ['Component of defined benefit cost', 'What it is', 'Recognised in'], 'rows': [
      ['**Current service cost**',
       'The increase in the obligation from employee service in the current period',
       'Surplus or deficit'],
      ['**Past service cost**',
       'The change in the obligation from a plan amendment or curtailment relating to prior '
       'service', 'Surplus or deficit, immediately'],
      ['**Net interest** on the net defined benefit liability or asset',
       'The discount rate applied to the opening net liability', 'Surplus or deficit'],
      ['**Remeasurements**',
       'Actuarial gains and losses; the return on plan assets excluding net interest; changes '
       'in the effect of the asset ceiling',
       '**Net assets / equity** — not surplus or deficit, and never reclassified'],
    ]}},
    {'warn': 'The single most examinable point on defined benefit plans is that '
             '**remeasurements bypass surplus or deficit entirely** and are taken to net '
             'assets/equity, where they remain permanently. Service cost and net interest go '
             'through surplus or deficit. Getting these two the wrong way round loses the whole '
             'of the marks for that part.'},
  ]},

  {'n': '5.5', 't': 'Other long-term and termination benefits', 'b': [
    {'h4': 'Other long-term employee benefits'},
    {'p': 'Measured on the same basis as a defined benefit obligation, but with one important '
          'simplification: **all** of the cost, including remeasurements, is recognised in '
          '**surplus or deficit**. There is no separate treatment of actuarial gains and losses, '
          'because the uncertainty and the amounts involved are generally smaller.'},
    {'h4': 'Termination benefits'},
    {'p': 'Recognised at the **earlier** of:'},
    {'ul': [
      'when the entity can **no longer withdraw** the offer of the benefits; and',
      'when the entity recognises **costs for a restructuring** that involves the payment of '
      'termination benefits.',
    ]},
    {'p': 'Termination benefits arise from the **termination** of employment rather than from '
          'service rendered, which is why they are recognised at the point of the decision '
          'rather than spread over the service period. If they are not expected to be settled '
          'wholly within twelve months, they are discounted.'},
    {'h4': 'Principal disclosures'},
    {'ul': [
      'The accounting policy for recognising actuarial gains and losses.',
      'A general description of the type of plan.',
      'A reconciliation of the opening and closing balances of the defined benefit obligation '
      'and of the plan assets.',
      'The principal actuarial assumptions used, including the discount rate, expected salary '
      'increases and mortality.',
      'A sensitivity analysis for each significant actuarial assumption.',
      'The amount recognised as an expense for defined contribution plans.',
      'The expected contributions to the plan for the next reporting period.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': 'Net defined benefit liability',
   'tex': 'PV(\\text{obligation}) - FV(\\text{plan assets})'},
  {'lb': 'Accumulating vesting leave',
   'tex': 'N \\times \\text{days} \\times \\text{daily rate}'},
  {'lb': 'Defined contribution expense',
   'tex': '\\text{Contribution rate} \\times \\text{pensionable emolument}'},
  {'lb': 'Net interest',
   'tex': '\\text{Discount rate} \\times \\text{opening net liability}'},
 ],
 'focus':
   'Usually one or two Section A marks on the four categories or on which plan carries the '
   'investment risk. In Section B it appears as a short discussion of defined contribution '
   'against defined benefit, or a computation of a leave accrual or a contribution expense. The '
   'full projected unit credit computation is beyond Part II; what is examined is the principle '
   'and where each component of cost is recognised.',
 'errors': [
   'Classifying a benefit by its name rather than by when it is expected to be settled.',
   'Discounting short-term benefits; they are measured at their undiscounted amount.',
   'Providing for non-accumulating absences before they occur.',
   'Recognising remeasurements of a defined benefit plan in surplus or deficit instead of in '
   'net assets/equity.',
   'Treating the employee\'s own pension contribution as an additional expense of the employer; '
   'it is already within the salary cost.',
   'Recognising termination benefits over the remaining service period rather than at the point '
   'the offer can no longer be withdrawn.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Under IPSAS 39, benefits expected to be settled wholly within twelve months after the '
         'end of the reporting period in which the service was rendered are classified as',
    'o': ['post-employment benefits', 'short-term employee benefits',
          'other long-term employee benefits', 'termination benefits',
          'defined benefit obligations'],
    'a': 1,
    'w': 'The twelve-month test is the dividing line between short-term and other long-term '
         'benefits.',
    'src': 'Chapter 5.2'},
   {'q': 'In a defined contribution plan, actuarial and investment risk falls on the',
    'o': ['employer', 'employee', 'pension fund custodian', 'government', 'actuary'],
    'a': 1,
    'w': 'The employer\'s obligation ends when the contribution is paid, so any shortfall in '
         'investment returns reduces the employee\'s eventual benefit.',
    'src': 'Chapter 5.4'},
   {'q': 'Remeasurements of a net defined benefit liability are recognised in',
    'o': ['surplus or deficit', 'net assets / equity', 'the statement of cash flows',
          'the notes only', 'surplus or deficit over the remaining service life'],
    'a': 1,
    'w': 'Remeasurements — actuarial gains and losses and the return on plan assets excluding '
         'net interest — go to net assets/equity and are never reclassified to surplus or '
         'deficit.',
    'src': 'Chapter 5.4'},
   {'q': 'A ministry has 200 staff each with 5 days of accumulating vesting leave unused at the '
         'year end. The average daily rate is ₦9,000. The liability to be recognised is',
    'o': ['₦1,800,000', '₦9,000,000', '₦45,000', '₦900,000', '₦4,500,000'],
    'a': 1,
    'w': 'Vesting entitlement is paid in cash if not taken, so the whole accumulated balance is '
         'provided for.',
    'calc': '200 \\times 5 \\times 9{,}000 = ₦9{,}000{,}000',
    'src': 'Chapter 5.3'},
   {'q': 'Termination benefits are recognised at the earlier of the date the entity can no '
         'longer withdraw the offer and the date',
    'o': ['the employee accepts the offer',
          'the entity recognises costs for a related restructuring',
          'the payment is made', 'the employee leaves employment',
          'the reporting period ends'],
    'a': 1,
    'w': 'IPSAS 39 sets these two dates as the recognition trigger, because the obligation '
         'arises from the decision to terminate rather than from service rendered.',
    'src': 'Chapter 5.5'},
   {'q': 'Which of the following is an "other long-term employee benefit"?',
    'o': ['Paid annual leave taken within the year', 'Long-service leave after ten years',
          'A pension payable on retirement', 'Redundancy pay on restructuring',
          'Monthly salary'],
    'a': 1,
    'w': 'Long-service leave is not expected to be settled within twelve months, is not payable '
         'after employment ends, and does not arise from termination — so it falls into the '
         'residual "other long-term" category.',
    'src': 'Chapter 5.2'},
  ],
  'theory': [
   {'q': 'Explain the four categories of employee benefit recognised by IPSAS 39, and '
         'distinguish between the accounting treatment of a defined contribution plan and that '
         'of a defined benefit plan.',
    'marks': 15,
    'a': [
      {'h4': 'The objective of IPSAS 39'},
      {'p': 'IPSAS 39 requires an entity to recognise a **liability** when an employee has '
            'rendered service in exchange for benefits to be paid in the future, and an '
            '**expense** when the entity consumes the economic benefit or service potential '
            'arising from that service. The classification of the benefit determines how the '
            'liability is measured.'},
      {'h4': 'The four categories'},
      {'ol': [
        '**Short-term employee benefits** — benefits, other than termination benefits, expected '
        'to be settled wholly within twelve months after the end of the reporting period in '
        'which the employees rendered the related service. They include wages and salaries, '
        'social security contributions, paid annual and sick leave, profit-sharing and bonuses '
        'payable within twelve months, and non-monetary benefits such as medical care, housing '
        'and motor vehicles. They are measured at their **undiscounted** amount, require no '
        'actuarial assumptions, and give rise to no remeasurement.',
        '**Post-employment benefits** — benefits, other than termination benefits, payable '
        'after the completion of employment. They include pensions, retirement lump sums, '
        'post-employment life insurance and post-employment medical care. They are accounted '
        'for as either defined contribution or defined benefit plans, discussed below.',
        '**Other long-term employee benefits** — all employee benefits other than short-term, '
        'post-employment and termination benefits. They include long-service and sabbatical '
        'leave, jubilee awards, long-term disability benefits and deferred bonuses. They are '
        'measured in the same way as a defined benefit obligation, but with the important '
        'simplification that **all** the cost, including remeasurements, is recognised in '
        'surplus or deficit.',
        '**Termination benefits** — benefits payable as a result of either the entity\'s '
        'decision to terminate employment before the normal retirement date, or an employee\'s '
        'decision to accept voluntary redundancy in exchange for those benefits. Because they '
        'arise from termination rather than from service, they are recognised at the earlier of '
        'the date the entity can no longer withdraw the offer and the date it recognises costs '
        'for a related restructuring.',
      ]},
      {'h4': 'Defined contribution against defined benefit'},
      {'p': 'The distinction rests on **where the risk lies**. Under a defined contribution '
            'plan the entity pays fixed contributions into a separate fund and has **no legal '
            'or constructive obligation** to pay further amounts if the fund proves insufficient. '
            'Under a defined benefit plan the entity has undertaken to provide agreed benefits, '
            'and must make good any shortfall.'},
      {'table': {'align': 'lll',
        'head': ['', 'Defined contribution', 'Defined benefit'], 'rows': [
        ['Nature of the obligation', 'To pay the agreed contribution and nothing more',
         'To provide the agreed benefit, whatever it costs'],
        ['Actuarial and investment risk', 'Borne by the employee', 'Borne by the entity'],
        ['Actuarial valuation', 'Not required',
         'Required, using the projected unit credit method'],
        ['Amount recognised as a liability',
         'The contribution payable for the period, less amounts already paid',
         'Present value of the defined benefit obligation less the fair value of plan assets'],
        ['Expense in surplus or deficit', 'The contribution payable for the period',
         'Current service cost, past service cost and net interest'],
        ['Remeasurements', 'None arise',
         'Actuarial gains and losses and the return on plan assets other than net interest, '
         'recognised in net assets/equity and never reclassified'],
        ['Disclosure burden', 'Light — the expense for the period',
         'Extensive — reconciliations, actuarial assumptions and sensitivity analysis'],
      ]}},
      {'p': '**Defined contribution accounting** is straightforward. The contribution payable '
            'in exchange for service in the period is recognised as an expense and as a '
            'liability, less any amount already paid. Where the amount paid exceeds the amount '
            'due, the excess is recognised as an asset to the extent that it will give rise to '
            'a refund or a reduction in future contributions. Contributions not due within '
            'twelve months are discounted.'},
      {'p': '**Defined benefit accounting** requires four steps: an actuary estimates the '
            'benefit attributable to current and prior periods using the projected unit credit '
            'method; that benefit is discounted to a present value; the fair value of the plan '
            'assets is deducted to give the net liability; and the total defined benefit cost '
            'is determined and split between the components recognised in surplus or deficit '
            '(current service cost, past service cost, net interest) and those recognised in '
            'net assets/equity (remeasurements).'},
      {'note': 'In the Nigerian public service the Contributory Pension Scheme under the '
               'Pension Reform Act 2014 is a **defined contribution** plan, which is precisely '
               'why it removed the unfunded liability that destroyed the previous arrangement. '
               'The obligation of government now ends when the 10% is remitted.'}],
    'src': 'Chapter 5.2, 5.4'},
  ]},
}
