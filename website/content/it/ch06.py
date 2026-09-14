CH = {
 'n': 6,
 't': 'Systems Development and Issues in Management of Information',
 'brief': 'The Systems Development Life Cycle and structured methodologies (SSADM), '
          'prototyping/JAD/RAD, outsourcing, computer security/viruses/cybercrime/cyber law, '
          'workplace health, computer forensics, Big Data, and the disruptive technologies — '
          'AI/machine learning, IoT, distributed ledgers/blockchain, cryptocurrency, robotics/'
          'business automation and drones.',
 'outcomes': [
   'Understand what is meant by the development of a computer-based system',
   'Understand the cycle of stages that the development of a typical system goes through',
   'Understand the importance of user involvement in the development of a system',
   'Appreciate the concept of prototyping and its importance',
   'Understand the concept and application of outsourcing',
   'Understand the crimes committed by internal users of computers',
   'Understand the definition and application of forensics in legal issues',
   'Understand the concept of Big Data',
   'Understand cloud computing',
   'Appreciate disruptive technologies and their impact on business',
 ],
 'secs': [
  {'n': '6.1', 't': 'Systems Development Life Cycle (SDLC)', 'b': [
    {'p': 'New computer systems frequently replace existing systems, and this process of '
          'replacement is organised into a series of stages called the **systems life cycle**. '
          'It is the traditional method for developing new systems; newer alternative methods '
          'attempt to improve on it. Our focus is the traditional method, the **Systems '
          'Development Life Cycle (SDLC)**, developed by the **National Computing Centre '
          '(NCC)** in the UK in **1960**.'},
    {'h3': 'Stages of the SDLC'},
    {'p': 'The seven stages: **Problem Definition → Feasibility Study → Systems Definition → '
          'Systems Investigation → System Analysis → System Design → System Implementation → '
          'Post-Implementation Review**.'},
    {'h4': '(a) Problem definition'},
    {'p': 'Analysis of the system (or sub-system) in conjunction with users, so that their '
          '**actual** requirements are identified, rather than their likely requirements.'},
    {'h4': '(b) Feasibility study'},
    {'def': {'t': 'Feasibility study', 'd': 'a formal, detailed study to decide what type of '
                  'system can be developed to meet the needs of users or the organization. Its '
                  'goal is to identify, as quickly as possible, whether the benefits of a '
                  'proposed project appear to outweigh its expected cost and disruption, based '
                  'on what is already known. Since early estimates may be overly optimistic, a '
                  'feasibility study is usually repeated at various points through the SDLC, to '
                  'decide whether to continue, revise or abandon the project.'}},
    {'h4': '(c) Systems definition (systems specification)'},
    {'p': 'The systems specification is the detailed documentation of the proposed new system, '
          'serving two purposes: **(i) Communication** — to management for final approval, to '
          'programmers so they can write the necessary programs, to operating staff detailing '
          'necessary operating procedures, and to users, whose agreement is essential since '
          'they will run the system; **(ii) Record** — a permanent record used for evaluation, '
          'modification and training.'},
    {'p': '**Terms of reference** are set up by a management **steering committee**, whose '
          'functions may include: investigating and reporting on the existing system, its '
          'procedures and cost; defining the system\'s requirements; establishing whether the '
          'existing system meets them, or whether an alternative could; specifying performance '
          'criteria; recommending the most suitable system; preparing a detailed cost budget '
          'within a specified limit; preparing a draft implementation plan within a specified '
          'time frame; establishing whether expected benefits can be realised; establishing a '
          'detailed design/implementation/operating budget; comparing it with the current '
          'system\'s cost; setting the report-back date; and identifying operational managers '
          'the study group may approach.'},
    {'h4': 'Criteria for project selection'},
    {'p': 'Four key areas (criteria) in which a project must be feasible:'},
    {'ul': [
      '**Technical feasibility** — the system requirements must be technically achievable, '
      'using available hardware, software and other equipment, considering transaction '
      'volumes, storage capacity, response times, and number of users.',
      '**Operational feasibility** — the option must not lead to inefficiency or '
      'ineffectiveness; operational changes must enhance the attainment of business objectives.',
      '**Social feasibility** — addresses personnel problems, job enrichment, threats to '
      'industrial relations, expected skills requirements, motivation, and social/'
      'environmental impact.',
      '**Economic feasibility** — a system satisfying all the above criteria must still be a '
      'good investment, able to recover the amount invested and realise profits.',
    ]},
    {'h4': 'Costs and benefits'},
    {'p': 'The cost of an Information System project falls under:'},
    {'ul': [
      '**One-off costs** — hardware, software, other equipment and project team costs; cost '
      'of producing documentation; training cost; cost of installing the system.',
      '**Running (operating) costs** — staff salaries; overheads; training; maintenance; '
      'utilities and consumables; insurance and financing.',
    ]},
    {'p': 'Benefits include non-quantitative/qualitative ones (better decision-making, fewer '
          'delays, better services, competitive advantage) and quantitative/tangible ones '
          '(reduction in waste, increase in revenues).'},
    {'h4': 'Cost-benefit analysis'},
    {'p': 'Complicated by the fact that a number of benefits are qualitative and '
          'non-quantifiable. Approaches available:'},
    {'ul': [
      '**Payback period method** — calculates how long a project takes to recoup the initial '
      'investment (pay for itself), based on cash flows. Disadvantage: does not consider the '
      'present value of future inflows.',
      '**Discounted Cash Flow (DCF)** — two approaches: **(i) Net Present Value (NPV)** — '
      'considers all relevant cash flows over the project\'s life, discounted to "present '
      'value" at a rate called the "cost of capital". A **positive NPV** means the project is '
      'feasible; a **negative NPV** means discounted outflows exceed discounted inflows, so '
      'it is not feasible; a **zero NPV** reflects break-even, and the project should not be '
      'undertaken. **(ii) Internal Rate of Return (IRR)** — compares the project\'s expected '
      'discounted rate of return with the cost of capital; projects with IRR higher than the '
      'cost of capital are worth undertaking.',
      '**Cost-benefit ratio** — used where cash is a constraint and NPV alone may mislead; '
      'also called the profitability index, or NPV per ₦ initial outlay: '
      '$\\text{Cost-benefit ratio} = \\dfrac{\\text{NPV}}{\\text{Initial outlay}}$.',
    ]},
    {'h4': 'The feasibility study report'},
    {'p': 'A formal report written by the project manager, submitted to the Steering '
          'Committee, seeking agreement to proceed. Contents: **executive summary** (a short '
          'summary of the whole report); **terms of reference** (restated); **current system '
          'issues** (good and bad sides found during the study); **evaluation of each option** '
          '(strengths and weaknesses); **description of the options** (why each was '
          'selected); **feasibility** (how each option met the selection criteria); '
          '**conclusion** (the team\'s final choices); and **recommendation** (seeking '
          'permission to continue).'},
    {'h4': '(d) Systems investigation'},
    {'p': 'A fact-finding exercise investigating the existing system to assess its problems '
          'and requirements — data volumes, response time and other key indicators. Steps: '
          '**(1) fact-finding** (interviews, questionnaires, observation, organisation '
          'charts); **(2) fact recording** (flowcharts, decision tables, narrative '
          'descriptions, organisation/responsibility charts); **(3) evaluation** (assessing '
          'strengths and weaknesses of the existing system).'},
    {'h4': 'Fact-finding methods'},
    {'p': '**(i) Questionnaires** — needed when collecting information from widely dispersed '
          'respondents; may be used ahead of an interview to save time. Used to ensure '
          'consistency of approach, achieve a logical flow of questions, avoid omissions, and '
          'ensure data is collected in a form suitable for tabulation and analysis. A '
          'questionnaire should: **not** contain too many questions (may discourage '
          'co-operation); be organised in a logical sequence; include an occasional '
          'corroborating question, to check honesty/realism of responses; be designed with '
          '**dichotomous questions** (attracting only one of two answers, e.g. yes/no) as much '
          'as possible; be independently tested before issue, to check it is simple, '
          'unambiguous and easily answered; and take into account respondents\' job-security '
          'sensitivities, avoiding asking for their identities if honest responses are wanted.'},
    {'p': '**(ii) Interviews** — the analyst meets face-to-face with staff to obtain vital '
          'information; if properly conducted, breaks through fears and resistance to change, '
          'as well as gathering facts. The analyst must adapt their approach to the individual '
          'interviewee rather than follow a standard routine, plan interviews well, and have '
          'ready, convincing answers to questions about how the project may affect '
          'interviewees.'},
    {'table': {'cap': 'Interview guidelines', 'align': 'll', 'head': ['DO', "DON'T"], 'rows': [
      ['Plan for the interview', "Be late (disturbs the interviewee's schedule)"],
      ['Make appointments and be committed to meeting them', 'Be too formal or too casual (to '
       'identify with the group)'],
      ['Identify the right people to answer questions', 'Interrupt (to help the free flow of '
       'information)'],
      ['Listen carefully, since the exercise is meant to learn about the system in use', 'Use '
       'technical jargon (ensures questions are understood and answered)'],
      ['Use the local terminology appropriate to the type of job', 'Confuse opinions with '
       'facts'],
      ['Accept ideas and hints from the interviewee', 'Jump to conclusions (this is a '
       'learning process)'],
      ['Hear from all people who join efforts to complete a task', 'Argue (might offend the '
       'interviewee)'],
      ['Collect documents/forms — these may be needed for a future system', 'Criticise'],
      ['Check facts back, to ensure correctness of information', 'Suggest (any suggestion '
       'might distort the real issues)'],
      ['Part pleasantly, showing appreciation — there might be a need for a repeat visit', ''],
    ]}},
    {'p': '**(iii) Observation** — once the analyst understands the organisation\'s methods '
          'and procedures, observing operations verifies findings and clarifies problem areas, '
          'cross-checking facts from interviews/questionnaires. Reliable results need maximum '
          'co-operation from those observed, since staff may act differently if they know they '
          'are being watched. Long periods on any one staff member should be avoided, since it '
          'may make the subject nervous and the observer sleepy — shifting from person to '
          'person keeps the observer active and awake.'},
    {'h4': '(e) System analysis'},
    {'p': 'A thorough, detailed description of the current system, documenting its strengths '
          'and weaknesses and why it works the way it does; identifies what role its strengths '
          'may have in future processing. Examines why current methods are used, what '
          'alternatives might achieve the same or better results, what restricts the system\'s '
          'effectiveness, and what performance criteria are required.'},
    {'h4': '(f) System design'},
    {'p': 'A technical stage considering both computerised and manual procedures — inputs, '
          'outputs, program design, file design and security — leading to a detailed '
          'specification, also called the **"logical design"**. It is the process of creating '
          'alternative solutions to meet the feasibility study\'s goals, evaluating the '
          'choices, and specifying the chosen alternative, deciding how to produce an '
          '**efficient** (economical) and **effective** (relevant and useful) system.'},
    {'p': '**Design reviews and walkthroughs (user validation)** — a crucial approach: the '
          'analyst breaks the process into sections ("**milestones**"); at each milestone, the '
          'resulting output ("**deliverable**") is presented to users for approval, in '
          'periodic sessions where interested users "walk through" the input and processing '
          'operations. Users look for errors and comment; honest review ensures necessary '
          'corrections. A **formal sign-off** on each section is required before the next can '
          'begin. Any late changes should stem only from unanticipated changes in user '
          'requirements, if everyone involved did what was expected.'},
    {'h4': '(g) System implementation'},
    {'p': 'Carries development from design to operations: acquisition (or writing) of '
          'software, program testing, file conversion, file set-up, education and training, '
          'hardware acquisition and installation, and changeover — turning the theoretical '
          '("logical") design into a working ("physical") system.'},
    {'p': '**System testing** — ensures the system works accurately and efficiently before '
          'live operations, testing hardware, software and staff in a live or simulated '
          'environment, to prove the computer and clerical procedures are understood and '
          'produce the required results.'},
    {'p': '**Education and training** — education creates the right atmosphere and motivates '
          'user staff, established first at senior level for greater effectiveness lower down; '
          'it overcomes resentment at the computer seeming to remove responsibility, and '
          'allays fears of redundancy/job loss. Training equips staff with changeover '
          'procedures and new-system procedures (not the full operating skill needed later).'},
    {'p': '**File conversion** — converting old file data into the form required by the new '
          'system, usually involving live files (e.g. stock, customer files) — a major '
          'organisational/scheduling difficulty since incoming data continually updates them. '
          'Large-file conversion may separate and convert the **static** part of each record '
          'first, converting the **dynamic** contents as late as possible, then merging them '
          'into complete new records/files.'},
    {'p': '**File set-up** — creating the new computer files from the converted data, usually '
          'via special "once-only" conversion programs. Main problems: accuracy of conversion '
          'and error detection; users must be satisfied with the new files, and master-file '
          'data at changeover must be accurate. Incorrect data may arise from: errors in the '
          'original source document; clerical transcription errors; data entry errors; or a '
          'faulty conversion program.'},
    {'h4': 'Changeover'},
    {'p': 'Changeover from old to new system may occur when: the system has been proved to the '
          'analyst\'s satisfaction and other implementation activities are complete; users and '
          'managers are satisfied with system testing, staff training and reference manuals; '
          'the operations manager is satisfied with equipment, staff and the timetable; and '
          'the target changeover date is due. Four main approaches:'},
    {'ul': [
      '**Direct changeover** — the old system is suddenly replaced by the new. A bold '
      'approach best attempted during slack periods, adopted when: the new system succeeded '
      'previously in a similar situation; there is no basis for comparison, since both '
      'systems are substantially different; or there is no extra staff to oversee parallel '
      'running.',
      '**Parallel running** — both old and new systems run together for a period, processing '
      'current data; results are checked for consistency. Disagreements may stem from errors '
      'in the new system, errors in the old system, sabotage of the new system, or wrong '
      'handling of an error-free new system. Provides a degree of safety but is expensive, '
      'duplicating effort and resources. Should be planned with: a firm time limit; details of '
      'what results are to be checked; instructions on handling errors; instructions on '
      'coping with major problems; and simulation of period-end (e.g. year-end) processing.',
      '**Pilot operation** — cheaper and easier to control than parallel running, with more '
      'safety than direct changeover. Two types: **(a) Retrospective parallel running** — the '
      'new system runs on data previously processed by the old system, so existing results '
      'are available for checking without the staffing/disruption of true parallel running; '
      '**(b) Restricted data running** — a complete logical part of the system\'s files is '
      'chosen and run as a unit on the new system; if it works well, the remaining parts are '
      'transferred, gradually transferring the whole system piecemeal.',
      '**Staged/phased changeover** — best suited to very large or complex projects; the first '
      'stage uses the parallel approach, followed by a series of discrete direct changeovers. '
      'Care must be taken to control amendments in later stages, so the overall system stays '
      'compatible. Unlike restricted data running (which implements part of the *entire* '
      'system piecemeal), staged changeover implements the *entire new system* in stages.',
    ]},
    {'h4': '(h) Post-implementation review'},
    {'p': 'An investigation reviewing an operational system\'s performance: comparing actual '
          'with planned performance; verifying the system\'s stated objectives are still valid '
          'in the present environment; evaluating achievement of those objectives; and '
          'examining the level of control in the system. The initial review checks whether the '
          'feasibility study\'s forecast objectives/benefits have been achieved; subsequent '
          '(usually annual) reviews cover continued achievement of benefits, deviations from '
          'the master specification, and opportunities for improvement.'},
  ]},

  {'n': '6.2', 't': 'Advantages and disadvantages of the SDLC', 'b': [
    {'p': '**Impact/advantages:** the SDLC has had a very positive effect on the standards of '
          'computer systems — its systematic approach substantially enhances quality and '
          'efficiency. The feasibility study establishes whether the new system is justified; '
          'proper analysis and design increase the chances of meeting users\' requirements; '
          'the cycle recognises that an implemented system should be continually monitored '
          'and updated.'},
    {'p': '**Disadvantages:** leads to very limited, restricted attitudes to systems '
          'development. Users tend to be relegated to a passive role — requirement definition '
          'is technical and relies more on the analyst\'s abilities, often leading to '
          'managers\' information needs being ignored, poorly defined user requirements, and a '
          'lack of user involvement. Most systems were also developed independently of each '
          'other. Other models (waterfall, spiral, etc.) ensure better user participation, but '
          'are outside the scope of this manual.'},
  ]},

  {'n': '6.3', 't': 'Structured methodologies', 'b': [
    {'p': 'The introduction of methodologies helped reduce many of the SDLC\'s drawbacks.'},
    {'def': {'t': 'System development methodology', 'd': 'a collection of procedures, '
                  'techniques, tools and documentation aids that help system developers '
                  'develop and implement a new system.'}},
    {'p': 'Methodologies help: involve users more closely in development; analyse user needs '
          'more fundamentally; allow flexibility of systems; and produce easily understood '
          'documentation.'},
    {'h3': '6.3.1 Advantages and disadvantages of system methodologies'},
    {'p': '**Advantages:** detailed documentation is produced; standardised methods make '
          'application easier and cheaper; leads to improved system specifications; systems '
          'developed this way are easier to maintain and improve; users are involved from an '
          'early stage and required to sign off each stage; diagrams make the system easier to '
          'understand than a merely descriptive account; and a logical design is produced, '
          'independent of hardware and software.'},
    {'p': '**Disadvantages:** may be inappropriate for strategic information collected on an '
          'ad-hoc basis; some methodologies are too concerned with system design and not with '
          'their impact on actual work processes or social context; and it may encourage '
          'excessive documentation and bureaucracy, being just as suitable for documenting bad '
          'design as good.'},
    {'h3': '6.3.2 Structured Systems Analysis and Design Methodology (SSADM)'},
    {'p': 'A very popular structured methodology, with the following features: it describes '
          'how a system is to be developed; it reduces development into **phases**, each '
          'reduced into **stages** (sub-phases), each containing **steps** with tasks, inputs '
          'and outputs; and it is self-checking and can be tailored to a number of '
          'applications.'},
    {'h4': 'Stages of SSADM'},
    {'p': '**Phase 1 — Feasibility study** (not mandatory in many SSADM projects) examines '
          'the "case" for the project in terms of technical feasibility and cost-benefit: '
          '**FS1** — basic requirements and terms of reference are set out, and initial '
          'investigations carried out; **FS2** — a number of ways of satisfying the '
          'requirements are identified and costed.'},
    {'p': '**Phase 2 — System analysis** (Stages 1–3): **Stage 1** — the current situation is '
          'investigated by the analyst, who documents current processes, data flows and any '
          'problems encountered or anticipated. **Stage 2** — user needs are identified and '
          'laid down in detail; where needs conflict or compete for resources, priorities are '
          'established. **Stage 3** — hardware and software options are specified; the '
          'analyst recommends the best option, agreed by management.'},
    {'p': '**Phase 3 — System design** (Stages 4–6): **Stage 4** — a relational data analysis '
          'is carried out, normalising the data if required (normalisation is beyond this '
          'manual\'s scope). **Stage 5** — the processes required to produce relevant output '
          'are specified and cross-checked with the Stage 4 data design. **Stage 6** — the '
          'logical data and process designs are combined into a definition of how the system '
          'will be written and implemented.'},
  ]},

  {'n': '6.4', 't': 'Prototyping', 'b': [
    {'p': 'During development, developers must not simply "dump" on users what they think is '
          'appropriate — end-user input must be solicited. Prototyping affords users this '
          'vital role.'},
    {'def': {'t': 'Prototyping', 'd': 'a fourth-generation language (4GL) development tool '
                  'used to let users quickly produce a simulation of the output required from '
                  'a completed system. The prototype is a smaller version of the system or '
                  'program, with the appearance of the final working system, which may be '
                  'tested and experimented on by users on the way to reaching what they want. '
                  'Users can better clarify their requirements, refined through the '
                  'prototype\'s evolution; the prototype may become part of the system '
                  'specification.'}},
    {'h3': 'Stages of prototyping'},
    {'p': 'Based on the known form of the final product, a prototype is created, subjected to '
          'review, testing and amendment. As long as users indicate the current version is not '
          'exactly what is required, amendment/testing continues for user approval — an '
          'iterative process ensuring user needs are exactly catered for, avoiding handing '
          'over a failed system, and ensuring user ownership. Stages: **Create prototype → '
          'Test prototype → (if not OK) Amend prototype → (repeat) → Accept prototype → Create '
          'real system.**'},
    {'note': 'The prototype is a live working application that can perform actual work; it may '
             'become the actual application, or be replaced by another, and is used to test '
             'assumptions about users\' requirements and system design.'},
    {'h3': 'Advantages and disadvantages of prototyping'},
    {'p': '**Advantages:** the user can judge the prototype before things go too far to '
          'change; it makes custom-built application software more economical for users; and '
          'a prototype need not be written in the language of what it prototypes.'},
    {'p': '**Disadvantages:** many prototyping tools assume the user is computerising an '
          'application for the first time, which may not be true; programs produced may be '
          'tied to a particular hardware platform or database system; prototyping tools may '
          'be inefficient in the programs they produce; and not all prototyping tools let '
          'programmers insert hand-written code when necessary.'},
  ]},

  {'n': '6.5', 't': 'Joint Applications Development (JAD)', 'b': [
    {'p': 'Just as prototyping lets end-users ensure their exact requirements are met, JAD '
          'brings users and the systems team together to collaborate during development, also '
          'ensuring the required system is produced.'},
    {'def': {'t': 'Joint Applications Development (JAD)', 'd': 'describes the partnership '
                  'between users and systems developers during the process of developing a '
                  'system.'}},
    {'p': '**Potential benefits of JAD:** creates a pool of expertise from all relevant '
          'functions; reduces the risk of systems being imposed on users; increases user '
          'ownership and responsibility for the systems solution; and emphasises users\' '
          'information needs and their relationship to business needs and decision-making. '
          'This shift towards end-user application development needs good management and '
          'control, well done via an information centre with a help desk.'},
  ]},

  {'n': '6.6', 't': 'Rapid Applications Development (RAD)', 'b': [
    {'p': 'Certain situations need a system developed very quickly, since end-users and the '
          'organisation cannot afford to wait unduly for completion. RAD is one novel approach '
          'for such situations.'},
    {'def': {'t': 'Rapid Applications Development (RAD)', 'd': 'a quick way of developing '
                  'software, combining a managed approach to systems development with the use '
                  'of modern software tools such as prototyping and modelling, involving '
                  'end-users heavily. The RAD team should be highly motivated, with at least '
                  'one person very skilled in advanced tools, to ensure such tools are used '
                  'effectively.'}},
    {'h3': 'When is RAD appropriate?'},
    {'ul': [
      'If users are not clear about their requirements, RAD can quickly help them find out.',
      'If there is a culture of user involvement in systems development, the RAD team can '
      'work productively.',
      'Where there is a need for faster delivery than conventional development can provide.',
      'Where the target system is limited in scope.',
      'Where the target system is not expected to be implemented on a new platform.',
    ]},
  ]},

  {'n': '6.7', 't': 'Outsourcing', 'b': [
    {'p': 'Owing to ever-increasing competition, management often seeks means to carry out '
          'functions more efficiently. Outsourcing offloads certain non-key functions to '
          'external expert firms, for a fee.'},
    {'def': {'t': 'Outsourcing', 'd': 'purchasing from outside the organization the services '
                  'required to perform certain business functions, covering facilities '
                  'management, types of services and a range of contracts with intangible '
                  'benefits — the ultimate expression of treating a supplier as an extension '
                  'of in-house resources. Facilities previously provided in-house are instead '
                  'performed by external contractors working closely with the buying '
                  'organisation, including computer centre operations, network operations, '
                  'applications management and systems integration. Often closely related to '
                  'downsizing/divesting, to concentrate on key business competencies — driven '
                  'by lower costs, reduced dilution of management attention, or covering '
                  'temporary skill gaps.'}},
    {'warn': 'A company should not outsource any of its key operational functions — it risks '
             'losing competitive advantage if the outsourcing vendor also serves a competitor.'},
    {'h3': 'Types of outsourcing'},
    {'ul': [
      '**Body shop outsourcing** — management uses outsourcing to meet short-term IS/IT '
      'demand, e.g. getting outside programming assistance when expertise is temporarily '
      'unavailable in-house.',
      '**Project management outsourcing** — used for all or part of a particular IS project, '
      'e.g. developing a new system.',
      '**Total outsourcing** — an organisation outsources more than **70%** of its IS '
      'capability to a single outsourcing vendor.',
    ]},
    {'h3': 'Ensuring the success of outsourcing'},
    {'p': 'Gary J. Zenz\'s steps for managers to ensure outsourcing succeeds:'},
    {'ul': [
      'Establish a strategy for the proper balancing of management, contracting and '
      'consulting.',
      'Establish a strategy to deal with possible staff reductions.',
      'Closely integrate the external suppliers.',
      'Provide appropriate communication channels.',
    ]},
  ]},

  {'n': '6.8', 't': 'Computer security, viruses, worms and cybercrime', 'b': [
    {'p': 'An **information technology crime** may be an illegal act carried out on computers '
          'or telecommunications, or the use of computers/telecommunications to accomplish an '
          'illegal act. A computer system is **secured** against a threat if countermeasures '
          'reduce, to an acceptably low level, the loss the threat may cause over a given '
          'period.'},
    {'p': 'Three types of loss an organisation does not want its system to suffer: '
          '**(i) loss of availability** (the system is not available for use); **(ii) loss of '
          'integrity (accuracy)** (e.g. brought about by a virus attack); **(iii) loss of '
          'confidentiality** (the system is easily accessed by unauthorised people).'},
    {'p': 'A **threat** is any event whose occurrence adversely affects one or more of the '
          'assets/resources (hardware, software, network, media, data, etc.) making up the '
          'system. Threats group into **(a) physical threats** (fire, water, weather, physical '
          'environment) and **(b) human threats** (damage, theft, strike actions, etc.). Crimes '
          'include hardware/software theft, stealing computer time, and stealing information '
          'or money.'},
    {'h3': 'Theft'},
    {'p': '**(a) Theft of hardware** — usually associated with smaller PCs, rampant at '
          'airports, hotels and campuses; with desktops, thieves often steal the system unit '
          'and leave peripherals. Devices must be documented in asset registers and labelled '
          'with site/identification codes to discourage removal.'},
    {'p': '**(b) Theft of software** — may be discouraged by requiring a valid key/code '
          '(including the processor\'s serial number) before a program will run, so the same '
          'program cannot run on a different computer, making piracy not worthwhile.'},
    {'h3': 'Computer viruses and worms'},
    {'def': {'t': 'Computer virus', 'd': 'infectious or malicious coding — any software '
                  'designed to damage or compromise computer systems. The coding is parasitic: '
                  'once it finds a host (e.g. a PC), it is released and replicates itself very '
                  'quickly, possibly infecting memory and backing storage media.'}},
    {'p': 'The commonest spread is via e-mail attachments; viruses can also travel by '
          'diskettes, flash disks, networks, CDs, and software downloaded from the internet — '
          'even from online chatting, visiting a website, or playing computer games. Many '
          'exploit vulnerabilities and sneak in through unprotected "back doors" in commercial '
          'software. Reports indicate more than **57,000** individual viruses exist; some are '
          'merely mischievous, others infiltrate sophisticated systems.'},
    {'h4': 'Examples of viruses'},
    {'ul': [
      '**The Jerusalem Virus** — slows the computer until virtually unusable, and deletes '
      'files.',
      '**Cascade** — causes screen characters to fall to the bottom, and may reformat the hard '
      'disc, deleting everything on it.',
      '**Casino** — displays a one-armed-bandit game; if the user fails to win the jackpot, '
      'the hard disc is wiped clean.',
      '**Love Bug** — attacks the operating system.',
      '**Boot Sector Virus** — replaces boot instructions with its own; once switched on, it '
      'loads into main memory before the OS, from where it infects files.',
      '**Time Bomb** — programmed to execute at a specific date/time.',
      '**Logic Bomb** — triggered into action by the occurrence of an event.',
      '**Trojan Horse** — a type of virus: code hidden within an authorised program to carry '
      'out illegal processing.',
    ]},
    {'def': {'t': 'Worm', 'd': 'a high-tech malicious program that copies itself repeatedly '
                  'into memory or a selected medium until no more space is left. After making '
                  'copies of itself, a worm usually releases a "**pay load**" — an action '
                  'designed to disrupt the system, e.g. the **Magistrate** worm hides in the '
                  'hard disc, moves around the main address book, and mails itself to '
                  'electronic contacts. It usually does not live long, but is quite '
                  'destructive while alive. A worm is like a virus except it is a program '
                  'rather than a code segment hidden in a host program.'}},
    {'p': 'Examples of worms: **Blaster**, **Slammer**.'},
    {'h4': 'Detection, prevention and avoidance of viruses/worms'},
    {'p': 'Detected by effective anti-virus software: **Norton Anti-Virus, Dr Solomon\'s, AVG '
          'Anti-virus, Kaspersky Anti-virus Personal, PC-Cillin, Bitdefender, McAfee Virus '
          'Scan, Panda**. The software scans main memory and media to detect and, if possible, '
          'destroy viruses; a particular antivirus may be ineffective against a given virus/'
          'worm, needing a more powerful type.'},
    {'p': '**To avoid viruses and worms:** use the right anti-virus software and back up '
          'regularly; update anti-virus software regularly (via the internet); guard your '
          'e-mail inbox, especially attachments; download only from well-known, reputable '
          'sources; contact your ISP about virus scanning; and establish rules on media '
          'usable on the network/PC.'},
    {'h3': 'Cybercrimes'},
    {'p': 'Some criminals are more interested in abusing/vandalising systems than profiting '
          'from them. Basic devices: **warez trading** (exchanging or selling pirated '
          'software); **super zapping** (bypassing all security via specialised software '
          'tools); **data leakage** (removing copies of confidential information without '
          'trace); **carding** (obtaining, using or selling others\' credit card numbers).'},
    {'p': 'Further computer crimes and abuse techniques:'},
    {'ul': [
      '**Cracking** — unauthorised access to and use of computer systems, usually via a PC '
      'and telecommunications network; crackers are hackers with malicious intent.',
      '**Data diddling** — changing data before, during or after entry, to delete, alter or '
      'add key system data.',
      '**Data leakage** — unauthorised copying of company data, such as computer files.',
      '**Denial of service attack** — the attacker sends e-mail bombs (hundreds of messages '
      'per second) from randomly generated false addresses, overloading and shutting down the '
      'ISP\'s mail server.',
      '**Eavesdropping** — listening to private voice or data transmission, often via a '
      'wiretap.',
      '**E-mail forgery** — sending an e-mail that looks as if sent by someone else.',
      '**E-mail threats** — a threatening message trying to get the recipient to do something '
      'that enables fraud.',
      '**Hacking** — unauthorised access and use of computer systems, usually via a PC and a '
      'telecommunications network; hackers do not intend damage, only access for its own sake.',
      '**Internet misinformation** — using the internet to spread false or misleading '
      'information about companies.',
      '**Internet terrorism** — using the internet to disrupt electronic commerce and destroy '
      'company/individual communications.',
      '**Logic time bomb** — a program that lies idle until a special circumstance or '
      'particular time triggers it, then sabotages the system by destroying programs/data.',
      '**Masquerading/impersonation** — a perpetrator gains access by pretending to be an '
      'authorised user, enjoying the same privileges.',
      '**Password cracking** — an intruder penetrates a system\'s defences, steals the '
      'password file, decrypts it, and uses it to access system resources.',
      '**Piggybacking** — tapping a telecommunication line and latching onto a legitimate '
      'user before they log in, so the legitimate user unknowingly carries the perpetrator in.',
      '**Round-down** — computer rounds down interest calculations to two decimal places; the '
      'remaining fraction of a cent is placed in an account controlled by the perpetrator.',
      '**Salami technique** — tiny slices of money are stolen over time (e.g. expenses '
      'increased by a fraction of a percent, the increments placed in a dummy account and '
      'later pocketed).',
      '**Scavenging** — gaining access to confidential information by searching corporate '
      'records — from trashcans for printouts/carbon copies, to scanning computer memory.',
      '**Social engineering** — tricking an employee into giving out the information needed to '
      'get into a system.',
      '**Software piracy** — copying computer software without the publisher\'s permission.',
      '**Spamming** — e-mailing the same message to everyone on one or more UseNet newsgroup '
      'or LISTSERV lists.',
      '**Super zapping** — unauthorised use of special system programs to bypass regular '
      'system controls and perform illegal acts.',
      '**Trap door** — the perpetrator enters via a backdoor that bypasses normal system '
      'controls to perpetrate fraud.',
      '**Trojan horse** — unauthorised computer instructions hidden in an authorised, properly '
      'functioning program.',
      '**Virus** — as described above.',
      '**War dialling** — programming a computer to search for an idle modem by dialling '
      'thousands of phone lines; the perpetrator enters via the idle modem, captures the PC '
      'attached to it, and gains access to its network.',
    ]},
    {'h3': 'Computer privacy and security'},
    {'p': '**Information privacy** includes individuals\' rights to know that their recorded '
          'personal information is accurate, pertinent, complete, up-to-date and reasonably '
          'secured from unauthorised access, and the right to influence the kind, quantity and '
          'quality of readily identifiable personal information held in a system — whether or '
          'not the information is publicly viewable or legally required to be confidential, '
          'these privacy guidelines should be observed by all operators and users.'},
    {'p': '**Data security** is neither a social nor a legal issue but a procedural matter — '
          'the way organizations protect information from unauthorized or accidental '
          'modification, destruction and disclosure. There is no such thing as perfect '
          'security; most organizations aim for a level of protection appropriate to their '
          'needs. The objective of a data security programme is to cut the risk and '
          'probability of loss to the lowest affordable level, and to be able to implement a '
          'full recovery programme if a loss occurs. The first step is management awareness of '
          'the importance of information management and its consequences, followed by a plan '
          'that is developed and put into action.'},
    {'h4': 'Security concerns'},
    {'p': 'Four areas of concern: **identification and access; encryption; protection of '
          'software and data; disaster recovery planning**.'},
    {'p': '**(a) Identification and access** — systems authenticate identity by determining '
          '(i) what the user **has** (card, key, signature, badge); (ii) what the user '
          '**knows** (PIN, password, digital signature); (iii) **who** the user is (biometrics). '
          'A **digital signature** is a string of characters and numbers a user "signs" to an '
          'electronic document sent by their computer; the receiving computer performs '
          'mathematical operations on it to verify validity.'},
    {'p': '**(b) Encryption** — the technique of disguising information to preserve '
          'confidentiality during transmission and storage. Encryption/decryption comprise an '
          '**algorithm** and a **key**; the algorithm transforms data into cipher, and the key '
          'controls the algorithm — changing the key value gives a completely different '
          'conversion.'},
    {'p': '**(c) Protection of software and data** — measures include educating staff on '
          'back-up procedures and virus protection, plus: **(i) control of access** (physical '
          'and logical); **(ii) audit controls** (track programs/servers used, files opened, '
          'creating audit trails); **(iii) staff controls** (screening job applicants, '
          'segregation of duty, manual/automated controls, destruction of printouts, printer '
          'ribbons and other waste that might yield passwords or trade secrets).'},
    {'p': '**(d) Disaster recovery plans** — methods to restore information-processing '
          'operations halted by destruction or accident, including alternative locations: a '
          '**Hot site** (a fully equipped computer centre able to resume functions quickly, '
          'not necessarily owned by the company needing it) and a **Cold site** (a building or '
          'other suitable environment where a company installs its own systems, when a mishap '
          'renders continued operations impossible).'},
  ]},

  {'n': '6.9', 't': "Nigeria's Cybersecurity Act and Data Protection Regulations", 'b': [
    {'p': 'Nigeria has established key cybersecurity and data protection regulations to '
          'safeguard digital assets, personal data and national security.'},
    {'h3': 'The Nigerian Cybersecurity Act'},
    {'def': {'t': 'Cybercrimes (Prohibition, Prevention, etc.) Act', 'd': 'first enacted in '
                  '**2015** and amended in **2024**; Nigeria\'s primary cybersecurity law, '
                  'addressing cybercrime, data security and digital fraud.'}},
    {'p': '**Key provisions:** cybercrime offences (hacking, identity theft, cyberstalking, '
          'financial fraud); data protection measures (secure handling of sensitive '
          'information, especially in financial/government sectors); penalties and '
          'enforcement (fines and imprisonment, varying with the severity of the crime); '
          'international compliance (alignment with global cybersecurity standards).'},
    {'h3': 'Data Protection Regulations in Nigeria'},
    {'def': {'t': 'Nigeria Data Protection Act (NDPA) 2023', 'd': 'signed into law to regulate '
                  'personal data processing and privacy rights.'}},
    {'p': '**Key features:** personal data protection (defines personal and sensitive data, '
          'ensures lawful processing); data subject rights (access, correction, deletion); '
          'regulatory oversight (establishes the **Nigeria Data Protection Commission '
          '(NDPC)** to enforce compliance); sector-specific regulations (financial '
          'institutions, healthcare, telecommunications).'},
    {'h3': 'Cybercrime laws — key provisions'},
    {'ol': [
      '**Cybercrime offences** — hacking, identity theft, financial fraud; cyberstalking and '
      'online harassment; cyberterrorism and unauthorized access to critical systems.',
      '**Data protection and privacy** — safeguards personal/sensitive data; regulates '
      'electronic communications and online transactions.',
      '**Penalties and enforcement** — offenders face fines/imprisonment based on severity; '
      'law enforcement agencies are empowered to investigate and prosecute.',
      '**Regulation of digital transactions** — ensures secure online banking/e-commerce, and '
      'mandates cybersecurity-standard compliance for businesses.',
    ]},
    {'note': 'The 2024 amendment, particularly Section 24, has been criticised for its vague '
             'definitions of cyberstalking/online offences, with advocacy groups arguing the '
             'law has been used to suppress free speech and target journalists and activists.'},
    {'h3': "Ensuring compliance with Nigeria's cybercrime and data protection laws"},
    {'p': '**For businesses:** (1) implement robust cybersecurity measures — firewalls, '
          'encryption, multi-factor authentication, regular software/protocol updates; '
          '(2) comply with data protection laws — follow the NDPA 2023, obtain consent before '
          'collecting user information, and be transparent about its use; (3) conduct '
          'employee cybersecurity training — phishing, password security, secure e-mail use, '
          'access control policies; (4) secure financial transactions — trusted payment '
          'gateways, monitoring for fraud, prompt reporting; (5) develop incident response '
          'plans — a strategy for detecting/responding to attacks, and regular audits.'},
    {'p': '**For individuals:** (1) protect personal data — avoid sharing sensitive '
          'information on unsecured platforms, enable privacy settings; (2) be cautious of '
          'cyber fraud — verify transactions, recognise phishing/fraudulent websites; '
          '(3) use strong passwords and authentication, changed regularly; (4) stay informed '
          'on cyber laws, including Section 24 of the Cybercrime Act; (5) report cybercrime '
          'to the Nigeria Cybercrime Agency or appropriate law enforcement.'},
  ]},

  {'n': '6.10', 't': 'Workplace security and health issues', 'b': [
    {'h3': 'Workplace security'},
    {'p': 'Since an average employee spends more than one-third of the day at work, workplace '
          'security is paramount. Most workplace hazards are preventable. It is a legal '
          'obligation on employers to provide a healthy and safe workplace, under the '
          '**Factories Act (Cap F1 LFN 2004)** and the **National Policy on Occupational '
          'Safety and Health**, which mandate all employers to:'},
    {'ol': [
      'Promote a safe and healthy workplace for employees and protect them from injury and '
      'illness;',
      'Make provision for protecting others against risks connected with employees\' '
      'activities;',
      'Provide preventive mechanisms in respect of injury or accidents in the workplace;',
      'Ensure the provision of occupational safety and health services to all workers;',
      'Develop consultations between employers and employees on safety, health and welfare;',
      'Develop and promote public awareness and enlightenment on measures to prevent '
      'accidents and injuries;',
      'Provide a legal basis for national policy on occupational safety and health;',
      'Provide a regulatory framework for compliance with safety and health standards by '
      'employers, agents and employees.',
    ]},
    {'h3': 'Health issues'},
    {'p': 'The use of computers and communications technology can adversely affect health. '
          'Major health issues:'},
    {'ul': [
      '**Repetitive strain injuries (RSIs)** — wrist, hand, arm and neck injuries from fast, '
      'repetitive muscle motions, often affecting journalists, data-entry staff, postal '
      'workers, pianists, etc. RSIs cover disorders from easily curable to very damaging, '
      'including **carpal tunnel syndrome (CTS)** — a debilitating condition from pressure on '
      'the median nerve in the wrist, damaging nerves/tendons and causing pain, sometimes '
      'requiring surgery.',
      '**Eyestrain and headaches** — computer users are often forced to read the screen at '
      'very short distances, affecting eyesight. **Computer Vision Syndrome (CVS)** presents '
      'with eyestrain, headaches, double vision and other problems from improper monitor use; '
      'reduced by keeping the screen at a good distance, using good screen resolution, and '
      'installing screen shields.',
      '**Back and neck pains** — result from improper furniture or keyboard/screen '
      'positioning; users must adapt to the right furniture/equipment and sit straight-up to '
      'minimise this.',
    ]},
  ]},

  {'n': '6.11', 't': 'Computer forensics', 'b': [
    {'def': {'t': 'Computer forensics (digital forensics)', 'd': 'a branch of forensic science '
                  'pertaining to legal evidence found on computers and digital storage media.'}},
    {'p': 'Reasons for computer forensics: analysing systems belonging to defendants (criminal '
          'cases) or litigants (civil cases); recovering data after hardware/software failure; '
          'analysing a computer after a break-in (how attackers gained access, what they did); '
          'gathering evidence against an employee an organisation wishes to terminate; and '
          'gaining information on how computer systems work, for debugging or performance '
          'optimisation.'},
    {'h3': 'Forensics processes/techniques'},
    {'p': 'Five basic steps: **(a) preparation of investigation data; (b) collection of the '
          'data; (c) examination of data; (d) analysis of data; (e) reporting.** The '
          'investigator must be properly trained for the specific investigation, and report-'
          'generating tools must be validated.'},
    {'p': 'Digital evidence can be collected from computers, cell phones, digital cameras, '
          'hard drives, CD-ROMs, USB memory devices, etc. It must be handled with care, since '
          'digital information is easily changed, and once changed it is usually impossible to '
          'detect the change without other measures. Most valuable forensic information often '
          'comes from an interview with the computer user.'},
  ]},

  {'n': '6.12', 't': 'Big Data', 'b': [
    {'def': {'t': 'Big Data', 'd': 'extremely large data sets that may be analysed '
                  'computationally to reveal patterns, trends and associations, especially '
                  'relating to human behaviour and interactions — also defined as data '
                  'containing greater variety, arriving in increasing volumes and with more '
                  'velocity (the "three Vs" definition). Put simply, larger, more complex data '
                  'sets, especially from new data sources.'}},
    {'p': 'Classified into three types: **structured data** (regular formats, following '
          'particular trends and patterns); **unstructured data** (no identifiable patterns); '
          '**semi-structured data** (part follows regular patterns, part does not). Big data '
          'is a combination of these, mined for information and used in machine learning, '
          'predictive modelling and other advanced analytics.'},
    {'p': 'Big data is often characterised by **the three Vs**: **volume** (the large amount '
          'of data from many environments); **variety** (the wide variety of data types); and '
          '**velocity** (the speed at which data is generated, collected and processed). These '
          'may be extended to **six Vs** by adding: **value** (the worth of the information to '
          'the company, determined by its relevance); **veracity** (the accuracy of the data, '
          'determining reliability); **variability** (the rate of change in the data\'s '
          'structure). Big data deployments often involve terabytes, petabytes and even '
          'exabytes of data, created and collected over time.'},
    {'h3': 'Benefits of Big Data'},
    {'p': 'Companies use big data to: improve operations; provide better customer service by '
          'tracking customer behaviour more closely and accurately; create personalised '
          'marketing campaigns from more comprehensive knowledge of customer behaviour; take '
          'actions that ultimately increase revenue and profits; and gain competitive '
          'advantage by taking faster, more informed business decisions.'},
    {'h3': 'Applications of Big Data in organizations'},
    {'ul': [
      'Medical research — disease diagnosis and identification of risk factors.',
      'Tracking threats and disease outbreaks (e.g. the coronavirus pandemic).',
      'Energy industry — identifying drilling locations and monitoring pipeline operations.',
      'Electricity generation, transmission and distribution — tracking electrical grids.',
      'Financial services — risk management and real-time market data analysis.',
      'Manufacturing and transportation — managing supply chains and optimising delivery '
      'routes.',
      'Government — emergency response, crime prevention and smart-city initiatives.',
    ]},
    {'h3': 'Big Data analytics'},
    {'p': 'To get valid, relevant results, data scientists must understand the available data '
          'and the expectations of it — making data preparation a crucial first step: '
          '**profiling, cleansing, validation and transformation** of data sets. Once prepared, '
          'various data science and advanced analytics disciplines run different applications: '
          '**machine learning and deep learning, predictive modelling, data mining, '
          'statistical analysis, streaming analytics, text mining.**'},
    {'h3': 'Data visualisation'},
    {'def': {'t': 'Data visualisation', 'd': 'representing information using graphical '
                  'elements — charts, graphs, maps and infographics — to make complex data '
                  'easier to understand, analyse and communicate.'}},
    {'p': '**Importance:** enhances understanding (turns raw data into meaningful insights); '
          'identifies trends (patterns, correlations, outliers); improves decision-making '
          '(clear visuals for better choices); engages the audience (more appealing, digestible '
          'information).'},
    {'p': '**Common data visualisation types:** **(1) bar charts** (compare categories/values); '
          '**(2) line graphs** (show trends over time); **(3) pie charts** (illustrate '
          'proportions of a whole); **(4) heatmaps** (represent data intensity with colours); '
          '**(5) scatter plots** (display relationships between variables).'},
    {'h3': 'Big Data management technologies and deployment tools'},
    {'p': '**Hadoop**, an open-source distributed processing framework, used to be the centre '
          'of many big-data architectures; big-data platforms now combine many technologies '
          'in a single package, primarily for the cloud, including: **Amazon EMR** (formerly '
          'Elastic MapReduce), **Cloudera Data Platform, Google Cloud Dataproc, HPE Ezmeral '
          'Data Fabric** (formerly MapR Data Platform), **Microsoft Azure HDInsight**.'},
    {'p': 'For organizations deploying big-data systems themselves, technology categories '
          'available (besides Hadoop and Spark) include: **storage repositories** — Hadoop '
          'Distributed File System (HDFS), Amazon S3, Google Cloud Storage, Azure Blob '
          'Storage; **cluster management frameworks** — Kubernetes, Mesos, YARN (Yet Another '
          'Resource Negotiator, Hadoop\'s built-in resource manager/job scheduler); **stream '
          'processing engines** — Flink, Hudi, Kafka, Samza, Storm, Spark Streaming and '
          'Structured Streaming; **NoSQL databases** — Cassandra, Couchbase, CouchDB, HBase, '
          'MarkLogic Data Hub, MongoDB, Neo4j, Redis, etc.; **data lake/warehouse platforms** '
          '— Amazon Redshift, Delta Lake, Google BigQuery, Kylin, Snowflake; **SQL query '
          'engines** — Drill, Hive, Impala, Presto, Trino.'},
    {'h3': 'Challenges to implementing Big Data'},
    {'ul': [
      'Big Data analytics require high computer capacity.',
      'Big data must be tailored to the organization\'s specific needs.',
      'IT and data management teams must assemble a customised set of technologies and tools.',
      'It requires new skills to be acquired by database management teams.',
    ]},
    {'p': 'These challenges may be addressed by a **managed cloud service**, though this '
          'involves high cost and the managed process of migrating in-house data and work into '
          'the cloud. Other challenges include making data accessible to analysts in '
          'distributed, mixed-platform environments (addressed via **data catalogues** with '
          'metadata management and data lineage), and the complexity of integrating big-data '
          'sets, especially where variety and velocity prevail.'},
    {'h3': 'Strategy for effective Big Data implementation'},
    {'p': 'Developing a Big Data strategy requires understanding business goals and available '
          'data, plus assessing the need for additional data. Next steps: prioritising planned '
          'use cases/applications; identifying new systems/tools needed; creating a deployment '
          'roadmap; evaluating internal skills for retraining/hiring needs.'},
    {'p': 'To keep Big Data sets clean, consistent and properly used: put in place a **data '
          'governance programme**; **data quality management processes**; ensure management '
          'and analysis of Big Data focuses on business needs for information over available '
          'technologies; and use **data visualisation** to aid discovery and analysis.'},
  ]},

  {'n': '6.13', 't': 'Disruptive technology, artificial intelligence and machine learning', 'b': [
    {'def': {'t': 'Disruptive technology', 'd': 'an innovation that significantly alters the '
                  'way consumers, industries or businesses operate, sweeping away the systems '
                  'or habits it replaces because its attributes are recognisably superior. '
                  'Recent examples: e-commerce, online news sites, ride-sharing apps, GPS '
                  'systems; historically, the automobile, electricity service and television '
                  'were disruptive. Disruptive technologies are especially pervasive in the '
                  'post-pandemic "new normal".'}},
    {'p': 'This chapter\'s discussion is limited to: **artificial intelligence and machine '
          'learning; Internet of Things; distributed ledgers/blockchain technology; computer '
          'robotics and business automation; and drone technology.**'},
    {'h3': 'Artificial Intelligence (AI)'},
    {'def': {'t': 'Artificial Intelligence (AI)', 'd': 'systems or machines that mimic human '
                  'intelligence to perform tasks, and can iteratively improve themselves based '
                  'on the information they collect. A wide-ranging branch of computer science '
                  'concerned with building smart machines capable of performing tasks that '
                  'typically require human intelligence — intelligence demonstrated by '
                  'machines, as opposed to the natural intelligence of animals including '
                  'humans. AI also draws upon computer science, psychology, linguistics and '
                  'philosophy, founded on the assumption that human intelligence "can be so '
                  'precisely described that a machine can be made to simulate it".'}},
    {'p': 'AI is not intended to replace humans, but to significantly enhance human '
          'capabilities and contributions. Forms of AI: **chatbots** (understand customer '
          'problems faster, provide efficient answers); **intelligent assistants** (parse '
          'critical information from large free-text data sets, to improve scheduling); '
          '**recommendation engines** (automated recommendations, e.g. for TV shows, based on '
          'viewing habits).'},
    {'p': 'Other applications: using transactional/demographic data to predict customer '
          'lifetime value; optimising pricing based on customer behaviour/preferences; using '
          'image recognition to analyse X-rays for signs of cancer. According to the Harvard '
          'Business Review, enterprises primarily use AI to: detect and deter security '
          'intrusions; resolve users\' technology issues; improve production management work; '
          'and evaluate internal compliance in using approved vendors.'},
    {'h4': 'Drivers of AI adoption'},
    {'ol': [
      'Affordable, high-performance computing capability is readily available — cloud '
      'computing power makes AI computing affordable, unlike the earlier, cost-prohibitive '
      'non-cloud environments.',
      'Large volumes of data are available for training — tools for labelling data, and easier '
      'storage/processing of structured and unstructured data, enable more organizations to '
      'build and train AI algorithms.',
      'Applied AI delivers a competitive advantage — enterprises increasingly recognise the '
      'advantage of applying AI insights to business objectives, leading to lower costs, '
      'reduced risks and faster time to market.',
    ]},
    {'h4': 'Benefits and challenges of operationalizing AI'},
    {'p': '**Success stories:** the Associated Press produced 12 times more stories by '
          'training AI to write short earnings news stories automatically, freeing journalists '
          'for in-depth pieces (Harvard Business Review). **Deep Patient**, an AI tool built by '
          'the Icahn School of Medicine at Mount Sinai, analyses a patient\'s medical history '
          'to predict almost 80 diseases up to a year before onset, helping doctors identify '
          'high-risk patients before diagnosis.'},
    {'p': '**Ready-to-use AI** — solutions/tools/software with built-in AI capabilities, or '
          'that automate algorithmic decision-making, from autonomous self-healing databases '
          'to prebuilt models for image recognition/text analysis — helps companies achieve '
          'faster time to value, increased productivity, reduced costs, and improved customer '
          'relationships.'},
    {'p': '**Challenges to deployment:** AI projects are often computationally expensive '
          'without cloud computing; they are complex to build, needing expertise in high '
          'demand and short supply; knowing when/where to use AI (or a third party) helps '
          'minimise these difficulties.'},
    {'p': '**Impediments to realising AI\'s full potential:** inefficient workflows; data '
          'scientists struggling for resources/data, or to collaborate, while managing many '
          'open-source tools (and developers sometimes having to recode their models); IT '
          'spending increasing time supporting data-science teams amid limited '
          'standardisation; and senior executives failing to visualise AI\'s full potential, '
          'so under-supporting the collaborative ecosystem AI needs.'},
    {'p': '**Creating the right AI culture:** business analysts work with data scientists to '
          'define problems/objectives; data engineers manage the data and platform; data '
          'scientists prepare/explore/visualize/model data; IT architects manage the '
          'underlying infrastructure (on-premises or cloud); application developers deploy '
          'models into data-driven products.'},
    {'h3': 'Adaptive intelligence'},
    {'def': {'t': 'Adaptive intelligence', 'd': 'an evolving term from Artificial Intelligence '
                  '— applications that help enterprises make better business decisions by '
                  'combining real-time internal and external data with decision science and '
                  'highly scalable computing infrastructure, essentially making the business '
                  'smarter and empowering it to provide better products, recommendations and '
                  'services.'}},
    {'h3': 'Machine learning'},
    {'def': {'t': 'Machine learning', 'd': 'a data analytics technique that teaches computers '
                  'to do what comes naturally to humans and animals: learn from experience. '
                  'Machine learning algorithms use computational methods to "learn" '
                  'information directly from data, without a predetermined equation as a '
                  'model, adaptively improving performance as more samples become available. '
                  '**Deep learning** is a specialized form of machine learning.'}},
    {'p': 'With the rise of big data, machine learning has become key to solving problems in: '
          '**computational finance** (credit scoring, algorithmic trading); **image '
          'processing/computer vision** (face recognition, motion/object detection); '
          '**computational biology** (tumour detection, drug discovery, DNA sequencing); '
          '**energy production** (price/load forecasting); **automotive, aerospace and '
          'manufacturing** (predictive maintenance); **natural language processing** (voice '
          'recognition).'},
    {'p': 'Machine learning is deployed when an organization faces a complex task with a large '
          'amount of data and variables, but no existing formula or equation.'},
    {'p': 'Two techniques: **supervised learning** — trains a model on known input and output '
          'data, so it can predict future outputs; **unsupervised learning** — finds hidden '
          'patterns or intrinsic structures in input data.'},
    {'p': 'Algorithm choice depends on the size/type of data, the desired insights, and how '
          'they will be used: **supervised learning** is chosen to train a model to predict, '
          'e.g., a continuous variable\'s future value (temperature, stock price), or a '
          'classification (e.g. identifying car makes from video footage); **unsupervised '
          'learning** is chosen to explore data and find a good internal representation, such '
          'as splitting data into clusters.'},
  ]},

  {'n': '6.14', 't': 'Internet of Things (IoT)', 'b': [
    {'def': {'t': 'Internet of Things (IoT)', 'd': 'physical objects (or groups of objects) '
                  'with sensors, processing ability, software and other technologies, that '
                  'connect and exchange data with other devices and systems over the Internet '
                  'or other communications networks.'}},
    {'p': '**Enablers of IoT:** the convergence of multiple technologies — ubiquitous '
          'computing, commodity sensors, increasingly powerful embedded systems, machine '
          'learning, wireless sensor networks, control systems, and automation (including '
          'home/building automation) — independently and collectively enable it.'},
    {'h3': 'Applications of IoT'},
    {'p': 'Applications divide into consumer, organizational (medical, transportation, '
          'building/home automation), industrial and infrastructure spaces.'},
    {'p': '**Consumer applications:** connected vehicles (autonomous attributes); home '
          'automation/smart homes (e.g. an iPhone controlling home devices); wearable '
          'technology (monitoring various parameters); connected health (appliances connecting '
          'patients directly to hospitals in emergencies, with remote monitoring).'},
    {'p': '**Medical and healthcare:** the **Internet of Medical Things (IoMT)** applies IoT to '
          'medical/health purposes, data collection, research and monitoring — creating a '
          'digitized healthcare system connecting medical resources and services; used in '
          'remote health monitoring, emergency notification, wearable heart monitors and '
          'point-of-care diagnostics; fundamental to managing chronic diseases and disease '
          'prevention/control.'},
    {'p': '**Transportation:** smart traffic control; smart parking; electronic toll '
          'collection; logistics and fleet management; vehicle control; safety and road '
          'assistance; vehicular communication systems — **Vehicle-to-Everything (V2X)** '
          'communication, comprising **V2V** (vehicle-to-vehicle), **V2I** (vehicle-to-'
          'infrastructure) and **V2P** (vehicle-to-pedestrian), the first step to autonomous '
          'driving and connected road infrastructure.'},
    {'p': '**Building and home automation:** monitoring and controlling mechanical, electrical '
          'and electronic systems in public, private, industrial, institutional or residential '
          'buildings.'},
    {'p': '**Industrial applications (IIoT)** — industrial IoT devices acquire and analyse '
          'data from connected equipment, operational technology (OT), locations and people, '
          'helping regulate and monitor industrial systems.'},
    {'p': '**Manufacturing:** connects devices with sensing, identification, processing, '
          'communication, actuation and networking capabilities; enables network control and '
          'management of equipment, asset/situation management, and process control — '
          'supporting rapid manufacturing, product optimisation and fast response to demand. '
          'Also used to automate process controls, optimise plant safety/security via digital '
          'control systems, and support predictive maintenance and smart-grid energy '
          'optimisation; also used in the industrialization of construction.'},
    {'p': '**Agriculture:** collecting data on temperature, rainfall, humidity, wind speed, '
          'pest infestation and soil content, to automate farming techniques, improve '
          'decisions, minimise risk/waste, and reduce management effort.'},
    {'p': '**Maritime:** monitoring the environment and systems of boats/yachts left '
          'unattended for long periods, providing early alerts of flooding, fire or deep '
          'battery discharge.'},
    {'p': '**Infrastructure applications:** monitoring and controlling urban/rural '
          'infrastructure — bridges, railway tracks — for structural conditions that could '
          'compromise safety; benefits include cost-saving, time reduction, paperless workflow '
          'and productivity increases; also used for scheduling repair/maintenance, '
          'coordinating between service providers/users, and controlling critical '
          'infrastructure (e.g. bridges providing ship access); can also improve incident '
          'management, waste management and up-times across infrastructure areas.'},
    {'p': '**Metropolitan-scale deployments:** e.g. **Songdo, South Korea** — a fully '
          'equipped, wired smart city, largely automated with little human intervention.'},
    {'p': '**Energy management:** IoT-connected lamps, appliances, motors and pumps '
          'communicate with utilities to balance power generation and optimise consumption, '
          'enabling remote/central control and scheduling functions.'},
    {'p': '**Environmental monitoring:** sensors assist environmental protection by monitoring '
          'air/water quality, atmospheric/soil conditions, and even wildlife movements/'
          'habitats.'},
    {'p': '**Military applications:** the **Internet of Military Things (IoMT)** applies IoT '
          'to reconnaissance, surveillance and combat objectives, using sensors, munitions, '
          'vehicles, robots and human-wearable biometrics. The **Internet of Battlefield '
          'Things (IoBT)** enhances soldiers\' capabilities. The **Ocean of Things** project '
          '(DARPA-led) deploys about **50,000 floats** with passive sensors to autonomously '
          'detect and track military/commercial vessels across large ocean areas, as part of '
          'a cloud-based network.'},
    {'p': '**Product digitalization ("Internet of Packaging")** — a QR code or NFC tag on a '
          'product/packaging carries a unique identifier (typically a URL), letting a user '
          'access digital content via a smartphone, automating supply chains at scale. '
          'Authentication is possible via a copy-sensitive digital watermark or copy-detection '
          'pattern for QR scanning; NFC tags can encrypt communication.'},
    {'h3': 'Architecture of IoT'},
    {'p': 'An IoT system has three tiers: **Tier 1 — Devices**: networked things (sensors, '
          'actuators) using protocols such as Modbus, Bluetooth, Zigbee or proprietary '
          'protocols, connecting to an Edge Gateway. **Tier 2 — The Edge Gateway**: sensor-'
          'data aggregation systems providing pre-processing of data, secure cloud '
          'connectivity (e.g. via Web Sockets, the event hub), and sometimes edge analytics or '
          'fog computing, giving upper layers a common view of devices for easier management. '
          '**Tier 3 — The Cloud**: the cloud application, built for IoT and inherently secure '
          '(HTTPS/OAuth), including database systems storing sensor data (e.g. time-series '
          'databases, asset stores) and an event queuing/messaging system handling '
          'communication across all tiers.'},
  ]},

  {'n': '6.15', 't': 'Distributed Ledger Technology', 'b': [
    {'def': {'t': 'Distributed ledger', 'd': 'databases shared across a network and spread '
                  'over various geographical locations. A ledger is a collection of financial '
                  'accounts; "distributed" means spread out and controlled globally — so a '
                  'distributed ledger is held and reorganized by multiple parties in different '
                  'locations and institutions. Participants at each network node can access an '
                  'identical copy of the shared recordings; when the ledger is edited or '
                  'appended, changes are replicated and copied to participants, and the '
                  'database is synchronized for accuracy.'}},
    {'def': {'t': 'Distributed ledger technology', 'd': 'a digital system that records '
                  'asset-related transactions simultaneously at numerous places, with no '
                  'administration facility or central data storage — the database exists among '
                  'several participants or across different geographical locations. It allows '
                  'users to record, share and synchronize data and transactions across a '
                  'distributed network of numerous participants, and covers a range of '
                  'technologies with comparable structures but different rules of execution. It '
                  'can be **public** or **private** (based on accessibility to anyone or to '
                  'devices/nodes), and **permissioned** or **permissionless** (based on whether '
                  'participants need permission from an entity to edit the ledger).'}},
    {'h3': 'Importance of distributed ledger technology'},
    {'ul': [
      'Can make the finance sector more resilient, efficient and reliable — processing '
      'transactions without third-party involvement, enabling cross-border payments, and '
      'helping make finance accessible to the unbanked.',
      'Can be applied to other industries, such as government financial systems, clean '
      'energy and manufacturing.',
      'Removes the requirement for a central authority, increasing transaction speed.',
      'Can reduce transaction costs.',
      'Since records are held at each network node, manipulating or attacking the system is '
      'very difficult, making it a more secure way to handle records.',
      'As information is shared and viewed across the network, it provides a more '
      'transparent means of handling records.',
      'Can be used to distribute social benefits, transfer property deeds, collect tax, and '
      'run voting procedures; also used for processing/executing legal documents; and lets '
      'individuals hold and control their personal information, sharing selective pieces of '
      'it when required.',
    ]},
    {'h3': 'How distributed ledgers work'},
    {'p': 'Distributed ledgers are held, reorganized and controlled by individuals called '
          '**nodes**. Each node independently constructs the database; every transaction is '
          'processed, and each node draws a conclusion on database development. Voting is '
          'carried out on the changes; all nodes participate, and if at least **51%** agree, '
          'the new transaction is accepted, after which nodes update their database versions '
          'so all are consistent. The new transaction is written onto a block on the '
          'blockchain.'},
    {'p': 'Nodes in a **Proof-of-Work** blockchain are also called **miners**; a miner who '
          'successfully puts a new transaction into a block receives a reward. It requires '
          'dedicated 24×7 computer power, since miners compute the cryptographic hash for new '
          'blocks — whoever finds the hash first gets the reward. Miners dedicating more '
          'computational power are more successful, but finding subsequent hashes becomes '
          'harder as blocks keep generating, with the goal of keeping a constant block-'
          'generation speed.'},
    {'h3': 'Benefits of distributed ledgers'},
    {'ol': [
      '**Highly transparent, secure, tamper-proof and immutable** — entries happen without '
      'third-party involvement, and once written, records cannot be altered by any other '
      'party.',
      '**The need for a third party is eliminated** — saving money, effort and time, e.g. in '
      'supply chains where sensors write results directly to the blockchain.',
      '**Inherently decentralized** — spread globally, adding a layer of security since it is '
      'difficult to attack.',
      '**Highly transparent** — all stored information is freely and easily viewable, '
      'providing transparency desired by many industries.',
    ]},
    {'h3': 'Examples of distributed ledgers'},
    {'ul': [
      '**Bitcoin** — a highly popular virtual currency for payments on a network enabling '
      'non-reversible payments with transaction fees lower than conventional online payment '
      'methods.',
      '**Ethereum** — a popular distributed ledger letting developers create their own '
      'applications, well known for introducing **smart contracts** — self-executing '
      'contracts triggered when pre-set, real-world conditions are fulfilled and related data '
      'is entered into the blockchain.',
      '**Ripple** — an open-source ledger focusing on payments, especially cross-border '
      'transactions, originally intended for banks.',
    ]},
  ]},

  {'n': '6.16', 't': 'Blockchain', 'b': [
    {'def': {'t': 'Blockchain', 'd': 'a list of records called **blocks** that store data '
                  'publicly and in chronological order. Information is encrypted using '
                  'cryptography to preserve user privacy and prevent alteration. A blockchain '
                  'network is not controlled by a centralized authority (unlike modern '
                  'financial institutions); participants maintain the data and hold democratic '
                  'authority to approve transactions — a typical blockchain network is a '
                  '**public** blockchain. Any participant has access to the data and holds the '
                  'same copy of the ledger as everyone else; if one participant\'s node or '
                  'data is corrupted, other participants are alerted immediately and can '
                  'rectify it.'}},
    {'h3': 'Blockchain techniques'},
    {'p': 'A combination of three technologies: **cryptographic keys**, a **peer-to-peer '
          'network**, and a **digital ledger**.'},
    {'p': 'Cryptographic keys are of two types — **private key** and **public key**. Each '
          'individual/node has both, used to create a **digital signature** — a unique, secure '
          'digital identity reference, and the most important aspect of blockchain '
          'technology, since every transaction is authorized by the owner\'s digital signature. '
          'A deal/transaction is authorized by mathematical verification in a peer-to-peer '
          'network — a large group of individuals acting as authorities to reach a consensus '
          'on transactions. All transactions are stored in the **digital ledger**, which works '
          'like a spreadsheet, containing all the nodes in a network and the history of all '
          'purchases made by each node. The digital signature safeguards it from tampering; '
          'anyone can see the data, but no one can corrupt it.'},
    {'h3': 'Features of blockchain'},
    {'ul': [
      'It is a public distributed ledger, working via hashing encryption.',
      'Every block has a **hash value** — the digital signature of the block.',
      'Transactions are approved and verified using a **proof-of-work consensus algorithm**.',
      'The network utilises the resources of **miners**, who validate transactions for '
      'rewards.',
    ]},
    {'h3': 'Fields of a blockchain block'},
    {'p': 'Every block has four fields: **previous hash** (the hash of the previous block); '
          '**transaction details** (information on several transactions); **nonce** (a random '
          'value acting as a variate for the hash value); **hash address** (the block\'s unique '
          'identification — a 64-character hex value, letters and numbers, obtained via the '
          '**SHA-256** algorithm).'},
    {'h3': 'Uses of blockchain'},
    {'p': 'Beyond cryptocurrency and Bitcoin: **anti-money laundering tracking systems; NFT '
          'marketplaces; original content creation; real-time IoT operating systems; '
          'advertising insights; music royalties tracking; cross-border payments; voting '
          'mechanisms; supply chain and logistics monitoring.**'},
    {'h3': 'Other fields that use blockchain'},
    {'ul': [
      '**Financial services** — healthcare provision, crowdfunding, ride-sharing.',
      '**Travel** — tracking luggage across multiple flights/international itineraries; '
      'identifying passengers to save time and reduce queues; making/accepting payments for '
      'services.',
      '**Music** — helps prevent piracy (illegal sharing) of music files; compensates artists '
      'for purchased songs/albums.',
      '**Cyber security** — secures sensitive data via cryptography; eliminates the need for '
      'passwords, since users/devices authenticate via public and private keys.',
      '**Human resources** — eliminates individual verification checks by storing identity/'
      'employment history on blockchain; tracks payments and expenses, easing tax obligations '
      'for employers and employees.',
    ]},
    {'h3': 'Distributed ledger technology vs blockchain technology'},
    {'ul': [
      'Often used interchangeably, but distinct — blockchain uses many technologies, and '
      'distributed ledger technology is one of them.',
      '**Blockchain** is a type of distributed ledger technology using cryptography, making '
      'it difficult to manipulate — an unchangeable, distributed ledger for recording '
      'transactions, transferring ownership and tracking assets, ensuring security, '
      'transparency and trust.',
      'In blockchain, data is organised and stored in packages ("blocks") chained together; '
      'blocks cannot be edited — blockchain technology allows only the **addition** of more '
      'blocks.',
      'Blockchains are usually **public** — transaction histories can be viewed by anyone, '
      'and anyone can become a node and participate; hence blockchain is **permissionless**.',
      'Not all distributed ledger technologies use chains of blocks, though they still use '
      'cryptographic validation; distributed ledger technology creates a decentralized ledger '
      'for obtaining consensus among participants who distrust each other, so new information '
      'is added only when all participants consent.',
      'Unlike blockchain, distributed ledger technology usually restricts access, use, and who '
      'may be a node, and uses a cryptographic signature to automatically timestamp new '
      'entries.',
      'Distributed ledger technology can be both public and private, and both permissioned '
      'and permissionless.',
    ]},
  ]},

  {'n': '6.17', 't': 'Cryptocurrency', 'b': [
    {'def': {'t': 'Cryptocurrency', 'd': 'a form of digital currency used to verify the '
                  'transfer of assets, control the addition of new units, and secure financial '
                  'transactions, using cryptography.'}},
    {'p': 'One of its most important advantages over fiat currencies is that it is not '
          'controlled by any central authority — with no central point of failure or "vault", '
          'funds cannot be hacked or stolen in the traditional sense. The shared, distributed '
          'nature of cryptocurrencies keeps everyone on the same page, so blockchain\'s '
          'transparency and distribution are what make cryptocurrencies (at least those using '
          'blockchain) secure.'},
    {'h3': 'Types of cryptocurrency'},
    {'p': 'Popular examples: **Bitcoin, Litecoin, Ethereum, Z Cash, Dash, Ripple, Monero, NEM, '
          'Stellar, Binance Coin.** There are close to **3,000** cryptocurrencies in a nearly '
          'saturated market; most experts expect the vast majority to eventually fail as users '
          'gravitate to a few.'},
  ]},

  {'n': '6.18', 't': 'Computer robotics and business automation (CRBA)', 'b': [
    {'h3': 'Computer robotics'},
    {'def': {'t': 'Robotics', 'd': 'a branch of engineering concerned with the design and '
                  'construction of robots, and the use of computers to manipulate and reuse '
                  'them.'}},
    {'p': 'In manufacturing, robots speed up processes. **Robotic Process Automation (RPA)** '
          'is used in large firms with big HR, IT and finance departments, automating '
          'labour-intensive workflow, infrastructure and back-office procedures. Robotics is a '
          'sub-category of industrial automation, since a robot is only a set of sensors and '
          'processors performing an industrial task. **Software robots** (workstation '
          'automation/RPA) are computer programs that automate **virtual** operations instead '
          'of physical ones — using the same logic humans use with computer applications. A '
          'physical robot speeds up assembly/production; software-driven automation is better '
          'suited to making repetitive administrative activities more efficient. Industrial '
          'automation is about controlling and maintaining physical processes — e.g. Amazon\'s '
          'fully automated, robot-staffed warehouses, which explains its short shipping times.'},
    {'h3': 'Business Process Automation (BPA)'},
    {'def': {'t': 'Business Process Automation (BPA)', 'd': 'the use of technology to execute '
                  'recurring tasks or processes where manual effort can be replaced, done to '
                  'minimize costs, increase efficiency and streamline processes.'}},
    {'h4': 'Examples of BPA'},
    {'p': '**(1) Employee engagement** — hiring involves filling employee information forms, '
          'setting up induction/training sessions, opening bank accounts, collecting '
          'documents, and assigning supervisors. Without automation this can become chaotic: '
          'endless paperwork, missed tasks, employee dissatisfaction, low productivity. '
          'Automating it ensures smooth transitions between tasks, keeps relevant employees '
          'informed, and provides visibility into the process status.'},
    {'p': '**(2) Purchase order (PO) processing** — a requesting team fills a form sent to '
          'purchasing; the approving authority examines and may reject it (inadequate '
          'information, budget constraints), sending it back; if approved, a PO is created and '
          'sent to the supplier and inventory team. Without automation: delayed PO approval, '
          'impacted productivity, incomplete records, PO errors, and errors on delivery. '
          'Automation improves accountability, transparency and accurate data recording, and '
          'retains all process communication within the workflow for faster, easier execution.'},
    {'h4': 'Benefits of BPA'},
    {'ol': [
      '**Stepping stone to digital transformation** — a manageable start toward continuous '
      'transformation culture, beginning with a few clearly-needed processes.',
      '**Business process clarity** — automation demands clarity about tasks and '
      'responsibility at the design stage; process mapping also aids training, and reveals '
      'the gap between the process as-is and as it should be.',
      '**Streamlined processes** — clear accountability, customisable notifications, valuable '
      'insights and faster turnaround eliminate wasteful activities.',
      '**Compliance records** — every process detail is recorded, useful to demonstrate '
      'compliance during audits.',
      '**Standardised operations** — a consistent standard of outcomes, positioning the '
      'organization as reliable and helping grow its customer base.',
      '**Increased customer satisfaction** — process/operational excellence helps exceed '
      'customer expectations and build customer preference.',
    ]},
    {'h4': 'Identifying business processes to automate'},
    {'p': 'Indicators that a process needs automation: high volume of tasks; multiple people '
          'required to execute tasks; time-sensitive nature; significant impact on other '
          'processes/systems; need for compliance and audit trails.'},
    {'p': 'Commonly automated processes: e-mail and push notifications; helpdesk support; data '
          'aggregation and migration; backup and restoration; employee leave requests; '
          'procurement; call centre processes; sales orders; time and attendance tracking; '
          'payroll; invoicing; collections; product launches.'},
    {'h4': 'Benefits of using BPA tools'},
    {'ol': [
      'Boost in productivity from enhanced access — cloud-based tools store data centrally, '
      'accessible from any location/device.',
      'Business processes become more transparent — tracking and monitoring while running '
      'improves accountability and visibility.',
      'Insight through performance reports — spotting and fixing errors, taking preventive '
      'measures against recurring ones.',
      'Improved efficiency — faster turnaround and reduced costs from fewer manual '
      'interventions.',
      'Allocation of the workforce to more challenging functions — the application handles '
      'mundane, recurring tasks, freeing employees for tasks needing human judgment.',
    ]},
    {'h4': 'Best practices for BPA'},
    {'ul': [
      'Start with a clear understanding of the tasks, who is responsible, and when each is to '
      'be executed.',
      'Have clearly defined goals when automating, to save time on course correction.',
      'Measure results with a phased approach, expecting results gradually rather than '
      'immediately.',
      'Invest adequate time training employees, and allow for an adjustment period.',
      'Adopt a long-term outlook for good return on investment (ROI).',
      'Use readymade solutions where available.',
    ]},
    {'h3': 'Key differences between robotics and automation'},
    {'ol': [
      'Robotics is better defined as a sub-category of automation, which includes software '
      'agents needing no hardware.',
      'A robot is controlled by programming and mechatronics, letting it perform sophisticated '
      'movements; automation varies by the component used.',
      'Manufacturers deal with both daily, creating electrical products that make life easier.',
      'Robotics and automation go hand in hand when automating a system/machine to complete a '
      'task quickly and precisely — both are mechanically working industrial machines.',
      'Not all robots are built for process automation, though most industrial robots are — a '
      'toy line-following robot is not "automation" since it does not carry out a defined '
      'duty, but a line-following robot moving drugs through a hospital would be.',
      'Neither aims to eliminate all human workers — both speed up manufacturing and reduce '
      'errors. Automation ranges from fully mechanical to fully virtual, and from simple to '
      'elaborate.',
      'Many automations do not include a robot at all — a robot is just one piece of '
      'equipment that can be combined into a semi- or fully automated system.',
      'RPA\'s primary goal is to reduce staff, whereas other automation techniques aim to '
      'reduce processing time; non-technical people can use RPA to boost productivity by '
      'freeing them for tasks that cannot be automated, whereas traditional automation is '
      'solely available to technical users.',
    ]},
  ]},

  {'n': '6.19', 't': 'Drone technology', 'b': [
    {'def': {'t': 'Drone (unmanned aerial vehicle, UAV)', 'd': 'basically a flying robot that '
                  'can be controlled remotely, or that may fly on its own using software-'
                  'controlled flight plans embedded in its systems.'}},
    {'p': 'Wide range of uses: military intelligence gathering and anti-aircraft target '
          'practice; weather monitoring/prediction; traffic monitoring; search and rescue in '
          'places impenetrable to humans or larger machines; surveillance; personal and '
          'business use; real estate and delivery services; aerial photography/videography '
          '(with attached cameras).'},
    {'h3': 'Components of drone technology'},
    {'ul': [
      '**Radar positioning and Return-to-Home** — modern drones integrate dual Global '
      'Navigational Satellite Systems (GNSS), including **GPS** and **GLONASS**, flying in '
      'GNSS or non-satellite modes; radar positioning aids accurate navigation and shows the '
      'drone\'s position relative to the controller; the **Return-to-Home** feature guides the '
      'drone back to the controller.',
      '**Obstacle detection and collision avoidance technology** — high-tech drones scan the '
      'surrounding environment with sensors, while **SLAM** technology and software '
      'algorithms transform the scanned images into a 3D map.',
      '**Gyroscope stabilization** — lets drones fly smoothly, and provides navigational data '
      'to the flight controller.',
      '**Inertial Measurement Unit (IMU)** — detects current acceleration using one or more '
      'accelerometers, by tracking rotational-attribute changes via the gyroscope.',
      '**Motors and propellers** — enable the drone to move into the air and hover or fly in '
      'any direction, based on data from the flight controller and electronic speed '
      'controllers.',
    ]},
    {'h3': 'Uses of drones'},
    {'ul': [
      '**Military** — the earliest use (Cold War spying); modern drones carry thermal '
      'imaging, laser range finders, and even airstrike tools.',
      '**Delivery** — autonomous "last mile" delivery UAVs transport food, packages or goods '
      'from local stores/warehouses; brands testing/using them include Amazon, Walmart, '
      'Google, FedEx, UPS.',
      '**Emergency rescue** — deployed where scenes are unsafe for humans; an **Autonomous '
      'Underwater Vehicle (AUV)** assists rescuing capsized-boat or drowning victims; drones '
      'search avalanche victims; pilot-less helicopters assist firefighting (China, '
      'Australia).',
      '**Agriculture** — field surveys, seeding, tracking livestock, estimating crop yield, '
      'saving farmers time and reducing physical strain.',
      '**Outer space** — NASA and the US Air Force have secretly tested unmanned space '
      'aircraft (e.g. the **X-37B**, an ultra-secretive drone resembling a miniature space '
      'shuttle); private companies (SpaceX, Blue Origin, Virgin Galactic) carry payloads and '
      '(more recently) passengers, marking the start of space tourism.',
      '**Wildlife and historical-site conservation** — track roaming animal groups (lions, '
      'elephants, orangutans, bison) to assess species/ecosystem health, help fight poaching, '
      'and support reforestation (dropping seed vessels with fertilizer/nutrients on '
      'fire-decimated forest floors); produce 3D maps of historical sites (e.g. Chernobyl, '
      'Ephesus) to aid preservation and reconstruction.',
      '**Medicine** — deliver critical medical supplies (vaccines, transplant organs) to '
      'difficult-to-reach areas, quickly and safely.',
      '**Photography** — used by photographers for expansive aerial photos of cities, beaches '
      'or buildings.',
    ]},
    {'h3': 'Requirement to fly a drone'},
    {'p': 'In many jurisdictions, commercial drone use requires a pilot\'s licence; some '
          'jurisdictions offer a **Remote Pilot Certificate**, obtained via an aeronautical '
          'knowledge test.'},
    {'h4': 'General rules for flying a drone in Nigeria (NCAA)'},
    {'ul': [
      'It is unlawful to operate a drone without the required authorisations — flight plans '
      'must be submitted to the **Nigeria Civil Aviation Authority (NCAA)** for authorization '
      'before each individual flight.',
      'Drones weighing more than **250 grams (0.55 lb)** must be registered with the NCAA.',
      'Operators must obtain a **Remotely Piloted Aircraft Systems Certificate** before flying '
      'in Nigeria.',
      'All drone operators must be at least **16 years of age** or older.',
      'Drones may not be operated recklessly, or in a manner that may harm persons, property '
      'or other aircraft.',
      'Do not fly across a border into or from another state.',
      'Do not operate over the high seas without proper authorization from Air Traffic '
      'Control.',
    ]},
    {'h3': 'Challenges of drone technology'},
    {'ul': [
      '**Privacy** — cameras let operators photograph/record without consent, causing '
      'discontent; laws restricting this exist, but many users ignore them.',
      '**Air accidents** — drones can now reach heights up to **50,000 feet** (commercial '
      'flight range), moving stealthily and being hard for pilots and air-traffic radar to '
      'track, risking air accidents.',
      '**Crashes** — a high risk from limited battery power, fast-spinning propellers, and the '
      'potential to fall from great heights, posing risks to people, property and the '
      'environment as drone numbers increase.',
    ]},
  ]},

  {'n': '6.20', 't': 'Chapter summary', 'b': [
    {'p': 'The systems development life cycle is a comprehensive tool for solving '
          'organizational problems, especially those relating to the flow of computer-based '
          'information; an organisation must select a particular development approach to '
          'avoid ad-hoc or trial-and-error methods likely to result in failed systems.'},
    {'p': 'Prototyping is a typical 4GL tool used to develop good working systems — early '
          'definition of a system, creation of a prototype, and continued test/review with '
          'users, iterating until the final working system is attained, so users are assured '
          'of a good system rather than something simply "thrown" at them. **JAD** and **RAD** '
          'let users be fully engaged in development, assuring user ownership of the resulting '
          'systems.'},
    {'p': '**Outsourcing** lets an organisation focus its management capability on critical '
          '(key) areas of competence, giving out non-key activities to outside experts, so '
          'management can concentrate on core activities while paying for expert outside '
          'services. An organisation should not outsource a core activity, since this can leak '
          'operational information and expose it to attack from competitors.'},
    {'p': 'This chapter also discussed computer crimes (viruses and worms), cybercrime (with '
          'many examples), standard health issues, the definition and application of computer '
          'forensics to legal issues, and the cloud computing model — its advantages and '
          'disadvantages. It also discussed disruptive technologies: **artificial intelligence '
          'and machine learning; Internet of Things; distributed ledgers/blockchain '
          'technology; computer robotics and business automation; and drone technology.**'},
  ]},

  {'n': '6.21', 't': 'End-of-chapter questions (study text)', 'b': [
    {'h3': 'Multiple-choice questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–49 with answers', 'open': True, 'q': [
      {'ol': [
        'A crime in which an imposter obtains pieces of personal identification in order to '
        'impersonate someone else is called (A) Espionage  (B) Identity theft  (C) Fraud  '
        '(D) Spamming  (E) Data diddling',
        'One way of providing security to prevent unauthorised persons gaining physical '
        'access to a company\'s IT environment when computer personnel are on duty is by '
        'using (A) Password  (B) Firewall  (C) Identity cards  (D) Locks and keys  (E) Fire '
        'extinguishers',
        'The Repetitive Stress Injury (RSI) problems normally associated with computer users '
        'does NOT include (A) Hepatitis  (B) Tendonitis  (C) Tennis elbow  (D) Inability to '
        'hold objects  (E) Sharp pains in the fingers',
        'A program capable of attaching itself to disks and other files and replicating '
        'itself repeatedly without the user\'s knowledge is called (A) Virus  (B) Worm  '
        '(C) Trojan Horse  (D) Logic Bomb  (E) Variant',
        'In the assessment stage of the System Development Life Cycle (SDLC), system analysis '
        'focuses on three types of need, which are input, output and … (A) Central Processing '
        'Unit  (B) Processing  (C) Arithmetic and Logic Unit  (D) Control Unit  (E) Random '
        'Access Memory',
        'After the new system is developed, the four strategies for implementation are: '
        'Direct Conversion, Parallel Conversion, Pilot Changeover and … (A) Phased '
        'Changeover  (B) Control  (C) Pending  (D) Horizontal  (E) Changeover',
        'Which of the following is a method for collecting data during system investigation? '
        '(A) Interview  (B) Collation  (C) Scanning  (D) Probing  (E) Persuasion',
        'Which of the following is NOT part of implementation activities in a System '
        'Development Life Cycle? (A) Acquisition of hardware and software  (B) End-user '
        'training  (C) Cost-benefit analysis  (D) System documentation  (E) File conversion',
        'Which one of the following is NOT a key element in presenting digital evidence that '
        'is legally acceptable? (A) Identification  (B) Investigation  (C) Preservation  '
        '(D) Analysis  (E) Presentation',
        'A software that provides a variety of tools for investigating a suspect\'s personal '
        'computer is called (A) Computer software  (B) Cyber software  (C) Forensic software  '
        '(D) Software tools  (E) Service software',
        'Which one of the following is NOT a computer crime? (A) Impersonation  (B) Computer '
        'virus  (C) Spoofing  (D) Spooling  (E) Scavenging',
        'Security threats related to computer crime or abuse include the following EXCEPT '
        '(A) Impersonation  (B) Trojan horse method  (C) Logic Bomb  (D) Computer virus  '
        '(E) Provision of service',
        'Computer forensics does NOT involve one of the following: (A) Data extraction  '
        '(B) Data recovery  (C) Data gathering of computer system and peripherals  '
        '(D) Investigation of computer personnel  (E) Investigation of a computer believed to '
        'be involved in cybercrime',
        'Forensic investigation as a process does NOT involve the … of digital evidence '
        '(A) Identification  (B) Presentation  (C) Preservation  (D) Analysis  (E) Design',
        'If a robot can alter its own trajectory in response to external conditions, it is '
        'considered to be: (A) Intelligent  (B) Mobile  (C) Open loop  (D) Non-servo  '
        '(E) Creative',
        '… provide the means to create capability that reflects true awareness of the '
        'physical world and people. (A) Sensors  (B) Heterogeneity  (C) Security  '
        '(D) Connectivity  (E) Feelers',
        '… in IoT, as one of the key characteristics, means devices have different hardware '
        'platforms and networks. (A) Sensitivity  (B) Heterogeneity  (C) Security  '
        '(D) Connectivity  (E) Homogeneity',
        'What is the full meaning of IoT? (A) Introduction of Things  (B) Internet of Things  '
        '(C) Internet of Tracking  (D) Interaction of Things  (E) Improvement of Things',
        'What is the role of the cloud in the smart-grid architecture of IoT? (A) Store data  '
        '(B) Manage data  (C) Collect data  (D) Security  (E) Dispose of data',
        'What is the role of Big Data in the smart-grid architecture of IoT? (A) Store data  '
        '(B) Manage data  (C) Collect data  (D) Security  (E) Dispose of data',
        'Data of … bytes in size is called Big Data. (A) Tera  (B) Giga  (C) Peta  (D) Meta  '
        '(E) Kilo',
        'Numbers, text, image, audio and video data is … (A) Volume  (B) Value  (C) Veracity  '
        '(D) Variety  (E) Velocity',
        'The examination of large amounts of data to see what patterns or other useful '
        'information can be found is known as (A) Data examination  (B) Information analysis  '
        '(C) Big Data analytics  (D) Data analysis  (E) Pattern mapping',
        'Application of machine learning methods to large databases is called (A) Data '
        'mining  (B) Artificial intelligence  (C) Big data computing  (D) Internet of Things  '
        '(E) Big data simulation',
        'If a machine learning model\'s output involves a target variable, that model is '
        'called a (A) Descriptive model  (B) Predictive model  (C) Reinforcement learning  '
        '(D) Generic model  (E) Linear model',
        'In what type of learning is labelled training data used? (A) Unsupervised learning  '
        '(B) Supervised learning  (C) Reinforcement learning  (D) Active learning  '
        '(E) Q-learning',
        'What characterizes unlabelled examples in machine learning? (A) There is no prior '
        'knowledge  (B) There is no confusing knowledge  (C) There is prior knowledge  '
        '(D) There is plenty of confusing knowledge  (E) There is no knowledge at all',
        'Data used to build a data mining model is called … (A) Training data  (B) '
        'Validation data  (C) Test data  (D) Hidden data  (E) Mined data',
        'The problem of finding hidden structure in unlabelled data is called … '
        '(A) Supervised learning  (B) Unsupervised learning  (C) Reinforcement learning  '
        '(D) Semi-supervised learning  (E) Mixed learning',
        'Which scenario would you address using a supervised learning algorithm? (A) Given '
        'e-mails labelled as spam or not spam, learn a spam filter  (B) Given a set of news '
        'articles, group them into sets about the same story  (C) Given customer data, '
        'automatically discover and group market segments  (D) Find patterns in market basket '
        'analysis  (E) Given a set of unrelated materials',
        'You are given reviews of a few Netflix series marked as positive, negative and '
        'neutral. Classifying reviews of a new Netflix series is an example of '
        '(A) Supervised learning  (B) Unsupervised learning  (C) Semi-supervised learning  '
        '(D) Reinforcement learning  (E) Mixed learning',
        'The output of the training process in machine learning is (A) A machine learning '
        'model  (B) A machine learning algorithm  (C) Null  (D) Accuracy  (E) A training '
        'algorithm',
        'Blockchain is a peer-to-peer … distributed ledger technology that makes the records '
        'of any digital asset transparent and unchangeable. (A) Decentralized  '
        '(B) Centralised  (C) Demanding  (D) Secure  (E) Popular',
        '… hosts the software needed for transaction initiation, validation, mining, block '
        'creation and smart contract execution. (A) External Account  (B) EVM  (C) Ethereum '
        'full node  (D) Smart Contract  (E) Cryptograph',
        'What is Blockchain? (A) A currency  (B) An accounting ledger  (C) A type of currency  '
        '(D) A distributed ledger on a peer-to-peer network  (E) A general ledger',
        'Bitcoin is based on … blockchain. (A) Private  (B) Public  (C) Private permissioned  '
        '(D) Public permissioned  (E) Permissioned',
        'BATM stands for … (A) Bounded Access Transaction Machine  (B) Broad Access '
        'Transaction Machine  (C) Broadcast ATM  (D) Bitcoin ATM  (E) Blockchain ATM',
        'Smart contract characteristics do NOT include: (A) Alterable  (B) Fast  '
        '(C) Cost-effective  (D) A high degree of accuracy  (E) Transparency',
        'The size and weight of micro drones vary between (A) 200 cm–300 cm and 2 kg–3 kg  '
        '(B) 50 cm–200 cm and 250 g–2 kg  (C) 300 cm–400 cm and 3 kg–4 kg  (D) 10 cm–40 cm and '
        '50 g–150 g  (E) 500 cm–700 cm and 1 kg–2 kg',
        'What is a UAV? (A) Unmanned Aerial Vehicle  (B) Unmanned Automatic Vehicle  '
        '(C) Unused Automatic Vehicle  (D) Upper Aerial Vehicle  (E) Unarmed Aerial Vehicle',
        'Material borne by a drone while in operation is called (A) Drone material  '
        '(B) Drone luggage  (C) Payload  (D) Camera  (E) Visor',
        '… is the process of retaining or keeping data at a secure place for long-term '
        'storage. (A) Data archiving  (B) Archival storage  (C) Disposal of data  (D) Backup  '
        '(E) Disk storage',
        'What does DPIA stand for? (A) Data Privacy Impact Assessment  (B) Data Privacy '
        'Information Assessment  (C) Data Protection Impact Assessment  (D) Data Privacy '
        'Identification Assessment  (E) Data Protection Identification Assessment',
        'Who is responsible under the GDPR to notify the supervisory authority in the event of '
        'a data breach? (A) Data Subject  (B) Data User  (C) Data Processor  (D) Data '
        'Controller  (E) Data Report Manager',
        'What does GDPR stand for? (A) General Data Privacy Regulation  (B) Global Data '
        'Protection Regulation  (C) Global Data Protection Regulation  (D) General Data '
        'Protection Regulation  (E) Global Data Privacy Registration',
        'In case of a data breach, the GDPR requires the notification to be sent to '
        'authorities within: (A) 72 hours  (B) 42 hours  (C) 24 hours  (D) 12 hours  '
        '(E) 8 hours',
        'Which data is NOT considered "personal data" under the GDPR? (A) Name  (B) Date of '
        'birth  (C) Maiden name  (D) Phone number  (E) Ethnicity',
        'Which of the following is available on a company\'s website? (A) Data Privacy '
        'Policy  (B) Employee Privacy Notice  (C) Management Privacy Policy  (D) Employment '
        'Candidate Privacy Notice  (E) Website Privacy Policy',
        'The two major categories of software are application software and … '
        '(A) Utility software  (B) System software  (C) UNIX software  (D) High-level '
        'languages  (E) CAD software',
      ]}],
      'a': [
      {'p': '**1.** B  **2.** C  **3.** A  **4.** B  **5.** B  **6.** A  **7.** A  **8.** C  '
            '**9.** B  **10.** C  **11.** D  **12.** E  **13.** D  **14.** E  **15.** A  '
            '**16.** A  **17.** B  **18.** B  **19.** B  **20.** A  **21.** C  **22.** D  '
            '**23.** C  **24.** A  **25.** B  **26.** B  **27.** A  **28.** A  **29.** B  '
            '**30.** A  **31.** A  **32.** A  **33.** A  **34.** C  **35.** D  **36.** B  '
            '**37.** D  **38.** A  **39.** B  **40.** A  **41.** C  **42.** A  **43.** C  '
            '**44.** D  **45.** D  **46.** A  **47.** E  **48.** E  **49.** B'}]}},
    {'h3': 'Short-answer questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–11 with answers', 'open': True, 'q': [
      {'ol': [
        'The personnel responsible for determining the information needs of users and '
        'producing a system design in accordance with these is called …',
        'The terms of reference for a feasibility study group during system development is '
        'set out by …',
        'The most widely used method of fact-finding in system investigation is …',
        'The people for whom systems are designed, and who actually use the computer systems '
        'to perform their job, are called …',
        'A user or person who illegally penetrates a computer network to access and '
        'manipulate data is called …',
        'A computer crime that involves transferring funds in small quantities from large '
        'accounts to the criminal\'s account is called …',
        'A protective measure taken to prevent physical, logical and procedural damage to '
        'computer systems is called …',
        'A malicious program that spreads from computer to computer with the capability to '
        'travel without human action is …',
        'A computer crime that uses a system program to bypass regular system controls to '
        'perform unauthorised acts is called …',
        'In computer forensics, the three types of data of concern are active, archival and '
        '…',
        'Which organ is granted regulatory oversight and power to ensure compliance under the '
        'Nigeria Data Protection Act?',
      ]}],
      'a': [
      {'ol': [
        '**System Analyst.**',
        '**Steering Committee.**',
        '**Interview.**',
        '**End User.**',
        '**Hacker.**',
        '**Salami Technique.**',
        '**Computer Security.**',
        '**Worm(s).**',
        '**Super Zapping.**',
        '**Latent (data).**',
        '**Nigeria Data Protection Commission.**'],
      }]}},
    {'h3': 'Self-assessment questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–7 with answers', 'open': True, 'q': [
      {'ol': [
        'What is the difference between the parallel approach and the retrospective parallel '
        'approach as applied to a system changeover?',
        'In the development of a new system, why is prototyping important?',
        'Explain briefly the term "outsourcing".',
        'What is the relevance of Joint Application Development (JAD) to the organization?',
        'Define the concept of Rapid Application Development (RAD).',
        'Define the term computer virus.',
        'The use of computers and communication technology can have some adverse effects on '
        'human health. List any three of such effects on human health.',
      ]}],
      'a': [
      {'ol': [
        '**Whereas the parallel approach uses current transaction data to compare the old and '
        'new systems, the retrospective parallel approach uses old transaction data already '
        'run on the old system — making the latter approach faster to apply.**',
        '**Prototyping is important because it lets the eventual users of the system ensure '
        'the final product meets their exact needs; the iteration process lets users suggest '
        'necessary changes on the way to the final product.**',
        '**Outsourcing involves an organisation\'s management giving certain non-key '
        'functions to other companies to perform on its behalf, so the organisation can focus '
        'better on its core business functions. It covers services such as computer centre '
        'operations, network operations, applications management and systems integration, and '
        'is often related to downsizing/divesting to concentrate on key competencies.**',
        '**Joint Application Development describes the process by which an organisation lets '
        'its system developers work in close collaboration with the users of those systems. '
        'User participation ensures users get precisely what they require, which ultimately '
        'benefits the organisation.**',
        '**Rapid Application Development (RAD) is a quick way of building software, '
        'combining a managed approach to systems development with modern software tools such '
        'as prototyping and modelling. RAD involves end-users heavily, since their needs must '
        'be fully covered — best achieved with their full commitment and participation.**',
        '**A computer virus is a type of infectious or malicious coding designed to change or '
        'compromise a computer system. It is parasitic — once it finds a host (e.g. a PC), it '
        'is released and replicates itself very quickly. It typically infects memory and/or '
        'backing storage; some viruses cause no visible harm, while others cause extreme '
        'havoc immediately.**',
        '**Adverse effects of computers on human health: (i) repetitive strain injuries; '
        '(ii) eyestrain and headaches; (iii) back and neck pains.**'],
      }]}},
    {'h3': 'Standard examination-type questions and answers'},
    {'note': 'These fifteen questions, as printed in the study text, draw on material from '
             'across the whole IT syllabus (languages, data elements, printers, application '
             'packages, flowcharts, networks, office automation, encryption, input devices, '
             'Big Data, disruptive technologies, IoT and distributed ledgers/blockchain) rather '
             'than chapter 6 alone; they are reproduced here in full since this is the final '
             'chapter of the study text.'},
    {'eg': {'tag': 'Study text', 't': 'Question 1 — low-level vs high-level language features', 'open': True,
      'q': [{'p': 'Low-level and high-level languages are major programming languages used '
                  '(probably) in the immediate past; itemize five main features of these '
                  'languages.'}],
      'a': [
        {'h4': 'Features of a low-level language'},
        {'ul': ['Machine-oriented.', 'Runs (executes) very fast.', 'Tedious to write, and '
          'time-consuming.', 'Written in mnemonics (symbols).', 'Written by experts.',
          'Conserves internal memory space.', 'Has complex coding details.']},
        {'h4': 'Features of a high-level language'},
        {'ul': ['Problem-oriented.', 'A procedural language — needs instructions to execute a '
          'process.', 'Runs very slowly compared to a low-level language.', 'Very easy to '
          'write.', 'Written in the programmer\'s spoken language.', 'Can be written by a '
          'non-expert end-user.', 'Uses more internal memory space than a low-level language.',
          'Has fewer coding details.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 2 — computer virus and prevention', 'open': True,
      'q': [{'p': 'What is a computer virus? Give five ways of preventing a computer virus in '
                  'your environment.'}],
      'a': [
        {'p': 'A computer virus is a segment of computer code which, once maliciously '
              'introduced by an attacker into a host program, is able to gain control of the '
              'system and replicate itself onto other programs in internal memory and '
              'external media inserted into the infected PC. After a period of dormancy, the '
              'virus activates itself to destroy the host program and data.'},
        {'h4': 'Ways of prevention'},
        {'ul': ['Using original storage media.', 'Not copying software from untrusted '
          'internet sources.', 'Not using game diskettes on official PCs.', 'Regularly '
          'running antivirus software during the system\'s booting.', 'Not allowing personnel '
          'to bring external storage media into the computer environment.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 3 — data elements and a worked table', 'open': True,
      'q': [
        {'p': '(a) Explain the following data elements: file, field, bit, byte, record, '
              'database, and arrange them in ascending order.'},
        {'p': '(b) Given the table below, identify: (i) the file; (ii) a field; (iii) a byte; '
              '(iv) a record.'},
        {'table': {'align': 'lllll', 'head': ['Customer Number', 'Customer Name', 'State '
          'Code', 'Credit Limit', 'Credit Balance'], 'rows': [
          ['10568', 'AJET Co.', 'Lagos', '40,000', '10,000'],
          ['23795', 'Tosa Co.', 'Oyo', '20,000', '5,000'],
          ['38697', 'Willy Co.', 'Ogun', '10,000', '50,000'],
          ['56696', 'Best Co.', 'Benue', '50,000', '20,000'],
        ]}}],
      'a': [
        {'ul': [
          '**Bit** — the smallest unit of data; a binary digit, represented by 1 or 0.',
          '**Byte** — a string of bits, representing a character. In ASCII, 7 bits = 1 byte; '
          'in EBCDIC, 8 bits = 1 byte.',
          '**Field** — a sequence of characters storing information. Four types: character '
          'field (text), numeric field (numbers), date field (dates), logical field (testing '
          'if a condition is true or false).',
          '**Record** — a group of related fields.',
          '**File** — a collection of related records.',
          '**Database** — an integrated collection of data files.']},
        {'p': '**Ascending order:** bit → byte → field → record → file → database.'},
        {'ul': [
          '(i) **File** — the whole table, being a collection of records (all the rows).',
          '(ii) **Field** — each column, e.g. customer number, customer name, state code, '
          'credit limit, credit balance.',
          '(iii) **Byte** — a single character, e.g. any alphabet like "C", any number like '
          '"1", or any other symbol/punctuation.',
          '(iv) **Record** — any row in the table.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 4 — hardcopy vs softcopy, and printers', 'open': True,
      'q': [
        {'p': '(a) Give two differences between a hardcopy and a softcopy.'},
        {'p': '(b) Mention four characteristics that determine the choice of a printer.'},
        {'p': '(c) Name and describe briefly the two classifications of printers.'},
        {'p': '(d) Give three examples of each classification.'}],
      'a': [
        {'table': {'cap': '(a) Hardcopy vs softcopy', 'align': 'll',
          'head': ['Hardcopy', 'Softcopy'], 'rows': [
          ['Can be touched', 'Cannot be touched'],
          ['Persists', 'Transient'],
          ['May not be used as a classified document', 'Can be used as a classified/'
           'confidential document'],
          ['Can be distributed physically', 'Cannot be distributed physically'],
          ['Page size can be as large as needed', 'Page size is restricted to the screen '
           'size'],
          ['Takes some time to produce', 'Generated instantly'],
        ]}},
        {'h4': '(b) Characteristics determining choice of printer (any four)'},
        {'ul': ['Speed of producing output.', 'Quality of output.', 'Cost of purchase.',
          'Graphics abilities.', 'Associated noise level.', 'Multiple-colour output.']},
        {'h4': '(c) Classifications of printers'},
        {'p': '**Impact printers** — make contact with paper, producing sound (noise) during '
              'printing. **Non-impact printers** — do not make contact with paper, and are '
              'relatively noiseless.'},
        {'h4': '(d) Examples (three each)'},
        {'p': '**Impact:** dot-matrix, daisy wheel, chain/barrel printers, band printers (any '
              'three). **Non-impact:** LASER printers, inkjet printers, thermal printers, '
              'xerographic printers (any three).'}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 5 — application packages, sources, criteria', 'open': True,
      'q': [
        {'p': '(a)(i) What is an application package? (ii) State five sources of an '
              'application package. (iii) List five criteria used in selecting an application '
              'package.'},
        {'p': '(b) You have been appointed as accounting staff in a newly computerized '
              'company. Recommend five different application packages for your office '
              'computer.'}],
      'a': [
        {'p': '(a)(i) An **application package** is a suite of programs designed to solve a '
              'particular problem, including documentation on how to set it up and run it on '
              'the computer, and the media on which the program is stored (usually a magnetic '
              'floppy diskette or optical disk). Application packages rationalize programming '
              'efforts.'},
        {'h4': '(ii) Sources of application packages (any five)'},
        {'ul': ['Mail order, as advertised in computer magazines.', 'Over the counter, from '
          'retail shops or stores (off-the-shelf).', 'Dealers (vendors) in microcomputers.',
          'Manufacturers of computers, who also develop software.', 'Computer bureaux and '
          'information centres with expanded activities.', 'Specialised organisations known '
          'as "software houses".', 'The Internet.', 'In-house programmers (tailor-made '
          'programs).']},
        {'h4': '(iii) Criteria for selecting application packages (any five)'},
        {'ul': ['Purchase price of the package.', 'Primary memory capacity required.',
          'Availability of installed security facilities.', 'After-sales maintenance.',
          'Ability to meet users\' needs.', 'User-friendliness.', 'Flexibility of the '
          'package.', 'The technology version of the package.']},
        {'h4': '(b) Recommended packages (any five types)'},
        {'ul': [
          '**Electronic spreadsheet** — e.g. Microsoft Excel, Google Sheets, Quicken, '
          'Multiplan.',
          '**Word processing package** — e.g. Microsoft Word, Google Docs, Apache OpenOffice '
          'Writer, WordStar.',
          '**File manager/DBMS** — e.g. dBase, Access, Oracle, MySQL, IBM DB2, Microsoft SQL '
          'Server.',
          '**Graphics** — e.g. Freelance Graphics, Adobe PageMaker, PowerPoint, Canva.',
          '**Statistical package** — e.g. SPSS (Statistical Package for Social Sciences).',
          '**Accounting package** — e.g. Sage, Dac Easy, Peachtree, Zoho Books, FreshBooks, '
          'QuickBooks, SAP, Xero.',
          '**Stock/inventory control package; payroll package; general ledger package.**']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 6 — anniversary bonus flowchart', 'open': True,
      'q': [{'p': 'LAD company has 50 employees and plans to give 20% of basic salary as an '
                  'anniversary bonus. Draw a flowchart to depict the process.'}],
      'a': [{'steps': [
        'START',
        'Read name and basic salary, for each of the 50 employees',
        'Compute Bonus = 20% × salary (i.e. 2/10 × salary)',
        'Write name and Bonus',
        'Repeat until EOF (End Of File)',
        'END',
      ]}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 7 — methods of interconnecting networks', 'open': True,
      'q': [{'p': 'Describe briefly four main methods of interconnecting networks or '
                  'independent computers.'}],
      'a': [{'ul': [
        '**MODEM connection** — MODEM (MOdulation-DEModulation) converts signals from digital '
        'to analogue and back.',
        '**ISDN connection** — Integrated Service Digital Network; uses public telephone '
        'services, with data sent in digital form; all connections require Network Terminal '
        'Equipment (NTE).',
        '**Bridge or Router** — normally connects networks of the same type.',
        '**Gateway** — connects one type of network to a different type of network.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 8 — cable selection parameters', 'open': True,
      'q': [{'p': 'Cables used in networks and interconnecting independent computers include '
                  'twisted-pair, coaxial and fibre optics. Give five parameters used in '
                  'determining the selection of any one type.'}],
      'a': [{'ul': [
        'The data bit rate.', 'The reliability of the cable.', 'The maximum length between '
        'nodes.', 'The possibility of electrical hazards.', 'Power loss (noise) in the '
        'cable.', 'Tolerance to harsh conditions.', 'Expense and general availability of the '
        'cable.', 'Ease of connection and maintenance.', 'Ease of running cables.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 9 — office automation systems', 'open': True,
      'q': [
        {'p': '(a) Explain briefly what is meant by an office automation system.'},
        {'p': '(b) Enumerate and discuss three application areas of an office automation '
              'system.'},
        {'p': '(c) List two adverse effects of an office automation system on office '
              'workers.'}],
      'a': [
        {'p': '(a) An **Office Automation System** is a conglomerate of various technologies '
              'intended to improve the efficiency of office work by replacing routine '
              'clerical, secretariat and paper-based tasks with computer-based devices.'},
        {'h4': '(b) Application areas (any three)'},
        {'ul': [
          '**Word processing** — hardware/software letting the computer behave like a '
          'typewriting device, giving excellent presentation of prepared documents.',
          '**Desktop publishing** — computer systems with special features producing '
          'professionally-printed-looking documents, combining text, art and a variety of '
          'fonts.',
          '**Electronic mail** — technologies for sending messages/documents between '
          'electronic workstations; business uses include facsimile, voice mail and '
          'electronic mailboxes.',
          '**Teleconferencing and audio conferencing** — holding meetings among people at '
          'physically different sites (video and audio teleconferencing), letting work happen '
          'from home or other sites.',
          '**Desktop organizers** — software packages providing the electronic equivalent of '
          'office desk tools: calendar, card file, notepad, clock, calculator.',
          '**Archival storage** — off-line storage for historical/long-term materials, using '
          'technologies like magnetic tape and Computer Output on Microfilm/microfiche '
          '(COM).']},
        {'h4': '(c) Adverse effects on office workers (any two)'},
        {'ul': ['Possible harmful effects/danger of display devices (e.g. monitors) to '
          'users\' eyes.', 'Strain on the body (e.g. back pain) from long sitting to operate '
          'the computer system.', 'Reduction in the number of office workers.', 'Reduction in '
          'retirement age.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 10 — units, public-key encryption, websites', 'open': True,
      'q': [
        {'p': '(a) The following are some common units used in a computing environment: '
              'Byte, Hertz, Baud and MIPS. Explain each of these units and what they are used '
              'to quantify.'},
        {'p': '(b) Briefly describe the operation of public key encryption.'},
        {'p': '(c)(i) What is a website? (ii) Give any two reasons why a business '
              'organisation may choose to develop and maintain a website.'}],
      'a': [
        {'h4': '(a) Units'},
        {'ul': [
          '**Byte** — a sequence of bits forming a character; in ASCII, 1 byte = 7 bits, '
          'though the usual definition (EBCDIC) is 1 byte = 8 bits. A unit of measurement for '
          'computer main memory or any storage medium.',
          '**Hertz** — the number of pulses or cycles per second; a measure of processor '
          'speed.',
          '**Baud** — the number of bits of data that can be transmitted along a '
          'communication line in one second; a unit of data-transmission speed.',
          '**MIPS** — Million Instructions Per Second; measures the number of instructions '
          'processed per second for a given processor type.']},
        {'p': '(b) **Public key encryption** uses two different keys — one private and one '
              'public. The public key is used by the sender to encode the message; the '
              'private (secret) key is used by the recipient to unscramble it. The sender '
              'locates the recipient\'s public key and encrypts the message with it; on '
              'receipt, the recipient uses their private key to decrypt it.'},
        {'p': '(c)(i) A **website** is a place on the internet where an individual, company or '
              'organisation has information about itself.'},
        {'h4': '(c)(ii) Reasons for a business website (any two)'},
        {'ul': ['To sell or market products and services.', 'To advertise products and '
          'services.', 'To promote corporate image.', 'To provide information about itself.',
          'To reach out to several people simultaneously.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 11 — input devices vs the keyboard', 'open': True,
      'q': [{'p': 'The keyboard is the most widely used input device for the microcomputer. '
                  'Give other input devices and state one advantage of each over the '
                  'keyboard.'}],
      'a': [{'ul': [
        '**Mouse** — used in a Windows environment on the VDU; a better means of controlling '
        'a cursor than the keyboard, e.g. on a spreadsheet.',
        '**Voice data entry** — uses a voice recognition unit recognising a limited number of '
        'keyboard strokes; advantageous to blind people who cannot operate a keyboard; also '
        'used in home banking systems and air traffic control systems.',
        '**Touch screens** — touch-sensitive screens built onto a normal VDU, transmitting '
        'messages depending on which part is touched; used in manufacturing and stock '
        'control operations.',
        '**Magnetic stripe cards** — input via a magnetic card reader; used in banking, e.g. '
        'ATMs.',
        '**Document readers** (MICR, OMR, OCR) — MICR is used in banking for cheque clearing; '
        'OMR is used by examination bodies for multiple-choice questions; OCR is used on '
        'turnaround documents such as credit card invoices.']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 12 — Big Data, the six Vs and its benefits', 'open': True,
      'q': [
        {'p': '(a) What is Big Data? (2 marks)'},
        {'p': '(b) Describe the SIX Vs of Big Data. (9 marks)'},
        {'p': '(c) What are the benefits of Big Data? (9 marks) — Total 20 marks'}],
      'a': [
        {'p': '(a) Big Data is extremely large data sets that may be analysed computationally '
              'to reveal patterns, trends and associations, especially relating to human '
              'behaviour and interactions — also defined as data containing greater variety, '
              'arriving in increasing volumes and with more velocity.'},
        {'h4': '(b) The six Vs of Big Data'},
        {'ul': [
          '**Volume** — the large amount of data from many environments.',
          '**Variety** — the wide variety of data types frequently stored in big data '
          'systems.',
          '**Velocity** — the speed at which data is generated, collected and processed.',
          '**Value** — the worth of the information to the company, determined by its '
          'relevance.',
          '**Veracity** — the accuracy of the data, determining its reliability.',
          '**Variability** — the rate of change in the structure of the data.']},
        {'h4': '(c) Benefits of Big Data'},
        {'p': 'Companies use big data to: improve operations; provide better customer service '
              'by following customer-behaviour trends more closely and accurately; create '
              'personalised marketing campaigns from more comprehensive knowledge of customer '
              'behaviour; take actions that ultimately increase revenue and profits; and gain '
              'competitive advantage by making faster, more informed business decisions.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 13 — disruptive technologies and AI', 'open': True,
      'q': [
        {'p': '(a) Describe disruptive technologies.'},
        {'p': '(b) Why are they important?'},
        {'p': '(c) State FIVE examples of disruptive technologies.'},
        {'p': '(d) What is artificial intelligence (AI)?'},
        {'p': '(e) What are the factors encouraging the adoption of AI?'},
        {'p': '(f) What is adaptive intelligence?'}],
      'a': [
        {'p': '(a) **Disruptive technology** is an innovation that significantly alters the '
              'way consumers, industries or businesses operate; it sweeps away the systems or '
              'habits it replaces because it has recognisably superior attributes.'},
        {'h4': '(b) Why they are important'},
        {'ul': ['They affect the way we live, work and earn income.', 'They change the '
          'structure of industries and economies.', 'They render some old technologies '
          'redundant.']},
        {'h4': '(c) Examples (any five)'},
        {'p': 'Artificial intelligence and machine learning; Internet of Things; distributed '
              'ledgers/blockchain technology; computer robotics and business automation; '
              'drone technology; e-commerce; online news sites; ride-sharing apps; GPS '
              'systems; the automobile; electricity service; television.'},
        {'p': '(d) **Artificial intelligence** refers to systems or machines that mimic human '
              'intelligence to perform tasks and can iteratively improve themselves based on '
              'the information they collect — a wide-ranging branch of computer science '
              'concerned with building smart machines capable of performing tasks that '
              'typically require human intelligence; intelligence demonstrated by machines, '
              'as opposed to the natural intelligence of animals including humans.'},
        {'h4': '(e) Factors driving AI adoption'},
        {'ol': [
          'Affordable, high-performance computing capability is readily available (cloud '
          'compute power, versus the earlier cost-prohibitive non-cloud environments).',
          'Large volumes of data are available for training, aided by tools for labelling '
          'data and easier storage/processing of structured and unstructured data.',
          'Applied AI delivers a competitive advantage, e.g. via faster, better-informed '
          'business decisions, lower costs, reduced risks and faster time to market.']},
        {'p': '(f) **Adaptive intelligence** is a new term evolving from Artificial '
              'Intelligence: applications that help enterprises make better business '
              'decisions by combining real-time internal and external data with decision '
              'science and highly scalable computing infrastructure, making the business '
              'smarter and enabling better products, recommendations and services.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 14 — IoT and its areas of application', 'open': True,
      'q': [
        {'p': '(a) What is the Internet of Things (IoT)?'},
        {'p': '(b) Discuss any SIX areas of application of IoT.'}],
      'a': [
        {'p': '(a) The **Internet of Things (IoT)** describes physical objects (or groups of '
              'such objects) with sensors, processing ability, software and other '
              'technologies, that connect and exchange data with other devices and systems '
              'over the internet or other communications networks.'},
        {'h4': '(b) Areas of application (any six)'},
        {'ul': [
          '**Consumer applications** — connected vehicles, home automation/smart homes, '
          'wearable technology, connected health.',
          '**Medical and healthcare** — the Internet of Medical Things (IoMT): remote health '
          'monitoring, emergency notification systems, wearable heart monitors, point-of-care '
          'diagnostics; managing chronic diseases and disease prevention/control.',
          '**Transportation** — smart traffic control, smart parking, electronic toll '
          'collection, logistics/fleet management, vehicle control, and vehicle-to-everything '
          '(V2X: V2V, V2I, V2P) communication.',
          '**Building and home automation** — monitoring/controlling mechanical, electrical '
          'and electronic building systems.',
          '**Industrial applications (IIoT)** and **manufacturing** — network control of '
          'equipment, asset/situation management, process control, predictive maintenance, '
          'and smart-grid energy optimisation.',
          '**Agriculture** — collecting temperature, rainfall, humidity, wind speed, pest and '
          'soil data, to automate farming and reduce risk/waste.',
          '**Maritime** — monitoring unattended boats/yachts for flooding, fire or battery '
          'discharge.',
          '**Infrastructure applications** — monitoring bridges/railway tracks; metropolitan-'
          'scale smart cities (e.g. Songdo, South Korea); energy management; environmental '
          'monitoring.',
          '**Military applications** — the Internet of Military Things (IoMT), the Internet '
          'of Battlefield Things (IoBT), and the Ocean of Things project.',
          '**Product digitalization** — QR codes/NFC tags on packaging linking to digital '
          'content ("Internet of Packaging").']}]}},
    {'eg': {'tag': 'Study text', 't': 'Question 15 — distributed ledgers, blockchain and cryptocurrency', 'open': True,
      'q': [
        {'p': '(a) What are distributed ledgers?'},
        {'p': '(b) Describe FOUR benefits of distributed ledgers.'},
        {'p': '(c) Describe FOUR fields of a blockchain.'},
        {'p': '(d) Describe FOUR features of a blockchain.'},
        {'p': '(e) Describe a cryptocurrency.'},
        {'p': '(f) State FIVE examples of cryptocurrency.'}],
      'a': [
        {'p': '(a) **Distributed ledgers** are databases shared across a network and spread '
              'over various geographical locations — held and reorganized by multiple parties '
              'in different locations and institutions.'},
        {'h4': '(b) Benefits of distributed ledgers'},
        {'ol': [
          'Highly transparent, secure, tamper-proof and immutable — records cannot be altered '
          'once written, since entries happen without third-party involvement.',
          'The need for a third party is eliminated, saving money, effort and time.',
          'Inherently decentralized — spread globally, adding a layer of security.',
          'Highly transparent — all stored information is freely and easily viewable.']},
        {'h4': '(c) Four fields of a blockchain block'},
        {'ul': [
          '**Previous hash** — stores the hash of the previous block in the blockchain.',
          '**Transaction details** — information on several transactions.',
          '**Nonce** — a random value acting as a variate for the hash value.',
          '**Hash address** — the block\'s unique identification: a 64-character hex value, '
          'letters and numbers, obtained via the SHA-256 algorithm.']},
        {'h4': '(d) Four features of blockchain'},
        {'ul': [
          'It is a public distributed ledger, working via hashing encryption.',
          'Every block has a hash value — the digital signature of the block.',
          'Transactions are approved and verified using a proof-of-work consensus algorithm.',
          'The network utilises the resources of miners, who validate transactions for '
          'rewards.']},
        {'p': '(e) A **cryptocurrency** is a form of digital currency used to verify the '
              'transfer of assets, control the addition of new units, and secure financial '
              'transactions using cryptography.'},
        {'p': '(f) Examples: **Bitcoin, Litecoin, Ethereum, Z Cash, Dash, Ripple, Monero, NEM, '
              'Stellar** (any five).'}]}},
  ]},
 ],
 'formulas': [
   {'lb': 'Cost-benefit (profitability) ratio', 'tex': '\\text{Cost-benefit ratio} = \\dfrac{\\text{NPV}}{\\text{Initial outlay}}', 'nt': 'Used instead of NPV alone when cash is a constraint; also called the profitability index, or NPV per ₦ initial outlay.'},
 ],
 'focus':
   'The examiner tests the SDLC stages and the four changeover strategies (direct, parallel, '
   'pilot [retrospective/restricted data], staged) as "which changeover is this" scenarios — '
   'learn what distinguishes each. Know NPV vs IRR vs payback vs cost-benefit ratio cold, and '
   'the four feasibility criteria (technical/operational/social/economic). For the second half '
   'of the chapter, fix one distinguishing fact per disruptive technology (AI vs machine '
   'learning vs adaptive intelligence; distributed ledger vs blockchain vs cryptocurrency; '
   'IoT\'s three architecture tiers; robotics vs automation) since MCQs test them as pairs '
   'the examiner expects you to confuse.',
 'errors': [
   'Confusing parallel running (both systems run current data concurrently) with '
   'retrospective parallel running (the new system reruns data the old system already '
   'processed) — the second is faster to apply precisely because it avoids double staffing.',
   'Treating restricted data running and staged/phased changeover as the same thing — '
   'restricted data running implements part of the *whole* system piecemeal; staged '
   'changeover implements the *entire new system* in stages.',
   'Saying a positive NPV means a project should be rejected — a positive NPV means the '
   'project is feasible; zero NPV is break-even (should not be undertaken); negative NPV is '
   'infeasible.',
   'Using "blockchain" and "distributed ledger technology" interchangeably — blockchain is '
   'one particular (permissionless, block-chained) type of distributed ledger technology, not '
   'a synonym for the whole category.',
   'Confusing a computer virus (a code segment hidden in a host program, needing the host to '
   'run) with a worm (a standalone program that copies itself without needing a host program '
   'or human action).',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In the Systems Development Life Cycle, the stage where the analyst breaks the '
         'design process into "milestones" and requires a formal sign-off from users at each '
         'one before proceeding is called',
    'o': ['Systems investigation', 'System analysis', 'Design reviews and walkthroughs '
          '(user validation)', 'Post-implementation review', 'Systems definition'],
    'a': 2,
    'w': 'Design reviews and walkthroughs (user validation) break system design into '
         'milestones with deliverables that users must formally sign off before the next '
         'stage begins.',
    'src': 'Chapter 6.1(f)', 'sec': '6.1'},
   {'q': 'A changeover in which the new system is run on data previously processed by the '
         'old system, so existing results are available for comparison without the staffing '
         'burden of true parallel running, is called',
    'o': ['Direct changeover', 'Parallel running', 'Retrospective parallel running',
          'Staged/phased changeover', 'Restricted data running'],
    'a': 2,
    'w': 'Retrospective parallel running reruns the new system on data the old system already '
         'processed, avoiding the disruption of running both systems on live current data at '
         'once.',
    'src': 'Chapter 6.1, pilot operation', 'sec': '6.1'},
   {'q': 'Which discounted cash flow measure compares a project\'s own expected rate of '
         'return with the cost of capital, accepting the project only if its value exceeds '
         'that rate?',
    'o': ['Payback period', 'Net Present Value (NPV)', 'Internal Rate of Return (IRR)',
          'Cost-benefit ratio', 'Break-even analysis'],
    'a': 2,
    'w': 'IRR is the discounted rate of return the project itself generates; it is worth '
         'undertaking only if that IRR exceeds the cost of capital. NPV instead expresses the '
         'result in currency terms, discounted at the cost of capital.',
    'src': 'Chapter 6.1, cost-benefit analysis', 'sec': '6.1'},
   {'q': 'A type of outsourcing where an organisation outsources more than 70% of its IS '
         'capability to a single vendor is called',
    'o': ['Body shop outsourcing', 'Project management outsourcing', 'Total outsourcing',
          'Facilities management', 'Joint Application Development'],
    'a': 2,
    'w': 'Total outsourcing is specifically defined by that 70% threshold to a single vendor; '
         'body shop outsourcing meets short-term IS/IT demand, and project management '
         'outsourcing covers all or part of one project.',
    'src': 'Chapter 6.7.1', 'sec': '6.7'},
   {'q': 'A malicious program that copies itself repeatedly into memory or a medium until no '
         'space is left, and does not need to hide inside a host program, is a',
    'o': ['Virus', 'Worm', 'Trojan Horse', 'Logic bomb', 'Time bomb'],
    'a': 1,
    'w': 'A worm is a standalone program (unlike a virus, which is a code segment hidden in a '
         'host program) that replicates itself and typically releases a "payload" once memory '
         'or a medium is filled.',
    'src': 'Chapter 6.8, computer viruses and worms', 'sec': '6.8'},
   {'q': 'A blockchain\'s "nonce" field is best described as',
    'o': ['The hash of the previous block', 'Information on several transactions',
          'A random value acting as a variate for the hash value',
          'The block\'s unique 64-character hash address', 'The digital signature of the '
          'block\'s owner'],
    'a': 2,
    'w': 'Every block has four fields: previous hash, transaction details, nonce (a random '
         'value varying the hash computation) and hash address (the unique SHA-256 '
         'identifier).',
    'src': 'Chapter 6.16, fields of a blockchain block', 'sec': '6.16'},
  ],
  'theory': [
   {'q': 'Describe the four criteria a project must satisfy to be judged feasible, with one '
         'illustrative consideration under each.',
    'marks': 8,
    'a': [
      {'ul': [
        '**Technical feasibility** — achievable with available hardware/software, considering '
        'transaction volumes, storage capacity, response times and number of users.',
        '**Operational feasibility** — must not create inefficiency; operational changes must '
        'enhance business objectives.',
        '**Social feasibility** — personnel problems, job enrichment, industrial relations, '
        'skills requirements, motivation, social/environmental impact.',
        '**Economic feasibility** — must be a good investment able to recover its outlay and '
        'realise profits.']}],
    'src': 'Chapter 6.1, criteria for project selection', 'sec': '6.1'},
   {'q': 'Distinguish direct changeover, parallel running, pilot operation and staged/phased '
         'changeover, stating one condition favouring each.',
    'marks': 12,
    'a': [
      {'ul': [
        '**Direct changeover** — the old system is suddenly replaced; favoured where the new '
        'system succeeded previously in a similar situation, or no extra staff exist for '
        'parallel running.',
        '**Parallel running** — both systems run concurrently on current data, checked for '
        'consistency; favoured when maximum safety is wanted despite the cost of duplicated '
        'effort.',
        '**Pilot operation** — cheaper/easier to control than parallel running: either '
        'retrospective parallel running (rerunning old data) or restricted data running (one '
        'logical part transferred first); favoured for moderate risk with lower disruption.',
        '**Staged/phased changeover** — the first stage uses the parallel approach, then a '
        'series of direct changeovers; favoured for very large or complex projects.']}],
    'src': 'Chapter 6.1, changeover', 'sec': '6.1'},
   {'q': 'Explain the difference between artificial intelligence, machine learning and '
         'adaptive intelligence.',
    'marks': 9,
    'a': [
      {'p': '**Artificial intelligence (AI)** is the broad field of building machines that '
            'mimic human intelligence to perform tasks and improve themselves from '
            'information collected. **Machine learning** is a data-analytics technique within '
            'AI, teaching computers to learn directly from data (via supervised or '
            'unsupervised methods) rather than a predetermined equation. **Adaptive '
            'intelligence** is a newer, more applied term for AI-based applications that '
            'combine real-time internal and external data with decision science and scalable '
            'computing infrastructure specifically to make business decisions smarter.'}],
    'src': 'Chapter 6.13', 'sec': '6.13'},
   {'q': 'State the three tiers of an IoT system architecture and the role of each.',
    'marks': 6,
    'a': [
      {'ul': [
        '**Tier 1 — Devices** — networked sensors/actuators using protocols like Modbus, '
        'Bluetooth or Zigbee, connecting to an Edge Gateway.',
        '**Tier 2 — The Edge Gateway** — aggregates sensor data, pre-processes it, and '
        'secures connectivity to the cloud, giving upper layers a common device view.',
        '**Tier 3 — The Cloud** — the IoT application itself (secured via HTTPS/OAuth), with '
        'database systems for sensor data and an event queuing/messaging system for cross-'
        'tier communication.']}],
    'src': 'Chapter 6.14.2', 'sec': '6.14'},
   {'q': 'Distinguish blockchain from distributed ledger technology, and state any THREE '
         'features of blockchain.',
    'marks': 10,
    'a': [
      {'p': 'Blockchain and distributed ledger technology are often used interchangeably but '
            'differ: blockchain is one particular type of distributed ledger technology, using '
            'cryptography and chaining data into blocks that can only be added to, never '
            'edited; it is usually public and permissionless. Distributed ledger technology '
            'more broadly need not use chains of blocks, can be public or private and '
            'permissioned or permissionless, and typically restricts who may be a node.'},
      {'h4': 'Features of blockchain (any three)'},
      {'ul': [
        'A public distributed ledger, working via hashing encryption.',
        'Every block has a hash value — its digital signature.',
        'Transactions are verified using a proof-of-work consensus algorithm.',
        'The network relies on miners, who validate transactions for rewards.']}],
    'src': 'Chapter 6.15.5, 6.16.2', 'sec': '6.15'},
  ]},
}
