CH = {
 'n': 4,
 't': 'Data Processing',
 'brief': 'Processing techniques and configurations, the effect of CPU/OS type, the '
          'microcomputer in accounting, the Information Centre and computer bureau, the full '
          'family of information systems, and the e-commerce, e-government, e-payment and '
          'digitized-middleman ecosystem built on top of them.',
 'outcomes': [
   'Appreciate different data processing activities',
   'Distinguish among the types of data processing methods',
   'Understand the role of a microcomputer in the accounting and finance environments',
   'Understand the role of user departments',
   'Appreciate the functions of an information centre',
   'Understand the concept and services available from a computer service bureau',
   'Distinguish among various information systems',
   'Describe various e-commerce models, electronic payment systems and digitized middleman',
 ],
 'secs': [
  {'n': '4.1', 't': 'Processing techniques', 'b': [
    {'def': {'t': 'Batch', 'd': 'a number of transactions accumulated together and processed '
                  'at a predetermined time as a single unit.'}},
    {'h3': '4.1.1 Batch processing'},
    {'def': {'t': 'Batch processing', 'd': 'updating master files periodically to reflect all '
                  'the transactions that occurred during a given time period. The master file '
                  'is updated at predetermined times (e.g. daily or weekly), or whenever a '
                  'manageable number of transactions has been gathered.'}},
    {'p': 'Transaction data can be entered either as a batch, or as each transaction occurs — '
          'entering data as each transaction occurs is called **Online Batch Processing**. In '
          'batch processing, jobs are entered and stored on disk in a **Batch Queue** before '
          'being run under the control of the OS.'},
    {'key': '**Turn-around time** is the time that elapses between the submission of a job and '
            'the return of its result.'},
    {'table': {'cap': 'Batch processing', 'align': 'll',
      'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Repeated jobs are done fast, without user interaction', 'Delay in the generation of '
       'computer output'],
      ['No special hardware/system support needed to input data', 'Accumulation of data '
       'often puts pressure on computer staff during processing'],
      ['Can work offline, so puts less stress on the processor', 'No direct access to the '
       'system by the user department'],
      ['Less expensive', 'Computer operators must be trained for using batch systems'],
      ['Encourages proper documentation of transaction data', 'Difficult to debug batch '
       'systems'],
      ['Allows enough time for independent review and authorization of input data by a '
       'responsible officer before processing', 'If an error occurs in a job, other jobs must '
       'wait for an unknown time'],
      ['Computer failure and temporary breakdowns have less impact on processing',
       'Batch systems are sometimes costly'],
      ['Specific time can be assigned for batch jobs, so idle computer time is used', ''],
      ['Batch systems can be shared by multiple users', ''],
    ]}},
    {'h3': '4.1.2 Remote Job Entry (RJE) processing'},
    {'def': {'t': 'Remote Job Entry (RJE)', 'd': '(batch) processing where jobs are entered '
                  'at a terminal remote from the computer and transmitted to the computer '
                  'either online (through telecommunication links) or offline (using external '
                  'storage systems).'}},
    {'h3': '4.1.3 Online processing'},
    {'def': {'t': 'Online processing', 'd': 'the processing of data from terminals connected '
                  'directly to the central processor.'}},
    {'table': {'cap': 'Online processing', 'align': 'll',
      'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Enables data to be captured close to where transactions occur', 'More expensive to '
       'set up and maintain than offline systems'],
      ['Minimizes paperwork', 'May cause the host computer to be overloaded'],
      ['Prevents delays caused by manual transmission of data/output between terminal and '
       'processor', 'Increases the risk of unauthorized access to computer files from remote '
       'terminals'],
      ['Enables interactive data processing', 'Electronic data processing activities may be '
       'halted if the host computer breaks down'],
      ['Enables users to directly access, view and update files at the central computer', ''],
      ['Makes error correction easy', ''],
      ['Less labour-intensive than offline systems', ''],
      ['Avoids the risk of unauthorized amendment of data/output in transit', ''],
    ]}},
    {'h3': '4.1.4 Real-time processing'},
    {'def': {'t': 'Real-time processing', 'd': 'the computer captures data electronically, '
                  'edits it for accuracy and completeness, and immediately processes it — so '
                  'quickly that the results are available to influence the activity currently '
                  'taking place. Used for critical systems where a time delay is not '
                  'allowed.'}},
    {'note': '**All real-time systems are online, but not all online systems are real-time** — '
             'online batch processing is not real-time.'},
    {'p': 'Examples of real-time processing: **international hotel reservation**, **airline '
          'reservation**, **space exploration**.'},
    {'table': {'cap': 'Real-time processing', 'align': 'll',
      'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Computer output is instantaneously made available', 'No adequate time for clerical '
       'checking and authorization of input data'],
      ['The output can be used to influence the transaction', 'Very complex to design, '
       'implement and maintain'],
      ['Avoids time-consuming and unnecessary paperwork', 'Increases the risk of unauthorized '
       'access to the computer'],
      ['Enables users to see the cumulative effect of all transactions for decision making',
       'Reliant on the continued existence and proper functioning of the computer system'],
      ['Avoids costly and time-consuming data preparation and control operations', 'Requires '
       'a lot of expertise'],
      ['', 'Very expensive'],
      ['', 'The intensive light from the monitor affects users\' eyes'],
    ]}},
  ]},

  {'n': '4.2', 't': 'Configuration of processing methods', 'b': [
    {'p': 'Three basic ways to configure processing methods — i.e. to determine the '
          'arrangements and locations of the computer systems:'},
    {'h3': '4.2.1 Centralized processing method'},
    {'def': {'t': 'Centralized processing', 'd': 'all processing is done in a single place '
                  '(e.g. the headquarters), and results are later distributed to the various '
                  'departments. All terminals and other devices are connected to a central '
                  'corporate computer (the server).'}},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Better control over the processing', 'Greater complexity'],
      ['More experienced IT staff', 'Higher communication cost of results to the departments'],
      ['Economies of scale — cheaper to run', 'Less flexibility in meeting individual '
       'departments\' needs'],
      ['', 'No departmental secrecy'],
    ]}},
    {'h3': '4.2.2 Decentralized processing method'},
    {'def': {'t': 'Decentralized processing', 'd': 'each department does its own processing '
                  'using its own IT staff within the department. There is no connection among '
                  'the departments, and even none with the headquarters.'}},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Allows departments to meet their needs and separate users\' needs', 'Complexity of '
       'coordinating data among the departments'],
      ['Less communication cost associated with distributing information', 'Increase in '
       'administrative cost'],
      ['Departmental secrecy is achieved, since data is stored locally', 'Increase in '
       'machinery/hardware costs'],
      ['', 'Greater difficulty in implementing effective control'],
    ]}},
    {'h3': '4.2.3 Distributed Data Processing (DDP)'},
    {'def': {'t': 'Distributed Data Processing (DDP)', 'd': 'a hybrid of the centralized and '
                  'decentralized approaches — each location has its own computers for local '
                  'processing, and the departments are all linked to each other and to the '
                  'corporate server.'}},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Since departments are linked, they back each other up — less risk of catastrophic '
       'loss, since resources are in multiple locations', 'Multiple locations and varying '
       'needs complicate coordinating the system and maintaining hardware/software/data '
       'consistency'],
      ['Since local processing is treated as a module, more modules can easily be added or '
       'deleted from the system', 'Difficulty standardizing documentation and control, since '
       'authority and responsibility are distributed'],
      ['', 'Multiple locations and communication channels hinder adequate security controls '
       'and separation of duties'],
      ['', 'Data duplication across multiple locations increases data storage costs and data '
       'inconsistency'],
    ]}},
  ]},

  {'n': '4.3', 't': 'Effects of CPU and operating systems', 'b': [
    {'p': 'The type of CPU/OS in use determines the way processing jobs/tasks can be done. '
          'Four types considered: **time sharing**, **multi-processing**, **multi-tasking**, '
          '**multiprogramming**.'},
    {'h4': '(a) Time-sharing processing'},
    {'def': {'t': 'Time sharing', 'd': 'a method of data processing that enables many users '
                  'to gain access to a centrally located computer by means of terminals. The '
                  'central computer allocates equal CPU time (a **time slice**) to each user '
                  'to perform their jobs, attended to either on a first-come-first-served '
                  'basis or according to predetermined priority levels — the highest-priority '
                  'user is attended to for the time slice, then, on its expiration, the next '
                  'highest-priority user is serviced, until all users are serviced.'}},
    {'p': '**Advantages:** the facility may be provided by an in-house installation or a '
          'computer time-sharing bureau; each user is geographically remote from the central '
          'computer and from each other; the system interacts with many users, giving each '
          'fast individual attention in time.'},
    {'p': '**Disadvantages:** system interlocking may create disturbances; non-availability '
          'of computer resources to be shared; when the system fails, it fails completely and '
          'totally.'},
    {'h4': '(b) Multi-tasking process'},
    {'def': {'t': 'Multi-tasking', 'd': 'a system that allows the computer to work on more '
                  'than one job or task at a time. On personal computers it usually supports a '
                  'single user running multiple programs at once.'}},
    {'p': 'Multi-tasking is accomplished in these ways:'},
    {'ul': [
      '**Context switching** — the user switches back and forth between programs.',
      '**Cooperative multitasking** — programs switch when they reach a logical break point.',
      '**Pre-emptive multi-tasking** — the OS switches programs based on the allocated amount '
      'of time and priority.',
    ]},
    {'h4': '(c) Multi-processing technique'},
    {'def': {'t': 'Multi-processing', 'd': 'executing several processes simultaneously on a '
                  'computer with more than one Central Processing Unit; a computer with more '
                  'than one CPU is a **multiprocessor**.'}},
    {'p': 'A multi-processing system coordinates the CPUs using either **asymmetric** '
          'multiprocessing (processing is assigned to a specific CPU with its own memory) or '
          '**symmetric** multiprocessing (processes are assigned to whichever CPU is '
          'available, and memory is shared among the CPUs). Symmetric multiprocessing is more '
          'complex, but achieves a higher processing rate because the OS has more flexibility '
          'in assigning processing to available CPUs.'},
    {'p': '**Advantages:** if one CPU fails, the system can shift work to the remaining CPUs; '
          'provides fast throughput for jobs; pays particular attention to individual '
          'tasks/jobs to give rapid service; if a task requires more resources than are '
          'available on any single system, all the resources can be pooled to serve one '
          'process.'},
    {'h4': '(d) Multiprogramming'},
    {'def': {'t': 'Multiprogramming', 'd': 'a technique that enables a number of programs '
                  '(jobs) to interleave with each other, so that the execution of one program '
                  'overlaps with the I/O operation of the others, adopted to reduce the idle '
                  'time of the central processor. Many jobs may be run at the same time — '
                  'loaded into memory and assigned to the processor(s) in sequence. For '
                  'efficiency, jobs to be multiprogrammed should be properly selected to '
                  'maximize use of the system\'s resources.'}},
  ]},

  {'n': '4.4', 't': 'The role of microcomputers in the accounting and finance environments', 'b': [
    {'p': 'The user-friendliness of the microcomputer and its software, together with low cost '
          'and ready availability, make the microcomputer the preferred processing tool in '
          'most organizations; the activities of a typical accounting and finance environment '
          'lend themselves well to the use of personal computers.'},
    {'p': 'A number of PC accounting packages are available for the accountant. General '
          'accounting software products such as spreadsheet and database programs can be used '
          'to process accounting transactions; integrated accounting packages may be used for '
          'features like:'},
    {'ul': [
      'Creation of chart of accounts,',
      'Recurring journal entries,',
      'Variance analysis reports,',
      'Payroll,',
      'Accounts payable, and',
      'Accounts receivable, etc.',
    ]},
  ]},

  {'n': '4.5', 't': 'Microcomputer business applications', 'b': [
    {'p': 'Typical business applications facilitated by the microcomputer include **payroll, '
          'stock control, purchases, invoicing, sales ledger, general ledger**, etc.'},
    {'p': 'The various ways a microcomputer is utilized in an organization vary depending on, '
          'among others, the nature of the business, its organizational structure, management '
          'style, geographical dispersion of its operating units, and volume of work. The '
          'computer has taken over a lot of what the accountant previously handled manually, '
          'especially in management reports of all kinds, forecasting and modelling.'},
  ]},

  {'n': '4.6', 't': 'The Information Centre', 'b': [
    {'p': 'The widespread dependence on computer-based information systems means many '
          'individuals and organizations must use computer systems — some of whom may not be '
          'very knowledgeable in computer use, and so must depend on others for assistance. '
          'The **Information Centre** plays this role.'},
    {'def': {'t': 'Information Centre (IC)', 'd': 'a department or office manned by '
                  'technically skilled staff that assists the Information System (IS) '
                  'department staff with regard to user requests and complaints.'}},
    {'def': {'t': 'Help desk', 'd': 'an office or desk with staff using telephones and hot '
                  'lines to receive user staff complaints and requests, which are eventually '
                  'passed on to the Information Centre for a solution — important because not '
                  'all user staff are IT experts, so there will always be issues on which they '
                  'need assistance.'}},
    {'p': 'This arrangement ensures IS staff have sufficient time to focus on their routine '
          'functions, avoiding a backlog of work. IC staff are **not** supposed to usurp the '
          'powers and functions of IS staff.'},
    {'h3': '4.6.1 Role of user department'},
    {'def': {'t': 'User', 'd': 'a person who uses a computer system or network service, '
                  'generally without the technical expertise required to fully understand it.'}},
    {'p': 'Users are expected to play the following roles in an information systems '
          'environment:'},
    {'ol': [
      'Specify requirements — during system development and acquisition, users specify their '
      'exact needs to the IT team.',
      'Use the hardware and software responsibly for the business of the organization.',
      'Report issues in the right format as agreed in the organization.',
      'Comply with the usage policy of their organization.',
      'Report any suspicion of a breach of security in their system to the appropriate '
      'quarters.',
      'Users are not expected to develop the software themselves, regardless of how much '
      'technical knowledge they may possess.',
    ]},
    {'h3': '4.6.2 Staffing of an IT department'},
    {'p': 'The major roles available in an IT department (depending on the size of the '
          'organization):'},
    {'ul': [
      '**Software Engineer** (application programmer, software architect, system programmer/'
      'engineer) — designs and programs system-level software: operating systems, database '
      'systems, embedded systems, etc.; understands how both software and hardware function.',
      '**Systems Analyst** (product specialist, systems engineer, solutions specialist, '
      'technical designer) — investigates and analyses business problems, then designs '
      'information systems that provide a feasible solution, typically in response to '
      'requests from the business or a customer.',
      '**Business Analyst** (business architect, enterprise-wide information specialist) — '
      'analyses users\' needs, gathers and documents requirements, and creates a project plan '
      'to design the resulting technology solution.',
      '**Technical Support** (help desk support, operations analyst).',
      '**Network Engineer** (hardware engineer, network designer) — sets up, administers, '
      'maintains and upgrades communication systems, LANs and WANs.',
      '**Software Tester** (test analyst, software quality assurance tester) — prepares test '
      'scripts and tests applications before release to end-users.',
    ]},
    {'h3': '4.6.3 Computer bureau'},
    {'def': {'t': 'Computer service bureau', 'd': 'a company that operates computer services '
                  'to process data for other companies, particularly those that cannot justify '
                  'acquiring their own computer system; a business that provides computer '
                  'services to other organizations, such as data processing, software '
                  'development and technical support.'}},
    {'p': 'Two types of computer bureau: (a) **independent companies** specially formed to '
          'provide computing services to clients; (b) **computer users with spare capacity**, '
          'who allow other firms to use their computer systems, either for standby facilities '
          'or for testing a program before installing a similar computer system.'},
    {'p': 'Services provided by a computer bureau:'},
    {'ol': [
      '**Data preparation** — conversion of source data into machine code/object data for '
      'computer processing.',
      '**Program preparation and testing** — testing prepared programs for debugging and '
      'other characteristics.',
      '**Hiring of computer time** — the client uses the bureau\'s computer operators to '
      'process their own data using their own programs; only the bureau\'s computer time and '
      'resources are used, not its programs.',
      '**Hiring of computer systems** — the client takes the computer system away for short '
      'duration usage, operated by the client or the client\'s staff in a private safe '
      'location.',
      '**Do-it-yourself service** — provision of computing facilities to allow the client\'s '
      'own operators to process data with their own programs.',
      '**Time-sharing facility** — access to the bureau\'s computer system by communication '
      'links, giving each user computing facilities as if they had an in-house system.',
      '**Sales of computer system resources** — printer, mouse, keyboard, monitor, cables, '
      'etc.',
      '**Repairs and maintenance** of clients\' hardware and software.',
      '**Acts as an information centre** — offers information on general computer resources, '
      'sources of data, use of data, etc.',
      '**System installation** — facilities for installing clients\' systems.',
      '**Training of staff** — particularly useful when installing a new OS or database '
      'software.',
      '**Feasibility study consultants** — bureau staff may act as consultants during a '
      'feasibility study for systems development.',
    ]},
    {'p': '**Reasons for using a bureau:**'},
    {'ul': [
      'To obtain valuable initial experience of computer processing before deciding whether '
      'to install an in-house system.',
      'To provide a standby facility, by arrangement, in case of breakdown of the in-house '
      'computer.',
      'To cope with peak data processing loads, owing to insufficient in-house capacity.',
      'Non-availability of liquid funds for installing an in-house computer.',
      'Space restrictions for accommodating a computer installation (e.g. mainframes/minis).',
      'To avoid the responsibility of operating an in-house computer — repairs and software '
      'installation are done by the bureau.',
      'Insufficient volume of work to justify installing or owning a computer system.',
    ]},
    {'p': '**Disadvantages of using a bureau:**'},
    {'ul': [
      'Loss of control over the time taken to process data, because of the computing '
      'requirements of the bureau\'s other clients.',
      'Loss of the experience that would have been gained from using an in-house system, '
      'giving an advantage to competitors using similar application packages/services.',
      'Lack of adequate security for data processed at the bureau.',
      'No secrecy of the client\'s data processing activity.',
    ]},
  ]},

  {'n': '4.7', 't': 'Information systems', 'b': [
    {'def': {'t': 'Information System', 'd': 'an integrated set of components for collecting, '
                  'storing and processing data into information, knowledge and digital '
                  'products.'}},
    {'p': 'Information systems are deployed by diverse organizations to achieve a wide range '
          'of objectives, including: management of internal operations; management of '
          'relationships with customers, suppliers, etc.; management of relationships with '
          'regulatory authorities, publics, etc.; provision of effective tools of competition '
          'in the marketplace; and delivery of digital products.'},
    {'p': 'Organizations that use information systems include: commercial organizations; '
          'regulatory authorities; Non-Governmental Organizations (NGOs); educational '
          'institutions; and digitized middlemen, etc.'},
    {'h3': '4.7.1 Components of information systems'},
    {'p': 'The main components of an information system, under **Information Technology**:'},
    {'ul': [
      '**Computer hardware** — computer CPUs, input and output devices, storage devices.',
      '**Computer software** — **system software** (e.g. operating systems), which enables '
      'users to control the computer and manages program files, data, hardware and other '
      'system resources; and **application software** — programs designed to meet the '
      'specific requirements, needs or tasks of the user, general-purpose (spreadsheets, word '
      'processors, etc.) or specialized.',
      '**Telecommunication networks** — connect computer systems and other devices and '
      'transmit information among them and with the external environment, wired or wireless.',
      '**Databases and data warehouses** — a **database** is a collection of inter-related '
      'data arranged so that individual data, or a group of data meeting specific criteria, '
      'can be accessed, retrieved and processed to generate information or a digital product. '
      'Massive collection and processing of data on a subject of interest on the World Wide '
      'Web produces **Big Data**, which provides general trends on which prompt decisions can '
      'be taken. A **Data Warehouse** is a data management system containing large amounts of '
      'historical data derived from a wide variety of sources, designed for queries and '
      'analytics, and enabling and supporting business intelligence.',
      '**Human resources** — the skilled manpower needed to manage the entire process: IT '
      'specialists (systems engineers, systems analysts, programmers, etc.); security experts, '
      'to design security systems and processes preventing breaches; management, to provide '
      'resources and direction of operation; and users of the system, to specify the tasks to '
      'be undertaken, the problems to be solved, and the format of the solution.',
      '**Procedures and processes** — the details of the steps taken to transform input data '
      'into information or a product, in a secure environment.',
    ]},
    {'h3': '4.7.2 Types of information system'},
    {'p': 'Information systems can be classified by the type of function they perform: (a) '
          'Management Information System (MIS); (b) Decision Support System (DSS); '
          '(c) Executive Support System (ESS); (d) Transaction Processing System (TPS); '
          '(e) Office Information System (OIS); (f) Knowledge Management System (KMS); '
          '(g) Expert System (ES); (h) Knowledge Work System (KWS); (i) Government Integrated '
          'Financial Management Information System (GIFMIS); (j) Integrated Payroll and '
          'Personnel Information System (IPPIS); (k) University Transparency and '
          'Accountability Solution (UTAS); (l) Accounting Transaction Recording and Reporting '
          'System (ATRRS); (m) Open Treasury Portal (OTP).'},
    {'h4': '(a) Management Information System (MIS)'},
    {'def': {'t': 'Management Information System (MIS)', 'd': 'an information system used to '
                  'perform management functions — decision-making, coordination, control, '
                  'analysis and visualization of information in an organization. Its ultimate '
                  'goal is to maximize the value of the firm by giving managers timely and '
                  'appropriate information for effective decisions within a shorter period.'}},
    {'p': 'Kenneth C. Laudon and Jane Laudon identified **five historical eras of MIS**: '
          '(1) mainframe and minicomputer computing; (2) personal computers; (3) client/'
          'server networks; (4) enterprise computing; (5) cloud computing.'},
    {'p': '**Benefits of MIS:**'},
    {'ol': [
      'It helps managers make better and faster decisions.',
      'It improves an organization\'s operational efficiency.',
      'It adds value to existing products.',
      'It engenders innovation and new product development.',
      'It facilitates managers\' ability to identify their companies\' strengths and '
      'weaknesses, due to the presence of revenue reports, employee performance records, etc.',
      'It helps a company improve its business processes and operations.',
      'It gives an overall picture of the company.',
      'It acts as a communication and planning tool.',
      'It can allow a company to gain a competitive advantage.',
    ]},
    {'h4': '(b) Decision Support System (DSS)'},
    {'def': {'t': 'Decision Support System (DSS)', 'd': 'a computerized program used to '
                  'support judgments and courses of action in an organization or business '
                  'environment. A DSS accesses and analyses massive amounts of data, '
                  'synthesizing them into comprehensive information used to solve problems and '
                  'make decisions — used mostly for **semi-structured and unstructured** '
                  'decision problems by middle and higher management.'}},
    {'p': 'Typical DSS information includes target/projected revenue, sales figures (current '
          'or past), and other inventory- or operations-related data.'},
    {'p': '**Benefits of DSS:** helps make more informed decisions; used to make actionable '
          'decisions; enables production of multiple possible outcomes based on current and '
          'historical data; can produce easily digestible reports for customers; reports can '
          'be easily adjusted to user specifications; facilitates timely problem-solving; '
          'provides improved efficiency in dealing with issues, operations, planning and '
          'management; flexible, hence portable from one industry to another.'},
    {'h4': '(c) Executive Support System (ESS)'},
    {'def': {'t': 'Executive Support System (ESS)', 'd': 'also called an Executive Information '
                  'System; software that allows users to transform enterprise data into '
                  'quickly accessible, executive-level reports, such as those used by billing, '
                  'accounting and staffing departments. Enhances decision-making for '
                  'executives, and provides easy access to internal and external information '
                  'relevant to organizational goals.'}},
    {'p': 'A typical ESS has four components: **hardware**, **software**, **user interface**, '
          '**telecommunication**.'},
    {'h4': '(d) Transaction Processing System (TPS)'},
    {'def': {'t': 'Transaction Processing System (TPS)', 'd': 'a type of information system '
                  'that collects, stores, modifies and retrieves the data transactions of an '
                  'enterprise, providing predictable response times to requests.'}},
    {'p': '**Benefits of TPS:** enhances accuracy of transaction records; enhances speed of '
          'processing, reducing transaction time; reduces processing cost; makes transaction '
          'time predictable to customers.'},
    {'p': 'TPS generally involves five steps: **data entry**; **transaction processing**; '
          '**file and database updating**; **document and report generation**; **processing '
          'of inquiries**. There are two types of TPS processing: **real-time** and **batch '
          'processing**.'},
    {'h4': '(e) Office Information System (OIS)'},
    {'def': {'t': 'Office Information System (OIS)', 'd': 'an information system that uses '
                  'software, hardware and networks to improve work flow and communications '
                  'among employees, providing technical support and services for the timely '
                  'retrieval of accurate information to enable effective planning, operation '
                  'and monitoring of services in an organization.'}},
    {'p': '**Benefits of OIS:** improved accuracy of records; reduced costs in office '
          'administration; reduced time and resources; improved data storage and management; '
          'provides more insight into the organization\'s data, enabling more informed '
          'decisions; business process improvement.'},
    {'h4': '(f) Knowledge Management System (KMS)'},
    {'def': {'t': 'Knowledge Management System (KMS)', 'd': 'a platform that facilitates the '
                  'creation, organization, storage and retrieval of knowledge within an '
                  'organization, aiming to improve collaboration, innovation and efficiency by '
                  'making information easily accessible to employees and potentially '
                  'customers. In other words, a tool that helps an organization capture, '
                  'organize, share and utilize its knowledge assets.'}},
    {'p': '**Key features:** centralized knowledge repository, improved collaboration, '
          'enhanced decision-making, knowledge retention, increased efficiency.'},
    {'h4': '(g) Expert System (ES)'},
    {'def': {'t': 'Expert System (ES)', 'd': 'a computer system or program that uses '
                  'artificial intelligence techniques to solve problems that ordinarily '
                  'require a knowledgeable human — software that attempts to reproduce the '
                  'performance of one or more human experts, most commonly in a specific '
                  'problem domain; an organized collection of people, devices, databases and '
                  'procedures used for suggesting decisions and acting like a human expert in '
                  'a certain area or discipline.'}},
    {'p': 'Methods used to simulate the expert\'s performance: (a) creation of a **knowledge '
          'base** using some knowledge-representation formalism to capture the Subject Matter '
          'Expert\'s (SME) knowledge; and (b) a process of gathering that knowledge from the '
          'SME and codifying it according to the formalism. While an expert system does not '
          'often replace the human expert, it can serve as a useful assistant — e.g. '
          '**INTERNIST**, a medical diagnosis tool containing over 100,000 relationships '
          'between symptoms and diseases.'},
    {'table': {'cap': 'Expert Systems', 'align': 'll',
      'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Provides consistent answers for repetitive decisions, processes and tasks', 'Lacks '
       'common sense needed in some decision-making'],
      ['Holds and maintains a significant level of information', 'Cannot make creative '
       'responses like a human expert in an unusual circumstance'],
      ['Encourages the organization to clarify the logic of its decision-making', 'Errors may '
       'occur in the knowledge base, leading to wrong decisions'],
      ['Never forgets to ask a question, as a human might', 'Cannot adapt to a changing '
       'environment, unless the knowledge base is changed'],
      ['Works round the clock', ''],
      ['Can be used by the user more frequently', ''],
      ['A multi-user Expert System can serve more than one user at a time', ''],
    ]}},
    {'h4': '(h) Knowledge Work System (KWS)'},
    {'def': {'t': 'Knowledge Work System (KWS)', 'd': 'a specialized information system '
                  'designed to support professionals who create, process and disseminate new '
                  'knowledge within an organization, used by professionals in fields like '
                  'engineering, finance and science to manage complex data, perform '
                  'simulations and make informed decisions.'}},
    {'p': '**Examples:** Computer-Aided Design (CAD) software for engineers; financial '
          'modelling platforms for analysts; knowledge management systems; Artificial '
          'Intelligence (AI) systems.'},
    {'p': '**Benefits of KWS:** increased productivity; improved decision-making; enhanced '
          'innovation; better knowledge management.'},
    {'h4': '(i) Government Integrated Financial Management Information System (GIFMIS)'},
    {'def': {'t': 'GIFMIS', 'd': 'a system used by the Federal Government of Nigeria to manage '
                  'and improve public finances — a tool for better budget management, '
                  'accounting and public expenditure management. Its purpose is to modernize '
                  'fiscal processes, enhance accountability and transparency, and improve the '
                  'efficiency of public resource management, covering the entire financial '
                  'management cycle: budget preparation, execution, procurement, payment and '
                  'reporting.'}},
    {'p': 'Major benefits: improving the reliability of financial information, streamlining '
          'financial transactions and reducing costs. Implemented across various Ministries, '
          'Departments and Agencies (MDAs) in Nigeria, with ongoing training so auditors and '
          'other stakeholders can use GIFMIS platforms effectively.'},
    {'p': 'Objectives of GIFMIS: increases the ability to access information on financial and '
          'operational performance; increases internal controls to prevent and detect '
          'potential and actual fraud; increases the ability to access information on '
          'government cash position and economic performance.'},
    {'p': 'Major challenges of GIFMIS in Nigeria: **low financial literacy**; **inadequate '
          'infrastructural facilities**; **inadequate and inefficient technology-based '
          'facilities by financial institutions**.'},
    {'h4': '(j) Integrated Payroll and Personnel Information System (IPPIS)'},
    {'def': {'t': 'IPPIS', 'd': 'an information system used by the Nigerian Government to '
                  'manage personnel records and payroll for its employees, designed to '
                  'improve efficiency, eliminate fraud and provide a comprehensive database '
                  'for the public service — centralizing and streamlining the management of '
                  'personnel information and payroll processing for government. Functions '
                  'include personnel records management, exit and termination management, and '
                  'statistical reporting.'}},
    {'p': '**Benefits of IPPIS:** manpower planning and reduced fraud; facilitates easy '
          'storage and retrieval of records; supports monitoring of staff emolument '
          'payments.'},
    {'h4': '(k) University Transparency and Accountability Solution (UTAS)'},
    {'def': {'t': 'UTAS', 'd': 'a proposed payment platform designed to be a more transparent '
                  'and accountable alternative to IPPIS in Nigeria — proposed by ASUU as a '
                  'replacement for IPPIS, aiming for wide acceptance by universities.'}},
    {'p': '**Key features:** transparency, accountability, alternative to IPPIS, home-grown '
          'solution, wider acceptance.'},
    {'h4': '(l) Accounting Transaction Recording and Reporting System (ATRRS)'},
    {'def': {'t': 'ATRRS', 'd': 'a computerized system used by the Accountant-General\'s '
                  'office to record transactions at various Federal Pay Offices (FPOs), MDAs '
                  'and the main Treasury, and electronic transcripts of transactions submitted '
                  'by FPOs/MDAs to the Treasury using compact disks, for consolidation and '
                  'reporting. It typically involves identifying, recording, classifying, '
                  'summarizing and reporting financial transactions, ensuring accurate and '
                  'reliable financial information for decision-making and regulatory '
                  'reporting.'}},
    {'p': '**Key features of ATRRS:** identifying and analysing transactions; recording '
          'transactions; classifying transactions; summarizing transactions; preparing '
          'financial statements; reporting.'},
  ]},

  {'n': '4.8', 't': 'Open Treasury Portal', 'b': [
    {'def': {'t': 'Treasury', 'd': 'a financial department or organization within a government '
                  'or organization that manages and controls financial resources, including '
                  'funds, assets and investments, playing a crucial role in budgeting, cash '
                  'management, and ensuring the financial stability of the entity.'}},
    {'p': 'Functions of treasury include: cash management, financial risk management, '
          'investment management, budgeting and forecasting, debt management, regulatory '
          'compliance, long-term financial planning, etc.'},
    {'p': 'The **Open Treasury Portal** contains reports such as:'},
    {'ul': [
      'Daily Treasury Statement',
      'Daily Treasury Reports',
      'Monthly Budget Performance Report',
      'Monthly Fiscal Accounts',
      'Quarterly Financial Statements (MDAs)',
      'Annual General Purpose Financial Statements',
    ]},
  ]},

  {'n': '4.9', 't': 'Electronic Commerce (e-commerce)', 'b': [
    {'def': {'t': 'E-commerce (electronic commerce)', 'd': 'the buying and selling of goods '
                  'and services, or the transmitting of funds or data, over an electronic '
                  'network, primarily the internet.'}},
    {'p': 'Common areas of e-commerce application: finance, manufacturing, retail and '
          'wholesale, online marketing, online booking, online publishing, digital '
          'advertising.'},
    {'p': '**Benefits of e-commerce:**'},
    {'ol': [
      '**Convenience** — makes purchases simpler, faster and less time-consuming, allowing '
      '24-hour sales, quick delivery and easy returns.',
      '**Personalization and customer experience** — marketplaces create rich user profiles '
      'that personalize the products offered and suggest other interesting products, '
      'improving customer experience and increasing brand loyalty.',
      '**Global marketplace** — customers worldwide can shop e-commerce sites; companies are '
      'no longer restricted by geography or physical barriers.',
      '**Minimized expenses** — without needing a brick-and-mortar store, digital sellers can '
      'launch online stores with minimal start-up and operating costs.',
    ]},
    {'h4': 'Common e-commerce models'},
    {'ul': [
      '**Business to Consumer (B2C)** — a business transacts directly with a consumer, '
      'usually a sale to an ultimate consumer, e.g. buying a product from a retailer\'s '
      'website. **The most popular e-commerce model.**',
      '**Business to Business (B2B)** — a business sells a good or service to another '
      'business, like a manufacturer to a wholesaler, or a wholesaler to a retailer; does not '
      'involve the ultimate consumer, and usually involves products like raw materials, '
      'software, or components to be combined.',
      '**Consumer to Consumer (C2C)** — the sale of a good or service by one consumer to '
      'another, taking place on platforms like eBay, Etsy, Fiverr, Jiji, etc.',
      '**Consumer to Business (C2B)** — an individual sells their services or products to a '
      'business organization, e.g. photographers, consultants and freelance writers offering '
      'services to businesses.',
      '**Direct to Consumer (D2C)** — the newest e-commerce model; a brand sells directly to '
      'its end customer without going through a retailer, distributor or wholesaler. '
      'Subscriptions are a popular D2C item; social selling via Instagram, Pinterest, TikTok, '
      'Facebook, Snapchat, etc. is popular for D2C sales.',
      '**Manufacturer to Consumer (M2C)** — a form of the D2C model, where manufacturers '
      'relate directly with ultimate consumers, eliminating wholesalers, distributors and '
      'retailers.',
    ]},
  ]},

  {'n': '4.10', 't': 'E-Government', 'b': [
    {'p': 'Governments and public enterprises deploy e-commerce models to enhance efficiency, '
          'transparency and their interactions with businesses, citizens and other governments '
          'and agencies. The COVID-19 pandemic gave a huge boost to e-governance '
          'implementation, because of the enhanced efficiency and the mandatory social/'
          'physical distancing required while delivering services.'},
    {'p': 'According to the United Nations\' definition, e-government comprises three (now '
          'four, with a newly identified category) integral parts:'},
    {'ul': [
      '**Government-to-Government (G2G)** — sharing data and conducting electronic '
      'communications between government agencies: intra- and inter-agency interactions at '
      'the national level, and exchanges between national, provincial and local levels.',
      '**Government-to-Business (G2B)** — a relationship between businesses and government, '
      'where agencies provide services or information to business organizations, using B2G-'
      'style websites that support auctions, tenders and application submission. Services '
      'include: online information/advisory services to businesses; government contracting; '
      'digital procurement marketplaces; business licenses, permits and regulation updates; '
      'electronic auctions; tax payments and reporting; electronic forms; online application '
      'submission; virtual business dispute resolution; online company registration. G2B '
      'refers to business-specific transactions (payments, buying/selling goods and services) '
      'and the provision of business-focused services online.',
      '**Government-to-Citizen (G2C)** — programs meant to make it easier for citizens and '
      'consumers of public services to communicate with government, covering interactions '
      'such as the delivery of public services and participation in consultation and '
      'decision-making processes.',
      '**Government-to-Employees (G2E)** — a newly identified category, involving maintaining '
      'personal information and employee records; includes **e-payroll** (viewing pay cheques, '
      'pay stubs, pay bills, and keeping tax records) and **e-learning** (keeping employees '
      'informed via visuals, animation or videos, through a computer-based learning tool).',
    ]},
  ]},

  {'n': '4.11', 't': 'Electronic payment systems', 'b': [
    {'def': {'t': 'Electronic payment (e-payment)', 'd': 'systems that allow customers to pay '
                  'for goods and services electronically, without the use of cheque or cash.'}},
    {'p': 'Common modes of e-payment: **debit cards**, **credit cards**, **direct bank '
          'deposits**, **e-wallets**, **cryptocurrencies**.'},
    {'p': '**Features of an electronic payment system:**'},
    {'ul': [
      '**Ease of use** — easy to implement and use.',
      '**Security** — provides a secure mode of payment.',
      '**Reliability** — the technology is reliable.',
      '**Scalability** — usable over a wide range/scope of operation.',
      '**Anonymity** — provides anonymity for the transaction.',
      '**Acceptability** — widely accepted as a mode of payment.',
      '**Customer-base** — enhances the merchant\'s ability to widen its customer base.',
      '**Flexibility** — very adaptable to various uses.',
      '**Convertibility** — allows proceeds to be easily converted into other liquid assets.',
      '**Efficiency** — efficient, with very low transaction cost.',
      '**Ease of integration with applications** — easily integrated into other applications '
      'for further processing.',
    ]},
    {'p': '**Benefits of electronic payment to the merchant:** saves time; more efficient; '
          'takes cash out of the equation; more secure; generates more revenue; easier to '
          'administer; certainty of payment.'},
    {'h3': '4.11.1 Automated Teller Machine (ATM)'},
    {'def': {'t': 'Automated Teller Machine (ATM)', 'd': 'also called a bank machine or cash '
                  'machine — an electronic banking outlet that allows customers to complete '
                  'basic transactions without the aid of a branch representative or teller.'}},
    {'p': 'Anyone with a credit or debit card can access cash at most ATMs; there are also '
          'card-less ATMs. No fees are charged for transactions on the ATMs of one\'s own '
          'bank, but fees may be charged on other banks\' ATMs.'},
    {'p': 'Two main types of ATM: **Basic ATM**, which only dispenses cash and displays '
          'balances; and **Complex/Advanced ATM**, which performs other banking transactions '
          'such as accepting deposits, transferring funds between accounts, and bill '
          'settlement.'},
    {'p': '**Components of an ATM:**'},
    {'ul': [
      '**Card reader** — reads the chip on the front of the card or the magnetic stripe on '
      'the back.',
      '**Keypad** — used by the customer to input information: PIN, type of transaction, and '
      'amount.',
      '**Cash dispenser** — dispenses bills through a slot connected to a safe at the bottom '
      'of the machine.',
      '**Printer** — prints receipts on request, recording the type of transaction, amount and '
      'account balance.',
      '**Screen** — issues prompts guiding the consumer through the transaction, and displays '
      'information such as account details and balances.',
    ]},
    {'note': 'Full-service machines also often have slots for depositing paper cheques or '
             'cash.'},
    {'p': '**Benefits of ATM:** easy to use for customers; very efficient; secure mode of '
          'payment; services available round the clock; available in more locations than '
          'bricks-and-mortar banking halls; customers may be served by ATMs of banks other '
          'than their own; reduces transaction cost for banks; reduces the cost of teller '
          'labour.'},
    {'h3': '4.11.2 Mobile payment platforms'},
    {'p': '**Mobile payments** (mobile wallets and mobile money transfers) are digitally '
          'regulated transactions that take place through mobile devices instead of cash, '
          'cheque or physical credit cards.'},
    {'def': {'t': 'Mobile wallet', 'd': 'a virtual wallet that stores payment card information '
                  'on a mobile device, convenient for in-store payments at merchants listed '
                  'with the wallet service provider. Mobile wallets are safe apps for storing '
                  'financial instruments and documents such as credit cards, bank information '
                  'and driver\'s licences; many smart phones come loaded with one. They use '
                  '**near-field communication (NFC)** technology, which requires the user to '
                  'be present when paying, and utilize many layers of encryption and security '
                  'to keep transactions safe.'}},
    {'p': '**Online payment platforms** allow the seller to accept payments and the buyer to '
          'send payments over the internet, offering electronic alternatives to traditional '
          'methods such as money orders and cheques. Examples of online payment companies: '
          '**PayPal, Apple Pay, Stripe, Due, Square**.'},
    {'p': 'Modes of e-payment: **(a) Credit cards** — allow consumers to draw on a line of '
          'credit to pay for goods and services; **(b) Debit cards** — customers draw from an '
          'existing balance to pay; **(c) Digital wallets** — store information on debit/'
          'credit cards, used to pay for goods and services; **(d) Internet banking** — '
          'digitally transferring funds over the internet from one bank account to another, '
          'tending to be used by smaller businesses or personal users; **(e) Direct debit/'
          'bank transfer**.'},
    {'h3': '4.11.3 Card payments'},
    {'def': {'t': 'Payment card', 'd': 'part of a payment system issued by a financial '
                  'institution (e.g. a bank) to a customer, enabling the cardholder to access '
                  'funds in their designated bank accounts, or through a credit account, and '
                  'make payments by electronic transfer and access ATMs.'}},
    {'p': 'Usually debit cards, credit cards, charge cards or prepaid cards; other names '
          'include bank cards, ATM cards, client cards, key cards or cash cards. These cards '
          'are electronically linked to an account (deposit, loan or credit) belonging to the '
          'cardholder, and the card is a means of authenticating the cardholder. It can also '
          'be a smart card containing a unique card number and security information (e.g. an '
          'expiration date) or a magnetic strip on the back enabling machines to read and '
          'access information.'},
    {'h3': '4.11.4 Remita'},
    {'def': {'t': 'Remita', 'd': 'a comprehensive electronic payment platform used for a wide '
                  'range of transactions, including paying bills, transferring money and '
                  'managing finances — used by individuals, businesses, government and '
                  'financial institutions for online and offline payments.'}},
    {'p': '**Usage by individuals:** paying bills (utilities, government fees, other '
          'recurring bills); money transfer (national and international); managing finances '
          '(viewing balances across multiple banks, tracking income/expenses, accessing '
          'detailed transaction reports); mobile app access to all the above features.'},
    {'p': '**Usage for business:** receiving payments from customers via the Remita app, '
          'website, internet banking and POS terminals; payroll and HR solutions; streamlined '
          'payment processes, tracking inflow/outflow in real time; integration with existing '
          'business back-end systems to validate payer details and provide real-time '
          'transaction notifications.'},
    {'p': '**Usage by government and financial institutions:** the **Treasury Single Account '
          '(TSA)** — the default payment gateway for the Federal Government of Nigeria; '
          'government payments (salaries, fees, other obligations); financial institutions can '
          'use Remita to offer payment services to their customers.'},
    {'h3': '4.11.5 Taxpro-Max'},
    {'def': {'t': 'Taxpro-Max', 'd': 'a self-service platform or portal that enables a '
                  'taxpayer to file tax returns, pay taxes, and process and validate Tax '
                  'Clearance Certificates, etc. — enabling seamless registration, filing, '
                  'payment of taxes and automatic credit of withholding tax and other credits '
                  'to the taxpayer\'s account, among other features.'}},
    {'p': '**Benefits of Taxpro-Max:**'},
    {'ol': [
      'Facilitates seamless registration and payment of taxes.',
      'Enables automatic credit of withholding tax and other credits to the taxpayer\'s '
      'account.',
      'Creates ease and convenience for taxpayers in filing returns and paying tax liabilities '
      'from any physical location.',
      'Promotes tax compliance, leading to an increased rate of revenue allocations.',
      'Allows taxpayers to access information about tax laws and regulations without visiting '
      'Federal Inland Revenue Service (FIRS) offices.',
    ]},
  ]},

  {'n': '4.12', 't': 'Digitized middleman', 'b': [
    {'def': {'t': 'Digitized (digital) middleman', 'd': 'a company that gathers information '
                  'about companies providing similar services or products and displays them on '
                  'its own website so customers can procure those products or services through '
                  'that site — typically referred to as digital or online intermediaries: '
                  'companies or platforms that use the internet to connect buyers and sellers, '
                  'often facilitating transactions and charging a commission or fee.'}},
    {'p': 'Examples include online marketplaces, e-commerce platforms and freelance '
          'marketplaces. Notable marketplaces/e-commerce platforms: **Amazon, Alibaba, eBay, '
          'Uber, Jumia, Konga, Jiji**, etc.'},
    {'p': 'Other categories of digitized middleman, grouped by services provided:'},
    {'ul': [
      '**Food delivery services** — platforms like DoorDash and Uber Eats connect customers '
      'with restaurants for food delivery.',
      '**Travel booking websites** — companies like Expedia, Booking.com and Airbnb connect '
      'travellers with lodging, flights and activities.',
      '**Digital music distributors** — platforms like TuneCore and CD Baby distribute music '
      'to streaming services and online music stores.',
      '**Online marketplaces** — e-commerce platforms like Amazon, eBay and AliExpress connect '
      'buyers and sellers for a wide range of goods.',
      '**Social media management platforms** — e.g. Hootsuite and Buffer, help businesses '
      'manage their social media presence, acting as intermediaries.',
      '**Digital identity providers** — platforms that manage and store digital identities, '
      'like Google\'s OAuth and Facebook\'s login services.',
    ]},
    {'h3': '4.12.1 Amazon and digital middleman'},
    {'p': 'Amazon functions as a digitized middleman in Nigeria by facilitating e-commerce '
          'transactions between buyers and sellers, offering services like Prime Video, and '
          'expanding its cloud services through Amazon Web Services (AWS). It provides a '
          'platform for Nigerian consumers to buy from national and international sellers, '
          'while enabling Nigerian businesses to sell globally through the Amazon network.'},
    {'p': '**Key services provided by Amazon:** acts as an e-commerce platform; Prime Video '
          'provides movies and TV shows for Nigerian audiences; AWS provides cloud computing '
          'services to local businesses and start-ups, from data storage/processing to '
          'application development; provides a platform for Nigerian businesses to sell their '
          'products, directly or through the seller network. Amazon acts as a digitized '
          'middleman by facilitating transactions, providing infrastructure, and offering '
          'services that connect buyers, sellers and content creators in Nigeria.'},
    {'h3': '4.12.2 eBay as a middleman'},
    {'p': 'eBay functions as a digitized middleman in Nigeria by providing a platform where '
          'Nigerian sellers and buyers can connect and transact, primarily through auctions '
          'and fixed-price listings — acting as an intermediary, facilitating the exchange of '
          'goods and services while providing payment processing and shipping options.'},
    {'p': '**Key responsibilities of eBay:** brings together buyers and sellers worldwide; '
          'offers both auction-style and fixed-price listings; integrates with payment methods '
          'including PayPal, for secure and reliable transactions; provides tools and '
          'resources for sellers to manage shipping (domestic and international); provides the '
          'infrastructure and platform for buyers and sellers to interact; earns revenue via '
          'commissions and fees charged to both sellers and buyers; offers measures to protect '
          'both buyers and sellers via feedback systems, buyer protection policies and dispute '
          'resolution; is subject to regulation under the **Digital Services Act (DSA)**, '
          'which outlines the obligations of digital services acting as intermediaries.'},
  ]},

  {'n': '4.13', 't': 'Revenue models', 'b': [
    {'def': {'t': 'Revenue model', 'd': 'a blueprint for how a company produces income from '
                  'its services or products — the methods through which a business makes '
                  'money, including how it prices its product and which sales channels it '
                  'chooses. A revenue model is established to answer how a company plans to '
                  'financially optimize its business model.'}},
    {'p': 'Several types of revenue model exist, including **ad-based, affiliate, '
          'transactional, subscription, channel sales, commission marketplace, licensing, and '
          'retail**. Common examples include product/information sales, online advertising, '
          'subscription-based services and transaction fees.'},
    {'p': '**Benefits of implementing revenue models:** financial sustainability, pricing '
          'strategy, profitability analysis, scalability, decision-making, investor '
          'confidence.'},
    {'h3': '4.13.1 Drop-shipping business model'},
    {'def': {'t': 'Drop shipping', 'd': 'a retail fulfilment method where a business sells '
                  'products online without holding any inventory. When a customer places an '
                  'order, the business passes it on to a third-party supplier, who ships the '
                  'product directly to the customer, letting the entrepreneur focus on '
                  'marketing and sales without managing inventory or shipping — with lower '
                  'initial investment, a wide range of selectable products, and reliance on '
                  'the supplier.'}},
    {'h3': '4.13.2 Wholesale revenue model'},
    {'def': {'t': 'Wholesale revenue model', 'd': 'selling goods in bulk to other businesses '
                  '(e.g. retailers) at discounted prices, generating revenue from the '
                  'difference between the purchase price and the sale price. It works when the '
                  'wholesaler bulk-purchases and resells to businesses, acting as an '
                  'intermediary between manufacturer and retailer and helping to streamline '
                  'the distribution process.'}},
    {'h3': '4.13.3 Private labelling revenue model'},
    {'def': {'t': 'Private labelling (white labelling / private branding)', 'd': 'a business '
                  'model where a company (the retailer) outsources the manufacturing of a '
                  'product to a third-party manufacturer and sells it under its own brand '
                  'name; the retailer designs the product, specifies manufacturing '
                  'requirements, and handles branding, marketing and sales.'}},
    {'p': '**Key elements:** outsourcing manufacturing; branding and marketing; sales and '
          'distribution.'},
    {'p': '**How it works:** the retailer designs the product and provides specifications to '
          'the manufacturer; the manufacturer produces the product to specification; the '
          'retailer applies its own branding, packaging and labelling; the retailer markets '
          'and sells the product under its own brand name.'},
    {'p': '**Benefits of private/white labelling:**'},
    {'ol': [
      'Allows businesses to enter a market with a product with reduced upfront investment.',
      'Allows businesses to easily scale operations by adjusting production volumes and '
      'adding new products.',
      'Retailers have complete control over branding, packaging and marketing.',
      'Allows retailers to offer unique/exclusive products unavailable from competitors.',
      'Can be more cost-effective than traditional manufacturing, especially for smaller '
      'businesses.',
    ]},
    {'p': '**Examples** of private/white labelling: grocery stores, fashion retailers, '
          'e-commerce businesses. **Types** of private/white label: **(1) generic brands; '
          '(2) copycat brands; (3) premium store brands; (4) value innovations.**'},
    {'h3': '4.13.4 Subscription business revenue model'},
    {'def': {'t': 'Subscription revenue model', 'd': 'a business strategy where customers pay '
                  'a recurring fee for access to a service or product, generating ongoing '
                  '(recurring) revenue by charging customers a recurring fee processed at '
                  'regular intervals — built on establishing long-term customer '
                  'relationships.'}},
    {'p': 'Examples: **Spotify** (music streaming access), **Netflix** (movie/TV content), '
          '**Mailchimp** (email marketing tools). Features: receiving payment and access to '
          'services/products.'},
    {'p': 'Types of subscription: **(1) Digital subscriptions** (e.g. streaming services); '
          '**(2) Physical subscriptions** (receiving physical products delivered regularly, '
          'e.g. subscription boxes); **(3) Membership subscription** (access to a community, '
          'exclusive content and benefits).'},
    {'h3': '4.13.5 Government revenue model'},
    {'def': {'t': 'Government revenue', 'd': 'the total income received by government from '
                  'various sources — the money government collects to finance its operations, '
                  'public services and other programs; the opposite of government spending, '
                  'and a key tool of fiscal policy.'}},
    {'p': '**Sources of government revenue:** taxes (on income, wealth, consumption goods, '
          'investment, property, etc.); non-tax revenue (income from government-owned '
          'corporations, fines, fees, assets, sales and other sources); social insurance '
          'levies (e.g. payroll taxes funding social security, Medicare, etc.).'},
    {'p': 'In summary, government revenue is money received from taxes and non-tax sources to '
          'enable government to assume full resource employment and undertake non-'
          'inflationary public expenditure.'},
  ]},

  {'n': '4.14', 't': 'Chapter summary', 'b': [
    {'ul': [
      'The smallest unit of data is the **byte** (8 bits); a **character** can be alphabetic, '
      'numeric or a special symbol.',
      'A **field** is a combination of characters; a **record** is a collection of related '
      'fields; a **file** is a collection of records.',
      'A **primary key** is a unique identifier for a record.',
      'Files are organized as **serial, sequential, indexed sequential and random** on disk.',
      '**Batch processing** updates master files at a predetermined time period.',
      '**Online processing** is a technique where data is entered as it occurs.',
      '**Online real-time processing** processes data as it occurs, with results obtained '
      'immediately — used in critical events.',
      'Configuration of processing methods may be **centralized, decentralized or '
      'distributed**.',
      'Types of CPU and OS also determine processing methods such as **multitasking, '
      'multiuser, multiprocessing and multiprogramming**.',
      'Staffing and roles of the Information Centre.',
      'Information systems and electronic business technologies.',
      'E-commerce and its various models.',
      'Electronic payment methods and digitized middlemen.',
    ]},
  ]},

  {'n': '4.15', 't': 'End-of-chapter questions (study text)', 'b': [
    {'h3': 'Multiple-choice questions'},
    {'warn': 'The printed study text\'s MCQ set skips a numbered question — it jumps straight '
             'from Q18 to Q20, so Q19 has an answer key entry ("19. D") but no printed '
             'question stem; reproduced here exactly as printed. The key also gives **"18. B" '
             'for the question "the number system of 0 and 1 is called ____" whose own '
             'options list D as "binary"** — likely a misprint in the source (the correct '
             'answer should be D); flagged rather than silently corrected.'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–27 with answers', 'open': True, 'q': [
      {'ol': [
        'Which ONE of the following is odd? (A) Batch Processing  (B) Online processing  '
        '(C) Independent processing  (D) Real-time processing  (E) Online Batch processing',
        'Which ONE of the following is odd? (A) Updating  (B) Referencing  (C) File '
        'processing  (D) File maintenance  (E) File Enquiry',
        'A type of processing method that allows tasks to be gathered over a period of time '
        'and processed at the same time is called … processing. (A) Batch Processing  '
        '(B) Realtime Processing  (C) Online  (D) Job Remote Entry  (E) Centralized Processing',
        'A type of computer bureau formed specifically to render computing services to '
        'clients is referred to as … companies. (A) Independent companies  (B) Computer users '
        'with spare capacity  (C) Software developers  (D) Technical support  (E) Data '
        'processing',
        'Which of the following facilities CANNOT be taken over by facilities management? '
        '(A) Project management assistance  (B) Taking over employment contracts of IT staff  '
        '(C) Redeployment of IT staff to other departments  (D) Complete control of system to '
        'service other departments  (E) Running the entire Information System function',
        'The following are data processing methods EXCEPT (A) Transaction processing  '
        '(B) Batch processing  (C) Online processing  (D) Real-time processing  (E) Ring '
        'processing',
        'A transaction processing technique with severe time limitation is called (A) Time '
        'sharing processing  (B) Distributed processing  (C) Real-time processing  '
        '(D) Multitasking  (E) Multiprocessing',
        'Which of the following is NOT an example of a real-time application? (A) Payroll  '
        '(B) Airline reservation system  (C) Credit card system  (D) Missile guidance system  '
        '(E) Stock control system',
        'What is the processing technique by which many processors are used to accomplish '
        'data processing? (A) Multiple processing  (B) Multiprocessing  (C) Multiple '
        'processor  (D) Multiprocessing  (E) Multiple programming',
        'Which one of the following is NOT a data processing method? (A) Batch processing  '
        '(B) Online processing  (C) Distributed processing  (D) Multiprogramming  '
        '(E) Direct processing',
        'Data processing carried out by the use of large computers in a single location is '
        'described as … (A) Centralized  (B) Decentralized  (C) Distributed  (D) Realtime  '
        '(E) Online',
        'The use of multiple computers in different locations linked by a communication '
        'network, so that a single job is shared between them, is called … (A) Centralized  '
        '(B) Decentralized  (C) Distributed  (D) Realtime  (E) Online',
        'Accumulating source documents into groups prior to processing is a characteristic of '
        '… processing (A) Batch  (B) Realtime  (C) Online  (D) Remote Job Entry  (E) Star '
        'Topology',
        'An information system that responds immediately to the needs of the physical system '
        'is called a … system (A) Batch  (B) Realtime  (C) Online  (D) Remote Job Entry  '
        '(E) Star Topology',
        'Which ONE of the following information systems monitors the elementary activities '
        'and transactions of the organization? (A) Management level system  (B) Operational '
        'level system  (C) Knowledge level system  (D) Strategic level system  (E) Enterprise '
        'level system',
        'Projections and responses to queries are information-output characteristics '
        'associated with … (A) Decision Support System (DSS)  (B) Management Information '
        'System (MIS)  (C) Executive Support System (ESS)  (D) Transaction Processing System '
        '(TPS)  (E) Office Information System (OIS)',
        'Summary transaction data, high-volume data, and simple models are information-input '
        'characteristics of … (A) Decision Support System (DSS)  (B) Management Information '
        'System (MIS)  (C) Executive Support System (ESS)  (D) Transaction Processing System '
        '(TPS)  (E) Office Information System (OIS)',
        'In computers, the number system of 0 and 1 is called … (A) octal  (B) hexadecimal  '
        '(C) decimal  (D) binary  (E) dual',
        '[Question 19 as printed: no stem is given in the study text; only the answer key '
        'entry "19. D" exists.]',
        'OLX is an example of a(n) … e-commerce segment. (A) B2B  (B) B2C  (C) C2B  (D) C2C  '
        '(E) G2C',
        'Customers pay a fixed amount, usually monthly, quarterly or annually, to get some '
        'type of service. This is known as the … E-Commerce Business Model. (A) Licensing  '
        '(B) Transaction  (C) Affiliate  (D) Subscription fee-based',
        'E-commerce has … scope than E-Business or Digital Business. (A) Higher  (B) Narrower  '
        '(C) Wider  (D) Deeper  (E) Better',
        'Companies like Flipkart, Amazon and Myntra belong to which type of e-commerce '
        'segment? (A) B2B  (B) B2C  (C) P2P  (D) C2B  (E) C2C',
        'The concept of online marketing and selling of products and services through the '
        'internet is … (A) B2G  (B) B2C  (C) B2B  (D) B2E  (E) M2C',
        'What is the percentage of customers who visit a website and actually buy something '
        'called? (A) Affiliate programs  (B) Click-through  (C) Spam  (D) Conversion rate  '
        '(E) Hit rate',
        'What is the process in which a buyer posts its interest in buying a certain quantity '
        'of items, and sellers compete for the business by submitting successively lower bids '
        'until only one seller is left? (A) B2B marketplace  (B) Intranet  (C) Reverse auction  '
        '(D) Internet  (E) Electronic bidding',
        'What are plastic cards the size of a credit card that contain an embedded chip on '
        'which digital information can be stored? (A) Customer Relationship Management '
        'system cards  (B) E-government identity cards  (C) Credit cards  (D) Smart cards  '
        '(E) Call cards',
      ]}],
      'a': [
      {'p': '**1.** C  **2.** C  **3.** A  **4.** A  **5.** C  **6.** E  **7.** C  **8.** A  '
            '**9.** B  **10.** C  **11.** A  **12.** C (Distributed)  **13.** A  **14.** B  '
            '**15.** B  **16.** B  **17.** C  **18.** B (printed; but the question\'s own '
            'options make D "binary" the technically correct answer)  **19.** D (no printed '
            'stem)  **20.** D  **21.** D  **22.** B  **23.** B  **24.** B  **25.** D  '
            '**26.** C  **27.** D'}]}},
    {'h3': 'Self-assessment questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–5 with answers', 'open': True, 'q': [
      {'ol': [
        'Describe the purpose of an information centre in an organization.',
        'What is a computer service bureau?',
        'Give any two reasons to show why facilities management is beneficial to an '
        'organization.',
        'What is meant by the term "helpdesk"?',
        'Give any two reasons why the accountant finds the microcomputer quite invaluable.',
      ]}],
      'a': [
      {'ol': [
        '**In the organization, an information centre gives the end-users of information '
        'systems the opportunity to interact with experts to get their work done, without '
        'putting undue pressure on the Information Systems staff.**',
        '**A computer service bureau is an organization set up to offer computing services to '
        'individuals or other organizations that require such facilities but are not in a '
        'position to provide them for themselves.**',
        '**An organization might enter a facilities management contract because: (i) it might '
        'not have staff with the requisite skills or management competence to help itself; '
        '(ii) it may require the needed solution more cheaply and with the highest level of '
        'expertise.**',
        '**A help desk is an office established with at least two staff members equipped with '
        'reliable telephone facilities, used to receive complaints and problems from end-users '
        'of the system and find appropriate solutions from among the staff of the information '
        'centre.**',
        '**The accountant finds the microcomputer invaluable because: (i) it is very '
        'user-friendly and can be carried to any place where the accountant may be working; '
        '(ii) there are numerous microcomputer-based software products the accountant can use '
        'for any job requiring a computer, and these products are inexpensive and '
        'user-friendly.**',
      ]}]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'The examiner loves confusing the four CPU/OS processing modes (time-sharing, '
   'multitasking, multiprocessing, multiprogramming) with the three processing configurations '
   '(centralized, decentralized, distributed) and the four processing techniques (batch, '
   'online, real-time, RJE) — keep all three groups separate in your head. Also memorise the '
   'growing list of Nigerian public-sector systems (GIFMIS, IPPIS, UTAS, ATRRS, Open Treasury '
   'Portal, Remita, Taxpro-Max) with one distinguishing fact each, and the e-commerce/'
   'e-government model initialisms (B2C/B2B/C2C/C2B/D2C/M2C and G2G/G2B/G2C/G2E).',
 'errors': [
   'Saying all online systems are real-time — online batch processing is online but not '
   'real-time.',
   'Confusing multiprogramming (one processor switching between programs, based on I/O '
   'interrupts) with time-sharing (predetermined time slices for each of several users).',
   'Mixing up GIFMIS (budget/accounting/public expenditure management) with IPPIS (personnel '
   'records and payroll) — they are both Nigerian public-sector systems but serve different '
   'functions.',
   'Treating "Digitized Middleman" and "E-commerce" as the same thing — a digitized middleman '
   'is one type of e-commerce business model (an intermediary), not the whole field.',
   'Assuming DSS and MIS serve the same decision level — MIS supports structured, routine '
   'decisions; DSS is for semi-structured/unstructured problems for middle-to-senior '
   'management.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Updating master files periodically, at predetermined times or once a manageable '
         'number of transactions has accumulated, is called',
    'o': ['Real-time processing', 'Batch processing', 'Remote Job Entry',
          'Distributed processing', 'Online processing'],
    'a': 1,
    'w': 'Batch processing accumulates transactions and updates the master file at scheduled '
         'intervals or when enough transactions have gathered — the time between submission '
         'and the return of results is the turn-around time.',
    'src': 'Chapter 4.1.1', 'sec': '4.1'},
   {'q': 'A processing configuration in which each department does its own processing with '
         'its own IT staff, with no link between departments or to headquarters, is called',
    'o': ['Centralized processing', 'Distributed Data Processing', 'Decentralized processing',
          'Time-sharing', 'Multiprocessing'],
    'a': 2,
    'w': 'Decentralized processing gives each department its own independent processing '
         'capability. Distributed Data Processing is the hybrid that links every location to '
         'each other and to the corporate server.',
    'src': 'Chapter 4.2.2', 'sec': '4.2'},
   {'q': 'A computer with more than one CPU, where processes are assigned to whichever CPU is '
         'free and memory is shared among the CPUs, is running',
    'o': ['asymmetric multiprocessing', 'symmetric multiprocessing', 'multiprogramming',
          'time-sharing', 'pre-emptive multitasking'],
    'a': 1,
    'w': 'Symmetric multiprocessing shares memory and assigns any available CPU to a process; '
         'asymmetric multiprocessing dedicates a specific CPU (with its own memory) to a '
         'specific type of processing.',
    'src': 'Chapter 4.3', 'sec': '4.3'},
   {'q': 'A computer program that uses artificial intelligence techniques to solve problems '
         'that would normally require a knowledgeable human is a(n)',
    'o': ['Decision Support System', 'Transaction Processing System', 'Expert System',
          'Office Information System', 'Executive Support System'],
    'a': 2,
    'w': 'An Expert System reproduces the performance of a human expert in a specific problem '
         'domain, typically built on a knowledge base plus a way of codifying the expert\'s '
         'knowledge, e.g. INTERNIST for medical diagnosis.',
    'src': 'Chapter 4.7.2(g)', 'sec': '4.7'},
   {'q': 'GIFMIS is best described as a system for',
    'o': ['managing personnel records and payroll for Nigerian government employees',
          'budget management, accounting and public expenditure management',
          'a proposed replacement for IPPIS championed by ASUU',
          'recording transactions at Federal Pay Offices onto compact disks',
          'a self-service portal for filing and paying taxes'],
    'a': 1,
    'w': 'GIFMIS modernizes fiscal processes across the budget preparation-to-reporting cycle. '
         'Personnel/payroll is IPPIS; the ASUU-proposed alternative is UTAS; the CD-based '
         'transaction recording system is ATRRS; the tax filing portal is Taxpro-Max.',
    'src': 'Chapter 4.7.2(i)', 'sec': '4.7'},
   {'q': 'A business selling directly to its end customer, without going through a retailer, '
         'distributor or wholesaler — popular for subscriptions and social selling — is the',
    'o': ['B2B model', 'C2B model', 'Direct to Consumer (D2C) model', 'G2C model',
          'Wholesale revenue model'],
    'a': 2,
    'w': 'D2C cuts out every intermediary between brand and end customer. When a manufacturer '
         'specifically does this, it is called M2C — a form of D2C.',
    'src': 'Chapter 4.9', 'sec': '4.9'},
  ],
  'theory': [
   {'q': '(a) Distinguish between batch processing and real-time processing. (b) State any '
         'FOUR advantages of real-time processing.',
    'marks': 10,
    'a': [
      {'p': '(a) In **batch processing**, transactions are accumulated over a period and the '
            'master file is updated at predetermined times or once a manageable number of '
            'transactions has gathered; results are delayed (turn-around time applies). In '
            '**real-time processing**, data is captured electronically, edited and processed '
            'immediately, so results are available quickly enough to influence the activity '
            'currently taking place — used for critical systems, e.g. airline reservation and '
            'space exploration.'},
      {'h4': '(b) Advantages of real-time processing (any four)'},
      {'ol': [
        'Computer output is instantaneously made available.',
        'The output can be used to influence the transaction.',
        'Avoids time-consuming and unnecessary paperwork.',
        'Enables users to see the cumulative effect of all transactions for decision making.',
        'Avoids costly and time-consuming data preparation and control operations.']}],
    'src': 'Chapter 4.1', 'sec': '4.1'},
   {'q': 'Enumerate the services provided by a computer bureau, and state any THREE reasons '
         'an organization might choose to use one.',
    'marks': 12,
    'a': [
      {'h4': 'Services of a computer bureau'},
      {'ol': [
        'Data preparation.', 'Program preparation and testing.', 'Hiring of computer time.',
        'Hiring of computer systems.', 'Do-it-yourself service.', 'Time-sharing facility.',
        'Sales of computer system resources.', 'Repairs and maintenance.',
        'Acting as an information centre.', 'System installation.', 'Training of staff.',
        'Feasibility study consultants.']},
      {'h4': 'Reasons for using a bureau (any three)'},
      {'ol': [
        'To obtain valuable initial experience of computer processing before deciding whether '
        'to install an in-house system.',
        'To provide a standby facility in case of breakdown of the in-house computer.',
        'To cope with peak data processing loads owing to insufficient in-house capacity.',
        'Non-availability of liquid funds for installing an in-house computer.']}],
    'src': 'Chapter 4.6.3', 'sec': '4.6'},
   {'q': 'List the five main components of an information system, and state the five '
         'historical eras of Management Information System (MIS) identified by Laudon and '
         'Laudon.',
    'marks': 10,
    'a': [
      {'h4': 'Components of an information system'},
      {'ol': ['Computer hardware.', 'Computer software (system + application).',
        'Telecommunication networks.', 'Databases and data warehouses.',
        'Human resources (IT specialists, security experts, management, users).',
        'Procedures and processes.']},
      {'h4': 'Five eras of MIS'},
      {'ol': ['Mainframe and minicomputer computing.', 'Personal computers.',
        'Client/server networks.', 'Enterprise computing.', 'Cloud computing.']}],
    'src': 'Chapter 4.7', 'sec': '4.7'},
   {'q': 'Distinguish between Government-to-Government (G2G), Government-to-Business (G2B), '
         'Government-to-Citizen (G2C) and Government-to-Employees (G2E) e-government models.',
    'marks': 8,
    'a': [
      {'ul': [
        '**G2G** — sharing data and electronic communications between government agencies, '
        'both intra-agency and inter-agency, and across national, provincial and local '
        'levels.',
        '**G2B** — government agencies providing services or information to business '
        'organizations, e.g. online tendering, digital procurement, business licensing, tax '
        'payments and reporting.',
        '**G2C** — programs making it easier for citizens to communicate with government, '
        'covering delivery of public services and participation in consultation/decision-'
        'making.',
        '**G2E** — maintaining personal information and employee records, including e-payroll '
        'and e-learning for government employees.']}],
    'src': 'Chapter 4.10', 'sec': '4.10'},
   {'q': 'Explain the drop-shipping, wholesale, and subscription revenue models, giving one '
         'example of each.',
    'marks': 9,
    'a': [
      {'ul': [
        '**Drop shipping** — a retailer sells online without holding inventory; orders are '
        'passed to a third-party supplier who ships directly to the customer. Example: a '
        'small online store listing products it never stocks itself.',
        '**Wholesale** — selling goods in bulk to other businesses at a discount, earning the '
        'margin between purchase and sale price. Example: a wholesaler supplying retail '
        'shops.',
        '**Subscription** — customers pay a recurring fee for ongoing access to a service or '
        'product. Example: Netflix (movies/TV) or Spotify (music streaming).']}],
    'src': 'Chapter 4.13', 'sec': '4.13'},
  ]},
}
