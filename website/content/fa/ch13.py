CH = {
 'n': 13,
 't': 'Company Financial Statements',
 'brief': 'Share capital and reserves, bonus and rights issues, loan notes, company income tax, '
          'and the statement of changes in equity.',
 'outcomes': [
   'Distinguish the types of share capital and explain the rights attaching to each',
   'Account for the issue of shares at par and at a premium',
   'Account for a bonus issue and a rights issue',
   'Account for company income tax including under- and over-provisions',
   'Prepare a statement of changes in equity',
 ],
 'secs': [
  {'n': '13.1', 't': 'Share capital', 'b': [
    {'table': {'head': ['Term', 'Meaning'], 'align': 'll', 'rows': [
      ['Authorised (registered) capital', 'The maximum the company may issue under its memorandum'],
      ['Issued capital', 'The nominal value of shares actually allotted'],
      ['Called-up capital', 'The portion of issued capital the company has demanded'],
      ['Paid-up capital', 'The amount of called-up capital actually received'],
      ['Calls in arrear', 'Called up but not yet received — deducted from equity'],
      ['Calls in advance', 'Received before being called — a liability'],
    ]}},
    {'h3': 'Ordinary and preference shares'},
    {'table': {'head': ['', 'Ordinary shares', 'Preference shares'], 'align': 'lll', 'rows': [
      ['Dividend', 'Variable, at the directors\' discretion', 'Fixed percentage of nominal value'],
      ['Priority', 'Last', 'Ahead of ordinary shares for dividend and capital'],
      ['Voting rights', 'Normally full', 'Normally none, except in defined circumstances'],
      ['Risk and reward', 'Highest risk, unlimited upside', 'Lower risk, capped return'],
    ]}},
    {'h3': 'Types of preference share'},
    {'ul': [
      '**Cumulative** — unpaid dividends accumulate and must be paid before any ordinary dividend. '
      'Arrears are disclosed, not provided for, until declared.',
      '**Non-cumulative** — a missed dividend is lost for ever.',
      '**Participating** — receives the fixed rate plus a further share of surplus profits.',
      '**Redeemable** — repayable at a future date. Under IAS 32 a redeemable preference share '
      'with a mandatory dividend is classified as a **liability**, not equity, and its dividend '
      'is a finance cost.',
      '**Convertible** — carries a right to convert into ordinary shares.',
    ]},
    {'key': 'Substance over form: the label on the certificate does not decide the classification. '
            'A share that obliges the company to deliver cash is a financial liability.'},
  ]},

  {'n': '13.2', 't': 'Issue of shares and the share premium', 'b': [
    {'p': 'Where shares are issued above nominal value, the excess is credited to the **share '
          'premium account**, which is a non-distributable capital reserve.'},
    {'eg': {'t': 'Issue at a premium', 'q': [
      {'p': 'A company issues 2,000,000 ordinary shares of ₦50 each at a premium of ₦15 per share, '
            'fully paid on application. Show the entries and the effect on equity.'}],
      'a': [
      {'tex': '\\text{Cash received} = 2{,}000{,}000 \\times (50 + 15) = ₦130{,}000{,}000'},
      {'table': {'head': ['', 'Dr (₦)', 'Cr (₦)'], 'align': 'lrr', 'rows': [
        ['Bank', '130,000,000', ''],
        ['Ordinary share capital (2,000,000 × ₦50)', '', '100,000,000'],
        ['Share premium (2,000,000 × ₦15)', '', '30,000,000'],
      ]}},
      {'note': 'Share capital is **always** at nominal value. The premium never enters the share '
               'capital account, and it never passes through profit or loss.'}]}},
    {'h3': 'Permitted uses of the share premium account'},
    {'ol': [
      'Paying up unissued shares to be issued as fully paid **bonus shares**.',
      'Writing off the **preliminary expenses** of the company.',
      'Writing off the **expenses, commission or discount** on any issue of shares or debentures.',
      'Providing for the **premium payable on redemption** of shares or debentures.',
    ]},
    {'warn': 'The share premium may **not** be used to pay a cash dividend. It is part of the '
             'capital the creditors look to, and distributing it would reduce their protection.'},
  ]},

  {'n': '13.3', 't': 'Bonus and rights issues', 'b': [
    {'table': {'head': ['', 'Bonus (scrip / capitalisation) issue', 'Rights issue'], 'align': 'lll',
     'rows': [
      ['Cash raised', 'None', 'Yes, at a price below market'],
      ['Source', 'Capitalising reserves', 'New money from existing shareholders'],
      ['Effect on net assets', 'None', 'Increases by the cash raised'],
      ['Effect on equity total', 'None — a transfer within equity', 'Increases'],
      ['Reserves used', 'Share premium first, then revenue reserves', 'Not applicable'],
      ['Shareholder wealth', 'Unchanged in principle', 'Unchanged if the rights are taken up'],
    ]}},
    {'eg': {'t': 'Bonus issue then rights issue', 'q': [
      {'p': 'A company has 8,000,000 ordinary shares of ₦25 each fully paid, a share premium of '
            '₦45,000,000 and retained earnings of ₦120,000,000. It makes a bonus issue of one for '
            'four, using the share premium as far as possible, followed by a rights issue of one '
            'for five at ₦40 per share, fully taken up. Show the effect on equity.'}],
      'a': [
      {'h4': 'Bonus issue, one for four'},
      {'tex': '\\text{Bonus shares} = \\frac{8{,}000{,}000}{4} = 2{,}000{,}000 '
              '\\text{ shares} \\times ₦25 = ₦50{,}000{,}000'},
      {'p': 'The share premium of ₦45,000,000 is used first; the balance of ₦5,000,000 comes from '
            'retained earnings.'},
      {'h4': 'Rights issue, one for five at ₦40'},
      {'p': 'Shares in issue after the bonus are 10,000,000, so the rights issue is 2,000,000 '
            'shares.'},
      {'tex': '\\text{Cash raised} = 2{,}000{,}000 \\times 40 = ₦80{,}000{,}000'},
      {'tex': '\\text{Share capital} = 2{,}000{,}000 \\times 25 = ₦50{,}000{,}000; \\quad '
              '\\text{Premium} = 2{,}000{,}000 \\times 15 = ₦30{,}000{,}000'},
      {'h4': 'Equity'},
      {'table': {'align': 'lrrr',
        'head': ['', 'Before (₦)', 'After bonus (₦)', 'After rights (₦)'], 'rows': [
        ['Ordinary share capital', '200,000,000', '250,000,000', '300,000,000'],
        ['Share premium', '45,000,000', '—', '30,000,000'],
        ['Retained earnings', '120,000,000', '115,000,000', '115,000,000'],
        ['Total equity', '365,000,000', '365,000,000', '445,000,000', '@tot'],
      ]}},
      {'note': 'Total equity is unchanged by the bonus issue — ₦365,000,000 before and after — '
               'because nothing left or entered the company. It rises by exactly the ₦80,000,000 '
               'of cash raised in the rights issue. That check is worth doing every time.'}]}},
    {'h3': 'Reasons for a bonus issue'},
    {'ul': [
      'To bring the share capital into line with the assets actually employed.',
      'To reduce the market price per share, improving marketability.',
      'To capitalise reserves that the directors do not intend to distribute.',
      'As a signal of confidence, since the company can afford a larger capital base.',
    ]},
  ]},

  {'n': '13.4', 't': 'Loan notes and debentures', 'b': [
    {'p': 'A loan note or debenture is **borrowing**, not ownership. Interest on it is a '
          '**finance cost** charged in arriving at profit, whether or not the company is '
          'profitable; a dividend is an appropriation and is paid only if declared.'},
    {'table': {'head': ['', 'Share', 'Debenture / loan note'], 'align': 'lll', 'rows': [
      ['Holder is', 'An owner', 'A creditor'],
      ['Return', 'Dividend, discretionary', 'Interest, contractual'],
      ['Return charged as', 'An appropriation of profit', 'An expense before profit'],
      ['On liquidation', 'Paid last', 'Paid before members'],
      ['Security', 'None', 'Often secured by fixed or floating charge'],
      ['Tax treatment of return', 'Not deductible', 'Deductible for company income tax'],
    ]}},
    {'p': 'Accrued interest at the year end is a current liability. Where interest is 10% on '
          '₦40,000,000 of loan notes and only ₦2,000,000 has been paid, the charge is ₦4,000,000 '
          'and ₦2,000,000 is accrued.'},
  ]},

  {'n': '13.5', 't': 'Company income tax', 'b': [
    {'p': 'Tax is an estimate at the reporting date, so the estimate for one year is settled in '
          'the next and any difference is adjusted then. Three figures matter and questions '
          'usually give you two of them.'},
    {'tex': '\\begin{aligned}'
            '\\text{Charge in P/L} &= \\text{Current year estimate} \\\\'
            '&\\quad + \\text{Under-provision brought forward} \\\\'
            '&\\quad - \\text{Over-provision brought forward}'
            '\\end{aligned}', 'tag': '(13.1)'},
    {'eg': {'t': 'Under-provision', 'q': [
      {'p': 'The tax liability at 1 January 2024 was ₦3,200,000. During 2024 the company paid '
            '₦3,500,000 in settlement of that liability. The estimated charge for 2024 is '
            '₦4,100,000. Show the tax charge and the closing liability.'}],
      'a': [
      {'p': 'The company paid ₦300,000 more than it had provided, so 2023 was **under-provided** '
            'by ₦300,000.'},
      {'stmt': {'t': 'Income tax expense for 2024', 'rows': [
        ['Estimated charge for the current year', 4100000],
        ['Add under-provision in respect of 2023', 300000],
        ['Charge to profit or loss', 4400000, '@tt'],
      ]}},
      {'tacc': {'t': 'Company income tax account', 'dr': [
          ['Cash paid', 3500000], ['Balance c/d', 4100000], ['', 7600000, '@tot']],
        'cr': [['Balance b/d', 3200000], ['Profit or loss (charge)', 4400000],
               ['', 7600000, '@tot']]}},
      {'p': 'The current liability at 31 December 2024 is **₦4,100,000**.'},
      {'note': 'The under-provision is not a prior period error and is never restated — it is a '
               'change in an accounting estimate, dealt with prospectively under IAS 8.'}]}},
  ]},

  {'n': '13.6', 't': 'Reserves and the statement of changes in equity', 'b': [
    {'table': {'head': ['Capital reserves (not distributable)', 'Revenue reserves (distributable)'],
     'align': 'll', 'rows': [
      ['Share premium', 'Retained earnings'],
      ['Revaluation surplus', 'General reserve'],
      ['Capital redemption reserve', 'Any reserve created by appropriating profit'],
    ]}},
    {'stmt': {'t': 'Statement of changes in equity',
      'sub': 'for the year ended 31 December 2024 (₦\'000)', 'rows': [
      ['', 'Share capital', 'Share premium', 'Revaluation surplus', 'Retained earnings', 'Total'],
      ['Balance at 1 January', 200000, 45000, 18000, 120000, 383000],
      ['Profit for the year', '—', '—', '—', 62000, 62000],
      ['Other comprehensive income', '—', '—', 19000, '—', 19000],
      ['Issue of shares', 50000, 30000, '—', '—', 80000],
      ['Bonus issue', 50000, -45000, '—', -5000, 0],
      ['Dividends paid', '—', '—', '—', -28000, -28000],
      ['Transfer of excess depreciation', '—', '—', -543, 543, 0],
      ['Balance at 31 December', 300000, 30000, 36457, 149543, 516000, '@tt'],
    ]}},
    {'key': 'The statement of changes in equity is where the examiner checks that you know which '
            'movements go where. Profit lands in retained earnings; a revaluation surplus lands '
            'in other comprehensive income; a bonus issue moves money within equity and nets to '
            'zero; a dividend leaves equity altogether.'},
    {'h3': 'Dividends'},
    {'ul': [
      'A **final** dividend proposed after the reporting date is **not** a liability at that date '
      '(IAS 10). It is disclosed in the notes and recognised when approved.',
      'An **interim** dividend already paid is recognised in the period paid.',
      'Preference dividends on shares classified as equity are appropriations; on shares '
      'classified as liabilities they are finance costs.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': 'Share premium on issue',
   'tex': '\\text{Premium} = \\text{Number of shares} \\times (\\text{Issue price} '
          '- \\text{Nominal value})'},
  {'lb': 'Income tax expense',
   'tex': '\\text{Charge} = \\text{Current estimate} + \\text{Under-provision} '
          '- \\text{Over-provision}'},
  {'lb': 'Bonus issue',
   'tex': '\\text{Bonus} = \\frac{\\text{Existing shares}}{n} \\times \\text{Nominal value}',
   'nt': 'Charged to share premium first, then to revenue reserves.'},
 ],
 'focus':
   'Reliably examined in Section A on share premium, bonus versus rights, and the tax '
   'under-provision computation. In Section B it usually appears folded into the Chapter 14 '
   'final-accounts question, often with a statement of changes in equity attached. Know which '
   'reserves are distributable and which are not — that single distinction generates several '
   'questions a diet.',
 'errors': [
   'Crediting the whole issue proceeds to share capital instead of splitting out the premium.',
   'Treating a bonus issue as increasing total equity.',
   'Recognising a final dividend proposed after the reporting date as a liability.',
   'Charging a debenture interest payment as an appropriation rather than a finance cost.',
   'Deducting an under-provision from the tax charge instead of adding it.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A company issues 1,500,000 ordinary shares of ₦20 each at ₦32 per share. The amount '
         'credited to share premium is',
    'o': ['₦48,000,000', '₦30,000,000', '₦18,000,000', '₦12,000,000', '₦78,000,000'],
    'a': 2,
    'w': 'The premium is the excess of issue price over nominal value, per share, times the '
         'number of shares.',
    'calc': '1{,}500{,}000 \\times (32 - 20) = 1{,}500{,}000 \\times 12 = 18{,}000{,}000',
    'src': 'Chapter 13.2', 'sec': '13.2'},
   {'q': 'Which of the following is NOT a permitted use of the share premium account?',
    'o': ['Issuing fully paid bonus shares', 'Writing off preliminary expenses',
          'Writing off the expenses of an issue of debentures',
          'Paying a cash dividend to ordinary shareholders',
          'Providing for the premium on redemption of debentures'],
    'a': 3,
    'w': 'Share premium is a non-distributable capital reserve. Using it to pay a cash dividend '
         'would return capital to members and reduce the fund creditors rely on.',
    'src': 'Chapter 13.2', 'sec': '13.2'},
   {'q': 'A bonus issue of shares',
    'o': ['increases total equity and increases net assets',
          'leaves total equity unchanged and leaves net assets unchanged',
          'increases total equity but leaves net assets unchanged',
          'decreases total equity and decreases net assets',
          'increases net assets but leaves total equity unchanged'],
    'a': 1,
    'w': 'A bonus issue capitalises reserves: it moves an amount from one part of equity to '
         'another. No cash enters or leaves, so neither total equity nor net assets change.',
    'src': 'Chapter 13.3', 'sec': '13.3'},
   {'q': 'The tax liability brought forward was ₦2,800,000 and ₦2,600,000 was paid in settlement. '
         'The current year estimate is ₦3,400,000. The charge to profit or loss is',
    'o': ['₦3,400,000', '₦3,600,000', '₦3,200,000', '₦3,000,000', '₦2,600,000'],
    'a': 2,
    'w': 'The company paid ₦200,000 less than provided, so the prior year was **over**-provided '
         'and the excess is credited back against this year\'s charge.',
    'calc': '3{,}400{,}000 - (2{,}800{,}000 - 2{,}600{,}000) = 3{,}400{,}000 - 200{,}000 '
            '= 3{,}200{,}000',
    'src': 'Chapter 13.5', 'sec': '13.5'},
   {'q': 'Which of the following does NOT appear in the statement of changes in equity?',
    'o': ['Profit for the year', 'Dividends paid', 'Revaluation surplus arising in the year',
          'Depreciation charge for the year', 'Proceeds of a share issue'],
    'a': 3,
    'w': 'Depreciation is an expense within profit or loss. Only the resulting profit figure '
         'reaches the statement of changes in equity.',
    'src': 'Chapter 13.6', 'sec': '13.6'},
   {'q': 'Interest on loan notes is',
    'o': ['an appropriation of profit', 'a finance cost charged before profit for the year',
          'deducted from the loan note balance', 'credited to share premium',
          'shown in other comprehensive income'],
    'a': 1,
    'w': 'Loan note holders are creditors, not owners. Their return is contractual and is charged '
         'as a finance cost whether or not the company is profitable.',
    'src': 'Chapter 13.4', 'sec': '13.4'},
  ],
  'theory': [
   {'q': 'Distinguish between a bonus issue and a rights issue of shares, and state TWO reasons a '
         'company might make each.',
    'marks': 8,
    'a': [
      {'table': {'head': ['', 'Bonus issue', 'Rights issue'], 'align': 'lll', 'rows': [
        ['Nature', 'Free shares issued by capitalising reserves',
         'New shares offered to existing members at a price below market'],
        ['Cash raised', 'None', 'Yes'],
        ['Effect on net assets', 'None', 'Increased by the cash received'],
        ['Effect on total equity', 'None — a transfer between reserves and share capital', 'Increased'],
        ['Effect on the individual shareholding', 'Proportion unchanged; more shares held',
         'Proportion unchanged if the rights are taken up'],
        ['Reserves used', 'Share premium first, then revenue reserves', 'None'],
      ]}},
      {'h4': 'Reasons for a bonus issue'},
      {'ol': ['To bring the issued share capital into line with the assets actually employed in '
              'the business.',
              'To reduce the market price per share and so improve marketability.',
              'To capitalise reserves the directors do not intend ever to distribute, signalling '
              'permanence.']},
      {'h4': 'Reasons for a rights issue'},
      {'ol': ['To raise new capital more cheaply than a public offer, since issue costs are lower.',
              'To preserve existing shareholders\' proportionate control, since they have first refusal.',
              'To fund expansion or reduce gearing without incurring the fixed interest burden of debt.']}],
    'src': 'Chapter 13.3', 'sec': '13.3'},
  ]},
}
