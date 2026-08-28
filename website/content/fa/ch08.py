CH = {
 'n': 8,
 't': 'Accounting for Not-for-Profit Organisations',
 'brief': 'Clubs and societies: the receipts and payments account, the income and expenditure '
          'account, subscriptions, bar trading and the accumulated fund.',
 'outcomes': [
   'Distinguish a receipts and payments account from an income and expenditure account',
   'Compute the subscription income for a period',
   'Prepare a bar or refreshment trading account',
   'Account for life membership and for donations and legacies',
   'Compute the accumulated fund and prepare the statement of financial position',
 ],
 'secs': [
  {'n': '8.1', 't': 'How a club differs from a business', 'b': [
    {'p': 'A club exists to serve its members, not to earn profit. Three consequences follow, and '
          'together they are worth several short-answer marks.'},
    {'table': {'head': ['Trading entity', 'Not-for-profit entity'], 'align': 'll', 'rows': [
      ['Capital', 'Accumulated fund'],
      ['Statement of profit or loss', 'Income and expenditure account'],
      ['Profit or loss', 'Surplus or deficit'],
      ['Drawings', 'No equivalent — no owner to withdraw'],
      ['Sales', 'Subscriptions, donations, levies, bar takings'],
    ]}},
  ]},

  {'n': '8.2', 't': 'Receipts and payments versus income and expenditure', 'b': [
    {'table': {'head': ['', 'Receipts and payments', 'Income and expenditure'], 'align': 'lll',
     'rows': [
      ['Nature', 'A summarised cash book', 'A statement of profit or loss equivalent'],
      ['Basis', 'Cash', 'Accruals'],
      ['Capital items', 'Included (e.g. purchase of a minibus)', 'Excluded'],
      ['Accruals and prepayments', 'Ignored', 'Adjusted for'],
      ['Depreciation', 'Not shown', 'Charged'],
      ['Opens and closes with', 'Cash balances', 'Nothing — it is a period statement'],
      ['Result', 'Closing cash balance', 'Surplus or deficit for the year'],
    ]}},
    {'key': 'The commonest short-answer question in this chapter is precisely this comparison. '
            'The two lines that earn marks fastest: a receipts and payments account **includes '
            'capital items and ignores accruals**; an income and expenditure account does the '
            'opposite.'},
  ]},

  {'n': '8.3', 't': 'Subscriptions', 'b': [
    {'p': 'This is the calculation the chapter exists for. Subscriptions can be in arrears (a '
          'member owes) or in advance (a member has paid early), at both the start and the end of '
          'the year — four balances in all.'},
    {'tex': '\\begin{aligned}'
            '\\text{Income} &= \\text{Cash received} \\\\'
            '&\\quad + \\text{Closing arrears} - \\text{Opening arrears} \\\\'
            '&\\quad + \\text{Opening advance} - \\text{Closing advance}'
            '\\end{aligned}', 'tag': '(8.1)'},
    {'p': 'As always, the safer route is the T-account, because the signs then look after '
          'themselves. Arrears are an **asset** (owed to the club); advances are a **liability** '
          '(the club owes a service).'},
    {'eg': {'t': 'Subscription income', 'q': [
      {'p': 'The Ikoyi Sports Club had the following subscription balances:'},
      {'table': {'head': ['', '1 Jan 2024 (₦)', '31 Dec 2024 (₦)'], 'align': 'lrr', 'rows': [
        ['Subscriptions in arrears', '145,000', '210,000'],
        ['Subscriptions in advance', '78,000', '96,000'],
      ]}},
      {'p': 'Cash received during 2024 was ₦3,840,000, of which ₦25,000 related to arrears '
            'written off as irrecoverable during the year. Compute the subscription income.'}],
      'a': [
      {'tacc': {'t': 'Subscriptions account', 'dr': [
          ['Balance b/d (arrears)', 145000], ['Income and expenditure', 3893000],
          ['Balance c/d (advance)', 96000], ['', 4134000, '@tot']],
        'cr': [['Balance b/d (advance)', 78000], ['Cash received', 3840000],
               ['Arrears written off', 25000], ['Balance c/d (arrears)', 210000],
               ['', 4153000, '@tot']]}},
      {'p': 'Working it as a schedule, which is what most candidates find safer:'},
      {'stmt': {'t': 'Subscription income for 2024', 'rows': [
        ['Cash received', 3840000],
        ['Add closing arrears (earned, not yet received)', 210000],
        ['Less opening arrears (received this year, earned last year)', -145000],
        ['Add opening advance (received last year, earned this year)', 78000],
        ['Less closing advance (received now, earned next year)', -96000],
        ['Subscription income', 3887000, '@tt'],
      ]}},
      {'note': 'The ₦25,000 written off is a separate expense in the income and expenditure '
               'account, not a deduction from income — treat it exactly as an irrecoverable debt. '
               'Some examiners instead net it against the arrears figure; either is defensible '
               'provided you state which you have done.'},
      {'warn': 'The traps here are the two "opening" lines. Opening arrears were **last year\'s** '
               'income even though this year\'s cash; opening advances were **last year\'s** cash '
               'but this year\'s income. Getting either sign wrong reverses a five-figure number.'}]}},
  ]},

  {'n': '8.4', 't': 'Bar and refreshment trading', 'b': [
    {'p': 'Where a club runs a bar, its profit is computed separately in a **bar trading '
          'account** and only the resulting profit or loss is carried into the income and '
          'expenditure account.'},
    {'stmt': {'t': 'Bar trading account', 'sub': 'for the year ended 31 December 2024', 'rows': [
      ['Bar takings', 2650000],
      '@gap',
      'Cost of bar sales',
      ['Opening bar inventory', 185000],
      ['Bar purchases', 1420000],
      ['Less closing bar inventory', -220000],
      ['', -1385000, '@t'],
      ['Gross bar profit', 1265000, '@t'],
      ['Less barman\'s wages', -480000],
      ['Less bar expenses', -95000],
      ['Net bar profit to income and expenditure', 690000, '@tt'],
    ]}},
    {'p': 'Bar purchases are derived from the payables control account in exactly the way credit '
          'purchases were derived in Chapter 6 where the question gives payments and payable '
          'balances rather than the purchases figure itself.'},
  ]},

  {'n': '8.5', 't': 'Life membership, donations and legacies', 'b': [
    {'p': 'These three items all raise the same question: is the receipt income of this year, or '
          'a capital receipt belonging to the fund?'},
    {'ul': [
      '**Life membership** — a single payment for membership in perpetuity. It is credited to a '
      'Life Membership Fund and released to income over an estimated period (often the average '
      'expected remaining membership). Crediting it all to one year overstates that year\'s surplus.',
      '**Donations** — small or recurring donations are income of the year. A large or specific '
      'donation, especially one for a stated purpose such as a new pavilion, is capitalised in '
      'the accumulated fund or in a separate designated fund.',
      '**Legacies** — usually treated as capital and credited to the accumulated fund, because '
      'they are non-recurring windfalls.',
      '**Entrance fees** — treated as income unless the club\'s rules say otherwise; if they are '
      'substantial and non-recurring, capitalise them.',
    ]},
    {'note': 'Where a question does not tell you, state your assumption in a note. Examiners give '
             'the mark for a defended treatment, not for reading their mind.'},
  ]},

  {'n': '8.6', 't': 'The accumulated fund and the statement of financial position', 'b': [
    {'p': 'The accumulated fund is the club\'s equivalent of capital, and it is found exactly as '
          'opening capital is found in incomplete records — by a statement of affairs.'},
    {'tex': '\\text{Accumulated fund} = \\text{Total assets} - \\text{Total liabilities}'},
    {'tex': '\\text{Closing fund} = \\text{Opening fund} + \\text{Surplus} + '
            '\\text{Capitalised donations and legacies}'},
    {'eg': {'t': 'Opening accumulated fund', 'q': [
      {'p': 'At 1 January 2024 the Ikoyi Sports Club held: clubhouse ₦18,000,000; equipment (net) '
            '₦2,400,000; bar inventory ₦185,000; subscriptions in arrears ₦145,000; cash at bank '
            '₦960,000. It owed: bar creditors ₦230,000; accrued electricity ₦64,000; '
            'subscriptions in advance ₦78,000. Compute the accumulated fund.'}],
      'a': [
      {'stmt': {'t': 'Statement of affairs at 1 January 2024', 'rows': [
        'Assets',
        ['Clubhouse', 18000000], ['Equipment', 2400000], ['Bar inventory', 185000],
        ['Subscriptions in arrears', 145000], ['Cash at bank', 960000],
        ['', 21690000, '@t'],
        '@gap',
        'Liabilities',
        ['Bar creditors', 230000], ['Accrued electricity', 64000],
        ['Subscriptions in advance', 78000],
        ['', 372000, '@t'],
        '@gap',
        ['Accumulated fund at 1 January 2024', 21318000, '@tt'],
      ]}},
      {'warn': 'Subscriptions in arrears are an **asset** and subscriptions in advance are a '
               '**liability**. Candidates reverse these more often than any other pair in the '
               'paper, and it moves the fund by twice the smaller figure.'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Subscription income',
   'tex': '\\text{Income} = \\text{Cash} + \\text{Closing arrears} - \\text{Opening arrears} '
          '+ \\text{Opening advance} - \\text{Closing advance}'},
  {'lb': 'Accumulated fund',
   'tex': '\\text{Fund} = \\text{Assets} - \\text{Liabilities}'},
  {'lb': 'Bar profit',
   'tex': '\\text{Bar profit} = \\text{Takings} - \\bigl(\\text{Opening inv} + \\text{Purchases} '
          '- \\text{Closing inv}\\bigr) - \\text{Bar expenses}'},
 ],
 'focus':
   'A frequent Section B question worth 12–15 marks, and one where the layout carries a lot of the '
   'marks: a bar trading account, an income and expenditure account and a statement of financial '
   'position, with the accumulated fund as a working. The subscription computation is the '
   'discriminator — do it in a T-account rather than in your head. Section A tests the receipts '
   'and payments versus income and expenditure comparison.',
 'errors': [
   'Treating subscriptions in advance as an asset.',
   'Putting the purchase of equipment in the income and expenditure account.',
   'Carrying the gross bar takings into the income and expenditure account instead of the net bar profit.',
   'Crediting a whole life membership receipt to one year\'s income.',
   'Forgetting to charge depreciation, because a receipts and payments account never shows it.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Subscriptions received in cash were ₦2,400,000. Arrears were ₦120,000 at the start and '
         '₦185,000 at the end; advances were ₦90,000 at the start and ₦65,000 at the end. '
         'Subscription income for the year is',
    'o': ['₦2,490,000', '₦2,310,000', '₦2,530,000', '₦2,270,000', '₦2,400,000'],
    'a': 0,
    'w': 'Add closing arrears and opening advances (both earned this year); deduct opening '
         'arrears and closing advances (both belong to another year).',
    'calc': '2{,}400{,}000 + 185{,}000 - 120{,}000 + 90{,}000 - 65{,}000 = 2{,}490{,}000',
    'src': 'Chapter 8.3'},
   {'q': 'The accumulated fund of a not-for-profit organisation represents',
    'o': ['the cash at bank', 'the surplus for the year',
          'the excess of assets over liabilities', 'the total subscriptions received to date',
          'the value of the clubhouse'],
    'a': 2,
    'w': 'The accumulated fund is the club\'s capital: assets less liabilities. It is exactly the '
         'residual the accounting equation defines for any entity.',
    'src': 'Chapter 8.6'},
   {'q': 'Which of the following would appear in a receipts and payments account but NOT in an '
         'income and expenditure account?',
    'o': ['Depreciation of equipment', 'Purchase of a new minibus',
          'Accrued electricity', 'Subscription income for the year',
          'Loss on disposal of equipment'],
    'a': 1,
    'w': 'A receipts and payments account is a summarised cash book, so it records the whole '
         'capital payment. An income and expenditure account excludes capital items and shows '
         'only the depreciation.',
    'src': 'Chapter 8.2'},
   {'q': 'Bar takings were ₦1,800,000; opening bar inventory ₦140,000; bar purchases ₦990,000; '
         'closing bar inventory ₦175,000; barman\'s wages ₦260,000. The net bar profit is',
    'o': ['₦845,000', '₦585,000', '₦810,000', '₦510,000', '₦675,000'],
    'a': 1,
    'w': 'Cost of bar sales is 140,000 + 990,000 − 175,000 = ₦955,000, giving gross bar profit of '
         '₦845,000, then deduct the wages.',
    'calc': '1{,}800{,}000 - (140{,}000 + 990{,}000 - 175{,}000) - 260{,}000 = 585{,}000',
    'src': 'Chapter 8.4'},
   {'q': 'Subscriptions received in advance at the year end are shown in the statement of '
         'financial position as',
    'o': ['a current asset', 'a current liability', 'part of the accumulated fund',
          'a deduction from subscription income only', 'a non-current liability'],
    'a': 1,
    'w': 'The club has received cash for a period of membership it has not yet provided, so it '
         'owes a service. That is a current liability.',
    'src': 'Chapter 8.6'},
  ],
  'theory': [
   {'q': 'Distinguish between a receipts and payments account and an income and expenditure '
         'account under any SIX headings.',
    'marks': 6,
    'a': [{'table': {'head': ['Heading', 'Receipts and payments', 'Income and expenditure'],
      'align': 'lll', 'rows': [
      ['Nature', 'A summary of the cash book', 'Equivalent of a statement of profit or loss'],
      ['Basis', 'Cash basis', 'Accruals basis'],
      ['Period of items', 'All cash of the period, whatever period it relates to',
       'Only income and expenses of the period'],
      ['Capital items', 'Included in full', 'Excluded; only depreciation is charged'],
      ['Non-cash items', 'Never appear', 'Depreciation, bad debts and provisions all appear'],
      ['Opening and closing entries', 'Begins and ends with cash balances',
       'No opening or closing balance'],
      ['Result', 'Closing balance of cash and bank', 'Surplus or deficit for the year'],
      ['Debit side records', 'Receipts', 'Expenditure'],
    ]}}],
    'src': 'Chapter 8.2'},
  ]},
}
