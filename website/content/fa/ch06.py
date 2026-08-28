CH = {
 'n': 6,
 't': 'Incomplete Records and Single Entry',
 'brief': 'Reconstructing a full set of accounts from a cash book, a bundle of invoices and two '
          'statements of affairs — worked through the study text\'s own three running '
          'illustrations, plus the margin/mark-up technique and the search for a cash '
          'defalcation, both essential to this topic even though this particular study text '
          'never quite spells them out on their own.',
 'outcomes': [
   'Use the accounting equation to calculate profit where only opening and closing net assets '
   'figures are available',
   'Convert single entry and incomplete records into double entry',
   'Prepare financial statements from records maintained on a single-entry basis',
   'Determine the figures for purchases and revenue from the purchases and receivables control '
   'accounts',
   'Derive expenses and revenue earned from incomplete records, including accruals and prepayments',
   'Use margin and mark-up to derive a missing cost-of-sales or inventory figure',
   'Identify a cash shortage (defalcation) from a cash and bank summary',
 ],
 'secs': [
  {'n': '6.1', 't': 'Single entry and incomplete records, precisely defined', 'b': [
    {'p': 'The term **single entry** "is applied to any system which does not provide for the '
          'two-fold aspect of transactions"; the alternative term, **incomplete records**, is '
          'often applied to books of account kept on such a single-entry or incomplete '
          'double-entry system.'},
    {'p': '"Single entry" recognises only the **personal** aspect of transactions, with '
          'receivables and payables. In practice, however, a cash book is invariably kept — but, '
          'with that one exception, the **impersonal** aspect of transactions (the nominal '
          'accounts: sales, purchases, expenses) is usually left entirely unrecorded. This is '
          'exactly the situation a sole trader or small partnership is typically in: they keep '
          'track of who owes them money and who they owe money to, and they keep a cash book, but '
          'they have never opened a full ledger of nominal accounts.'},
    {'p': 'In this chapter you learn the procedure for preparing the statement of profit or loss '
          'and the statement of financial position for an enterprise that has only opening and '
          'closing net assets, and perhaps capital, as the only known figures. You also learn how '
          'to ascertain the proprietor\'s drawings and any additional capital contribution during '
          'an accounting period from scanty information provided by a cash book summary.'},
    {'key': 'Questions on incomplete records and single entry are popular with examiners because '
            'they let the examiner test techniques that are also relevant to other topics — most '
            'obviously ledger control accounts (Chapter 5). They also provide the basic '
            'information necessary to prepare financial statements **without** the examiner ever '
            'handing you a trial balance — which is exactly why this topic feels so different '
            'from every other computational chapter in this paper.'},
  ]},

  {'n': '6.2', 't': 'Ascertaining profit from incomplete records', 'b': [
    {'p': 'Generally speaking, profit (or loss) is ascertained under the single-entry system by a '
          '**comparison of the values of net assets at two specified dates**, after taking into '
          'account additions to, or withdrawals from, capital during the period. The difference '
          'between these two values represents the profit or loss, according to whether there is '
          'an increase or a decrease in the figures.'},
    {'p': 'The accounting equation states that:'},
    {'tex': '\\text{Business Assets} = \\text{Owner\'s Capital} + \\text{Business Liabilities}'},
    {'p': 'which can be restated as:'},
    {'tex': '\\text{Owner\'s Capital} = \\text{Business Net Assets} - \\text{Business Liabilities}'},
    {'p': 'During an accounting period, where the business realises an excess of income over '
          'expenditure, the additional cash or assets generated **belong to the owner(s)**, thus '
          'increasing capital. The accounting equation now becomes:'},
    {'tex': '\\text{Opening capital} + \\text{Profit} = \\text{Opening net assets} + '
            '\\text{Increase in net assets}'},
    {'p': 'The introduction or withdrawal of resources by the owner will also increase or decrease '
          'the owner\'s capital. As a result, profit can be calculated using this format:'},
    {'stmt': {'rows': [
      'Closing capital ... XXX',
      'Less opening capital ... (XXX)',
      'Increase in net assets ... XXX',
      'Add owners\' drawings ... XXX',
      'Less additional capital ... (XXX)',
      'Net profit for the year ... XXX',
    ]}},
    {'tex': '\\text{Profit} = (\\text{Closing capital} - \\text{Opening capital}) + '
            '\\text{Drawings} - \\text{Additional capital}', 'tag': '(6.1)'},
    {'h3': 'Illustration 6.1 — profit by capital comparison alone'},
    {'p': 'Calculate the net profit for the year ended 31 December 2024 from the following:'},
    {'table': {'head': ['', '31/12/2023 (GH¢)', '31/12/2024 (GH¢)'], 'align': 'lrr', 'rows': [
      ['Property', '200,000', '200,000'],
      ['Equipment', '60,000', '90,000'],
      ['Trade receivables', '40,000', '80,000'],
      ['Cash', '10,000', '15,000'],
      ['Overdraft', '60,000', '90,000'],
      ['Trade payables', '50,000', '30,000'],
    ]}},
    {'p': 'Drawings during the year were GH¢45,000, and additional capital introduced during the '
          'year was GH¢50,000.'},
    {'stmt': {'t': 'Net assets at each date', 'rows': [
      '', '31/12/2023 (GH¢)', '31/12/2024 (GH¢)',
      ['Total assets (property + equipment + receivables + cash)', '310,000', '385,000'],
      ['Total liabilities (overdraft + payables)', '(110,000)', '(120,000)'],
      ['Net assets', '200,000', '265,000', '@tt'],
    ]}},
    {'stmt': {'t': 'Computation of profit', 'rows': [
      ['Closing capital', 265000],
      ['Less opening capital', -200000],
      ['Increase in net assets', 65000, '@t'],
      ['Owners\' drawings', 45000],
      ['Additional capital', -50000],
      ['Net profit for the year', 60000, '@tt'],
    ]}},
    {'note': 'This is exactly the **financial capital maintenance** computation already met in '
             'Chapter 2 §2.5 — the same arithmetic, just given a different name here. Whenever '
             'you see "statement of affairs" and "capital comparison" together, recognise it as '
             'the Chapter 2 formula wearing a Chapter 6 costume.'},
  ]},

  {'n': '6.3', 't': 'Preparing a full statement of profit or loss and statement of financial '
   'position from incomplete records', 'b': [
    {'p': 'It is understandably certain that calculating the profit of an enterprise using the '
          'method presented above is **not satisfactory** on its own. The accountant does not '
          'only prepare the final accounts of an enterprise but also communicates accounting and '
          'financial information to stakeholders — it is therefore much more informative when a '
          'full statement of profit or loss is drawn up. It is important for the accountant to '
          'convert these scanty and incomplete records into acceptable double-entry form.'},
    {'p': 'To prepare a full statement of profit or loss and statement of financial position from '
          'single entry and incomplete records, the following procedure is recommended, step by '
          'step:'},
    {'h3': 'Step 1 — the statement of affairs'},
    {'p': 'First construct a statement of financial position at the **beginning** of the '
          'accounting year — the assets and liabilities of the business must be ascertained and '
          'calculated. The statement prepared to show the financial position of the business at '
          'the beginning of the year is technically called a **"statement of affairs."**'},
    {'p': 'In most practical situations the owner of the business will provide lists of values of '
          'non-current assets used in the business, together with the dates of acquisition — it '
          'should therefore be easy to calculate accumulated depreciation on the non-current '
          'assets from the date of purchase to the date of reporting. Values of items such as '
          'inventories in trade, receivables and liabilities may have to be estimated with the '
          'help of the owner.'},
    {'p': 'From this information, a journal should be opened and accounting entries made with the '
          'aim of achieving the dual purpose of recording accounting transactions: appropriate '
          'debit entries are posted to asset accounts, and credit entries are entered into capital '
          'or liabilities accounts. **The difference between the assets and liabilities**, which '
          'usually ends up with the assets exceeding the liabilities, may be assumed to be the '
          'initial amount the owner used in starting the business, and is recorded as the '
          '**capital** of the business. Where the owner is able to state the initial amount used '
          'to commence the business, any difference between that stated capital and the estimated '
          'net assets may instead be recorded as the balance on the statement of profit or loss '
          'retained in the business.'},
    {'h3': 'Step 2 — the cash and bank summary'},
    {'p': 'Ascertain the cash position of the business. This is usually done by carefully '
          'examining any available bank statement, any pay-in-slip, and the cheque counterfoil. '
          'The bank statement, together with the cheque counterfoil, could reveal information '
          'concerning purchases, payment of rent, bank charges, wages, insurance, interest earned, '
          'the acquisition of non-current assets, and any personal withdrawals. Information '
          'extracted from the pay-in-slip, bank statement and credit alerts received will help '
          'determine the amount of money paid in by customers to whom goods were sold on credit, '
          'and also direct sales by cheque instead of cash. This information is used to prepare a '
          '**cash summary**, or a receipt and payment account, for the business.'},
    {'h3': 'Step 3 — analysis of unbanked cash sales'},
    {'p': 'At this stage, determine the amount of cash sales which have **not** been banked by the '
          'owner, but which might have been used to pay for business expenses, cash purchases, and '
          'personal drawings. It is possible the owner might also have made use of some of the '
          'physical inventory in trade for personal use — an informal interview with the owner '
          'could confirm the existence of such occurrences and so help the bookkeeper make an '
          'appropriate estimate for inventory drawings. Physical inventory counting at the close '
          'of business will give the actual closing inventory figure, so it need not be '
          'estimated.'},
    {'h3': 'Step 4 — posting from the cash and bank summary'},
    {'p': 'After the analysis above, the following postings can be made into the ledger. Note '
          'that, in Step 1, opening entries were made through the ledger, so some of these entries '
          'will be made into existing ledger accounts, irrespective of how inaccurate they may '
          'later prove to be.'},
    {'p': '**From the analysis of the debit side of the cash and bank summary**, and information '
          'obtained from the pay-in-slips:'},
    {'ol': [
      'All cash sales or takings should be credited to the trade receivables account in the sales '
      'ledger;',
      'Any proceeds from the sale of non-current assets should be credited to the respective '
      'asset account;',
      'Any interest or income from investment must also be credited to the appropriate revenue '
      'account;',
      'Any other item should be posted to the credit of the relevant account.',
    ]},
    {'p': '**From the analysis of the credit side of the cash and bank summary**, and information '
          'obtained from the cheque counterfoils:'},
    {'ol': [
      'All payments for goods purchased should be debited to the trade payables account in the '
      'purchase ledger;',
      'Payment of expenses should be debited to the relevant nominal account;',
      'All purchases in connection with non-current assets should be debited to the appropriate '
      'asset accounts;',
      'Any bank charges should be posted to the debit of the bank charges account;',
      'Any other item should be posted to the debit of the relevant account.',
    ]},
    {'key': 'Where a **difference exists** on the cash book summary once every known item has '
            'been posted, entries should be posted to make it balance. If the difference is on '
            'the **credit** side, the cash book should be credited and the proprietor\'s '
            '**drawings** account debited. If the difference is on the **debit** side, one can '
            'safely presume the owner has introduced **additional capital** — debit cash and '
            'credit the capital account of the business.'},
    {'h3': 'Step 5 — trade receivables and trade payables'},
    {'p': 'At this stage, year-end adjustments and balances must be determined. A schedule must be '
          'compiled detailing all customers who owe the business money, as a result of goods sold '
          'to them on credit. The total of the schedule of trade receivables represents debts owed '
          'to the business, and so must be carried forward to the **credit** of the total sales '
          'ledger control account. There is likely to be a **missing figure on the debit side** of '
          'the total trade receivables account, representing total sales on credit for the period, '
          'which should be transferred to the credit of the statement of profit or loss as sales '
          'or revenue.'},
    {'p': 'Another schedule that must be prepared is a list of amounts owed by the business to '
          'suppliers for goods purchased on credit. The total of this schedule represents the '
          'total liability by way of trade payables outstanding at the end of the period, and '
          'should be carried forward to the **debit** of the purchases ledger control account. '
          'Total purchases for the period will be derived from the **credit** side of the '
          'purchases ledger control account as a **balancing figure**, and should be transferred '
          'to the debit side of the statement of profit or loss.'},
    {'h3': 'Step 6 — extraction of a trial balance'},
    {'p': 'This is the final stage: once all the transactions above have been recorded, the entry '
          'process is complete, and the business is able to extract a trial balance — which forms '
          'the basis for preparing the statement of profit or loss and the statement of financial '
          'position.'},
  ]},

  {'n': '6.4', 't': 'Illustration 6.2 — a full reconstruction, worked in every step', 'b': [
    {'p': 'Boakye, a sole proprietor trading as KKB Enterprise, requested Oko & Associates, a firm '
          'of Chartered Accountants where you are employed as a trainee accountant, to prepare '
          'the accounts of his business for the year ended 31 December 2024. He did not maintain '
          'a double-entry bookkeeping system.'},
    {'p': 'The interview with Boakye revealed: all sales were on credit; during the year Boakye '
          'received GH¢9,025,000 by cheque and GH¢475,000 in cash from his customers; suppliers '
          'were paid GH¢6,840,000 by cheque; Boakye rented two premises — at Danso Man (for '
          'residential use) and on High Street (for business use). In July 2023 he paid GH¢480,000 '
          'as one year\'s rent in advance for his residence; in July 2024 he paid a further cheque '
          'of GH¢600,000 to cover another year\'s advance rent for his residence. Rent for the '
          'High Street business premises was GH¢60,000 per month throughout 2024, always paid by '
          'cheque. General business expenses paid by cheque amounted to GH¢106,200. He took cash '
          'of GH¢38,000 every month for his private use. Additional information at each date:'},
    {'table': {'head': ['', '31/12/2023 (GH¢)', '31/12/2024 (GH¢)'], 'align': 'lrr', 'rows': [
      ['Trade receivables', '1,045,000', '1,254,000'],
      ['Trade payables', '380,000', '617,500'],
      ['Rent owing', '120,000', '60,000'],
      ['Bank balance', '1,073,500', '3,000,000'],
      ['Cash in hand', '76,000', '60,000'],
      ['Inventories', '1,510,500', '1,700,500'],
      ['Furniture and fittings', '920,000', '—'],
    ]}},
    {'p': 'Depreciation is provided annually at 20% on furniture and fittings; Boakye agreed to '
          'pay GH¢100,000 as accountancy fees; and differences in the cash and bank balances at '
          'the end of 2024, once every known item is posted, represent additional drawings and '
          'capital respectively.'},
    {'h4': 'Working 1 — opening capital, from a statement of affairs'},
    {'p': 'We need the opening capital to enable us to calculate the closing balance in the '
          'statement of financial position. All that is required is to pick up all opening '
          'balances, not forgetting the balancing figure.'},
    {'stmt': {'t': 'Statement of affairs', 'rows': [
      '', '31/12/2024 (GH¢)', '31/12/2023 (GH¢)',
      ['Furniture & fittings (net, W5)', '736,000', '920,000'],
      ['Trade receivables', '1,254,000', '1,045,000'],
      ['Inventories', '1,700,500', '1,510,500'],
      ['Bank', '3,000,000', '1,073,500'],
      ['Cash in hand', '60,000', '76,000'],
      ['Trade payables', '(617,500)', '(380,000)'],
      ['Rent owing', '(60,000)', '(120,000)'],
      ['Accountancy fees owing', '(100,000)', '—'],
      ['Net worth (capital)', '5,973,000', '4,125,000', '@tt'],
    ]}},
    {'stmt': {'t': 'Computation of profit', 'rows': [
      ['Increase in net worth (5,973,000 − 4,125,000)', 1848000],
      ['Add drawings (456,000 + 600,000 + 35,000)', 1091000],
      ['', 2939000, '@t'],
      ['Less additional capital (W below)', -1227700],
      ['Net profit', 1711300, '@tt'],
    ]}},
    {'p': 'The three components of drawings are worth separating out, because each comes from a '
          'different place: **GH¢456,000** is the cash drawings actually stated in the question '
          '($38{,}000 \\times 12$); **GH¢600,000** is the July 2024 advance rent paid on Boakye\'s '
          '*personal residence* — this is a private expense paid out of the business bank '
          'account, so it is drawings, not a business expense, even though a cheque was written '
          'for it; and **GH¢35,000** is the balancing figure needed in the *cash* column of the '
          'cash book summary below, which — following the rule in §6.3 Step 4 — is presumed to be '
          'further drawings because the shortfall falls on the credit (payments) side.'},
    {'h4': 'Working 2 — the cash and bank summary'},
    {'tacc': {'t': 'Cash book summary — Cash column (GH¢)', 'dr': [
        ['Balance b/d', 76000], ['Received from customers', 475000], ['', 551000, '@tot']],
      'cr': [['Drawings (balancing figure)', 35000], ['Balance c/d', 60000],
             ['', 551000, '@tot']]}},
    {'tacc': {'t': 'Cash book summary — Bank column (GH¢)', 'dr': [
        ['Balance b/d', 1073500], ['Received from customers', 9025000],
        ['Additional capital (balancing figure)', 1227700], ['', 11326200, '@tot']],
      'cr': [['Suppliers', 6840000], ['Drawings — advance rent on residence', 600000],
             ['General business expenses', 106200], ['Rent (High Street, W3)', 780000],
             ['Balance c/d', 3000000], ['', 11326200, '@tot']]}},
    {'p': 'The additional capital of **GH¢1,227,700** is the balancing figure needed on the debit '
          '(receipts) side of the bank column to make it balance — following §6.3 Step 4 exactly, '
          'a shortfall on the *debit* side is presumed to be capital introduced.'},
    {'h4': 'Working 3 — the receivables and payables control accounts, for the missing sales and '
     'purchases figures'},
    {'tacc': {'t': 'Sales ledger control account (GH¢)', 'dr': [
        ['Balance b/d', 1045000], ['Sales (missing figure)', 9709000], ['', 10754000, '@tot']],
      'cr': [['Cash', 475000], ['Bank', 9025000], ['Balance c/d', 1254000],
             ['', 10754000, '@tot']]}},
    {'tacc': {'t': 'Purchases ledger control account (GH¢)', 'dr': [
        ['Bank', 6840000], ['Balance c/d', 617500], ['', 7457500, '@tot']],
      'cr': [['Balance b/d', 380000], ['Purchases (missing figure)', 7077500],
             ['', 7457500, '@tot']]}},
    {'h4': 'Working 4 — cost of goods sold'},
    {'stmt': {'rows': [
      ['Opening inventory (1/1/24)', 1510500],
      ['Purchases (W3)', 7077500],
      ['', 8588000, '@t'],
      ['Less closing inventory (31/12/24)', -1700500],
      ['Cost of goods sold', 6887500, '@tt'],
    ]}},
    {'h4': 'Working 5 — depreciation'},
    {'stmt': {'rows': [
      ['Fixtures and fittings at cost (1/1/24)', 920000],
      ['Less depreciation (20% × 920,000)', -184000],
      ['Net book value (31/12/24)', 736000, '@tt'],
    ]}},
    {'h4': 'Working — the rent expense control account, separating cash paid from the P&L charge'},
    {'p': 'Only the High Street *business* rent belongs in the statement of profit or loss — the '
          'GH¢600,000 residence advance is drawings, as already noted. The annual business rent '
          'is $60{,}000 \\times 12 = ₦720{,}000$, but the cash actually paid during the year is a '
          'different figure, once the opening and closing amounts owing are taken into account:'},
    {'tacc': {'t': 'High Street rent expense account (GH¢)', 'dr': [
        ['Bank (missing figure)', 780000], ['Balance c/d', 60000], ['', 840000, '@tot']],
      'cr': [['Balance b/d', 120000], ['Profit or loss (12 × 60,000)', 720000],
             ['', 840000, '@tot']]}},
    {'h4': 'The statement of profit or loss'},
    {'stmt': {'t': 'KKB Enterprise — Statement of profit or loss for the year ended 31 December '
     '2024 (GH¢)', 'rows': [
      ['Revenue (W3, sales control)', 9709000],
      ['Cost of sales (W4)', -6887500],
      ['Gross profit', 2821500, '@t'],
      '@gap',
      'Less expenses',
      ['Depreciation (W5)', 184000],
      ['Rent (business, High Street)', 720000],
      ['General business expenses', 106200],
      ['Consultancy (accountancy) fees', 100000],
      ['', 1110200, '@t'],
      ['Net profit', 1711300, '@tt'],
    ]}},
    {'note': 'Notice this ties out precisely with the profit already reached by capital comparison '
             'in Working 1 (GH¢1,711,300 both ways) — the two methods must always agree, and '
             'checking one against the other is the standard way to catch an arithmetic slip '
             'before you hand in a full reconstruction question.'},
    {'key': 'This illustration is worth studying closely because it combines **every** technique '
            'this chapter teaches in one place: a statement of affairs at both dates, a two-column '
            '(cash and bank) summary with a balancing-figure rule for drawings versus capital, '
            'control accounts for the missing sales and purchases figures, an expense control '
            'account to separate cash paid from the period\'s true charge, straight-line '
            'depreciation, and — the point most likely to catch you out — correctly identifying '
            'that a cheque paid for the owner\'s **personal** residence is drawings, never a '
            'business expense, no matter which bank account it was paid from.'},
  ]},

  {'n': '6.5', 't': 'Illustration 6.3 — reconstructing from till takings', 'b': [
    {'p': 'Damask is a retailer dealing in spare parts at Kokompe. He pays into his bank account '
          'the amount of his cash takings, **after** retaining GH¢10,000 per week for personal '
          'use and after paying wages and expenses out of the till. For the year ended 31 '
          'December 2024, those till payments were: staff wages GH¢1,200,000; goods (a cash '
          'purchase) GH¢220,000; cleaning GH¢75,000; carriage GH¢35,000; others GH¢20,000.'},
    {'p': 'The transactions through his bank account during the year:'},
    {'table': {'head': ['Receipts', 'GH¢', 'Payments', 'GH¢'], 'align': 'lrlr', 'rows': [
      ['Balance at 1 January 2024', '2,000,000', 'Suppliers', '30,830,000'],
      ['Lodgements from takings (cash)', '30,100,000', 'Rates', '400,000'],
      ['Bulk sales account (cheques)', '4,800,000', 'Furniture & fittings', '600,000'],
      ['Interest on treasury bills', '30,000', 'Telephone & electricity', '150,000'],
      ['', '', 'Rent', '400,000'],
      ['', '', 'Consultancy', '70,000'],
      ['', '', 'Repairs', '150,000'],
      ['', '', 'Others', '70,000'],
      ['', '', 'Air conditioning expenses', '220,000'],
      ['', '', 'Fire insurance', '60,000'],
      ['', '', 'Income tax', '900,000'],
      ['', '', 'Drawings', '180,000'],
      ['', '', 'Balance c/d', '2,900,000'],
      ['Total', '36,930,000', 'Total', '36,930,000'],
    ]}},
    {'table': {'head': ['', '31/12/2023 (GH¢)', '31/12/2024 (GH¢)'], 'align': 'lrr', 'rows': [
      ['Receivables — bulk sales', '490,000', '430,000'],
      ['Payables — goods purchased', '2,900,000', '3,195,000'],
      ['Rent owing', '80,000', '30,000'],
      ['Electricity owing', '25,000', '65,000'],
      ['Telephone owing', '45,000', '—'],
      ['Consultancy fees owing', '40,000', '40,000'],
      ['Inventories in trade', '2,050,000', '1,875,000'],
      ['Furniture and fittings', '—', '540,000'],
    ]}},
    {'p': 'Rates and air-conditioning expenses included GH¢55,000 and GH¢20,000 respectively, '
          'relating to Damask\'s **private residence**.'},
    {'h4': 'Step 1 — the statement of affairs, both dates'},
    {'stmt': {'t': 'Statement of affairs', 'rows': [
      '', '31/12/2023 (GH¢)', '31/12/2024 (GH¢)',
      ['Furniture & fittings', '—', '540,000'],
      ['Trade receivables', '490,000', '430,000'],
      ['Inventories', '2,050,000', '1,875,000'],
      ['Cash at bank', '2,000,000', '2,900,000'],
      ['Total assets', '4,540,000', '5,745,000', '@t'],
      ['Trade payables', '(2,900,000)', '(3,195,000)'],
      ['Rent owing', '(80,000)', '(30,000)'],
      ['Electricity owing', '(25,000)', '(65,000)'],
      ['Telephone owing', '(45,000)', '—'],
      ['Consultancy fees owing', '(40,000)', '(40,000)'],
      ['Capital', '1,450,000', '2,415,000', '@tt'],
    ]}},
    {'h4': 'Step 2 — deriving sales (the "horizontal" missing-figure format)'},
    {'p': 'Because takings are banked **net** of expenses paid from the till, the sales figure has '
          'to be grossed back up before it means anything. The source presents this derivation '
          'horizontally rather than as a T-account — an equally valid layout, and worth knowing '
          'both ways:'},
    {'stmt': {'t': 'Cash sales', 'rows': [
      ['Lodgements — shop takings', 30100000],
      ['Add: proprietor\'s drawings (GH¢10,000 × 52 weeks)', 520000],
      ['Add: expenses paid out of takings (1,200,000 + 220,000 + 75,000 + 35,000 + 20,000)', 1550000],
      ['Cash sales', 32170000, '@tt'],
    ]}},
    {'stmt': {'t': 'Credit (bulk) sales', 'rows': [
      ['Bulk sales account (cheques)', 4800000],
      ['Add: closing receivables', 430000],
      ['Less: opening receivables', -490000],
      ['Credit sales', 4740000, '@tt'],
    ]}},
    {'stmt': {'t': 'Total sales', 'rows': [
      ['Cash sales', 32170000], ['Credit sales', 4740000],
      ['Total sales / revenue', 36910000, '@tt'],
    ]}},
    {'h4': 'Step 3 — deriving purchases'},
    {'stmt': {'rows': [
      ['Payments for goods supplied (bank)', 30830000],
      ['Add: closing trade payables', 3195000],
      ['', 34025000, '@t'],
      ['Less: opening trade payables', -2900000],
      ['Credit purchases', 31125000, '@t'],
      ['Add: cash purchases (from the till)', 220000],
      ['Total purchases', 31345000, '@tt'],
    ]}},
    {'h4': 'The statement of profit or loss'},
    {'stmt': {'t': 'Damask — Statement of profit or loss for the year ended 31 December 2024 (GH¢)',
     'rows': [
      ['Sales / revenue', '', 36910000],
      'Less cost of sales',
      ['Opening inventories', 2050000, ''],
      ['Purchases', 31345000, ''],
      ['Carriage inwards', 35000, ''],
      ['', 33430000, ''],
      ['Less closing inventories', -1875000, ''],
      ['', -31555000, ''],
      ['Gross profit', '', 5355000],
      ['Add: interest on treasury bills', '', 30000],
      ['', '', 5385000, '@t'],
      'Less expenses',
      ['Staff wages', 1200000, ''],
      ['Rates (400,000 − 55,000 private)', 345000, ''],
      ['Rent (W1)', 350000, ''],
      ['Telephone & electricity (W2)', 145000, ''],
      ['Consultancy fees (W3)', 70000, ''],
      ['Repairs', 150000, ''],
      ['Air conditioning (220,000 − 20,000 private)', 200000, ''],
      ['Fire insurance', 60000, ''],
      ['Cleaning', 75000, ''],
      ['Other expenses', 90000, ''],
      ['Depreciation', 60000, ''],
      ['', 2745000, ''],
      ['Net profit before tax', '', 2640000],
      ['Income tax', '', -900000],
      ['Net profit for the year', '', 1740000, '@tt'],
    ]}},
    {'warn': 'The two private-use adjustments are the whole point of this illustration, and the '
             'thing candidates get wrong most often in questions built like this one: **rates** '
             'of GH¢400,000 were paid by cheque, but GH¢55,000 of that related to Damask\'s own '
             'residence, so only GH¢345,000 is a genuine business expense — the GH¢55,000 is '
             'drawings. **Air-conditioning** expenses of GH¢220,000 were paid, but GH¢20,000 '
             'related to the residence, leaving GH¢200,000 as the real business expense — again, '
             'the GH¢20,000 is drawings. In both cases, the cheque was written from the *business* '
             'bank account, but that tells you nothing about whether the cost was a *business* '
             'expense — the test is always what the money was actually spent on, exactly as the '
             'business entity concept (Chapter 1 §1.6) requires.'},
    {'h4': 'Workings W1–W3 — the three expense control accounts'},
    {'tacc': {'t': 'W1 — Rent expense control account (GH¢)', 'dr': [
        ['Bank', 400000], ['', 400000, '@tot'], ['Balance b/d', 30000]],
      'cr': [['Balance b/d', 80000], ['Profit or loss', 350000], ['Balance c/d', 30000],
             ['', 460000, '@tot']]}},
    {'note': 'Cash paid GH¢400,000, opening owing GH¢80,000, closing owing GH¢30,000: charge to '
             'profit or loss $= 400{,}000 + 80{,}000 - 30{,}000 = ₦350{,}000$ — exactly the '
             'Chapter 4 §4.1 formula for an accrued expense.'},
    {'tacc': {'t': 'W2 — Telephone and electricity control account (GH¢)', 'dr': [
        ['Bank', 150000], ['', 150000, '@tot'], ['Balance b/d', 65000]],
      'cr': [['Balance b/d', 70000], ['Profit or loss', 145000], ['Balance c/d', 65000],
             ['', 215000, '@tot']]}},
    {'tacc': {'t': 'W3 — Consultancy fees control account (GH¢)', 'dr': [
        ['Bank', 70000], ['Balance c/d', 40000], ['', 110000, '@tot']],
      'cr': [['Balance b/d', 40000], ['Profit or loss', 70000], ['', 110000, '@tot']]}},
    {'h4': 'W4 — Drawings, in full'},
    {'stmt': {'t': 'Drawings for the year (GH¢)', 'rows': [
      ['Bank — cheque drawings', 180000],
      ['Cash — GH¢10,000 × 52 weeks', 520000],
      ['Rates — private portion', 55000],
      ['Air conditioning — private portion', 20000],
      ['Total drawings', 775000, '@tt'],
    ]}},
    {'h4': 'The statement of financial position'},
    {'stmt': {'t': 'Damask — Statement of financial position as at 31 December 2024 (GH¢)',
     'rows': [
      'Non-current assets',
      ['Furniture and fittings', 600000, ''],
      ['Less depreciation', -60000, ''],
      ['', '', 540000],
      '@gap',
      'Current assets',
      ['Inventories', 1875000, ''],
      ['Trade receivables', 430000, ''],
      ['Bank', 2900000, ''],
      ['', '', 5205000],
      '@gap',
      'Current liabilities',
      ['Trade payables', 3195000, ''],
      ['Rent owing (W1)', 30000, ''],
      ['Electricity owing (W2)', 65000, ''],
      ['Accountancy/consultancy fee owing (W3)', 40000, ''],
      ['', '', -3330000],
      ['Net current assets', '', 1875000, '@t'],
      ['Net assets', '', 2415000, '@tt'],
      '@gap',
      'Financed by',
      ['Capital at 1/1/24', '', 1450000],
      ['Net profit', '', 1740000],
      ['', '', 3190000, '@t'],
      ['Less drawings (W4)', '', -775000],
      ['Capital at 31/12/24', '', 2415000, '@tt'],
    ]}},
  ]},

  {'n': '6.6', 't': 'Margin and mark-up', 'b': [
    {'p': 'This study text\'s own two worked illustrations happen to give purchases and closing '
          'inventory directly, so neither one needs a margin or mark-up conversion to solve. Many '
          'incomplete-records questions are **not** so generous: they give a gross profit margin '
          'or a cost mark-up instead, and expect you to derive cost of sales, or closing '
          'inventory, or even sales itself, from it. This is where most marks are lost in this '
          'topic generally, and the fix is a single habit: **write down what the base is** before '
          'you compute anything.'},
    {'table': {'head': ['', 'Mark-up', 'Margin'], 'align': 'lll', 'rows': [
      ['Percentage of', 'Cost of sales', 'Sales'],
      ['If sales = 100', 'Cost + mark-up on cost', 'Gross profit is x% of the 100'],
      ['Convert to the other',
       '$\\text{Margin} = \\dfrac{m}{1+m}$', '$\\text{Mark-up} = \\dfrac{g}{1-g}$'],
    ]}},
    {'table': {'cap': 'Common conversions', 'head': ['Mark-up on cost', 'Equivalent margin on sales'],
     'align': 'll', 'rows': [
      ['25% (1/4)', '20% (1/5)'], ['33⅓% (1/3)', '25% (1/4)'], ['50% (1/2)', '33⅓% (1/3)'],
      ['100%', '50%'], ['20% (1/5)', '16⅔% (1/6)'],
    ], 'note': 'The pattern: a mark-up of 1/n is a margin of 1/(n+1).'}},
    {'eg': {'t': 'Using mark-up to find gross profit', 'q': [
      {'p': 'Sales for the year were ₦4,600,000 and closing inventory ₦600,000. The business '
            'maintains a mark-up of 33⅓% on cost. Compute the gross profit and the goods '
            'available for sale.'}],
      'a': [
      {'p': 'A mark-up of 33⅓% means cost is 3 parts and profit 1 part, so sales are 4 parts. '
            'Gross profit is therefore $\\tfrac14$ of sales — a **margin of 25%**:'},
      {'tex': '\\text{Margin} = \\frac{m}{1+m} = \\frac{1/3}{1+1/3} = \\frac{1/3}{4/3} '
              '= \\frac{1}{4} = 25\\%'},
      {'tex': '\\text{Gross profit} = 0.25 \\times 4{,}600{,}000 = ₦1{,}150{,}000'},
      {'p': 'Cost of sales is then $4{,}600{,}000 - 1{,}150{,}000 = ₦3{,}450{,}000$, and:'},
      {'tex': '\\text{Goods available for sale} = \\text{Cost of sales} + \\text{Closing '
              'inventory} = 3{,}450{,}000 + 600{,}000 = ₦4{,}050{,}000'},
      {'warn': 'Applying 33⅓% to **sales** instead of cost gives ₦1,533,333 — wrong, and the '
               'error then propagates through every later figure. Whenever a question says '
               '"mark-up", the base is cost; "margin" means the base is sales.'}]}},
  ]},

  {'n': '6.7', 't': 'Finding a cash defalcation', 'b': [
    {'p': 'Where a trader banks only part of the takings and pays expenses from the till — exactly '
          'the situation in Illustration 6.3 above — the cash column of the summary can reveal '
          'either the cash sales figure, or, more interestingly, money that has gone missing '
          'entirely. This did not arise in Damask\'s figures because everything reconciled; the '
          'next worked example shows what happens when it does not.'},
    {'eg': {'t': 'Finding a defalcation', 'q': [
      {'p': 'Cash at the start of the year was ₦85,000 and at the end ₦62,000. Cash sales banked '
            'were ₦6,400,000; wages of ₦780,000 and sundry expenses of ₦215,000 were paid from '
            'the till, and the owner took ₦25,000 a week for 52 weeks. Total sales derived from '
            'the receivables account and the mark-up were ₦8,900,000, of which credit sales were '
            '₦1,150,000. Has any cash gone missing?'}],
      'a': [
      {'p': 'Cash sales should be $8{,}900{,}000 - 1{,}150{,}000 = ₦7{,}750{,}000$.'},
      {'tacc': {'t': 'Cash account (till)', 'dr': [
          ['Balance b/d', 85000], ['Cash sales', 7750000], ['', 7835000, '@tot']],
        'cr': [['Banked', 6400000], ['Wages', 780000], ['Sundry expenses', 215000],
               ['Drawings (25,000 × 52)', 1300000], ['Balance c/d', 62000],
               ['', 8757000, '@tot']]}},
      {'p': 'The credit side exceeds the debit side by $8{,}757{,}000 - 7{,}835{,}000 = '
            '₦922{,}000$. Since the account must balance, that amount of cash has been paid out '
            'or removed without record — a **cash shortage or defalcation of ₦922,000**.'},
      {'note': 'Present it as an expense in the statement of profit or loss, described as cash '
               'shortage, and say in your answer that it requires investigation. Examiners award '
               'the mark for identifying it, not for accusing anyone.'}]}},
  ]},

  {'n': '6.8', 't': 'The limitations of incomplete records', 'b': [
    {'ul': [
      'No trial balance can be extracted, so arithmetic accuracy cannot be proved.',
      'Errors and fraud are hard to detect, since there is nothing to reconcile against.',
      'Figures rest on estimates and on the proprietor\'s memory.',
      'The statements are unlikely to be acceptable to a bank or to the tax authorities.',
      'Comparison between years is unreliable if the estimating basis changes.',
    ]},
    {'key': 'Number your workings W1, W2, W3 and reference them from the face of the statements. '
            'A correct figure with no visible working earns fewer marks than a wrong figure '
            'reached by a visibly correct method — and, as Illustration 6.2 shows, cross-checking '
            'the capital-comparison profit against the full statement of profit or loss is a '
            'free, built-in way to catch your own arithmetic errors before you submit.'},
    {'note': 'It is imperative for readers to note that, as with all accounting topics, frequent '
             'practice of incomplete-records questions is essential for the skill and confidence '
             'required.'},
  ]},

  {'n': '6.9', 't': 'Further reading', 'b': [
    {'note': '[AccountingCoach\'s course on preparing financial statements from incomplete '
             'records](https://www.accountingcoach.com/single-entry-accounting-system/explanation) '
             'covers the same statement-of-affairs and cash-summary technique with additional '
             'practice examples. [IAS 2 Inventories](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/) '
             'is the standard behind the closing-inventory figures used throughout this chapter\'s '
             'illustrations. If you want to see how a real accountancy firm frames the same '
             'engagement — a client with "no proper books" needing a full set of accounts '
             'reconstructed for the first time — search for "incomplete records engagement" on '
             'the [ICAN website](https://icanig.org), which periodically publishes guidance and '
             'past questions on exactly this scenario.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Profit by capital comparison',
   'tex': '\\text{Profit} = \\Delta\\text{Capital} + \\text{Drawings} - \\text{Additional capital}'},
  {'lb': 'Mark-up to margin', 'tex': '\\text{Margin} = \\frac{\\text{mark-up}}{1 + \\text{mark-up}}'},
  {'lb': 'Margin to mark-up', 'tex': '\\text{Mark-up} = \\frac{\\text{margin}}{1 - \\text{margin}}'},
  {'lb': 'Cost of sales',
   'tex': '\\text{COS} = \\text{Opening inventory} + \\text{Purchases} - \\text{Closing inventory}'},
  {'lb': 'Goods available for sale',
   'tex': '\\text{GAFS} = \\text{Cost of sales} + \\text{Closing inventory} '
          '= \\text{Opening inventory} + \\text{Purchases}'},
 ],
 'focus':
   'One of the two or three most heavily examined Section B topics, worth 12–15 marks whenever it '
   'appears, and it appears often. The examiner nearly always plants a margin/mark-up conversion, '
   'a missing cash figure, and — as Illustration 6.3 shows — a private-use expense hidden inside '
   'a business bank payment. Section A tests the conversions as one-liners. If you drill only one '
   'thing from this chapter, drill converting between mark-up and margin until it is instant; if '
   'you drill a second thing, drill spotting a private expense paid from the business account.',
 'errors': [
   'Applying a mark-up percentage to sales, or a margin percentage to cost.',
   'Forgetting to add drawings back when computing profit by capital comparison.',
   'Treating capital introduced as profit.',
   'Including cash sales in the receivables control account when deriving credit sales.',
   'Omitting accruals and prepayments from the statements of affairs, which distorts both '
   'capital figures and therefore the profit.',
   'Treating a private expense paid from the business bank account (rates, insurance, rent on '
   'the owner\'s own residence) as a business expense instead of drawings.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A business marks up goods by 25% on cost. Sales for the year were ₦3,000,000. Gross '
         'profit is',
    'o': ['₦750,000', '₦600,000', '₦500,000', '₦375,000', '₦800,000'],
    'a': 1,
    'w': 'A mark-up of 25% (1/4 on cost) is a margin of 1/5, or 20%, on sales. Take 20% of sales.',
    'calc': '\\text{Margin} = \\frac{0.25}{1.25} = 0.20; \\quad 0.20 \\times 3{,}000{,}000 '
            '= 600{,}000',
    'src': 'Chapter 6.6'},
   {'q': 'Opening capital ₦2,400,000; closing capital ₦2,900,000; drawings ₦600,000; capital '
         'introduced ₦250,000. Profit for the year is',
    'o': ['₦500,000', '₦850,000', '₦1,100,000', '₦250,000', '₦350,000'],
    'a': 1,
    'w': 'Add back drawings and remove the capital introduced from the movement in capital.',
    'calc': '(2{,}900{,}000 - 2{,}400{,}000) + 600{,}000 - 250{,}000 = 850{,}000',
    'src': 'Chapter 6.2'},
   {'q': 'Opening receivables ₦520,000; closing receivables ₦610,000; cash received from '
         'customers ₦4,300,000; discounts allowed ₦75,000; bad debts written off ₦40,000. Credit '
         'sales were',
    'o': ['₦4,210,000', '₦4,390,000', '₦4,505,000', '₦4,935,000', '₦4,300,000'],
    'a': 2,
    'w': 'Build the receivables control account and take credit sales as the balancing figure.',
    'calc': '610{,}000 + 4{,}300{,}000 + 75{,}000 + 40{,}000 - 520{,}000 = 4{,}505{,}000',
    'src': 'Chapter 6.3'},
   {'q': 'A trader operates on a gross profit margin of 33⅓%. If cost of sales was ₦2,400,000, '
         'sales were',
    'o': ['₦3,200,000', '₦3,600,000', '₦3,000,000', '₦2,800,000', '₦7,200,000'],
    'a': 1,
    'w': 'A margin of 1/3 means cost is 2/3 of sales, so sales are cost × 3/2.',
    'calc': '\\text{Sales} = \\frac{2{,}400{,}000}{1 - \\frac13} = 2{,}400{,}000 \\times '
            '\\frac{3}{2} = 3{,}600{,}000',
    'src': 'Chapter 6.6'},
   {'q': 'A statement of affairs is prepared in order to ascertain',
    'o': ['the profit for the period', 'the capital at a particular date',
          'the cash balance at a date', 'the credit sales for the period',
          'the value of closing inventory'],
    'a': 1,
    'w': 'A statement of affairs lists assets and liabilities at a date; the balancing figure is '
         'the capital. Profit then comes from comparing two such capitals.',
    'src': 'Chapter 6.3'},
   {'q': 'Which of the following is NOT a limitation of incomplete records?',
    'o': ['No trial balance can be extracted',
          'Fraud is difficult to detect',
          'Figures often rest on estimates',
          'The records are cheaper and quicker to maintain',
          'The statements may be unacceptable to a lender'],
    'a': 3,
    'w': 'Cheapness is the reason small traders keep incomplete records — it is an advantage, '
         'not a limitation.',
    'src': 'Chapter 6.8'},
  ],
  'theory': [
   {'q': 'Explain the capital comparison method of ascertaining profit from incomplete records, '
         'and state THREE limitations of accounts prepared from such records.',
    'marks': 8,
    'a': [
      {'p': '**The method.** Where no ledger exists, profit is measured by the change in the '
            'owner\'s stake over the period, adjusted for transactions with the owner:'},
      {'tex': '\\text{Profit} = (\\text{Closing capital} - \\text{Opening capital}) + '
              '\\text{Drawings} - \\text{Capital introduced}'},
      {'steps': [
        'Prepare a statement of affairs at the beginning of the period: assets less liabilities '
        'gives opening capital.',
        'Prepare a statement of affairs at the end: assets less liabilities gives closing capital.',
        'Add back drawings, because they reduced capital without being a cost of trading.',
        'Deduct capital introduced, because it increased capital without being profit.']},
      {'p': 'The logic is financial capital maintenance: the business is better off by the amount '
            'its net assets grew, once the owner\'s own contributions and withdrawals are stripped out.'},
      {'h4': 'Limitations'},
      {'ol': [
        'No trial balance can be extracted, so the arithmetical accuracy of the records cannot be '
        'demonstrated.',
        'Errors, omissions and fraud are difficult to detect because there is no independent '
        'record to reconcile against.',
        'Many figures rest on estimates or on the proprietor\'s recollection, so the profit is '
        'approximate.',
        'The method gives a profit figure only — it produces no analysis of revenue and expenses, '
        'so it cannot show *why* profit moved.',
        'Such statements are often unacceptable to lenders and revenue authorities.']}],
    'src': 'Chapter 6.2'},
  ]},
}
