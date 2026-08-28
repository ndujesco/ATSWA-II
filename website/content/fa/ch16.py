CH = {
 'n': 16,
 't': 'Professional Ethics and Information Technology in Accounting',
 'brief': 'The IFAC fundamental principles, the threats to them and the safeguards, and the '
          'technologies now reshaping how accounting work is done.',
 'outcomes': [
   'State and explain the five fundamental principles of the IFAC Code',
   'Identify the five categories of threat and appropriate safeguards',
   'Apply the conceptual framework approach to an ethical dilemma',
   'Describe the advantages and disadvantages of computerised accounting systems',
   'Explain the relevance of cloud computing, blockchain, big data and artificial intelligence '
   'to the accountant',
 ],
 'secs': [
  {'n': '16.1', 't': 'The five fundamental principles', 'b': [
    {'p': 'The IFAC Code of Ethics for Professional Accountants binds members of ICAN and the '
          'other ABWA institutes. Five principles, and the mnemonic **PIPCO** holds them.'},
    {'table': {'head': ['Principle', 'What it requires'], 'align': 'll', 'rows': [
      ['**Professional behaviour**', 'Comply with relevant laws and regulations and avoid any '
       'conduct that discredits the profession'],
      ['**Integrity**', 'Be straightforward and honest in all professional and business '
       'relationships'],
      ['**Professional competence and due care**', 'Maintain knowledge and skill at the level '
       'required, and act diligently in accordance with applicable standards'],
      ['**Confidentiality**', 'Respect the confidentiality of information acquired, and do not '
       'disclose or use it for personal advantage'],
      ['**Objectivity**', 'Do not allow bias, conflict of interest or undue influence to override '
       'professional judgement'],
    ]}},
    {'h3': 'When confidentiality may be breached'},
    {'ol': [
      'Where disclosure is **permitted by law** and authorised by the client or employer.',
      'Where disclosure is **required by law** — for example, producing documents in legal '
      'proceedings, or reporting a suspected money laundering offence.',
      'Where there is a **professional duty or right** to disclose, not prohibited by law: '
      'complying with a quality review, responding to an inquiry by the institute, protecting '
      'the member\'s own professional interests in legal proceedings.',
    ]},
    {'warn': 'Confidentiality continues **after** the relationship ends. A former client\'s '
             'information is still confidential, and using it at a new employer breaches the '
             'principle even though the engagement is over.'},
  ]},

  {'n': '16.2', 't': 'Threats and safeguards', 'b': [
    {'p': 'The Code does not list every prohibited act. It requires a **conceptual framework '
          'approach**: identify threats, evaluate their significance, and apply safeguards to '
          'reduce them to an acceptable level — or decline the engagement.'},
    {'table': {'head': ['Threat', 'Arises when', 'Example'], 'align': 'lll', 'rows': [
      ['**Self-interest**', 'A financial or other interest inappropriately influences judgement',
       'Holding shares in an audit client; a contingent fee; undue fee dependence'],
      ['**Self-review**', 'The accountant reviews their own previous work or judgement',
       'Auditing financial statements you prepared'],
      ['**Advocacy**', 'The accountant promotes a client\'s position to the point that objectivity '
       'is compromised', 'Acting as an advocate in litigation for a client'],
      ['**Familiarity**', 'A long or close relationship makes the accountant too sympathetic',
       'A close relative in a senior finance role at the client; a very long tenure'],
      ['**Intimidation**', 'Actual or perceived pressure deters objective action',
       'Threat of dismissal or of litigation; a dominant client threatening to remove the audit'],
    ]}},
    {'h3': 'Safeguards'},
    {'ul': [
      'Created by the **profession or by legislation**: education and training requirements, '
      'continuing professional development, corporate governance codes, professional standards, '
      'monitoring and disciplinary procedures, external review.',
      'Created within the **work environment**: firm-wide policies on independence, rotation of '
      'senior personnel, an engagement quality review by a partner not on the team, consultation '
      'with a third party, using different teams for different services, and where nothing is '
      'sufficient, **declining or resigning from the engagement**.',
    ]},
    {'eg': {'t': 'Applying the framework', 'q': [
      {'p': 'You are the accountant of a company. The managing director asks you to delay '
            'recognising ₦40,000,000 of expenses until after the year end so that the profit '
            'target is met and the staff bonus is paid. He hints that your own contract renewal '
            'depends on your co-operation. Analyse this.'}],
      'a': [
      {'h4': 'Principles at risk'},
      {'ul': [
        '**Integrity** — deliberately deferring an expense that has been incurred misstates the '
        'financial statements and is not straightforward or honest.',
        '**Objectivity** — the pressure from the managing director and the personal consequence '
        'to your contract are influences that must not override judgement.',
        '**Professional competence and due care** — the accruals concept and IAS 1 require the '
        'expense in the period incurred; complying would breach the applicable framework.',
        '**Professional behaviour** — producing misleading statements discredits the profession '
        'and may constitute an offence under CAMA.']},
      {'h4': 'Threats'},
      {'ul': ['**Intimidation** — the implied threat to your contract renewal.',
              '**Self-interest** — your own employment and any bonus you would receive.']},
      {'h4': 'Response'},
      {'ol': [
        'Explain to the managing director why the treatment is not permitted, in writing, citing '
        'the accruals concept and the standard.',
        'Escalate within the entity — to the finance director, the audit committee, or the board.',
        'Take advice from the ethics helpline of your professional body, and from your own legal '
        'adviser, keeping a contemporaneous written record throughout.',
        'If the pressure continues and the statements would be materially misstated, **refuse to '
        'be associated with them**, and consider resignation.']},
      {'note': 'The examiner is looking for the structure — principles, then threats, then '
               'safeguards, then action — not for a moral essay. Documenting each step is itself '
               'a safeguard and is worth a mark.'}]}},
  ]},

  {'n': '16.3', 't': 'Computerised accounting systems', 'b': [
    {'table': {'head': ['Advantages', 'Disadvantages'], 'align': 'll', 'rows': [
      ['Speed and volume of processing', 'High initial cost of hardware, software and conversion'],
      ['Arithmetical accuracy is guaranteed', 'Requires trained staff and ongoing training'],
      ['One entry updates every affected record', 'Vulnerable to virus, hacking and data loss'],
      ['Reports available instantly and in many formats', 'System failure halts the whole operation'],
      ['Better internal control through access rights and audit trails',
       'A programming error is repeated in every transaction'],
      ['Lower long-run staff costs', 'Loss of the audit trail if not properly configured'],
      ['Data stored compactly and backed up', 'Risk of fraud on a large scale if controls are weak'],
    ]}},
    {'key': 'A computer removes **arithmetical** error, not **classification** error. Posting a '
            'repair to the vehicle account is just as wrong in Sage as it is in a handwritten '
            'ledger, and the machine will repeat it faithfully every month.'},
    {'h3': 'Controls in a computerised environment'},
    {'ul': [
      '**Input controls** — batch totals, hash totals, control totals, range and format checks, '
      'check digits, authorisation before entry.',
      '**Processing controls** — run-to-run totals, reasonableness checks, exception reports.',
      '**Output controls** — distribution lists, reconciliation of output to input, review of '
      'exception reports.',
      '**Storage and access controls** — passwords, access levels, encryption, backup and '
      'off-site storage, disaster recovery plans.',
    ]},
  ]},

  {'n': '16.4', 't': 'Emerging technologies', 'b': [
    {'ul': [
      '**Cloud computing** — accounting software and data hosted remotely and accessed over the '
      'internet. Lower up-front cost, automatic updating, access from anywhere, easier '
      'collaboration; against that, dependence on connectivity and on the provider, and questions '
      'of data sovereignty and confidentiality.',
      '**Blockchain** — a distributed ledger in which transactions are recorded in blocks, '
      'cryptographically linked, replicated across many nodes and effectively **immutable**. It '
      'raises the possibility of triple-entry accounting and continuous audit, and reduces the '
      'need for reconciliation between counterparties.',
      '**Big data and analytics** — the volume, velocity and variety of data now available allow '
      'the accountant to test entire populations rather than samples, and to move from reporting '
      'the past to predicting the future.',
      '**Artificial intelligence and machine learning** — automates routine classification, '
      'invoice matching and anomaly detection; frees the accountant for judgement and advice, but '
      'raises questions of explainability and of responsibility for the output.',
      '**Robotic process automation** — software robots performing repetitive rule-based tasks '
      'such as data entry and reconciliation.',
      '**Spreadsheets** — still the most widely used analytical tool in accounting, and still the '
      'largest single source of undetected error. Version control, cell protection, documented '
      'assumptions and independent review are essential.',
    ]},
    {'note': 'The examiner\'s recurring theme is that technology changes **how** accounting work '
             'is done without changing **what** the accountant is responsible for. The '
             'fundamental principles apply identically to work done by a machine, and the '
             'accountant remains answerable for the output.'},
  ]},
 ],
 'focus':
   'A short chapter that reliably supplies short-answer and Section A marks, and increasingly a '
   'Section B part on ethics or on technology. Learn the five principles and the five threats as '
   'lists you can write out in thirty seconds. Ethics scenarios are marked on **structure** — '
   'principles, threats, safeguards, action — so answer in that order every time.',
 'errors': [
   'Listing only three or four fundamental principles. There are five.',
   'Confusing self-interest with self-review. Self-review is reviewing your own earlier work.',
   'Saying confidentiality is absolute. There are circumstances in which disclosure is required '
   'or permitted.',
   'Writing a moral essay on an ethics scenario instead of applying the framework.',
   'Claiming a computerised system eliminates errors. It eliminates arithmetical errors only.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Which of the following is NOT one of the five fundamental principles of the IFAC Code?',
    'o': ['Integrity', 'Objectivity', 'Professional competence and due care', 'Independence',
          'Confidentiality'],
    'a': 3,
    'w': 'Independence is a state of mind and appearance required in assurance engagements; it is '
         'not itself one of the five fundamental principles. The fifth is professional behaviour.',
    'src': 'Chapter 16.1'},
   {'q': 'An accountant audits financial statements that the same firm prepared. The threat is',
    'o': ['self-interest', 'self-review', 'advocacy', 'familiarity', 'intimidation'],
    'a': 1,
    'w': 'A self-review threat arises when an accountant reviews their own previous work or '
         'judgement, because they are unlikely to identify their own errors objectively.',
    'src': 'Chapter 16.2'},
   {'q': 'A distributed ledger technology that records transactions in a secured, transparent and '
         'tamper-resistant manner is called',
    'o': ['cloud computing', 'a blockchain', 'a data warehouse', 'robotic process automation',
          'an expert system'],
    'a': 1,
    'w': 'A blockchain links cryptographically hashed blocks across a distributed network, making '
         'past records effectively immutable — which is why it is described as immutable, '
         'decentralised and tamper-proof.',
    'src': 'Chapter 16.4'},
   {'q': 'A client threatens to dismiss the accountant unless a questionable accounting treatment '
         'is accepted. This is a threat to objectivity described as',
    'o': ['self-interest', 'advocacy', 'familiarity', 'intimidation', 'self-review'],
    'a': 3,
    'w': 'Intimidation arises where actual or perceived pressures, including attempts to exercise '
         'undue influence, deter the accountant from acting objectively.',
    'src': 'Chapter 16.2'},
   {'q': 'Which of the following is NOT an advantage of a computerised accounting system?',
    'o': ['Faster processing of large volumes', 'Guaranteed arithmetical accuracy',
          'Instant availability of reports',
          'Elimination of the need for classification judgement',
          'A single entry updates all affected records'],
    'a': 3,
    'w': 'A computer applies whatever classification it is told to apply. Deciding whether an item '
         'is capital or revenue remains a matter of judgement, and an error in that judgement is '
         'repeated faithfully.',
    'src': 'Chapter 16.3'},
  ],
  'theory': [
   {'q': 'State the FIVE fundamental principles of the IFAC Code of Ethics and explain each '
         'briefly. Identify the FIVE categories of threat to compliance with them.',
    'marks': 10,
    'a': [
      {'h4': 'The fundamental principles'},
      {'ol': [
        '**Integrity** — to be straightforward and honest in all professional and business '
        'relationships, and not to be knowingly associated with information that is materially '
        'false or misleading.',
        '**Objectivity** — not to allow bias, conflict of interest or the undue influence of '
        'others to override professional or business judgement.',
        '**Professional competence and due care** — to maintain professional knowledge and skill '
        'at the level required to ensure a competent service, and to act diligently in accordance '
        'with applicable technical and professional standards.',
        '**Confidentiality** — to respect the confidentiality of information acquired as a result '
        'of professional and business relationships, and not to disclose it without proper '
        'authority or use it for personal advantage.',
        '**Professional behaviour** — to comply with relevant laws and regulations and to avoid '
        'any conduct that the accountant knows or should know might discredit the profession.']},
      {'h4': 'Categories of threat'},
      {'ol': [
        '**Self-interest** — a financial or other interest will inappropriately influence judgement.',
        '**Self-review** — the accountant will not appropriately evaluate the results of a '
        'previous judgement made, or service performed, by themselves or their firm.',
        '**Advocacy** — the accountant will promote a client\'s or employer\'s position to the '
        'point that objectivity is compromised.',
        '**Familiarity** — a long or close relationship will make the accountant too sympathetic '
        'to the other party\'s interests or too accepting of their work.',
        '**Intimidation** — actual or perceived pressures, including attempts to exercise undue '
        'influence, will deter the accountant from acting objectively.']},
      {'note': 'A complete answer adds that the Code requires a conceptual framework approach: '
               'identify the threat, evaluate its significance, and apply safeguards to reduce it '
               'to an acceptable level, declining or resigning where no adequate safeguard exists.'}],
    'src': 'Chapter 16.1'},
  ]},
}
