CH = {
 'n': 13,
 't': 'Cash Book, Transcripts and Subsidiary Accounts',
 'brief': 'The treasury cash book and the distinction between above-the-line and below-the-line '
          'transactions, the subsidiary accounts for advances, deposits and remittances, the '
          'monthly transcript rendered by a sub-accounting officer, and bank reconciliation.',
 'outcomes': [
   'Distinguish above-the-line from below-the-line transactions',
   'Record transactions in a treasury cash book and extract the balance',
   'Explain and account for advances, deposits and remittances',
   'State the contents of a monthly transcript and its supporting schedules',
   'Prepare a bank reconciliation statement for a government office',
 ],
 'secs': [
  {'n': '13.1', 't': 'Above the line and below the line', 'b': [
    {'p': 'Every transaction passing through a government cash book is either **above the line** '
          'or **below the line**. The "line" is the boundary of the revenue and expenditure '
          'account: transactions above it change the surplus or deficit for the year, and '
          'transactions below it do not.'},
    {'table': {'align': 'lll', 'head': ['', 'Above the line', 'Below the line'], 'rows': [
      ['Nature', 'Revenue and expenditure of the year',
       'Movements on personal and impersonal accounts that create or discharge an asset or a '
       'liability'],
      ['Effect on the accounts',
       'Enters the Statement of Cash Receipts and Payments as revenue or expenditure',
       'Enters the Statement of Assets and Liabilities; does not affect revenue or expenditure'],
      ['Examples', 'Taxes, fees, fines, rents; personnel cost, overhead cost, capital '
       'expenditure', 'Advances, deposits, remittances, investments, unallocated stores'],
      ['Recorded in', 'Revenue and expenditure heads and subheads',
       'Subsidiary (below-the-line) accounts'],
    ]}},
    {'key': 'The test is whether the transaction is **the government\'s own income or expense**, '
            'or merely **money held for or owed by someone else**. A deposit received as '
            'security for a contract is not revenue: it must be returned. An advance to an '
            'officer is not expenditure: it must be repaid.'},
  ]},

  {'n': '13.2', 't': 'The subsidiary accounts', 'b': [
    {'table': {'align': 'lll',
      'head': ['Account', 'Nature', 'Balance represents'], 'rows': [
      ['**Advances**',
       'Money paid out that will be repaid or accounted for — salary advances, touring '
       'advances, advances to contractors, imprest advances',
       'A **debit** balance: an **asset**, being amounts recoverable'],
      ['**Deposits**',
       'Money received that will be repaid or applied for a specified purpose — tender and '
       'performance deposits, retention money, court deposits, unclaimed salaries',
       'A **credit** balance: a **liability**, being amounts repayable'],
      ['**Remittances**',
       'Transfers of funds between government offices — from the Treasury to a sub-treasury '
       'and back, or between sub-treasuries',
       'A **contra** item that must clear on consolidation; a balance means a transfer is in '
       'transit or unrecorded at one end'],
    ]}},
    {'h4': 'Advances'},
    {'ul': [
      'An advance may be granted only where the Financial Regulations authorise it, and within '
      'the limits prescribed.',
      'Every advance must be **recorded in the Advances Ledger** in the name of the officer or '
      'body concerned.',
      'It must be **retired or repaid** within the period stipulated — a touring advance within '
      'a set number of days of return, a salary advance by monthly deduction.',
      'An advance not retired when due is recovered from salary, and an officer who fails to '
      'retire an advance may not be granted another.',
      'At the year end, outstanding advances appear as an **asset** in the Statement of Assets '
      'and Liabilities, and irrecoverable advances are written off only with the authority '
      'competent to approve the amount.',
    ]},
    {'h4': 'Deposits'},
    {'ul': [
      'Deposits are recorded in the **Deposits Ledger** in the name of the depositor.',
      'They may be applied only for the purpose for which they were received, and are otherwise '
      'refundable.',
      'A deposit **unclaimed for the period prescribed** in the Financial Regulations is '
      'transferred to revenue, but remains repayable if the depositor subsequently establishes '
      'the claim.',
      'Deposits outstanding at the year end appear as a **liability**.',
    ]},
    {'warn': 'A deposit is **never** treated as revenue merely because the money is in hand, and '
             'an advance is never treated as expenditure merely because the money has gone out. '
             'Doing so overstates both the revenue and the expenditure of the year and '
             'misstates the assets and liabilities.'},
  ]},

  {'n': '13.3', 't': 'The treasury cash book', 'b': [
    {'p': 'The cash book is the book of prime entry for all receipts and payments at a treasury '
          'or sub-treasury. It is columnar, with separate columns for cash and bank on each '
          'side, and analysis columns for revenue heads, expenditure heads and each of the '
          'below-the-line accounts. It is **balanced daily** and the balance agreed with the '
          'cash actually held.'},
    {'eg': {'t': 'Summarising a sub-treasury cash book', 'q': [
      {'p': 'The following transactions passed through the cash book of the Ilorin Sub-Treasury '
            'during the month of March 2026:'},
      {'table': {'align': 'lr', 'head': ['', '₦'], 'rows': [
        ['Balance at 1 March — cash on hand', '150,000'],
        ['Balance at 1 March — bank', '4,250,000'],
        ['Fees collected', '1,800,000'],
        ['Fines collected', '420,000'],
        ['Rents collected', '630,000'],
        ['Deposits received from contractors', '350,000'],
        ['Advances repaid by officers', '180,000'],
        ['Remittances received from Headquarters Treasury', '12,000,000'],
        ['Personnel cost paid', '8,400,000'],
        ['Overhead cost paid', '2,650,000'],
        ['Advances granted to officers', '500,000'],
        ['Deposits refunded', '120,000'],
        ['Remittances to Headquarters Treasury', '2,850,000'],
      ]}},
      {'p': 'Cash on hand at 31 March was ₦150,000. Prepare a summary of the cash book '
            'distinguishing above-the-line from below-the-line items, and determine the closing '
            'bank balance.'}],
      'a': [
      {'h4': 'Summary of receipts and payments'},
      {'stmt': {'t': 'Cash book summary — March 2026', 'rows': [
        ['Balance brought forward (cash 150,000 + bank 4,250,000)', 4400000],
        ['**Receipts**@t', None],
        ['Fees', 1800000],
        ['Fines', 420000],
        ['Rents', 630000],
        ['Deposits received', 350000],
        ['Advances repaid', 180000],
        ['Remittances from Headquarters', 12000000],
        ['Total receipts@sub', 15380000],
        ['**Payments**@t', None],
        ['Personnel cost', -8400000],
        ['Overhead cost', -2650000],
        ['Advances granted', -500000],
        ['Deposits refunded', -120000],
        ['Remittances to Headquarters', -2850000],
        ['Total payments@sub', -14520000],
        ['Balance carried forward@tot', 5260000],
      ]}},
      {'p': 'Cash on hand at 31 March is ₦150,000, so the **closing bank balance** is '
            '$5{,}260{,}000 - 150{,}000 = ₦5{,}110{,}000$.'},
      {'h4': 'Classification'},
      {'table': {'align': 'lrr', 'head': ['', 'Receipts (₦)', 'Payments (₦)'], 'rows': [
        ['**Above the line**', '', ''],
        ['Revenue — fees, fines and rents', '2,850,000', ''],
        ['Expenditure — personnel and overhead cost', '', '11,050,000'],
        ['**Below the line**', '', ''],
        ['Advances', '180,000', '500,000'],
        ['Deposits', '350,000', '120,000'],
        ['Remittances', '12,000,000', '2,850,000'],
        ['**Total**', '**15,380,000**', '**14,520,000**'],
      ]}},
      {'p': 'The net movements below the line for the month are: advances **₦320,000 net '
            'granted** (an increase in the asset); deposits **₦230,000 net received** (an '
            'increase in the liability); and remittances **₦9,150,000 net received** from '
            'headquarters.'},
      {'note': 'A useful check: the net increase in cash of ₦860,000 must equal revenue less '
               'expenditure, adjusted for the below-the-line movements: '
               '$2{,}850{,}000 - 11{,}050{,}000 - 320{,}000 + 230{,}000 + 9{,}150{,}000 '
               '= ₦860{,}000$. ✓'}]}},
  ]},

  {'n': '13.4', 't': 'The monthly transcript', 'b': [
    {'def': {'t': 'Transcript',
             'd': 'The monthly return rendered by a sub-accounting officer to the '
                  'Accountant-General (or by a self-accounting unit to its headquarters), '
                  'consisting of a copy of the cash book for the month together with all '
                  'supporting schedules and documents, by which the transactions of the '
                  'outstation are brought into the central accounts.'}},
    {'h4': 'Contents of a transcript'},
    {'ol': [
      'The **cash book** for the month, cast, balanced and certified.',
      'A **schedule of revenue collected**, analysed by head and subhead, supported by the '
      'receipt vouchers and treasury receipts.',
      'A **schedule of expenditure**, analysed by head and subhead, supported by the paid '
      'payment vouchers in serial order.',
      'A **schedule of advances** — opening balance, advances granted, advances repaid, closing '
      'balance, with the names of the officers concerned.',
      'A **schedule of deposits** — opening balance, deposits received, deposits refunded, '
      'closing balance, with the names of the depositors.',
      'A **schedule of remittances** in and out, with the numbers of the transfer advices.',
      'A **bank reconciliation statement** with the bank statement and, where required, a bank '
      'certificate of balance.',
      'A **certificate of cash and stamps** on hand at the close of the month.',
      'A statement of **unpaid and outstanding vouchers**.',
      'The **certificate of the sub-accounting officer** that the transcript is correct and '
      'complete.',
    ]},
    {'h4': 'Purposes of the transcript'},
    {'ul': [
      'To bring the outstation\'s transactions into the **central accounts** of the Federation '
      'or of the ministry.',
      'To enable the Treasury to **check and verify** the transactions and the balances of the '
      'outstation.',
      'To provide the basis of the **consolidated financial statements**.',
      'To provide **control** over sub-accounting officers, since the transcript must be '
      'rendered by a fixed date each month and delay is a disciplinary matter.',
      'To supply the **audit evidence** on which the Auditor-General relies for the outstation.',
    ]},
    {'note': 'The transcript is the mechanism by which the accounts of a geographically '
             'dispersed government are consolidated. Where transcripts are rendered late — a '
             'perennial complaint in the Auditor-General\'s reports — the annual accounts of '
             'the Federation cannot be closed on time, which is why the Financial Regulations '
             'treat late rendition as a serious offence.'},
  ]},

  {'n': '13.5', 't': 'Bank reconciliation', 'b': [
    {'p': 'The balance in the cash book will rarely agree with the balance on the bank statement '
          'at the same date. The reconciliation identifies the reasons and establishes the '
          'correct balance.'},
    {'table': {'align': 'll', 'head': ['Cause of difference', 'Treatment'], 'rows': [
      ['Cheques or mandates issued but not yet presented',
       'Deduct from the bank statement balance'],
      ['Lodgements made but not yet credited by the bank',
       'Add to the bank statement balance'],
      ['Bank charges, commission and interest debited by the bank',
       'Deduct in the **adjusted cash book**'],
      ['Interest or direct credits received by the bank',
       'Add in the **adjusted cash book**'],
      ['Dishonoured cheques', 'Deduct in the adjusted cash book'],
      ['Errors in the cash book', 'Correct in the adjusted cash book'],
      ['Errors by the bank', 'Adjust against the bank statement balance'],
    ]}},
    {'eg': {'t': 'Bank reconciliation for the sub-treasury', 'q': [
      {'p': 'Continuing the Ilorin example, the cash book bank balance at 31 March 2026 was '
            '₦5,110,000 and the bank statement showed ₦5,640,000. Investigation revealed: '
            'mandates issued but not presented ₦680,000; lodgements not yet credited ₦140,000; '
            'bank charges not recorded in the cash book ₦18,000; and interest credited by the '
            'bank and not recorded ₦8,000. Prepare the adjusted cash book and the bank '
            'reconciliation statement.'}],
      'a': [
      {'stmt': {'t': 'Adjusted cash book (bank column)', 'rows': [
        ['Balance per cash book', 5110000],
        ['Add: Interest credited by the bank', 8000],
        ['Less: Bank charges not recorded', -18000],
        ['Adjusted cash book balance@tot', 5100000],
      ]}},
      {'stmt': {'t': 'Bank reconciliation statement as at 31 March 2026', 'rows': [
        ['Balance per bank statement', 5640000],
        ['Less: Mandates issued but not presented', -680000],
        ['Add: Lodgements not yet credited', 140000],
        ['Adjusted cash book balance@tot', 5100000],
      ]}},
      {'p': 'The two statements agree at **₦5,100,000**, which is the figure to be carried into '
            'the transcript and into the Statement of Assets and Liabilities. The unadjusted '
            'cash book figure of ₦5,110,000 is not the correct balance, because the bank '
            'charges and interest were genuine transactions of the month that the office had '
            'not yet recorded.'},
      {'key': 'Two rules govern every reconciliation. **Items the office knows about but the '
              'bank has not yet processed** — unpresented mandates and uncredited lodgements — '
              'are adjusted against the **bank statement**. **Items the bank has processed but '
              'the office has not yet recorded** — charges, interest, direct credits, '
              'dishonoured cheques — are adjusted in the **cash book**, because they are real '
              'entries that were simply omitted.'}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Closing cash balance',
   'tex': '\\text{Opening} + \\text{Receipts} - \\text{Payments}'},
  {'lb': 'Net advance movement',
   'tex': '\\text{Advances granted} - \\text{Advances repaid}'},
  {'lb': 'Net deposit movement',
   'tex': '\\text{Deposits received} - \\text{Deposits refunded}'},
  {'lb': 'Adjusted cash book',
   'tex': '\\text{Cash book} + \\text{credits omitted} - \\text{debits omitted}'},
  {'lb': 'Reconciliation',
   'tex': '\\text{Bank statement} - \\text{unpresented} + \\text{uncredited} '
          '= \\text{adjusted cash book}'},
 ],
 'focus':
   'One of the two or three most reliable Section B preparation questions in the paper. The '
   'usual form is a list of transactions from which you must prepare a cash book summary or a '
   'transcript, classify items above and below the line, and produce a bank reconciliation. '
   'Marks are given line by line, so present the work in proper statement form with headings '
   'and a total, even where you are unsure of one or two classifications.',
 'errors': [
   'Treating deposits received as revenue, or advances granted as expenditure.',
   'Adjusting bank charges against the bank statement instead of in the cash book.',
   'Netting remittances in and out instead of showing both, which loses the audit trail.',
   'Omitting the certificate of cash and stamps and the bank reconciliation from the contents '
   'of a transcript.',
   'Failing to deduct cash on hand when deriving the bank balance from a combined cash book '
   'total.',
   'Leaving the reconciliation to end at the unadjusted cash book figure rather than the '
   'adjusted one.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Which of the following is a below-the-line transaction?',
    'o': ['Payment of salaries', 'Receipt of a contractor\'s performance deposit',
          'Collection of market fees', 'Payment for stationery consumed',
          'Collection of tenement rates'],
    'a': 1,
    'w': 'A deposit is repayable, so it creates a liability rather than revenue and does not '
         'affect the surplus or deficit for the year.',
    'src': 'Chapter 13.1'},
   {'q': 'An advance granted to an officer and outstanding at the year end appears in the '
         'financial statements as',
    'o': ['expenditure', 'an asset', 'a liability', 'revenue', 'a contingent liability'],
    'a': 1,
    'w': 'The advance is recoverable, so it is an asset until it is retired or repaid.',
    'src': 'Chapter 13.2'},
   {'q': 'In a bank reconciliation, bank charges not recorded in the cash book are',
    'o': ['added to the bank statement balance', 'deducted in the adjusted cash book',
          'deducted from the bank statement balance', 'added in the adjusted cash book',
          'ignored'],
    'a': 1,
    'w': 'The bank has already processed the charge; it is the office that has not recorded it, '
         'so the cash book must be adjusted.',
    'src': 'Chapter 13.5'},
   {'q': 'The monthly return by which a sub-accounting officer brings his transactions into the '
         'central accounts is called a',
    'o': ['warrant', 'transcript', 'voucher', 'mandate', 'schedule of losses'],
    'a': 1,
    'w': 'The transcript comprises the cash book for the month together with all supporting '
         'schedules and certificates.',
    'src': 'Chapter 13.4'},
   {'q': 'A cash book shows a bank balance of ₦2,400,000. Unpresented cheques are ₦350,000 and '
         'uncredited lodgements ₦120,000. There are no other differences. The bank statement '
         'balance is',
    'o': ['₦2,170,000', '₦2,630,000', '₦2,870,000', '₦1,930,000', '₦2,400,000'],
    'a': 1,
    'w': 'Work backwards: the bank statement balance less unpresented cheques plus uncredited '
         'lodgements equals the cash book balance.',
    'calc': '\\text{Bank} = 2{,}400{,}000 + 350{,}000 - 120{,}000 = ₦2{,}630{,}000',
    'src': 'Chapter 13.5'},
   {'q': 'Remittances between government offices are recorded',
    'o': ['as revenue at the receiving office and expenditure at the sending office',
          'below the line at both offices, clearing on consolidation',
          'as expenditure at both offices', 'only at the Headquarters Treasury',
          'in the Statement of Cash Receipts and Payments as revenue'],
    'a': 1,
    'w': 'A remittance is an internal transfer of the government\'s own money. Treating it as '
         'revenue and expenditure would inflate both figures on consolidation.',
    'src': 'Chapter 13.2'},
  ],
  'theory': [
   {'q': 'The following transactions passed through the cash book of the Bauchi Sub-Treasury '
         'for the month of June 2026:\n\nBalance at 1 June: cash ₦200,000, bank ₦3,600,000. '
         'Receipts: court fees ₦940,000; motor licence fees ₦1,260,000; fines ₦180,000; '
         'deposits received ₦420,000; advances repaid ₦150,000; remittances from Headquarters '
         'Treasury ₦9,000,000. Payments: personnel cost ₦6,800,000; overhead cost ₦1,940,000; '
         'advances granted ₦360,000; deposits refunded ₦95,000; remittances to Headquarters '
         '₦1,500,000.\n\nCash on hand at 30 June was ₦200,000. The bank statement at 30 June '
         'showed ₦5,080,000. Mandates issued but not presented amounted to ₦480,000, '
         'lodgements not yet credited ₦230,000, and bank charges of ₦25,000 had not been '
         'recorded in the cash book.\n\n(a) Prepare a summary of the cash book for the month. '
         '(b) Classify the transactions into above-the-line and below-the-line items. '
         '(c) Prepare the adjusted cash book and the bank reconciliation statement at 30 June '
         '2026. (d) State six items that must accompany the transcript for the month.',
    'marks': 20,
    'a': [
      {'h4': '(a) Cash book summary'},
      {'stmt': {'t': 'Bauchi Sub-Treasury — cash book summary for June 2026', 'rows': [
        ['Balance brought forward (200,000 + 3,600,000)', 3800000],
        ['**Receipts**@t', None],
        ['Court fees', 940000],
        ['Motor licence fees', 1260000],
        ['Fines', 180000],
        ['Deposits received', 420000],
        ['Advances repaid', 150000],
        ['Remittances from Headquarters Treasury', 9000000],
        ['Total receipts@sub', 11950000],
        ['**Payments**@t', None],
        ['Personnel cost', -6800000],
        ['Overhead cost', -1940000],
        ['Advances granted', -360000],
        ['Deposits refunded', -95000],
        ['Remittances to Headquarters Treasury', -1500000],
        ['Total payments@sub', -10695000],
        ['Balance carried forward@tot', 5055000],
      ]}},
      {'p': 'Cash on hand at 30 June is ₦200,000, so the cash book **bank balance** is '
            '$5{,}055{,}000 - 200{,}000 = ₦4{,}855{,}000$.'},
      {'h4': '(b) Classification'},
      {'table': {'align': 'lrr', 'head': ['', 'Receipts (₦)', 'Payments (₦)'], 'rows': [
        ['**Above the line — revenue**', '', ''],
        ['Court fees', '940,000', ''],
        ['Motor licence fees', '1,260,000', ''],
        ['Fines', '180,000', ''],
        ['', '**2,380,000**', ''],
        ['**Above the line — expenditure**', '', ''],
        ['Personnel cost', '', '6,800,000'],
        ['Overhead cost', '', '1,940,000'],
        ['', '', '**8,740,000**'],
        ['**Below the line**', '', ''],
        ['Advances', '150,000', '360,000'],
        ['Deposits', '420,000', '95,000'],
        ['Remittances', '9,000,000', '1,500,000'],
        ['', '**9,570,000**', '**1,955,000**'],
        ['**Total**', '**11,950,000**', '**10,695,000**'],
      ]}},
      {'p': 'The revenue of the month is therefore **₦2,380,000** and the expenditure '
            '**₦8,740,000**, giving a deficit for the month of ₦6,360,000 which was financed by '
            'the net remittance of ₦7,500,000 from headquarters. Below the line, advances '
            'increased by ₦210,000 (an asset) and deposits by ₦325,000 (a liability).'},
      {'p': 'Check: $2{,}380{,}000 - 8{,}740{,}000 - 210{,}000 + 325{,}000 + 7{,}500{,}000 '
            '= ₦1{,}255{,}000$, which equals the increase in cash from ₦3,800,000 to '
            '₦5,055,000. ✓'},
      {'h4': '(c) Adjusted cash book and reconciliation'},
      {'stmt': {'t': 'Adjusted cash book (bank column)', 'rows': [
        ['Balance per cash book', 4855000],
        ['Less: Bank charges not recorded', -25000],
        ['Adjusted cash book balance@tot', 4830000],
      ]}},
      {'stmt': {'t': 'Bank reconciliation statement as at 30 June 2026', 'rows': [
        ['Balance per bank statement', 5080000],
        ['Less: Mandates issued but not presented', -480000],
        ['Add: Lodgements not yet credited', 230000],
        ['Adjusted cash book balance@tot', 4830000],
      ]}},
      {'p': 'Both statements arrive at **₦4,830,000**, which is the bank figure to be carried '
            'into the transcript and into the Statement of Assets and Liabilities. Together '
            'with cash on hand of ₦200,000, total cash and bank at 30 June is ₦5,030,000.'},
      {'warn': 'If the two sides of a reconciliation do not agree, the difference is never to '
               'be forced or written off. It means a further item exists that has not been '
               'identified — an unrecorded lodgement, a second unpresented mandate, or an '
               'arithmetical error — and the sub-accounting officer must find it before the '
               'transcript is rendered.'},
      {'h4': '(d) Items accompanying the transcript'},
      {'ol': [
        'The **cash book** for the month, cast, balanced and certified by the sub-accounting '
        'officer.',
        'A **schedule of revenue collected**, analysed by head and subhead, with the treasury '
        'receipts and receipt vouchers.',
        'A **schedule of expenditure**, analysed by head and subhead, with the paid payment '
        'vouchers in serial order.',
        'A **schedule of advances** showing the opening balance, advances granted, advances '
        'repaid and the closing balance, with the names of the officers concerned.',
        'A **schedule of deposits** showing the opening balance, deposits received, deposits '
        'refunded and the closing balance, with the names of the depositors.',
        'A **schedule of remittances** in and out, with the transfer advice numbers.',
        'The **bank statement, bank certificate and bank reconciliation statement**.',
        'A **certificate of cash and postage stamps** on hand at the close of the month.',
        'A statement of **unpaid and outstanding vouchers**.',
      ]}],
    'src': 'Chapter 13.3–13.5'},
  ]},
}
