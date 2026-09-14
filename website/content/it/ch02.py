CH = {
 'n': 2,
 't': 'Hardware Fundamentals',
 'brief': 'The block diagram of the hardware system; input, output and storage devices; the '
          'CPU (processor and primary memory); and the input, output and storage controls that '
          'protect an application system.',
 'outcomes': [
   'Describe the computer architecture (the block diagram of the hardware system)',
   'Distinguish peripheral from auxiliary equipment, and online from offline equipment',
   'Classify input devices as direct or indirect, and describe each input device',
   'Distinguish impact from non-impact output devices, and describe each output device',
   'Describe the CPU — the processor (ALU and control unit) and the primary memory',
   'Distinguish RAM from the various forms of ROM, and describe cache memory',
   'Describe the magnetic, optical, solid-state and cloud external storage media',
   'Describe input, output and storage application controls',
 ],
 'secs': [
  {'n': '2.1', 't': 'Computer hardware structure', 'b': [
    {'p': 'A **Computer System** consists of three broad components:'},
    {'ul': [
      '**Hardware** — the physical unit; the collection of electronic components of the '
      'computer system.',
      '**Software** — the suite of programs processed by the hardware, which allows the '
      'hardware to function effectively and efficiently. A **program** is a sequence of '
      'instructions, written in a particular computer language, carried out by the hardware to '
      'solve a given problem.',
      '**Human-ware** — the people who operate and maintain the computer system. No computer '
      'system can function without human beings, no matter how remotely controlled.',
    ]},
    {'h3': '2.1.1 Hardware components'},
    {'p': 'The hardware divides into two major components: the **Central Processing Unit '
          '(CPU)** and the **support devices** (external storage, input and output devices).'},
    {'p': 'The **CPU** consists of the **processor** and the **primary memory**. The primary '
          'memory works with the processor during processing, temporarily storing incoming '
          'data and processed results for easy access. The processor itself consists of the '
          '**Arithmetic Logic Unit (ALU)** and the **Control Unit**, plus a '
          '**Communications unit** linking to input, output and storage.'},
    {'p': 'The **support devices** are primarily involved with input, output and/or secondary '
          'storage functions. Storage devices provide an area to keep programs and '
          'data/information, and a means to save and retrieve them. Support equipment is often '
          'classified, with respect to its relationship with the CPU, as either **peripheral** '
          'or **auxiliary** equipment.'},
    {'h3': '2.1.2 Online and offline equipment'},
    {'def': {'t': 'Online equipment', 'd': 'support equipment currently set up so that it can '
                  'transmit data to, or receive output information from, the CPU over a '
                  'communications line — i.e. it is connected to the CPU.'}},
    {'def': {'t': 'Offline equipment', 'd': 'support equipment without this capability.'}},
    {'table': {'head': ['Peripheral equipment', 'Auxiliary equipment'], 'align': 'll', 'rows': [
      ['Designed primarily to be used in an **online** mode', 'Designed to work in an '
       '**offline** mode'],
      ['Examples: communication terminals; printers and VDU; keyboard',
       'Examples: the microfilm reader found in many libraries; data-entry devices used in '
       'large data processing centres to enter data offline onto a tape or disk'],
    ]}},
    {'h3': '2.1.3 Summary of the elemental structure of the hardware'},
    {'ol': [
      '**Input device** — transfers data and programs to the internal memory.',
      '**Central Processing Unit (CPU)** — the main unit of the hardware. It consists of the '
      'internal memory, the Arithmetic Logic Unit (ALU) and the Control Unit. It accepts data '
      'from an input device, performs the instructions specified by the program, and sends '
      'results to an output device. The **control unit** interprets and executes instructions '
      'received from the computer system. The **processor** is the combination of the ALU and '
      'the control unit.',
      '**Output device** — receives the results of processing from the processor.',
      '**Storage device** — an external (bulk) auxiliary device providing for the storage of '
      'records and programs until required for processing activities.',
    ]},
  ]},

  {'n': '2.2', 't': 'Computer input unit', 'b': [
    {'p': 'Data to be stored or processed in a computer system is first converted to a '
          '**machine-readable form**, which is read by an input unit, transformed to the '
          'appropriate internal code, and stored in memory.'},
    {'h3': '2.2.1 Direct and indirect input devices'},
    {'p': 'Data input is categorised into **direct** and **indirect**.'},
    {'def': {'t': 'Direct input', 'd': 'data is in a form suitable for processing without the '
                  'need for data conversion.'}},
    {'ul': [
      'Examples of **direct** input devices: **Optical Mark Reader (OMR)**, **Magnetic Ink '
      'Character Reader (MICR)**, **Optical Character Reader (OCR)**.',
      'Examples of systems that **need data conversion** (indirect): punched card, barcode, '
      'tag and paper tape. In these systems, the data is usually converted to magnetic media '
      'before being input for processing.',
    ]},
    {'h3': '2.2.2 Categories of input media'},
    {'ol': [
      'Tags / barcode systems', 'Punched cards / paper tape systems', 'Magnetic media',
      'Optical media', 'Voice-input devices', 'Imaging devices',
    ]},
    {'key': 'The magnetic, optical, voice and imaging devices are **direct data entry '
            'devices**. Direct data entry gives **source data automation** — data is captured '
            'electronically at the point where it originates. For example, when a sale is '
            'made, the transaction is recorded immediately in machine-readable form, so: '
            '(i) data is available quickly for use; (ii) fewer errors occur, since there is no '
            'manual transcription; (iii) data integrity and accuracy are enhanced through '
            'validation programs; (iv) data can be made available on a real-time or fast '
            'batch-turnaround basis.'},
    {'h4': '(a) Magnetic media — data converted to machine-readable form (electronic pulses) '
           'using magnetic properties'},
    {'ul': [
      '**Keyboard** — the primary input device for microcomputers; typewriter-like keys that, '
      'when depressed, provide input. Contains: alphabetic keys, numeric keys, punctuation '
      'keys, arithmetic operation keys, 12 function keys (F1–F12), control keys, and special '
      'symbol keys. Used with a screen as an input device.',
      '**Mouse** — usually contains a rolling metal ball and one or more buttons; moving it on '
      'a flat surface feeds electrical signals that move the cursor. (The **cursor** is a '
      'screen element — a blinking underline or small arrow — that points to where the next '
      'character may be entered.) It enhances, rather than replaces, the keyboard.',
      '**Magnetic Ink Character Recognition (MICR)** — characters printed in magnetic ink '
      '(ferromagnetic substance) in a special type font, readable by both humans and machine. '
      'An input device called a **magnetic ink character reader/sorter** accomplishes MICR. '
      'Used mainly in banks and financial institutions for processing cheques.',
      '**Key-to-disk system** — a number of key stations enable many operators to read data '
      'from source documents and encode it onto magnetic disks simultaneously. Verifies data '
      'and validates data fields, controlled by **ROM**; data is then transmitted to the '
      'mainframe some distance away. Essential elements: the key station, mini-processor, disk '
      'drive, tape decks, and a supervisor\'s console for monitoring system status.',
      '**Key-to-diskette system** — a data station records data onto floppy diskettes. As data '
      'is entered it is stored in a buffer and displayed on screen for error correction before '
      'being recorded. Accomplished by an integrated floppy disk unit built into a processor\'s '
      'cabinet, or a free-standing unit.',
      '**Joystick** — familiar from electronic arcade games. Used like a mouse, but a movable '
      'stick (instead of a rolling ball) positions the cursor; buttons on the stick or unit '
      'execute commands.',
      '**Magnetic stripe card** — a rectangular card carrying machine-sensitive data on a '
      'magnetic stripe (a thin strip of magnetic recording tape). A magnetic stripe card '
      'reader converts the information to computer-sensitive form. Applications: bank credit '
      'or service cards, ATMs, bank payment systems.',
      '**Smart card** — similar to a magnetic stripe card, but the information is held on a '
      'plastic card embedded with a microprocessor chip using **EPROM**. Besides basic '
      'accounting data, it contains memory and processing capability. Used like a magnetic '
      'stripe card for money transmission; harder to duplicate and so more secure.',
    ]},
    {'h4': '(b) Optical devices'},
    {'ul': [
      '**Optical Character Recognition (OCR)** — optical characters in a special type font, '
      'readable by both humans and optical scanning equipment; no special ink required (unlike '
      'MICR). Read by a scanner attached to another device, e.g. an electronic cash register. '
      'The most familiar optical code is the **barcode** — the **Universal Product Code '
      '(UPC)** found on supermarket goods. **Point-of-sale (POS)** describes situations where '
      'optical scanning equipment records purchases for source data entry, interfacing with '
      'the consumer; at the hub of a POS system is an electronic cash register — a '
      'microcomputer or communications terminal that transmits data online to managers.',
      '**Optical Mark Recognition (OMR)** — a source document pre-printed as a **turnaround '
      'document**, with pre-designated column values; a mark (graphite pencil, ball-point pen, '
      'or a typed line/cross) is recorded in the appropriate column. A scanner senses the '
      'graphite in each column using an electric current and translates it into machine code. '
      'Applied in marking multiple-choice examinations. A **turnaround document** is one '
      'initially produced by the computer to collect data, then re-input to the computer for '
      'processing — OMR and OCR are turnaround documents.',
    ]},
    {'h4': '(c) Source data automation'},
    {'p': 'An example is the **scanner** — a document (text or image) is fed in, a light band '
          'passes along the page, and the pattern is transferred to the computer. Scanners are '
          'used for **document image processing (DIP)** or in **desktop publishing (DTP)** to '
          'input an image to a published document.'},
    {'h4': '(d) Light pen'},
    {'p': 'An electronic device — a photo-diode on the end of a cable — used with a VDU to '
          'display, modify or detect images on screen in **CAD (Computer Aided Design)** '
          'applications. It traces the outline of the image across the screen; the computer '
          'detects the pen\'s position by counting vertical and horizontal synchronisation '
          'pulses.'},
    {'h4': '(e) Touch screen'},
    {'p': 'A display screen that is touch-sensitive: pointing a finger at a displayed command '
          'executes it. Applications:'},
    {'ol': [
      'Factories — a worker wearing gloves can point to a screen selection to initiate an '
      'action.',
      'Banks and stores — untrained customers, reluctant to read instructions, can interact '
      'via the touch-screen labelling.',
      'Sales point / retail services — items bought with their prices can be scanned or '
      'highlighted on screen, helping stock inventory.',
    ]},
    {'h4': '(f) Image input devices'},
    {'p': 'An **imaging device** transforms graphical images (drawings, photographs, maps) '
          'into machine-readable form. Example: the **graphic (digitising) tablet** — '
          'constructed from a sensitive semi-conducting material that traces the movement of a '
          'stylus, forming graphical shapes; the shapes are converted to digital signals input '
          'directly into memory and sent to the display device.'},
  ]},

  {'n': '2.3', 't': 'Computer output devices', 'b': [
    {'p': 'The primary output devices are the **Monitor**, **Printer**, **MODEM**, and '
          '**loudspeaker**. Computer output is categorised as **softcopy** or **hardcopy**.'},
    {'def': {'t': 'Softcopy', 'd': 'a transient message that disappears when power is off. It '
                  'cannot be touched or kept for long — it can only be seen or heard. Examples: '
                  'the display on the monitor; information transmitted by a MODEM; the sound '
                  'from a computer loudspeaker (e.g. a beep on a data-entry error).'}},
    {'def': {'t': 'Hardcopy', 'd': 'a permanent message on paper or other writing material. It '
                  'can be touched and stored for a very long time. Examples: output from a '
                  'printer or a graph plotter.'}},
    {'h3': '2.3.1 Advantages and disadvantages of display equipment'},
    {'table': {'head': ['Advantages', 'Disadvantages'], 'align': 'll', 'rows': [
      ['Allows easy access to a vast amount of data', 'Output cannot be removed from the '
       'screen'],
      ['Does not encourage paper wastage', 'The amount of output handled at one time is '
       'limited by screen size and the rate of paging through screens'],
      ['', 'One cannot output with a pencil or pen'],
      ['', 'One must be physically present at the display device site to see the output'],
    ]}},
    {'h3': '2.3.2 Category of output devices'},
    {'h4': '(a) Monitor'},
    {'p': 'A **monitor** is a display device that works with a keyboard. A monitor alone is an '
          'output device; the monitor and keyboard together serve as an input device for '
          'microcomputers. Also called **VDU (Visual Display Unit)**, **Video Display Unit**, '
          '**VPU (Visual Presentation Unit)**, or **screen**. The message displayed is a '
          'softcopy, letting users see what they typed and how the system is responding.'},
    {'p': 'The VDU has three primary features: **screen resolution**, **colour presentation**, '
          'and **screen shape**.'},
    {'ul': [
      '**Screen resolution** — the clarity of images on the screen. The display forms images '
      'from tiny dots called **pixels** (picture elements), arranged in a rectangular pattern. '
      'More pixels → sharper image → higher resolution.',
      '**Colour presentation** — a VDU may be **monochrome** (a single foreground colour, e.g. '
      'black on white) or **colour**. Colour allows better presentation because important '
      'items can be highlighted. Display devices can produce **text output** (alphabetic '
      'characters, digits, special characters) and **graphic output** (drawings, images, '
      'maps) — graphics are used by managers for information-intensive presentation (bar '
      'charts, pie charts, line charts).',
    ]},
    {'table': {'cap': 'Colour screen standards', 'align': 'll', 'head': ['Acronym', 'Meaning'],
      'rows': [
      ['VGA', 'Video Graphic Array'],
      ['CGA', 'Colour Graphic Adapter'],
      ['EGA', 'Enhanced Colour Graphic Adapter'],
      ['MCGA', 'Multi Colour Graphic Adapter'],
      ['SVGA', 'Super Video Graphic Adapter'],
    ]}},
    {'ul': [
      '**Monitor shapes** — monitors are either **CRT (cathode ray tube)** type or '
      '**flat-panel** type.',
      '**CRT** — uses a large tube-type element like a TV set; bulky and limited in '
      'resolution, but inexpensive.',
      '**Flat-panel** — uses **liquid crystal display (LCD)** or **gas-plasma** technology. '
      'LCD devices use crystalline materials sandwiched between two planes of glass; applying '
      'voltage lines up the crystals, blocking light in certain areas to produce the display. '
      'Gas-plasma displays trap gas between glasses to form images, and give better resolution '
      'than LCD.',
    ]},
    {'p': 'Advantages of flat-panel displays: (i) lightweight; (ii) compact; (iii) better '
          'resolution than CRT; (iv) modern.'},
    {'h4': '(b) Graph plotter'},
    {'p': 'A peripheral device primarily used for output of complicated, fine graphical '
          'information; produces multicolour hardcopy. Used for engineering, scientific and '
          'business-presentation graphics. Modern plotters can produce three-dimensional, '
          'multicolour drawings.'},
    {'h4': '(c) Computer Output on Microfilm/Microfiche (COM)'},
    {'p': 'Used to store massive data in compact form, often for archival purposes. Output — '
          'alphanumeric or graphic — is displayed on a high-resolution cathode-ray tube and '
          'photographed into a much-reduced **microform**, either a **microfilm** (a '
          'continuous strip, with images in frames one at a time along the strip) or a '
          '**microfiche** (separate sheets of film, each containing many frames/"pages"). A '
          'special microfilm reader reads the output; a microfiche is easier to read than a '
          'microfilm. Some microfilm readers also produce hardcopy by the xerographic process.'},
    {'table': {'head': ['Advantages of COM', 'Disadvantages of COM'], 'align': 'll', 'rows': [
      ['Large volume of information condensed into a small physical storage space',
       'Prohibitive price — highly expensive'],
      ['Information stored permanently for future use in a small space',
       'Restricted access to information, since it is not readable to the naked eye'],
      ['Film can be indexed by computer to aid searching', 'Requires highly trained / skilled '
       'personnel to handle'],
      ['Higher speed printout', ''],
      ['Cheaper output medium for high-volume applications', ''],
      ['Frames viewed easily on a special COM reader that projects the image on screen', ''],
      ['A microfilm frame/page can be produced on paper or in enlarged readable form when '
       'required', ''],
    ]}},
    {'h4': '(d) Printers — output devices that produce hardcopy'},
    {'p': 'Printers are classified, first, by whether they make noise while printing:'},
    {'table': {'head': ['Impact printers', 'Non-impact printers'], 'align': 'll', 'rows': [
      ['Wires or embossed characters strike a piece of paper or a ribbon, forming a character '
       'on the page', 'Use a quieter method — heating, spraying, or electrically forming '
       'characters onto the page'],
    ]}},
    {'p': 'They are also classified by output quality and speed: **character printers**, '
          '**line printers**, and **page printers**.'},
    {'ul': [
      '**Character (serial) printers** — print one character at a time and are bidirectional. '
      'Examples: **dot-matrix** and **daisy wheel** (both impact). Dot-matrix letter quality '
      'improves in "Near Letter Quality (NLQ)" mode, but at reduced speed. Daisy wheel cannot '
      'print graphical images, but its output quality is exceptionally high — though slow.',
      '**Line printers** — impact printers that print a complete line at a time. Examples: '
      '**chain/barrel printers** and **band printers**. Used for large-volume printing on '
      'mainframes and minicomputers, operating at high speed.',
      '**Page printers** — non-impact; due to their high speed, they appear to print a whole '
      'page at a time. Example: **LASER printers** — **L**ight **A**mplification for the '
      '**S**imulation of **E**mitted **R**adiation. Images are formed by charging dots on a '
      'plate with a laser beam; toner adheres to the charged dots and transfers to paper. '
      'Combines daisy-wheel quality with dot-matrix flexibility; more expensive. Page '
      'printers are themselves computers, containing a processor and memory (used to store '
      'fonts for automatic document preparation).',
      '**Ink-jet printer** — non-impact, character printer; electrically charged ink is '
      'sprayed through fine nozzles in a print head to form images. Capable of multicolour '
      'graphical output via a selection of ink wells connected to the print head.',
      '**Thermal transfer printer** — non-impact, character printer using thermal '
      'electro-sensitive paper (a thin coating of aluminium over a black- or blue-inked '
      'surface). Produces letter-quality text and colour graphics; expensive.',
    ]},
  ]},

  {'n': '2.4', 't': 'Central Processing Unit (CPU)', 'b': [
    {'p': 'The CPU is the **brain of the computer system**, divided into two parts: **the '
          'processor** and **the primary memory**.'},
    {'h3': '2.4.1 The computer processor'},
    {'p': 'The processor consists of the **Arithmetic-Logic Unit (ALU)** and the '
          '**Control Unit**. The set of operations the processor performs is its '
          '**instruction set**, which partly determines processing speed.'},
    {'ul': [
      '**The ALU** — where arithmetic and logic operations are carried out. Arithmetic: '
      'addition and subtraction; multiplication and division; exponentiation. Logic: '
      'comparison; branch operation (changes the order of execution); movement of data.',
      '**The Control Unit (CU)** — (i) receives instructions in a program, one at a time, from '
      'main memory; (ii) interprets the instructions; (iii) sends control signals to the '
      'peripheral devices (particularly I/O devices).',
    ]},
    {'p': 'The control unit\'s operations are coordinated by a **clock**. The number of pulses '
          '(cycles) produced per second is measured in **hertz (MHz)**, indicating processing '
          'speed. Other speed measures:'},
    {'table': {'align': 'll', 'head': ['Measure', 'Meaning'], 'rows': [
      ['MIPS', 'Million Instructions Per Second — measures the number of micro-instructions '
       '(each executed in one clock cycle) performed per second'],
      ['FLOPS', 'FLoating-point Operations Per Second — used to compare microcomputer speeds'],
    ]}},
    {'h4': 'Central processor and specialised processor'},
    {'p': 'Computers are distinguished by whether they possess a **central** or **specialised '
          '(slave)** processor.'},
    {'ul': [
      '**Central processor** — does a variety of operations; found in microcomputers.',
      '**Specialised (slave) processor** — dedicated to specialised tasks such as (i) speeding '
      'up computation and (ii) providing better graphics. Slaves are embedded into a '
      'peripheral device such as computer keyboards and printers. The development of slaves '
      'led to **Reduced Instruction Set Computing (RISC)** computers, which contain a smaller '
      'instruction set than conventional computers, increasing processor speed.',
    ]},
    {'h4': 'Processing power of the CPU'},
    {'p': '**CPU processing power** refers to the speed and capability of the CPU to execute '
          'instructions and perform calculations — essentially, how quickly and efficiently '
          'it manipulates data. It is measured in **GHz (gigahertz)**. Factors dictating '
          'higher power: clock speed; architecture; the number of cores; cache size; '
          'instructions per clock (IPC); instructions per second (IPS).'},
    {'h3': '2.4.2 The primary memory'},
    {'p': 'Also called **main** or **internal memory**. Made up of a large number of cells, '
          'each capable of storing one bit. It contains:'},
    {'ol': [
      'Programs — instructions used for processing.',
      'Data read from an input device or a secondary storage device.',
      'Intermediate results — data currently being processed, or used for processing other '
      'data.',
      'Output information ready to be sent to an output device or secondary storage.',
    ]},
    {'p': 'Data and instructions stored can be addressed and accessed very quickly — hence '
          'called **Immediate Access Storage (IAS)**. Holding programs and data in memory '
          'speeds up processing, because transferring data within memory is slower than '
          'transfer between the processor and peripherals... but memory has a small capacity, '
          'complemented by external storage (larger capacity, slower access). Data/programs '
          'for immediate use are in main memory; those for later use are in backing storage. '
          '**All data and programs must be resident in internal memory before processing can '
          'take place.** The primary memory is made from **silicon chips**, based on '
          '**Metal Oxide Semiconductor (MOS)** technology (also **MOSFET** — Metal Oxide '
          'Semiconductor Field Effect Transistor technology), and divides into **RAM** and '
          '**ROM**.'},
    {'def': {'t': 'Random Access Memory (RAM)', 'd': 'the larger part of the primary memory, '
                  'used for working storage when running application programs — it holds the '
                  'data and programs currently in use. Data can be written to or read from '
                  'RAM. "Random access" means the computer can go directly to any address in '
                  'memory and read or write data there, with the same speed regardless of '
                  'location. **Read-time** is the time to read a symbol from a cell; '
                  '**write-time** is the time to write one. RAM is expensive, and — because it '
                  'is the larger part — the primary memory is loosely called "RAM". RAM is '
                  '**volatile**: it loses its contents when the computer\'s power is shut off, '
                  'so its data and instructions are temporary/transient. Reading a symbol from '
                  'a cell normally leaves it undisturbed (**non-destructive readout**); '
                  'otherwise readout is **destructive**.'}},
    {'def': {'t': 'Read Only Memory (ROM)', 'd': 'memory in which information is permanently '
                  'written and can only be read — it cannot be written to. ROM is '
                  '**non-volatile**; micro-programs for I/O operations and the booting '
                  'programs are kept in ROM.'}},
    {'table': {'cap': 'Variants of ROM', 'align': 'll', 'head': ['Variant', 'Description'],
      'rows': [
      ['**PROM** (Programmable ROM)', 'Can be programmed by the user, unlike ROM which is '
       'pre-programmed by the manufacturer; a special device (a PROM programmer) is needed to '
       'put the bit pattern into it.'],
      ['**EPROM** (Erasable Programmable ROM)', 'Behaves like ROM, but its contents can be '
       'changed by using ultraviolet light to revert all cells to "1"s, after which new data '
       'and programs can be written onto the chip.'],
    ]}},
    {'h3': '2.4.3 Cache memory'},
    {'p': 'A high-speed memory capable of keeping up with the processor\'s processing speed. It '
          'acts as a **buffer** between the processor and the slower primary memory — since the '
          'processor is not delayed by memory accesses, overall processing speed increases. '
          'The operating system (OS) transfers segments of programs and data from disk backing '
          'storage into the cache buffer.'},
    {'def': {'t': 'Cache', 'd': 'in computing, a hardware or software component that stores '
                  'data so future requests for it can be served faster; the stored data may be '
                  'the result of an earlier computation or a copy of data stored elsewhere. A '
                  '**cache memory** in a computer is a small, high-speed memory acting as a '
                  'buffer between the CPU and main memory (RAM); it stores frequently accessed '
                  'data and instructions so the CPU can retrieve them quickly, improving overall '
                  'system performance — a temporary storage area for commonly used '
                  'information, faster to access than the main storage.'}},
    {'p': '**Purpose:** cache memory speeds up data access by storing frequently used data and '
          'instructions closer to the CPU.'},
    {'table': {'cap': 'Levels of cache memory', 'align': 'lll',
      'head': ['Level', 'Speed / size', 'Position'], 'rows': [
      ['L1', 'Fastest, smallest', 'Closest to (embedded directly within) the processor'],
      ['L2', 'Higher capacity, slower', 'Situated on the processor chip'],
      ['L3', 'Largest capacity', 'Situated on the computer that uses the L2 cache'],
    ]}},
    {'note': 'The **fastest memory in a computer system is cache memory, particularly L1**, '
             'which operates at the same speed as the CPU or faster.'},
    {'p': '**Cache memory vs CPU register:** cache memory is the fastest memory in a computer '
          'system used to store the data most frequently accessed by the CPU, while the '
          '**register** is the fastest *type* of memory — a small amount of storage available '
          'directly in the CPU for immediate data processing.'},
  ]},

  {'n': '2.5', 't': 'External storage devices', 'b': [
    {'p': 'Also called **secondary**, **auxiliary**, **backing** or **bulk** storage devices. '
          'Used to save programs and data for repeated use. They are **non-volatile**, have '
          '**higher capacity** than primary memory, and **cost far less** — but are **slower** '
          'than primary memory. Secondary storage involves both a **medium** (which stores the '
          'programs and data) and a **peripheral storage device/unit** (which has the '
          'read/write mechanism, on which the medium is mounted). Magnetic and optical '
          'technologies are used for external storage media.'},
    {'h3': '2.5.1 Magnetic storage media (disks and tapes)'},
    {'h4': '(a) Magnetic disks'},
    {'p': 'Smooth metal plates coated on both sides with a thin film of magnetic material; a '
          'set of plates fixed to a spindle, one below the other, makes up a **disk pack**. '
          'Data is held on circular, concentric **tracks** on the disk surfaces, read/written '
          'by rotating the disk past read/write heads. A set of corresponding tracks across '
          'all surfaces of a disk pack is a **cylinder**. Tracks are divided into **sectors**, '
          'and data is located by its sector. The read/write head does not touch the disk '
          'surface — it floats above it on a cushion of air, preventing wear; if a dust '
          'particle settles between the surface and the head, a **crash** results, damaging '
          'both. An exchangeable disk medium is commonly called a **hard disk**.'},
    {'h4': '(b) Winchester disk'},
    {'p': 'The head assembly is **sealed in** with the disk pack, to prevent crashing caused '
          'by dust particles. Winchester disks are **non-exchangeable**, being sealed units. '
          'Magnetic disks generally are **direct/random-access media** — records are '
          'retrieved in any sequence, independent of specific addresses.'},
    {'h4': '(c) Magnetic floppy disk (diskette)'},
    {'p': 'An exchangeable, circular, flexible disk made of magnetic-oxide-coated Mylar '
          'platters, held permanently in a rigid plastic case or square paper sleeve (which '
          'carries an identification label). Available in **3½-inch** and **5¼-inch** '
          'diameters; the 3½-inch disk is encased in a hard sleeve and does not feel floppy, '
          'unlike the 5¼-inch. The case/sleeve has openings for a movable, combined read/write '
          'head, and is inserted into the disk unit/drive on the CPU casing. The 5¼-inch disk '
          'has a square plastic envelope with a slit for read/write head access, a centre hole '
          'for the drive hub, and a hole for index-mark sensing. **Today, optical media have '
          'completely replaced magnetic floppy disks.**'},
    {'h4': '(d) Cartridge disk'},
    {'p': 'A hard disk packaged into a plastic cartridge; must be inserted into the appropriate '
          'unit to access its data and programs. Cartridges generally have more capacity than '
          'Winchester disks, and are more secure because they are removable.'},
    {'h4': '(e) Magnetic tapes'},
    {'p': 'Similar to a commonly used audio tape; **no longer in use**, superseded by disc '
          'storage (which has higher speed due to direct access). Although slow, tape is still '
          'useful for archival purposes because of its low cost. Tapes use '
          '**serial/sequential access**. The most common is the **nine-track tape**, the '
          'standard for data interchange between PCs and mainframes: eight tracks record a '
          'byte of data, and the ninth records a **parity bit** for each byte. Data are '
          'recorded in **blocks**, with an **Inter-Block Gap (IBG)** between them; the block '
          'should be at least 10 times as long as the IBG to reduce tape wastage.'},
    {'p': 'A magnetic-foil **BOT (Beginning Of Tape) marker** marks the start; on a write '
          'command, a block of data is written and the drive waits for the next block, written '
          'after the IBG — a series of blocks is written this way. A metal-tail **EOT (End Of '
          'Tape) marker** marks the end. The tape is read **sequentially** — data in the order '
          'it was written — so **data recorded on a tape cannot be addressed**.'},
    {'h4': '(f) Digital cassette tape'},
    {'p': 'A storage medium for microcomputers; cheap, but slow, with sequential retrieval. '
          'Popular because it is easily available.'},
    {'h4': '(g) Streaming tape'},
    {'p': 'Used to back up the contents of a hard disk; has much higher capacity, high speed, '
          'and is inexpensive.'},
    {'h4': '(h) Video tape recorder'},
    {'p': 'A high-density backup tape used for video and audio.'},
    {'h3': '2.5.2 Optical storage media'},
    {'def': {'t': 'Optical storage', 'd': 'devices that use laser beams to write and read data '
                  'on an optical disc.'}},
    {'p': 'Examples: CD-ROM, Compact Disc (CD), Digital Versatile Disc (DVD), Blu-ray discs — '
          'all use LASER to read and write data. Optical storage media divide into the flash '
          'EPROM and the **optical disks**, the most common of which are:'},
    {'ul': [
      '**CD-ROM (Compact Disk – Read Only Memory)** — allows the disk\'s content to be read, '
      'but data on it cannot be changed; the data is pre-recorded, read by an optical disk '
      'unit. Modern CDs can be written using a CD-writer, with data "burnt in" (the content '
      'then cannot be changed). Has higher capacity than a magnetic disk, and is more secure '
      'than a floppy disk.',
      '**WORM (Write Once Read Many)** — data can be written on, but once written it cannot be '
      'changed and can only be read repeatedly. Access is **sequential**; very large capacity; '
      'data cannot be erased. Ideal for archiving very large amounts of data.',
      '**Video disk** — an optical disk storing audio, video and text data; can be accessed a '
      'frame at a time for motionless viewing, or played like a video tape for moving action '
      'and sound. Accessed very quickly.',
      '**Magneto-optical disk** — an erasable disk with both magnetic and optical properties: '
      'a magnetised recording medium sandwiched between two plastic disks; the contents can be '
      'altered magnetically at high temperature.',
    ]},
    {'h3': '2.5.3 Solid state storage'},
    {'p': 'Often called **flash memory**; uses electronic switches (transistors) instead of '
          'moving parts to store data. Examples: **Solid State Drive (SSD)**; **USB flash '
          'drive**; memory cards such as the **SD card**; **flash EPROM disks** — today the '
          'most widely used optical storage, allowing data to be stored and erased "in a '
          'flash", very small physically but with very high storage capacity; the **SIM card** '
          'in a mobile phone, offering faster speed, durability and lower power consumption '
          'than a traditional Hard Disk Drive (HDD). Solid state storage media are '
          '**non-volatile** storage that store persistent data.'},
    {'h3': '2.5.4 Cloud storage'},
    {'def': {'t': 'The cloud', 'd': 'an extensive network of remote servers around the world '
                  'that store and manage data, run applications, and deliver content and '
                  'services (streaming video, webmail, office productivity software) over the '
                  'internet.'}},
    {'def': {'t': 'Cloud storage', 'd': 'a mode of computer data storage in which digital data '
                  'is stored on servers in off-site locations, maintained by third-party '
                  'providers who host, manage and secure the data on their infrastructure.'}},
    {'p': 'Examples of cloud storage services: Dropbox, iCloud, Google Drive, Microsoft '
          'OneDrive, Mega, Box, pCloud.'},
    {'ul': [
      '**Advantage** — it lets organisations store, access and maintain data without owning '
      'and operating their own data centre.',
      '**Disadvantages** — cloud storage hosts can be targeted by hackers; people have less '
      'control over their own data; access to data is only possible with an internet '
      'connection — no connection means no access.',
    ]},
  ]},

  {'n': '2.6', 't': 'Application controls', 'b': [
    {'p': '**Application controls** are controls over the input, processing and output '
          'processes, to:'},
    {'ul': [
      'ensure that input data is complete, accurate and valid;',
      'ensure that internal processing produces the expected results;',
      'ensure that output reports are protected from disclosure.',
    ]},
    {'h3': '2.6.1 Input controls'},
    {'p': 'These include: input authorisation; accuracy, batch controls and balancing; error '
          'reporting and handling; batch integrity in online or database systems.'},
    {'ul': [
      '**Input authorisation** — controls to ensure data has been properly authorised for '
      'input. Examples: user name; passwords; signatures on batch forms.',
      '**Batch controls and balancing** — controls to ensure total monetary amounts, total '
      'items, etc. are arithmetically correct.',
      '**Error reporting and handling** — controls to prevent erroneous data being input. '
      'Techniques: transaction log; reconciliation of data; documentation; error correction '
      'procedures; transmittal log; **version usage** (e.g. a March file cannot be used to '
      'update an April file — it should be the other way round); **file updating and '
      'maintenance authorisation** — only authorised persons can log in to update the '
      'database.',
    ]},
    {'h3': '2.6.2 Output controls'},
    {'p': 'The essence of output control is to ensure that: (i) information distributed gets '
          'to the appropriate recipient; (ii) the information distributed is correct; '
          '(iii) there is no change in the content and presentation of information between '
          'the point of processing and output.'},
    {'ol': [
      'Sensitive reports must have specific printers from which they can be printed.',
      'There must be a controlled way of distributing reports.',
      'How long sensitive reports are retained must be specified.',
      'Sensitive/confidential reports must be stored in a protected environment.',
      'There must be a screen saver on desktops where sensitive information is input.',
      'Data validation checks must prevent bad data from being stored in the database.',
    ]},
    {'table': {'cap': 'Examples of data validation checks', 'align': 'll',
      'head': ['Check', 'What it does'], 'rows': [
      ['**Control totals**', 'A control total field is held on each file stored in the '
       'database.'],
      ['**Sequence check**', 'Flags a break in sequence — e.g. 1, 2, 3, 5 is wrong because 4 '
       'should follow 3.'],
      ['**Limit check**', 'A maximum amount is set as a limit — e.g. an amount over ₦1 billion '
       'should be rejected.'],
      ['**Validity check**', 'Rejects an impossible value — e.g. "34th January 2017" is '
       'invalid because January ends on the 31st.'],
      ['**Reasonableness check**', 'Flags an implausible value — e.g. a payroll run of '
       '50 million records fails: how many employers have 50 million staff?'],
      ['**Existence check**', 'Confirms a record exists before processing — e.g. check the '
       'name exists before processing an individual\'s salary.'],
      ['**Completeness check**', 'Confirms the expected count — e.g. if there are 45 '
       'employees, the payroll file must contain 45 records, or it fails.'],
      ['**Duplicate check**', 'Surnames and first names must not be duplicated.'],
      ['**Logical relationship check**', 'Flags data with no logical relationship — e.g. there '
       'is no logical relationship between the sales figure and the MD\'s haircut expense.'],
    ]}},
    {'h3': '2.6.3 Storage controls'},
    {'p': 'Controls at the database level, where data is stored, guaranteeing that data cannot '
          'be changed while resting on the database tables. Examples:'},
    {'ol': [
      'File labelling in a particular order, to prevent accidental loss of storage media.',
      'Segregation of duty between the input officers and the storage officers.',
      'Access to storage media must be properly authorised and authenticated.',
      'Access to the database must be properly authorised and authenticated.',
      'A log file must record every activity carried out on the database.',
      'Physical security of the storage media environment, including the data processing '
      'centre.',
      'Regular file backup, and storage in a secure place, to prevent data loss.',
    ]},
  ]},

  {'n': '2.7', 't': 'Chapter summary', 'b': [
    {'p': 'The components of the hardware system are Input, Output, Storage and the CPU. The '
          'CPU is composed of the main memory and the processor (the ALU and the control '
          'unit). The three types of computer — digital, analog and hybrid — are distinguished '
          'by how they represent data. Digital computers are classified as supercomputer, '
          'mainframe, minicomputer and microcomputer, distinguished by size, heat evolved '
          'during processing, purchase price, security measures, level of usage, etc.'},
    {'p': 'The input devices use magnetic or optical technology, and can be classified as '
          'pointing devices, document readers and speech devices; the most common are the '
          'keyboard and mouse. The most common output devices are the monitor (softcopy) and '
          'the printer (hardcopy).'},
    {'p': 'Storage devices divide into the internal memory (ROM and RAM) and external storage. '
          'Internal memory is direct access and made of metal-oxide semiconductor; external '
          'memory is either direct-access or sequential-access, made of optical and magnetic '
          'technology.'},
    {'p': 'To ensure the confidentiality, integrity and availability of data, every application '
          'system needs input controls, output controls and storage controls.'},
  ]},

  {'n': '2.8', 't': 'End-of-chapter questions (study text)', 'b': [
    {'h3': 'Multiple-choice questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–33 with answers', 'open': True, 'q': [
      {'ol': [
        'Which one of the following is NOT a model? (A) Mathematical  (B) Graphical  '
        '(C) Arithmetic Operation  (D) Narrative  (E) Logical',
        'An approach to problem solving that involves using modelling theory in combination '
        'with a sampling experiment is called … (A) Mathematical model  (B) Optimisation '
        'model  (C) Monte Carlo Simulation model  (D) Linear programming model  '
        '(E) Non-linear programming model',
        'Which of the following is correct? (A) A logical description specifies the essential '
        'part while a physical description specifies the implementation  (B) A logical '
        'description specifies the implementation while a physical description specifies the '
        'essential part  (C) A logical representation gives a physical implementation  '
        '(D) A physical implementation gives a logical description  (E) Both logical and '
        'physical descriptions do not exist separately',
        'One thousand megabytes is equivalent to one … (A) Terabyte  (B) Kilobyte  '
        '(C) Gigabyte  (D) Multibyte  (E) Polybyte',
        'The brain of any computer system is the (A) Control unit  (B) Arithmetic and Logic '
        'Unit  (C) Central Processing Unit  (D) Storage Unit  (E) Memory Unit',
        'Analog computers work on which of the following inputs? (A) Continuous electrical '
        'signals  (B) Discontinuous electrical signals  (C) Magnetic strength  (D) Numerical '
        'data  (E) Alphabetic data',
        'USB is an acronym for (A) Unique Serial Bus  (B) Unique Save Bus  (C) Universal '
        'Serial Bus  (D) Ultra Serial Bus  (E) Universal System Bus',
        'Which of the following features does NOT describe a supercomputer? (A) Smaller in '
        'size and processing than microcomputers  (B) Usually used by multinational companies '
        '(C) Contains thousands of microprocessors  (D) Large in size and generates a lot of '
        'heat  (E) Used to solve complex computing problems',
        'Which one of the following is a direct input device? (A) Optical Character Reader  '
        '(B) Bar code  (C) Punch card  (D) Paper tape  (E) Optical Mark Reader',
        'Which one of the following loses its content when the computer is turned off? '
        '(A) RAM  (B) ROM  (C) CD-ROM  (D) PROM  (E) Hard disk',
        'Which ONE of the following is the role of the logic unit in a CPU? (A) Production of '
        'results  (B) Comparison of quantities or numbers  (C) Control of the flow of '
        'information  (D) Performing arithmetic computations  (E) Interpreting instructions',
        'The following are storage media for a computer system EXCEPT (A) Magnetic  '
        '(B) Hard disk  (C) Soft disk  (D) Optical disk  (E) Solid state storage disk',
        'The language that the computer understands without a translator is (A) High-level '
        'language  (B) Machine language  (C) System program  (D) Assembly language  '
        '(E) Low-level language',
        'Which one of the following is NOT a hardware component? (A) Printer  (B) Monitor  '
        '(C) Magnetic tape  (D) Microsoft Excel  (E) Smart card',
        'Which of the following is required when more than one person uses a central computer '
        'at the same time? (A) Terminal  (B) Light pen  (C) Digitizer  (D) Mouse  '
        '(E) Magnetic disk',
        'Which of the following is NOT an output device? (A) Printer  (B) Plotter  (C) Touch '
        'screen  (D) Flat-screen monitor  (E) Microfilm',
        'Which of the following is NOT an example of a pointing input device? (A) Mouse  '
        '(B) Joystick  (C) Smartcard  (D) Light pen  (E) Touch screen',
        'Examples of peripheral devices do NOT include which ONE of the following? '
        '(A) Communication terminals  (B) Printer  (C) Visual Display Unit  (D) Keyboard  '
        '(E) Internal memory',
        'All of the following are shortcomings of display equipment EXCEPT: (A) the user must '
        'be physically present to see what is displayed  (B) one cannot output with a pencil '
        'or pen  (C) output cannot be removed from the screen  (D) it encourages paper '
        'wastage  (E) the output that can be handled is limited by the screen size',
        'The following are examples of impact printers EXCEPT: (A) Line printer  (B) Drum '
        'printer  (C) Dot-matrix printer  (D) Thermal printer  (E) Daisy-wheel printer',
        'Which of the following is NOT an example of an output device? (A) Microphone  '
        '(B) Speaker  (C) Plotter  (D) Projector  (E) Headphone',
        'Which of the following is NOT a classification of printer? (A) Character printer  '
        '(B) Plot printer  (C) Page printer  (D) Ink-jet printer  (E) Line printer',
        'Which of the following is NOT a unit used for measuring the capacity of computer '
        'memory? (A) Gigabyte  (B) Multibyte  (C) Megabyte  (D) Byte  (E) Kilobyte',
        'Which one of the following combinations represents a computer processor? (A) CPU and '
        'memory  (B) Memory and control unit  (C) ALU and control unit  (D) ALU and memory  '
        '(E) CPU and motherboard',
        'Which of the following operations is performed by the control unit of the computer? '
        '(A) Perform logical comparison  (B) Receives the results of processing from the '
        'processor  (C) Interprets the instructions given to the computer  (D) Performs '
        'multiplication and division  (E) Performs addition and subtraction',
        'Which one of the following is NOT an example of an impact printer? (A) Dot-matrix '
        'printer  (B) Daisy-wheel printer  (C) Line printer  (D) Drum printer  '
        '(E) Laser-jet printer',
        'The following are types of secondary storage device EXCEPT (A) Hard disk drive  '
        '(B) Soft disk drive  (C) Optical disk drive  (D) Floppy disk drive  (E) Zip drive',
        'Which of the following is NOT a peripheral device? (A) Communication terminal  '
        '(B) Printers  (C) Visual Display Unit  (D) Keyboard  (E) Data entry device',
        'Which of the following is NOT part of the CPU? (A) Control unit  (B) Arithmetic unit  '
        '(C) Logical unit  (D) External storage  (E) Internal storage',
        'The following input devices produce direct data input into the computer EXCEPT: '
        '(A) OMR  (B) Barcode  (C) OCR  (D) MICR  (E) Magnetic disk',
        'Which one of the following is NOT an image input device? (A) Graphics tablet  '
        '(B) Cross-hair cursor  (C) OCR  (D) Image scanner  (E) Digitizing camera',
        'Which one of the following is NOT part of input controls? (A) Input authorisation  '
        '(B) Accuracy, batch controls and balancing  (C) Logical relationship check  '
        '(D) Error reporting and handling  (E) Batch integrity in online systems',
        'Which of the following is NOT an example of a validation check? (A) Sequence check  '
        '(B) Existence check  (C) Duplicate check  (D) Limit check  (E) Screen saver check',
      ]}],
      'a': [
      {'p': '**1.** C  **2.** A  **3.** B  **4.** C  **5.** A  **6.** C  **7.** D  **8.** A  '
            '**9.** A  **10.** A  **11.** B  **12.** C  **13.** B  **14.** D  **15.** A  '
            '**16.** C  **17.** C  **18.** E  **19.** D  **20.** D  **21.** B  **22.** D  '
            '**23.** B  **24.** C  **25.** C  **26.** E  **27.** B  **28.** A  **29.** D  '
            '**30.** B  **31.** B  **32.** D  **33.** E'},
      {'warn': 'Questions 1–3 examine modelling vocabulary (iconic/analogue/symbolic models, '
               'Monte Carlo simulation, logical vs physical description) rather than hardware '
               '— they are printed here in the study text\'s own chapter 2 question set, so '
               'they are reproduced as given. The printed key for **Q2 looks inconsistent** — '
               'the question\'s wording ("modelling theory combined with a sampling '
               'experiment") is the textbook definition of option **C, Monte Carlo Simulation '
               'model**, yet the key gives **A**. Both are shown; use your judgement in the '
               'exam.'}]}},
    {'h3': 'Short-answer questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–24 with answers', 'open': True, 'q': [
      {'ol': [
        'Auxiliary equipment is equipment which is offline to the …',
        'During data processing, turn-around is the time that elapses between job submission '
        'and the return of …',
        'Magnetic disk and magnetic tape are examples of external … devices.',
        'Magnetic tape can be used as both serial and … access memory.',
        'A video disk is an optical disk that can store text, pictures and … data.',
        'A computer operates under the control of instructions stored in its …',
        'The category of computer that can be used to process numeric, alphabetic and '
        'alphanumeric data is known as …',
        'A device embedded with a microprocessor chip and containing EPROM, used as a bank '
        'payment system, is called a …',
        'An output device that takes text and images displayed on a computer screen and sends '
        'them to a large screen clearly for an audience is called a …',
        'The type of memory used for storing information, external to the CPU, is called …',
        'The processor is the combination of the Arithmetic and Logic Unit (ALU) and the …',
        'A computer system is made up of hardware, software and …',
        'A suite of programs processed by the hardware, allowing it to function effectively '
        'and efficiently, is known as …',
        'A sequence of instructions written in a certain computer language, carried out by '
        'hardware to solve a given problem, is called a …',
        'The hardware device designed for transforming graphical images such as drawings, '
        'photographs and maps into machine-readable form is called a …',
        'The input device that can take pictures and immediately store them in digital memory, '
        'for display on screen, is known as a …',
        'The optical disk for storing audio, video and text data is known as a …',
        'The type of input control that prevents erroneous data from being entered into the '
        'computer system is called …',
        'A high-speed memory capable of keeping up with the processing speed of the computer '
        'processor is called …',
        'The type of memory that stores input-output operations and booting programs is '
        'called …',
        'The measure of the processing speed of the computer — the number of cycles per '
        'second — is called …',
        'The type of processor capable of performing specialised tasks such as speeding up '
        'computations is called a …',
        'The clarity of the image formed on the monitor of the computer is known as …',
        'The messages displayed on the screen/monitor of the computer, which can be seen but '
        'not touched, are called …',
      ]}],
      'a': [
      {'ol': [
        '**Central Processing Unit.**',
        '**Results or information.**',
        '**Memory or storage.**',
        '**Sequential (and direct/random) access.**',
        '**Sound.**',
        '**Primary/internal/main memory or ROM.**',
        '**Digital computers.**',
        '**Smart card.**',
        '**Projector.**',
        '**Secondary or auxiliary memory unit.**',
        '**Control unit.**',
        '**Human-ware.**',
        '**Software.**',
        '**Program.**',
        '**Image input device.**',
        '**Digital camera / copier.**',
        '**Video disk.**',
        '**Error reporting (and handling).**',
        '**Cache memory.**',
        '**Read Only Memory (ROM).**',
        '**Hertz.**',
        '**Slave (specialised) processor.**',
        '**Screen resolution.**',
        '**Softcopy.**'],
      }]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'A descriptive chapter, examined mainly through recall of classifications and lists: input '
   'vs output vs storage; direct vs indirect input; impact vs non-impact printers; RAM vs the '
   'ROM family; magnetic vs optical vs solid-state storage; and the three families of '
   'application control (input, output, storage). Learn each list as a fixed set — "name the '
   'variants of ROM", "name the types of validation check" — because Section A draws directly '
   'on them.',
 'errors': [
   'Confusing a peripheral (online) device with an auxiliary (offline) device.',
   'Saying ROM is volatile — it is RAM that is volatile.',
   'Calling a magnetic tape a direct-access medium; tape is sequential access, disk is direct '
   'access.',
   'Mixing up cache memory (a fast buffer of frequently used data) with a CPU register (the '
   'smallest, fastest storage inside the CPU itself).',
   'Listing "screen saver" as a data validation check — it is an output control, not a '
   'validation check.',
   'Confusing MICR (needs magnetic ink, used for cheques) with OCR (any special font, no '
   'special ink) and OMR (a mark in a box, read by sensing graphite).',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A support equipment currently set up to transmit data to, or receive output from, '
         'the CPU over a communications line is said to be',
    'o': ['auxiliary', 'peripheral', 'online', 'offline', 'a slave processor'],
    'a': 2,
    'w': 'Online means connected to and communicating with the CPU. Peripheral equipment is '
         'designed to be used online; auxiliary equipment is designed to work offline.',
    'src': 'Chapter 2.1.2', 'sec': '2.1'},
   {'q': 'Which of the following is a direct input device?',
    'o': ['Punched card', 'Paper tape', 'Barcode requiring conversion',
          'Optical Mark Reader (OMR)', 'Magnetic tape'],
    'a': 3,
    'w': 'OMR (like MICR and OCR) produces data already in a form suitable for processing — no '
         'conversion is needed, which is what makes it a direct input device.',
    'src': 'Chapter 2.2.1', 'sec': '2.2'},
   {'q': 'RAM is described as volatile because',
    'o': ['it can be read but not written to', 'it loses its contents when power is switched '
          'off', 'it is more expensive than ROM', 'it stores booting programs',
          'it has a smaller capacity than ROM'],
    'a': 1,
    'w': 'Volatile means the memory\'s contents are temporary and disappear once power is '
         'removed — the defining difference from non-volatile ROM.',
    'src': 'Chapter 2.4.2', 'sec': '2.4'},
   {'q': 'A memory whose contents can be erased by exposure to ultraviolet light, after which '
         'new data can be written to it, is',
    'o': ['RAM', 'ROM', 'PROM', 'EPROM', 'cache memory'],
    'a': 3,
    'w': 'EPROM (Erasable Programmable ROM) is erased with ultraviolet light, reverting all '
         'cells to "1", after which it can be reprogrammed. Plain PROM can be written once by '
         'the user but not subsequently erased this way.',
    'src': 'Chapter 2.4.2', 'sec': '2.4'},
   {'q': 'Which storage medium is read sequentially, so that the data on it cannot be '
         'addressed directly?',
    'o': ['Magnetic disk', 'Winchester disk', 'Magnetic tape', 'CD-ROM', 'Solid state drive'],
    'a': 2,
    'w': 'Magnetic tape is read in the order the data was written (serial/sequential access); '
         'disks and optical/solid-state media are direct-access.',
    'src': 'Chapter 2.5.1', 'sec': '2.5'},
   {'q': 'A validation check that rejects "34th January" as an invalid date is an example of a',
    'o': ['limit check', 'sequence check', 'validity check', 'existence check',
          'reasonableness check'],
    'a': 2,
    'w': 'A validity check rejects a value that cannot exist under the rules of the field — '
         'here, a calendar date that does not exist.',
    'src': 'Chapter 2.6.2', 'sec': '2.6'},
  ],
  'theory': [
   {'q': '(a) Computers can be classified using different attributes such as signal '
         'generation, purpose and size. (i) List and briefly explain the three classes of '
         'computer by signal generation. (ii) Enumerate any five features/characteristics '
         'each of the third and fourth generations of computers. (b) Give two examples of '
         'computers classified by purpose, and four examples classified by size.',
    'marks': 15,
    'a': [
      {'h4': '(a)(i) The three classes by signal generation'},
      {'ol': [
        '**Digital computer** — receives information in a discrete form ("ON" or "OFF"), i.e. '
        'binary digits (0s and 1s); all data used must be converted to binary form. Example: a '
        'TV channel selector.',
        '**Analog computer** — receives physical information or data in a continuous form '
        '(vibration, waves, electrical states); processes physical quantities such as '
        'temperature, pressure, speed. Examples: thermometers, speedometers, a petrol-pump '
        'filling station.',
        '**Hybrid computer** — combines the high speed of the analog machine with the '
        'flexibility of a digital system, receiving information in both discrete and '
        'continuous form. Used in hospitals, aircraft, etc., where physical quantities are '
        'measured and converted into digital data for analysis.']},
      {'h4': '(a)(ii) Features of third- and fourth-generation computers'},
      {'table': {'head': ['Third generation', 'Fourth generation'], 'align': 'll', 'rows': [
        ['Use of integrated circuits (ICs) instead of transistors',
         'Microprocessors used as switching devices'],
        ['ICs made the computer smaller, cheaper and faster',
         'Marked the arrival of microcomputers, because of microprocessors'],
        ['Marked the beginning of keyboards as input and VDU/monitor as output',
         'Improved input and output devices'],
        ['Metal oxide semiconductor replaced magnetic core memory',
         'Many high-level languages developed to solve business problems'],
        ['On-line, real-time systems became popular', 'CPU became smaller and faster'],
        ['Sophisticated operating systems were designed to aid communication',
         'Cost of computers reduced, so people could afford to buy them'],
        ['Marked the use of high-level languages, e.g. FORTRAN, COBOL',
         'Development of application packages (software)'],
      ]}},
      {'h4': '(b) Examples by purpose and by size'},
      {'ul': [
        '**By purpose:** special-purpose computers; general-purpose computers.',
        '**By size:** mainframe computers; minicomputers; supercomputers; microcomputers.']}],
    'src': 'Chapter 2.8, Q1', 'sec': '2.8'},
   {'q': '(a) List any four examples of microcomputers. (b) State two features each of '
         'mechanistic and stochastic systems. (c) Enumerate any four unpredictable '
         'disturbances that may cause a business system to deviate from its expected '
         'objectives. (d) Enumerate any five roles of information in an accounting '
         'environment.',
    'marks': 14,
    'a': [
      {'h4': '(a) Examples of microcomputers (any four)'},
      {'ul': ['Desktop computers', 'Mini tower', 'Workstation', 'Notebook computers',
              'Laptop computers', 'Palmtop computers', 'Pen computers']},
      {'h4': '(b) Mechanistic vs stochastic systems'},
      {'ul': [
        '**Mechanistic system** — states/activities follow each other predictably; operates on '
        'standard rules and regulations restricting its ability to react to its environment; '
        'output can be dictated from its inputs. Example: a computer program/software.',
        '**Stochastic system** — the outcome cannot be predicted exactly; the output cannot be '
        'dictated from the inputs with precision; it is subject to random influences from the '
        'environment. Examples: business, economic, agricultural and weather systems.']},
      {'h4': '(c) Unpredictable disturbances (any four)'},
      {'ul': [
        'Introduction of a powerful, advanced new computer technology into the market.',
        'An unexpected rise in labour costs.',
        'The failure of a supplier to deliver promised raw materials.',
        'Government legislation, etc.']},
      {'h4': '(d) Roles of information in an accounting environment (any five)'},
      {'ul': [
        'Identification of activities requiring action.',
        'It reduces uncertainty and provides a basis for choosing among alternative actions.',
        'It makes the accountant\'s decision-making process fast.',
        'It makes the accountant\'s output accurate.',
        'It enables the accountant to develop strategies and formulate policies for the '
        'survival of the profession.',
        'It enables effective planning and control.',
        'It enables accountants to monitor and gain insight into the activities of '
        'professional competitors.',
        'It enables accountants to meet customers\' requests adequately.']}],
    'src': 'Chapter 2.8, Q2', 'sec': '2.8'},
   {'q': 'A computer system is made up of two broad subsystems, namely hardware and software. '
         '(a) Define computer hardware. (b) List and state one major function of each of the '
         'five basic units of computer hardware. (c) Enumerate any eight examples of input '
         'devices.',
    'marks': 15,
    'a': [
      {'p': '**(a)** Computer hardware consists of the physical units/components making up '
            'the computer configuration, that can be seen, touched and felt.'},
      {'h4': '(b) The five basic units of computer hardware'},
      {'ol': [
        '**Input unit** — the unit through which data and information are communicated to the '
        'computer for processing, e.g. keyboard, mouse, joystick, light pen.',
        '**Output unit** — displays the data and information processed by the computer, '
        'bringing processed information from the computer to the user, e.g. monitor, printer, '
        'graph plotter.',
        '**Control unit** — controls and coordinates all the other units into one integrated '
        'unit; ensures they are properly coordinated and execute instructions; controls the '
        'transfer of data to, and within, the main memory as required by the program.',
        '**Arithmetic and Logic Unit (ALU)** — responsible for arithmetic operations '
        '(addition, subtraction, multiplication, division) and logical operations (comparison '
        'such as $=, <, >$).',
        '**Memory unit** — storage that holds data and information until needed for '
        'processing; a temporary storage area holding the data and instructions the CPU '
        'needs. Divided into Random Access Memory (RAM) and Read Only Memory (ROM).']},
      {'h4': '(c) Examples of input devices (any eight)'},
      {'ol': [
        'Mouse', 'Magnetic Ink Character Recognition (MICR)', 'Joystick',
        'Magnetic stripe card', 'Smart card', 'Optical Character Recognition (OCR)',
        'Optical Mark Recognition (OMR)', 'Scanner', 'Light pen', 'Touch screen']}],
    'src': 'Chapter 2.8, Q3', 'sec': '2.8'},
   {'q': 'Computer storage consists of a number of cells for storing data and programs. '
         '(a) Define a direct access storage device. (b) List three advantages and two '
         'disadvantages of a direct access storage device. (c) List four examples of a direct '
         'access storage device.',
    'marks': 10,
    'a': [
      {'p': '**(a)** A **Direct Access Storage Device (DASD)** is a storage device in which '
            'data can be accessed directly, regardless of the sequence or order in which the '
            'data was stored.'},
      {'p': '**(b) Advantages:** high data transfer speed; high storage capacity; data in the '
            'device is relatively easy and quick to locate. **Disadvantages:** more expensive '
            'than sequential-access media; more complex read/write mechanisms, so more prone '
            'to mechanical failure (e.g. a head crash).'},
      {'p': '**(c) Examples of DASD:** hard disk; flash drive; compact disk; diskette; '
            'magnetic drum; DVD.'}],
    'src': 'Chapter 2.8, Q4', 'sec': '2.8'},
   {'q': 'Application controls are controls over the input, processing and output processes. '
         '(a) State the essence of output controls. (b) Enumerate five examples of output '
         'controls. (c) List five examples of storage controls.',
    'marks': 13,
    'a': [
      {'p': '**(a)** The essence of output controls: (i) information distributed gets to the '
            'appropriate recipient; (ii) the information distributed is correct; (iii) there '
            'is no change in the content and presentation of information between the point '
            'of processing and output.'},
      {'p': '**(b) Examples of output controls (any five):** sensitive reports must have '
            'specific printers from which they can be printed; there must be a controlled way '
            'of distributing reports; the retention period of sensitive reports must be '
            'defined; sensitive/confidential reports must be stored in a protected '
            'environment; there must be a screen saver on desktops where sensitive '
            'information is input; data validation checks must prevent bad data being stored '
            'in the database.'},
      {'p': '**(c) Examples of storage controls (any five):** file labelling in a particular '
            'order, to prevent accidental loss of storage media; segregation of duty between '
            'input and storage officers; access to storage media properly authorised and '
            'authenticated; access to the database properly authorised and authenticated; a '
            'log file recording every activity on the database; physical security of the '
            'storage media environment, including the data processing centre; regular file '
            'backup and secure storage to prevent data loss.'}],
    'src': 'Chapter 2.8, Q5', 'sec': '2.8'},
   {'q': 'A memory is made up of a large number of cells. (a) State any four contents of the '
         'primary memory. (b) Enumerate any four distinctions between Read Only Memory (ROM) '
         'and Random Access Memory (RAM).',
    'marks': 8,
    'a': [
      {'h4': '(a) Contents of the primary memory (any four)'},
      {'ol': [
        'Programs containing instructions to be used for processing.',
        'Data that has been read from an input device or a secondary storage device.',
        'Intermediate results — data currently being processed or to be used for further '
        'processing.',
        'Output information ready to be sent to an output device or secondary storage '
        'device.']},
      {'h4': '(b) ROM vs RAM (any four distinctions)'},
      {'table': {'head': ['ROM', 'RAM'], 'align': 'll', 'rows': [
        ['Information is permanently stored', 'Information is temporarily stored (working)'],
        ['Information can only be read', 'Information can be read from and written to'],
        ['Smaller than RAM', 'Bigger than ROM'],
        ['Non-volatile — does not lose its content on power failure',
         'Volatile — its content is lost on power failure'],
        ['Less expensive than RAM', 'Very expensive'],
      ]}}],
    'src': 'Chapter 2.8, Q6', 'sec': '2.8'},
  ]},
}
