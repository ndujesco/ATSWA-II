CH = {
 'n': 4,
 't': 'Accruals, Prepayments, Provisions and Bad Debts',
 'brief': 'The period-end adjustments that turn a cash record into an accruals-based profit: '
          'deferred revenue, prepayments, accrued expenses and accrued revenue, depreciation as '
          'the non-current-asset version of the same idea, and writing down what customers will '
          'not pay — including a source-material worked example that gets its own arithmetic '
          'wrong in exactly the way this topic most often trips candidates up.',
 'outcomes': [
   'Explain prepayments and accruals, and why adjustments for them are needed at all',
   'Pass adjusting entries in respect of prepayments, accruals, deferred revenue and accrued revenue',
   'Compute and record depreciation and understand why it needs the same logic as an accrual',
   'Explain and pass entries in respect of bad (irrecoverable) debts and the allowance for doubtful debts',
   'Record increases and decreases in the allowance for doubtful debts — correctly',
   'Account for the recovery of a debt previously written off',
   'Calculate and make entries in respect of the allowance for discount on receivables',
   'Prepare a statement of profit or loss and statement of financial position extract showing '
   'the treatment of bad debts, the allowance for doubtful debts, depreciation, and the '
   'allowance for discount on receivables',
 ],
 'secs': [
  {'n': '4.1', 't': 'Why these adjustments exist', 'b': [
    {'p': 'Adjustments occur in final accounts whenever certain events do not properly fit into '
          'the financial year as cash moved: either income has been earned but not yet received, '
          'or expenditure has been incurred but not yet paid for. In conformity with the '
          '**matching (accruals) concept**, all income and expenses must be accounted for in the '
          'accounting year they belong to — so income and expenses are either carried forward or '
          'provided for in the current year.'},
    {'p': 'In any financial year, day-to-day transactions create financial obligations and '
          'entitlements that do not automatically close out at the year end: interest that '
          'accrues daily on debts, rent payable for the use of an office, prepaid stationery '
          'expense, income receivable, and similar items in the day-to-day management of a '
          'business. Other resources and obligations arise as service is rendered, customers buy '
          'goods on credit, suppliers supply goods on credit, and lenders give loans with '
          'repayment following at specified dates. In most cases, the end of the accounting period '
          'simply does **not** coincide with the receipt or payment of cash associated with these '
          'events. **Adjusting entries** exist to record these resource changes — expenses '
          'accrued or prepaid, income receivable, and provisions for doubtful debts made where '
          'necessary — so that the financial statements truthfully and accurately represent the '
          'economic reality of the period.'},
    {'p': 'Accountants rely on two principles here. The **revenue recognition** principle requires '
          'revenue to be reported when earned, not before or after — for most entities, revenue '
          'is earned when goods and services are *delivered* to a customer, not when cash is '
          'eventually paid. If an entity sells goods on 31 December 2024, the revenue was earned '
          'in 2024 and belongs in the 2024 statement of profit or loss, even if the customer pays '
          'in 2025 — the amount owed is recorded as a trade receivable in the statement of '
          'financial position at 31 December 2024. Where there is a likelihood of default on that '
          'credit sale, the entity makes a **provision for doubtful debts** as an expense of 2024, '
          'reducing the receivable to its expected recoverable value. The **matching principle**, '
          'in turn, aims to report expenses in the *same* accounting period as the revenue earned '
          'as a result of incurring them — if a business earns monthly revenue while renting a '
          'store, the December rent belongs in the December statement of profit or loss, whether '
          'the rent was actually paid earlier, later, or exactly in December.'},
    {'p': 'The simple adjustments affecting the statement of profit or loss and the statement of '
          'financial position fall into four categories:'},
    {'ol': [
      'Allowances for irrecoverable and doubtful trade receivables;',
      'Allowance for discounts on trade receivables;',
      'Deferrals and prepayments;',
      'Accrued expenses and revenue.',
    ]},
    {'key': 'The last three categories are really **one idea applied four ways**: whenever cash '
            'moves in a different period from the income or expense it relates to, the difference '
            'is deferred (if cash moved *early*) or accrued (if cash will move *late*). The first '
            'category — allowances for doubtful debts — is a different idea again: it is not a '
            'timing difference at all, but **prudence** applied to an asset whose full recovery is '
            'in doubt (see §4.6).'},
  ]},

  {'n': '4.2', 't': 'Deferred revenue and prepayments', 'b': [
    {'p': '**Deferrals or prepayments** refer to transactions where cash is paid or received '
          '*before* a related expense or revenue is recognised. These transactions are recorded '
          'when cash is paid for expenses that apply to more than one accounting period, or when '
          'cash is received for revenue that relates to more than one accounting period. The '
          'portion of the expense or revenue that applies to *future* periods is deferred — as a '
          '**prepaid expense (an asset)** or **unearned/deferred revenue (a liability)**. If no '
          'adjustment is made for prepayments and unearned revenue, profit for the current period '
          'will be **understated** or **overstated** respectively. Items that normally need to be '
          'prepaid include rates, rent, interest, insurance and road licensing fees.'},
    {'p': 'The accounting entry requires the prepayment to **reduce** the relevant expense in the '
          'statement of profit or loss, thereby increasing profit. The same logic applies to '
          'unearned revenue, where the adjusting entry **reduces** the relevant revenue in the '
          'statement of profit or loss, thereby decreasing profit. Conceptually, a prepayment '
          'represents an amount **owed to** the entity by a third party, and unearned revenue '
          'represents an amount **owed by** the entity to a third party — so they are included '
          'under current assets and current liabilities respectively in the statement of '
          'financial position.'},
    {'pre': 'Dr  Prepayments (statement of financial position)\n'
            '    Cr  Expenses (statement of profit or loss)\n\n'
            'Dr  Revenue (statement of profit or loss)\n'
            '    Cr  Unearned revenue (statement of financial position)'},
    {'h3': 'Illustration 4.1 — a prepaid expense'},
    {'p': 'Santo Ltd paid ¢2,400,000 for two years\' insurance protection, beginning 1 December '
          '2023. The cash payment is debited in full to the insurance account; as time passes, the '
          'benefit of the insurance gradually expires, and the unexpired portion is transferred to '
          'the next accounting period as a prepaid expense. One month\'s cover expires by 31 '
          'December 2023: $2{,}400{,}000 \\times \\tfrac{1}{24} = ¢100{,}000$.'},
    {'tacc': {'t': 'Insurance account — 2023', 'dr': [['Cash', 2400000], ['', 2400000, '@tot']],
      'cr': [['Profit or loss (1/24 × 2,400,000)', 100000], ['Prepaid c/d', 2300000],
             ['', 2400000, '@tot']]}},
    {'tacc': {'t': 'Insurance account — 2024', 'dr': [
        ['Prepaid b/f', 2300000], ['', 2300000, '@tot']],
      'cr': [['Profit or loss (12/24 × 2,400,000)', 1200000], ['Prepaid c/d', 1100000],
             ['', 2300000, '@tot']]}},
    {'p': 'The balances carried forward of ¢2,300,000 (2023) and ¢1,100,000 (2024) represent '
          'insurance prepaid, shown under current assets in the statement of financial position '
          'for each year respectively.'},
    {'table': {'head': ['Year', 'Detail', 'Dr (¢)', 'Cr (¢)'], 'align': 'llrr', 'rows': [
      ['2023', 'Insurance prepaid', '2,300,000', ''],
      ['', 'Insurance expense', '', '2,300,000'],
      ['2024', 'Insurance prepaid', '1,100,000', ''],
      ['', 'Insurance expense', '', '1,100,000'],
    ]}},
    {'h3': 'Illustration 4.2 — deferred revenue'},
    {'p': 'Santo Ltd rented a small office in its building to a customer on 1 January 2023. The '
          'rental agreement required payment of ¢1,800,000 cash in advance for 18 months\' rent, '
          'recorded as **Dr Cash / Cr Rent received**. At 31 December 2023 the unadjusted trial '
          'balance would report the full ¢1,800,000 as rent received, which is **overstated** by '
          '¢600,000 ($\\tfrac{6}{18} \\times 1{,}800{,}000$) relating to 2024.'},
    {'tacc': {'t': 'Rent received account — 2023', 'dr': [
        ['Profit or loss', 1200000], ['Balance c/d', 600000], ['', 1800000, '@tot']],
      'cr': [['Cash', 1800000], ['', 1800000, '@tot'], ['Balance b/d', 600000]]}},
    {'p': 'The balance carried forward of ¢600,000 represents **unearned (deferred) revenue**, '
          'recorded under current liabilities in the statement of financial position for 2023.'},
    {'pre': 'Dr  Rent receivable account          600,000\n    Cr  Deferred rent revenue               600,000'},
  ]},

  {'n': '4.3', 't': 'Accrued expenses', 'b': [
    {'p': 'Accrued expenses reflect transactions where cash is paid *after* a related expense is '
          'recognised. An accrued expense represents an item the firm has already benefited from '
          'during the current accounting period, but which will not be paid for until the next '
          'accounting period. If no adjustment is made, profit for the current period will be '
          '**overstated**. Examples of items that need to be accrued include electricity, since '
          'the bills are not likely to coincide exactly with the entity\'s accounting year end.'},
    {'pre': 'Dr  Expense (statement of profit or loss)          x\n    Cr  Accrued expense (statement of financial position)   x'},
    {'p': 'The relevant expense in the statement of profit or loss is **increased** by the accrued '
          'amount, while in the statement of financial position, accruals appear under current '
          'liabilities, reflecting an amount owing by the business.'},
    {'warn': 'The source study text labels the worked example below **"Illustration 4.2"** as '
             'well — the same number already used, two pages earlier, for the rent-received '
             'illustration in §4.2. It is renumbered here as a distinct example to avoid '
             'confusion; the figures themselves are transcribed exactly as given.'},
    {'h3': 'Illustration — an accrued expense'},
    {'p': 'Santo Ltd\'s trial balance recorded electricity expenses of ¢6,000,000, covering the '
          'period 1 January to 31 October 2023. A careful examination of previous bills shows the '
          'company\'s energy consumption is even throughout the period — so the ¢6,000,000 '
          'represents 10 months\' charge, and an accrual is needed for November and December: '
          '$¢6{,}000{,}000 \\times \\tfrac{2}{10} = ¢1{,}200{,}000$.'},
    {'tacc': {'t': 'Electricity expenses account', 'dr': [
        ['Cash', 6000000], ['Balance c/d', 1200000], ['', 7200000, '@tot']],
      'cr': [['Profit or loss', 7200000], ['', 7200000, '@tot'], ['Balance b/d', 1200000]]}},
    {'p': 'The balance carried forward of ¢1,200,000 represents an accrued expense, recognised '
          'as a current liability in the statement of financial position.'},
    {'pre': 'Dr  Electricity expense account       1,200,000\n    Cr  Accrued expense account                1,200,000'},
  ]},

  {'n': '4.4', 't': 'Accrued revenue', 'b': [
    {'p': 'Accrued revenue refers to transactions where cash is received *after* the related '
          'revenue is recognised. It represents an item the entity has already earned during the '
          'current accounting period, but which will not be received until the next period. If no '
          'adjustment is made, profit for the current period will be **understated**. Examples '
          'include interest earned on treasury bills for which payment has not yet been received, '
          'since the maturity of such bills is not likely to coincide exactly with the entity\'s '
          'accounting year end.'},
    {'pre': 'Dr  Accrued income (statement of financial position)     x\n'
            '    Cr  Interest receivable (statement of profit or loss)      x'},
    {'p': 'The relevant income in the statement of profit or loss is **increased** by the accrued '
          'amount; in the statement of financial position, the accrued income appears under '
          'current assets, reflecting an amount owed *to* the business.'},
    {'h3': 'Illustration 4.3 — interest receivable'},
    {'p': 'Sky Ltd\'s trial balance shows interest receivable of ¢855,000. Excluded from the trial '
          'balance is a 182-day Bank of Ghana bond, purchased 1 August 2024 at 15% per annum for '
          '¢12,000,000. Sky Ltd prepares accounts to 31 December each year. The bond will earn a '
          'total of $15\\% \\times 12{,}000{,}000 \\times \\tfrac{6}{12} = ¢900{,}000$ over its '
          '182-day (6-month) life, running from 1 August 2024 to 31 January 2025. Five of those '
          'six months (August to December) fall in 2024, so $\\tfrac{5}{6} \\times 900{,}000 = '
          '¢750{,}000$ must be accrued in the 2024 statement of profit or loss, even though the '
          'cash will only be received after the year end.'},
    {'tacc': {'t': 'Interest receivable account', 'dr': [
        ['Profit or loss', 1605000], ['', 1605000, '@tot'], ['Balance b/d', 750000]],
      'cr': [['Cash', 855000], ['Balance c/d', 750000], ['', 1605000, '@tot']]}},
    {'pre': 'Dr  Interest accrued account          750,000\n    Cr  Interest receivable account             750,000'},
  ]},

  {'n': '4.5', 't': 'Non-current assets and depreciation expense', 'b': [
    {'p': 'Non-current assets (both tangible and intangible) reduce in value over their expected '
          'useful life, for various reasons. That reduction in value is accounted for using '
          '**depreciation** — the depreciable value of a non-current asset is spread over its '
          'useful life, exactly as an accrued or prepaid expense spreads a cost over the periods '
          'that actually benefit from it.'},
    {'pre': 'Dr  Depreciation expense (statement of profit or loss)          X\n'
            '    Cr  Accumulated depreciation (statement of financial position)  X'},
    {'p': 'The effect of this entry is to show depreciation as a business expense in the statement '
          'of profit or loss, reflecting the proportion of cost or valuation attributable to the '
          'current period. It must not be forgotten that **depreciation is a non-cash item** — it '
          'is a book adjustment only, and does not involve the physical movement of any cash.'},
    {'h3': 'Illustration 4.4 — straight-line depreciation, split by function'},
    {'p': 'Santos Ltd depreciates two assets on the straight-line method: a building costing '
          '¢1,600,000 with a residual value of ¢100,000 and a 15-year estimated useful life, used '
          '46% for selling and 54% for administration; and equipment costing ¢910,000 with a '
          'residual value of ¢10,000 and a 10-year useful life, used 40% for selling and 60% for '
          'administration.'},
    {'table': {'head': ['Asset', 'Annual depreciation', 'Selling (¢)', 'Administration (¢)'],
     'align': 'llrr', 'rows': [
      ['Building', '(1,600,000 − 100,000) ÷ 15', '46,000', '54,000'],
      ['Equipment', '(910,000 − 10,000) ÷ 10', '36,000', '54,000'],
      ['Total', '', '82,000', '108,000'],
    ]}},
    {'pre': 'Dr  Depreciation — selling expense              82,000\n'
            'Dr  Depreciation — administration expense      108,000\n'
            '    Cr  Accumulated depreciation — building         100,000\n'
            '    Cr  Accumulated depreciation — equipment          90,000'},
    {'p': 'The adjusting entry reduces the **carrying amount** of the building and equipment. The '
          'accumulated depreciation account is a **contra account** with a balance stated against '
          'that of the asset account it relates to — it is deducted from the gross building and '
          'equipment accounts, leaving carrying amounts of ¢1,500,000 (¢1,600,000 − ¢100,000) and '
          '¢820,000 (¢910,000 − ¢90,000) for the building and equipment respectively, in the '
          'statement of financial position.'},
  ]},

  {'n': '4.6', 't': 'Bad (irrecoverable) debts', 'b': [
    {'p': 'An entity that sells its goods on a purely cash basis does not have to worry about '
          'customers not paying for such goods. This is not always the case in reality: goods and '
          'services are usually sold or rendered on credit, giving rise to trade receivables, and '
          'the business entity is therefore taking the risk that some customers will default on '
          'payment. **Trade receivables that cannot be collected are called bad debts or '
          'irrecoverable debts** — the risk of doing business on credit terms.'},
    {'p': 'Where a customer\'s debt is found to be irrecoverable, it must be **completely written '
          'off** from the receivables account. Writing off a debt reduces the value of the '
          'business\'s assets (receivables); this has the effect that the business has incurred a '
          'loss, accounted for by increasing the irrecoverable debts expense — which reduces both '
          'profit and, ultimately, the net assets of the business.'},
    {'pre': 'Dr  Bad/irrecoverable debts expense account (statement of profit or loss)   x\n'
            '    Cr  Trade receivables account (statement of financial position)              x'},
    {'p': 'Entities should periodically review their receivables and identify debts unlikely to be '
          'collected in full; these are then written off. This practice prevents the '
          'overstatement of both profit and assets, and should be applied wherever irrecoverable '
          'debts are probable and can be estimated. At the end of the accounting period, the total '
          'debt written off is transferred from the irrecoverable debts account to the statement '
          'of profit or loss.'},
    {'h3': 'Illustration 4.5 — the allowance for doubtful debts, and where the source solution '
     'goes wrong'},
    {'p': 'Kumasi Venture\'s trial balance shows: trade receivables ¢500,000, allowance for '
          'doubtful debt ¢50,000 (Cr), trade payable ¢100,000, gross profit ¢150,000, capital '
          '¢200,000. Eight independent situations are then considered.'},
    {'warn': 'This is the single most important correction in the whole chapter, because the '
             'source study text\'s own worked solution makes exactly the mistake this topic is '
             'most famous for tripping candidates up on — treating "**increase the allowance TO** '
             'a target figure" as if it meant "**increase the allowance BY** that figure." The '
             'rule, always, is: **only the movement between the opening and closing allowance is '
             'charged to (or credited back to) profit or loss.** The closing balance shown in the '
             'statement of financial position is always the new *target* figure itself — never '
             'the opening balance plus the whole target added on top. Situations I and III below '
             'are worked exactly as the source text presents them, with the error clearly marked, '
             'immediately followed by the correct working. Situations II and IV–VIII are '
             'transcribed as the source gives them, because the source gets those ones right.'},
    {'eg': {'t': 'Situation I — "increase the allowance for doubtful debt to 15%" (source '
     'solution is wrong)', 'q': [
      {'p': 'What the source text does: it calculates 15% of ¢500,000 = ¢75,000, and then '
            'charges the *entire* ¢75,000 to profit or loss, on top of the existing ¢50,000 '
            'allowance — producing a closing allowance of ¢50,000 + ¢75,000 = **¢125,000**, and '
            'net trade receivables of ¢500,000 − ¢125,000 = ¢375,000.'}],
      'a': [
      {'p': '**Why this is wrong.** "Increase the allowance *to* 15%" means the **closing '
            'balance itself** should be 15% of receivables, i.e. ¢75,000 — not that a further '
            '¢75,000 should be piled on top of the ¢50,000 already there. Only the **movement** '
            'from ¢50,000 to ¢75,000 — an increase of ¢25,000 — has actually happened this year '
            'and belongs in profit or loss.'},
      {'stmt': {'t': 'The correct working', 'rows': [
        ['Required closing allowance: 15% × 500,000', 75000],
        ['Less opening allowance', -50000],
        ['Increase charged to profit or loss', 25000, '@tt'],
      ]}},
      {'stmt': {'t': 'Statement of profit or loss extract (corrected)', 'rows': [
        ['Gross profit', 150000],
        ['Less: increase in allowance for doubtful debt', -25000],
        ['Profit for the year', 125000, '@tt'],
      ]}},
      {'stmt': {'t': 'Statement of financial position extract (corrected)', 'rows': [
        ['Trade receivables', 500000],
        ['Less allowance for doubtful debt', -75000],
        ['Net trade receivables', 425000, '@tt'],
      ]}},
      {'note': 'The source\'s own figures (profit ¢75,000; net receivables ¢375,000) are both '
               '¢50,000 out — exactly the opening allowance, double-counted. That is the '
               'signature of this exact error: whenever a "closing balance" answer is too low (or '
               'a "profit" answer too low) by precisely the opening allowance, this is the mistake '
               'that has been made.'}]}},
    {'eg': {'t': 'Situation III — "allowances increase to ¢62,000" (source solution is also '
     'wrong, the same way)', 'q': [
      {'p': 'What the source text does: it treats ¢62,000 as the amount to be *added* to the '
            'existing ¢50,000, giving a closing allowance of ¢50,000 + ¢62,000 = **¢112,000**, '
            'and charges the full ¢62,000 to profit or loss.'}],
      'a': [
      {'p': '**Correct reading.** "Increase... to ¢62,000" fixes the **closing balance** at '
            '¢62,000. The movement — the only amount that ever touches profit or loss — is '
            '¢62,000 − ¢50,000 = ¢12,000.'},
      {'stmt': {'t': 'The correct working', 'rows': [
        ['Required closing allowance', 62000],
        ['Less opening allowance', -50000],
        ['Increase charged to profit or loss', 12000, '@tt'],
      ]}},
      {'stmt': {'t': 'Statement of profit or loss extract (corrected)', 'rows': [
        ['Gross profit', 150000],
        ['Less: increase in allowance for doubtful debt', -12000],
        ['Profit for the year', 138000, '@tt'],
      ]}},
      {'stmt': {'t': 'Statement of financial position extract (corrected)', 'rows': [
        ['Trade receivables', 500000],
        ['Less allowance for doubtful debt', -62000],
        ['Net trade receivables', 438000, '@tt'],
      ]}}]}},
    {'p': 'The remaining six situations, transcribed exactly as the source gives them — and '
          'correctly worked there:'},
    {'table': {'head': ['Situation', 'Instruction', 'Closing allowance (¢)', 'Movement',
     'Effect on profit', 'Net receivables (¢)'], 'align': 'llrlll', 'rows': [
      ['II', 'Increase allowance by 2½%', '62,500', 'Increase of 12,500 (2½% × 500,000)',
       'Profit falls to ¢137,500', '437,500'],
      ['IV', 'Reduce allowance by ¢10,000', '40,000', 'Decrease of 10,000',
       'Profit rises to ¢160,000', '460,000'],
      ['V', 'Reduce allowance to 7½% of receivables', '37,500', 'Decrease of 12,500 '
       '(50,000 − 37,500)', 'Profit rises to ¢162,500', '462,500'],
      ['VI', 'Decrease allowance by 3% of receivables', '35,000', 'Decrease of 15,000 '
       '(3% × 500,000)', 'Profit rises to ¢165,000', '465,000'],
      ['VII', 'Allowance no longer required', '0', 'Decrease of the full 50,000',
       'Profit rises to ¢200,000', '500,000'],
      ['VIII', 'A customer owing ¢80,000 is declared bankrupt', 'n/a — this is a write-off, not '
       'an allowance change', 'Bad debt of 82,000 (see note)', 'Profit falls to ¢68,000',
       '368,000'],
    ]}},
    {'note': 'Situation VIII is worth reading carefully: it is **not** an allowance movement at '
             'all — it is an irrecoverable debt actually being written off, so the receivable is '
             'removed entirely, not merely provided against. The source solution\'s own figures '
             'here use a ¢82,000 bad debt expense against a receivable balance shown net of both '
             'the original ¢50,000 allowance *and* the ¢82,000 write-off (¢500,000 − ¢50,000 − '
             '¢82,000 = ¢368,000) — this situation, unlike I and III, is transcribed here exactly '
             'as correctly given.'},
    {'h3': 'Illustration 4.6 — irrecoverable debts across three years'},
    {'p': 'Jack Terror has been in business for several years, dealing in second-hand clothes. '
          'Over three years to 31 October he presented:'},
    {'table': {'head': ['Year ended', 'Credit sales (¢)', 'Irrecoverable debts (¢)'], 'align':
     'lrr', 'rows': [
      ['31 October 2022', '4,500,000', '1,200,000'],
      ['31 October 2023', '8,750,000', '3,850,000'],
      ['31 October 2024', '12,200,000', '6,300,000'],
    ]}},
    {'table': {'head': ['Year', 'Sales (¢)', 'Irrecoverable debts written off (¢)',
     'Closing receivables c/d (¢)'], 'align': 'lrrr', 'rows': [
      ['2022', '4,500,000', '1,200,000', '3,300,000'],
      ['2023', '8,750,000', '3,850,000', '4,900,000'],
      ['2024', '12,200,000', '6,300,000', '5,900,000'],
    ]}},
    {'note': 'The source presents each year\'s trade receivables account **independently** — '
             'sales less that year\'s write-offs — rather than carrying the previous year\'s '
             'closing balance forward as an opening balance (each closing figure above is simply '
             'that year\'s sales less that year\'s irrecoverable debts, e.g. 2023: '
             '$8{,}750{,}000 - 3{,}850{,}000 = 4{,}900{,}000$). In a real trade receivables '
             'account, of course, the closing balance also carries the opening balance and any '
             'cash collected during the year — this illustration is simplified purely to show the '
             'effect of the write-off on the year\'s own sales.'},
    {'note': 'Each year, the whole amount written off is transferred straight to the statement of '
             'profit or loss as an expense — ¢1,200,000 in 2022, ¢3,850,000 in 2023, ¢6,300,000 '
             'in 2024 — and deducted from gross profit to arrive at profit for the year.'},
  ]},

  {'n': '4.7', 't': 'Allowance for doubtful debts and irrecoverable debts — the underlying logic', 'b': [
    {'p': 'It is the process of making allowance for the possibility that a debt will become '
          'irrecoverable in the future, but for an amount that cannot yet be calculated with '
          'substantial accuracy. In the case of doubtful debts, the amount, or its estimate, still '
          'remains in the list of receivables and is **not** cancelled from the receivables '
          'account — unlike a debt that has actually become irrecoverable. A doubtful-debt '
          'allowance does not relate to any specific debtor; rather, the business recognises that '
          'not all existing debts will be collected, and prudence requires that this uncertainty '
          'be reflected in both the statement of profit or loss and the statement of financial '
          'position.'},
    {'h3': 'The accounting treatment, step by step'},
    {'p': '**When a provision is made for the first time:**'},
    {'pre': 'Dr  Statement of profit or loss (with the initial allowance)\n    Cr  Allowance for doubtful debts account'},
    {'p': 'This reduces the current year\'s profit, while in the statement of financial position '
          'the allowance is clearly shown, deducted from trade receivables.'},
    {'p': 'In subsequent accounting periods, a new estimate must be made of debts that may be '
          'considered doubtful. The new allowance is compared with the existing one:'},
    {'ul': [
      'Where the **current allowance is greater** than the previous one, the difference — the '
      '**increase** — is: **Dr** statement of profit or loss (with the increase), **Cr** '
      'allowance for doubtful debts (current allowance less previous allowance).',
      'Where the **current allowance is less** than the previous one, the difference — the '
      '**decrease** — is: **Dr** allowance for doubtful debts (with the reduction), **Cr** '
      'statement of profit or loss (previous allowance less current allowance).',
    ]},
    {'key': 'This is, word for word, the correct logic already applied above in §4.6 to fix '
            'situations I and III of Illustration 4.5 — **only ever the movement**, never the '
            'whole new percentage or figure stacked on top of what was already there.'},
    {'h3': 'Illustration 4.7 — the allowance for doubtful debts over three years, correctly done'},
    {'p': 'Viscosity Ltd has traded since 2022, dealing in mobile phones. It makes a provision '
          'for doubtful debt at 6% of receivables, and had no balance on the allowance at the '
          'start of 2022.'},
    {'table': {'head': ['Year ended 31 December', 'Receivables excl. irrecoverable debts (¢)',
     'Irrecoverable debts (¢)'], 'align': 'lrr', 'rows': [
      ['2022', '7,000,000', '1,000,000'],
      ['2023', '18,250,000', '2,500,000'],
      ['2024', '10,000,000', '4,300,000'],
    ]}},
    {'table': {'head': ['Year', 'Required allowance (6% of receivables)', 'Movement',
     'Effect on profit'], 'align': 'lrll', 'rows': [
      ['2022', '420,000', 'Increase of 420,000 (first allowance made)',
       'Charged in full against gross profit'],
      ['2023', '1,095,000', 'Increase of 675,000 (1,095,000 − 420,000)', 'A further charge of '
       '675,000 against gross profit'],
      ['2024', '600,000', 'Decrease of 495,000 (1,095,000 − 600,000)', 'A credit of 495,000 '
       '*added back* to gross profit — but the bad debts of ¢4,300,000 are still deducted '
       'separately'],
    ]}},
    {'stmt': {'t': '2024 statement of profit or loss extract', 'rows': [
      ['Gross profit', 'xxxxxxx'],
      ['Add: decrease in allowance for doubtful debt', 495000],
      ['Less: irrecoverable debts', -4300000],
      ['Net effect on profit', -3805000, '@tt'],
    ]}},
    {'table': {'head': ['Year', 'Trade receivables (¢)', 'Less allowance (¢)', 'Net (¢)'],
     'align': 'lrrr', 'rows': [
      ['2022', '7,000,000', '420,000', '6,580,000'],
      ['2023', '18,250,000', '1,095,000', '17,155,000'],
      ['2024', '10,000,000', '600,000', '9,400,000'],
    ]}},
    {'note': 'Notice the discipline this illustration demonstrates correctly, in contrast to '
             'Illustration 4.5: the **closing allowance** shown each year is always the freshly '
             'computed 6% figure itself (420,000; 1,095,000; 600,000) — never that figure added '
             'onto the year before\'s balance.'},
  ]},

  {'n': '4.8', 't': 'Allowance for discounts on trade receivables', 'b': [
    {'p': 'Some businesses also make an allowance for the cash (settlement) discount expected to '
          'be offered to customers on the trade receivables balance at the reporting date. The '
          'reasoning: since entities allow discounts on credit sales for prompt payment, recording '
          'the gross realisable value of receivables as merely the balance on the receivables '
          'account, less the allowance for doubtful debts alone, will **not** give the best '
          'estimate of the amount actually expected to be collected. The best estimate of the '
          'value of receivables is one that also gives effect to the cash discounts likely to be '
          'taken — hence the determination of an allowance for discounts on receivables.'},
    {'key': 'The way an allowance for discount on receivables is calculated is almost the same as '
            'for the allowance for doubtful debts alone — **except** that the rate or percentage '
            'must be applied to the **net** amount of trade receivables, *after* deducting the '
            'allowance for doubtful debts. This is because discounts are only ever allowed on '
            'debts that are actually expected to be paid — not on debts already judged '
            'irrecoverable.'},
    {'h3': 'Illustration 4.8 — allowance for discounts, over three years'},
    {'p': 'Mahatma Ltd has traded since 2022, dealing in Italian executive shoes.'},
    {'table': {'head': ['31 December', 'Trade receivables (¢)', 'Allowance for doubtful debts '
     '(¢)', 'Cash discount allowed (%)'], 'align': 'lrrr', 'rows': [
      ['2022', '17,000,000', '1,000,000', '4'],
      ['2023', '28,550,000', '4,500,000', '4'],
      ['2024', '22,000,000', '2,800,000', '4'],
    ]}},
    {'table': {'head': ['Year', 'Net receivables base', 'Allowance for discount (4%)',
     'Movement'], 'align': 'llrl', 'rows': [
      ['2022', '17,000,000 − 1,000,000 = 16,000,000', '640,000', 'First allowance: 640,000'],
      ['2023', '28,550,000 − 4,500,000 = 24,050,000', '962,000', 'Increase of 322,000 '
       '(962,000 − 640,000)'],
      ['2024', '22,000,000 − 2,800,000 = 19,200,000', '768,000', 'Decrease of 194,000 '
       '(962,000 − 768,000)'],
    ]}},
    {'stmt': {'t': 'Statement of financial position extract, 2022–2024', 'rows': [
      '2022', ['Trade receivables', 17000000], ['Less allowance for doubtful debt', -1000000],
      ['Less allowance for discount on receivables', -640000], ['Net', 15360000, '@tt'],
      '@gap',
      '2023', ['Trade receivables', 28550000], ['Less allowance for doubtful debt', -4500000],
      ['Less allowance for discount on receivables', -962000], ['Net', 23088000, '@tt'],
      '@gap',
      '2024', ['Trade receivables', 22000000], ['Less allowance for doubtful debt', -2800000],
      ['Less allowance for discount on receivables', -768000], ['Net', 18432000, '@tt'],
    ]}},
    {'note': 'Both the doubtful-debt allowance **and** the discount allowance are deducted from '
             'trade receivables to reach the net figure — the two allowances serve different '
             'purposes (one for debts that may never be paid at all, the other for debts that '
             'will be paid, but at a discount), and both must be provided for.'},
  ]},

  {'n': '4.9', 't': 'Irrecoverable debts recovered', 'b': [
    {'p': 'It is a common occurrence that a debt previously written off in an earlier accounting '
          'period may later be paid or recovered. In such a situation, the recovered debt should '
          'be **reinstated**. The debt is reinstated in the sales ledger account, to ensure a '
          'detailed and concise history of the customer is available as a guide for granting '
          'credit to the same customer in future — it also assists the entity in credit-rating '
          'all customers who buy goods from them on credit.'},
    {'p': 'The accounting entries when a debt is recovered:'},
    {'pre': 'Dr  Trade receivables account (with the amount of debt reinstated)\n'
            '    Cr  Irrecoverable debts recovered account\n\n'
            'Dr  Cash or bank account (with the amount recovered from the customer)\n'
            '    Cr  Trade receivables account (in full or part settlement of the debt owed)'},
    {'p': 'At the end of the accounting period, the balance in the irrecoverable debts recovered '
          'account is transferred either directly to the statement of profit or loss, or to the '
          'main irrecoverable debts account. Whichever way the transfer is made, it produces the '
          '**same result** — income of the period, offsetting the earlier expense.'},
  ]},

  {'n': '4.10', 't': 'Further reading', 'b': [
    {'note': 'The two IFRS standards this chapter sits closest to are '
             '[IAS 16 Property, Plant and Equipment](https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/), '
             'which governs depreciation in full, and '
             '[IAS 37 Provisions, Contingent Liabilities and Contingent Assets](https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/). '
             'Worth knowing, even though it is beyond this syllabus: modern IFRS no longer uses '
             'the "allowance for doubtful debts, based on management judgement" approach this '
             'chapter teaches at all. Since 2018, '
             '[IFRS 9 Financial Instruments](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/) '
             'requires an **expected credit loss** model instead — receivables are provided '
             'against from the moment they are recognised, using forward-looking data, rather '
             'than only once a specific doubt arises. [IFRS 9\'s summary page on ifrs.org]'
             '(https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/) '
             'is the place to read about this once the ATSWA-level treatment here is second '
             'nature. For the arithmetic itself, '
             '[AccountingCoach\'s notes on adjusting entries](https://www.accountingcoach.com/adjusting-entries/explanation) '
             'and on '
             '[bad debts and the allowance method](https://www.accountingcoach.com/bad-debts-expense/explanation) '
             'are clear, free companions to §4.1–4.8 above.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Expense charged for the period',
   'tex': '\\text{Charge} = \\text{Cash paid} + \\text{Closing accrual} - \\text{Opening accrual} '
          '- \\text{Closing prepayment} + \\text{Opening prepayment}',
   'nt': 'Or simply balance the expense T-account and take the transfer to profit or loss.'},
  {'lb': 'Movement in an allowance (doubtful debts or discount)',
   'tex': '\\text{Movement} = \\text{Closing allowance required} - \\text{Opening allowance}',
   'nt': 'The closing allowance is always the fresh target figure itself — never the opening '
         'balance plus the target added on top. See Illustration 4.5, situations I and III.'},
  {'lb': 'Allowance for discount base',
   'tex': '\\text{Base} = \\text{Receivables} - \\text{Allowance for doubtful debts}'},
 ],
 'focus':
   'This chapter is guaranteed marks, in Section A as a one-line computation and in Section B as '
   'part of a final-accounts question. The reliable earners: compute the charge from cash paid '
   'plus movements; charge only the movement in an allowance, never the whole new percentage or '
   'figure; apply the discount allowance to receivables net of the doubtful-debt allowance, never '
   'the gross figure. Section B questions often combine this with depreciation in a single '
   'adjustments schedule — practise them together. Above all, drill the "increase TO a figure" '
   'versus "increase BY a figure" distinction until it is automatic: it is the single most common '
   'trap in this entire topic, in this study text\'s own worked answers as much as in any exam.',
 'errors': [
   'Reading "increase the allowance to X" as "increase the allowance by X", and so charging the '
   'whole new percentage to profit or loss instead of just the movement — exactly the error in '
   'the source text\'s own Illustration 4.5, situations I and III.',
   'Applying the discount allowance to the gross receivables balance, instead of receivables net '
   'of the doubtful-debt allowance.',
   'Getting the sign wrong: an accrual increases the charge, a prepayment reduces it.',
   'Deducting an allowance from receivables in profit or loss rather than in the statement of '
   'financial position.',
   'Forgetting that depreciation is a non-cash adjustment — crediting cash instead of accumulated '
   'depreciation.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Wages paid during the year were ₦4,800,000. Wages accrued at the start were ₦210,000 '
         'and at the end ₦295,000. The charge to profit or loss is',
    'o': ['₦4,505,000', '₦4,715,000', '₦4,885,000', '₦4,800,000', '₦5,305,000'],
    'a': 2,
    'w': 'Add the closing accrual (used but not paid) and deduct the opening accrual (paid this '
         'year but belonging to last).',
    'calc': '4{,}800{,}000 + 295{,}000 - 210{,}000 = 4{,}885{,}000',
    'src': 'Chapter 4.3'},
   {'q': 'The allowance for doubtful debts was ₦140,000 at the start of the year and is to be '
         '₦185,000 at the end. Bad debts of ₦62,000 were written off during the year. The charge '
         'to profit or loss is',
    'o': ['₦45,000', '₦62,000', '₦107,000', '₦185,000', '₦247,000'],
    'a': 2,
    'w': 'Only the increase in the allowance is charged, plus the debts actually written off.',
    'calc': '62{,}000 + (185{,}000 - 140{,}000) = 107{,}000',
    'src': 'Chapter 4.6'},
   {'q': 'Receivables are ₦6,000,000 before adjustment. Debts of ₦200,000 are to be written off '
         'and a general allowance of 5% made. The closing allowance is',
    'o': ['₦300,000', '₦290,000', '₦310,000', '₦280,000', '₦200,000'],
    'a': 1,
    'w': 'Write off first, then take the percentage of what is left.',
    'calc': '0.05 \\times (6{,}000{,}000 - 200{,}000) = 0.05 \\times 5{,}800{,}000 = 290{,}000',
    'src': 'Chapter 4.6'},
   {'q': 'Why are accrued expenses shown in the financial statements?',
    'o': ['So that the correct total assets are shown',
          'So that the income of the period is matched against the cost of that period',
          'To show how much customers owe the business',
          'To reduce the non-current assets of the business',
          'To satisfy the money measurement concept'],
    'a': 1,
    'w': 'An accrual exists to satisfy the matching (accruals) concept: the expense belongs to '
         'the period in which the benefit was consumed, whether or not it has been paid.',
    'src': 'Chapter 4.1'},
   {'q': 'Insurance of ₦960,000 was paid on 1 October 2024 covering the twelve months to 30 '
         'September 2025. In the statement of financial position at 31 December 2024 this gives',
    'o': ['a prepayment of ₦240,000', 'a prepayment of ₦720,000', 'an accrual of ₦240,000',
          'an accrual of ₦720,000', 'no balance at all'],
    'a': 1,
    'w': 'Three months (October to December) belong to 2024 and nine months are paid in advance.',
    'calc': '\\frac{9}{12} \\times 960{,}000 = 720{,}000',
    'src': 'Chapter 4.2'},
   {'q': 'A debt of ₦85,000 written off two years ago was received in cash this year. The correct '
         'entry is',
    'o': ['Dr Receivables, Cr Cash', 'Dr Cash, Cr Receivables',
          'Dr Cash, Cr Irrecoverable debts recovered',
          'Dr Irrecoverable debts, Cr Cash', 'Dr Allowance for doubtful debts, Cr Cash'],
    'a': 2,
    'w': 'The receivable no longer exists — it was removed when the debt was written off. The '
         'cash received is therefore income of the current period.',
    'src': 'Chapter 4.9'},
  ],
  'theory': [
   {'q': 'Distinguish between an irrecoverable debt and an allowance for doubtful debts, and '
         'state the accounting entries for each.',
    'marks': 6,
    'a': [
      {'table': {'head': ['', 'Irrecoverable debt', 'Allowance for doubtful debts'],
        'align': 'lll', 'rows': [
        ['Certainty', 'Known to be uncollectable', 'Collection is doubtful but still possible'],
        ['The receivable', 'Removed from the ledger permanently', 'Remains in the ledger'],
        ['Nature of the account', 'An expense', 'A contra-asset offsetting receivables'],
        ['Charge to profit or loss', 'The full amount written off', 'Only the movement in the allowance'],
        ['Presentation', 'Reduces receivables directly', 'Deducted from receivables on the face of the statement'],
      ]}},
      {'h4': 'Entries'},
      {'ul': [
        'Write off: **Dr** Irrecoverable debts expense, **Cr** Trade receivables.',
        'Create or increase an allowance: **Dr** Statement of profit or loss, **Cr** Allowance '
        'for doubtful debts.',
        'Reduce an allowance: **Dr** Allowance for doubtful debts, **Cr** Statement of profit or loss.',
        'Recovery of a debt written off: **Dr** Trade receivables / Cash, **Cr** Irrecoverable '
        'debts recovered.']}],
    'src': 'Chapter 4.6'},
   {'q': 'Explain, with the accounting entry in each case, the treatment at the year end of '
         '(a) an accrued expense, (b) a prepaid expense, (c) accrued income and (d) deferred income.',
    'marks': 8,
    'a': [{'ol': [
      '**(a) Accrued expense** — the benefit has been consumed but not yet paid or invoiced. '
      '**Dr** the expense account, **Cr** accruals. The accrual is a current liability and it '
      '*increases* the charge above the cash paid.',
      '**(b) Prepaid expense** — cash has been paid for a benefit that belongs to a later period. '
      '**Dr** prepayments, **Cr** the expense account. The prepayment is a current asset and it '
      '*reduces* the charge below the cash paid.',
      '**(c) Accrued income** — income has been earned but the cash has not arrived. **Dr** '
      'accrued income, **Cr** the income account. A current asset, increasing income above cash '
      'received.',
      '**(d) Deferred income** — cash has been received for a service not yet rendered. **Dr** '
      'the income account, **Cr** deferred income. A current liability, reducing income below '
      'cash received.']},
      {'note': 'All four exist to satisfy the accruals concept, which requires income and '
               'expenses to be recognised as earned or incurred rather than as received or paid.'}],
    'src': 'Chapter 4.1'},
  ]},
}
