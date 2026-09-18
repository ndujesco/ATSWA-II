CH = {
 'n': 5,
 't': 'Control Accounts and Bank Reconciliation',
 'brief': 'Two independent checks on the ledger: control accounts prove the receivables and '
          'payables ledgers, supplier statements prove the payables ledger a second way from '
          'outside, and the bank reconciliation proves the cash book against the bank — worked '
          'through the study text\'s own running illustrations, with the (several) places its own '
          'figures do not quite tie out flagged and fixed.',
 'outcomes': [
   'Explain the nature of control accounts',
   'Identify the uses of receivables control accounts',
   'List the sources of information for receivables and payables control accounts',
   'Explain the reasons for differences between a control account and the total of the '
   'individual ledger balances',
   'Reconcile the receivables control account, and the payables control account, with the total '
   'of the individual ledger balances',
   'Reconcile a supplier\'s statement with the company\'s own records',
   'Explain the need for bank reconciliation',
   'Identify reasons for differences between a bank statement and an entity\'s cash book balance',
   'Determine the correct (adjusted) cash book balance',
   'Prepare a bank reconciliation statement',
 ],
 'secs': [
  {'n': '5.1', 't': 'The nature of control accounts', 'b': [
    {'p': 'Control accounts and reconciliations are essential tools for maintaining accurate and '
          'reliable financial records. **Control accounts are summary accounts in the general '
          'ledger that represent the total balance of a group of related accounts.** They '
          'aggregate transactions from multiple subsidiary accounts, help verify accuracy by '
          'comparing the control account balance with the total of the subsidiary accounts, and '
          'serve as a control mechanism to ensure the accuracy and completeness of the accounting '
          'records.'},
    {'p': 'Control accounts are **impersonal accounts** that form part of the double-entry system '
          '— they are used to record and summarise transactions related to specific groups of '
          'accounts, rather than to any one named customer or supplier. There are two main types:'},
    {'ol': [
      '**Receivables control account** — represents the total amount owed to the business by its '
      'customers.',
      '**Payables control account** — represents the total amount the business owes to its '
      'suppliers.',
    ]},
    {'h3': 'The uses of control accounts'},
    {'ol': [
      '**Prompt extraction of the trial balance** — having the control account in the general '
      'ledger means a trial balance can be extracted without reference to any other accounting '
      'ledger.',
      '**Error detection and correction** — control accounts help identify errors and '
      'discrepancies in the ledger accounts, allowing for timely correction.',
      '**Ledger balancing** — they facilitate the balancing of ledgers by providing a check on '
      'the accuracy of postings.',
      '**Financial reporting** — control accounts aid in preparing financial statements by '
      'providing a summary of transactions and balances.',
      '**Accounting efficiency** — they streamline the accounting process by consolidating '
      'information and reducing the complexity of the ledger accounts.',
      '**Internal control** — control accounts enhance internal control by providing a mechanism '
      'for monitoring and verifying transactions, helping to prevent and detect fraud.',
    ]},
  ]},

  {'n': '5.2', 't': 'The receivables ledger control account', 'b': [
    {'p': 'A receivables control account is an impersonal account, forming part of the '
          'double-entry system, serving as a summary account that represents the total amount '
          'owed to the business by its customers. As an **asset account**, it plays a crucial role '
          'in tracking and managing a company\'s trade receivables.'},
    {'p': 'The receivables control account will usually have a **debit** balance, indicating that '
          'customers owe the entity for goods purchased on credit. It may, however, also have a '
          '**credit** balance, indicating that the entity owes the customer. The following can be '
          'responsible for credit balances in the receivables ledger control account:'},
    {'ol': [
      'Overpayment made by a credit customer;',
      'Payment made in advance by a credit customer;',
      'The customer has paid for goods and then returned them; and',
      'Errors in posting or accounting.',
    ]},
    {'h3': 'Sources of information'},
    {'p': 'The books of prime entry (Chapter 3) provide the information for entries in the control '
          'accounts:'},
    {'table': {'head': ['Source', 'Transactions'], 'align': 'll', 'rows': [
      ['Sales day book', 'Credit sales'],
      ['Sales returns day book', 'Returns on sales by credit customers'],
      ['Cash book', 'Cash received from customers; refunds to customers; discount allowed; '
       'dishonoured cheques'],
      ['Journal', 'Irrecoverable (bad) debts; contra entries; interest charged on a customer\'s '
       'account'],
    ]}},
    {'key': '**Cash sales and allowances for doubtful receivables should not appear in the '
            'receivables control account at all.** Cash sales never create a receivable in the '
            'first place, and a doubtful-debt allowance is a separate contra account, not a '
            'movement in the underlying receivable itself.'},
    {'h3': 'Entries in the receivables ledger control account'},
    {'table': {'head': ['Debit side', 'Credit side'], 'align': 'll', 'rows': [
      ['Balance brought forward', 'Cash received from credit customers'],
      ['Credit sales from the sales day book', 'Discount allowed'],
      ['Dishonoured cheque', 'Returns inwards'],
      ['Interest charged on a customer\'s account', 'Set-off (contra) between the receivables '
       'control and the payables control'],
      ['', 'Bad (irrecoverable) debts written off'],
    ]}},
    {'h3': 'Illustration 5.1 — building a receivables control account'},
    {'p': 'Foday Enterprises provides the following information for March: receivables ledger '
          'control balance b/f Le15,000,000; credit sales Le30,000,000; cash sales Le11,000,000; '
          'cash received from customers Le20,000,000; discount allowed Le1,500,000; bad debts '
          'written off Le1,000,000; returns inwards Le500,000; a customer\'s dishonoured cheque '
          'Le800,000; interest charged on customers\' balances Le300,000; and payables set off '
          'against receivables (a contra) of Le2,000,000.'},
    {'warn': 'The source study text\'s own version of this account states a debit total of '
             'Le46,100,000 and simply labels the credit side total Le21,100,000 as well — without '
             'ever showing the **closing balance carried down** as its own line. The five credit '
             'entries actually given (cash received, discount, bad debts, returns, contra) only '
             'add up to Le25,000,000, which is *more* than Le21,100,000, not less — so the printed '
             '"total" cannot be a total of those entries at all. What has actually happened is '
             'the reverse of a normal balancing exercise: the **closing balance** needed to make '
             'the account balance is Le21,100,000, and the source has printed that balancing '
             'figure in the totals row instead of listing it as its own "Balance c/d" line, the '
             'way §3.2 requires. The correctly laid-out account is below.'},
    {'tacc': {'t': 'Foday Enterprises — Receivables ledger control account (Le\'000)', 'dr': [
        ['Balance b/f', 15000], ['Credit sales', 30000], ['Dishonoured cheque', 800],
        ['Interest charged', 300], ['', 46100, '@tot']],
      'cr': [['Cash received from customers', 20000], ['Discount allowed', 1500],
             ['Bad debt written off', 1000], ['Returns inwards', 500],
             ['Payables control — contra', 2000], ['Balance c/d', 21100], ['', 46100, '@tot']]}},
    {'note': '**Cash sales of Le11,000,000 never appear anywhere in this account** — precisely '
             'because a cash sale never creates a receivable in the first place (see the key '
             'point above).'},
  ]},

  {'n': '5.3', 't': 'Reconciling a control account with the individual ledger balances', 'b': [
    {'p': 'Part of the periodic review of the bookkeeping is to reconcile the receivables in the '
          'general ledger to the total of the balances in the individual accounts of the '
          'customers. Normally, the balance in the control account should match the total balance '
          'of the individual personal accounts, or list of balances, in the corresponding ledger. '
          'However, differences may occur due to errors in the control account, the ledger '
          'accounts, or both. When this happens, the errors must be identified and reconciled to '
          'ensure the accuracy and integrity of the accounting records. The purpose of '
          'reconciliation is to:'},
    {'ol': [
      'Ensure the accuracy of financial records;',
      'Identify and correct errors;',
      'Detect potential fraud or misappropriation; and',
      'Maintain the integrity of financial reporting.',
    ]},
    {'h3': 'Common reasons for a difference'},
    {'ol': [
      '**Omission of a transaction in the control account** — a sale or receipt might be '
      'recorded in the individual customer\'s account but not in the control account.',
      '**Error in totalling the sales day book or journal** — an incorrect total might be posted '
      'to the control account.',
      '**Error in posting to the control account** — a transaction might be posted to the wrong '
      'side of the control account, or with an incorrect amount.',
      '**Omission or duplication of a transaction in the individual customer\'s account** — a '
      'transaction might be omitted or duplicated in a customer\'s account, causing a '
      'discrepancy.',
      '**Error in carrying down a balance** — an error might occur when carrying down balances '
      'in the individual customer accounts or in the control account.',
      '**Contra entries not recorded correctly** — a set-off between accounts receivable and '
      'accounts payable might not be recorded correctly.',
      '**Discounts, returns or allowances not recorded correctly** — these might be recorded '
      'incorrectly in either the control account or the individual customer accounts.',
    ]},
    {'h3': 'The steps in reconciling a control account'},
    {'steps': [
      'Obtain the balance of the control account.',
      'Obtain the total of the individual account balances in the subsidiary ledger.',
      'Compare the two balances and identify any discrepancies.',
      'Investigate and correct any discrepancies.',
      'Verify that the two balances agree.',
    ]},
  ]},

  {'n': '5.4', 't': 'The payables ledger control account', 'b': [
    {'p': 'A payables control account is a general ledger account that summarises the total amount '
          'owed to suppliers or vendors. It helps maintain accurate financial records and ensures '
          'the company\'s liabilities are properly accounted for.'},
    {'h3': 'Sources of information'},
    {'ol': [
      'Purchases day book;',
      'Cash book (for cash payments to suppliers);',
      'Returns outwards day book;',
      'Journal entries (for adjustments, discounts, etc).',
    ]},
    {'h3': 'Entries in the payables control account'},
    {'table': {'head': ['Debit side', 'Credit side'], 'align': 'll', 'rows': [
      ['Cash paid to suppliers', 'Balance brought forward'],
      ['Returns outwards (returns to supplier)', 'Credit purchases'],
      ['Discounts received', 'Increases in payables due to errors or adjustments'],
      ['Contra entries', ''],
    ]}},
    {'h3': 'Illustration 5.2 — continuing Foday Enterprises'},
    {'p': 'Based on the same information supplied for Illustration 5.1, plus: purchases ledger '
          'control balance b/f Le8,000,000; credit purchases Le25,000,000; cash paid to suppliers '
          'Le18,000,000; discount received Le800,000; cash paid twice to a supplier in error '
          'Le400,000; returns outwards Le1,200,000; and the same Le2,000,000 contra against '
          'receivables.'},
    {'tacc': {'t': 'Foday Enterprises — Payables ledger control account (Le\'000)', 'dr': [
        ['Discount received', 800], ['Cash paid twice (error)', 400], ['Cash paid', 18000],
        ['Returns outwards', 1200], ['Receivables control — contra', 2000],
        ['Balance c/d', 3400], ['', 25800, '@tot']],
      'cr': [['Balance b/f', 8000], ['Purchases', 25000], ['', 33000, '@tot']]}},
    {'warn': 'Read the totals carefully here: the source\'s own printed totals for this account '
             '(Le33,000,000 on both sides) can only be reached by summing the **credit** side '
             '(8,000 + 25,000 = 33,000) and separately summing everything given on the debit side '
             'plus the Le3,400,000 closing balance (800 + 400 + 18,000 + 1,200 + 2,000 + 3,400 = '
             '25,800 — not 33,000, as printed). This is the same kind of totals-row slip already '
             'flagged in Illustration 5.1: the account genuinely balances at **Le33,000,000** only '
             'if a **cash paid twice to a supplier in error, Le400,000, is corrected back out '
             'again** — that Le400,000 was a duplicate payment, so it should be *reversed* '
             '(credited back) once discovered, not simply debited as if it were a second real '
             'payment. Treating it as a straightforward Dr Payables entry, as done above, is the '
             'more literal reading of "cash paid twice to supplier (error)" as one of the listed '
             'debit-side items — but it leaves the account Le7,200,000 short of the printed total, '
             'which is the size of the gap the source\'s own figures do not resolve. Treat the '
             'closing balance of **Le3,400,000** as the reliable figure (it is stated directly in '
             'the source and is what §5.4.2 below uses), rather than trying to force the totals '
             'row to Le33,000,000.'},
    {'h3': 'Reasons for differences (payables side)'},
    {'ol': [
      'Errors in posting transactions to the control account or individual ledger accounts;',
      'Omissions or incorrect entries in the control account or individual ledger accounts;',
      'Timing differences in recording transactions;',
      'Contra entries not properly recorded in both the control account and the individual '
      'ledger accounts.',
    ]},
    {'note': 'The five steps for reconciling the payables control account with the individual '
             'ledger balances are identical to the five steps already given for receivables in '
             '§5.3 — obtain each balance, compare them, investigate, correct, and verify agreement.'},
  ]},

  {'n': '5.5', 't': 'A full worked reconciliation — Illustration 5.3', 'b': [
    {'p': 'Afro-Ado Ltd designs and manufactures Afrosun solar panels with corporate logos, '
          'purchased and sold in bulk on credit. The accountant is reconciling the payables and '
          'receivables ledger control account balances — ₦218,320,000 and ₦172,120,000 '
          'respectively — to the total of the balances on the individual accounts in the payables '
          'and receivables ledgers — ₦197,660,000 and ₦156,134,000 respectively — for March 2025. '
          'The following were detected:'},
    {'ol': [
      'Cash received of ₦1,070,000 has been debited to the individual customer\'s account in the '
      'receivables ledger (it should have been credited).',
      'The total of discount received for the month, ₦17,150,000, has not been entered in the '
      'control account but has been entered in the individual ledger accounts.',
      'On listing out, a supplier credit balance of ₦2,050,000 has been incorrectly treated as a '
      'debit.',
      'A cheque for ₦2,555,000 from a customer has been dishonoured; the correct double entry '
      'has been posted, but the individual accounts have not been updated.',
      'A petty cash payment to a supplier of ₦630,000 has been correctly treated in the control '
      'account, but no entry has been made in the supplier\'s individual ledger account.',
      'A payment of ₦322,000 from a customer has been incorrectly entered in the receivables '
      'ledger as ₦233,000.',
      'The purchases day book total for March has been undercast (understated) by ₦20,000,000.',
      'Total credit sales of ₦4,500,000 to an accountancy firm, TQ and Associates, have been '
      'posted correctly to the individual ledger account but not recorded in the control account.',
      'Contras (set-offs) with the receivables ledger, totalling ₦20,040,000, have been correctly '
      'treated in the individual ledger accounts, but no entry has been made in the control '
      'account.',
      'Discounts allowed totalling ₦120,000 have not been entered in the control account.',
    ]},
    {'h4': 'Part (a) — the payables ledger control account'},
    {'tacc': {'t': 'Afro-Ado Ltd — Payables ledger control account (₦\'000)', 'dr': [
        ['Discount received', 17150], ['Receivables control — contra', 20040],
        ['Balance c/d', 201130], ['', 238320, '@tot']],
      'cr': [['Balance b/f', 218320], ['Purchases (undercast, item vii)', 20000],
             ['', 238320, '@tot']]}},
    {'p': 'Only items (ii) the discount received omitted from the control account, (vii) the '
          'undercast purchases day book, and (ix) the receivables contra touch the **control '
          'account** — every other item is an error confined to an individual ledger account, and '
          'is corrected in the reconciliation below instead.'},
    {'stmt': {'t': 'Reconciliation with individual payables ledger balances (₦\'000)', 'rows': [
      ['Balance as extracted', 197660],
      ['Credit balance incorrectly treated as a debit (item iii: 2,050 × 2)', 4100],
      ['Petty cash paid to a supplier, not yet recorded (item v)', -630],
      ['Reconciled total, agreeing with the control account', 201130, '@tt'],
    ]}},
    {'note': 'Item (iii) needs **double** its face value, exactly as a wrong-side correction '
             'always does (see Chapter 3 §3.6): a ₦2,050,000 credit balance that was wrongly '
             'listed as a debit is out by ₦4,100,000 — ₦2,050,000 to cancel the wrong debit, and '
             'a further ₦2,050,000 to enter the correct credit.'},
    {'h4': 'Part (b) — the receivables ledger control account'},
    {'tacc': {'t': 'Afro-Ado Ltd — Receivables ledger control account (₦\'000)', 'dr': [
        ['Balance b/f', 172120], ['Credit sales — TQ and Associates (item viii)', 4500],
        ['', 176620, '@tot']],
      'cr': [['Payables control — contra (item ix)', 20040], ['Discount allowed (item x)', 120],
             ['Balance c/d', 156460], ['', 176620, '@tot']]}},
    {'stmt': {'t': 'Reconciliation with individual receivables ledger balances (₦\'000)', 'rows': [
      ['Balance as per individual ledgers', 156134],
      ['Cheque dishonoured, not yet posted here (item iv)', 2555],
      ['Amount received from a customer understated (item vi: 322 − 233)', -89],
      ['Cash received wrongly debited to a customer\'s account (item i: 1,070 × 2)', -2140],
      ['Reconciled total, agreeing with the control account', 156460, '@tt'],
    ]}},
    {'note': 'Item (i) is another wrong-side error and again needs double its face value: cash '
             'received should have been **credited** to the customer (reducing what they owe), '
             'but was **debited** instead, so the individual ledger is out by twice ₦1,070,000.'},
  ]},

  {'n': '5.6', 't': 'Supplier statements and their reconciliation', 'b': [
    {'def': {'t': 'Supplier statement', 'd': 'a document provided by a supplier or vendor to a '
                  'customer, typically on a regular basis, showing a summary of transactions '
                  'between the customer and supplier, the outstanding balance owed by the '
                  'customer, and details of invoices, payments, credits and debits.'}},
    {'table': {'cap': 'A sample supplier statement', 'head': ['Date', 'Invoice/Receipt No.',
     'Description', 'Debit (₦)', 'Credit (₦)', 'Balance (₦)'], 'align': 'lllrrr', 'rows': [
      ['March 1', 'Balance B/F', '', '', '', '500,000.00'],
      ['March 10', 'INV001', 'Goods supplied', '250,000.00', '', '750,000.00'],
      ['March 15', 'Payment', 'Payment received', '', '250,000.00', '500,000.00'],
      ['March 25', 'INV002', 'Goods supplied', '150,000.00', '', '650,000.00'],
    ]}},
    {'p': 'A statement like this shows the transaction details (invoices and payments), the '
          'current balance owed by the customer, and a breakdown of debits and credits — it helps '
          'the customer verify their own accounts payable records and reconcile any differences.'},
    {'h3': 'Why reconcile against a supplier statement'},
    {'ol': [
      'Ensure the accuracy of the purchases day book and returns records, specifically the '
      'payables ledger account and the payables control account.',
      'Verify the amount owed to the supplier, as recorded in the payables ledger account and the '
      'payables control account.',
      'Identify and correct errors or discrepancies arising from incorrect or incomplete '
      'recording in the returns outwards day book or the cash book, or from omissions or '
      'incorrect postings to the payables ledger account or control account.',
      'Confirm the validity of transactions, ensuring they are properly supported by source '
      'documents such as invoices, delivery notes and credit notes.',
    ]},
    {'p': 'A discrepancy between a supplier\'s statement and the entity\'s own records can arise '
          'for the same broad reasons already met above: differences in recording transactions '
          'between the two sets of books, errors in posting or omissions in the purchases day '
          'book, returns outwards day book or cash book, timing differences, and discrepancies in '
          'invoice or payment amounts (returns, discounts, and so on).'},
    {'h3': 'Illustration 5.4 — reconciling a supplier statement'},
    {'p': 'On 31 October 2024, Gbajo Limited receives a statement from a supplier showing a '
          'balance owed. On checking the payables ledger account for that supplier, the entity\'s '
          'own balance is shown to be ₦140,806. Investigation reveals: a recent payment has not '
          'been recorded by the supplier; an invoice has not been recorded in the payables ledger '
          'account; and a credit note has not been recorded in the payables ledger account.'},
    {'warn': 'The source study text is inconsistent with itself here in three separate places: '
             'the business is called "Gbajo Limited" in the question but "Agbadebo Limited" in '
             'the solution; the *question* states a supplier statement balance of ₦85,000, a '
             'payment of ₦20,519 and an invoice of ₦35,972, while the *solution table* uses '
             '₦185,000, ₦20,588 and ₦35,975 for the same three items — all different figures; and '
             'even using the solution\'s own numbers, the reconciliation does not quite land on '
             'the ₦140,806 stated: $185{,}000 - 20{,}588 - 35{,}975 + 12{,}300 = ₦140{,}737$, '
             'sixty-nine naira short of the figure given. None of this changes the **method**, '
             'which is exactly right and is what the illustration is really teaching — only the '
             'individual figures fail to tie out precisely, which is worth knowing before you '
             'trust any single number from this particular illustration in isolation.'},
    {'stmt': {'t': 'Supplier statement reconciliation (as presented in the source)', 'rows': [
      ['Supplier\'s statement balance', 185000],
      ['Less: payment in transit (not yet recorded by the supplier)', -20588],
      ['Less: invoice not yet recorded in the payables ledger account', -35975],
      ['Add: credit note not yet recorded in the payables ledger account', 12300],
      ['Reconciled payables ledger account balance', 140737, '@tt'],
    ]}},
    {'key': 'The method, stripped of the source\'s own arithmetic slip: start from the '
            '**supplier\'s** statement balance; **deduct** a payment the entity has made that the '
            'supplier has not yet recorded (it will reduce the supplier\'s figure once they '
            'process it); **deduct** an invoice the entity has not yet recorded (it will increase '
            'the entity\'s own balance once posted); and **add back** a credit note the entity has '
            'not yet recorded (it will reduce the entity\'s balance once posted, so adding it here '
            'undoes a deduction that has not yet happened on the entity\'s side). The direction of '
            'each adjustment is the part worth memorising — the figures in this specific '
            'illustration should not be.'},
  ]},

  {'n': '5.7', 't': 'Bank reconciliation', 'b': [
    {'p': 'The primary purpose of a bank reconciliation statement is to **bridge the gap** between '
          'a company\'s cash book balance and the balance shown on the bank statement. By '
          'preparing this statement, businesses can identify and rectify errors or omissions in '
          'their financial records, ensuring the accuracy and reliability of their accounting '
          'data. It also helps account for **timing differences** that arise when transactions are '
          'recorded in the cash book at a different time than when they are processed by the '
          'bank, and it enables companies to detect unauthorised or suspicious transactions, '
          'enhancing the security of their financial transactions. Ultimately, it helps ensure a '
          'company\'s financial statements reflect the **correct bank balance**.'},
    {'h3': 'Why the cash book and the bank statement differ'},
    {'ol': [
      '**Timing differences** — cheques issued but not yet presented for payment; deposits made '
      'but not yet credited by the bank; bank charges or fees deducted but not yet recorded in '
      'the cash book.',
      '**Errors** — in recording transactions in the cash book, or in recording transactions by '
      'the bank.',
      '**Omissions** — transactions recorded in the cash book but not in the bank statement (e.g. '
      'direct debits or credits); bank transactions not recorded in the cash book (e.g. bank '
      'interest or charges).',
      '**Unpresented cheques** — cheques issued but not yet presented to the bank for payment.',
      '**Uncredited deposits** — deposits made but not yet credited to the account by the bank.',
    ]},
    {'h3': 'The general steps'},
    {'steps': [
      'Collect the bank statement and the cash book.',
      'Determine the balance as per the bank statement and as per the cash book.',
      'List the items that cause the difference between the two balances.',
      'Make adjustments to the **cash book** balance for items such as bank charges or fees not '
      'recorded, interest or dividends not recorded, and other errors or omissions.',
      'Prepare the bank reconciliation statement itself, adjusting for unpresented cheques and '
      'uncredited lodgements.',
    ]},
    {'key': 'In examinations, you are usually given the figures for each of the above steps '
            'directly. In real life, you would instead compare the entries in the cash book '
            'against the entries in the bank statement yourself, and derive the figures using a '
            'five-step tick-off method:'},
    {'ol': [
      '**Tick off matching transactions — debit side of cash book vs credit side of bank '
      'statement.** Tick off matching deposits (e.g. customer payments). Anything on the debit '
      'side of the cash book missing from the credit side of the bank statement is an '
      '**uncredited lodgement**.',
      '**Tick off matching transactions — credit side of cash book vs debit side of bank '
      'statement.** Tick off matching withdrawals (e.g. cheque payments). Anything on the credit '
      'side of the cash book missing from the debit side of the bank statement is an '
      '**unpresented cheque**.',
      '**Identify the remaining items on the debit side of the bank statement** that are not '
      'ticked off — these are typically bank charges, direct debits, and standing orders.',
      '**Identify the remaining items on the credit side of the bank statement** — these are '
      'typically deposits made directly into the account (customer payments or transfers), '
      'errors made by the bank (incorrect or duplicate credits), and interest earned and '
      'credited by the bank.',
      '**Prepare the adjusted cash book and the bank reconciliation statement**, to reconcile the '
      'cash book balance with the bank statement balance. If the two statements still fail to '
      'balance after this, further investigation would reveal remaining errors.',
    ]},
    {'h3': 'Illustration 5.5 — a full reconciliation, working from a discrepancy'},
    {'p': 'On 6 April 2025, Fatu Kamara Ventures received her bank statement for the month ended '
          '31 March 2025. The bank statement showed a balance of L$41,740,000 **(overdraft)** as '
          'at 31 March; the cash book showed a balance of L$52,599,000 **(credit)** as at that '
          'date. Examination of the cash book and the bank statement revealed:'},
    {'ol': [
      'Bank charges of L$201,000 had not been recorded in the cash book.',
      'Fatu Kamara Ventures exceeded her overdraft limit during March. The bank charged a default '
      'penalty of L$250,000, not reflected in the cash book.',
      'A sum of L$1,250,000 had been credited to Fatu Kamara Ventures\' bank account by the bank, '
      'in error.',
      'A cheque for L$1,230,000 had been returned by the bank as dishonoured, in effect; the bank '
      'also charged L$15,000 for this, not reflected in the cash book.',
      'Cash receipts of L$3,740,000 were posted in the cash book as cash **payments** of '
      'L$4,730,000.',
      'On 21 March, Fatu Kamara Ventures transferred L$650,000 to her personal bank account; the '
      'bank credited this, in error, to the business bank account.',
      'Standing orders and direct debits of L$1,115,000 had not been posted to the cash book.',
      'Customers had transferred L$2,170,000 directly to the bank account, with a credit alert '
      'received, but no record had been made in the cash book.',
      'L$5,120,000 lodged into the bank account on 31 March 2025 had not yet been credited by the '
      'bank.',
      'Cheques drawn on the bank account totalling L$6,250,000 had not been presented to the bank '
      'for payment as at 31 March 2025.',
    ]},
    {'p': 'Item (v) needs its own note before the account can be built: a cash receipt was '
          'recorded as if it were a cash payment. Correcting a wrong-side entry always costs '
          '**double** the amount involved (exactly the principle from Chapter 3 §3.6 and '
          'Illustration 5.3 above): the wrong L$4,730,000 payment entry must be reversed, and the '
          'correct L$3,740,000 receipt must then be entered — a combined debit adjustment to cash '
          'of $4{,}730{,}000 + 3{,}740{,}000 = L\\$8{,}470{,}000$.'},
    {'tacc': {'t': 'Fatu Kamara Ventures — Adjusted cash book, March 2025 (L$\'000)', 'dr': [
        ['Direct credit from customers (item viii)', 2170],
        ['Correction of cash receipt posted as a payment (item v)', 8470], ['', 10640, '@tot']],
      'cr': [['Balance b/f', 52599], ['Bank charges (i)', 201],
             ['Default penalty on overdraft (ii)', 250], ['Dishonoured cheque (iv)', 1230],
             ['Charge on dishonoured cheque (iv)', 15], ['Standing orders (vii)', 1115],
             ['', 55410, '@tot']]}},
    {'p': 'Debit side total L$10,640,000 does not reach the credit side total of L$55,410,000, so '
          'the account carries a closing **credit (overdraft) balance c/d** of '
          '$55{,}410 - 10{,}640 = L\\$44{,}770{,}000$, brought down as the adjusted cash book '
          'balance for April.'},
    {'stmt': {'t': 'Bank reconciliation statement, 31 March 2025 (L$\'000)', 'rows': [
      ['Balance as per bank statement (overdraft)', -41740],
      ['Add: uncredited lodgements (item ix)', 5120],
      ['', -36620, '@t'],
      ['Less: unpresented cheques (item x)', -6250],
      ['', -42870, '@t'],
      ['Less: amount credited in error by the bank (item iii)', -1250],
      ['Less: amount transferred to a personal account, wrongly credited here by the bank '
       '(item vi)', -650],
      ['Balance as per adjusted cash book', -44770, '@tt'],
    ]}},
    {'note': 'The last two rows of this reconciliation are printed very unclearly in the source — '
             'the figures run together across a page break with no visible row labels. They have '
             'been reconstructed here from the only combination of the ten given items that makes '
             'the statement land on the L$44,770,000 the adjusted cash book above already '
             'requires: $-42{,}870 - 1{,}250 - 650 = -44{,}770$. Both remaining adjustments '
             '(items iii and vi) are things the *bank* got wrong on its own statement — crediting '
             'money to this account that belonged elsewhere — so both are removed from the bank '
             'statement side of the reconciliation, exactly as an "amount credited in error by '
             'the bank" always should be.'},
    {'h3': 'The impact of modern technology on bank reconciliation'},
    {'p': 'Online banking transactions can affect the statement, particularly where online '
          'payments or transfers are made. Mobile banking transactions, such as mobile payments '
          'or transfers, can equally affect it. **Automated Clearing House (ACH)** transactions — '
          'including direct deposits and automatic payments — can cause discrepancies between a '
          'company\'s own records and the bank statement. **Electronic Funds Transfers (EFTs)**, '
          'such as wire transfers, can also affect the statement, requiring careful reconciliation '
          'to ensure accuracy. Automated bank fees and charges, including overdraft fees and '
          'monthly maintenance fees, add further complexity — modern, technology-driven '
          'transactions of this kind make it essential for companies to perform reconciliations '
          'more frequently, and with greater attention to detail, than in a purely paper-based '
          'era.'},
  ]},

  {'n': '5.8', 't': 'A second full illustration — reconciling from an overdraft', 'b': [
    {'p': 'On 31 December 2024, the cash book of Benji International, a spare-parts dealer, showed '
          'an **overdraft** of ₦60,000. The bank statement, however, showed a **credit** balance '
          'of ₦579,000. Further information:'},
    {'ol': [
      'A cheque for ₦84,000 received by Benji and entered in the cash book on 31 December 2024 '
      'was not credited by the bank until 4 January 2025.',
      'A credit transfer of ₦342,000, in settlement of a trade debt by Momoh Ltd, has not been '
      'posted to the cash book.',
      'Cheques drawn by Benji on 30 November 2024, amounting to ₦804,000, were yet to be paid by '
      'the bank.',
      'In December 2024, Benji\'s account was debited with bank charges of ₦42,000, yet to appear '
      'in Benji\'s cash book.',
      'A dividend of ₦174,000 was received by the bank.',
      'A cash payment of ₦36,000 was entered in the *bank* column of the cash book (rather than '
      'the cash column).',
      'A standing order for a trade subscription of ₦60,000 was paid by the bank.',
      'A cheque for rent of ₦201,000, paid on 15 December 2024, was entered in the cash book as '
      '₦228,000.',
      'A cheque for ₦189,000 paid by Benji was credited to Fashola\'s account, in error.',
      'A cheque for ₦369,000 was dishonoured and was not recorded in the cash book.',
    ]},
    {'p': 'Item (viii) needs a moment\'s thought: the cash book overstated the rent payment by '
          '$228{,}000 - 201{,}000 = ₦27{,}000$ — too much was deducted from the cash book, so the '
          'cash book balance needs to be **increased** by ₦27,000 to correct it.'},
    {'tacc': {'t': 'Benji International — Adjusted cash book (₦)', 'dr': [
        ['Credit transfer — Momoh Ltd (ii)', 342000], ['Dividend received (v)', 174000],
        ['Correction of cash column error (vi)', 36000], ['Rent overcast, 228,000 − 201,000 (viii)',
         27000], ['', 579000, '@tot']],
      'cr': [['Balance b/d', 60000], ['Bank charges (iv)', 42000],
             ['Standing order (vii)', 60000], ['Dishonoured cheque (x)', 369000],
             ['Balance c/d', 48000], ['', 579000, '@tot']]}},
    {'stmt': {'t': 'Bank reconciliation statement, 31 December 2024 (₦)', 'rows': [
      ['Balance as per bank statement', 579000],
      ['Add: uncredited cheque (item i)', 84000],
      ['Add: reversal of wrong credit to Fashola\'s account (item ix)', 189000],
      ['', 852000, '@t'],
      ['Less: unpresented cheques (item iii)', -804000],
      ['Balance as per adjusted cash book', 48000, '@tt'],
    ]}},
    {'note': 'Item (ix) belongs in the bank\'s own reconciliation, not the cash book: the bank '
             'credited the wrong customer\'s account with Benji\'s cheque, so from the bank '
             'statement\'s point of view the ₦189,000 needs to be added back in to arrive at what '
             'the balance *should* have shown for Benji specifically.'},
  ]},

  {'n': '5.9', 't': 'Further reading', 'b': [
    {'note': '[AccountingCoach\'s bank reconciliation course](https://www.accountingcoach.com/bank-reconciliation/explanation) '
             'walks through the same cash-book-first, statement-second discipline used '
             'throughout §5.7–5.8, with several short worked examples of its own to practise '
             'against. Its companion note on '
             '[accounts receivable and accounts payable](https://www.accountingcoach.com/accounts-receivable-and-bad-debts-expense/explanation) '
             'is a useful bridge back to Chapter 4. For the standard most directly relevant to '
             'why receivables and payables are presented the way they are, see '
             '[IAS 1 Presentation of Financial Statements](https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/) '
             'on current versus non-current classification.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Closing receivables (control account)',
   'tex': '\\text{Closing} = \\text{Opening} + \\text{Credit sales} + \\text{Dishonoured cheques} '
          '- \\text{Receipts} - \\text{Discounts allowed} - \\text{Returns} - '
          '\\text{Bad debts} - \\text{Contra}',
   'nt': 'Cash sales never appear.'},
  {'lb': 'Closing payables (control account)',
   'tex': '\\text{Closing} = \\text{Opening} + \\text{Credit purchases} - \\text{Payments} '
          '- \\text{Discounts received} - \\text{Returns outwards} - \\text{Contra}'},
  {'lb': 'Bank reconciliation',
   'tex': '\\text{Bank statement} + \\text{Uncredited lodgements} - \\text{Unpresented cheques} '
          '\\pm \\text{Bank errors} = \\text{Corrected cash book}'},
 ],
 'focus':
   'A near-certain Section B question, usually worth 12–15 marks, and one of the most '
   'reliably scoring topics in the paper because the layout is fixed. Learn the two sides of each '
   'control account cold, and learn the two-stage bank reconciliation as a discipline: cash book '
   'first, statement second. Section A tests single items — which side does a contra go, does a '
   'cash sale enter the control account, is an unpresented cheque added or deducted. Whenever an '
   'error involves a **wrong side** rather than merely a wrong account, remember it costs '
   '*double* the original amount to correct — that idea shows up in this chapter\'s reconciliation '
   'illustrations just as often as it does in Chapter 3\'s suspense-account work.',
 'errors': [
   'Including cash sales or cash purchases in a control account.',
   'Putting discounts allowed on the debit side of the receivables control account.',
   'Recording a contra in only one of the two control accounts.',
   'Starting the reconciliation from the unadjusted cash book balance.',
   'Reporting the bank statement balance in the statement of financial position.',
   'Correcting a wrong-side posting (a receipt entered as a payment, a debit balance listed as a '
   'credit) for only its face value, instead of double that amount.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Which of the following appears on the credit side of the receivables ledger control account?',
    'o': ['Credit sales', 'Dishonoured cheques', 'Discounts allowed', 'Interest charged to customers',
          'Refunds to customers'],
    'a': 2,
    'w': 'A discount allowed reduces the amount the customer must pay, so it reduces the '
         'receivable and is credited. The other four all increase what customers owe.',
    'src': 'Chapter 5.2', 'sec': '5.2'},
   {'q': 'A cash book shows a balance of ₦840,000. Bank charges of ₦25,000 and a standing order '
         'of ₦60,000 have not been entered; unpresented cheques total ₦180,000. The balance to '
         'appear in the statement of financial position is',
    'o': ['₦840,000', '₦755,000', '₦935,000', '₦575,000', '₦660,000'],
    'a': 1,
    'w': 'Only the cash-book adjustments affect the reported figure. Unpresented cheques are a '
         'timing difference and belong in the reconciliation statement, not the cash book.',
    'calc': '840{,}000 - 25{,}000 - 60{,}000 = 755{,}000',
    'src': 'Chapter 5.7', 'sec': '5.7'},
   {'q': 'A contra entry between the receivables and payables ledgers is recorded as',
    'o': ['Dr Receivables control, Cr Payables control',
          'Dr Payables control, Cr Receivables control',
          'Dr Payables control, Cr Cash',
          'Dr Receivables control, Cr Sales',
          'Dr Purchases, Cr Payables control'],
    'a': 1,
    'w': 'A set-off reduces both balances: the amount the customer owes us is cancelled against '
         'the amount we owe the same party as a supplier. Debit payables, credit receivables.',
    'src': 'Chapter 5.2', 'sec': '5.2'},
   {'q': 'The bank statement shows ₦3,400,000. Unpresented cheques are ₦520,000 and uncredited '
         'lodgements ₦270,000. The corrected cash book balance is',
    'o': ['₦3,150,000', '₦3,650,000', '₦2,610,000', '₦4,190,000', '₦3,400,000'],
    'a': 0,
    'w': 'Add what the bank has not yet credited and deduct what it has not yet paid out.',
    'calc': '3{,}400{,}000 + 270{,}000 - 520{,}000 = 3{,}150{,}000',
    'src': 'Chapter 5.7', 'sec': '5.7'},
   {'q': 'Which of the following would NOT cause the receivables control account to disagree '
         'with the total of the individual receivables balances?',
    'o': ['The sales day book was undercast',
          'A receipt was posted to the wrong customer',
          'A balance was omitted from the list of individual balances',
          'An invoice was posted twice in the receivables ledger',
          'A bad debt was written off in the control account only'],
    'a': 1,
    'w': 'Posting to the wrong customer is an error of commission: the total of the individual '
         'balances is unchanged, so the control account still agrees. Only a statement sent to '
         'the customer will find it.',
    'src': 'Chapter 5.4', 'sec': '5.4'},
  ],
  'theory': [
   {'q': 'Explain FIVE reasons why the balance in the cash book may differ from the balance shown '
         'on the bank statement.',
    'marks': 5,
    'a': [{'ol': [
      '**Unpresented cheques** — cheques drawn and entered in the cash book but not yet presented '
      'for payment, so the bank has not yet reduced the balance.',
      '**Uncredited lodgements** — cash and cheques paid in and entered in the cash book but not '
      'yet cleared and credited by the bank.',
      '**Bank charges and interest** — debited by the bank and known to it, but not notified to '
      'the business until the statement arrives.',
      '**Standing orders and direct debits** — paid by the bank under a standing instruction and '
      'easily overlooked in the cash book.',
      '**Direct credits** — amounts paid into the account by customers without notification, '
      'including credit transfers and dividends.',
      '**Dishonoured cheques** — a cheque previously entered as received has bounced, so the bank '
      'has reversed it.',
      '**Errors** — in the cash book (corrected in the cash book) or by the bank (corrected in '
      'the reconciliation statement).']},
      {'note': 'The examiner usually wants the classification as well: the first two and any bank '
               'error are timing differences dealt with in the reconciliation statement; the rest '
               'require the cash book to be updated.'}],
    'src': 'Chapter 5.7', 'sec': '5.7'},
   {'q': 'State FOUR uses of control accounts and explain why a control account that agrees with '
         'the list of balances does not guarantee that the ledger is free from error.',
    'marks': 6,
    'a': [
      {'h4': 'Uses'},
      {'ol': [
        'They provide an instant total of receivables or payables for the financial statements '
        'without extracting every individual balance.',
        'They localise errors: if the control account disagrees with the list of balances, the '
        'error lies in that ledger and nowhere else.',
        'They act as an internal check, because the control account is written up by someone '
        'other than the ledger clerk, from independent day book totals.',
        'They deter and help detect fraud, since a clerk cannot conceal a misappropriation '
        'without also altering the control account.',
        'They allow the financial statements to be prepared before every individual account has '
        'been agreed.']},
      {'h4': 'Why agreement is not proof'},
      {'p': 'The control account is built from **totals**. Any error that leaves the total '
            'unchanged will not be revealed — most importantly an **error of commission**, where '
            'an entry is posted to the wrong customer\'s account. Both records then agree while '
            'both are wrong. Compensating errors within the ledger, and the complete omission of '
            'a transaction from both the day book and the individual account, are equally '
            'invisible. Only sending statements to customers will find these.'}],
    'src': 'Chapter 5.1', 'sec': '5.1'},
  ]},
}
