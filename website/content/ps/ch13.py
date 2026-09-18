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

  {'n': '13.6', 't': 'The cash office and cash control', 'b': [
    {'p': 'The cash office is a **sensitive department** — only diligent, trustworthy, '
          'experienced, security-conscious staff should work there.'},
    {'h4': 'Essential features'},
    {'p': 'A paying cage/cubicle; a notice of working hours; a cash tank or safe under '
          '**dual control**; a notice restricting entry to authorised staff; security '
          'personnel; CCTV; a security alarm; a counting machine; a UV/mercury light (for '
          'checking currency); a computer system; and a fire alarm.'},
    {'h4': 'Functions'},
    {'ul': [
      'Receiving and paying out liquid cash, and its safe custody.',
      'Maintaining a conventional cash book for all cash transactions, balanced **daily**.',
      'Operating the ministry\'s current account on which cheques are drawn.',
      'Reconciling the bank statement with the cash book, monthly or as required.',
      'Submitting the original cash book and voucher copies to the accounts department for '
      'the final accounts.',
    ]},
    {'note': 'A **contra entry** records cash moving between the office and the bank — cash '
             'withdrawn (by cheque, without a payment voucher) or surplus cash banked above '
             'the authorised maximum. The **cheque/mandate summary register** cross-checks '
             'every cheque, lodgement, bank advice and teller against the cash book, and must '
             'be **posted by someone other than the cashbook keeper**, as an internal check.'},
    {'h4': 'Security documents and retention'},
    {'p': 'Cheque books, Treasury Receipt Books 6/6A, the cheque summary register, cash '
          'books, payment vouchers, local purchase orders, postal and money orders are all '
          '**security documents** — kept in a safe/strong room under dual-key control. '
          'Retention: financial warrants, cash books and PE records — **permanently**; revenue '
          'collectors\' cash books and original payment vouchers — **7 years**; LPOs and '
          'transport-warrant book copies — **2 years**. Unclaimed cheques are written back '
          'after **six months**.'},
    {'h4': 'Cash control measures'},
    {'ul': [
      'Cash limits; daily banking of all takings; periodic surprise cash counts; a safe under '
      'dual control; a raid alarm; counting/sorting machines and mercury light.',
      'Adequate insurance over the cash limit; investment of idle funds; an authority limit; '
      'daily balancing of the cash book; and regular bank reconciliation.',
    ]},
  ]},

  {'n': '13.7', 't': 'Imprest and the imprest holder', 'b': [
    {'def': {'t': 'Imprest holder', 'd': 'an officer, other than a sub-accounting officer, '
             'entrusted with disbursing public money for which a voucher cannot be presented '
             'immediately to a sub-accounting officer — and who must keep an Imprest '
             'Holder\'s Cash Book.'}},
    {'def': {'t': 'Imprest', 'd': 'cash advanced to an officer to meet urgent, budgeted '
             'expenditure whose vouchers cannot be prepared and presented immediately for '
             'payment.'}},
    {'table': {'align': 'll', 'head': ['Type', 'Nature'], 'rows': [
      ['**Standing imprest**', 'A general imprest running the whole fiscal year, reimbursed '
       'as needed; must be **retired by 31 December**'],
      ['**Special imprest**', 'Raised for a specific purpose; terminated and retired '
       '**immediately the purpose is achieved**'],
    ]}},
    {'h4': 'Checks and balances'},
    {'ul': [
      'The imprest holder must be **Grade Level 04 or above**, of proven integrity.',
      'Imprest money is used for **no other purpose**, and there is **no lending** to '
      'employees from it.',
      'The imprest cash book is balanced regularly, and the sub-accounting officer checks it '
      'regularly for anomalies.',
      'Any balance must be **retired at the fiscal year end**.',
      '₦50,000 or more must be **banked** by the holder in an account opened in his official '
      'capacity.',
      'Every disbursement needs proper authorisation/approval and a **payment voucher** — '
      'vouchers are classified straight to the expenditure heads affected, **not** kept under '
      'an "imprest" head as in the private sector.',
    ]},
    {'p': 'On **reimbursement**, the imprest holder presents all payment vouchers for the '
          'money spent to the sub-accounting officer before the imprest is topped up.'},
  ]},

  {'n': '13.8', 't': 'The revenue collector', 'b': [
    {'def': {'t': 'Revenue collector', 'd': 'a government officer holding an official receipt '
             'book (TF6, TF6A, or similar) to collect specified budgeted revenue items. He '
             '**may not spend from his collections** — he accounts for them intact.'}},
    {'h4': 'Functions'},
    {'ul': [
      'Supervises the receipt of public revenue, ensuring prompt banking.',
      'Promptly reflects all monies collected under the proper heads and subheads.',
      'Ensures proper custody of public funds and securities, and supervises staff entrusted '
      'with receipts, custody or disbursement.',
      'Maintains internal checks against malpractice.',
      'Checks all cash and stamps in his care against the cash book and stamps register.',
      'Makes good any minor deficit not caused by theft/fraud, and reports it in writing to '
      'the appropriate officer.',
    ]},
    {'p': 'His cash book\'s debit side records each receipt (date, receipt number, NCOA code, '
          'payer, amount); the credit side records remittances of total collections to the '
          'sub-accounting officer (daily, weekly, monthly or as directed), each acknowledged '
          'with a **treasury receipt** and logged in the **cash remittance register**. '
          'Anything not yet remitted at month end is carried forward.'},
  ]},

  {'n': '13.9', 't': 'Advances: personal and non-personal', 'b': [
    {'p': 'Advances granted and authorised by the Minister of Finance are also used to write '
          'off a loss of government fund. **Chapter 14 of the Financial Regulations** '
          '(2009) governs their grant.'},
    {'def': {'t': 'Non-personal advance', 'd': 'granted to an officer to carry out a task for '
             'the organisation (e.g. off-site staff training) — authorised by the Minister of '
             'Finance through the Accountant-General, though the Accounting Officer may '
             'approve up to ₦50,000. Must be retired within a reasonable time, or the whole '
             'sum is deducted from salary en bloc; a fresh non-personal advance may not be '
             'granted while an earlier one is unretired.'}},
    {'h4': 'Personal advances (for the officer\'s own benefit)'},
    {'table': {'align': 'll', 'head': ['Type', 'When granted'], 'rows': [
      ['**Salary/rent advance**', 'Returning from leave of 21+ days and proceeding on '
       'transfer; assuming first appointment outside official quarters; returning to Nigeria '
       'by sea to a station other than Lagos; or posted to an overseas Foreign Affairs office'],
      ['**Correspondence-course advance**', 'The officer\'s ability warrants the course; it '
       'relates to his work and will raise his efficiency; the institution is reputable; '
       'completing it isn\'t itself grounds for promotion; repayable interest-free over 24 '
       'instalments; receipts must prove the money was properly used'],
      ['**Estacode advance (overseas tour)**', 'Drawn as traveller\'s cheques from the CBN '
       'against a Government mandate; the officer accounts for it afterwards with receipts '
       'and air tickets'],
    ]}},
  ]},

  {'n': '13.10', 't': 'Self-accounting, sub-self-accounting and non-self-accounting units',
   'b': [
    {'table': {'align': 'lll', 'head': ['Unit', 'Control over its own records', 'Example'],
      'rows': [
      ['**Self-accounting unit**', 'Full control; relates to the Treasury only by rendering '
       'transcripts', 'Ministries of Finance, Works, Education'],
      ['**Sub-self-accounting unit**', 'Same functions, but sends the Treasury the original '
       'cash book, duplicate vouchers, a certificate of cash/bank balances, a pre-listed '
       'voucher schedule and the bank reconciliation', 'The Federal Pay Office in each State'],
      ['**Non-self-accounting unit**', 'No control at all — prepares vouchers but pays through '
       'the Treasury; keeps no Treasury Cash Book and renders no transcript',
       'A State Code of Conduct Bureau'],
    ]}},
    {'p': 'A Ministry becomes **self-accounting** only once it has adequate qualified '
          'personnel, a functioning internal control system, and an internal audit '
          'department.'},
    {'table': {'align': 'll', 'head': ['Advantages of self-accounting', 'Disadvantages'],
      'rows': [
      ['Relieves top management of workload; speeds up operational decisions',
       'Co-ordination and consistency can be difficult to achieve'],
      ['Increases flexibility, reduces communication problems',
       'Extended communication lines can cause information overload'],
      ['Motivates staff, encourages initiative; trains junior management',
       'Risk of duplicated services and sub-optimality (ministerial goals over government '
       'goals); assumes managers of a quality that may not be available; inter-departmental '
       'friction'],
    ]}},
    {'h4': 'Transcripts: three types'},
    {'ul': [
      '**Main (cash) transcript** — the monthly transcript a self-accounting unit submits to '
      'the Accountant-General.',
      '**Supplementary transcript** — the double-entry adjustment to the main transcript.',
      '**Subsidiary transcript** — corrects errors or omissions in the main transcript.',
    ]},
    {'p': 'Preparing a transcript: obtain the cash book and all vouchers posted for the '
          'month and check them; **pre-list** vouchers by head/subhead; **post the totals** '
          'into an analysis book, reconciling with the cash book; **schedule** vouchers by '
          'serial number and gross amount; then **generate the transcript** itself, opening '
          'with the prior month\'s balance carried forward and closing with the balance '
          'carried down, which must agree with the cash book.'},
    {'def': {'t': 'Main ledger', 'd': 'kept by a self-accounting MDA for below-the-line and '
             'other Accountant-General-controlled accounts — cash, imprest, internal bank '
             'adjustment, deposit, personal advances, non-personal advances and cash-transfer '
             'accounts — posted and balanced monthly, and **reconciled with the Treasury '
             'general ledger**, any difference being flagged for follow-up.'}},
  ]},

  {'n': '13.11', 't': 'End-of-chapter questions (study text)', 'b': [
    {'h3': 'Section A'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–10 with answers', 'open': True, 'q': [
      {'ol': [
        'The following, except one, are essential features of a cash office: (i) Paying cage '
        'or cubicle  (ii) Close-circuit monitor  (iii) Cash tank or safe with dual control '
        'key  (iv) Means of convenience for toileting  (v) Counting machine',
        'Which of the following cannot be classified as a security document in government? '
        '(i) Cheque book  (ii) Cash flow statement  (iii) Cash book  (iv) Payment voucher  '
        '(v) Cheque summary register',
        'The following items, except one, should be posted into the Cheque/Mandate Summary '
        'Register: all cheques issued; money lodged into the bank account; vouchers raised '
        'to cover bank advices; total payroll bills of the local government council\'s '
        'staffers; teller particulars',
        'Which of the following documents is NOT required for preparing a bank reconciliation '
        'statement? Cash book and cheque summary register; bank statements; cheque stubs; '
        'debit and credit advices; list of contractors',
        'Salary and rent advances are granted to officers under the following conditions, '
        'except ONE: (A) An officer on official duty lost either of his parents  (B) An '
        'officer is returning from leave of not less than 21 days and/or proceeding on '
        'transfer bearing his own transport cost  (C) An officer is assuming first '
        'appointment and is not living in government residential quarters  (D) An officer '
        'is returning to Nigeria by sea to be stationed elsewhere other than Lagos  (E) An '
        'officer is posted to an overseas office of the Ministry of Foreign Affairs',
        'A register that serves as a useful record for verifying bank transactions in the '
        'cash book is called …',
        'Cash credits granted to individual officers in their ministries/parastatals/'
        'departments, or given to carry out a specified task and to be retired later, are '
        'called …',
        'An MDA that has no control whatsoever over any of its accounting records is called …',
        'A summary of the total receipts and payments as posted in the cash book is called …',
        'The ledger book used to record all receipts and payments of any nature is called …',
      ]}],
      'a': [
      {'p': '**1.** D  **2.** B  **3.** D  **4.** E (list of contractors)  **5.** A  '
            '**6.** Cheque/Mandate Summary Register  **7.** Advances  **8.** Non-self-'
            'accounting unit  **9.** Transcript  **10.** Treasury cash book'}]}},
    {'h3': 'Section B'},
    {'eg': {'tag': 'Study text', 't': 'Question 1 — cash control measures', 'open': True,
      'q': [
      {'p': 'Control of cash is a major activity required of MDAs. List the various cash '
            'control measures they adopt.'}],
      'a': [
      {'ol': [
        'Establishment of cash limits.', 'Daily banking of all takings.',
        'Periodic surprise cash counts (cash survey).',
        'A safe under dual control.', 'A raid alarm.',
        'Counting/sorting machines and mercury light.',
        'Adequate insurance cover over the cash limit.', 'Investment of idle funds.',
        'Establishment of an authority limit.', 'Balancing of the cash book.',
        'Preparation of bank reconciliation statements.',
      ]}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 2 — procedures for bank reconciliation',
      'open': True, 'q': [
      {'p': 'Enumerate the key procedures for preparing a bank reconciliation statement.'}],
      'a': [
      {'ol': [
        'Extract the cash book balance at the end of the month.',
        'Have the previous month\'s reconciliation to hand, for the outstanding unpresented '
        'cheques and uncredited lodgements.',
        'Tick cash-book debit entries against bank-statement credit entries, and cash-book '
        'credit entries against bank-statement debit entries.',
        'Extract the un-ticked items into schedules: A — unpresented cheques; B — credits in '
        'the bank not in the cash book; C — uncredited lodgements; D — debits in the bank '
        'not in the cash book.',
        'Prepare the reconciliation statement from the schedules.',
      ]}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 3 — controlling imprest and the imprest holder',
      'open': True, 'q': [
      {'p': 'Keeping an imprest is a sensitive role that may lead to fraudulent practice. '
            'Enumerate the checks and balances that may be instituted to control imprest and '
            'the imprest holder.'}],
      'a': [
      {'ol': [
        'The holder must be Grade Level 04 or above, of proven integrity.',
        'Imprest money is used for no other purpose.',
        'The imprest cash book is balanced regularly.',
        'The sub-accounting officer checks it regularly for anomalies.',
        'Any balance is retired at the end of the fiscal year.',
        '₦50,000 or more is banked in an account opened in the holder\'s official status.',
        'Every disbursement is properly authorised and approved.',
        'Payment vouchers are raised for all disbursements.',
        'There is no lending to employees from imprest money.',
      ]}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 4 — self-accounting units', 'open': True,
      'q': [
      {'p': '(a) State the conditions for a ministry to become a self-accounting unit. '
            '(b) List the advantages and disadvantages of a self-accounting unit.'}],
      'a': [
      {'p': '**(a)** Adequate qualified personnel; an adequate, functional internal control '
            'system; and an internal audit department.'},
      {'p': '**(b) Advantages:** relieves top management of workload; speeds operational '
            'decision-making; increases flexibility and reduces communication problems; '
            'motivates staff and encourages initiative; and provides better junior-management '
            'training.'},
      {'p': '**Disadvantages:** co-ordination can be hard to achieve; extended communication '
            'lines cause information overload; consistency is harder; services may be '
            'duplicated; ministerial sub-optimality (a ministry\'s goals overriding overall '
            'government objectives); it assumes well-qualified managers who may not be '
            'available; and inter-departmental friction where functions depend on each '
            'other.'}]}},
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
    'src': 'Chapter 13.1', 'sec': '13.1'},
   {'q': 'An advance granted to an officer and outstanding at the year end appears in the '
         'financial statements as',
    'o': ['expenditure', 'an asset', 'a liability', 'revenue', 'a contingent liability'],
    'a': 1,
    'w': 'The advance is recoverable, so it is an asset until it is retired or repaid.',
    'src': 'Chapter 13.2', 'sec': '13.2'},
   {'q': 'In a bank reconciliation, bank charges not recorded in the cash book are',
    'o': ['added to the bank statement balance', 'deducted in the adjusted cash book',
          'deducted from the bank statement balance', 'added in the adjusted cash book',
          'ignored'],
    'a': 1,
    'w': 'The bank has already processed the charge; it is the office that has not recorded it, '
         'so the cash book must be adjusted.',
    'src': 'Chapter 13.5', 'sec': '13.5'},
   {'q': 'The monthly return by which a sub-accounting officer brings his transactions into the '
         'central accounts is called a',
    'o': ['warrant', 'transcript', 'voucher', 'mandate', 'schedule of losses'],
    'a': 1,
    'w': 'The transcript comprises the cash book for the month together with all supporting '
         'schedules and certificates.',
    'src': 'Chapter 13.4', 'sec': '13.4'},
   {'q': 'A cash book shows a bank balance of ₦2,400,000. Unpresented cheques are ₦350,000 and '
         'uncredited lodgements ₦120,000. There are no other differences. The bank statement '
         'balance is',
    'o': ['₦2,170,000', '₦2,630,000', '₦2,870,000', '₦1,930,000', '₦2,400,000'],
    'a': 1,
    'w': 'Work backwards: the bank statement balance less unpresented cheques plus uncredited '
         'lodgements equals the cash book balance.',
    'calc': '\\text{Bank} = 2{,}400{,}000 + 350{,}000 - 120{,}000 = ₦2{,}630{,}000',
    'src': 'Chapter 13.5', 'sec': '13.5'},
   {'q': 'Remittances between government offices are recorded',
    'o': ['as revenue at the receiving office and expenditure at the sending office',
          'below the line at both offices, clearing on consolidation',
          'as expenditure at both offices', 'only at the Headquarters Treasury',
          'in the Statement of Cash Receipts and Payments as revenue'],
    'a': 1,
    'w': 'A remittance is an internal transfer of the government\'s own money. Treating it as '
         'revenue and expenditure would inflate both figures on consolidation.',
    'src': 'Chapter 13.2', 'sec': '13.2'},
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
    'src': 'Chapter 13.3–13.5', 'sec': '13.3'},
  ]},
}
