CH = {
 'n': 8,
 't': 'Vouchers and Their Classification',
 'brief': 'The types of voucher used in government accounting, the contents of a payment '
          'voucher, the registers in which vouchers are recorded, the treatment of a lost '
          'voucher, and the rules on custody and retention.',
 'outcomes': [
   'Define a voucher and state its purpose',
   'Classify vouchers into payment, receipt, adjustment and journal vouchers',
   'List the contents of a properly completed payment voucher',
   'Describe the flow of a payment voucher through the accounts department',
   'State the registers in which vouchers are recorded',
   'Explain the procedure where a voucher is lost',
 ],
 'secs': [
  {'n': '8.1', 't': 'Nature and purpose', 'b': [
    {'def': {'t': 'Voucher',
             'd': 'A document that evidences a transaction and authorises its entry in the '
                  'books of account. Every payment out of public funds and every receipt into '
                  'them must be supported by a voucher, and no entry may be made in the '
                  'accounts without one.'}},
    {'h4': 'Purposes'},
    {'ul': [
      'To **evidence** that a transaction actually took place and that value was received.',
      'To **authorise** the payment or the accounting entry — the voucher carries the signature '
      'of the officer empowered to approve it.',
      'To **classify** the transaction to the correct head, subhead and economic code, so that '
      'it is charged to the right vote.',
      'To provide the **audit trail** connecting the ledger entry to the underlying documents.',
      'To fix **responsibility**, since the officers who prepared, checked, authorised and paid '
      'are all identified on the face of it.',
    ]},
  ]},

  {'n': '8.2', 't': 'Classification of vouchers', 'b': [
    {'table': {'align': 'lll', 'head': ['Type', 'Purpose', 'Effect on the accounts'], 'rows': [
      ['**Payment voucher (PV)**',
       'Authorises and records a payment out of public funds — salaries, contractors, '
       'suppliers, advances',
       'Credit cash or bank; debit the relevant expenditure or asset head'],
      ['**Receipt voucher (RV)**',
       'Records money received into public funds where no treasury receipt is issued to a payer '
       '— for example a transfer from another government office, or a refund',
       'Debit cash or bank; credit the relevant revenue head'],
      ['**Adjustment voucher (AV)**',
       'Corrects an error of classification — a payment charged to the wrong head or subhead',
       'Debit the correct head; credit the head wrongly charged'],
      ['**Journal voucher (JV)**',
       'Records transactions that do not involve the movement of cash — depreciation, accruals, '
       'transfers between funds, write-off of losses',
       'As dictated by the entry; no cash movement'],
    ]}},
    {'p': 'Vouchers are further described by the stage they have reached: an **unpaid voucher** '
          'awaits payment; a **paid voucher** has been settled and is filed as evidence; an '
          '**outstanding voucher** was raised but not paid by the year end; and a **duplicate '
          'voucher** is a certified copy raised where the original is lost.'},
    {'warn': 'An **adjustment voucher** corrects a classification error only; it does not create '
             'or extinguish a liability. Using an adjustment voucher to record a genuine new '
             'transaction, or to move an over-expenditure quietly to a head with a balance, is a '
             'financial irregularity and is the sort of thing an auditor looks for.'},
  ]},

  {'n': '8.3', 't': 'Contents of a payment voucher', 'b': [
    {'p': 'The Financial Regulations prescribe the particulars a payment voucher must carry. A '
          'voucher missing any of them is not a valid authority to pay.'},
    {'ol': [
      'The **serial number** of the voucher and the date.',
      'The **name of the ministry, department or agency** and the station.',
      'The **head, subhead and economic code** to which the expenditure is chargeable.',
      'The **name and address of the payee**, and the bank account details where payment is by '
      'transfer.',
      'The **full particulars of the service or goods** — quantity, rate, description, period '
      'covered — sufficient for the charge to be checked without reference to other documents.',
      'The **amount in figures and in words**.',
      'The **supporting documents** attached: local purchase order, invoice, store receipt '
      'voucher, certificate of completion, contract agreement, nominal roll.',
      'The **certification** by the officer who checked the arithmetic and the classification.',
      'The **certificate of the accounting officer** or officer authorised on his behalf, that '
      'the service has been performed, the rates are correct and the charge is a proper charge '
      'on the vote.',
      'The **authority for the payment** — the warrant, contract or approval relied on.',
      'The **payee\'s receipt or acknowledgement**, and the officer\'s certificate of payment.',
      'The **stamp "PAID"** with the date, applied immediately on payment.',
    ]},
    {'key': 'The two certificates matter most. The **certifying officer** vouches that the '
            'service was performed and the rate correct; the **authorising officer** vouches '
            'that the charge is a proper charge against the vote and that funds remain. '
            'Separating those two functions from the officer who makes the payment is the basic '
            'internal control over expenditure.'},
  ]},

  {'n': '8.4', 't': 'The flow of a payment voucher', 'b': [
    {'steps': [
      'The **user department** raises a requisition and, where goods or services are required, '
      'a local purchase order or contract is issued after the procurement process.',
      'On delivery, the store receives the goods and issues a **store receipt voucher**; or the '
      'work is inspected and a **certificate of completion** issued.',
      'The **payment voucher is prepared** by the accounts section, classified to the correct '
      'head and subhead, and the supporting documents attached.',
      'The vote book is examined and the amount **charged to the vote**; if the uncommitted '
      'balance is insufficient the voucher cannot proceed.',
      'The voucher is **pre-audited** internally: arithmetic, classification, supporting '
      'documents, and compliance with the Financial Regulations.',
      'The voucher is **certified and authorised** by the officers empowered to do so.',
      'Payment is made — by mandate to the bank under the Treasury Single Account arrangement '
      '— and the voucher is **stamped "PAID"** and dated.',
      'The voucher is **entered in the cash book** and posted to the ledger, and recorded in '
      'the Register of Payment Vouchers.',
      'The paid voucher is **filed in serial order** and retained for the prescribed period, '
      'available for audit.',
    ]},
  ]},

  {'n': '8.5', 't': 'Registers', 'b': [
    {'table': {'align': 'll', 'head': ['Register', 'Purpose'], 'rows': [
      ['**Register of Payment Vouchers**',
       'Records every payment voucher in serial order — number, date, payee, amount, head and '
       'subhead. Establishes completeness and locates any voucher'],
      ['**Register of Receipts (Revenue Collectors\' Register)**',
       'Records receipt books issued to collectors and their return, so that every receipt form '
       'is accounted for'],
      ['**Register of Bill / Cheque Payments (Payment Mandate Register)**',
       'Records mandates issued to the bank, so that payments can be reconciled with the bank '
       'statement'],
      ['**Register of Losses**',
       'Records every loss of cash or stores, the officer responsible, the investigation and '
       'its outcome'],
      ['**Register of Unclaimed / Outstanding Vouchers**',
       'Records vouchers passed for payment but not yet settled'],
      ['**Vote book (DVEA)**',
       'Records commitments and expenditure against each subhead and shows the uncommitted '
       'balance'],
      ['**Register of Advances and Deposits**',
       'Records advances made to officers and deposits received, and their clearance'],
    ]}},
  ]},

  {'n': '8.6', 't': 'Loss of a voucher and custody', 'b': [
    {'h4': 'Where a voucher is lost'},
    {'p': 'Loss of a paid voucher is a serious matter, because the evidence supporting a payment '
          'out of public funds has disappeared. The Financial Regulations prescribe the '
          'following procedure.'},
    {'ol': [
      'The loss is **reported immediately** to the accounting officer, who reports it to the '
      'Accountant-General and the Auditor-General.',
      'A **thorough search** is made and the circumstances of the loss investigated.',
      'A **duplicate copy** is obtained — from the payee, from the file copy, or reconstructed '
      'from the records — and marked clearly as a **certified true copy** of the original.',
      'The duplicate is **certified by the accounting officer**, who states that the original '
      'has been lost, that the payment was properly made, that the service was performed, and '
      'that to the best of his knowledge no double payment has occurred or will occur.',
      'A **certificate of non-payment** is obtained where appropriate, confirming that the '
      'payment has not been made twice.',
      'The circumstances are **recorded in the Register of Losses**, and where negligence is '
      'established the officer responsible may be **surcharged** or otherwise disciplined.',
    ]},
    {'h4': 'Custody and retention'},
    {'ul': [
      'Paid vouchers are filed in **serial order** in a secure place under the control of a '
      'named officer.',
      'They must be produced to the internal auditor and the Auditor-General on demand and may '
      'not be released to any other person without authority.',
      'They are retained for the period prescribed in the Financial Regulations — generally not '
      'less than **five years**, and longer where litigation, an unresolved audit query or an '
      'investigation is outstanding.',
      'Vouchers may not be destroyed without the **written approval of the Auditor-General**.',
      'Unused voucher and receipt forms are treated as **security documents**, held under lock '
      'and issued against signature in a register.',
    ]},
    {'note': 'The examinable principle is that a lost voucher is never simply replaced. The '
             'duplicate is certified, the loss is reported to both the Accountant-General and '
             'the Auditor-General, and it is entered in the Register of Losses — because the '
             'possibility of a fraudulent second payment must be positively excluded.'},
  ]},
 ],
 'formulas': [],
 'focus':
   'One or two Section A marks most diets on the types of voucher or the contents of a payment '
   'voucher. In Section B it appears as "state the contents of a payment voucher and the '
   'procedure where one is lost", which is straightforward recall. Learn the contents as a '
   'numbered list of about ten and the loss procedure as six steps.',
 'errors': [
   'Confusing an adjustment voucher (corrects a misclassification) with a journal voucher '
   '(records a non-cash transaction).',
   'Omitting the head, subhead and economic code from the contents of a payment voucher — the '
   'classification is the point of the document.',
   'Saying a lost voucher is simply replaced by a photocopy, without certification or report.',
   'Failing to mention that destruction of vouchers requires the Auditor-General\'s written '
   'approval.',
   'Listing only payment and receipt vouchers when four types are examinable.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A voucher used to correct an expenditure charged to the wrong head or subhead is a',
    'o': ['payment voucher', 'adjustment voucher', 'receipt voucher', 'journal voucher',
          'duplicate voucher'],
    'a': 1,
    'w': 'The adjustment voucher moves the charge from the head wrongly debited to the correct '
         'one. It does not create or discharge a liability.',
    'src': 'Chapter 8.2'},
   {'q': 'Vouchers may not be destroyed without the written approval of the',
    'o': ['Accountant-General', 'Auditor-General', 'Minister of Finance',
          'accounting officer', 'internal auditor'],
    'a': 1,
    'w': 'Destruction would remove audit evidence, so it requires the approval of the officer '
         'who must rely on it.',
    'src': 'Chapter 8.6'},
   {'q': 'A voucher recording a transaction that does not involve any movement of cash — such '
         'as depreciation or a transfer between funds — is a',
    'o': ['receipt voucher', 'journal voucher', 'adjustment voucher', 'payment voucher',
          'store receipt voucher'],
    'a': 1,
    'w': 'The journal voucher records non-cash entries; the adjustment voucher is the special '
         'case of correcting a misclassification.',
    'src': 'Chapter 8.2'},
   {'q': 'Immediately a payment voucher is settled it should be',
    'o': ['filed unmarked', 'stamped "PAID" and dated', 'returned to the payee',
          'entered in the Register of Losses', 'sent to the Auditor-General'],
    'a': 1,
    'w': 'Stamping prevents the same voucher being presented a second time for payment.',
    'src': 'Chapter 8.4'},
   {'q': 'Where a paid voucher is lost, the duplicate obtained must be certified by the',
    'o': ['payee', 'accounting officer', 'internal auditor', 'Auditor-General',
          'Accountant-General'],
    'a': 1,
    'w': 'The accounting officer certifies that the original is lost, that the payment was '
         'properly made and that no double payment has occurred, and reports the loss to both '
         'the Accountant-General and the Auditor-General.',
    'src': 'Chapter 8.6'},
  ],
  'theory': [
   {'q': '(a) Define a voucher and state five purposes it serves in government accounting. '
         '(b) List ten items that a properly completed payment voucher should contain. '
         '(c) Describe the procedure to be followed where a paid voucher is lost.',
    'marks': 15,
    'a': [
      {'h4': '(a) Definition and purposes'},
      {'p': 'A voucher is a document evidencing a transaction and authorising its entry in the '
            'books of account. Every payment out of public funds and every receipt into them '
            'must be supported by a voucher, and no entry may be made in the accounts without '
            'one.'},
      {'p': '**Purposes**'},
      {'ol': [
        '**Evidence.** It proves that the transaction took place and that value was received '
        'for the money paid.',
        '**Authorisation.** It carries the signature of the officer empowered to approve the '
        'payment, so that no money leaves the treasury without proper authority.',
        '**Classification.** It states the head, subhead and economic code to which the '
        'transaction is chargeable, ensuring the correct vote is charged and the accounts '
        'correctly analysed.',
        '**Audit trail.** It links the entry in the cash book and ledger to the underlying '
        'invoice, order, store receipt and certificate of completion, so that an auditor can '
        'trace a figure to its source.',
        '**Fixing responsibility.** The officers who prepared, checked, certified, authorised '
        'and paid are each identified on the face of the voucher, so that liability can be '
        'established if the payment proves improper.',
        '**Budgetary control.** The voucher is the instrument by which the charge reaches the '
        'vote book, where it reduces the uncommitted balance.',
      ]},
      {'h4': '(b) Contents of a payment voucher'},
      {'ol': [
        'Serial number and date of the voucher.',
        'Name of the ministry, department or agency, and the station.',
        'The head, subhead and economic code to which the expenditure is chargeable.',
        'Name and address of the payee, with bank account details where payment is by transfer.',
        'Full particulars of the goods or services — description, quantity, rate and period '
        'covered — sufficient for the charge to be verified without reference to other '
        'documents.',
        'The amount, in both figures and words.',
        'A list of the supporting documents attached: local purchase order, invoice, store '
        'receipt voucher, certificate of job completion, contract agreement or nominal roll.',
        'The certificate of the checking officer as to arithmetical accuracy and correct '
        'classification.',
        'The certificate of the accounting officer, or an officer authorised on his behalf, '
        'that the service has been performed, the rates are correct and the charge is a proper '
        'charge on the vote.',
        'The authority for the payment — warrant, contract, approval or regulation relied upon.',
        'The payee\'s receipt or acknowledgement of the money.',
        'The "PAID" stamp with the date of payment.',
      ]},
      {'h4': '(c) Procedure on loss of a paid voucher'},
      {'p': 'The loss of a paid voucher removes the evidence supporting a payment already made '
            'out of public funds, and creates the risk that the same claim may be presented '
            'again. The Financial Regulations therefore prescribe a formal procedure.'},
      {'ol': [
        '**Immediate report.** The officer discovering the loss reports it at once to the '
        'accounting officer, who in turn reports it to the Accountant-General of the Federation '
        'and to the Auditor-General for the Federation.',
        '**Search and investigation.** A thorough search is conducted and the circumstances of '
        'the loss investigated, to establish whether it arose from negligence, from a defect in '
        'the filing system, or from an attempt to conceal an irregularity.',
        '**Obtain a duplicate.** A duplicate is obtained from the payee, from the departmental '
        'file copy, or reconstructed from the cash book, vote book and supporting documents. It '
        'is marked clearly as a certified true copy of the original.',
        '**Certification.** The accounting officer certifies on the duplicate that the original '
        'has been lost, that the payment was properly made and the service performed, that the '
        'charge was correctly classified, and that to the best of his knowledge and belief no '
        'double payment has been or will be made.',
        '**Certificate of non-payment.** Where appropriate, confirmation is obtained from the '
        'payee and from the bank that the sum has been received once only.',
        '**Record and sanction.** The loss is recorded in the Register of Losses with full '
        'particulars. Where negligence on the part of an officer is established, he may be '
        'surcharged with any resulting loss and is liable to disciplinary action; where fraud '
        'is suspected the matter is referred for investigation and possible prosecution.',
      ]},
      {'note': 'The reason for this weight of procedure is that a missing voucher is the '
               'classic cover for a fraudulent duplicate payment. The requirement to report to '
               'the Auditor-General ensures the matter is examined by someone outside the '
               'department in which the loss occurred.'}],
    'src': 'Chapter 8.3, 8.6'},
  ]},
}
