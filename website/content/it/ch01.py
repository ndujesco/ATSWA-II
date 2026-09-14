CH = {
 'n': 1,
 't': 'Data and Information',
 'brief': 'System theory and control systems; the difference between data and information; how '
          'data is represented inside a computer; and the classification and evolution of '
          'computer hardware.',
 'outcomes': [
   'Explain the concept of a system and identify its elements, environment and subsystems',
   'Distinguish coupling from decoupling and open from closed systems',
   'Describe feedback and feed-forward control systems',
   'Distinguish data from information and state the attributes of good information',
   'Describe an information system and the subsystems of an accounting information system',
   'Represent characters and numbers in binary, and convert between number bases',
   'State the elements of a database and how they relate',
   'Describe the five generations of computers and classify computers by type and size',
 ],
 'secs': [
  {'n': '1.1', 't': 'System theory', 'b': [
    {'p': 'System theory is a body of scientific principles that can be applied to systems of '
          'every kind — business systems, manufacturing systems, information systems, and the '
          'control systems for quality, production, budgets, cost and cash that together form a '
          'management information system.'},
    {'def': {'t': 'System', 'd': 'a combination of interrelated elements, called subsystems, '
                  'organised so as to ensure the efficient functioning of the whole. A system '
                  'element may be a tangible object (data, information) or an event (an '
                  'anniversary day).'}},
    {'p': 'Achieving that efficient functioning needs a high degree of **coordination** between '
          'the subsystems, each of which is designed for a specific purpose. Examples of systems '
          'include business systems, manufacturing systems, service systems, information systems, '
          'computer-based management information systems and stock control systems.'},
    {'h3': 'Objectives and trade-offs'},
    {'p': 'A system must have an **objective or goal**, and in practice every system has more '
          'than one. A business organisation might aim to:'},
    {'ol': [
      'generate a reasonable financial return for shareholders;',
      'maintain a high market share;',
      'increase productivity annually;',
      'offer an up-to-date product range of high quality and proven reliability;',
      'develop a reputation as a responsible employer;',
      'acknowledge its social responsibilities; and',
      'grow and survive autonomously.',
    ]},
    {'p': 'These objectives usually **conflict**, so the system must reach a compromise or '
          'trade-off between them. A wish to reduce production cost, for example, may conflict '
          'with health and safety at work, the cost of treating waste and effluent, the quality '
          'of goods produced, or spending on new technology and research and development.'},
    {'h3': 'System environment and boundary'},
    {'p': 'The **environment** of a system is the set of elements that surround it and interact '
          'with it but are **not part of it** — for a business system, the government and the '
          'competitors. A **boundary** separates the system from its environment: anything '
          'inside the boundary is part of the system, anything outside it is environment. Which '
          'elements fall inside depends on the problem being studied — in a study of batch '
          'turnaround time, data-entry operators are inside the system; in a study of how to '
          'make one program run faster, people are in the environment and only technical '
          'details are inside.'},
    {'h3': 'Constraints'},
    {'p': 'Every system has **constraints** — limiting factors that restrict its capacity to '
          'meet its objectives. Constraints on the objective of profit maximisation include:'},
    {'ol': [
      'scarcity of key resources such as cash or skilled labour;',
      'technological constraints limiting what goods and services can be produced;',
      'economic constraints;',
      'political and legal constraints;',
      'product completion time; and',
      'responsibilities towards society and for preserving the environment from pollution.',
    ]},
    {'note': 'Question 2 of the study text\'s theory set asks for "any FOUR constraints that can '
             'restrict the objectives of profit maximisation" — this is the list to reproduce.'},
    {'h3': 'Subsystems'},
    {'p': 'Every system can be broken down into subsystems, and each subsystem into '
          'sub-subsystems, which interact by communication or observation. Subsystems may be '
          'differentiated by:'},
    {'ol': [
      '**function** — e.g. production, finance, marketing, sales, personnel;',
      '**space** — e.g. Northern-area and Southern-area sales managers;',
      '**time** — e.g. morning, afternoon and evening shift managers;',
      '**people** — e.g. skilled and unskilled;',
      '**formality** — various ways of getting information; and',
      '**automation** — various processes carried out by the computer system.',
    ]},
    {'eg': {'tag': 'Illustration 1', 't': 'Subsystems of a manufacturing organisation', 'open': True,
      'q': [
      {'p': 'Show how a manufacturing organisation is a system with subsystems, and how one '
            'subsystem breaks down further.'}],
      'a': [
      {'p': '**(a)** The manufacturing organisation, divided by **function**, has subsystems: '
            'personnel department, marketing department, audit department, production department, '
            'information technology (IT), maintenance department and purchasing department.'},
      {'p': '**(b)** The production subsystem divides into sub-subsystems: machine operations '
            'control, work-handling, power supply and material production.'}]}},
    {'h3': 'Coupling and decoupling'},
    {'def': {'t': 'Coupling', 'd': 'a measure of the degree or extent of the dependence of the '
                  'subsystems on one another.'}},
    {'p': 'If subsystems are **over-integrated (over-coupled)** they become too complex to '
          'operate, and if one part fails the others are affected and may fail too. '
          '**Decoupling** — in both a physical and an information sense — gives subsystems more '
          'independence in planning and control: the system becomes less complex, more flexible, '
          'and better able to absorb random shocks without disruption. Decoupling generally '
          'leads to **system stability**, which is essential for survival in a dynamic '
          'environment; subsystems then exist separately on a functional basis but are '
          'coordinated by the chief executive for the overall objectives.'},
    {'h3': 'Logical and physical description; the three components'},
    {'p': 'A system has a **logical description** (the essential elements, irrespective of how '
          'they are implemented) and a **physical description** (the implementation). In a '
          'computer-based information system, *input, processing and output* are the logical '
          'description; a keyboard as the input device and a monitor or printer as the output '
          'device are the physical description. The three logical components are:'},
    {'ul': [
      '**INPUT** — what the system needs in order to operate: matter, energy, human effort, '
      'data or information.',
      '**PROCESS** — transforms input into output: tasks performed by humans, plant or machines.',
      '**OUTPUT** — the results of processing: e.g. finished products and work-in-progress in a '
      'manufacturing system.',
    ]},
    {'h3': 'Open and closed systems'},
    {'table': {'head': ['Open system', 'Closed system'], 'align': 'll', 'rows': [
      ['Interacts with its environment to collect and exchange information and to transact '
       'business', 'Does not interact with its environment for information or business'],
      ['Adapts to environmental change in order to survive; reacts quickly to competition and '
       'other threats', 'Self-contained — has neither input nor output'],
      ['**All business systems are open systems**',
       'No true closed system exists; the term is used for systems that interact only partially '
       'with their environment (an approximation is a reaction in a sealed, insulated container)'],
    ]}},
    {'h3': 'Classification of open systems'},
    {'p': 'Open systems are classified by their **degree of reaction to the environment** when '
          'producing output:'},
    {'ol': [
      '**Deterministic (mechanistic)** — states and activities follow each other in a '
      'completely predictable way; the system runs on standardised rules that restrict its '
      'ability to react. Outputs from given inputs can be measured without error. *A computer '
      'system is the example.* Business and economic systems are **not** deterministic.',
      '**Probabilistic (stochastic)** — some states can be predicted only with varying degrees '
      'of probability, because the system is subject to random influences from the environment. '
      'Its state is known only within specified limits. *Business and economic systems are '
      'probabilistic* — e.g. stocks of materials and finished goods vary with demand and supply.',
      '**Adaptive (self-organising, cybernetic)** — adapts and reacts to a stimulus; the same '
      'input does not always produce the same output. It alters its own inputs as a result of '
      'measuring its outputs, monitoring its own behaviour to optimise performance. *Animals, '
      'humans and business organisations are examples*; a physical example is the '
      'thermostat-controlled water boiler, and a computerised stock-ordering system is adaptive '
      'in nature.',
    ]},
    {'def': {'t': 'Cybernetics', 'd': 'the science of communication and control in man and '
                  'machine systems. From the Greek *kybernetes* (via Latin *gubernator*), '
                  'meaning governor or controller.'}},
  ]},

  {'n': '1.2', 't': 'Control systems', 'b': [
    {'p': 'A system must be **controlled** to keep it steady or let it change safely, because '
          'unpredictable disturbances enter the system and push actual results away from the '
          'objective. In a business, such disturbances include the entry of a powerful new '
          'competitor\'s technology, an unexpected rise in labour costs, a supplier\'s failure '
          'to deliver, or new government legislation.'},
    {'p': 'Control systems are often **structured separately** from the systems they control: '
          'the production control system controls the production quantity, the quality control '
          'system controls production quality, and the cost control system controls the cost of '
          'production. Their job is to detect variations in a system\'s behaviour so that '
          'control signals can be sent to the right manager for adjustment.'},
    {'h3': 'Elements of control'},
    {'ol': [
      '**Planning** — determining objectives or parameters: standard times, the level of '
      'production activity required, the level of sales required, maximum expenditure allowed, '
      'and required performance levels.',
      '**Collecting facts** — recording data on actual times taken, production achieved, sales '
      'achieved, expenditure incurred and actual performance.',
      '**Comparison** — computing the difference between objective and actual, identifying '
      'variances and reporting the significant deviations.',
      '**Corrective action** — action by the relevant manager (the *effector*) to restore a '
      'steady state.',
    ]},
    {'key': 'The four elements — plan, collect facts, compare, correct — are a recurring '
            'short-answer and MCQ target. "Leading" is **not** one of them (study text Q7 and '
            'Q25), and neither is "directing".'},
    {'h3': 'Open-loop and closed-loop control'},
    {'table': {'head': ['Open-loop control', 'Closed-loop control'], 'align': 'll', 'rows': [
      ['Control is exercised regardless of the output produced — by external intervention',
       'Part of the output is fed back into the system as input'],
      ['Physical examples: automatic light switches; traffic lights',
       'Many are self-regulating, with a built-in control mechanism'],
      ['No feedback', 'Contains the essential element of **feedback**; business systems '
       'contain integrated closed-loop control systems doing continuous monitoring'],
    ]}},
    {'h3': 'Feedback'},
    {'def': {'t': 'Feedback', 'd': 'part of the output of a system that is returned to the input '
                  'as a means of control.'}},
    {'ul': [
      '**Negative feedback** — where actual output differs from desired output, the deviation '
      '(error) is detected and action is taken **in the opposite direction** to counteract it. '
      'If a production line should make 10,000 units a month but makes 9,000, the 1,000-unit '
      'shortfall triggers corrective action to raise output back to 10,000. *Most business '
      'control systems are negative-feedback systems.*',
      '**Positive feedback** — action is taken to **enlarge (amplify)** the detected deviation. '
      'It applies, for example, to servo-mechanisms, where a small manual force is detected and '
      'amplified to achieve a defined purpose.',
    ]},
    {'h3': 'Feed-forward control'},
    {'p': 'Management can also act **proactively**. Under feed-forward control, error signals '
          'are monitored over time and used to **forecast** the future performance of an '
          'organisational unit, so that the historical trend or inherent behaviour of the '
          'system is allowed for when setting control parameters for future operations. '
          'Feed-forward control monitors both process operations and inputs to **predict '
          'potential deviations** and make adjustments *before* problems occur — rather than '
          'reacting after the event, as feedback does.'},
  ]},

  {'n': '1.3', 't': 'The nature of data and information', 'b': [
    {'def': {'t': 'Data', 'd': 'raw facts, events, numbers and transactions that have been '
                  'collected, recorded and stored but not yet processed. Data consist of '
                  'numbers and characters (alphabets and special symbols) used to record facts '
                  'and events.'}},
    {'def': {'t': 'Information', 'd': 'processed data — the meaningful, coherent form that data '
                  'takes after a series of processing operations (addition, subtraction, '
                  'comparison, sorting, rearrangement).'}},
    {'p': 'The costs of five different items are **data**; the total or average cost derived '
          'from them is **information**. Information must be communicated to and received by a '
          'manager who uses it for a decision. What is information to one manager is often data '
          'needing further processing to another — the two terms are confused because both are '
          'dynamic: the output of one computation is the input (data) of the next.'},
    {'table': {'cap': 'Data used as input, information as output, at each stage', 'align': 'lll',
      'head': ['Operation', 'Data (input)', 'Information (output)'], 'rows': [
      ['Typing a student\'s name, matriculation number and scores',
       'Characters — letters (A–Z, a–z), digits (0–9), special characters (+ − * /)',
       'Sets of characters (words) — "Ade", "70", "Sola"'],
      ['Computing a class average in Computer Science',
       'Each student\'s test score', 'The class average score'],
      ['Computing a school average', 'Each class\'s average score', 'The school\'s average score'],
    ]}},
    {'table': {'cap': 'Distinctions between data and information', 'align': 'll',
      'head': ['Data', 'Information'], 'rows': [
      ['Raw, unchanged fact', 'Organised and sorted fact'],
      ['Serves as **input** into the computer system', 'Serves as **output** from the system'],
      ['Observation and recording produce it', 'Analysis of data produces it'],
      ['The lowest level of knowledge', 'The second level of knowledge'],
      ['By itself, not significant', 'Significant'],
    ]}},
    {'h3': 'Attributes of good information'},
    {'ol': [
      'detailed enough to allow an effective decision, with an appropriate level of detail for '
      'the recipient — broad in scope for top management, very detailed at operating level;',
      'relates to the current situation and has an acceptable level of **integrity**;',
      'produced at an **optimum cost**, and compatible with the system\'s response-time needs;',
      'easily **understood** by the recipient — using charts, diagrams and tables where '
      'helpful; concise, with no unnecessary redundancy;',
      'precise, with an acceptable level of **accuracy** (bank balances to two decimal places); '
      'produced at regular intervals and relevant to its purpose;',
      '**verifiable** — many knowledgeable people acting independently would produce the same '
      'information;',
      'arranged or organised to suit the purpose for which it is needed; and',
      'communicated through the **right channel** to the recipient.',
    ]},
    {'warn': 'Study text MCQ 30 asks which is **not** an attribute of good information; the key '
             'answer is "must be in coded form". Good information must be relevant, timely, '
             'reliable, and simple/understandable — not necessarily coded.'},
    {'h3': 'Types of information'},
    {'table': {'head': ['Quantitative information', 'Qualitative information'], 'align': 'll',
      'rows': [
      ['Deals with the magnitude of variables, their variability or absolute values',
       'Relates to the attributes of an entity — quality factors; not exact, but useful for '
       'comparative measurement'],
      ['Examples: annual sales of a production company; variation in the wages of low-level '
       'staff; prices of goods; number of hours worked on a production line',
       'Examples: the standard of a finished product\'s paintwork or electroplating; variation '
       'of tolerances of manufactured parts (deviation from standard dimensions)'],
    ]}},
    {'h3': 'Value of information'},
    {'p': 'The value of information is the **perception of the receiver** — the change in the '
          'user\'s behaviour or action it produces, less the cost of generating it. A message '
          'can carry three meanings: what the sender intended to send, what the message '
          'actually contains, and what the receiver understood. The information specialist must '
          'know what the recipient expects and be familiar with the recipient\'s terminology '
          'and background. Value is enhanced by:'},
    {'ul': [
      'avoiding technical jargon;',
      'regular feedback from receiver to sender;',
      'gaining the confidence of the receiver;',
      'avoiding excessive detail;',
      'reducing noise to the barest minimum;',
      'using a proper and effective communication channel; and',
      'producing the information on time.',
    ]},
  ]},

  {'n': '1.4', 't': 'Information systems and the Accounting Information System', 'b': [
    {'def': {'t': 'Information system', 'd': 'a set of interconnected procedures whose purpose '
                  'is to provide managers at all levels and in all functions with the '
                  'information they need to make timely and effective decisions. Equivalently, '
                  'a combination of people, hardware, software, communication networks and data '
                  'resources that collects, transforms and provides information for timely, '
                  'effective decision-making.'}},
    {'p': 'Those decisions are for **planning, directing and controlling** the activities the '
          'manager is responsible for. Every information system has:'},
    {'ol': [
      'procedures for originating and/or collecting data;',
      'procedures that sort and classify data, perform arithmetic and logical operations, hold '
      'data as records for immediate or future use, and summarise, analyse and check it for '
      'accuracy — together, the **processing** of data; and',
      'procedures for communicating the processed data to the appropriate managers.',
    ]},
    {'h3': 'The Accounting Information System (AIS)'},
    {'p': 'An **Accounting Information System** consists of **people, procedures and information '
          'technology**. It performs three functions:'},
    {'ol': [
      'it **collects and stores** data about activities and transactions, so the organisation '
      'can review what has happened;',
      'it **processes** data into information useful for planning, executing and controlling '
      'activities; and',
      'it provides **controls** to safeguard the organisation\'s assets, including its data — '
      'ensuring data is available when needed, and is accurate and reliable.',
    ]},
    {'p': 'It also helps analyse information presented in payroll/payslips, stock reports, lists '
          'of debtors and creditors, cost summaries, budget reports and labour-turnover '
          'statistics. The AIS differs from other information systems in its **focus on '
          'accountability and control**.'},
    {'h3': 'The five subsystems (transaction cycles) of an AIS'},
    {'ol': [
      '**Expenditure** cycle — buying and paying for the goods and services the organisation '
      'uses.',
      '**Production** cycle — converting raw materials and labour into finished products (only '
      'manufacturing organisations have this).',
      '**Human resources / payroll** cycle — hiring and paying employees.',
      '**Revenue** cycle — selling goods or services and collecting payment.',
      '**Financing** cycle — obtaining the funds to run the organisation, repaying creditors '
      'and distributing profits to investors.',
    ]},
    {'p': 'These point to the main work of professional accountants: accounting systems and '
          'financial reporting; long-term strategic planning; managing the accounting and '
          'finance function; internal consulting; short-term budgeting; financial and economic '
          'analysis; process improvement; computer systems and operations; performance '
          'evaluation of the organisation; and customer and product profitability analysis.'},
    {'h3': 'Benefits of information systems'},
    {'ol': [
      '**Operational efficiency** — routine tasks done faster, cheaper, neater and more '
      'accurately (transaction-processing software, word processing, spreadsheets).',
      '**Functional effectiveness** — decision-support software that helps managers decide '
      'better.',
      '**Better and improved services** — ATMs, e-commerce, travel-agent reservation systems.',
      '**Better product selection** — information helps banks, insurers and financial-services '
      'firms select what to offer; products differentiated mainly by the information in them '
      'are **information-intensive products**.',
      '**Competitive advantage** — information and new information-technology products can give '
      'a firm an advantage over rivals in the same industry.',
    ]},
    {'h3': 'Disadvantages of information systems'},
    {'ol': [
      '**Ease of fraud** — a system that makes any user efficient also makes a fraudster '
      'efficient.',
      '**Data loss** — without regular back-ups, a disaster can destroy an organisation\'s '
      'information, leading to legal liability and possibly collapse.',
      '**GIGO effect** — *garbage in, garbage out*: wrong data produces wrong information and '
      'wrong decisions.',
      '**Deceptive information** — statistical information, if not well explained, can be '
      'misused.',
    ]},
    {'h3': 'Roles of information in the accounting environment'},
    {'ul': [
      'identifies activities requiring action (a cost report with a large variance prompts '
      'investigation);',
      'reduces uncertainty and provides a basis for choosing between alternatives (setting '
      'prices, credit policies);',
      'makes the accountant\'s decision-making faster and the output more accurate;',
      'helps develop strategies and formulate policies for the survival of the profession;',
      'enables effective planning and control;',
      'allows proactive response to rapidly changing conditions;',
      'keeps accountants abreast of government policy and regulation;',
      'gives insight into the activities of professional competitors; and',
      'helps meet customers\' requests and maintain their patronage and goodwill.',
    ]},
  ]},

  {'n': '1.5', 't': 'Information technology', 'b': [
    {'p': 'The definition of an **information system** says nothing about mechanisation — it '
          'describes how information is *used*, not how it is obtained. In **information '
          'technology (IT)**, processing is carried out with the help of electronic machines: '
          'IT is a computer-based information system (CBIS) in which the computer plays a major '
          'role. Aspects of electronic technology include:'},
    {'ol': [
      'microcomputers for processing and storing information;',
      'electronic spreadsheets for modelling business problems;',
      'word-processing software for preparing standard reports and correspondence at speed;',
      'electronic mail (e-mail), which partly replaces the physical postal system;',
      'electronic trading (e-commerce, e-marketing) and electronic banking, principally '
      'electronic money transfer;',
      'the electronic library, letting a business operate more efficiently than its '
      'competitors;',
      'electronic funds transfer — moving money between bank accounts electronically; and',
      'data transmission — sending data electronically from one place to another.',
    ]},
  ]},

  {'n': '1.6', 't': 'Types of decision', 'b': [
    {'p': 'One purpose of the AIS is to provide information for management decisions, and IT '
          'helps it do so. Decisions are classified by their **degree of structure** and by '
          'their **scope**.'},
    {'h3': 'By structure'},
    {'table': {'head': ['Type', 'Character', 'Example / support'], 'align': 'lll', 'rows': [
      ['Highly structured', 'Repetitive, routine, well understood; can be delegated to '
       'lower-level staff and even automated',
       'Granting credit to established customers, using PIN, credit limit and current balance'],
      ['Semi-structured', 'Incomplete rules; needs subjective judgement to supplement formal '
       'data analysis',
       'Setting a marketing budget for a new product; supported by neural systems, decision '
       'support systems (DSS), executive information systems (EIS)'],
      ['Unstructured', 'Non-recurring, non-routine; no model or framework exists; needs '
       'judgement and intuition',
       'Choosing a magazine cover, hiring senior management, choosing a research project; '
       'supported by aids that gather information from diverse sources'],
    ]}},
    {'h3': 'By scope'},
    {'ol': [
      '**Operational control** — the effective and efficient performance of specific tasks; '
      'lower-level supervisors face structured or semi-structured decisions (inventory '
      'management, extending credit).',
      '**Management control** — the effective and efficient use of resources to accomplish '
      'organisational objectives; middle managers face semi-structured decisions (budgeting, '
      'human-resource practices, research projects, product improvement).',
      '**Strategic planning** — establishing organisational objectives and the policies to '
      'achieve them; top management faces unstructured and semi-structured decisions (setting '
      'financial and accounting policies, developing new product lines, acquiring businesses).',
    ]},
  ]},

  {'n': '1.7', 't': 'Data representation in a computer', 'b': [
    {'p': 'There are two types of data: **characters** and **numbers**. A character is an '
          'alphabet or any special symbol — the 26 uppercase letters, the 26 lowercase '
          'letters, punctuation marks, and special symbols such as `! ^ * + - _`. A number is '
          'composed of the ten decimal digits 0–9. A string of alphabets and numbers together '
          'is **alphanumeric**.'},
    {'h3': 'External and internal representation'},
    {'ul': [
      '**External representation** — data in the ordinary language of the user (English '
      'alphabets for characters). A document presented for coding is in external '
      'representation.',
      '**Internal representation** — the physical devices that store and process data are '
      '**two-state devices**: a punched card (hole present / absent), a magnetic surface '
      '(magnetised one way or the other), a conducting device such as a semiconductor '
      '(conducting / non-conducting). Every switch has two states — call them **0 and 1** (OFF '
      'and ON).',
    ]},
    {'def': {'t': 'Bit', 'd': 'a **bi**nary digi**t** — one of the two symbols 0 and 1. A bit '
                  'is the smallest unit of data in a computer system.'}},
    {'p': 'Characters are coded as strings of bits. The number of bits per string depends on '
          'the computer\'s architecture. With $n$ bits, the number of distinct characters that '
          'can be represented is $2^{n}$: a 2-bit computer can represent $2^2 = 4$ characters '
          '(00, 01, 10, 11); a 3-bit computer $2^3 = 8$; a 4-bit computer $2^4 = 16$.'},
    {'tex': '\\text{Distinct characters with } n \\text{ bits} = 2^{n}', 'tag': '(1.1)'},
    {'p': 'Ordinary use needs 26 + 26 + 10 + 36 = **98** distinct characters (uppercase, '
          'lowercase, digits, and about 36 special characters). We need $2^{n} \\ge 98$; since '
          '$2^{6} = 64$ and $2^{7} = 128$, **$n = 7$** — a 7-bit code is adequate.'},
    {'table': {'cap': 'Standard character-coding forms', 'align': 'lll',
      'head': ['Code', 'Stands for', 'Bits per character'], 'rows': [
      ['BCD', 'Binary Coded Decimal', '4'],
      ['ASCII', 'American Standard Code for Information Interchange', '7'],
      ['EBCDIC', 'Extended Binary Coded Decimal Interchange Code (developed by IBM)', '8'],
    ]}},
    {'def': {'t': 'Byte', 'd': 'a string of bits used to represent one character. In standard '
                  'practice **1 byte = 8 bits** — one character (an alphabet, digit or special '
                  'character).'}},
    {'p': 'A **word** is a combination of 2 bytes, so **1 word = 2 bytes = 16 bits**. In IT, '
          '$2^{10} = 1024$ is called a **kilo**; in a business context 1 kilo is taken as '
          '$10^{3}$, a close approximation.'},
    {'table': {'cap': 'Units of storage', 'align': 'll', 'head': ['', ''], 'rows': [
      ['1,000 bytes ($10^{3}$)', '1 kilobyte (1 KB)'],
      ['$10^{3}$ KB', '1 megabyte (1 MB)'],
      ['$10^{3}$ MB', '1 gigabyte (1 GB)'],
      ['$10^{3}$ GB', '1 terabyte (1 TB)'],
    ]}},
    {'note': 'A combination of **4 bits** is a **nibble** (study text MCQ 21). $10^{12}$ bytes '
             '(that is, $10^{3}$ GB) is a **terabyte** (MCQ 32).'},
    {'h3': 'Data train / data stream'},
    {'p': 'In ASCII, A = 1000001, E = 1000101, J = 1001010, T = 1010100, SPACE = 0100000, '
          'M = 1001101, O = 1001111. The internal representation of "M.O. AJE" is the sequence '
          'of these codes (the full stops after M and O are also coded). Such a sequence is a '
          '**data train** or **data stream** — a sequence of characters that flows into or out '
          'of a process, either an input stream or an output stream.'},
    {'h3': 'Converting a decimal integer to binary'},
    {'p': 'Divide by 2 repeatedly, recording the remainder each time; read the remainders from '
          'bottom to top.'},
    {'eg': {'tag': 'Example 1', 't': 'Convert 4903 to binary', 'open': True, 'q': [
      {'p': 'Convert the decimal number 4903 to a binary number.'}],
      'a': [
      {'pre': '2 | 4903\n2 | 2451  r 1\n2 | 1225  r 1\n2 |  612  r 1\n2 |  306  r 0\n'
              '2 |  153  r 0\n2 |   76  r 1\n2 |   38  r 0\n2 |   19  r 0\n2 |    9  r 1\n'
              '2 |    4  r 1\n2 |    2  r 0\n2 |    1  r 0\n         r 1'},
      {'tex': '4903_{10} = 1001100100111_{2}'}]}},
    {'eg': {'tag': 'Example 2', 't': 'Convert 29 to binary', 'open': True, 'q': [
      {'p': 'Convert the decimal number 29 to a binary number.'}],
      'a': [
      {'pre': '2 | 29\n2 | 14  r 1\n2 |  7  r 0\n2 |  3  r 1\n2 |  1  r 1\n       r 1'},
      {'tex': '29_{10} = 11101_{2}'}]}},
    {'h3': 'Converting a binary number to decimal'},
    {'p': 'Attach the weights $2^{0}, 2^{1}, 2^{2}, \\dots$ from the rightmost bit leftwards, '
          'and sum bit × weight.'},
    {'eg': {'tag': 'Worked', 't': '11101 and 100111 to decimal', 'open': True, 'q': [
      {'p': 'Convert (a) 11101 and (b) 100111 from binary to decimal.'}],
      'a': [
      {'tex': '\\textbf{(a)}\\quad 1{\\cdot}2^{4} + 1{\\cdot}2^{3} + 1{\\cdot}2^{2} + '
              '0{\\cdot}2^{1} + 1{\\cdot}2^{0} = 16 + 8 + 4 + 0 + 1 = 29_{10}'},
      {'tex': '\\textbf{(b)}\\quad 1{\\cdot}2^{5} + 0 + 0 + 1{\\cdot}2^{2} + 1{\\cdot}2^{1} + '
              '1{\\cdot}2^{0} = 32 + 0 + 0 + 4 + 2 + 1 = 39_{10}'}]}},
    {'h3': 'Computer representation of fractions'},
    {'p': 'A binary fraction is interpreted with negative powers of 2: '
          '$0.1101_{2} = 1{\\cdot}2^{-1} + 1{\\cdot}2^{-2} + 0{\\cdot}2^{-3} + 1{\\cdot}2^{-4} '
          '= 0.5 + 0.25 + 0 + 0.0625 = 0.8125_{10}$. The weights to disintegrate a decimal '
          'fraction into are $0.5, 0.25, 0.125, 0.0625, 0.03125, \\dots$'},
    {'eg': {'tag': 'Examples 4–7', 't': 'Decimal fractions to binary', 'open': True, 'q': [
      {'p': 'Convert (4) 0.625, (5) 39.8125 and — by the multiplication method — (6) 0.625 and '
            '(7) 0.8125 to binary.'}],
      'a': [
      {'p': '**(4)** $0.625 = 0.5 + 0.125 = 2^{-1} + 0 + 2^{-3} = 0.101_{2}$.'},
      {'p': '**(5)** Integer part: $39_{10} = 100111_{2}$. Fraction: $0.8125 = 0.5 + 0.25 + '
            '0.0625 = 2^{-1} + 2^{-2} + 0 + 2^{-4} = 0.1101_{2}$. So '
            '$39.8125_{10} = 100111.1101_{2}$.'},
      {'p': '**Multiplication method** — repeatedly multiply the fraction by 2 and record the '
            'integer part; read from the first (most significant) bit down.'},
      {'pre': '(6) 0.625            (7) 0.8125\n'
              '2 x 0.625 = 1.250 -> 1   2 x 0.8125 = 1.6250 -> 1\n'
              '2 x 0.250 = 0.500 -> 0   2 x 0.6250 = 1.2500 -> 1\n'
              '2 x 0.500 = 1.000 -> 1   2 x 0.2500 = 0.5000 -> 0\n'
              '                         2 x 0.5000 = 1.0000 -> 1'},
      {'tex': '0.625_{10} = 0.101_{2} \\qquad 0.8125_{10} = 0.1101_{2}'}]}},
    {'h3': 'Arithmetic in other number bases'},
    {'p': 'Addition, subtraction and multiplication work exactly as in the decimal system, '
          'keeping the digits aligned by place value and carrying whenever the column total '
          'reaches the base.'},
    {'eg': {'tag': 'Worked', 't': 'Base arithmetic', 'open': True, 'q': [
      {'p': 'Compute: (1) $1101101_{2} + 1011_{2}$; (2) the product $1001_{2} \\times 111_{2}$; '
            '(3) $23_{4} \\times 12_{4}$ (checking each in decimal).'}],
      'a': [
      {'tex': '\\textbf{(1)}\\quad 1101101_{2} + 1011_{2} = 1111000_{2} '
              '\\quad (109 + 11 = 120)'},
      {'tex': '\\textbf{(2)}\\quad 1001_{2} \\times 111_{2} = 111111_{2} '
              '\\quad (9 \\times 7 = 63,\\ \\ 63_{10} = 111111_{2})'},
      {'tex': '\\textbf{(3)}\\quad 231_{4} \\times 12_{4} = 10303_{4}\\ ?'},
      {'note': 'The study text works these with base-4 ("BCD") and base-8 (octal) examples; some '
               'of its printed sums do not carry correctly in the scan. The method is the point '
               '— align by place value, carry at the base, and check by converting to decimal.'}]}},
  ]},

  {'n': '1.8', 't': 'Elements of a database', 'b': [
    {'ol': [
      '**Bit** — a binary digit, 0 or 1; the smallest unit of data.',
      '**Character (byte)** — a combination of 8 bits, representing one alphabet, digit or '
      'special character.',
      '**Field** — a data item or value containing one or more characters; it may be a name, a '
      'value, a number or an operator. "JOSHUA" is a field of six characters. A field used to '
      'identify a record uniquely is a **key**.',
      '**Record** — one or more fields treated together as a unit, accessed through a key. A '
      'student\'s examination scores form a record, keyed by the student\'s identification '
      'number.',
      '**File** — a collection of related records (e.g. the records of all accounting students '
      'in a class).',
      '**Database** — a collection of interrelated files (e.g. one database holding the files '
      'of all of a company\'s customers).',
    ]},
    {'tex': '\\text{bit(s)} \\to \\text{character(s)} \\to \\text{field(s)} \\to '
            '\\text{record(s)} \\to \\text{file(s)} \\to \\text{database}'},
    {'key': 'That hierarchy — bit, byte/character, field, record, file, database — is a '
            'guaranteed short-answer question. A field, record and file are subsets of a '
            'database; **text is not** (study text MCQ 29).'},
  ]},

  {'n': '1.9', 't': 'Data acquisition, cleansing and analysis', 'b': [
    {'h3': 'Data acquisition'},
    {'p': 'Data acquisition is the process by which real-world phenomena are captured and '
          'recorded in digital form. Sensors, transducers and final control elements are '
          '**analog** devices operating on analog electrical signals; the data-acquisition '
          'hardware converts analog to digital and back. Two steps are involved in the '
          'conversion: representing the continuous analog signal by a set of **discrete '
          'values**, and representing those discrete values by **bit sequences**. '
          'Analog-to-digital and digital-to-analog conversion is the interface between the '
          'analog world and digital processing.'},
    {'h3': 'Data cleansing'},
    {'def': {'t': 'Data cleansing', 'd': 'an operation performed on existing data to remove '
                  'anomalies and obtain a collection that accurately represents the real world '
                  '— eliminating errors, resolving inconsistencies and transforming the data '
                  'into a uniform format.'}},
    {'p': 'The process has three stages: **specifying the quality rules; detecting data errors; '
          'and repairing the errors.** Its challenges are incompatible data formats, incomplete '
          'data, non-aligned data structure and inconsistent data — all of which distort '
          'analysis. It is especially common with **big data**. Benefits include: removing '
          'errors when multiple data sources are combined; fewer errors and so happier clients '
          'and less frustrated staff; the ability to map what the data is meant to do; better '
          'error monitoring and reporting; and more efficient practices and quicker '
          'decision-making.'},
    {'h3': 'Data analysis'},
    {'p': 'Analysis that once required a mainframe now runs easily on a PC. **SPSS** '
          '(Statistical Package for the Social Sciences) analyses large data files with '
          'thousands of variables without loss of precision and is widely used for educational '
          'research. **SAS** (Statistical Analysis System) is used for quantitative analysis '
          'and **NUD*IST** for qualitative analysis.'},
  ]},

  {'n': '1.10', 't': 'Computer systems — evolution and types', 'b': [
    {'def': {'t': 'Computer system', 'd': 'a data-processing machine, under the control of '
                  'stored programs, that automatically accepts and processes data and supplies '
                  'or stores the result. It is an electronic machine that accepts data, '
                  'processes it into information using the end-user\'s logic, and stores or '
                  'supplies that information to end users.'}},
    {'h3': 'The five generations (hardware)'},
    {'table': {'align': 'lll', 'head': ['Generation', 'Period / technology', 'Main features'],
      'rows': [
      ['First', '1939–1954, vacuum tube',
       'Vacuum-tube technology; very unreliable; machine language only; very costly; huge heat '
       'output needing large air conditioners; slow input/output; huge size'],
      ['Second', '1954–1959, transistor',
       'Transistors; more reliable and smaller than first generation; less heat; less '
       'electricity'],
      ['Third', '1959–1971, integrated circuit (IC)',
       'ICs instead of individual transistors; smaller, cheaper, more efficient and faster; '
       'high-level programming languages; magnetic storage media'],
      ['Fourth', '1971–present, microprocessor',
       'VLSI technology; very cheap; portable and reliable; "personal computers"; pipeline '
       'processing; the 5.25-inch floppy disk; word processing, spreadsheet and office '
       'automation software; the concept of the internet introduced'],
      ['Fifth', 'present and beyond, nanotechnology',
       'Control-based rather than data-based; ULSI technology; true artificial intelligence; '
       'natural-language processing; parallel processing; superconductor technology; '
       'user-friendly multimedia interfaces'],
    ]}},
    {'h3': 'Classification by how data is represented'},
    {'ul': [
      '**Digital** — data and information represented in digital form by a coded set of '
      'electrical pulses. Examples: programmable calculators, mainframes, minicomputers, '
      'microcomputers. Advantages: accurate output, high arithmetic speed, ease of programming.',
      '**Analog** — data represented by a physical quantity proportional to it. Examples: '
      'thermometer, pressure gauge, voltmeter. Very cheap and high speed, but output may not be '
      'accurate.',
      '**Hybrid** — combines digital and analog in one system, marrying the analog computer\'s '
      'speed with the digital computer\'s flexibility; used mainly in scientific and technical '
      'applications.',
    ]},
    {'p': 'Most computers in use today are **digital**. Digital computers are further classified '
          'as **general-purpose** (fully programmable, for varied numerical and business work) '
          'or **special-purpose** (designed for one type of application, with pre-written '
          'programs).'},
    {'h3': 'Digital general-purpose computers, by size and power'},
    {'p': 'Rapidly changing technology has blurred the traditional classification (many super '
          'microcomputers now outrun old minicomputers), so classification uses features such '
          'as processing power, memory capacity, heat evolution, operating environment, cost, '
          'security measures, installation procedure, maintenance intervals, number of '
          'peripherals supported simultaneously, word size, bus size, and extent of usage.'},
    {'note': '**Word size** is the number of bits processed in one cycle (128-bit chips are now '
             'in use). **Processor power** is the frequency of the processor\'s clock — cycles '
             'per second, measured in hertz. **Bus size** is the number of bits transmitted at '
             'one time from one location to another. "Complexity of the computers" is **not** a '
             'classification feature (study text MCQ 28).'},
    {'table': {'align': 'll', 'head': ['Type', 'Characteristics'], 'rows': [
      ['Supercomputer', 'More powerful than a mainframe; uses parallel processing; more '
       'expensive than a mainframe; extraordinarily fast and exceptionally accurate; used for '
       'computer-generated movies and commercials, weather forecasting and structural '
       'modelling. Drawbacks: needs highly trained staff; software is poor'],
      ['Mainframe', 'Very expensive; large; used mainly by large multinationals; handles '
       'multiple simultaneous functions (batch and interactive processing) under an operating '
       'system; supports a wide range of peripherals; evolves large quantities of heat; housed '
       'in air-conditioned, secured rooms and run by professional operators; runs for many '
       'uninterrupted hours; large primary memory'],
      ['Minicomputer', 'Smaller and cheaper than a mainframe; easier to install (still by a '
       'professional); used by medium-sized companies; no complex management structure; can be '
       'networked; used for engineering and scientific applications; capabilities between a '
       'mainframe and a microcomputer'],
      ['Microcomputer', 'Used as part of a network or stand-alone; very small (desktop, laptop, '
       'pocket); a processor on a single silicon chip on a circuit board; keyboard for input; '
       'screen (monitor / VDU) for output; interfaces for peripherals; small word length; the '
       'cheapest; runs in normal room conditions; can be operated and installed by unskilled '
       'users'],
    ]}},
    {'p': '**Special-purpose digital computers** carry out dedicated operations only — video '
          'games, air-traffic control, sale of petrol from a tank, industrial process-control '
          'robots, meteorological weather-forecasting stations. They are often built into '
          'devices whose function is unrelated to computing: microwave ovens, television sets, '
          'compact-disc players, digital cameras, video sets, petrol gauges. Their programs are '
          '**permanently installed**. An application program for solving general problems is '
          '**not** a special-purpose operation (study text MCQ 24).'},
    {'h3': 'Types of microcomputer'},
    {'ol': [
      '**Desktop** — the most common; fits on a desk; mouse, keyboard and screen are separate '
      'from the main unit, joined by wires.',
      '**Mini tower** — a desktop with a smaller main unit designed to stand upright, taking '
      'less desk space.',
      '**Workstation** — expensive, high-end PC with powerful calculating and graphics '
      'capability; used by engineers for product design and testing.',
      '**Notebook** — as small as a physical notebook; powerful but easy to carry.',
      '**Laptop** — bigger and heavier than a notebook but still portable; built to sit on the '
      'lap.',
      '**Palmtop** — built-in personal-information-management functions (calendar, address and '
      'phone file, task list); no disk storage; non-standard keyboard.',
      '**Pen computer** — uses a pen-like device to enter data on a special input screen and as '
      'a pointing device; special software recognises handwriting. A small pen-input system is '
      'a **Personal Digital Assistant (PDA)** or personal communicator, often with built-in '
      'voice, fax and data communication.',
    ]},
    {'warn': 'A **minicomputer is not portable** (study text MCQ 16) — laptop, notebook, pen '
             'and palmtop computers are.'},
    {'h3': 'Advantages and disadvantages of computers'},
    {'table': {'head': ['Advantages', 'Disadvantages'], 'align': 'll', 'rows': [
      ['Increased speed of operation; efficiency', 'Eye strain from prolonged use; too much '
       'sitting'],
      ['Enhanced accuracy and precision', 'Short attention span; too much multitasking'],
      ['Vast storage capacity and task management', 'Can limit learning and create dependency'],
      ['Effective communication and collaboration', 'Potential loss of privacy; cybersecurity '
       'risk'],
      ['Easy access to a wide range of information', 'Can reduce job opportunities through '
       'automation'],
      ['Diverse entertainment and creative possibilities', 'Increases e-waste; environmental '
       'impact'],
      ['Promotes education and research', 'High initial cost and maintenance; needs constant '
       'upgrade; reliance on external devices; risk of data loss on system failure; irregular '
       'power supply; potential addiction and social isolation'],
    ]}},
  ]},

  {'n': '1.11', 't': 'Short-answer questions (study text)', 'b': [
    {'p': 'The study text\'s 16 fill-in short-answer questions, with its answer key.'},
    {'eg': {'tag': 'Study text short answers', 't': 'Questions and answers', 'open': True, 'q': [
      {'ol': [
        'A special-purpose digital computer used in the production of office documents is '
        'called a …',
        'An output organised in a meaningful fashion, prepared for both internal and external '
        'use, is called …',
        'The collection of people, hardware, software, communication networks and data '
        'resources that collects, transforms and provides information to managers for timely '
        'decision-making is called a(n) …',
        'An audible sound coming from the speaker when an audio CD is played on the computer is '
        'an example of …',
        'The major component of first-generation computers is …',
        'The type of computer that can process both analog and digital data is known as a(n) …',
        'EBCDIC stands for …',
        'ASCII stands for …',
        'The measure of the degree of dependence of the subsystems on one another is referred '
        'to as …',
        'A system that does not interact with other systems or its environment, either for '
        'exchange of information or business transaction, is called a … system.',
        'The basic elements of control in a business system are planning, collecting facts, '
        'comparison and …',
        'The control system where control is exercised by part of the output being fed back '
        'into the system as input is called … control.',
        'The type of information that deals with the magnitude of variables and absolute values '
        'is known as … information.',
        'The type of planning concerned with establishing organisational objectives and the '
        'policies for accomplishing them is called … planning.',
        'The category of computer system consisting of both analog and digital computers '
        'connected as a single unit is called a(n) …',
        'A rearranged and refined basic fact is regarded as …',
      ]}],
      'a': [
      {'ol': [
        'Word processor.',
        'Information.',
        'Information system.',
        'Information (the study text\'s answer — the sound the speaker plays is the output/'
        'information produced from the audio data on the disc).',
        'Vacuum tubes.',
        'Hybrid (computer).',
        'Extended Binary Coded Decimal Interchange Code.',
        'American Standard Code for Information Interchange.',
        'Coupling.',
        'Closed system.',
        'Corrective action.',
        'Closed-loop.',
        'Quantitative information.',
        'Strategic (planning).',
        'Hybrid computer.',
        'Information.',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Distinct characters representable with n bits',
   'tex': 'N = 2^{n}',
   'nt': 'Ordinary use needs 98 characters, so $2^{n} \\ge 98$ gives $n = 7$ (ASCII).'},
  {'lb': 'Decimal integer to binary',
   'tex': '\\text{divide by 2 repeatedly; read the remainders bottom-to-top}'},
  {'lb': 'Binary to decimal',
   'tex': 'd = \\sum b_i \\cdot 2^{i}',
   'nt': '$i$ counts from 0 at the rightmost (least significant) bit.'},
  {'lb': 'Units of storage',
   'tex': '1\\text{ byte} = 8\\text{ bits}, \\quad 1\\text{ word} = 2\\text{ bytes}, \\quad '
          '1\\text{ KB} = 10^{3}\\text{ bytes (}2^{10}\\text{ exactly)}'},
 ],
 'focus':
   'Chapter 1 supplies more Section A marks than any other IT chapter, and a large block of '
   'Section B definitions. Learn the classifications as lists: the three components of a system '
   '(input, process, output); the three types of open system (deterministic, probabilistic, '
   'adaptive); the four elements of control (plan, collect facts, compare, correct); negative '
   'versus positive feedback and feedback versus feed-forward; the five AIS cycles; and the '
   'database hierarchy bit-byte-field-record-file-database. The one calculation is number-base '
   'conversion — practise decimal-to-binary and binary-to-decimal both ways until they are '
   'automatic.',
 'errors': [
   'Calling any computer "a system" — a system is interrelated subsystems working to a common '
   'objective.',
   'Saying a closed system exists in practice; no true closed system does.',
   'Confusing feedback (reactive, after the event) with feed-forward (proactive, predicting the '
   'deviation).',
   'Confusing negative feedback (counteract the deviation) with positive feedback (amplify it).',
   'Reading binary-to-decimal weights from the left; the weight $2^{0}$ is the rightmost bit.',
   'Writing decimal-to-binary remainders top-to-bottom; they are read bottom-to-top.',
   'Saying 1 byte = 4 bits; that is a nibble. A byte is 8 bits.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Which of the following is a personal computer?',
    'o': ['Mainframe', 'Supercomputer', 'Minicomputer', 'Microcomputer', 'Computer chips'],
    'a': 3,
    'w': 'A microcomputer is designed to be used by one person at a time — the personal '
         'computer.',
    'src': 'Chapter 1.10 (study text MCQ 1)', 'sec': '1.10'},
   {'q': 'Semiconductor memory is made from',
    'o': ['silicon chips', 'mercury chips', 'memory chips', 'core chips', 'RAM'],
    'a': 0,
    'w': 'Semiconductor memory is fabricated on silicon chips.',
    'src': 'Chapter 1.10 (study text MCQ 2)', 'sec': '1.10'},
   {'q': 'A microprocessor consists of',
    'o': ['main memory and computer processor', 'the arithmetic unit only', 'the logic unit only',
          'the control unit only', 'a computer program'],
    'a': 0,
    'w': 'The study text\'s answer key gives "main memory and computer processor". More '
         'precisely a microprocessor integrates the arithmetic-logic unit and the control unit '
         'on one chip; take the key\'s wording for the exam.',
    'src': 'Chapter 1.10 (study text MCQ 3)', 'sec': '1.10'},
   {'q': 'Which of the following is NOT a kind of data?',
    'o': ['text', 'picture', 'voice', 'information', 'signal'],
    'a': 3,
    'w': 'Information is processed data — an output, not raw data.',
    'src': 'Chapter 1.3 (study text MCQ 4)', 'sec': '1.3'},
   {'q': 'Which of the following is NOT an example of data transformation?',
    'o': ['scores on an examination paper', 'a teacher collates a marked examination paper',
          'examination scores entered into score sheets', 'score sheets given to the class teacher',
          'calculation of the total and average scores of each student'],
    'a': 0,
    'w': 'The scores themselves are raw data — no transformation has taken place. The other '
         'options each process or move data.',
    'src': 'Chapter 1.3 (study text MCQ 5)', 'sec': '1.3'},
   {'q': 'The type of system in which the various states and activities follow each other in a '
         'predictable manner is',
    'o': ['stochastic system', 'adaptive system', 'cybernetic system', 'probabilistic system',
          'mechanistic system'],
    'a': 4,
    'w': 'A deterministic or mechanistic system is completely predictable.',
    'src': 'Chapter 1.1 (study text MCQ 6)', 'sec': '1.1'},
   {'q': 'The following are basic elements of control in a business system EXCEPT',
    'o': ['planning', 'leading', 'collecting facts', 'comparison', 'corrective action'],
    'a': 1,
    'w': 'The four elements are planning, collecting facts, comparison and corrective action. '
         'Leading is not one of them.',
    'src': 'Chapter 1.2 (study text MCQ 7)', 'sec': '1.2'},
   {'q': 'Which of the following is NOT quantitative information?',
    'o': ['variation of tolerance of finished goods', 'annual sales of a production company',
          'variation in the wages of low-level staff', 'price of goods',
          'number of hours worked on a production line'],
    'a': 0,
    'w': 'Variation of tolerance (a quality attribute) is qualitative information; the other '
         'four are magnitudes.',
    'src': 'Chapter 1.3 (study text MCQ 8)', 'sec': '1.3'},
   {'q': 'The external environment of an organisation consists of',
    'o': ['all forces outside the organisation', 'all buildings outside the organisation',
          'all functions outside management activity', 'all functions outside technical activity',
          'competitors\' actions only'],
    'a': 0,
    'w': 'The environment is everything outside the system boundary that interacts with it — '
         'not just competitors.',
    'src': 'Chapter 1.1 (study text MCQ 9)', 'sec': '1.1'},
   {'q': 'The transformation process of a system consists of input, process and',
    'o': ['action', 'integration', 'delivery', 'output', 'storage'],
    'a': 3,
    'w': 'Input, process, output are the three logical components of a system.',
    'src': 'Chapter 1.1 (study text MCQ 10)', 'sec': '1.1'},
   {'q': 'The essence of decoupling is to allow subsystems more',
    'o': ['efficiency', 'effectiveness', 'independence', 'adaptability', 'probability'],
    'a': 2,
    'w': 'Decoupling gives subsystems more independence in planning and control, leading to '
         'system stability.',
    'src': 'Chapter 1.1 (study text MCQ 11)', 'sec': '1.1'},
   {'q': 'The distinguishing feature of a deterministic system is',
    'o': ['hardness', 'control', 'feedback', 'predictability', 'adaptability'],
    'a': 3,
    'w': 'A deterministic system\'s states follow each other in a completely predictable way.',
    'src': 'Chapter 1.1 (study text MCQ 12)', 'sec': '1.1'},
   {'q': 'The system that has the ability to change itself or its environment in order to '
         'survive is called a(n) … system',
    'o': ['stochastic', 'adaptive', 'mechanistic', 'probabilistic', 'deterministic'],
    'a': 1,
    'w': 'An adaptive (self-organising, cybernetic) system adjusts its own behaviour to survive.',
    'src': 'Chapter 1.1 (study text MCQ 13)', 'sec': '1.1'},
   {'q': 'Data is transformed to information through which of the following?',
    'o': ['sorting', 'aggregation', 'integration', 'control', 'processing'],
    'a': 4,
    'w': 'Processing (which includes sorting and aggregation as particular operations) turns '
         'data into information.',
    'src': 'Chapter 1.3 (study text MCQ 14)', 'sec': '1.3'},
   {'q': 'The meaningful data that results from the processing of unorganised data is called',
    'o': ['information', 'a program', 'data', 'a megabyte', 'software'],
    'a': 0,
    'w': 'Processed, meaningful data is information.',
    'src': 'Chapter 1.3 (study text MCQ 15)', 'sec': '1.3'},
   {'q': 'Which of the following computers is NOT considered portable?',
    'o': ['laptop computer', 'minicomputer', 'notebook computer', 'pen computer',
          'palmtop computer'],
    'a': 1,
    'w': 'A minicomputer is a mid-range system used by medium-sized companies, not a portable '
         'machine.',
    'src': 'Chapter 1.10 (study text MCQ 16)', 'sec': '1.10'},
   {'q': 'A word of storage is made up of how many bits?',
    'o': ['8', '2', '16', '32', '64'],
    'a': 2,
    'w': '1 word = 2 bytes = 16 bits.',
    'src': 'Chapter 1.7 (study text MCQ 17)', 'sec': '1.7'},
   {'q': 'Which of the following represents the binary equivalent of the decimal number 23?',
    'o': ['01011', '10111', '10011', '11001', '10101'],
    'a': 1,
    'w': '23 = 16 + 4 + 2 + 1 = 10111 in binary.',
    'calc': '23_{10} = 1{\\cdot}16 + 0{\\cdot}8 + 1{\\cdot}4 + 1{\\cdot}2 + 1{\\cdot}1 = 10111_{2}',
    'src': 'Chapter 1.7 (study text MCQ 18)', 'sec': '1.7'},
   {'q': 'A data item that consists of one or more characters is known as a',
    'o': ['record', 'file', 'field', 'bit', 'database'],
    'a': 2,
    'w': 'A field is a data item or value containing one or more characters.',
    'src': 'Chapter 1.8 (study text MCQ 19)', 'sec': '1.8'},
   {'q': 'Which of the following is the decimal equivalent of the binary number 1010101?',
    'o': ['85', '87', '105', '81', '89'],
    'a': 0,
    'w': '1010101 = 64 + 16 + 4 + 1 = 85.',
    'calc': '1{\\cdot}2^{6} + 0 + 1{\\cdot}2^{4} + 0 + 1{\\cdot}2^{2} + 0 + 1{\\cdot}2^{0} '
            '= 64 + 16 + 4 + 1 = 85',
    'src': 'Chapter 1.7 (study text MCQ 20)', 'sec': '1.7'},
   {'q': 'A combination of 4 bits of memory is referred to as a',
    'o': ['byte', 'word', 'nibble', 'double word', 'kilobyte'],
    'a': 2,
    'w': 'Four bits make a nibble; eight bits make a byte.',
    'src': 'Chapter 1.7 (study text MCQ 21)', 'sec': '1.7'},
   {'q': 'A standard coding form developed by IBM in which each character is coded using 8 bits '
         'is known as',
    'o': ['EBCDIC', 'BCD', 'ASCII', 'octal', 'hexadecimal'],
    'a': 0,
    'w': 'EBCDIC (Extended Binary Coded Decimal Interchange Code) uses 8 bits per character; '
         'ASCII uses 7; BCD uses 4.',
    'src': 'Chapter 1.7 (study text MCQ 22)', 'sec': '1.7'},
   {'q': 'The major characteristic of the third generation of computers is',
    'o': ['use of vacuum tubes', 'use of integrated circuits', 'use of transistors',
          'use of very-large-scale integration', 'use of machine language for programming'],
    'a': 1,
    'w': 'The third generation replaced individual transistors with integrated circuits.',
    'src': 'Chapter 1.10 (study text MCQ 23)', 'sec': '1.10'},
   {'q': 'Which of the following is NOT an operation designed for special-purpose digital '
         'computers?',
    'o': ['video games', 'air-traffic control', 'meteorological weather forecasting',
          'robot for process control in industry', 'application programs for solving problems'],
    'a': 4,
    'w': 'General application programs run on general-purpose computers; the other four are '
         'dedicated, pre-programmed tasks.',
    'src': 'Chapter 1.10 (study text MCQ 24)', 'sec': '1.10'},
   {'q': 'Which of the following is NOT a basic element of control in a business system?',
    'o': ['planning', 'collecting facts', 'comparison', 'leading', 'corrective action'],
    'a': 3,
    'w': 'The four elements are planning, collecting facts, comparison and corrective action.',
    'src': 'Chapter 1.2 (study text MCQ 25)', 'sec': '1.2'},
   {'q': 'The smallest addressable unit of data in a computer system is the',
    'o': ['bit', 'byte', 'word', 'nibble', 'character'],
    'a': 1,
    'w': 'A bit is the smallest unit of data, but the smallest unit a computer can normally '
         'address is the byte — the study text\'s intended answer.',
    'src': 'Chapter 1.7 (study text MCQ 26)', 'sec': '1.7'},
   {'q': 'Which of the following is NOT one of the main features of first-generation computers?',
    'o': ['supports machine language only', 'the computer uses transistors',
          'computers are very costly', 'huge in size', 'generates a lot of heat'],
    'a': 1,
    'w': 'First-generation computers used vacuum tubes; transistors belong to the second '
         'generation.',
    'src': 'Chapter 1.10 (study text MCQ 27)', 'sec': '1.10'},
   {'q': 'Which of the following is NOT a feature used for classifying computers?',
    'o': ['complexity of the computers', 'processing power', 'memory capacity', 'cost',
          'word size'],
    'a': 0,
    'w': 'Classification uses processing power, memory capacity, cost, word size and similar '
         'measurable features — not "complexity".',
    'src': 'Chapter 1.10 (study text MCQ 28)', 'sec': '1.10'},
   {'q': 'Which of the following is NOT a subset of a database?',
    'o': ['record', 'field', 'bit', 'text', 'data item'],
    'a': 3,
    'w': 'The database hierarchy is bit, byte/character, field, record, file — "text" is not a '
         'level in it.',
    'src': 'Chapter 1.8 (study text MCQ 29)', 'sec': '1.8'},
   {'q': 'Which of the following is NOT an attribute of good information?',
    'o': ['must be relevant', 'must be in coded form', 'must be timely', 'must be reliable',
          'must be simple and understandable'],
    'a': 1,
    'w': 'Good information need not be coded; it must be relevant, timely, reliable and '
         'understandable.',
    'src': 'Chapter 1.3 (study text MCQ 30)', 'sec': '1.3'},
   {'q': 'Which of the following is NOT an example of data transformation?',
    'o': ['scores recorded on an examination paper', 'a teacher collates examination papers',
          'entering examination scores into a score sheet', 'score sheets given to class teachers',
          'calculating the totals and average scores of each student'],
    'a': 0,
    'w': 'Recording the raw scores is not a transformation; the other options process or move '
         'the data.',
    'src': 'Chapter 1.3 (study text MCQ 31)', 'sec': '1.3'},
   {'q': 'In a computer, $10^{12}$ bytes is known as a',
    'o': ['megabyte', 'kilobyte', 'terabyte', 'record', 'gigabyte'],
    'a': 2,
    'w': '$10^{3}$ bytes = 1 KB, $10^{6}$ = 1 MB, $10^{9}$ = 1 GB, $10^{12}$ = 1 TB.',
    'src': 'Chapter 1.7 (study text MCQ 32)', 'sec': '1.7'},
   {'q': 'Which of the following is NOT an advantage of using computers?',
    'o': ['it arranges data according to a specific order', 'it enhances accessibility',
          'it requires a large sum of money', 'it increases errors',
          'it saves time of recall when information is needed quickly'],
    'a': 2,
    'w': 'The study text\'s answer key selects "it requires a large sum of money" as the '
         'non-advantage. Note "it increases errors" is also clearly not an advantage — the '
         'printed question is imperfect; go with the key\'s answer.',
    'src': 'Chapter 1.10 (study text MCQ 33)', 'sec': '1.10'},
  ],
  'theory': [
   {'q': 'Give TWO examples each of qualitative information and quantitative information.',
    'marks': 4,
    'a': [
      {'ul': [
        '**Qualitative** — the standard of a finished product (e.g. its paintwork or '
        'electroplating); the variation of tolerances of manufactured parts (deviation from '
        'standard dimensions).',
        '**Quantitative** — the annual sales of a production company; the variation in the '
        'wages of low-level staff; the price of goods; the number of hours worked on a '
        'production line.']}],
    'src': 'Chapter 1.3 (study text theory Q1)', 'sec': '1.3'},
   {'q': 'State any FOUR constraints that can restrict the objective of profit maximisation in '
         'a business system.',
    'marks': 4,
    'a': [
      {'ol': [
        'Scarcity of key resources such as cash or skilled labour.',
        'Technological constraints limiting what goods and services can be produced.',
        'Economic constraints.',
        'Political and legal constraints.',
        'Product completion time.',
        'Responsibility towards society and for preserving the environment from pollution.']}],
    'src': 'Chapter 1.1 (study text theory Q2)', 'sec': '1.1'},
   {'q': 'Enumerate the aspects by which subsystems can be differentiated from one another.',
    'marks': 6,
    'a': [
      {'ol': [
        '**Function** — e.g. production, finance, marketing, sales, personnel.',
        '**Space** — e.g. Northern-area and Southern-area sales managers.',
        '**Time** — e.g. morning, afternoon and evening shift managers.',
        '**People** — e.g. skilled and unskilled.',
        '**Formality** — various ways of getting information.',
        '**Automation** — various processes carried out by the computer system.']}],
    'src': 'Chapter 1.1 (study text theory Q3)', 'sec': '1.1'},
   {'q': 'Enumerate any FOUR distinctions between data and information.',
    'marks': 4,
    'a': [
      {'table': {'head': ['Data', 'Information'], 'align': 'll', 'rows': [
        ['Raw, unchanged fact', 'Organised and sorted fact'],
        ['Serves as input into the computer system', 'Serves as output from the system'],
        ['Observation and recording produce it', 'Analysis of data produces it'],
        ['The lowest level of knowledge', 'The second level of knowledge'],
        ['By itself, not significant', 'Significant'],
      ]}}],
    'src': 'Chapter 1.3 (study text theory Q4)', 'sec': '1.3'},
   {'q': 'List any SIX functions performed by a professional accountant in a business '
         'organisation.',
    'marks': 6,
    'a': [
      {'ol': [
        'Accounting systems and financial reporting.',
        'Long-term strategic planning.',
        'Managing the accounting and finance function.',
        'Internal consulting.',
        'Short-term budgeting.',
        'Financial and economic analysis.',
        'Process improvement.',
        'Computer systems and operations.',
        'Performance evaluation of the organisation.',
        'Customer and product profitability analysis.']}],
    'src': 'Chapter 1.4 (study text theory Q5)', 'sec': '1.4'},
   {'q': 'The two types of data that can be entered into a computer system are characters and '
         'numbers. Enumerate the characters and numbers that can serve as input data.',
    'marks': 5,
    'a': [
      {'ul': [
        'Uppercase alphabets: A, B, C, …, Z.',
        'Lowercase alphabets: a, b, c, …, z.',
        'Punctuation marks: , . ; ?',
        'Special symbols such as ! ^ * + −',
        'Digits: 0, 1, 2, …, 9.']}],
    'src': 'Chapter 1.7 (study text theory Q6)', 'sec': '1.7'},
   {'q': '(a) Convert the decimal number 1297 to binary. (b) Convert the binary number 10111011 '
         'to decimal.',
    'marks': 6,
    'a': [
      {'p': '**(a)** Divide 1297 by 2 repeatedly and read the remainders upward:'},
      {'pre': '2 | 1297\n2 |  648  r 1\n2 |  324  r 0\n2 |  162  r 0\n2 |   81  r 0\n'
              '2 |   40  r 1\n2 |   20  r 0\n2 |   10  r 0\n2 |    5  r 0\n2 |    2  r 1\n'
              '2 |    1  r 0\n         r 1'},
      {'tex': '1297_{10} = 10100010001_{2}'},
      {'p': '**(b)** Weight each bit by a power of 2 from the right:'},
      {'tex': '1{\\cdot}2^{7} + 0 + 1{\\cdot}2^{5} + 1{\\cdot}2^{4} + 1{\\cdot}2^{3} + 0 + '
              '1{\\cdot}2^{1} + 1{\\cdot}2^{0} = 128 + 32 + 16 + 8 + 2 + 1 = 187_{10}'}],
    'src': 'Chapter 1.7 (study text theory Q7)', 'sec': '1.7'},
   {'q': '(a) Define: bit, character, field, record, file, database. (b) Indicate how these '
         'elements relate.',
    'marks': 8,
    'a': [
      {'ol': [
        '**Bit** — a binary digit, 0 or 1.',
        '**Character** — a combination of 8 bits (a byte).',
        '**Field** — a data item or value containing one or more characters, e.g. a name.',
        '**Record** — one or more fields treated together as a single unit.',
        '**File** — a collection of related records.',
        '**Database** — a collection of interrelated files.']},
      {'tex': '\\text{bit(s)} \\to \\text{character(s)} \\to \\text{field(s)} \\to '
              '\\text{record(s)} \\to \\text{file(s)} \\to \\text{database}'}],
    'src': 'Chapter 1.8 (study text theory Q8)', 'sec': '1.8'},
   {'q': 'Enumerate any FOUR main characteristics of third-generation computers.',
    'marks': 4,
    'a': [
      {'ol': [
        'Use of integrated circuits (ICs) instead of individual transistors.',
        'Smaller, cheaper, more efficient and faster than second-generation computers.',
        'Use of high-level languages (e.g. FORTRAN, COBOL).',
        'Storage media became magnetic storage.']}],
    'src': 'Chapter 1.10 (study text theory Q9)', 'sec': '1.10'},
   {'q': 'State any FIVE types of microcomputer.',
    'marks': 5,
    'a': [
      {'ol': [
        'Desktop computer.', 'Mini tower.', 'Workstation.', 'Notebook computer.',
        'Laptop computer.', 'Palmtop computer.', 'Pen computer.']}],
    'src': 'Chapter 1.10 (study text theory Q10)', 'sec': '1.10'},
   {'q': 'State and explain the function of each of the five basic subsystems of a typical '
         'accounting information system (AIS).',
    'marks': 10,
    'a': [
      {'ol': [
        '**Expenditure** — the activities involved in buying and paying for goods and services '
        'used by the organisation.',
        '**Production** — converting raw materials and labour into finished products (in a '
        'manufacturing organisation).',
        '**Human resources / payroll** — hiring employees who meet the organisation\'s '
        'requirements, and paying them.',
        '**Revenue** — selling goods and services and collecting the proceeds of sales.',
        '**Financing** — obtaining the funds needed to run the organisation, repaying creditors '
        'and distributing profit to investors.']}],
    'src': 'Chapter 1.4 (study text theory Q11)', 'sec': '1.4'},
  ]},
}
