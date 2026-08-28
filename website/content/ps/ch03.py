CH = {
 'n': 3,
 't': 'Standardisation of Reporting Format',
 'brief': 'The National Chart of Accounts and its segments, the GIFMIS platform, the Treasury '
          'Single Account, and the standard templates for the General Purpose Financial '
          'Statements.',
 'outcomes': [
   'Explain why a uniform chart of accounts is necessary in the public sector',
   'Describe the segments of the National Chart of Accounts',
   'Distinguish administrative, economic, functional, programme, fund, geographical and '
   'financing segments',
   'Explain GIFMIS and the Treasury Single Account',
   'List the General Purpose Financial Statements required under IPSAS',
 ],
 'secs': [
  {'n': '3.1', 't': 'The need for standardisation', 'b': [
    {'p': 'Before the adoption of IPSAS, each ministry, state and local government maintained '
          'its own classification of receipts and payments. The consequences were that '
          'consolidation was laborious and unreliable, comparison between states was '
          'impossible, national statistics were incompatible with international standards, and '
          'the same item of expenditure carried different codes in different entities.'},
    {'h4': 'Objectives of a national chart of accounts'},
    {'ul': [
      'To provide a **uniform basis of classification** for all receipts and payments across '
      'all tiers of government.',
      'To enable **consolidation** of the accounts of the Federal, State and Local Governments '
      'into government-wide statements.',
      'To align government reporting with the **IMF Government Finance Statistics (GFS) '
      'Manual** and the United Nations Classification of the Functions of Government (COFOG), '
      'so that national statistics are internationally comparable.',
      'To support **budget preparation, execution and monitoring** through the same codes used '
      'for accounting, so that budget and actual can be compared directly.',
      'To make **IPSAS-compliant financial statements** possible, since accrual accounting '
      'requires asset, liability and equity codes that a cash-based classification did not have.',
      'To provide the coding structure required by an integrated financial management '
      'information system.',
    ]},
  ]},

  {'n': '3.2', 't': 'The National Chart of Accounts', 'b': [
    {'p': 'The National Chart of Accounts (NCOA) was developed by the Sub-Committee on the '
          'roadmap for IPSAS implementation under the Federation Account Allocation Committee. '
          'It is a multi-dimensional coding structure in which every transaction is classified '
          'simultaneously along several independent **segments**, so that the same transaction '
          'can be reported by ministry, by economic nature, by function, by programme and by '
          'location without being recorded more than once.'},
    {'table': {'align': 'lll', 'head': ['Segment', 'Question it answers', 'Illustration'],
      'rows': [
      ['**Administrative**', 'Who spent it? Which ministry, department or agency?',
       'Federal Ministry of Health → Nigeria Centre for Disease Control'],
      ['**Economic**', 'What was it spent on, by nature?',
       'Personnel cost → salaries; Other service-wide votes → electricity'],
      ['**Functional (COFOG)**', 'For what purpose of government?',
       'Health; Education; Defence; Public order and safety'],
      ['**Programme**', 'Under which policy programme or project?',
       'Universal Basic Education; Immunisation programme'],
      ['**Fund**', 'From which fund?',
       'Consolidated Revenue Fund; Development Fund; a donor fund'],
      ['**Geographical**', 'Where was it spent?', 'State, senatorial district, local government'],
      ['**Financing / donor**', 'Who financed it?',
       'Government of Nigeria; World Bank credit; a bilateral donor'],
    ]}},
    {'h4': 'The economic segment'},
    {'p': 'This is the segment used most in accounting, and it follows the structure of the '
          'financial statements:'},
    {'table': {'align': 'll', 'head': ['Code series', 'Class'], 'rows': [
      ['**1**', 'Assets — cash, receivables, inventory, investments, property, plant and '
       'equipment'],
      ['**2**', 'Liabilities — payables, borrowings, provisions, employee benefit obligations'],
      ['**3**', 'Net assets / equity — accumulated surplus or deficit, reserves'],
      ['**4**', 'Revenue — tax revenue, statutory allocation, aid and grants, other revenue'],
      ['**5**', 'Expenditure — personnel cost, overhead cost, consolidated revenue fund '
       'charges, capital expenditure'],
    ]}},
    {'key': 'The multi-segment design is what allows one posting to serve every report. A '
            'salary payment at a rural clinic is at once **administrative** (Ministry of '
            'Health), **economic** (personnel cost), **functional** (health), **programme** '
            '(primary health care), **fund** (CRF) and **geographical** (that local '
            'government). No re-analysis is needed to produce any of those reports.'},
  ]},

  {'n': '3.3', 't': 'GIFMIS and the Treasury Single Account', 'b': [
    {'def': {'t': 'GIFMIS',
             'd': 'The Government Integrated Financial Management Information System — an '
                  'integrated computerised platform covering budget preparation, budget '
                  'execution, commitment control, payments, accounting, cash management, '
                  'payroll (through IPPIS) and reporting, built on the National Chart of '
                  'Accounts.'}},
    {'h4': 'Benefits of GIFMIS'},
    {'ul': [
      'A single, real-time record of government financial transactions, eliminating '
      'reconciliation between disconnected ledgers.',
      'Automatic **commitment control**: an order cannot be raised where the vote is exhausted, '
      'which prevents the accumulation of unfunded arrears.',
      'Faster and more reliable production of the monthly transcript and the annual accounts.',
      'A stronger audit trail, since every transaction is time-stamped and attributed to a user.',
      'Better cash management, because balances across government are visible.',
      'Reduction of ghost workers when combined with the **IPPIS** payroll platform.',
    ]},
    {'def': {'t': 'Treasury Single Account (TSA)',
             'd': 'A unified structure of government bank accounts, operated through the '
                  'Central Bank of Nigeria, which gives a consolidated view of government cash '
                  'resources. Implemented fully in Nigeria from September 2015, with revenue '
                  'collected through the Remita platform sweeping into the TSA daily.'}},
    {'h4': 'Benefits of the TSA'},
    {'ul': [
      'Consolidation of idle balances that were previously spread across thousands of accounts '
      'in commercial banks, reducing the need to borrow while holding cash.',
      'Elimination of the interest earned privately on public funds and of the associated '
      'incentives.',
      'A complete daily picture of government cash, which makes cash planning possible.',
      'Blocking of unauthorised accounts and of revenue diversion.',
      'Reduced cost of debt service, since borrowing no longer coexists with idle balances.',
    ]},
    {'note': 'The examinable criticism of the TSA is the strain it placed on deposit money '
             'banks, which lost substantial public sector deposits, and the administrative '
             'difficulty faced by agencies with genuine operational needs for local payments. '
             'A balanced answer states both sides.'},
  ]},

  {'n': '3.4', 't': 'The General Purpose Financial Statements', 'b': [
    {'p': 'The standardised templates issued with the National Chart of Accounts prescribe the '
          'form of the General Purpose Financial Statements. Under **cash basis IPSAS** the '
          'required statements are fewer than under **accrual basis IPSAS**.'},
    {'table': {'align': 'll', 'head': ['Cash basis IPSAS', 'Accrual basis IPSAS'], 'rows': [
      ['Statement of Cash Receipts and Payments',
       'Statement of Financial Performance'],
      ['Statement of Assets and Liabilities',
       'Statement of Financial Position'],
      ['Statement of Comparison of Budget and Actual Amounts',
       'Statement of Changes in Net Assets / Equity'],
      ['Notes to the financial statements, including a statement of accounting policies',
       'Statement of Cash Flows'],
      ['—', 'Statement of Comparison of Budget and Actual Amounts'],
      ['—', 'Notes, including a statement of accounting policies'],
    ]}},
    {'p': 'Each statement is examined in detail later: the cash basis statements in Chapter 14 '
          'and the accrual basis statements in Chapter 16.'},
    {'warn': 'The **Statement of Comparison of Budget and Actual Amounts** is required under '
             'both bases and is peculiar to the public sector. Because the budget is a legal '
             'authority rather than a management plan, comparison with it is a reporting '
             'obligation, not a management convenience. Candidates who omit it from a list of '
             'required statements lose an easy mark.'},
  ]},
 ],
 'formulas': [],
 'focus':
   'One or two Section A marks on the segments of the chart of accounts or on the meaning of '
   'GIFMIS, IPPIS and TSA. In Section B it appears as a discussion question — the benefits of a '
   'uniform chart of accounts, or the advantages and problems of the Treasury Single Account. '
   'Both are recall questions, and the segments should be learnt as a list of seven with an '
   'example each.',
 'errors': [
   'Listing only the administrative and economic segments; the chart has seven.',
   'Confusing GIFMIS (the financial management system) with IPPIS (the payroll platform) or '
   'with the TSA (the banking arrangement).',
   'Omitting the Statement of Comparison of Budget and Actual Amounts from the required '
   'statements.',
   'Describing the functional segment as the ministry; the ministry is the administrative '
   'segment, the function is health, education, defence and so on.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In the National Chart of Accounts, classification by ministry, department or agency '
         'is the',
    'o': ['economic segment', 'administrative segment', 'functional segment',
          'programme segment', 'fund segment'],
    'a': 1,
    'w': 'The administrative segment answers "who spent it". The economic segment answers "on '
         'what, by nature" and the functional segment "for what purpose of government".',
    'src': 'Chapter 3.2'},
   {'q': 'GIFMIS stands for',
    'o': ['Government Integrated Fiscal Management Information Service',
          'Government Integrated Financial Management Information System',
          'General Integrated Financial Monitoring Information System',
          'Government Internal Financial Management and Internal Systems',
          'Government Institutional Financial Management Information Service'],
    'a': 1,
    'w': 'It is the integrated platform covering budgeting, commitment control, payments, '
         'accounting and reporting, built on the National Chart of Accounts.',
    'src': 'Chapter 3.3'},
   {'q': 'The Treasury Single Account was fully implemented in Nigeria in',
    'o': ['2012', '2015', '2014', '2016', '2011'],
    'a': 1,
    'w': 'Full implementation followed the presidential directive of 2015, with collections '
         'sweeping into the CBN through Remita from September of that year.',
    'src': 'Chapter 3.3'},
   {'q': 'In the economic segment of the National Chart of Accounts, code series 4 represents',
    'o': ['Assets', 'Revenue', 'Liabilities', 'Expenditure', 'Net assets'],
    'a': 1,
    'w': 'The series run 1 assets, 2 liabilities, 3 net assets/equity, 4 revenue, '
         '5 expenditure.',
    'src': 'Chapter 3.2'},
   {'q': 'Which financial statement is required under BOTH cash basis and accrual basis IPSAS?',
    'o': ['Statement of Financial Performance',
          'Statement of Comparison of Budget and Actual Amounts',
          'Statement of Cash Flows', 'Statement of Changes in Net Assets',
          'Statement of Financial Position'],
    'a': 1,
    'w': 'Comparison with the budget is required under both bases, because the budget is a '
         'legal authority to spend rather than an internal plan.',
    'src': 'Chapter 3.4'},
  ],
  'theory': [
   {'q': 'Explain the objectives of the National Chart of Accounts, describe its segments, and '
         'discuss the benefits which the Treasury Single Account has brought to public '
         'financial management in Nigeria, together with the problems it has created.',
    'marks': 15,
    'a': [
      {'h4': 'Objectives of the National Chart of Accounts'},
      {'ol': [
        'To provide a **uniform classification** of all government receipts and payments across '
        'the Federal, State and Local Governments, in place of the incompatible classifications '
        'each previously operated.',
        'To make **consolidation** of the accounts of all tiers into government-wide financial '
        'statements possible.',
        'To align government reporting with the **IMF Government Finance Statistics Manual** '
        'and the UN Classification of the Functions of Government, so that Nigerian fiscal '
        'statistics are internationally comparable.',
        'To integrate the **budget with the accounts**, since the same codes are used for '
        'appropriation, for commitment and for recording actual expenditure, permitting direct '
        'comparison of budget and actual.',
        'To provide the asset, liability and net-asset codes necessary for **IPSAS-compliant '
        'accrual reporting**, which a purely cash-based classification did not contain.',
        'To supply the coding structure required by **GIFMIS**.',
      ]},
      {'h4': 'The segments'},
      {'p': 'The chart is multi-dimensional: each transaction carries a code in every segment '
            'simultaneously, so one posting supports every dimension of reporting.'},
      {'table': {'align': 'lll', 'head': ['Segment', 'Classifies by', 'Example'], 'rows': [
        ['Administrative', 'Ministry, department or agency incurring the transaction',
         'Federal Ministry of Education'],
        ['Economic', 'The nature of the receipt or payment',
         'Personnel cost; overhead; capital expenditure'],
        ['Functional', 'The purpose of government served', 'Education; health; defence'],
        ['Programme', 'The policy programme or project', 'Universal Basic Education'],
        ['Fund', 'The fund from which the money comes',
         'Consolidated Revenue Fund; Development Fund'],
        ['Geographical', 'The location of the activity', 'State; local government area'],
        ['Financing / donor', 'The source of finance',
         'Government of Nigeria; World Bank; bilateral donor'],
      ]}},
      {'h4': 'Benefits of the Treasury Single Account'},
      {'ol': [
        '**Consolidation of cash.** Balances formerly held in many thousands of accounts across '
        'commercial banks are now visible in one structure at the Central Bank, so that '
        'government knows daily what cash it actually has.',
        '**Reduced cost of borrowing.** Government previously borrowed at commercial rates '
        'while simultaneously holding large idle deposits. Netting the two has reduced debt '
        'service costs materially.',
        '**Elimination of leakage.** Revenue collected by agencies now sweeps automatically to '
        'the TSA rather than resting in accounts under agency control, which removed both the '
        'private interest earned on public money and much of the scope for diversion.',
        '**Better cash planning and budget execution.** A complete daily cash position permits '
        'realistic disbursement schedules rather than releases made in ignorance of the '
        'aggregate position.',
        '**Improved accountability and audit.** Every receipt and payment passes through a '
        'traceable channel, and unauthorised accounts were closed on implementation.',
        '**Support for the wider reform.** The TSA supplies the transaction data on which '
        'GIFMIS and IPSAS reporting depend.',
      ]},
      {'h4': 'Problems created'},
      {'ol': [
        '**Liquidity shock to the banking system.** Deposit money banks lost very large public '
        'sector deposits over a short period, which tightened liquidity, raised interbank rates '
        'and contributed to job losses in the sector.',
        '**Operational difficulty for agencies.** Institutions with genuine day-to-day payment '
        'needs — teaching hospitals, universities, embassies, agencies operating in remote '
        'areas — found centralised payment processing slow, and delays in releases disrupted '
        'operations.',
        '**Dependence on a single platform.** Reliance on one payment gateway and on the '
        'Central Bank\'s systems creates a single point of failure; downtime halts government '
        'payments nationally.',
        '**Transaction charges and disputes** over the fees payable on collections through the '
        'platform.',
        '**Incomplete coverage.** Some funds and some tiers of government remained outside the '
        'arrangement for a considerable period, limiting the completeness of the consolidated '
        'view.',
      ]},
      {'p': '**Conclusion.** The Treasury Single Account has been among the most effective of '
            'the public financial management reforms, chiefly because it removed opportunity '
            'rather than relying on exhortation: money that sweeps automatically cannot be '
            'diverted by an official who intends to divert it. The costs it imposed on the '
            'banking sector and on agency operations were real but largely transitional, and '
            'are outweighed by the improvement in control and in the cost of debt.'}],
    'src': 'Chapter 3.1–3.3'},
  ]},
}
