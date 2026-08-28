CH = {
 'n': 4,
 't': 'Pension and Gratuity',
 'brief': 'The Contributory Pension Scheme under the Pension Reform Act 2014: the rates of '
          'contribution, the roles of PenCom, the Pension Fund Administrators and Custodians, '
          'the Retirement Savings Account, and the modes of withdrawal at retirement.',
 'outcomes': [
   'Distinguish a defined benefit from a defined contribution scheme',
   'State the rates and basis of contribution under the Pension Reform Act 2014',
   'Compute an employer and employee contribution from an officer\'s emoluments',
   'Describe the roles of PenCom, PFAs and PFCs',
   'State the modes of withdrawal from a Retirement Savings Account',
   'Identify the categories of employee exempt from the scheme',
 ],
 'secs': [
  {'n': '4.1', 't': 'The two types of scheme', 'b': [
    {'table': {'align': 'lll',
      'head': ['', 'Defined benefit', 'Defined contribution'], 'rows': [
      ['Promise made', 'A specified pension, usually a fraction of final salary per year of '
       'service', 'Whatever the accumulated contributions and investment returns will buy'],
      ['Contributions', 'Whatever is needed to fund the promise; usually the employer alone',
       'A fixed percentage of emoluments from both employer and employee'],
      ['Investment risk', 'Borne by the **employer**', 'Borne by the **employee**'],
      ['Longevity risk', 'Borne by the employer', 'Borne by the employee'],
      ['Funding', 'Often unfunded, paid from current revenue (pay-as-you-go)',
       'Fully funded, in an individual account'],
      ['Portability', 'Poor; the benefit is tied to service with one employer',
       'Full; the account follows the employee'],
      ['Accounting', 'Requires actuarial valuation; complex',
       'Simple — the expense is the contribution payable'],
    ]}},
    {'p': 'Nigeria operated a **defined benefit** scheme before 2004. It failed because it was '
          'unfunded: pensions were paid out of current budget provision, arrears accumulated '
          'into the hundreds of billions of naira, the pensioner records were unreliable and '
          'heavily populated with ghost pensioners, and there was no fund from which any claim '
          'could be met. The Pension Reform Act 2004, re-enacted with amendments as the **Pension '
          'Reform Act 2014**, replaced it with a mandatory, fully funded **defined contribution** '
          'scheme.'},
  ]},

  {'n': '4.2', 't': 'The Contributory Pension Scheme', 'b': [
    {'h4': 'Scope'},
    {'ul': [
      'Applies to all employees in the **public service of the Federation**, the Federal '
      'Capital Territory, the States and Local Governments, and to the **private sector** where '
      'the organisation has **15 or more employees**.',
      'Organisations with fewer than three employees, and self-employed persons, may '
      'participate under guidelines issued by the Commission (the Micro Pension Plan).',
    ]},
    {'fbox': {'h': 'Rates of contribution (section 4, PRA 2014)', 'rows': [
      {'lb': 'Employer, minimum', 'tex': '10\\% \\text{ of monthly emolument}'},
      {'lb': 'Employee, minimum', 'tex': '8\\% \\text{ of monthly emolument}'},
      {'lb': 'Combined minimum', 'tex': '18\\% \\text{ of monthly emolument}'},
      {'lb': 'Employer alone, if it so elects',
       'tex': '\\ge 20\\% \\text{ (employee then contributes nothing)}'},
    ]}},
    {'def': {'t': 'Monthly emolument',
             'd': 'The total of **basic salary, housing allowance and transport allowance** '
                  '— not gross pay. Other allowances are excluded unless the employer elects to '
                  'include them.'}},
    {'ul': [
      'The employer must **deduct the employee\'s contribution at source** and remit both '
      'contributions to the Pension Fund Custodian within **seven working days** of paying the '
      'salary.',
      'Late remittance attracts a penalty of not less than **2% of the unremitted amount per '
      'month**, payable to the employee\'s Retirement Savings Account.',
      'The employer must in addition maintain a **group life insurance policy** for each '
      'employee of not less than **three times the annual total emolument**.',
      'Employees may make **voluntary contributions** in addition to the statutory minimum.',
    ]},
    {'eg': {'t': 'Computing the contributions', 'q': [
      {'p': 'An officer\'s annual emoluments are: basic salary ₦2,400,000; housing allowance '
            '₦600,000; transport allowance ₦300,000; utility allowance ₦180,000; meal '
            'subsidy ₦120,000. Compute the monthly employer and employee pension contributions '
            'and the total annual contribution to the officer\'s Retirement Savings Account.'}],
      'a': [
      {'p': 'Only basic salary, housing and transport enter monthly emolument. The utility '
            'allowance and meal subsidy are excluded.'},
      {'stmt': {'t': 'Annual pensionable emolument', 'rows': [
        ['Basic salary', 2400000],
        ['Housing allowance', 600000],
        ['Transport allowance', 300000],
        ['Total annual emolument@tot', 3300000],
      ]}},
      {'tex': '\\text{Monthly emolument} = \\frac{3{,}300{,}000}{12} = ₦275{,}000'},
      {'table': {'align': 'lrr', 'head': ['', 'Monthly (₦)', 'Annual (₦)'], 'rows': [
        ['Employer contribution at 10%', '27,500', '330,000'],
        ['Employee contribution at 8%', '22,000', '264,000'],
        ['**Total credited to the RSA**', '**49,500**', '**594,000**'],
      ]}},
      {'p': 'The employer\'s ₦330,000 is a charge in the statement of financial performance for '
            'the year; the employee\'s ₦264,000 is deducted from salary and is not an '
            'additional cost to the employer. The employer must also carry group life cover of '
            'at least $3 \\times ₦3{,}600{,}000 = ₦10{,}800{,}000$, taking the total annual '
            'emolument including the utility and meal allowances.'},
      {'warn': 'Applying the percentages to **gross pay** rather than to basic, housing and '
               'transport is the standard error, and it inflates the answer. Here gross pay is '
               '₦3,600,000 and would give an employer contribution of ₦360,000 instead of '
               '₦330,000.'}]}},
  ]},

  {'n': '4.3', 't': 'The institutional structure', 'b': [
    {'table': {'align': 'll', 'head': ['Body', 'Role'], 'rows': [
      ['**National Pension Commission (PenCom)**',
       'Regulates, supervises and ensures effective administration of all pension matters. '
       'Licenses and monitors PFAs and PFCs, issues guidelines, approves investment categories, '
       'maintains a national databank of pension contributors, and receives and investigates '
       'complaints'],
      ['**Pension Fund Administrator (PFA)**',
       'Opens and maintains the Retirement Savings Account, **invests and manages** the pension '
       'fund, maintains books of account, provides statements to contributors at least '
       'annually, and pays retirement benefits. Licensed by PenCom with minimum share capital '
       'prescribed by the Commission'],
      ['**Pension Fund Custodian (PFC)**',
       'Receives contributions from employers on behalf of the PFA and **holds the pension '
       'assets** in trust. Settles transactions on the instruction of the PFA. The custodian '
       'never manages the fund and the administrator never holds the assets'],
      ['**Employer**',
       'Deducts and remits contributions within seven working days, maintains group life '
       'insurance, and provides records to the PFA'],
      ['**Employee**',
       'Opens an RSA with a PFA of his own choice, notifies the employer of the PFA and account '
       'number, and may transfer between PFAs once a year'],
    ]}},
    {'key': 'The **separation of the administrator from the custodian** is the central control '
            'of the scheme. The PFA decides how the money is invested but never touches it; the '
            'PFC holds the money but has no discretion over it. Neither can misapply the fund '
            'without the other, and PenCom supervises both. Explaining this separation is worth '
            'several marks in any question on the structure of the scheme.'},
  ]},

  {'n': '4.4', 't': 'Retirement and withdrawal', 'b': [
    {'h4': 'When benefits become payable'},
    {'ul': [
      'On attaining the age of **50 years**, or on retirement in accordance with the terms of '
      'employment, whichever is later. The general retirement age in the public service is '
      '**60 years or 35 years of service**, whichever comes first.',
      'Judicial officers and certain other categories have longer statutory ages (65 or 70), '
      'and academic staff of universities may serve to 70.',
      'On **medical grounds**, certified by a suitably qualified physician or a properly '
      'constituted medical board.',
      'Where an employee **disengages before 50** and remains unemployed for four months, he '
      'may withdraw not more than **25% of the RSA balance**.',
      'On the **death** of the employee, the balance is paid to the named beneficiaries under '
      'a will or letters of administration, together with the group life insurance proceeds.',
    ]},
    {'h4': 'Modes of withdrawal at retirement'},
    {'ol': [
      '**Programmed monthly or quarterly withdrawal**, computed by the PFA on the basis of the '
      'retiree\'s expected life span.',
      '**Annuity for life** purchased from a life insurance company licensed by NAICOM, under '
      'guidelines jointly issued with PenCom, with monthly or quarterly payments.',
      '**A lump sum** from the balance, provided that the amount left is sufficient to procure '
      'a programmed withdrawal or annuity of not less than **50% of the retiree\'s annual '
      'remuneration as at the date of retirement**.',
    ]},
    {'h4': 'Exemptions from the scheme'},
    {'ul': [
      'Members of the **Armed Forces**, the **Department of State Services**, the **National '
      'Intelligence Agency** and the **Nigerian Financial Intelligence Unit**.',
      'Employees who, as at the commencement of the 2004 Act, had **three years or less to '
      'retire**.',
      'Categories of persons covered by section 291 of the Constitution (judicial officers) in '
      'respect of the pension provided there.',
    ]},
    {'note': 'The **minimum pension guarantee** provided by section 84 is a further feature: '
             'PenCom may, subject to guidelines, guarantee a minimum pension to a retiree who '
             'has contributed for a specified number of years. A **Pension Protection Fund** '
             'is established for the purpose, funded by an annual subvention, an annual pension '
             'protection levy on the Commission and licensed operators, and income from the '
             'fund\'s investments.'},
  ]},

  {'n': '4.5', 't': 'Gratuity', 'b': [
    {'p': 'Under the old defined benefit arrangement, **gratuity** was a lump sum paid on '
          'retirement in addition to a monthly pension, both computed from final salary and '
          'length of service. The Contributory Pension Scheme does not provide a separate '
          'gratuity: the lump sum a retiree may take is drawn from the balance in his own '
          'Retirement Savings Account, subject to the 50% test above.'},
    {'p': 'An employer may, however, operate a **separate gratuity scheme** in addition to the '
          'statutory pension contribution, either as a contractual benefit or under a collective '
          'agreement. Where it does, the gratuity is an employee benefit accounted for under '
          'IPSAS 39 (Chapter 5), and if it is a defined benefit promise it requires actuarial '
          'valuation.'},
    {'warn': 'A question asking you to "compute the gratuity" is almost always set under the '
             'old defined benefit rules or under a stated scheme rule, and will give you the '
             'formula — typically a percentage of final annual salary for each year of '
             'pensionable service. Read the rule given in the question; do not import one.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Monthly emolument',
   'tex': '\\text{Basic} + \\text{Housing} + \\text{Transport}'},
  {'lb': 'Employer contribution',
   'tex': '10\\% \\times \\text{Monthly emolument}'},
  {'lb': 'Employee contribution',
   'tex': '8\\% \\times \\text{Monthly emolument}'},
  {'lb': 'Group life cover',
   'tex': '3 \\times \\text{Annual total emolument}'},
  {'lb': 'Lump sum constraint',
   'tex': '\\text{Residual balance} \\ge \\text{fund a pension of } 50\\% '
          '\\text{ of final annual remuneration}'},
 ],
 'focus':
   'Reliably examined. One or two Section A marks on the contribution rates, the meaning of '
   'monthly emolument, or the roles of the PFA and PFC. Section B commonly asks for the '
   'features of the Contributory Pension Scheme, the reasons the old defined benefit scheme '
   'failed, or a computation of contributions from a salary schedule. The computation is easy '
   'marks provided the pensionable emolument is identified correctly.',
 'errors': [
   'Applying the contribution percentages to gross pay instead of to basic, housing and '
   'transport.',
   'Giving the employer rate as 7.5% and the employee rate as 7.5%; those were the rates under '
   'the 2004 Act, superseded in 2014 by 10% and 8%.',
   'Saying the PFA holds the pension assets; the PFC does.',
   'Stating the remittance period as seven calendar days rather than seven working days.',
   'Treating the group life insurance premium as part of the 18% contribution; it is separate '
   'and additional.',
   'Forgetting that the lump sum is limited by the requirement to leave enough to fund 50% of '
   'final annual remuneration.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Under the Pension Reform Act 2014, the minimum contribution rates are',
    'o': ['7.5% employer and 7.5% employee', '10% employer and 8% employee',
          '8% employer and 10% employee', '15% employer and 5% employee',
          '10% employer and 10% employee'],
    'a': 1,
    'w': 'The 2014 Act raised the combined rate to 18%, split 10% employer and 8% employee. '
         '7.5% each were the rates under the repealed 2004 Act.',
    'src': 'Chapter 4.2'},
   {'q': 'For pension purposes, "monthly emolument" means',
    'o': ['gross monthly salary', 'basic salary plus housing and transport allowances',
          'basic salary only', 'basic salary plus all allowances',
          'net salary after tax and deductions'],
    'a': 1,
    'w': 'The Act defines it as basic salary, housing allowance and transport allowance. Other '
         'allowances are excluded unless the employer elects to include them.',
    'src': 'Chapter 4.2'},
   {'q': 'Pension contributions must be remitted to the Pension Fund Custodian within',
    'o': ['seven calendar days of payment of salary',
          'seven working days of payment of salary',
          'thirty days of the end of the month', 'fourteen working days',
          'the end of the following month'],
    'a': 1,
    'w': 'Section 11(3)(b) requires remittance within seven working days of paying the salary, '
         'with a penalty of not less than 2% per month on late remittance.',
    'src': 'Chapter 4.2'},
   {'q': 'The body that holds pension fund assets in trust is the',
    'o': ['Pension Fund Administrator', 'Pension Fund Custodian',
          'National Pension Commission', 'Central Bank of Nigeria', 'employer'],
    'a': 1,
    'w': 'The PFC holds the assets; the PFA manages and invests them but never holds them. That '
         'separation is the central control of the scheme.',
    'src': 'Chapter 4.3'},
   {'q': 'An employer must maintain a group life insurance policy for each employee of not less '
         'than',
    'o': ['twice the annual total emolument', 'three times the annual total emolument',
          'five times the annual basic salary', 'the annual total emolument',
          'ten times the monthly emolument'],
    'a': 1,
    'w': 'Section 4(5) requires cover of a minimum of three times the annual total emolument, '
         'in addition to the pension contributions.',
    'src': 'Chapter 4.2'},
   {'q': 'An employee with an annual basic salary of ₦1,800,000, housing allowance ₦450,000 and '
         'transport allowance ₦150,000 will have an annual employee pension contribution of',
    'o': ['₦144,000', '₦192,000', '₦240,000', '₦180,000', '₦216,000'],
    'a': 1,
    'w': 'Pensionable emolument is $1{,}800{,}000 + 450{,}000 + 150{,}000 = ₦2{,}400{,}000$; '
         'the employee contributes 8% of it.',
    'calc': '8\\% \\times 2{,}400{,}000 = ₦192{,}000',
    'src': 'Chapter 4.2'},
  ],
  'theory': [
   {'q': 'The Pension Reform Act 2014 established a Contributory Pension Scheme in place of the '
         'defined benefit arrangement previously operated in the public service. '
         '(a) Distinguish between a defined benefit and a defined contribution pension scheme. '
         '(b) Explain why the previous defined benefit scheme failed. (c) Describe the roles of '
         'the National Pension Commission, the Pension Fund Administrator and the Pension Fund '
         'Custodian. (d) State the modes by which a retiree may withdraw benefits from a '
         'Retirement Savings Account.',
    'marks': 20,
    'a': [
      {'h4': '(a) The two types of scheme'},
      {'table': {'align': 'lll',
        'head': ['Feature', 'Defined benefit', 'Defined contribution'], 'rows': [
        ['The promise', 'A stated pension, typically a fraction of final salary for each year '
         'of service', 'No stated pension; the benefit is whatever the accumulated fund will '
         'provide'],
        ['Contributions', 'Set at whatever level is needed to fund the promise; usually the '
         'employer alone', 'A fixed percentage of emoluments by both employer and employee'],
        ['Who bears investment risk', 'The employer, who must make good any shortfall',
         'The employee, whose pension rises or falls with investment returns'],
        ['Who bears longevity risk', 'The employer, who must pay for as long as the pensioner '
         'lives', 'The employee, unless an annuity is purchased'],
        ['Funding', 'Frequently unfunded and paid from current revenue',
         'Fully funded in an individual account before benefits fall due'],
        ['Portability', 'Poor — the benefit is tied to service with the one employer',
         'Complete — the Retirement Savings Account follows the employee'],
        ['Accounting complexity', 'High; requires actuarial valuation and recognition of a net '
         'liability', 'Low; the expense is simply the contribution payable for the period'],
      ]}},
      {'h4': '(b) Why the previous scheme failed'},
      {'ol': [
        '**It was unfunded.** Pensions were paid out of the annual budget as they fell due, '
        'with no fund set aside. When revenue was short, pensions were simply not paid, and '
        'arrears accumulated into hundreds of billions of naira.',
        '**The liability was never measured.** Because no actuarial valuation was performed, '
        'government did not know the size of the obligation it had incurred, and successive '
        'budgets under-provided for it.',
        '**Records were unreliable.** There was no reliable database of pensioners. Verification '
        'exercises repeatedly disclosed large numbers of ghost pensioners, and genuine '
        'pensioners were excluded through poor record-keeping.',
        '**Administration was weak and corrupt.** The pension administration was fragmented '
        'across ministries and agencies; several large-scale frauds were subsequently '
        'prosecuted.',
        '**Benefits were not portable.** An employee who moved between the public and private '
        'sectors, or between agencies, frequently lost accrued entitlement.',
        '**Payment was humiliating and unreliable.** Elderly pensioners were required to attend '
        'periodic verification exercises in person, sometimes waiting for days, and payments '
        'were months or years in arrears.',
        '**Coverage was narrow.** Most private sector employees had no pension arrangement at '
        'all.',
      ]},
      {'h4': '(c) The institutional roles'},
      {'p': '**National Pension Commission (PenCom)** — the regulator. It licenses and '
            'supervises Pension Fund Administrators and Custodians; issues guidelines, rules and '
            'standards for the administration and investment of pension funds; approves the '
            'categories of investment and the limits on each; maintains a national databank of '
            'contributors; receives and resolves complaints; carries out routine and special '
            'examinations of operators; and imposes sanctions for breach. It does not manage or '
            'hold any pension money.'},
      {'p': '**Pension Fund Administrator (PFA)** — the manager. It opens and maintains the '
            'Retirement Savings Account for each contributor; invests and manages the pension '
            'fund within the categories PenCom permits; maintains books of account on all '
            'transactions; provides each contributor with a statement of account at least once '
            'a year; computes and pays retirement benefits; and reports to the Commission. It '
            'gives instructions to the custodian but never holds the assets itself.'},
      {'p': '**Pension Fund Custodian (PFC)** — the trustee of the assets. It receives '
            'contributions remitted by employers on behalf of the PFA and notifies the PFA '
            'within 24 hours; holds the pension fund assets in trust for the contributors; '
            'settles transactions and undertakes activities relating to the assets only on the '
            'instruction of the PFA; and reports to the Commission. It has no discretion over '
            'the investment of the fund.'},
      {'p': 'The separation of the three functions is deliberate and is the principal safeguard '
            'in the scheme. The administrator decides but cannot touch the money; the custodian '
            'holds the money but cannot decide; and the Commission supervises both. No single '
            'party can misapply the fund without the concurrence of another.'},
      {'h4': '(d) Modes of withdrawal'},
      {'ol': [
        '**Programmed withdrawal** — monthly or quarterly payments computed by the PFA by '
        'reference to the retiree\'s expected life span, drawn from the balance in the account, '
        'which continues to earn investment income.',
        '**Annuity for life** — purchased from a life insurance company licensed by NAICOM '
        'under guidelines jointly issued by NAICOM and PenCom, providing monthly or quarterly '
        'payments for life.',
        '**A lump sum from the balance** — provided that the amount remaining after the '
        'withdrawal is sufficient to fund a programmed withdrawal or an annuity of not less '
        'than 50% of the retiree\'s annual remuneration as at the date of retirement.',
      ]},
      {'note': 'A retiree who disengages before the age of 50 and remains unemployed for four '
               'months may withdraw not more than 25% of the balance, and on the death of a '
               'contributor the balance is paid to the beneficiaries named under a will or '
               'letters of administration, together with the proceeds of the group life '
               'policy.'}],
    'src': 'Chapter 4.1–4.4'},
  ]},
}
