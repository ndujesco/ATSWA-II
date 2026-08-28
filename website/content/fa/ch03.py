CH = {
 'n': 3,
 't': 'The Accounting Equation, Double Entry and Books of Prime Entry',
 'brief': 'The mechanics: how the equation stays balanced, which account is debited, which book '
          'a transaction enters first, the sixteen source documents that stand behind every entry, '
          'the journal and the seven jobs it does, and how to find and fix the errors a trial '
          'balance hides — all worked through the study text\'s own running illustrations, '
          'corrected where its own arithmetic slips.',
 'outcomes': [
   'Apply the accounting equation to analyse the impact of a transaction',
   'Understand the double-entry system and apply it to record transactions',
   'Balance ledger accounts and extract a trial balance',
   'Identify the purpose of the trial balance, and what it does and does not prove',
   'Identify the purpose of source documents, and explain each of the sixteen types',
   'Describe the different books of prime entry',
   'Record transactions in the sales day book, purchases day book and the returns day books',
   'Explain the use of the petty cash book and the imprest system, and list the internal '
   'controls over petty cash',
   'Explain the uses of the journal, post to it, and explain narrations',
   'State how to post from the journal to the ledger',
   'Correct errors through the journal and clear a suspense account',
   'Explain the chart of accounts and its purpose',
 ],
 'secs': [
  {'n': '3.1', 't': 'The accounting equation, and the entity concept behind it', 'b': [
    {'p': 'Bookkeeping, in the study text\'s own words, is a sequence of four steps: a '
          '**transaction takes place**; a **source document** is obtained as evidence of it; the '
          'transaction is recorded in a **book of prime entry**; and it is then recorded in the '
          '**ledger accounts**. Everything in this chapter is one of those four steps, in that '
          'order — which is also the order the sections below follow.'},
    {'p': 'The whole of double-entry bookkeeping rests on the **entity concept** (met already in '
          'Chapter 1 §1.6): the business is a unit distinct from its owner, applied universally to '
          'sole traders, partnerships, companies, governments and not-for-profit organisations '
          'alike. This has a very concrete consequence for recording transactions — when an owner '
          'invests cash into their business, that cash is **capital**; when an owner borrows money '
          '*for business purposes*, the amount borrowed is recorded as a **liability**, not as the '
          'owner\'s own money, precisely because the business and the owner are kept separate.'},
    {'tex': '\\text{Assets} = \\text{Capital} + \\text{Liabilities}', 'tag': '(3.1)'},
    {'p': 'These are the same three elements of the statement of financial position met in '
          'Chapter 1: **assets** are resources, while **capital** and **liabilities** are claims '
          'to those resources.'},
    {'h3': 'Classifying assets and liabilities'},
    {'table': {'head': ['', 'Non-current', 'Current'], 'align': 'lll', 'rows': [
      ['**Assets**', 'Held for use in the operations of the business — not held for resale. '
       'Examples: property, machinery, patent rights.', 'Inventory (goods manufactured or '
       'purchased for resale); trade receivables (money owed by customers who bought on credit); '
       'and cash.'],
      ['**Liabilities**', 'Payable more than 12 months after the reporting date. Examples: loans, '
       'long-term bonds.', 'Payable within 12 months of the reporting date. Examples: trade '
       'payables, tax payables, bank overdraft.'],
    ]}},
    {'def': {'t': 'Equity', 'd': 'the residual interest in the entity\'s assets after deducting '
                  'its liabilities. Capital is the clearest example of equity — it is, in effect, '
                  'a form of liability due to the *owner* of the business (the entity concept '
                  'again), and it grows year on year with the profit that is earned and retained.'}},
    {'key': 'In accounting, **every transaction that takes place affects the financial statements '
            'in two ways**. At any point in time, the assets of the business will equal the capital '
            'and liabilities of the business. This is called the **dual effect**, and it is the '
            'reason double-entry bookkeeping works at all — see §3.2.'},
    {'h3': 'Illustration 3.1 — tracking the equation through thirteen transactions'},
    {'p': 'Omoaji sets up a business selling cosmetics. The study text runs thirteen transactions '
          'through the accounting equation one at a time; the running table below carries every '
          'transaction through to a final balance (figures in ₦\'000, matching the source).'},
    {'ol': [
      'Omoaji puts ₦6,000,000 into the business bank account.',
      'Omoaji borrows ₦8,000,000 from his brother for the business.',
      'Omoaji buys a motor van with the money borrowed from his brother.',
      'Omoaji buys a market stall and pays ₦1,000,000 in cash.',
      'Omoaji buys cosmetics for ₦3,600,000 on credit.',
      'Omoaji pays ₦2,000,000 to his suppliers for some of the cosmetics purchased.',
      'Omoaji sells 50% of the cosmetics (cost = ₦1,800,000) for ₦2,400,000 in cash.',
      'Omoaji sells cosmetics costing ₦1,000,000, to a shop owner in another town, for '
      '₦1,800,000 on one month\'s credit.',
      'Omoaji repays ₦2,000,000 of the loan.',
      'Omoaji pays his trade suppliers ₦1,200,000.',
      'Omoaji receives ₦1,600,000 of the money owed to him by the customer in (8).',
      'Omoaji purchases another ₦500,000 of cosmetics, on credit.',
      'Omoaji takes ₦800,000 cash out of the business, and also takes inventory worth ₦400,000.',
    ]},
    {'warn': 'The source text\'s own running table for this illustration is badly garbled across '
             'two page images — rows and columns fall out of alignment and several figures are '
             'unreadable as printed. Rather than reproduce that confusion, the table below has '
             'been rebuilt from the study text\'s own **explanatory notes for each transaction**, '
             'which are unambiguous and are transcribed exactly as given.'},
    {'table': {'cap': 'Effect of each transaction on the equation (₦)', 'align': 'lrl',
     'head': ['Txn', 'Effect', 'Why the equation stays balanced'], 'rows': [
      ['(1)', 'Cash +6,000,000; Capital +6,000,000', 'Both sides rise by the same amount'],
      ['(2)', 'Cash +8,000,000; Loan (liability) +8,000,000', 'Both sides rise by the same amount'],
      ['(3)', 'Motor van +8,000,000; Cash −8,000,000', 'One asset swaps for another — total '
       'assets unchanged'],
      ['(4)', 'Stall +1,000,000; Cash −1,000,000', 'The business used one asset (cash) to acquire '
       'a different asset (a stall); no change in total assets, only in their make-up'],
      ['(5)', 'Inventory +3,600,000; Payables (liability) +3,600,000', 'The business acquired '
       'more assets and, in doing so, created a liability to the supplier — both sides rise '
       'equally'],
      ['(6)', 'Cash −2,000,000; Payables −2,000,000', 'The payment reduces the liability, and '
       'reduces cash by the same amount'],
      ['(7)', 'Cash +2,400,000; Inventory −1,800,000; Capital +600,000', 'The business sold '
       'assets that cost ₦1,800,000 for ₦2,400,000 cash; the ₦600,000 difference is profit, and '
       'profit is added to capital'],
      ['(8)', 'Inventory −1,000,000; Receivables (asset) +1,800,000; Capital +800,000', 'The sale '
       'was on credit, so cash is unaffected; the ₦800,000 profit still increases capital, and the '
       'business is now owed ₦1,800,000 by the customer — an asset called a trade receivable'],
      ['(9)', 'Cash −2,000,000; Loan −2,000,000', 'The loan repayment reduces both an asset and a '
       'liability by the same amount'],
      ['(10)', 'Cash −1,200,000; Payables −1,200,000', 'Paying trade suppliers reduces assets and '
       'liabilities equally'],
      ['(11)', 'Cash +1,600,000; Receivables −1,600,000', 'Cash received from a customer swaps '
       'one asset (a receivable) for another (cash) — no effect on total assets'],
      ['(12)', 'Inventory +500,000; Payables +500,000', 'More assets acquired on credit; both '
       'sides rise equally'],
      ['(13)', 'Cash −800,000; Inventory −400,000; Capital −1,200,000', 'The owner has withdrawn '
       '₦800,000 cash and ₦400,000 of inventory — drawings, reducing assets and capital by the '
       'same ₦1,200,000 total'],
    ]}},
    {'h3': 'Drawings'},
    {'p': 'The owner (or owners) of a business can draw out the profits the business makes. If '
          'they wish, they could draw out all of it; in practice, owners usually draw some profit '
          'and retain the rest, to finance the growth of the business. **Profit that is kept in '
          'the business is called retained earnings. Profit that is drawn out is called drawings**, '
          'for a sole trader or a partnership — the equivalent payment to the shareholders of a '
          'company is called a **dividend**. Drawings are usually cash, but an owner might instead '
          'take inventory, or even a larger asset such as a motor vehicle, out of the business for '
          'personal use — taking inventory or another asset is just as much a drawing as taking '
          'cash (exactly transaction (13) above).'},
    {'key': 'The original capital of a business can only increase through **retained earnings** '
            '(profit minus drawings) plus any **additional capital** the owner brings in. Once '
            'additional capital is introduced, the accounting equation becomes:'},
    {'tex': '\\text{Assets} = \\text{Capital} + \\text{Additional capital} + \\text{Profit} - '
            '\\text{Drawings} + \\text{Liabilities}', 'tag': '(3.2)'},
    {'p': 'This is exactly the "expanded equation" already met as formula (3.3) in earlier '
          'editions of this guide, and it lets you derive a **missing figure** — most often the '
          'closing capital, or the profit for the period — whenever the other four are known.'},
    {'eg': {'t': 'The practice question the study text leaves unanswered', 'q': [
      {'p': 'Olayode operates a business as a sole trader. On 1 July 2024 the net assets of the '
            'business were ₦670,000. During the year to 30 June 2025 the business made a profit '
            'of ₦250,000 and Olayode took out ₦220,000 in drawings. Due to a shortage of cash in '
            'the business, he paid in additional capital of ₦40,000 in early June 2025. Calculate '
            'the net assets of the business at 30 June 2025.'}],
      'a': [
      {'warn': 'The study text sets this up as a "practice question" and then simply stops after '
               'writing "the net assets... can be calculated as follows:" — no working, and no '
               'answer, is ever given. The full solution is below.'},
      {'p': 'Net assets always equal capital (equation 3.1, since liabilities net off within '
            '"net assets"). So the movement in net assets over the year is exactly the movement '
            'in capital, using equation (3.2) above:'},
      {'stmt': {'t': 'Net assets at 30 June 2025', 'rows': [
        ['Net assets (capital) at 1 July 2024', 670000],
        ['Add: profit for the year', 250000],
        ['Add: additional capital introduced', 40000],
        ['Less: drawings', -220000],
        ['Net assets at 30 June 2025', 740000, '@tt'],
      ]}}]}},
  ]},

  {'n': '3.2', 't': 'Double-entry bookkeeping and the ledger', 'b': [
    {'p': 'Double-entry bookkeeping is a method that **maintains the balance of the accounting '
          'equation** by ensuring every transaction affects at least two accounts. When a '
          'transaction occurs, one account is debited and another is credited, keeping the '
          'equation in balance. For example, if a business purchases equipment (an asset) on '
          'credit (a liability), the asset account is **debited** (increased) and the liability '
          'account is **credited** (increased) — the equation stays balanced because both sides '
          'moved together.'},
    {'p': 'Accounts are kept in a **ledger** — a term meaning a collection of related accounts. '
          'All transactions are classified into different types and recorded in the relevant '
          'accounts. The accounts holding the double entries for each transaction are kept in the '
          '**general ledger**, also known as the **nominal ledger** or the **main ledger**. There '
          'is a ledger account for **each asset, liability, income and expense item**; each '
          'transaction touches at least two ledger accounts, one debited and one credited, and '
          '**which** account is debited depends on whether it is an asset, a liability, equity, '
          'income or an expense.'},
    {'table': {'head': ['Account type', 'Debit records', 'Credit records', 'Normal balance'],
     'align': 'llll', 'rows': [
      ['Asset', 'Increase', 'Decrease', 'Debit'],
      ['Expense', 'Increase', 'Decrease', 'Debit'],
      ['Drawings', 'Increase', 'Decrease', 'Debit'],
      ['Liability', 'Decrease', 'Increase', 'Credit'],
      ['Capital', 'Decrease', 'Increase', 'Credit'],
      ['Income', 'Decrease', 'Increase', 'Credit'],
    ]}},
    {'key': 'The mnemonic **DEAD CLIC**: **D**ebits increase **E**xpenses, **A**ssets, '
            '**D**rawings; **C**redits increase **L**iabilities, **I**ncome, **C**apital. '
            '**Recording cash:** when cash is received, cash increases — being an increase in an '
            'asset, the cash account is **debited** and the corresponding account is **credited**, '
            'with equal amounts. When cash is paid, cash reduces — being a decrease in an asset, '
            'the cash account is **credited** and the corresponding account is **debited**, with '
            'equal amounts.'},
    {'h3': 'Illustration 3.2 — a month of transactions posted straight to the ledger'},
    {'p': 'Morayo, a trader in Oshodi market, had the following transactions in January 2025: '
          'started business with ₦500,000 cash (1 Jan); purchased goods for cash ₦82,000 (3 Jan); '
          'cash sales of ₦150,000 (5 Jan); paid rent of ₦50,000 by cash (10 Jan); received '
          '₦80,000 cash as a loan from Mr Bello (15 Jan); purchased goods for ₦70,000 cash (20 '
          'Jan); and paid ₦30,000 electricity for office use (25 Jan).'},
    {'tacc': {'t': 'Cash', 'dr': [
        ['Capital', 500000], ['Sales', 150000], ['Loan', 80000], ['', 730000, '@tot']],
      'cr': [['Purchases', 82000], ['Rent', 50000], ['Purchases', 70000],
             ['Electricity', 30000], ['Balance c/d', 498000], ['', 730000, '@tot']]}},
    {'p': 'Each of the other five accounts simply carries the **one entry** that corresponds to '
          'the cash account: Capital is credited ₦500,000; Purchases is debited ₦82,000 and then '
          'a further ₦70,000 (₦152,000 in total); Sales is credited ₦150,000; Rent is debited '
          '₦50,000; the Loan account is credited ₦80,000; and Electricity is debited ₦30,000. '
          'Notice that **purchases and sales of goods for cash never touch a receivables or '
          'payables account at all** — the entire transaction is complete the moment cash '
          'changes hands.'},
    {'h3': 'Purchases and sales of goods on credit'},
    {'p': 'Where goods are purchased or sold **on credit**, rather than debiting or crediting '
          'cash, the **customer\'s account (a receivables account)** is debited for a credit sale, '
          'and the **supplier\'s account (a payables account)** is credited for a credit purchase.'},
    {'h3': 'Illustration 3.3 — a fuller month, mixing cash and credit'},
    {'p': 'Akufor Joe Enterprises started a retail business selling cement. On 1 March 2025 the '
          'owner introduced a motor van valued at ₦4,800,000, cash from his salary account of '
          '₦3,300,000, and money borrowed from a friend of ₦660,000. During March: cement was '
          'purchased on credit from Fola Ltd for ₦1,890,000 (3 March); carriage on that cement to '
          'the warehouse was paid, ₦164,560 (3 March); goods were sold on credit to Aburi & Co for '
          '₦1,900,000 (6 March); cement was sold for cash, ₦262,800 (8 March); sundry expenses of '
          '₦162,780 were paid (11 March); further cement was purchased on credit from Fola Ltd, '
          '₦600,000 (15 March); tyres were bought on credit from Okechukwu Enterprises for '
          '₦108,520 (17 March); ₦1,675,000 cash was paid to Fola Ltd on account (20 March); Aburi '
          '& Co paid ₦1,250,000 cash on account (22 March); salaries and wages of ₦779,580 were '
          'paid (25 March); the electricity bill of ₦60,000 was paid (25 March); and cement was '
          'sold on credit to K. Opobo for ₦680,000 (27 March).'},
    {'warn': 'Two things in the study text\'s own worked solution to this illustration are worth '
             'flagging before the figures below: the business is introduced as **"Mensa Joe '
             'Enterprises"** in the question but the solution is headed **"Akufor Joe '
             'Enterprises"** — clearly the same business under two different names, a simple slip. '
             'And the Cash account\'s opening capital contribution is printed as **"₦330,000"**, '
             'which cannot be right — the introduction explicitly states ₦3,300,000 cash was '
             'brought in, and every total in the accounts below only reconciles if ₦3,300,000 is '
             'used (a missing zero). Both are corrected below without further comment.'},
    {'tacc': {'t': 'Capital account', 'dr': [['Balance c/d', 8100000], ['', 8100000, '@tot']],
      'cr': [['Cash', 3300000], ['Motor vehicle', 4800000], ['', 8100000, '@tot'],
             ['Balance b/d', 8100000]]}},
    {'tacc': {'t': 'Cash account', 'dr': [
        ['Capital', 3300000], ['Loan', 660000], ['Sales', 262800], ['Aburi & Co', 1250000],
        ['', 5472800, '@tot'], ['Balance b/d', 2630880]],
      'cr': [['Carriage inwards', 164560], ['Sundry expenses', 162780], ['Fola Ltd', 1675000],
             ['Electricity bill', 60000], ['Salaries & wages', 779580],
             ['Balance c/d', 2630880], ['', 5472800, '@tot']]}},
    {'p': 'Every other account in the illustration carries the single corresponding entry: **loan '
          '₦660,000** (Cr, from the friend, matched by the Dr in cash above); **motor vehicle '
          '₦4,800,000** (Dr, matched by the Cr in capital); **carriage inwards ₦164,560** (Dr); '
          '**Aburi & Co**, a debtor, is debited ₦1,900,000 for the sale and credited ₦1,250,000 '
          'for cash received, leaving a **debit balance of ₦650,000**; **Fola Ltd**, a creditor, '
          'is credited ₦1,890,000 and ₦600,000 for the two purchases (₦2,490,000 in total) and '
          'debited ₦1,675,000 for the cash paid, leaving a **credit balance of ₦815,000**; '
          '**sundry expenses ₦162,780** (Dr); **motor van expenses ₦108,520** (Dr, matched by a '
          '₦108,520 **credit balance** on Okechukwu Enterprises, a creditor); **salaries and '
          'wages ₦779,580** (Dr); **electricity bill ₦60,000** (Dr); **purchases ₦2,490,000** '
          '(Dr, the ₦1,890,000 and ₦600,000 from Fola Ltd combined); **sales ₦2,842,800** (Cr, '
          'being ₦1,900,000 from Aburi & Co, plus ₦262,800 cash sales, plus ₦680,000 from K. '
          'Opobo); and **K. Opobo**, a debtor, is debited ₦680,000.'},
    {'h3': 'Illustration 3.4 — drawing up the trial balance'},
    {'p': 'Once every ledger account above has been balanced, the closing balances are listed in '
          'a trial balance: assets\' accounts and expense accounts carry **debit** balances, '
          'liabilities\' accounts and income accounts carry **credit** balances, and the capital '
          'account carries a **credit** balance.'},
    {'stmt': {'t': 'Akufor Joe Enterprises — Trial Balance at 31 March 2025', 'rows': [
      ['Capital', '', -8100000],
      ['Loan', '', -660000],
      ['Cash', 2630880, ''],
      ['Motor vehicle', 4800000, ''],
      ['Carriage inwards', 164560, ''],
      ['Debtor — Aburi & Co', 650000, ''],
      ['Creditor — Fola Ltd', '', -815000],
      ['Sundry expenses', 162780, ''],
      ['Motor van expenses', 108520, ''],
      ['Salaries and wages', 779580, ''],
      ['Electricity bill', 60000, ''],
      ['Purchases', 2490000, ''],
      ['Sales', '', -2842800],
      ['Creditor — Okechukwu Enterprises (accounts payable)', '', -108520],
      ['Debtor — K. Opobo', 680000, ''],
      ['Totals', 12526320, -12526320, '@tt'],
    ]}},
    {'note': 'Three points the study text makes explicitly about this illustration: the balance '
             'carried down (c/d) at the end of one period becomes the balance brought down (b/d) '
             'at the start of the next; all **assets\'** accounts (cash, motor vehicle, debtors) '
             'carry debit balances, all **liabilities\'** accounts (loan, creditors) carry credit '
             'balances, and the **capital** account carries a credit balance; and — importantly — '
             'in this illustration transactions were posted **directly** to the ledger accounts '
             'to keep the example short. In real practice, every transaction would first pass '
             'through a **book of prime entry** (§3.4 below) before ever reaching the ledger.'},
  ]},

  {'n': '3.3', 't': 'Source documents', 'b': [
    {'p': 'Source documents perform six functions: they serve as **evidence** of financial '
          'transactions, thereby guarding against fraud; they provide the **basis for recording** '
          'transactions in the accounting records; they facilitate **auditing and verification**; '
          'they **support financial statements and tax returns**; where more than one source '
          'document exists for a transaction, they **complement each other**; and they are usually '
          '**signed by the parties** to the transaction, which makes them difficult to alter or '
          'deface.'},
    {'p': 'The study text describes **sixteen** types of source document in detail — far more '
          'than most study guides bother to list. Each is transcribed below, with its key details '
          'and who it typically goes to.'},
    {'table': {'head': ['Document', 'What it is', 'Typically distributed to'], 'align': 'lll',
     'rows': [
      ['**Purchases invoice**', 'Received from a supplier, requesting payment. Shows supplier '
       'information, invoice date and number, description of goods/services, quantity and unit '
       'price, total cost, payment terms. Cross-checked with the delivery note and purchase '
       'order.', 'Accounting, procurement, inventory management, finance departments'],
      ['**Sales invoice**', 'Sent to a customer, requesting payment for goods sold. Shows '
       'customer information, invoice date and number, description of goods/services sold, '
       'quantity and unit price, total amount due, payment terms. Serves revenue recognition, '
       'receivables management and cash flow tracking; checked against the purchase order and '
       'delivery note.', 'The customer, accounting department, sales team, finance department'],
      ['**Purchase order**', 'Issued by a buyer, authorising a supplier to deliver a specified '
       'quantity of goods. Shows the goods/services, quantity and description, unit price and '
       'total cost, delivery terms, payment terms. A formal agreement between buyer and supplier; '
       'checked against the invoice and quotation.', 'Supplier, procurement, accounting, '
       'inventory management'],
      ['**Quotation**', 'Provided by a supplier or vendor, outlining prices and terms of goods. '
       'Shows description, price and pricing details, terms and conditions, validity period. '
       'Helps purchasing decisions; checked against the purchase requisition or order.',
       'Potential customer, procurement department, sales team'],
      ['**Delivery note**', 'Accompanies goods being delivered to a customer. Shows description '
       'of goods delivered, quantity delivered, delivery address, order/reference numbers. Proof '
       'of delivery; checked with the goods received and the purchase order.', 'Customer, '
       'delivery team, warehouse/inventory management, accounting (for verification)'],
      ['**Goods received note (GRN)**', 'Proof of the receipt of goods from a supplier. Shows '
       'description and quantity received, date and time of receipt, supplier information, order/'
       'reference numbers. Helps verify shipment contents, update inventory, process payments.',
       'Procurement, inventory management, accounting, warehouse'],
      ['**Supplier\'s statement**', 'Sent by a supplier, typically monthly, to reconcile the '
       'amount owing. Shows outstanding invoices, payments made, credits or debits applied, '
       'current balance owed. Checked against the buyer\'s own records of the supplier.',
       'Accounting, procurement, finance departments'],
      ['**Credit note**', 'Issued by a supplier to a buyer, indicating the buyer\'s account has '
       'been credited for goods returned or for being overcharged. Shows the amount credited, the '
       'reason (returns, refunds, errors), the original invoice details. Adjusts accounts '
       'payable; checked with documents relating to goods returned.', 'Buyer/accounting, '
       'procurement, finance'],
      ['**Debit note**', 'Issued by a supplier to a buyer, indicating the amount due from the '
       'customer has been increased. Shows the amount debited and the reason (additional charges, '
       'fees, corrections). Adjusts accounts payable and reflects additional charges.',
       'Buyer/accounting, procurement, finance'],
      ['**Remittance advice**', 'Sent by a buyer to a supplier, as notification of payment. Shows '
       'payment details (amount, date, method), invoice/reference numbers being paid, any '
       'deductions or adjustments. Checked against the invoice.', 'Supplier/accounts receivable, '
       'buyer\'s accounting department'],
      ['**Receipt**', 'Issued to a buyer, confirming an amount received for goods sold or a '
       'service rendered. Shows amount received, date and method of payment, description of '
       'goods/services paid for. Compared with the invoice.', 'Customer, accounting department, '
       'sales team'],
      ['**Payment voucher**', 'Supports a payment transaction. Shows payment amount, payee '
       'information, payment method, date and description, details of the authorising officer.',
       'Accounting, finance, accounts payable'],
      ['**Bank pay-in-slip**', 'Used to deposit funds into a bank account. Shows the account '
       'holder\'s information, deposit amount, date, description of deposit (cash, cheque).',
       'Businesses, individuals, accounting/finance departments'],
      ['**Cheque counterfoil**', 'The stub or duplicate portion of a cheque, remaining in the '
       'cheque book after a cheque is written. Shows cheque number, date, payee information, '
       'amount, and sometimes the running balance.', 'Retained by the drawer, for recording '
       'transactions, tracking cheque payments and reconciling accounts'],
      ['**Bank statement**', 'A record of all transactions in a specific period, typically a '
       'month; proof of financial transactions, used for reconciliations, auditing, loan '
       'applications and financial analysis. Shows transaction dates and descriptions, debit and '
       'credit amounts, running balance.', 'The account holder, accountants/bookkeepers (for '
       'reconciliation), auditors (during audits) — checked against the cash book or general '
       'ledger, company records, and cheques and payment records, to identify errors, '
       'unauthorised transactions or missing entries'],
      ['**Bin card**', 'Tracks inventory levels in a warehouse or storage area. Shows item '
       'description, quantity received, quantity issued, balance quantity, date and transaction '
       'details.', 'Warehouse/inventory management'],
    ]}},
    {'key': 'Of these sixteen, the study text singles out **seven** as the source documents that '
            'directly impact double-entry bookkeeping: the **invoice**, the **receipt**, '
            '**pay-in-slips**, **cheque counterfoils**, **credit notes**, **debit notes**, and the '
            '**bank statement**. The other nine (purchase order, quotation, delivery note, GRN, '
            'supplier\'s statement, payment voucher, bin card) support and evidence the process '
            'without themselves being posted into the double-entry system.'},
  ]},

  {'n': '3.4', 't': 'Books of prime entry', 'b': [
    {'def': {'t': 'Book of prime entry', 'd': 'the book in which a transaction is first recorded, '
                  'before being posted to the ledger accounts.'}},
    {'p': 'Books of prime entry share several features. Transactions are recorded in '
          '**chronological order**, as they occur. They serve as the **point of original entry**. '
          'Each transaction is recorded in **detail** — date, amount, and the parties involved. '
          'The books follow a **specific format**, with columns and headings tailored to the type '
          'of transaction being recorded. And each book of prime entry is designed to record '
          '**specific types** of transaction — sales, purchases, cash receipts, or cash payments — '
          'allowing organised and efficient recording.'},
    {'h3': 'The sales day book'},
    {'p': 'Records **credit sales** of goods or services, and helps track sales transactions and '
          'update trade receivables. Where VAT does not apply, a typical sales day book looks like '
          'this:'},
    {'table': {'head': ['Date', 'Invoice No.', 'Customer', 'Amount Invoiced (₦)'], 'align':
     'llrr', 'rows': [
      ['20 Jan 2024', '340', 'Jaredada', '250,000'],
      ['23 Jan 2024', '341', 'Taiwo Kehinde', '155,000'],
      ['25 Jan 2024', '342', 'Janet Paul', '140,000'],
      ['2 Feb 2024', '343', 'Samson Ajayi', '165,000'],
      ['Total', '', '', '710,000'],
    ]}},
    {'p': 'Where the entity maintains a control account, the day book total forms part of the '
          'double entry:'},
    {'pre': 'Dr  Receivables ledger control account   710,000\n    Cr  Sales                            710,000'},
    {'p': 'The **individual customer accounts** are then updated from each line of the day book: '
          'debit Jaredada ₦250,000, debit Taiwo Kehinde ₦155,000, debit Janet Paul ₦140,000, debit '
          'Samson Ajayi ₦165,000 (credit sales, as already established in §3.2). This gives a '
          'clear, organised record of credit sales, making them easy to track and manage.'},
    {'h4': 'The sales day book with VAT'},
    {'p': 'Where VAT applies (illustrated here at 7.5%), a VAT column is added, and the double '
          'entry has three legs instead of two:'},
    {'table': {'head': ['Date', 'Invoice No.', 'Customer', 'Sales Amount (₦)', 'VAT (₦)',
     'Total (₦)'], 'align': 'llrrrr', 'rows': [
      ['Feb 1', '001', 'John & Co', '1,000,000', '75,000', '1,150,000'],
      ['Feb 5', '002', 'Jane Ventures', '800,000', '60,000', '920,000'],
      ['Feb 10', '003', 'Uzairu Ltd', '1,200,000', '90,000', '1,380,000'],
      ['Feb 15', '004', 'Alhaji Nig. Ltd', '900,000', '67,500', '1,035,000'],
      ['Total', '', '', '3,900,000', '292,500', '4,192,500'],
    ]}},
    {'pre': 'Dr  Receivables ledger control account   4,192,500\n'
            '    Cr  VAT (output tax)                      292,500\n'
            '    Cr  Sales                                3,900,000'},
    {'note': 'The individual customer accounts are then updated with the VAT-inclusive amount '
             'each owes — the customer owes the gross figure, even though only the net figure is '
             'revenue to the business.'},
    {'h3': 'The purchases day book'},
    {'p': 'Records **credit purchases** of goods or services, and helps track purchase '
          'transactions and update accounts payable. It keeps a list of invoices received from '
          'suppliers.'},
    {'table': {'head': ['Date', 'Supplier', 'Amount (₦)'], 'align': 'llr', 'rows': [
      ['30 Jan 2024', 'Kofi & Co', '50,000'],
      ['31 Jan 2024', 'Ahamed Nig. Ltd', '175,000'],
      ['4 Feb 2024', 'Maxi Ltd', '155,000'],
      ['5 Feb 2024', 'Wike & Co', '205,000'],
      ['Total', '', '585,000'],
    ]}},
    {'pre': 'Dr  Purchases                             585,000\n    Cr  Payables ledger control account        585,000'},
    {'note': 'There is deliberately **no invoice number column** in the purchases day book — '
             'unlike the sales day book. The business raises its own sequential invoice numbers '
             'for sales; but purchase invoices arrive from many different suppliers, each running '
             'their own separate numbering sequence, so a single "invoice number" column would not '
             'mean anything consistent across rows.'},
    {'h4': 'The purchases day book with VAT'},
    {'table': {'head': ['Date', 'Invoice No.', 'Supplier', 'Amount (₦)', 'VAT (₦)', 'Total (₦)'],
     'align': 'llrrrr', 'rows': [
      ['Feb 3', 'INV001', 'ABC Suppliers', '500,000', '37,500', '537,500'],
      ['Feb 8', 'INV002', 'XYZ Enterprises', '800,000', '60,000', '860,000'],
      ['Feb 12', 'INV003', 'DEF Industries', '1,000,000', '75,000', '1,075,000'],
      ['Feb 18', 'INV004', 'GHI Ventures', '600,000', '45,000', '645,000'],
      ['Total', '', '', '2,900,000', '217,500', '3,117,500'],
    ]}},
    {'eg': {'t': 'Completing the study text\'s own exercise', 'q': [
      {'p': 'Post the double entry of the VAT-inclusive purchases day book above.'}],
      'a': [{'pre': 'Dr  Purchases                             2,900,000\n'
                    'Dr  VAT (input tax)                         217,500\n'
                    '    Cr  Payables ledger control account          3,117,500'}]}},
    {'h3': 'The sales returns day book (returns inwards book)'},
    {'p': 'Records returns of goods **sold on credit**, and helps track sales returns and update '
          'trade receivables and sales accounts.'},
    {'table': {'head': ['Date', 'Customer', 'Credit Note No.', 'Amount (₦)'], 'align': 'llrr',
     'rows': [
      ['Feb 10, 2024', 'Alaba Martins', 'CN001', '50,000'],
      ['Feb 12, 2024', 'Femi Adebayo', 'CN002', '20,000'],
      ['Feb 15, 2024', 'Nneoma Okoro', 'CN003', '30,000'],
      ['Feb 18, 2024', 'Bola Olaitan', 'CN004', '45,000'],
      ['Feb 22, 2024', 'Chinedu Eze', 'CN005', '18,000'],
      ['Feb 25, 2024', 'Adaobi Okonkwo', 'CN006', '25,000'],
      ['Total', '', '', '188,000'],
    ]}},
    {'eg': {'t': 'Completing the study text\'s own exercise', 'q': [
      {'p': 'Calculate the total amount and post the double entry for the sales returns day book '
            'above (the study text sets this as an exercise and leaves both the total and the '
            'entry blank).'}],
      'a': [
      {'p': 'Total: $50{,}000+20{,}000+30{,}000+45{,}000+18{,}000+25{,}000 = ₦188{,}000$.'},
      {'pre': 'Dr  Sales returns (returns inwards)       188,000\n'
              '    Cr  Receivables ledger control account       188,000'}]}},
    {'h3': 'The purchases returns day book (returns outwards book)'},
    {'p': 'Records returns of goods **purchased on credit**, and helps track purchase returns and '
          'update trade payables and purchases accounts.'},
    {'table': {'head': ['Date', 'Supplier', 'Credit Note No.', 'Amount (₦)'], 'align': 'llrr',
     'rows': [
      ['Feb 3, 2024', 'Ebony Ventures', 'CN001', '120,000'],
      ['Feb 5, 2024', 'Akwa Ltd', 'CN002', '80,000'],
      ['Feb 8, 2024', 'Enugu Industries', 'CN003', '250,000'],
      ['Feb 12, 2024', 'Lagos Traders', 'CN004', '90,000'],
      ['Feb 18, 2024', 'Port Harcourt Supplies', 'CN005', '60,000'],
      ['Feb 22, 2024', 'Abuja Distributors', 'CN006', '200,000'],
      ['Total', '', '', '800,000'],
    ]}},
    {'eg': {'t': 'Completing the study text\'s own exercise', 'q': [
      {'p': 'Post the double entry for the purchases returns day book above.'}],
      'a': [{'pre': 'Dr  Payables ledger control account       800,000\n'
                    '    Cr  Purchases returns (returns outwards)      800,000'}]}},
    {'h3': 'The cash book'},
    {'p': 'The cash book is unusual among the books of prime entry: it is **both** a book of '
          'prime entry **and** a ledger account in its own right. It records all cash receipts '
          'and cash payments. Where an entity maintains the imprest system, the main cash book '
          'records only **bank** transactions — receipts from customers deposited into the bank, '
          'payments to suppliers or creditors by cheque or electronic transfer, bank charges and '
          'interest, and other bank-related transactions. This lets a business track bank '
          'transactions and balances, and reconcile bank statements against the cash book balance '
          '(see Chapter 5 for the full bank reconciliation).'},
    {'p': '**Cash discount given and received is recorded only as a memorandum in the cash '
          'book** — it is not itself part of the double entry there. The double entry for a '
          'discount is completed separately, in the general ledger and in the individual payables '
          'or receivables ledgers.'},
    {'p': 'Some entities keep a separate **cash receipts book** and **cash payments book** rather '
          'than one combined cash book.'},
    {'h4': 'Cash receipts book'},
    {'p': 'Records cash sales, cash received from credit customers, and other cash income; helps '
          'track cash inflows and update cash and bank balances. The **cash** column records cash '
          'actually received, the **bank** column records cheques or other bank transactions, and '
          'the **discount** column records any discount allowed to customers.'},
    {'table': {'head': ['Date', 'Particulars', 'Cash (₦)', 'Bank (₦)', 'Discount (₦)',
     'Total (₦)'], 'align': 'llrrrr', 'rows': [
      ['Feb 1', 'Cash sales', '10,000', '', '', '10,000'],
      ['Feb 3', 'Received cheque from John', '', '50,000', '1,000', '51,000'],
      ['Feb 5', 'Cash received from Jane', '8,000', '', '200', '8,200'],
      ['Feb 10', 'Received cheque from Uzairu Ltd', '', '100,000', '', '100,000'],
      ['Feb 15', 'Cash sales', '12,000', '', '', '12,000'],
    ]}},
    {'h4': 'Cash payments book'},
    {'p': 'Records cash purchases and other cash payments; helps track cash outflows and update '
          'cash and bank balances. The **cash** column records cash payments, the **bank** column '
          'records cheque payments or other bank transactions, and the **discount** column records '
          'any discount received from suppliers.'},
    {'table': {'head': ['Date', 'Particulars', 'Cash (₦)', 'Bank (₦)', 'Discount (₦)',
     'Total (₦)'], 'align': 'llrrrr', 'rows': [
      ['Feb 1', 'Paid rent', '50,000', '', '', '50,000'],
      ['Feb 5', 'Paid supplier by cheque', '', '100,000', '2,000', '102,000'],
      ['Feb 10', 'Paid wages in cash', '20,000', '', '', '20,000'],
      ['Feb 15', 'Paid utility bills by cheque', '', '30,000', '', '30,000'],
      ['Feb 20', 'Paid cash to creditor', '15,000', '', '500', '15,500'],
    ]}},
    {'h3': 'The petty cash book, and the imprest system'},
    {'p': 'The petty cash book is another important book of prime entry: it records small cash '
          'transactions, typically for miscellaneous expenses such as office supplies, postage, '
          'travel and entertainment expenses. It is used to track and control small cash '
          'expenditure, and is usually maintained by a designated person, the **petty cashier**. '
          'It typically records the date, a description of the transaction, the amount, and an '
          '**analysis** of expenses across a set of expense columns.'},
    {'p': 'Some businesses run petty cash on the **imprest system**: a fixed amount is allocated '
          'for petty cash expenses, and the petty cashier is responsible for accounting for the '
          'expenditure and having the fund replenished when necessary.'},
    {'warn': 'This section is headed **"6.1 The Imprest System and Control Over Petty Cash"** in '
             'the study text\'s own numbering — even though it sits inside Chapter Three, between '
             '§3.6 and §3.7. This is one more example of the numbering slips that run through this '
             'study text (see also Chapter 2\'s "other accounting concepts," and the missing '
             '"Chapter Five" in the book\'s overall table of contents). It is not a sign that '
             'content has been misplaced from a different chapter — the petty cash and imprest '
             'material genuinely belongs here, in Chapter Three, alongside the other books of '
             'prime entry.'},
    {'p': 'The imprest system works like this: a fixed amount of cash — the **imprest amount** — '
          'is entrusted to the petty cashier, who is responsible for making payments for petty '
          'expenses and for keeping receipts and records for each transaction. Every payment is '
          'supported by an **approved petty cash voucher** — a document showing evidence of the '
          'payment made. All payments made are recorded on the **credit** side of the petty cash '
          'book, each analysed to its related expense column, while the original imprest and the '
          'regular reimbursements are recorded on the **debit** side.'},
    {'p': 'When the fund is depleted, or at regular intervals, the petty cashier submits the '
          'receipts and records to request reimbursement. The imprest is then **replenished to '
          'its original amount**, based on the receipts and records submitted — this is exactly '
          'why the system is called "imprest": the fund is always restored to the same fixed '
          'level. There must be effective supervision of the petty cash book: the approved '
          'voucher and the cash received should be checked by a superior officer, the voucher '
          'must be signed by both the claimant and the petty cashier, and reimbursement should '
          'generally only be made after confirming that the petty cash book balance agrees with '
          'the actual cash balance held.'},
    {'h4': 'Illustration 3.5 — a month of petty cash'},
    {'p': 'Emzor Ventures operates the imprest system with a float of ₦50,000. During February: '
          'office supplies ₦10,000 (3rd); postage ₦5,000 (5th); bus fare to staff ₦2,000 (8th); '
          'stationery ₦8,000 (10th); refreshments for a meeting ₦3,000 (15th); courier services '
          '₦4,000 (18th); tea and snacks for the office ₦1,500 (20th); printing services ₦6,000 '
          '(22nd); a transport fare reimbursed to staff, ₦3,100 (25th); and a newspaper '
          'subscription ₦1,000 (28th).'},
    {'note': 'The study text\'s own transaction list describes the 25 February item as "reimbursed '
             'mileage to staff ₦3,500," but its own petty cash book table posts ₦3,100 against '
             'that date — and only the ₦3,100 figure reconciles with the stated total of ₦43,600 '
             'reimbursed at month end. The ₦3,100 figure is used below as the one that is '
             'internally consistent.'},
    {'table': {'head': ['Date', 'Details', 'Voucher', 'Total (₦)', 'Office expenses (₦)',
     'Transport (₦)', 'Refreshments (₦)', 'Postage (₦)'], 'align': 'llrrrrrr', 'rows': [
      ['Feb 3', 'Office supplies', '01', '10,000', '10,000', '', '', ''],
      ['Feb 5', 'Postage', '02', '5,000', '', '', '', '5,000'],
      ['Feb 8', 'Bus fare', '03', '2,000', '', '2,000', '', ''],
      ['Feb 10', 'Stationery', '04', '8,000', '8,000', '', '', ''],
      ['Feb 15', 'Refreshments', '05', '3,000', '', '', '3,000', ''],
      ['Feb 18', 'Courier', '06', '4,000', '4,000', '', '', ''],
      ['Feb 20', 'Tea and snacks', '07', '1,500', '', '', '1,500', ''],
      ['Feb 22', 'Printing', '08', '6,000', '6,000', '', '', ''],
      ['Feb 25', 'Transport fare', '09', '3,100', '', '3,100', '', ''],
      ['Feb 28', 'Newspaper', '10', '1,000', '1,000', '', '', ''],
      ['Total', '', '', '43,600', '29,000', '5,100', '4,500', '5,000'],
    ]}},
    {'p': 'The imprest was ₦50,000; vouchers total ₦43,600 (which checks against the four expense '
          'columns: $29{,}000+5{,}100+4{,}500+5{,}000 = 43{,}600$). At month end the petty cashier '
          'is reimbursed exactly ₦43,600, restoring the float to ₦50,000 for the start of March.'},
    {'key': 'The internal controls a petty cash system should have, in one list: a **fixed '
            'imprest**, so the maximum exposure to loss is capped; every payment supported by an '
            '**authorised, signed voucher**; **regular reimbursement** only against vouchers '
            'submitted; **independent checking** of the vouchers and the cash balance by a '
            'superior officer before reimbursement; and a **clear analysis** of expenditure by '
            'type, so postings to the general ledger are simple and auditable.'},
  ]},

  {'n': '3.5', 't': 'The journal', 'b': [
    {'p': 'The journal records **non-routine transactions** that do not fit into any of the other '
          'day books. The study text names five specific uses:'},
    {'ol': [
      'Adjustments and corrections;',
      'Opening and closing entries;',
      'Transfers from one account to another;',
      'Purchases and sales of non-current assets;',
      'Other non-cash transactions.',
    ]},
    {'key': 'On **every** journal entry, a **narration** (explanation) must be given, showing why '
            'the journal was raised.'},
    {'h3': 'Illustration 3.6 — adjustment and correction'},
    {'p': 'An error has been detected in the books of Varlee & Son: F. Zizi\'s account, a '
          'customer, has been debited instead of J. Zizi\'s, with goods sold for L$20,000 (note '
          'the Liberian-dollar figures — this study text is written for the whole West African '
          'region, not Nigeria alone, so illustrations sometimes use L$, GH¢ or other regional '
          'currencies).'},
    {'table': {'head': ['', 'Debit (L$)', 'Credit (L$)'], 'align': 'lrr', 'rows': [
      ['J. Zizi', '20,000', ''],
      ['F. Zizi', '', '20,000'],
      ['Being correction of the wrong entry in F. Zizi\'s account', '', ''],
    ]}},
    {'h3': 'Illustration 3.7 — closing entries'},
    {'p': 'Akua Enterprises, a Ghanaian company, has opening inventory of GH₵15,000, purchases of '
          'GH₵80,000, cost of goods sold of GH₵60,000, and closing inventory of GH₵35,000. Show '
          'the journal entry to record the closing inventory.'},
    {'table': {'head': ['', 'Debit (GH₵)', 'Credit (GH₵)'], 'align': 'lrr', 'rows': [
      ['Inventory', '35,000', ''],
      ['Cost of sales', '', '35,000'],
      ['Being adjustment for closing inventory, for Akua Enterprises', '', ''],
    ]}},
    {'p': 'The ₦35,000 (GH₵35,000) is **deducted from cost of sales** when preparing the '
          'statement of profit or loss, and is recognised as a **current asset** at the reporting '
          'date.'},
    {'h3': 'Illustration 3.8 — opening entries'},
    {'p': 'Fatu Ventures has the following assets and liabilities: fixtures L$450,000, motor '
          'vehicles L$600,000, inventory L$700,000, trade receivables L$200,000, cash L$250,000, '
          'trade payables L$240,000. Prepare the opening journal.'},
    {'table': {'head': ['', 'Debit (L$)', 'Credit (L$)'], 'align': 'lrr', 'rows': [
      ['Fixtures', '450,000', ''],
      ['Motor vehicles', '600,000', ''],
      ['Inventory', '700,000', ''],
      ['Trade receivables', '200,000', ''],
      ['Cash', '250,000', ''],
      ['Payables', '', '240,000'],
      ['Capital', '', '1,960,000'],
      ['Being opening assets and liabilities of Fatu Ventures', '2,200,000', '2,200,000'],
    ]}},
    {'note': 'This is an example of a **compound journal** — one with more than one debit or '
             'more than one credit line, provided the totals of each side still agree. Capital is '
             'the balancing figure: total assets (₦2,200,000) less trade payables (₦240,000) '
             'gives the owner\'s opening capital of ₦1,960,000, exactly as the accounting equation '
             'in §3.1 predicts.'},
    {'h3': 'Illustration 3.9 (transfers) — moving a balance from one account to another'},
    {'p': 'Zuba Ltd transferred ₦125,000 from its payables ledger control account to its '
          'receivables ledger control account, to offset purchases against sales (a **contra** — '
          'see also Chapter 5).'},
    {'table': {'head': ['', 'Debit (₦)', 'Credit (₦)'], 'align': 'lrr', 'rows': [
      ['Payables ledger control account', '125,000', ''],
      ['Receivables ledger control account', '', '125,000'],
      ['Being transfer of the balance in the payables ledger control account to the sales '
       'ledger control account', '', ''],
    ]}},
    {'h3': 'The worksheet (extended trial balance)'},
    {'p': 'A worksheet, or extended trial balance, is a working paper with three pairs of debit '
          'and credit columns: the **opening trial balance**, the **adjustments**, and the '
          '**adjusted trial balance** — followed by two further columns, without a debit/credit '
          'split shown separately, extending the adjusted figures into the **statement of profit '
          'or loss** and the **statement of financial position**.'},
    {'steps': [
      '**Extract the opening trial balance** from the ledger of the firm, including unadjusted '
      'balances.',
      '**Enter adjustments** — enter each necessary adjustment (debit and credit) against the '
      'relevant account affected.',
      '**Calculate the adjusted trial balance** — extend the trial balance and adjustment columns '
      'into the adjusted trial balance column, adding together debit or credit balances as '
      'necessary; both sub-columns must agree, confirming arithmetic accuracy.',
      '**Prepare the income statement** — extend the adjusted trial balance column into the '
      'income statement column for items relating to trading activities, operational income and '
      'expenses; calculate the net profit or loss and insert the difference into the short '
      'column, extending it to the opposite side in the statement of financial position column.',
      '**Prepare the statement of financial position** — extend all remaining balances in the '
      'adjusted trial balance into the statement of financial position column; both sub-columns '
      'should agree if all preceding steps have been correctly followed.',
    ]},
    {'p': 'A properly completed worksheet is a powerful working tool: it helps prepare the '
          'financial statements and supports analysis, all from one page.'},
  ]},

  {'n': '3.6', 't': 'The trial balance, and the errors it cannot detect', 'b': [
    {'p': 'A trial balance is a list of ledger balances at a date, with debits in one column and '
          'credits in the other. If the columns agree, the **arithmetic** of double entry is '
          'sound. That is all it proves.'},
    {'h3': 'The two categories of error'},
    {'ol': [
      '**Errors that are revealed by the trial balance** — the two columns will not agree.',
      '**Errors that are not revealed by the trial balance** — the two columns agree, but the '
      'figures are still wrong.',
    ]},
    {'table': {'head': ['Error', 'What happened', 'Example'], 'align': 'lll', 'rows': [
      ['**Omission**', 'The transaction was left out entirely',
       'An invoice never entered in either account'],
      ['**Commission**', 'Right side, right amount, wrong account of the same type',
       '₦40,000 posted to A. Bello instead of A. Bala, both receivables'],
      ['**Principle**', 'Right side, right amount, wrong *type* of account',
       'Motor repairs debited to Motor Vehicles'],
      ['**Original entry**', 'The wrong amount was used on both sides',
       '₦5,600 entered as ₦6,500 in both accounts'],
      ['**Reversal of entries**', 'Debit and credit were swapped',
       'Cash sale debited to Sales and credited to Cash'],
      ['**Compensating**', 'Two errors of equal amount on opposite sides cancel out',
       'Sales overcast by ₦10,000 and purchases overcast by ₦10,000'],
    ]}},
    {'warn': 'An error of **principle** is the dangerous one, because it misstates profit. '
             'Debiting motor repairs to the vehicle account overstates both profit and '
             'non-current assets, and keeps overstating profit through the reduced depreciation '
             'in every later year.'},
    {'h3': 'Correction of errors, and the suspense account'},
    {'p': 'Errors are normally corrected, once identified, through **journal entries**: the '
          'journal indicates the account(s) to be debited and the account(s) to be credited, and '
          'carries a narration describing the error.'},
    {'key': 'Errors that are **not** revealed by the trial balance do **not** pass through a '
            'suspense account. Errors that **are** revealed by the trial balance are corrected '
            '**through** a suspense account.'},
    {'p': 'When the trial balance does not agree, the difference is transferred to, or recorded '
          'in, a **suspense account**, which makes the trial balance totals agree so that '
          'statements can still be drafted while the error is tracked down. The suspense account '
          'can hold a debit or a credit balance, depending on which side of the trial balance had '
          'the higher total — a **debit** balance on suspense hints that some assets or expenses '
          'are unidentified (understated); a **credit** balance hints at an unidentified liability '
          'or income (understated). Once every underlying error has been found and corrected, the '
          'suspense account will show a **zero (nil) balance**.'},
    {'h3': 'Illustration 3.9 (errors) — two errors of principle, no suspense needed'},
    {'p': 'The trial balance of Kwame Ankra Enterprise at 30 April 2025 **agreed**, but the '
          'bookkeeper later discovered: (i) a cash purchase of ¢560,000 for new equipment had '
          'been debited to the office equipment *repairs* account; and (ii) ¢198,000 paid for '
          '*insurance* expenses had been debited to the *rent* account.'},
    {'table': {'head': ['', 'Debit (¢)', 'Credit (¢)'], 'align': 'lrr', 'rows': [
      ['Office equipment', '560,000', ''],
      ['Office repairs account', '', '560,000'],
      ['Being correction of an error of principle: office equipment wrongly debited to office '
       'equipment repairs', '', ''],
      ['Insurance account', '198,000', ''],
      ['Rent account', '', '198,000'],
      ['Being correction of an error of principle: ¢198,000 wrongly debited to rent account '
       'instead of insurance account', '', ''],
    ]}},
    {'note': 'Because the trial balance **already agreed** before these were found, **neither** '
             'correction touches a suspense account — both are errors of principle (right amount, '
             'both sides posted, just to the wrong type of account), which is exactly the '
             'category of error a trial balance can never reveal on its own.'},
    {'h3': 'Illustration 3.10 — a full suspense account reconciliation'},
    {'p': 'The trial balance of Malam Bako Enterprise at 31 December 2024 did **not** balance, and '
          'a **credit** balance of ₦1,717,000 was entered in a suspense account to make it agree. '
          'A detailed check of the books disclosed:'},
    {'ol': [
      'Purchases returns for December 2024, ₦400,000, was posted to the **debit of the purchases '
      'account** (instead of being credited to purchases returns).',
      'The sales day book for June was **undercast** by ₦40,000.',
      'Discount received in September, ₦480,000, was posted to the **wrong side** of the discount '
      'account.',
      'A sale of ₦41,000 to B. Adamu was correctly entered in the sales book, but posted to the '
      '**credit** of B. Adamu\'s account in the sales ledger as **₦22,000** (both the side and the '
      'amount are wrong).',
      '₦20,000 paid for vehicle repairs was **not entered** in the relevant repairs account at all.',
    ]},
    {'table': {'head': ['', 'Detail', 'Dr (₦)', 'Cr (₦)'], 'align': 'llrr', 'rows': [
      ['(a)', 'Suspense', '400,000', ''],
      ['', 'Purchases account', '', '400,000'],
      ['', '*Cancelling the wrong debit posted to purchases.*', '', ''],
      ['(a)', 'Suspense', '400,000', ''],
      ['', 'Purchases returns', '', '400,000'],
      ['', '*Recording the credit that should have gone to purchases returns all along.*', '', ''],
      ['(b)', 'Suspense', '40,000', ''],
      ['', 'Sales account', '', '40,000'],
      ['', '*Correcting the undercast sales day book.*', '', ''],
      ['(c)', 'Suspense', '480,000', ''],
      ['', 'Discount received', '', '480,000'],
      ['', '*Cancelling the entry posted to the wrong side.*', '', ''],
      ['(c)', 'Suspense', '480,000', ''],
      ['', 'Discount received', '', '480,000'],
      ['', '*Posting the discount received correctly, to the right side.*', '', ''],
      ['(d)', 'B. Adamu', '22,000', ''],
      ['', 'Suspense', '', '22,000'],
      ['', '*Cancelling the wrong ₦22,000 credited to B. Adamu.*', '', ''],
      ['(d)', 'B. Adamu', '41,000', ''],
      ['', 'Suspense', '', '41,000'],
      ['', '*Posting the correct ₦41,000, on the correct (debit) side, to B. Adamu.*', '', ''],
      ['(e)', 'Vehicle repairs account', '20,000', ''],
      ['', 'Suspense', '', '20,000'],
      ['', '*Entering the repair that had never been posted at all.*', '', ''],
    ]}},
    {'warn': 'Read item (a) and item (c) carefully — each needs **two** journal lines, not one, '
             'and each of those two lines is worth the **full** amount of the error, not half of '
             'it. In (a), the original entry did not just go to the wrong account; it went to the '
             'wrong account **and never generated the credit purchases returns needed at all** — '
             'so ₦400,000 must be removed from purchases *and* ₦400,000 must still be credited to '
             'purchases returns: two separate corrections, ₦800,000 through suspense in total. In '
             '(c), a **wrong-side** posting is even more expensive to fix: reversing a wrong-side '
             'entry takes the original amount out, and then the correct entry must still be made '
             '— so a wrong-side error always costs **double** the original amount to correct, '
             'here ₦960,000 through suspense for a ₦480,000 error. This is exactly why a '
             'wrong-side posting is so much more damaging to a trial balance than a wrong-account '
             'posting of the same size.'},
    {'tacc': {'t': 'Suspense account', 'dr': [
        ['Purchases', 400000], ['Purchases returns', 400000], ['Sales', 40000],
        ['Discount receivable', 960000], ['', 1800000, '@tot']],
      'cr': [['Balance b/f', 1717000], ['B. Adamu', 63000], ['Vehicle repairs', 20000],
             ['', 1800000, '@tot']]}},
    {'note': 'Check the two sides: debit total $400{,}000+400{,}000+40{,}000+960{,}000 = '
             '₦1{,}800{,}000$; credit total $1{,}717{,}000+22{,}000+41{,}000+20{,}000 = '
             '₦1{,}800{,}000$. They agree, and once every one of the five errors above has been '
             'posted, the suspense account carries **no remaining balance** — exactly as it '
             'should once every underlying error has genuinely been found.'},
  ]},

  {'n': '3.7', 't': 'How everything in this chapter fits together', 'b': [
    {'p': 'Control accounts (met in full in Chapter 5) are accounts in the general ledger that '
          '**summarise the balances of related subsidiary accounts**. Books of prime entry are '
          'essential to maintaining them, for two reasons: they help ensure transactions are '
          'accurately recorded and posted to the subsidiary ledgers, which are then reconciled '
          'with the control accounts in the general ledger; and they make it possible to '
          '**identify errors and discrepancies** between the subsidiary ledgers and the control '
          'accounts, enabling prompt correction and reconciliation.'},
    {'p': 'Putting the whole chapter\'s worth of machinery in one place: **source documents** are '
          'original records providing evidence of transactions (invoices, receipts, bank '
          'statements, contract documents); **books of prime entry** are where transactions are '
          'first recorded, in chronological order, based on those source documents; **ledger '
          'accounts** (the general ledger) are where transactions are classified and summarised by '
          'account. In summary: source documents provide evidence of transactions, which are '
          'recorded in books of prime entry and then posted to ledger accounts, leading to the '
          'extraction of a trial balance, and ultimately to the preparation of the financial '
          'statements.'},
    {'key': 'The chain, in one line: **Source Documents → Books of Prime Entry → Ledger Accounts '
            '→ Trial Balance → Financial Statements.** Every topic in this chapter is one link in '
            'that chain, and almost every exam question in this area is really just asking you to '
            'place a given fact at the correct link.'},
  ]},

  {'n': '3.8', 't': 'The chart of accounts', 'b': [
    {'def': {'t': 'Chart of accounts', 'd': 'a systematic listing of all the accounts used by a '
                  'business to record its financial transactions. Its primary purpose is to '
                  'provide a framework for organising and classifying financial data, enabling '
                  'accurate financial reporting and analysis.'}},
    {'h3': 'What it is built from'},
    {'ul': [
      '**Account numbers** — unique codes assigned to each account.',
      '**Account names** — descriptive names for each account.',
      '**Account types** — classification into asset, liability, equity, revenue and expense '
      'categories.',
    ]},
    {'p': '**Account codes** (also called account numbers) help to: **distinguish** between '
          'accounts with similar names or purposes; **efficiently record and retrieve** financial '
          'data; and **support automated** financial reporting and analysis.'},
    {'h3': 'How account codes are derived'},
    {'ul': [
      '**Sequential numbering** — assigning consecutive numbers to accounts (e.g. 1000, 1001, '
      '1002).',
      '**Hierarchical numbering** — using a hierarchical structure to reflect account '
      'relationships (e.g. 1000–1999 for assets, 2000–2999 for liabilities).',
      '**Alpha-numeric coding** — combining letters and numbers to create unique codes (e.g. '
      'ASH101 for Cash).',
    ]},
    {'h3': 'The five account types'},
    {'ol': [
      '**Assets** — resources owned or controlled by the business (e.g. cash, accounts '
      'receivable, inventory).',
      '**Liabilities** — debts or obligations owed by the business (e.g. accounts payable, loans '
      'payable).',
      '**Equity** — ownership interests in the business (e.g. common stock, retained earnings).',
      '**Revenue** — income earned by the business (e.g. sales, service revenue).',
      '**Expenses** — costs incurred by the business (e.g. salaries expense, rent expense).',
    ]},
    {'h3': 'Why bother with one'},
    {'ol': [
      'Enables the preparation of accurate financial statements.',
      'Facilitates analysis of financial performance and trends.',
      'Streamlines financial recording and reporting processes.',
      'Provides an informed basis for decision-making.',
    ]},
    {'h3': 'Designing, implementing and maintaining a chart of accounts'},
    {'p': '**Best practices when designing one:** consistency (use a consistent numbering system '
          'and account structure); logical structure (design a logical, intuitive account '
          'hierarchy); flexibility (allow for future expansion and changes); and industry-specific '
          'considerations (account for the requirements and regulations of the specific '
          'industry).'},
    {'p': '**Implementing a chart of accounts:** identify the business\'s specific needs; design '
          'the chart to meet those needs; assign unique account numbers; and configure the '
          'accounting system to use the chart.'},
    {'p': '**Maintaining a chart of accounts:** review it regularly; add or remove accounts as '
          'needed; and ensure account classifications and numbering are applied consistently over '
          'time.'},
    {'table': {'head': ['Range', 'Class'], 'align': 'll', 'rows': [
      ['1000–1999', 'Assets'], ['2000–2999', 'Liabilities'], ['3000–3999', 'Equity'],
      ['4000–4999', 'Income'], ['5000–5999', 'Cost of sales'], ['6000–6999', 'Expenses'],
    ]}},
  ]},

  {'n': '3.9', 't': 'Further reading', 'b': [
    {'note': 'Double-entry mechanics are old enough, and universal enough, that good free '
             'explainers are easy to find outside the standards themselves. '
             '[AccountingCoach\'s bookkeeping course](https://www.accountingcoach.com/bookkeeping/explanation) '
             'works through debits, credits and the ledger from first principles with short '
             'quizzes after each section, and its '
             '[trial balance explainer](https://www.accountingcoach.com/trial-balance/explanation) '
             'covers exactly the "what it proves and what it does not" distinction from §3.6. '
             'For source documents and the journal specifically, '
             '[Investopedia\'s note on the general journal](https://www.investopedia.com/terms/g/generaljournal.asp) '
             'is a quick refresher. On the regulatory side, the [Institute of Chartered '
             'Accountants of Nigeria](https://icanig.org) publishes past ATSWA-style questions '
             'and examiner guidance that are worth searching for once the mechanics here feel '
             'solid.'},
  ]},
 ],
 'formulas': [
  {'lb': 'The accounting equation', 'tex': '\\text{Assets} = \\text{Capital} + \\text{Liabilities}'},
  {'lb': 'Movement in capital',
   'tex': '\\text{Assets} = \\text{Capital} + \\text{Additional capital} + \\text{Profit} - '
          '\\text{Drawings} + \\text{Liabilities}',
   'nt': 'Rearrange it for profit and you have the incomplete-records method of Chapter 6.'},
  {'lb': 'Petty cash reimbursement',
   'tex': '\\text{Reimbursement} = \\text{Imprest} - \\text{Cash in hand} = \\sum\\text{vouchers}'},
 ],
 'focus':
   'This chapter supplies more marks than any other single chapter, in both sections. Section A '
   'tests the six errors, the effect of a transaction on the equation, which book of prime entry a '
   'document enters, and — the study text\'s own favourite — which of the sixteen source documents '
   'matches a given description. Section B tests correction of errors with a suspense account, and '
   'almost always asks for the **effect on profit** as a second part — practise that separately, '
   'because it is where candidates who can write the journals still lose marks. Pay particular '
   'attention to *wrong-side* postings (Illustration 3.10, items a and c): they cost double the '
   'original amount to correct, and that doubling is a favourite thing for the examiner to test.',
 'errors': [
   'Putting an error of principle or commission through suspense. If the original entry balanced, '
   'suspense is not involved.',
   'Forgetting that correcting a misposting between an income and an expense account moves profit '
   'by twice the entry.',
   'Treating payment to a supplier as an expense. It settles a liability; the expense arose when '
   'the goods were bought.',
   'Balancing an account by writing the balancing figure without carrying it down.',
   'Correcting a wrong-side posting for only the original amount, instead of double it.',
   'Including cash sales or cash purchases in the sales or purchases day book — they never touch '
   'a receivables or payables account, so they never appear there.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A business pays ₦120,000 to a trade payable. The effect on the accounting equation is',
    'o': ['Assets decrease, capital decreases', 'Assets decrease, liabilities decrease',
          'Assets increase, liabilities increase', 'Capital decreases, liabilities decrease',
          'No effect on the equation'],
    'a': 1,
    'w': 'Cash (an asset) falls by ₦120,000 and the payable (a liability) falls by ₦120,000. '
         'Both sides of the equation fall equally. Profit is untouched — the expense was '
         'recognised when the goods were received.',
    'src': 'Chapter 3.1'},
   {'q': 'Repairs to a motor vehicle were debited to the Motor Vehicles account. This is an error of',
    'o': ['omission', 'commission', 'principle', 'original entry', 'reversal'],
    'a': 2,
    'w': 'The entry went to the wrong *type* of account — a revenue expense treated as capital '
         'expenditure. That is an error of principle, and the trial balance still agrees.',
    'src': 'Chapter 3.6'},
   {'q': 'Opening capital was ₦1,800,000, closing capital ₦2,450,000. The owner introduced '
         '₦300,000 and drew ₦180,000. Profit for the period was',
    'o': ['₦350,000', '₦530,000', '₦650,000', '₦770,000', '₦1,130,000'],
    'a': 1,
    'w': 'Rearrange the capital movement formula for profit.',
    'calc': '\\text{Profit} = 2{,}450{,}000 - 1{,}800{,}000 - 300{,}000 + 180{,}000 = 530{,}000',
    'src': 'Chapter 3.1'},
   {'q': 'The imprest is ₦40,000. Vouchers for the month total ₦27,300 and the tin holds ₦12,700. '
         'The amount to reimburse is',
    'o': ['₦12,700', '₦27,300', '₦40,000', '₦52,700', '₦14,600'],
    'a': 1,
    'w': 'Reimbursement always equals the vouchers, restoring the float. Check: '
         '40,000 − 27,300 = 12,700, which is what the tin holds, so there is no shortage.',
    'calc': '\\text{Reimbursement} = 40{,}000 - 12{,}700 = 27{,}300',
    'src': 'Chapter 3.4'},
   {'q': 'A credit note received from a supplier is entered in the',
    'o': ['sales day book', 'purchases day book', 'sales returns day book',
          'purchases returns day book', 'petty cash book'],
    'a': 3,
    'w': 'A credit note *received* means goods were returned *to* the supplier, so it enters the '
         'purchases returns (returns outwards) day book.',
    'src': 'Chapter 3.4'},
   {'q': 'A trial balance shows a difference of ₦270. The most likely cause is',
    'o': ['an error of omission', 'a compensating error', 'a transposition on one side only',
          'an error of principle', 'a reversal of entries'],
    'a': 2,
    'w': 'A difference divisible by 9 points to a transposition — ₦8,730 written as ₦8,460, for '
         'example. The other four errors listed all leave the trial balance in agreement.',
    'calc': '270 \\div 9 = 30 \\quad \\text{(exact, so a transposition is likely)}',
    'src': 'Chapter 3.6'},
   {'q': 'Discount received of ₦12,000 was credited to the discount allowed account. Correcting '
         'this will change profit by',
    'o': ['nil', '₦12,000 increase', '₦12,000 decrease', '₦24,000 increase', '₦24,000 decrease'],
    'a': 3,
    'w': 'Two things are wrong at once: an income of ₦12,000 was omitted, and an expense account '
         'was wrongly reduced by ₦12,000. Correcting both moves profit by ₦24,000 upward.',
    'calc': '\\text{Effect} = 12{,}000 \\text{ (income restored)} + 12{,}000 '
            '\\text{ (expense restored)} = 24{,}000',
    'src': 'Chapter 3.6'},
  ],
  'theory': [
   {'q': 'State and explain SIX errors that would not be revealed by a trial balance, giving one '
         'example of each.',
    'marks': 12,
    'a': [{'ol': [
      '**Error of omission** — the transaction is not recorded at all, in either account. '
      'Example: a purchase invoice mislaid and never entered.',
      '**Error of commission** — the correct amount is entered on the correct side but in the '
      'wrong account *of the same class*. Example: ₦50,000 received from A. Musa posted to A. '
      'Mustapha, both receivables.',
      '**Error of principle** — the entry is made in the wrong *class* of account. Example: '
      'the purchase of stationery debited to office equipment.',
      '**Error of original entry** — the wrong figure is used consistently on both sides. '
      'Example: an invoice for ₦4,570 recorded throughout as ₦4,750.',
      '**Complete reversal of entries** — the account that should be debited is credited and '
      'vice versa. Example: cash paid to a supplier debited to cash and credited to the supplier.',
      '**Compensating error** — two or more errors of the same amount on opposite sides cancel '
      'each other. Example: the sales account overcast by ₦9,000 and the wages account overcast '
      'by ₦9,000.',
    ]},
    {'note': 'The trial balance agrees in every one of these cases because each error preserves '
             'equality of debits and credits. Only errors of principle and of original entry '
             'misstate profit; commission and omission of a transfer affect classification only.'}],
    'src': 'Chapter 3.6'},
   {'q': 'Explain the imprest system of petty cash and state FOUR of its advantages.',
    'marks': 6,
    'a': [
      {'p': '**The system.** A fixed sum, the imprest or float, is advanced to the petty cashier. '
            'Payments are made only against authorised vouchers. At the end of each period the '
            'cashier presents the vouchers and is reimbursed exactly the amount spent, so the '
            'float is restored to the original imprest for the start of the next period.'},
      {'p': 'At any moment: **cash in hand + vouchers held = the imprest amount.**'},
      {'h4': 'Advantages'},
      {'ol': [
        'The maximum exposure to loss or theft is limited to the imprest amount.',
        'A shortage is detected immediately, because cash plus vouchers must reconcile to a '
        'known fixed figure.',
        'Reimbursement is a single ledger entry each period instead of one entry per small payment.',
        'Every payment must be supported by an authorised voucher, which enforces control and '
        'gives an audit trail.',
        'It relieves the main cashier of a large volume of trivial payments.']}],
    'src': 'Chapter 3.4'},
  ]},
}
