CH = {
 'n': 3,
 't': 'Computer Software',
 'brief': 'System software (the operating system and its companions), application software '
          'and packages, the five generations of computer language, grid computing, and '
          'working in Microsoft Windows.',
 'outcomes': [
   'Distinguish system software from application software',
   'Describe the categories of system software and the functions of an operating system',
   'Distinguish assemblers, compilers and interpreters, and state their advantages',
   'Describe multi-user, multi-tasking, multi-programming and multi-processing environments',
   'Describe the types, sources and selection criteria for application packages',
   'Describe the five generations of computer language, with examples of each',
   'Describe grid computing, its types, applications and limitations',
   'Carry out basic Windows operations and use Windows Explorer',
 ],
 'secs': [
  {'n': '3.1', 't': 'Computer software', 'b': [
    {'p': 'Software is the suite of programs that allows the hardware to function optimally '
          'and lets the end-user interact with the hardware. **System software** is produced '
          'by the computer manufacturer, while **application packages** are acquired from '
          'many sources; they may be **off-the-shelf** or **bespoke**, and are intended for '
          'specific tasks. The most important system software is the **Operating System '
          '(OS)**. There are operating systems for various tasks/processes — single-user, '
          'multiprocessing, multiprogramming, distributed processing and multiuser.'},
    {'def': {'t': 'Software', 'd': 'a generic term for all computer programs that run on the '
                  'hardware system, and their accompanying documentation — the complete set '
                  'of instructions that enables users to perform tasks with the computer '
                  'system. Computer programs divide into **Systems Software** and '
                  '**Applications Software** (application packages).'}},
    {'def': {'t': 'Computer program', 'd': 'a sequence of instructions to solve a particular '
                  'problem, written in a particular computer language.'}},
  ]},

  {'n': '3.2', 't': 'System software', 'b': [
    {'p': 'Background programs that enable application software to run smoothly on a specific '
          'set of hardware. System software forms an **interface between application programs '
          'and the hardware system**, and provides a suitable environment for writing, '
          'editing, debugging, testing and running users\' programs. Most system software '
          'comes with the computer system and is often called **bundled software**. Types of '
          'system software: **operating system**; **language processor**; **utility '
          'routines**; **loaders**; **editors**.'},
    {'h3': '3.2.1 Operating System (OS)'},
    {'def': {'t': 'Operating System', 'd': 'a collection of programs that manages the '
                  'Computer Based Information System (CBIS) resources in the wisest manner '
                  'possible, giving the user features that make it easier to code, test, '
                  'execute, debug and maintain programs while efficiently managing the '
                  'hardware resources. It is the fundamental software that manages a '
                  'computer\'s hardware and software resources, providing a platform for '
                  'applications to run, and acts as an intermediary between the user and the '
                  'hardware.'}},
    {'p': 'Functions of the OS:'},
    {'ol': [
      'Resource sharing.',
      'Provision of a **virtual machine** — virtual storage is an interleaving technique in '
      'which disc storage is made to operate as a logical extension of RAM.',
      'Input and output (I/O) handling.',
      'Memory management.',
      'Filing system.',
      'Protection and error handling.',
      'Program control.',
      'Initial set-up of the computer when switched on, achieved by the **boot(strap) '
      'program**, normally resident in ROM, which loads the rest of the OS from secondary '
      'storage into RAM.',
    ]},
    {'p': 'Main components of an operating system: (i) a **supervisor**; (ii) a **command '
          'language translator**; (iii) an **Input/Output Control System (IOCS)**; '
          '(iv) a **librarian**.'},
    {'table': {'cap': 'Examples of operating systems', 'align': 'll', 'head': ['OS', 'Notes'],
      'rows': [
      ['**DOS** (Disk Operating System)', 'Used on stand-alone microcomputers: **MS-DOS**, '
       '**PC-DOS** (IBM-PC and compatibles). Limitations: cannot be used for multi-tasking; '
       'not suited to networking activities.'],
      ['**Windows**', 'Offers a full Graphical User Interface (GUI), simplifying DOS commands.'],
      ['**OS/2**', 'Used with the IBM PS/2 line of microcomputers; allows multitasking using '
       'a GUI.'],
      ['**Unix**', 'A multi-user, multi-tasking OS used on micros and minis; **Xenix** and '
       '**Venix** are variants of Unix.'],
      ['**MVS, VM**', 'Used with IBM mainframes.'],
      ["**Novell's Netware**", 'A network OS.'],
      ['**Windows NT**', 'Improves on Windows by also offering multitasking.'],
    ]}},
    {'h4': 'Classifications of operating system'},
    {'ul': [
      '**Single-user OS** — designed for one user at a time: only one user can be logged in '
      'and access the system\'s resources and applications at any given moment. Typically on '
      'personal computers, laptops, smartphones. Examples: Windows, Mac OS, Linux (on desktop '
      'systems). Key characteristics: limited user accounts; single tasking; user-friendly '
      'interface; personalised experience.',
      '**Multi-user OS** — allows multiple users on different computers to access a single '
      'system\'s OS resources simultaneously, running programs, executing commands and using '
      'resources concurrently, typically via networked terminals. Key features: resource '
      'allocation and management (CPU time, memory, storage); security features against '
      'unauthorised access; **time-sharing** to allocate CPU time to each user; multiple users '
      'accessing the same system at the same time.',
      '**Multiprocessing OS** — uses two or more CPUs to control a computer\'s functions, '
      'enabling simultaneous execution of different parts of a program by different '
      'processors, enhancing speed and efficiency. Examples: Windows and Linux.',
      '**Multitasking OS** — allows a computer to run multiple programs/processes '
      'concurrently (they appear to run simultaneously), by rapidly switching between tasks '
      'and allocating resources to each. Key features: concurrency; resource management; '
      'scheduling; context switching; user interface. Examples: all Windows versions, Mac OS, '
      'Linux (and distributions), Android, iOS.',
      '**Networking OS** — manages and controls the resources of a computer network, letting '
      'users and devices share files, printers and other resources; the core system of a '
      'server, facilitating communication and resource sharing among connected devices. '
      'Example: Microsoft Windows Server. Others: UNIX/LINUX, Cisco IOS, Junos OS, '
      'VMware NSX. It integrates all the network\'s components and lets multiple users share '
      'the same resources irrespective of physical location.',
      '**Windows-based OS** — a Microsoft program that manages a computer\'s resources and '
      'lets users interact with hardware and software via a GUI (icons, windows, menus). '
      'Types: Windows 11, 10, 8, 7, Vista, XP, 2000, etc.',
      '**Mobile OS** — lets mobile devices (smartphones, tablets, wearables) run applications '
      'and programs; interfaces between the device\'s hardware and software, manages cellular '
      'and wireless connectivity and enables phone access. Examples: Android, iOS, iPhone OS.',
      '**Cloud OS** — manages and delivers cloud-based services and resources, coordinating '
      'storage, computing power and networking so they work together seamlessly. Examples: '
      'Amazon Web Services, Microsoft Azure, Google Cloud Platform.',
    ]},
    {'h3': '3.2.2 Bootstrap program'},
    {'p': 'Part of the executive program of the OS, resident in the computer\'s memory, used to '
          'start up the computer. When switched on, the computer must bring some of its '
          'controlling software into main memory from secondary storage, after which the OS '
          'takes over supervision of the computer\'s operations — the **bootstrap** is the '
          'program that calls in the software that makes the computer operational.'},
    {'h3': '3.2.3 Utility programs'},
    {'p': 'Also called **service** or **general-purpose programs**, used for applications in '
          'general regardless of the nature of specific application programs. They perform: '
          '(a) file copy; (b) file re-organisation; (c) file maintenance; (d) sorting; '
          '(e) **dumping routines** — transfer a working program/data into secondary storage '
          'at regular intervals, from where it can be reloaded using a restart program; '
          '(f) **housekeeping operations** — clearing areas of storage, writing file labels, '
          'updating common data; (g) conversion of programs in ASCII code into EBCDIC code; '
          '(h) disk copying and formatting.'},
    {'h3': '3.2.4 Loader'},
    {'p': 'Before an instruction can be executed, it must be placed somewhere in the primary '
          'memory. The **loader** places the program segments into the appropriate locations '
          'in memory, ready for execution. The output from the linkage editor during program '
          'compilation is usually the input to the loader.'},
    {'h3': '3.2.5 Editors'},
    {'p': 'An editor converts input into a particular format of output, based on editing '
          'commands accompanying the input; most editors work on the source program, letting '
          'the user format, delete, insert or modify all or part of a file. Two types:'},
    {'ul': [
      '**Text editor** — a utility program closely associated with application packages, used '
      'for cutting and pasting programs together, changing data files by editing data fields, '
      'or changing the format of data. Not a word processor (which is designed specifically to '
      'prepare documents such as letters and reports); a text editor lacks extensive '
      'text-formatting and document-printing capabilities.',
      '**Linkage editor** — a more important editor; a piece of system software that works on '
      '**object programs** (during program compilation), resolving undefined references, '
      'linking together several object programs that must work together, and reassigning all '
      'relocatable addresses.',
    ]},
    {'h3': '3.2.6 Language processor'},
    {'def': {'t': 'Language processor (language translator)', 'd': 'a program that converts '
                  'the user\'s code (**source code**) into machine language code (**object '
                  'code**).'}},
    {'p': 'A computer can only process data in binary form (a string of 0 and 1) — the '
          '**machine code** — which is very difficult for people to write directly. Users '
          'write in a familiar language (source code), which a language processor converts to '
          'machine code before processing. The three most popular language processors are the '
          '**Assembler**, the **Compiler** and the **Interpreter**.'},
    {'ul': [
      '**Assemblers** — translate a source program written in **low-level (assembly) '
      'language** into the machine code/object program; the translation is performed by the '
      'computer itself. Purpose: to simplify and speed up programming, letting the programmer '
      'write in a language simpler than machine code. After translation, the **linkage '
      'editor** binds the object codes into a **load program**, which the processor executes. '
      'Programs may be saved as a source program, object program, or load program.',
      '**Compilers** — convert a source program written in a **high-level language** into a '
      'machine code/object program, all at once, before the program is run; more complex than '
      'assembling, but done for the same reason — to reduce the complexity and time of writing '
      'programs.',
      '**Interpreters** — also convert high-level language into machine code, but unlike '
      'compilers, they convert the program **a line at a time, as it is being run**; each '
      'statement is converted into machine language just before execution, and **no object '
      'code is ever produced**. The BASIC language uses an interpreter.',
    ]},
    {'table': {'cap': 'Advantages and disadvantages of interpreters over compilers',
      'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Fast and easier to use — no distinct, time-consuming compilation process',
       'It takes a longer time for a program to run'],
      ['Produce superior error messages that are easy to trace',
       'Since it does not compile, when the program is re-run it must be interpreted all over '
       'again'],
      ['Require less RAM space than compilers — usable in limited-memory environments', ''],
      ['Cheaper', ''],
      ['Suitable for interactive work — the programmer can test/amend the program on-line in '
       'segments, seeing results immediately', ''],
      ['Very useful for writing small programs', ''],
    ]}},
    {'note': 'Many small computers now have compilers, so a program need only be translated '
             'once (during compilation) and then stored on secondary storage until run — and '
             'because each statement is not translated at run-time, a compiled program runs '
             'faster than an interpreted one.'},
  ]},

  {'n': '3.3', 't': 'Associated phenomena', 'b': [
    {'p': 'Some phenomena associated with system software:'},
    {'h3': '3.3.1 Multi-user application'},
    {'p': '**Multi-user (time-sharing) application** allows a number of users in different '
          'departments to process their own particular requirements on an online basis, '
          'allocating each terminal user several small, fixed slices of time as their jobs are '
          'processed — the computer works so quickly that each user feels they have exclusive '
          'use of the system. It requires:'},
    {'ol': [
      'terminal controllers, for controlling the operations of groups of terminals;',
      'if terminals are remote: MODEMs (Modulator-Demodulator), multiplexors, and a '
      'front-end processor;',
      'private leased communication lines;',
      'a powerful processor to support the multi-user environment — capable of polling the '
      'lines to allocate time slots (time slices) to each terminal;',
      'large memory capacity for storing user programs, plus the high overhead needed to '
      'store the OS (overhead = the area of primary memory inaccessible to the user);',
      'protection features to prevent a system crash when several users process the same '
      'file simultaneously;',
      'record/file locking and unlocking facilities, to prevent a record/file being updated '
      'by another user.',
    ]},
    {'p': 'Individual terminals in a multi-user system cannot communicate with one another — '
          'unnecessary, since they share common files. A major disadvantage: if a terminal\'s '
          'connecting cable is severed, it becomes inoperative, having no link to the central '
          'computer (server). Networking (distributive) is an advantage here, because a '
          'microcomputer disconnected from the network can still continue to process.'},
    {'h3': '3.3.2 Multi-tasking environment'},
    {'p': 'The ability of a microcomputer OS to execute a user\'s tasks concurrently — e.g. '
          'printing a word-processed document while typing.'},
    {'h3': '3.3.3 Multi-programming environment'},
    {'p': 'A process whereby a mainframe computer works on several programs concurrently: '
          'since a single computer can do only one operation at a time, it works on one '
          'program for a while, then switches to another — keeping the CPU busy.'},
    {'key': '**Time-sharing (multi-user) differs from multi-programming**: in time-sharing, a '
            'predetermined time slice is given to each user; in multi-programming, the time '
            'slice is determined by the I/O interrupts logically encountered in each program.'},
    {'h3': '3.3.4 Multiprocessing environment'},
    {'p': '**Multiprocessing (parallel processing)** — the use of several CPUs (processors) '
          'linked together to perform coordinated work at the same time. (In multi-programming, '
          'only one processor is involved.)'},
    {'h3': '3.3.5 Spooling'},
    {'def': {'t': 'Spooling', 'd': 'because I/O devices are slow, jobs are batched to input '
                  'devices which store their contents on a magnetic disk (whose speed is close '
                  'to that of the processor), later fed into the CPU. Results are likewise '
                  'transformed to magnetic disk, which later transfers them to a printer. This '
                  'method — batching inputs and placing them on a magnetic medium, and queuing '
                  'the output on the same magnetic medium — is called spooling.'}},
    {'h3': '3.3.6 Virtual memory capability'},
    {'p': 'In a virtual memory system, the OS continually moves data back and forth between '
          'primary and secondary memory, so that the system appears to have a virtually '
          'unlimited amount of primary memory.'},
  ]},

  {'n': '3.4', 't': 'Application software', 'b': [
    {'p': 'Written to perform specific functions and support users. Divides into **User '
          'Application Programs** and **Application Packages** (used by specialists, and for '
          'generalised purposes).'},
    {'h3': '3.4.1 User application programs / in-house application packages'},
    {'p': 'Focused on expanding the role of the computer beyond traditional tasks. Examples: '
          '**Decision Support Systems (DSS)**, **Expert Systems (ES)**, **Artificial '
          'Intelligence (AI)**.'},
    {'h3': '3.4.2 Application packages'},
    {'def': {'t': 'Application package', 'd': 'a pre-written computer program widely used for '
                  'a specific application, avoiding unnecessary duplication of similar '
                  'programs by many users. It carries out specific tasks for the user, as '
                  'opposed to system software, which controls the working of a computer.'}},
    {'p': 'A package consists of a suite of programs and documentation — a program/system '
          'manual (details of how to set it up and run it), the medium on which it is stored, '
          'input/output formats and file layouts, a user instruction manual, the minimum RAM '
          'capacity required, and details of how the package may be varied to suit '
          'individual needs. Some packages need a specific make of computer, a minimum memory '
          'capacity, or a specific OS such as Windows.'},
    {'ul': [
      '**Bespoke software** — packages written in-house by an organisation\'s own programmers '
      'to meet a specific process — tailored to a specific need.',
      '**Off-the-shelf software** — bought for general use; can still be tailored to specific '
      'use by the vendor or the end-user.',
    ]},
    {'h4': 'Examples of application packages on microcomputers'},
    {'ul': [
      '**Electronic spreadsheets** — Excel, Multiplan, PC-focals, Professional Plan, Quattro, '
      'Supercalc, Lotus 1-2-3, SUN. These turn the computer into a sophisticated electronic '
      'calculator, presenting data in rows and columns, letting the user decide how data is '
      'displayed and manipulated on the grid; they include presentation-graphic generators for '
      'management presentations, and are used mainly for accounting purposes.',
      '**Word-processing packages** — WordStar, WordPerfect for Windows, DisplayWrite, '
      'MS-Word, MultiMate, Professional Write. These turn the computer into a powerful '
      'typewriting tool, offering special type fonts; menu-driven, executing commands such as '
      'PRINT, SAVE, SAVE AS, EXIT; facilities for formatting document pages (margin '
      'justification, underlining, deleting, highlighting, pasting paragraphs); some include '
      'desktop publishing, electronic calendaring and mail.',
      '**File Manager and Database Management Systems (DBMS)** — dBase, Rbase, Reflex, Oracle '
      'Database, Microsoft SQL Server, MySQL, PostgreSQL, Apache Cassandra.',
      '**Graphics generators** — used to quickly construct line charts, bar charts, pie '
      'charts, histograms and scatter diagrams; usually bundled as adjunct routines with '
      'packages like spreadsheets and reporting packages.',
      '**Desktop publishing (DTP)** — CorelDraw, Adobe PageMaker, PowerPoint. Uses '
      'microcomputer systems with special hardware and software features to produce documents '
      'looking as though produced by a professional print shop, combining word-processed text '
      'with artwork, photographs and magazine-style fonts.',
      '**Statistical packages** — used for analysing statistical data to aid management '
      'decisions; one important example is **SPSS** (Statistical Package for Social Sciences).',
      '**Mathematical packages** — used in mathematical modelling, e.g. systems of linear '
      'equations, differential equations, symmetries, and numerical solutions of such models. '
      'Examples: Mathematica, MATLAB.',
    ]},
    {'def': {'t': 'Database', 'd': 'a collection of data files, integrated and organised to '
                  'provide a single comprehensive file system. The data is governed by rules '
                  'defining its structure and how it can be accessed; the purpose of a database '
                  'is to provide convenient access to common data for a wide variety of users '
                  'and needs.'}},
    {'def': {'t': 'Database Management System (DBMS)', 'd': 'the software that builds, '
                  'manages and provides access to a database — a systematic approach to '
                  'storing and retrieving data, designed to store large amounts of data, '
                  'provide rapid access to it, and prepare reports from it.'}},
    {'p': 'A database system is used to: avoid data duplication (redundancy), by allowing a '
          'single item of data to be used in a number of applications; make data independent '
          'of the programs that use it; ensure consistency in an organisation\'s use of data.'},
    {'def': {'t': 'File manager', 'd': 'a proprietary applications generator that lets users '
                  'or programmers organise data into files and process those files one at a '
                  'time, used for information retrieval and report preparation. On '
                  'microcomputers it lets end users create files with easy-to-use, menu-driven '
                  'routines. Although it can create and store as many files as necessary, it '
                  'constrains users and programs from transparently interrelating data '
                  'appearing in different files, since it processes only a single file at a '
                  'time.'}},
    {'h3': '3.4.3 Integrated software'},
    {'p': 'A suite of programs performing a variety of processing operations, using data that '
          'is compatible with whatever operation is being carried out — e.g. transferring data '
          'from a spreadsheet into a word-processing document. Examples: **Framework**, '
          '**Enable**, **Symphony**, **Jazz**, **MS-Works**.'},
    {'h3': '3.4.4 Off-the-shelf packages'},
    {'p': 'Application packages acquired separately or as part of an integrated system, and '
          'tailored to specific user requirements. Many small organisations use off-the-shelf '
          'packages on microcomputers, e.g. in insurance, marine, and banking.'},
    {'table': {'cap': 'Off-the-shelf vs in-house (bespoke) packages', 'align': 'll',
      'head': ['Advantages of off-the-shelf', 'Disadvantages of off-the-shelf'], 'rows': [
      ['Written by software specialists, so of very high quality', 'Produces a standardised '
       'solution which may not suit the individual user'],
      ['Continually updated by the manufacturer, so the purchased version is up to date',
       'The end-user is dependent on the manufacturer/vendor for troubleshooting or '
       'maintenance'],
      ['Long in the market, so error-free and well suited to the general public',
       'May not have some special features the end-user requires'],
      ['Well documented, with an easy-to-follow user manual', 'May be incompatible with the '
       'organisation\'s hardware and/or data structure'],
      ['Cheap compared to in-house packages, which take long to develop and are costly',
       'May demand higher memory capacity, which may be expensive for the organisation'],
      ['Well tested, so the end-user can start using it immediately after purchase', ''],
      ['General-purpose, so can be tailored to the user\'s requirements (unlike in-house, '
       'tailor-made packages)', ''],
    ]}},
    {'h3': '3.4.5 Criteria for selecting application packages'},
    {'ol': [
      'A feasibility report, indicating the choice between off-the-shelf and in-house '
      'packages.',
      'Purchase price of the off-the-shelf package.',
      'Type of hardware and operating system designed for the environment (e.g. single-user or '
      'multi-user).',
      'Whether the package can be integrated with other standard packages — will it accept '
      'downloaded data from them?',
      'Whether the RAM capacity of the hardware on which it is installed will be adequate.',
      'The after-sales maintenance agreement.',
      'History of usage elsewhere — the performance of the package and the vendor with '
      'previous users.',
      'The technology version of the package — whether it is the most recent model.',
    ]},
    {'h3': '3.4.6 Sources of application packages'},
    {'p': 'Application packages may be acquired (rented or purchased) from:'},
    {'ol': [
      'Mail order sources advertised in computer magazines and dailies.',
      'Over the counter, from retail shops or stores.',
      'Dealers (vendors) in microcomputers.',
      'Manufacturers of microcomputers who also develop software.',
      'Specialist organisations known as "software houses", which develop software.',
      'Private organisations and institutions that developed software for their own use and '
      'make it available to others for a fee.',
      'Computer bureaux and information centres with expanded activities.',
      'In-house programmers — specialist staff who develop software as part of their official '
      'job routine.',
    ]},
  ]},

  {'n': '3.5', 't': 'Introduction to computer programming and computer languages', 'b': [
    {'p': 'Microcomputers have increased the computing capability of many non-computer '
          'professionals, and the use of application packages has become widespread. Some '
          'off-the-shelf packages (e.g. database packages) can be made more efficient and '
          'tailored to a specific task if the end-user can write some computer code to '
          'supplement the package.'},
    {'h3': '3.5.1 Computer languages'},
    {'p': 'Computer hardware processes data and program instructions in binary form — the '
          '**machine code/language** — which is inconvenient and time-consuming for '
          'programmers. Over the years, computer languages evolved through five generations.'},
    {'h4': '(a) Machine language — 1st generation, c. 1945–1955'},
    {'p': 'Each computer has its own machine language, interpreted by the computer\'s internal '
          'circuitry. Code is in the form of binary digits (0s and 1s); an instruction '
          'consists of an **operation code** (specifying the operation to be performed) and an '
          '**operand address** (specifying the memory address of the operand). Writing in '
          'machine language requires meticulous attention to detail and knowledge of the '
          'computer\'s internal structure, so only highly skilled programmers can do it. '
          'Example code: `0001101000111011`.'},
    {'table': {'head': ['Advantages of machine language', 'Disadvantages of machine language'],
      'align': 'll', 'rows': [
      ['Needs no language processor — already in the form the hardware can use',
       'Machine-dependent — code for one machine will not run on another'],
      ['Occupies less space in memory', 'Very difficult to write — the programmer must attend '
       'to machine architecture while coding'],
      ['Processing is very fast', 'Only written by highly skilled programmers and electrical '
       'engineers'],
    ]}},
    {'h4': '(b) Symbolic/assembly language — 2nd generation, c. 1955–1965'},
    {'p': 'A **low-level language**; codes are written in **mnemonics** (symbolic form, such '
          'as ADD, SUB, MULT). Must be translated into machine code by the **Assembler**; the '
          'translated code is saved on magnetic disk for data processing. Assembling need be '
          'done only once. The language is **machine-dependent**. ("Assembly" describes the '
          'translation process from symbolic to machine code; the language translator is the '
          'Assembler program.)'},
    {'table': {'head': ['Advantages of assembly language', 'Disadvantages of assembly language'],
      'align': 'll', 'rows': [
      ['Easier to learn and write than machine language, since it uses mnemonics',
       'Machine-dependent, like machine language — not portable between machines'],
      ['The resulting machine language is very efficient, being close to machine language',
       'Can only be written by a highly skilled programmer who understands the computer\'s '
       'logical structure'],
      ['Can write applications that take special advantage of computer architecture',
       'Coding is difficult and time-consuming compared to a high-level language'],
      ['Runs faster than high-level languages', ''],
      ['Uses less memory space than high-level languages', ''],
    ]}},
    {'h4': '(c) High-level languages — 3rd generation, c. 1965–1975'},
    {'p': 'Examples: **BASIC** (Beginner\'s All-purpose Symbolic Instruction Code), '
          '**FORTRAN** (Formula Translator), **COBOL** (Common Business-Oriented Language), '
          '**Pascal**, **PL/1** (Programming Language 1), **APL** (A Programming Language), '
          '**Ada**, **C**.'},
    {'p': 'Written in the programmer\'s (natural) language, with less coding detail to worry '
          'about, so accessible to a large number of end-users. Needs a language processor '
          '(compiler or interpreter) to translate the source code into machine object code; '
          'one high-level statement translates into many machine statements (**one-to-many '
          'translation**), which is where the name "high-level" comes from. High-level '
          'languages are **procedure-oriented** — they express in detail the procedure used '
          'to solve a problem. Some are also **problem-oriented**, solving a narrow class of '
          'problems without the end-user detailing the procedure — these are the **fourth '
          'generation languages (4GL)**, or very-high-level languages. A high-level language '
          'is **machine-independent** — a program can be compiled on one machine but executed '
          'on another.'},
    {'p': 'Features of high-level languages:'},
    {'ol': [
      'Facility to describe the nature of the data to be processed — data types (integer, '
      'real, alphanumeric).',
      'Facility to describe operators on appropriate data items, e.g. division on integers.',
      'Inclusion of an allowable character set — upper-case and/or lower-case alphabets.',
      'Allowable control (branching) structures and their syntax — logical IF statements, '
      'repetition (looping) statements, etc.',
      'Input and output statements — reading data via keyboard or files, and sending '
      'information to the screen or a magnetic disk.',
      'Syntax and semantic structures for all statements — precise specification of work and '
      'allowable operations.',
    ]},
    {'table': {'head': ['Advantages of high-level languages',
      'Disadvantages of high-level languages'], 'align': 'll', 'rows': [
      ['Easier to write and understand — written in the programmer\'s spoken language, e.g. '
       'English', 'Less efficient in speed, since it is more abstracted and cannot usually '
       'exploit specific hardware facilities'],
      ['Machine-independent — can be compiled and executed on different machines',
       'Less efficient in the use of internal memory management'],
      ['Problem-oriented — may be written to solve a particular problem easily', ''],
      ['Procedure-oriented — expresses in detail the procedure used to solve a problem (4GLs '
       'are not procedure-oriented)', ''],
      ['Supports program testing and error correction', ''],
    ]}},
    {'h4': '(d) Very high-level languages — 4th generation'},
    {'p': 'A 4GL is easy to learn and use, more or less error-free, high-productivity, quickly '
          'created and needing much less maintenance — a variety of software tools letting '
          'end-users develop applications with minimal or no technical assistance. Objectives:'},
    {'ol': [
      'To help users develop their own application programs more quickly, cheaply and easily.',
      'It demands fewer lines of code than a 3GL to achieve a given task.',
      'It is **non-procedure-oriented** — the user specifies only *what* task is needed, not '
      '*how* to do it.',
      'Best used for retrieval and reporting of information.',
    ]},
    {'p': 'Examples: **RPG** (Report Program Generator), **SQL** (Structured Query Language), '
          '**QBE** (Query-By-Example), Data, Easytrieve Plus, Mark, Intellect.'},
    {'p': '4GLs generally divide into seven categories: query languages (e.g. SQL); report '
          'generators (e.g. RPG); graphics languages; application generators; very-high-level '
          'programming languages; application software packages; and PC tools (e.g. word '
          'processing, spreadsheet packages).'},
    {'p': 'Two powerful 4GL features: **Report generators** — developed to make customising '
          'reports easier and faster, since producing a report requires selecting and '
          'formatting data, specifying titles/page numbers, calculating totals, and '
          'specifying the number and width of columns; and **Application generators** — '
          'produce a program to accomplish tasks the user specifies, including a programming '
          'language, a code generator, a library of commonly used program code, and tools for '
          'creating files, databases and a data dictionary.'},
    {'h4': '(e) Fifth generation languages'},
    {'p': 'Important 5GL areas: **Expert Systems (ES)**, **Natural Languages**, '
          '**Object-Oriented Programming Languages (OOP)**, **Parallel Processing Languages**.'},
    {'def': {'t': 'Object', 'd': 'a predetermined set of program code that, once written and '
                  'tested, always behaves the same way, so it can be reused for other '
                  'applications. In object-oriented programming (OOP), an object is written '
                  'for each specific task and saved in a library so anyone can use it. Rather '
                  'than writing a new program line by line, a program selects objects (by '
                  'pointing to a representative icon) and links them together; objects can be '
                  'modified, used, copied or created.'}},
    {'table': {'head': ['Advantages of OOP', 'Disadvantages of OOP'], 'align': 'll', 'rows': [
      ['Uses a graphical interface', 'Steep initial development costs'],
      ['Ease of use', 'More extensive start-up time'],
      ['Faster program development', 'Programs produced are larger'],
      ['Enhanced programmer productivity', 'Programs produced are slower'],
      ['Programs are more reliable and contain fewer errors, since the modules used have '
       'already been extensively tested', 'Programs use more memory and other computer '
       'resources than traditional methods'],
    ]}},
    {'p': 'Examples of OOP languages: **Smalltalk**, **C++**, **Visual Basic**, **Java**, '
          '**Python**.'},
  ]},

  {'n': '3.6', 't': 'Introduction to grid computing', 'b': [
    {'def': {'t': 'Grid computing', 'd': 'a computing technology through which users or client '
                  'applications gain access to computing resources (processors, storage, data, '
                  'applications, etc.) as needed, with little or no knowledge of where these '
                  'resources are located, or of the underlying technologies, hardware or '
                  'operating systems. The client has no knowledge of where the work is '
                  'executed; the task is returned once completed, and the resource fee is '
                  'handled by the **grid manager**.'}},
    {'p': 'By contrast, in **cloud computing**, work is submitted by the client to cloud '
          'servers (established internally as parallel servers, or as distributed servers), '
          'and the service fee is handled by **utility computing**. Grid computing is mostly '
          'used in remote education services, bioinformatics data storage, and chemical '
          'calculation processing.'},
    {'h3': 'Merits of grid computing'},
    {'ul': [
      '**Access to inaccessible resources** — a user can access resources otherwise '
      'unavailable to them (through financial or other constraints), including hardware, '
      'applications/software and network connectivity, by using unused computing resources '
      'from other organisations.',
      '**Resources utilisation and balancing** — a grid-enabling architecture combines '
      'dispersed resources under a centralised controlling system. An **overloaded** grid '
      '(more tasks than capacity) can shift tasks to **under-loaded** (spare-capacity) parts '
      'of the grid, giving optimum resource utilisation.',
      '**Reliability** — a single processor is a higher risk, since its failure can stop the '
      'whole system; under grid architecture, tasks are distributed, so overall failure is '
      'less likely, and tasks can migrate to another processor if one fails (reliability is '
      'reduced if migration is impossible due to a network problem).',
      '**Parallel computing and scalability** — programs written so that different parts '
      '("**sub-jobs**") run simultaneously can be performed in parallel across the grid; a job '
      'taking 10 seconds could theoretically be completed in 5, 2 or 1 second, depending on '
      'the number of sub-jobs.',
    ]},
    {'h3': '3.6.1 Grid computing applications'},
    {'ul': [
      '**Microprocessor design** — simulations requiring high computing power (not possible '
      'locally) improve the product development lifecycle.',
      '**Medical field** — sharing knowledge and creating repositories used by experts '
      'worldwide.',
      '**Pharmaceutical industry** — simulating the process of creating new medicines or '
      'cures.',
      '**E-learning** — providing important computing resources for e-learning.',
      '**Scientific applications** — complex problems in physics, geology, astronomy, etc., '
      'requiring high computing power.',
      '**Medical imaging** — storing large medical images, requiring high computing power and '
      'data storage.',
    ]},
    {'h3': 'Limitations of grid computing'},
    {'ul': [
      'Not useful for applications that do not need higher computing power.',
      'The other (grid) resource must have higher computing capacity than the user\'s own '
      'computer, or there is no improvement in performance.',
      'More suitable for applications run in **batch mode**; applications needing a graphical '
      'user interface are not very suitable.',
      'Suits applications that can be run in parallel across heterogeneous processors; '
      'applications not designed for parallel mode are unsuitable.',
      'Moving large data to other computing resources raises security and network-capacity '
      'challenges. A solution: reduce data size before moving it, and use encryption/security '
      'protocols. Making multiple copies of the data is another solution, but it increases '
      'network load and requires continuous updating of all data sets.',
    ]},
    {'h3': '3.6.2 Types of grid computing'},
    {'ol': [
      '**Computational grid** — used for distributing resources for better computing power.',
      '**Scavenging grid** — uses idle servers so that desktop computer resources are made '
      'strong enough to complete tasks and jobs.',
      '**Data grid** — used in organisations to assign an interface that helps with data '
      'checking and security.',
    ]},
    {'h3': '3.6.3 Application areas of grid computing'},
    {'ol': [
      'Super distributed computing.',
      'Systems distributed in real time.',
      'Intensive processing of data.',
      'Virtual collaboration environments.',
    ]},
  ]},

  {'n': '3.7', 't': 'Interacting with Microsoft Windows', 'b': [
    {'p': 'System software is made up of: the Operating System (OS); Utility Software; '
          'Language Translators; Editors; and Loaders. The OS is the most important element, '
          'allowing the end-user to interface with the hardware; application packages '
          'interface with the hardware via the OS — e.g. when printing from a word processor, '
          'the package works with the OS to send the document to the printer.'},
    {'p': 'Different companies manufacture their own, mutually incompatible, operating '
          'systems. The most common: **Windows** (Microsoft, called MS Windows); **Mac OS** '
          '(Apple Computing); **Linux** (used for web operations). MS Windows has several '
          'versions, including the older **Windows XP**, **Windows 2000** and **Windows 98** — '
          'all with almost the same capabilities, though newer versions look prettier and are '
          'more robust; all perform system maintenance functions such as copying files and '
          'turning off the system.'},
    {'h3': 'Working around the desktop'},
    {'p': 'The major parts of the Windows desktop:'},
    {'ol': [
      '**Start button** — opens the Start menu, used to open all programs and documents.',
      '**Taskbar** — displays buttons of open applications and windows, and different '
      'toolbars for different tasks.',
      '**Notification area** — formerly the "system tray"; holds the clock, volume control, '
      'and icons for other utilities running in the background.',
      '**Sidebar and gadgets** — an area on the right of the desktop holding utilities '
      '("gadgets") that sit on the desktop performing specific operations.',
      '**Shortcut icons** — links to software programs, installed on the desktop (a "clean" '
      'desktop includes just one icon, for the Recycle Bin).',
      '**Recycle Bin** — where files marked for deletion are dumped.',
    ]},
    {'h3': 'Windows operations'},
    {'ul': [
      '**Pointing and clicking** — move the mouse until the cursor points at an object, then '
      'click the left button once. An effective way to select menu items, directories and '
      'files.',
      '**Double-clicking** — clicking the left button twice in rapid succession, to open '
      'program groups or launch individual programs.',
      '**Right-clicking** — selecting an object and clicking the right button gives a pop-up '
      'menu of commands related to the object — e.g. right-clicking a file icon gives COPY, '
      'MOVE, DELETE, etc.',
      '**Dragging and dropping** — point at an object, press and hold the left button, move '
      'the mouse without releasing it to a new location, then release to drop it there — e.g. '
      'to move files between folders, or delete files by dragging them onto the Recycle Bin.',
      '**Hovering** — positioning the cursor over an item without clicking; many operations '
      'require the cursor to hover before another action is performed.',
      '**Scrolling through a window** — click the up/down arrow on the scroll bar to move a '
      'line at a time; drag the scroll box to jump to a specific place in a long document; or '
      'click between the scroll box and the end arrow to scroll one screen at a time.',
      '**Using menus** — a row of pull-down menus, aligned across the top of the window below '
      'the title bar (the **menu bar**); clicking a menu\'s name opens (pulls down) the full '
      'menu, and a command is activated by clicking it.',
      '**Using toolbars** — the most frequently used operations are placed on one or more '
      'toolbars (typically below the menu bar), each button showing a small picture (icon) or '
      'a bit of text; clicking the button activates the associated command.',
    ]},
  ]},

  {'n': '3.8', 't': 'Windows Explorer', 'b': [
    {'ul': [
      '**Start menu** — all software programs and utilities are accessed via the Start menu, '
      'displayed by clicking the Start button in the lower-left corner. Clicking "All '
      'Programs" opens the Program menu, sorted by type/manufacturer.',
      '**Windows Explorers** — in Windows Vista, all items stored on the computer (programs, '
      'documents, configuration settings) are accessible from special windows called '
      '**Explorers**, used to find, copy, delete, launch and configure programs and '
      'documents. Example: clicking the Music icon opens the Music Explorer, showing all songs '
      'stored on the hard disk.',
      '**Documents Explorer / My Documents** — the most-used Explorer, where documents, '
      'photos, music and other files are stored. Clicking the Documents icon opens a window of '
      'folders; double-clicking a folder shows its contents (files or subfolders); '
      'double-clicking an item launches or opens it; right-clicking gives a pop-up menu of '
      'other tasks (copying, deleting, etc.).',
      '**Computer Explorer / My Computer** — allows access to each major component of the '
      'computer and basic maintenance functions (opening the hard disk\'s contents, copying, '
      'moving, deleting individual files). Opened via the Computer icon in the Start menu; '
      'contains icons for each major component (hard disk drive, external drives, CD-ROM/DVD '
      'drive, etc.); double-click a drive icon to see its files and folders.',
      '**Control Panel** — used to manage Windows configuration settings; opened via the '
      'Control Panel icon in the Start menu. Selecting a category opens a window with a '
      'different set of options; successive clicks lead to the specific item desired.',
      '**Mouse** — a small hand-held device connected to the CPU by a cable; most mice have an '
      'oblong case with a roller underneath and two or three buttons on top. Moving the mouse '
      'moves the **cursor** on screen; clicking (pressing and releasing a button) initiates an '
      'action in the program. Wireless mice are also common. A **pointing input device**.',
      '**Graphical User Interface (GUI)** — the OS is stored on the hard disk; part of it is '
      'loaded into primary memory when the system boots, after which it manages the computer '
      'and provides a user interface. Different operating systems and applications use '
      'different interfaces — most typically the **command line interface** and the '
      '**Graphical User Interface**. The command line interface requires typed text commands '
      '(e.g. DELETE); Unix is an example. The GUI — the most common interface for the desktop '
      'PC — uses pictures, icons and menus to send instructions from the user to the computer. '
      'Examples of GUI operating systems: Windows and Mac OS.',
    ]},
  ]},

  {'n': '3.9', 't': 'Chapter summary', 'b': [
    {'ol': [
      'Software divides into System Software and Application Software.',
      'System software examples: Operating System (OS), language translator, utility '
      'routine, loader, editor, etc.',
      'The Operating System is the most important system software; there are operating '
      'systems for standalone computers, minis and mainframes.',
      'There are also operating systems for different environments — integrated application, '
      'multiprocessing and multiprogramming.',
      'The language processor converts the source code into machine-readable form.',
      'Application packages are meant for specific processes, and every process running on '
      'the computer has an associated application package.',
      'The (computer) bureau plays an important role for people/companies that could not '
      'acquire a computer system, or as a standby facility for those that have one.',
      'Off-the-shelf packages are general application packages, while bespoke software is a '
      'tailored application package.',
      'There are now five generations of computer language: machine language, symbolic '
      '(assembly) language, high-level languages, very-high-level languages, and the fifth '
      'generation languages used in Artificial Intelligence (AI).',
      'Machine and assembly languages are classified as low-level languages: they execute '
      'faster but use lengthy, difficult coding.',
      'High-level languages, such as BASIC and FORTRAN, use the programmer\'s spoken language '
      '(natural languages), but execute more slowly.',
      'Very-high-level languages, such as RPG, are non-procedural.',
      'Fifth-generation languages also use natural languages and are used in AI.',
      'The major computer operations are arithmetic computations, comparisons and I/O '
      'operations.',
      'Program flowcharts, decision tables, decision trees and structured English are aids to '
      'program development.',
    ]},
    {'p': 'The chapter also covered MS Windows, an operating system for the desktop computer, '
          'including the Start button and Start menu, working around the desktop, and Windows '
          'operations in both Vista and earlier versions — the use of the mouse and menus as '
          'aids to Windows operation, and the functions of Windows Explorer, My Documents, My '
          'Computer and Control Panel.'},
  ]},

  {'n': '3.10', 't': 'End-of-chapter questions (study text)', 'b': [
    {'h3': 'Multiple-choice questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–29 with answers', 'open': True, 'q': [
      {'ol': [
        'Which one of the following is NOT a programming language? (A) Machine Language  '
        '(B) Symbolic Language  (C) Narrative Language  (D) High-level Language  (E) 4GL',
        'C++ is an example of … (A) Object-Oriented Language  (B) Machine Language  '
        '(C) Symbolic Language  (D) Low-level Language  (E) High-level Language',
        'A computer Operating System is … (A) an application software  (B) a user application '
        'package  (C) a system software  (D) an interface  (E) a machine driver software',
        'MS Excel is an example of … (A) Word processor  (B) Spreadsheet  (C) Presentation '
        'software  (D) Graphical software  (E) Desktop publishing package',
        'Multiprocessing capability can be achieved by … (A) Operating system  (B) Application '
        'package  (C) User software  (D) Computer memory  (E) Language processor',
        'Operating Systems manage the following computer resources EXCEPT (A) CPU time  '
        '(B) Memory space  (C) Cable sharing  (D) Input/Output devices  (E) File system',
        'Which of the following is NOT a word-processing package? (A) MS Word  '
        '(B) WordPerfect  (C) MultiMate  (D) Multiplan  (E) DisplayWrite',
        'A system program that converts a source program written in a high-level language to '
        'machine code all at once is called (A) Assembler  (B) Compiler  (C) Interpreter  '
        '(D) Loader  (E) Editor',
        'Which of the following is NOT a desktop publishing package? (A) Multiplan  '
        '(B) PageMaker  (C) CorelDraw  (D) Studio Publisher  (E) Microsoft Office Publisher',
        'All of the following are examples of utility programs EXCEPT (A) Loader  '
        '(B) Text editor  (C) Linkage editor  (D) Sorter  (E) Assembler',
        'Sequencing, selection and repetition are examples of (A) Computer program '
        'instructions  (B) System flowchart elements  (C) Computer program operations  '
        '(D) Program flowchart elements  (E) Process flowchart elements',
        'Which of the following is NOT an aid to computer program construction? (A) Structured '
        'Narrative Language  (B) Program flowchart  (C) Decision table  (D) Decision tree  '
        '(E) Structured System Analysis and Design',
        'The following are advantages of using high-level languages EXCEPT (A) it is easier '
        'to write and understand because of the use of English  (B) it is problem-oriented  '
        '(C) it is machine-dependent  (D) it is a procedure-oriented language  (E) it can be '
        'compiled and executed on several machines',
        'A software program designed to perform a specific task is known as (A) Operating '
        'System  (B) System Software  (C) Customised Software  (D) Utility Software  '
        '(E) Application Software',
        'Which one of the following is NOT a function performed by system software? '
        '(A) Provision of utility services  (B) Providing settings for application packages  '
        '(C) Enabling the use of peripheral devices  (D) Memory management  (E) Providing a '
        'suitable environment for program development',
        'The software capable of creating, retrieving, expanding and maintaining a database is '
        'called (A) Database software  (B) File management system  (C) Database management '
        'system  (D) Database program  (E) Database library',
        'An automated file for storing definitions of data elements and their characteristics, '
        'such as usage and physical relationships, is known as (A) Database management system  '
        '(B) Data manipulation language  (C) Database language  (D) Data dictionary  '
        '(E) Data definition language',
        'A keypad on the keyboard that creates blank space when pressed is called the '
        '(A) Control key  (B) Shift key  (C) Space bar key  (D) Backspace key  '
        '(E) Navigation key',
        'A peripheral device used to move or drag objects in a Graphical User Interface '
        'environment is called (A) Operating system  (B) Windows  (C) Desktop  (D) Icon  '
        '(E) Mouse',
        'Which of the following is NOT a component of the menu displayed by Microsoft Word? '
        '(A) View  (B) File  (C) Help  (D) Data  (E) Insert',
        'Assembly language belongs to which generation of computer? (A) First  (B) Second  '
        '(C) Third  (D) Fourth  (E) Fifth',
        'The main purpose of a program flowchart is to (A) create a graphical illustration of '
        'the program logic  (B) clarify the logic of the algorithm  (C) beautify the program '
        'logic  (D) provide an interface for the user  (E) provide an interface for computing',
        'Windows operating system is an example of which one of the following? (A) Single-user '
        'operating system only  (B) Single-user and multi-tasking operating system  '
        '(C) Multi-tasking operating system only  (D) Multi-user and multi-tasking operating '
        'system  (E) Multi-user operating system only',
        'In computer programming, a repetitive statement is also known as a (A) Cycle  '
        '(B) Turn-around  (C) Loop  (D) Round robin  (E) Ring',
        'The components of the desktop window are: (A) Status bar, background and icons  '
        '(B) Start button, status bar, background and icons  (C) Start button, program menu '
        'and icons  (D) Start menu, program menu and background  (E) Status bar, background '
        'and font',
        'Microsoft PowerPoint is an example of a … package (A) Graphical  (B) Spreadsheet  '
        '(C) Word-processing  (D) Presentation  (E) Accounting',
        'An application generator is an example of a … generation language (A) First  '
        '(B) Second  (C) Third  (D) Fourth  (E) Fifth',
        'The following are examples of electronic spreadsheet packages used on microcomputers '
        'EXCEPT (A) Excel  (B) Multiplan  (C) MultiMate  (D) Quattro  (E) Supercalc',
        'Which of the following is NOT an example of an Object-Oriented Language? '
        '(A) Smalltalk  (B) Java  (C) C++  (D) Visual Basic  (E) Ada',
      ]}],
      'a': [
      {'p': '**1.** C  **2.** A  **3.** C  **4.** B  **5.** A  **6.** C  **7.** D  **8.** B  '
            '**9.** A  **10.** E  **11.** D  **12.** E  **13.** C  **14.** E  **15.** B  '
            '**16.** C  **17.** D  **18.** C  **19.** E  **20.** D  **21.** B  **22.** B  '
            '**23.** D  **24.** C  **25.** C  **26.** D  **27.** D  **28.** C  **29.** E'}]}},
    {'h3': 'Short-answer questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–31 with answers', 'open': True, 'q': [
      {'ol': [
        'A 4GL package that enables a user or programmer to develop a set of programs that '
        'comprise an entire application is called a …',
        'Compiler, Interpreter and Assembler are examples of …',
        'A data field that uniquely identifies a record is called a …',
        'The application software that enables users to create and manipulate data organised '
        'in rows and columns is known as a …',
        'The technology capable of processing text, graphics, video, sound and animation is '
        'called …',
        'A collection of files, integrated and organised to provide a single comprehensive '
        'file system, is known as a …',
        'The method of batching inputs and queuing the output on the same magnetic medium is '
        'called …',
        'The use of several processing units (processors) linked together to perform '
        'coordinated work concurrently is known as …',
        'The software system responsible for the creation, expansion, maintenance and '
        'provision of access to a database is called …',
        'Throughput is the amount of useful … performed during a given period of time.',
        'OMR as an input device is an example of a … document.',
        'START and END are instructions used in a program … .',
        'Software is a generic term for all … that run on the hardware system.',
        'In a program flowchart, "less than" is a(n) … operation.',
        'The programming language whose instructions are made up of operation codes '
        '(specifying operations to be performed) and operand addresses (specifying the memory '
        'address of the operand) is called …',
        'An application package with facilities to assist accountants in creating and editing '
        'texts, graphics, letters and reports is called …',
        'The use of television, video and sound technology together with computers, to enable '
        'people at different locations to see, hear and talk with one another, is called …',
        'A suite of computer programs that controls the use of hardware and acts as an '
        'interface with application programs is called …',
        'The operating system that allows many users to work on one computer at the same '
        'time, where each user has processing capability at their end, is called …',
        'A program solution plan expressed in a meta-language, containing step-by-step actions '
        'to solve a particular problem, is called …',
        'Assembly language is said to be machine-dependent, whereas a procedural language is '
        'said to be …',
        'The software program that places program segments into the appropriate locations in '
        'memory, ready for execution, is called the …',
        'C++ is an example of what type of programming language?',
        'The pictorial or diagrammatic representation of the steps to be followed in an '
        'algorithm is called a …',
        'A collection of files, integrated and organised to provide a single comprehensive '
        'file system, is called a …',
        'A program that converts a source program written in a high-level language into a '
        'machine code/object program is called a …',
        'The ability of an operating system to execute a user\'s tasks concurrently is known '
        'as …',
        'The style of computer programming that uses the principle of objects is called …',
        'The two types of editor that convert input into a particular output format are the '
        'text editor and the … editor.',
        'The application software that can be purchased from a computer vendor is called a(n) '
        '… application.',
        'The use of video and sound technology, together with computers, to enable people at '
        'different locations to see, hear and talk with one another is called …',
      ]}],
      'a': [
      {'ol': [
        '**Application generator.**',
        '**Language translators/processors.**',
        '**Primary key.**',
        '**Spreadsheet.**',
        '**Multimedia.**',
        '**Database.**',
        '**Spooling.**',
        '**Multiprocessing.**',
        '**Database Management System (DBMS).**',
        '**Work.**',
        '**Turnaround (document).**',
        '**Flowchart (I/O — input/output).**',
        '**Programs.**',
        '**A logical (operation).**',
        '**Machine language.**',
        '**Word processing (package).**',
        '**Video conferencing.**',
        '**Operating system.**',
        '**Multi-user (operating system).**',
        '**Pseudocode.**',
        '**Problem-oriented.**',
        '**Loader.**',
        '**Object-oriented (programming language).**',
        '**Flowchart.**',
        '**Database.**',
        '**Compiler.**',
        '**Multi-tasking.**',
        '**Object-Oriented Programming.**',
        '**Linkage (editor).**',
        '**Off-the-shelf (application).**',
        '**Videoconferencing.**'],
      }]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'Half the marks in this chapter are pure recall of classifications: the five generations of '
   'language (with an example of each), the three language processors (assembler, compiler, '
   'interpreter — and why an interpreter is slower but friendlier), and the difference between '
   'multi-user, multi-tasking, multi-programming and multi-processing, which examiners '
   'deliberately confuse. Learn the Windows vocabulary (Explorer, Control Panel, right-click, '
   'drag-and-drop) as a practical skill as well as a definition — it is tested both ways.',
 'errors': [
   'Confusing multi-programming (one processor, switching between programs) with '
   'multi-processing (several processors working at once).',
   'Saying an interpreter produces object code — it does not; each line is executed and '
   'discarded, which is exactly why re-running a program means re-interpreting it.',
   'Calling a high-level language machine-dependent; it is machine-independent, which is the '
   'whole point of compiling it.',
   'Confusing a file manager (processes one file at a time) with a DBMS (integrates many '
   'files and removes duplication).',
   'Treating off-the-shelf and bespoke software as interchangeable terms for the same thing — '
   'their advantages and disadvantages are mirror images of each other.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A program that translates a high-level source program into machine code, converting '
         'and executing one line at a time as the program runs, is a(n)',
    'o': ['Assembler', 'Compiler', 'Interpreter', 'Loader', 'Linkage editor'],
    'a': 2,
    'w': 'An interpreter converts and executes a line at a time and produces no object code — '
         'unlike a compiler, which translates the whole program at once before it is run.',
    'src': 'Chapter 3.2.6', 'sec': '3.2'},
   {'q': 'A mainframe working on several programs by switching between them, keeping the CPU '
         'continuously busy, is running under a',
    'o': ['multi-user environment', 'multi-tasking environment', 'multi-programming '
          'environment', 'multiprocessing environment', 'time-sharing environment'],
    'a': 2,
    'w': 'In multi-programming, one processor switches between programs, with the time slice '
         'set by I/O interrupts. Multiprocessing, by contrast, uses several processors '
         'working at once; time-sharing gives each user a predetermined time slice.',
    'src': 'Chapter 3.3.3', 'sec': '3.3'},
   {'q': 'Which of the following is a fourth-generation language (4GL)?',
    'o': ['FORTRAN', 'COBOL', 'Assembly language', 'SQL', 'Machine language'],
    'a': 3,
    'w': 'SQL (Structured Query Language) is a 4GL — non-procedural, telling the system what '
         'is wanted rather than how to get it. FORTRAN and COBOL are 3GLs; assembly and '
         'machine language are 2GL and 1GL.',
    'src': 'Chapter 3.5.1', 'sec': '3.5'},
   {'q': 'The software that builds, manages and provides access to a database, avoiding data '
         'duplication across many applications, is a',
    'o': ['file manager', 'Database Management System (DBMS)', 'utility program',
          'linkage editor', 'language processor'],
    'a': 1,
    'w': 'A DBMS integrates many files and lets several applications share the same data '
         'without duplication; a file manager, by contrast, processes only one file at a time.',
    'src': 'Chapter 3.4.2', 'sec': '3.4'},
   {'q': 'Software written in-house, tailored to one organisation\'s specific needs, is called',
    'o': ['off-the-shelf software', 'bespoke software', 'system software', 'a utility program',
          'an operating system'],
    'a': 1,
    'w': 'Bespoke (custom) software is written or commissioned for one organisation\'s '
         'specific process; off-the-shelf software is bought ready-made for general use.',
    'src': 'Chapter 3.4.2', 'sec': '3.4'},
   {'q': 'Which of these is a function of the operating system?',
    'o': ['Compiling a high-level language program', 'Providing a virtual machine and managing '
          'memory', 'Producing multicolour hardcopy graphics', 'Storing data on a magnetic '
          'stripe card', 'Converting analogue signals to digital form'],
    'a': 1,
    'w': 'Resource sharing, virtual storage, I/O handling, memory management, the filing '
         'system, protection/error handling, program control, and booting are all OS '
         'functions.',
    'src': 'Chapter 3.2.1', 'sec': '3.2'},
  ],
  'theory': [
   {'q': 'Enumerate any FIVE requirements of a multi-user application.',
    'marks': 5,
    'a': [
      {'ol': [
        'Terminal controllers for controlling the operations of groups of terminals.',
        'If remote terminals are involved: MODEMs, multiplexors and a front-end processor.',
        'Private leased communication lines.',
        'A powerful processor to support the multi-user environment, for polling the lines to '
        'allocate time slots.',
        'Large memory capacity for storing the various user programs, and the high overhead '
        'required for storing the operating system.',
        'Protection features for preventing a system crash, and record/file locking and '
        'unlocking facilities to prevent a record/file being updated by another user.']}],
    'src': 'Chapter 3.10, theory Q1', 'sec': '3.10'},
   {'q': '(a) Enumerate the sources of application packages. (b) State any FIVE factors to be '
         'considered when selecting application packages.',
    'marks': 13,
    'a': [
      {'h4': '(a) Sources of application packages'},
      {'ol': [
        'Mail order sources advertised in computer magazines.',
        'Retail shops/stores (over the counter) — off-the-shelf.',
        'Dealers (vendors) of microcomputers.',
        'Manufacturers of computers who also develop software.',
        'Software houses that develop software.',
        'Computer bureaux and information centres.',
        'In-house programmers (who develop software as part of their job).',
        'The internet — downloading software.',
        'Microcomputer dealers who also sell software.']},
      {'h4': '(b) Factors for selecting application packages (any five)'},
      {'ol': [
        'Purchase price of the package.',
        'Type of hardware and operating system designed for the environment, e.g. single-user '
        'or multi-user.',
        'Integration of the package with other standard packages.',
        'RAM capacity of the hardware on which it will be installed.',
        'Processing time and response time fast enough.',
        'Availability of full and clear documentation.',
        'Ability of the supplier/dealer to demonstrate the package.',
        'Ease of use and user-friendliness (menus, screen prompts, help).',
        'Adequacy of controls (e.g. passwords, data validation checks, accounting controls).',
        'Provision for updating/amending/modifying the package.',
        'Support and maintenance service provided by the software supplier.',
        'The vendor\'s or developer\'s reputation.',
        'Provision of an alternative package should the chosen one fail.']}],
    'src': 'Chapter 3.10, theory Q2', 'sec': '3.10'},
   {'q': 'High-level languages are written in the programmer\'s language. (a) State any FIVE '
         'features of high-level languages. (b) Enumerate any THREE advantages and TWO '
         'disadvantages of high-level languages. (c) List any FOUR examples of high-level '
         'languages.',
    'marks': 14,
    'a': [
      {'h4': '(a) Features (any five)'},
      {'ol': [
        'Facility to describe the data to be processed — specification of data types, e.g. '
        'integer, real.',
        'Facility to describe operators on appropriate data items, e.g. division on integers.',
        'Inclusion of allowable characters, e.g. upper-case and lower-case alphabets.',
        'Allowable control (branching) structures and syntax, e.g. logical IF, repetition '
        '(looping) statements.',
        'Input and output statements, allowing data to be read and information sent to the '
        'screen.',
        'Inclusion of syntax and semantic structures — precise specification of work and '
        'allowable operations.']},
      {'h4': '(b) Advantages (any three) and disadvantages (two)'},
      {'p': '**Advantages:** easier to write and understand, since written in the '
            'programmer\'s spoken language (e.g. English); machine-independent; '
            'problem-oriented (written to solve a particular problem); procedure-oriented; '
            'speeds up program testing and error correction.'},
      {'p': '**Disadvantages:** less efficient in terms of execution speed; less efficient in '
            'the use of internal memory management.'},
      {'h4': '(c) Examples (any four)'},
      {'p': 'FORTRAN (Formula Translator); COBOL (Common Business Oriented Language); BASIC; '
            'Pascal; PL/1 (Programming Language 1); Ada; C; APL.'}],
    'src': 'Chapter 3.10, theory Q3', 'sec': '3.10'},
   {'q': '(a) Enumerate the basic operations performed in a computer program. (b) List the '
         'purposes of a program flowchart.',
    'marks': 9,
    'a': [
      {'h4': '(a) Basic operations'},
      {'ol': [
        '**Input and output** — reading data by an input device and writing information to '
        'the screen.',
        '**Arithmetic operations** — addition, multiplication, subtraction, division and '
        'exponentiation.',
        '**Logical operations** — comparing two data items to a Boolean value (TRUE/FALSE): '
        'less than, less than or equal to, greater than, greater than or equal to, and equal '
        'to.',
        '**Branching operations** — *sequencing* (e.g. read data from a file, write it to '
        'another); *selection* (e.g. logical IF, IF-THEN-ELSE, GOTO, CASE); *repetition/'
        'looping* (executing instructions repeatedly until a condition is met, e.g. '
        'DO-UNTIL).']},
      {'h4': '(b) Purposes of a program flowchart'},
      {'ol': [
        'To clarify the logic of the algorithm.',
        'To analyse the actions resulting from a set of conditions.',
        'To sort out the procedural steps in the program.',
        'As an aid to program construction and coding.',
        'As a communicating document in program documentation.']}],
    'src': 'Chapter 3.10, theory Q4', 'sec': '3.10'},
   {'q': 'What is the basic function of each of the following Microsoft Windows operations? '
         '(a) Menu bar (b) Toolbar (c) Start button (d) My Computer (e) My Documents '
         '(f) Control Panel.',
    'marks': 6,
    'a': [
      {'ul': [
        '**Menu bar** — located at the top of the window; a drop-down menu of commands used '
        'on the file, e.g. creating a new file, opening an existing one, saving and printing.',
        '**Toolbar** — made up of icons that serve as mouse shortcuts to common commands.',
        '**Start button** — used to open all the software programs and utilities on the '
        'computer for access.',
        '**My Computer** — allows access to each major component of the computer, and to '
        'perform basic maintenance functions such as copy, move and delete individual files.',
        '**My Documents** — provides quick access to all the documents, photos, music and '
        'other files stored on the computer\'s hard disk.',
        '**Control Panel** — provides access to Windows configuration settings, and a means '
        'to manage those settings.']}],
    'src': 'Chapter 3.10, theory Q5', 'sec': '3.10'},
  ]},
}
