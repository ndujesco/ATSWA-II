CH = {
 'n': 10,
 't': 'Partnership Accounts I',
 'brief': 'Formation, the partnership agreement, the appropriation account, capital and current '
          'accounts, and guaranteed shares of profit.',
 'outcomes': [
   'State the contents of a partnership agreement and the rules that apply without one',
   'Distinguish fixed capital accounts from current accounts',
   'Prepare the appropriation account',
   'Compute interest on capital, interest on drawings, salaries and shares of profit',
   'Deal with a guaranteed minimum share of profit',
 ],
 'secs': [
  {'n': '10.1', 't': 'The partnership and its agreement', 'b': [
    {'def': {'t': 'Partnership', 'd': 'the relationship that subsists between persons carrying on '
                  'a business in common with a view to profit.'}},
    {'p': 'A partnership has **no separate legal personality** in Nigeria. The partners own the '
          'assets, and their liability is **unlimited, joint and several** — a creditor may '
          'pursue any one partner for the whole debt.'},
    {'h3': 'What the agreement should cover'},
    {'ul': [
      'Capital to be contributed by each partner.',
      'The profit and loss sharing ratio.',
      'Whether interest is allowed on capital, and at what rate.',
      'Whether interest is charged on drawings, and at what rate.',
      'Salaries payable to partners.',
      'Arrangements on admission, retirement, death and dissolution.',
      'How goodwill is to be valued and treated.',
      'Procedures for keeping accounts and for settling disputes.',
    ]},
    {'h3': 'Where there is no agreement'},
    {'p': 'The Partnership Act rules apply, and examiners test them precisely because they are '
          'counter-intuitive:'},
    {'ol': [
      'Profits and losses are shared **equally**, regardless of the capital contributed.',
      '**No interest** is allowed on capital.',
      '**No interest** is charged on drawings.',
      '**No salary** is payable to any partner.',
      'A partner who advances a loan beyond agreed capital receives interest at **5% a year**, '
      'and that interest is an **expense**, not an appropriation.',
      'Every partner may take part in the management of the business.',
      'No new partner may be admitted without the consent of all existing partners.',
    ]},
    {'key': 'Interest on a partner\'s **loan** is charged in the statement of profit or loss '
            'before arriving at net profit. Interest on **capital** is an appropriation of profit '
            'below the line. Mixing the two changes the profit figure itself, and it is a '
            'favourite trap.'},
  ]},

  {'n': '10.2', 't': 'Capital and current accounts', 'b': [
    {'table': {'head': ['', 'Fixed capital account', 'Current account'], 'align': 'lll', 'rows': [
      ['Records', 'Agreed capital contributions only', 'All routine annual movements'],
      ['Credited with', 'Capital introduced', 'Interest on capital, salary, share of profit'],
      ['Debited with', 'Capital withdrawn permanently', 'Drawings, interest on drawings, share of loss'],
      ['Balance', 'Rarely changes', 'Changes every year'],
      ['Normal balance', 'Credit', 'Credit, but may be debit if a partner overdraws'],
    ]}},
    {'p': 'Under the **fluctuating capital** method there is no current account and everything '
          'goes through the capital account. The fixed capital method is preferred because it '
          'keeps the agreed capital visible, which matters when interest on capital is computed.'},
    {'warn': 'A **debit** balance on a current account means the partner has drawn more than '
             'earned. It is shown as a receivable from that partner, not netted against the '
             'others, unless the question tells you to present a combined figure.'},
  ]},

  {'n': '10.3', 't': 'The appropriation account', 'b': [
    {'p': 'Net profit is computed exactly as for a sole trader. The appropriation account then '
          'divides it among the partners. The order is fixed.'},
    {'steps': [
      'Start with net profit for the year (after charging interest on any partner **loan**).',
      'Add interest charged on drawings — it increases the amount available to share.',
      'Deduct interest allowed on capital.',
      'Deduct partners\' salaries.',
      'Share the residue in the profit sharing ratio.',
    ]},
    {'tex': '\\begin{aligned}'
            '\\text{Residual profit} &= \\text{Net profit} + \\text{Interest on drawings} \\\\'
            '&\\quad - \\text{Interest on capital} - \\text{Salaries}'
            '\\end{aligned}', 'tag': '(10.1)'},
    {'h3': 'Interest on drawings'},
    {'p': 'Where drawings are made through the year, interest runs from the date of each drawing '
          'to the year end:'},
    {'tex': '\\text{Interest} = \\text{Amount} \\times r \\times \\frac{\\text{months to year end}}{12}'},
    {'eg': {'t': 'A full appropriation account', 'q': [
      {'p': 'Ada, Bode and Chidi are in partnership sharing profits 3 : 2 : 1. Their fixed '
            'capitals are ₦6,000,000, ₦4,000,000 and ₦2,000,000. The agreement provides for '
            'interest on capital at 8%, interest on drawings at 10% a year, and a salary of '
            '₦900,000 to Chidi. Net profit for the year ended 31 December 2024, before any '
            'appropriation, was ₦7,260,000. Bode had advanced a loan of ₦3,000,000 to the '
            'partnership on 1 January 2024 at 6%; no interest has yet been recorded.'},
      {'p': 'Drawings were: Ada ₦1,200,000 on 30 April; Bode ₦900,000 on 30 June; Chidi ₦600,000 '
            'on 30 September. Prepare the appropriation account and the current accounts.'}],
      'a': [
      {'h4': 'W1 — interest on Bode\'s loan'},
      {'p': '$6\\% \\times 3{,}000{,}000 = ₦180{,}000$. This is an **expense**, so the net profit '
            'to appropriate becomes $7{,}260{,}000 - 180{,}000 = ₦7{,}080{,}000$.'},
      {'h4': 'W2 — interest on capital at 8%'},
      {'table': {'align': 'lrr', 'head': ['Partner', 'Capital (₦)', 'Interest (₦)'], 'rows': [
        ['Ada', '6,000,000', '480,000'], ['Bode', '4,000,000', '320,000'],
        ['Chidi', '2,000,000', '160,000'], ['', '12,000,000', '960,000', '@tot'],
      ]}},
      {'h4': 'W3 — interest on drawings at 10%'},
      {'table': {'align': 'lrlr',
        'head': ['Partner', 'Drawings (₦)', 'Months to 31 Dec', 'Interest (₦)'], 'rows': [
        ['Ada', '1,200,000', '8', '80,000'],
        ['Bode', '900,000', '6', '45,000'],
        ['Chidi', '600,000', '3', '15,000'],
        ['', '2,700,000', '', '140,000', '@tot'],
      ], 'note': 'Ada: 1,200,000 × 10% × 8/12 = 80,000, and so on.'}},
      {'h4': 'Appropriation account'},
      {'stmt': {'t': 'Appropriation account',
        'sub': 'for the year ended 31 December 2024', 'rows': [
        ['Net profit after loan interest (W1)', 7080000],
        ['Add interest on drawings (W3)', 140000],
        ['', 7220000, '@t'],
        '@gap',
        ['Less interest on capital (W2)', -960000],
        ['Less salary — Chidi', -900000],
        ['Residual profit to share', 5360000, '@tt'],
      ]}},
      {'h4': 'Sharing the residue 3 : 2 : 1'},
      {'table': {'align': 'lrr', 'head': ['Partner', 'Fraction', 'Share (₦)'], 'rows': [
        ['Ada', '3/6', '2,680,000'], ['Bode', '2/6', '1,786,667'],
        ['Chidi', '1/6', '893,333'], ['', '', '5,360,000', '@tot'],
      ]}},
      {'h4': 'Current accounts'},
      {'table': {'align': 'lrrr', 'head': ['', 'Ada (₦)', 'Bode (₦)', 'Chidi (₦)'], 'rows': [
        ['Interest on capital', '480,000', '320,000', '160,000'],
        ['Salary', '—', '—', '900,000'],
        ['Share of residual profit', '2,680,000', '1,786,667', '893,333'],
        ['', '3,160,000', '2,106,667', '1,953,333', '@sub'],
        ['Less drawings', '(1,200,000)', '(900,000)', '(600,000)'],
        ['Less interest on drawings', '(80,000)', '(45,000)', '(15,000)'],
        ['Balance carried down', '1,880,000', '1,161,667', '1,338,333', '@tot'],
      ]}},
      {'note': 'Bode\'s loan interest of ₦180,000 is credited to his **loan account** (or paid to '
               'him), not to his current account, because it is a creditor\'s return rather than '
               'a partner\'s appropriation. Putting it through the appropriation account would '
               'both overstate the residue and misstate his entitlement.'}]}},
  ]},

  {'n': '10.4', 't': 'Guaranteed share of profit', 'b': [
    {'p': 'Where one partner is guaranteed a minimum, share the residue normally first, then top '
          'that partner up to the guaranteed figure and charge the shortfall to the guarantors — '
          'in their own profit sharing ratio unless the agreement says otherwise.'},
    {'eg': {'t': 'Meeting a guarantee', 'q': [
      {'p': 'D, E and F share profits 5 : 3 : 2. F is guaranteed a minimum of ₦1,500,000 a year, '
            'the shortfall to be borne by D and E in their profit sharing ratio. Residual profit '
            'for the year was ₦6,000,000. Show the final division.'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['', 'D (₦)', 'E (₦)', 'F (₦)'], 'rows': [
        ['Share 5 : 3 : 2 of 6,000,000', '3,000,000', '1,800,000', '1,200,000'],
        ['Guarantee top-up to F', '(187,500)', '(112,500)', '300,000'],
        ['Final share', '2,812,500', '1,687,500', '1,500,000', '@tot'],
      ]}},
      {'p': 'F\'s normal share is $\\tfrac{2}{10} \\times 6{,}000{,}000 = ₦1{,}200{,}000$, so the '
            'shortfall is ₦300,000. D and E share that between themselves 5 : 3:'},
      {'tex': 'D = \\frac{5}{8} \\times 300{,}000 = ₦187{,}500 \\qquad '
              'E = \\frac{3}{8} \\times 300{,}000 = ₦112{,}500'},
      {'warn': 'The shortfall is divided in D and E\'s ratio **between themselves** — 5 : 8 and '
               '3 : 8 — not in the original 5 : 10 and 3 : 10. Using the original denominators is '
               'the standard error and leaves the columns not adding back to ₦6,000,000.'}]}},
  ]},

  {'n': '10.5', 't': 'Peculiar features and drawings of stock', 'b': [
    {'ul': [
      'Where a partner **takes goods** for personal use: **Dr** that partner\'s current account, '
      '**Cr** Purchases, at cost. If the agreement says at selling price, the difference is '
      'credited to profit.',
      'Where a partner pays a business expense **personally**: **Dr** the expense, **Cr** that '
      'partner\'s current account.',
      'Where the partnership pays a **personal** expense of a partner: **Dr** current account, '
      '**Cr** Cash.',
      'Interest on capital and salaries are appropriations even where there is a **loss** — they '
      'are still allowed, and the residual loss shared is correspondingly larger.',
    ]},
    {'note': 'That last point catches candidates out. If net profit is ₦400,000 and interest on '
             'capital plus salaries come to ₦960,000, the residue is a **loss of ₦560,000** to be '
             'shared in the profit sharing ratio. You do not scale down the appropriations to fit '
             'unless the agreement expressly says so.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Residual profit for sharing',
   'tex': '\\text{Residual} = \\text{Net profit} + \\text{Interest on drawings} '
          '- \\text{Interest on capital} - \\text{Salaries}'},
  {'lb': 'Interest on drawings',
   'tex': '\\text{Interest} = \\text{Drawings} \\times r \\times \\frac{n}{12}',
   'nt': '$n$ = months from the date of drawing to the year end.'},
  {'lb': 'Closing current account',
   'tex': '\\text{Closing} = \\text{Opening} + \\text{Interest on capital} + \\text{Salary} '
          '+ \\text{Share of profit} - \\text{Drawings} - \\text{Interest on drawings}'},
 ],
 'focus':
   'Partnership appears in Section B nearly every diet, split between this chapter and Chapter 11. '
   'The appropriation account plus current accounts is the most predictable 12-mark question in '
   'the paper — the layout never changes, so practise it until you can write the skeleton before '
   'reading the numbers. Section A tests the no-agreement rules (especially 5% on a loan and '
   'equal sharing) and interest on drawings.',
 'errors': [
   'Treating interest on a partner\'s loan as an appropriation instead of an expense.',
   'Sharing profits in the capital ratio when no ratio is given — without an agreement, profits '
   'are shared equally.',
   'Charging interest on drawings for a full year regardless of the date of the drawing.',
   'Scaling down interest on capital and salaries when the profit is insufficient.',
   'Dividing a guarantee shortfall using the original denominators rather than the guarantors\' '
   'ratio between themselves.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In the absence of a partnership agreement, profits and losses are shared',
    'o': ['in the ratio of capital contributed', 'in the ratio of time devoted to the business',
          'equally', 'in the ratio of drawings', 'as the senior partner determines'],
    'a': 2,
    'w': 'The Partnership Act default is equal sharing, whatever the capitals. This is why an '
         'agreement matters so much where contributions are unequal.',
    'src': 'Chapter 10.1'},
   {'q': 'Where there is no agreement, a loan advanced by a partner beyond agreed capital carries '
         'interest at',
    'o': ['nil', '5% a year', '6% a year', '8% a year', 'the commercial bank rate'],
    'a': 1,
    'w': 'The Act allows 5% a year on an advance beyond capital, and that interest is an expense '
         'in arriving at net profit rather than an appropriation of it.',
    'src': 'Chapter 10.1'},
   {'q': 'A partner withdrew ₦1,800,000 on 31 March. Interest on drawings is 12% a year and the '
         'year ends 31 December. The interest charged is',
    'o': ['₦216,000', '₦162,000', '₦54,000', '₦108,000', '₦180,000'],
    'a': 1,
    'w': 'Interest runs from the date of the drawing to the year end — nine months.',
    'calc': '1{,}800{,}000 \\times 0.12 \\times \\frac{9}{12} = 162{,}000',
    'src': 'Chapter 10.3'},
   {'q': 'Net profit is ₦5,400,000. Interest on capital totals ₦720,000, partners\' salaries '
         '₦1,200,000 and interest on drawings ₦95,000. The residual profit to be shared is',
    'o': ['₦3,385,000', '₦3,575,000', '₦3,480,000', '₦4,575,000', '₦3,385,500'],
    'a': 1,
    'w': 'Interest on drawings is added back because it increases the pool available; interest on '
         'capital and salaries are deducted.',
    'calc': '5{,}400{,}000 + 95{,}000 - 720{,}000 - 1{,}200{,}000 = 3{,}575{,}000',
    'src': 'Chapter 10.3'},
   {'q': 'A debit balance on a partner\'s current account indicates that the partner',
    'o': ['has contributed extra capital', 'has drawn more than has been credited to the account',
          'is owed money by the partnership', 'has made a loan to the partnership',
          'is guaranteed a minimum share of profit'],
    'a': 1,
    'w': 'Current accounts are normally credit balances. A debit balance means drawings and '
         'interest on drawings have exceeded the partner\'s entitlements, so the partner owes '
         'the firm.',
    'src': 'Chapter 10.2'},
  ],
  'theory': [
   {'q': 'State SIX matters that should be dealt with in a partnership agreement, and state the '
         'rules that apply in the absence of one.',
    'marks': 10,
    'a': [
      {'h4': 'Contents of the agreement'},
      {'ol': [
        'The capital each partner is to contribute and whether it is fixed.',
        'The ratio in which profits and losses are to be shared.',
        'Whether interest is to be allowed on capital, and at what rate.',
        'Whether interest is to be charged on drawings, and at what rate.',
        'Salaries or commission payable to any partner.',
        'The treatment and valuation of goodwill on a change in the firm.',
        'Procedures on admission, retirement, death and dissolution.',
        'Limits on drawings, and the keeping and auditing of accounts.',
        'The method of resolving disputes.']},
      {'h4': 'Rules in the absence of an agreement'},
      {'ol': [
        'Profits and losses are shared **equally**.',
        'No interest is allowed on capital.',
        'No interest is charged on drawings.',
        'No partner is entitled to a salary.',
        'A partner who advances money beyond agreed capital is entitled to interest at **5% a '
        'year**, charged as an expense.',
        'Every partner may take part in the management of the business.',
        'No person may be introduced as a partner without the consent of all existing partners.',
        'The partnership books are kept at the place of business and every partner may inspect them.']}],
    'src': 'Chapter 10.1'},
  ]},
}
