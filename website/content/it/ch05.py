CH = {
 'n': 5,
 't': 'Computer Networks and Data Communication',
 'brief': 'Network types and topologies, protocols and the OSI model, the Internet/intranet/'
          'extranet, transmission media, modes and equipment, the Internet\'s other '
          'applications (email, e-banking, EDI, telecommuting, teleconferencing, social '
          'media), electronic payment platforms and cloud computing.',
 'outcomes': [
   'Understand what networks are',
   'Distinguish among the three major types of networks (LANs, MANs and WANs)',
   'Understand the issues concerned with network security',
   'Understand major applications of the Internet',
   'Understand what is meant by computer crimes and how these can be managed',
   'Understand what computer viruses and worms are and how to deal with them',
 ],
 'secs': [
  {'n': '5.1', 't': 'Computer networks', 'b': [
    {'def': {'t': 'Computer network', 'd': 'an interconnection of a number of computers, '
                  'telephones and other shared devices, in various ways, so that users can '
                  'process and share information.'}},
    {'p': 'Networks make it possible for users to: share peripheral devices, programs and '
          'data; engage in better communication; have more secure information; and have '
          'access to databases.'},
    {'h3': 'Types of networks'},
    {'ul': [
      '**Wide Area Network (WAN)** — a communications network covering a wide geographical '
      'area, such as a region of a country or an entire country. The Internet links together '
      'several computer WANs; most telephone networks are typical examples of WANs.',
      '**Metropolitan Area Network (MAN)** — a communications network covering a geographical '
      'area the size of a town, a suburb of a city, or an entire city.',
      '**Local Area Network (LAN)** — a privately owned communications network operating in a '
      'confined geographical area, usually within a kilometre — within a building, a number of '
      'buildings close together, or the campus of an educational institution.',
    ]},
    {'p': 'Local networks are either **Private (Automatic) Branch Exchanges (PABX)** or '
          '**Local Area Networks (LANs)**.'},
    {'def': {'t': 'Private Branch Exchange (PABX)', 'd': 'a private or leased telephone '
                  'switching system that connects telephone extensions in-house, and often '
                  'also to the outside telephone system. Apart from analog telephones, a PABX '
                  'can also handle digital equipment, including computers, and often shares '
                  'existing telephone lines with the telephone system.'}},
    {'def': {'t': 'Remote Job Entry (RJE)', 'd': 'a computing process that allows users to '
                  'submit tasks or jobs to a central computer from a remote location — commonly '
                  'used in networked environments where multiple users need to process data on '
                  'a mainframe or large server without direct access.'}},
  ]},

  {'n': '5.2', 't': 'Network topology and protocol', 'b': [
    {'def': {'t': 'Topology (configuration)', 'd': 'the logical layout or shape of a network — '
                  'the manner in which the component computers are physically connected.'}},
    {'def': {'t': 'Protocol', 'd': 'the set of rules that governs the way information is '
                  'carried over the network.'}},
    {'h3': '5.2.1 Components of a LAN'},
    {'ul': [
      '**Connection or cabling** — LANs are wired or wireless. Wired networks may use '
      'twisted-pair wires, coaxial cables or fibre-optic cables; wireless networks use '
      'infra-red or radio waves.',
      '**Network interface card (NIC)** — each computer on the network requires one, to send '
      'and receive messages on the LAN.',
      '**Network operating system** — the software that manages activities on the network.',
      '**Other shared devices** — printers, fax machines, scanners and storage devices may be '
      'added to the network and shared by all users.',
      '**Bridges, routers and gateways** — a LAN may stand alone or connect to other networks; '
      'a bridge or router facilitates communication between similar networks, while a '
      '**gateway** lets dissimilar networks communicate (e.g. a LAN with a WAN).',
    ]},
    {'h3': '5.2.2 LAN topologies'},
    {'h4': '(a) Star network'},
    {'p': 'All PCs and communication devices connect to a **central server** — a typical '
          'client/server LAN. No client communicates directly with other clients; messages are '
          'routed through the server, which monitors traffic flow. **Advantages:** the server '
          'prevents message collisions, and if a connection between a device and the server '
          'breaks, the rest of the network keeps functioning. **Disadvantage:** a server '
          'breakdown renders the whole network inoperative. A PABX system is an example of a '
          'star network.'},
    {'h4': '(b) Ring (or loop) network'},
    {'p': 'All devices are connected in a **continuous loop** — a typical peer-to-peer LAN, '
          'with no server. Messages flow in only one direction, so there is no danger of '
          'collisions; however, if a connection is broken, the entire network may stop '
          'working. A user who wants to send information must be allocated a **"bit token"** '
          '(0 or 1) indicating permission to send.'},
    {'h4': '(c) Bus network'},
    {'p': 'All communication devices connect to a **common channel**. If a connection breaks, '
          'the network may stop working. May be organised as client/server or peer-to-peer; a '
          'signal from any device moves in both directions to the ends of the bus. Imminent '
          'message collisions are detected by the protocol **Carrier Sense Multiple Access/'
          'Collision Detection (CSMA/CD)**, which delays messages and later allows retransmission.'},
    {'h4': '(d) Tree network topology'},
    {'p': 'A **hierarchical structure** combining elements of bus and star topologies — a root '
          'node at the top with multiple branches extending downward, each with multiple child '
          'nodes. Commonly used in large networks (corporate structures, academic '
          'institutions), for efficient data management and scalability.'},
    {'p': '**Key features:** hierarchical structure (nodes arranged in levels, easy to expand); '
          'scalability (more devices without disrupting the network); centralized management '
          '(a main node oversees traffic); combines star and bus aspects; improved fault '
          'isolation (issues in one branch need not affect the whole network).'},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Supports large networks efficiently', 'Higher cost, due to extensive cabling'],
      ['Easily scalable and organized', 'If the root node fails, the whole network may '
       'collapse'],
      ['Facilitates troubleshooting within different segments', 'Complex structure can lead '
       'to difficult maintenance'],
    ]}},
    {'h4': '(e) Mesh network topology'},
    {'p': 'Each node connects directly to many other nodes, creating multiple paths for data '
          'to travel — improving reliability and redundancy, so that even if one connection '
          'fails, data can take alternative routes.'},
    {'p': 'Types of mesh network: **(1) Full mesh** — every node connects to every other node, '
          'maximum redundancy; **(2) Partial mesh** — only some nodes have multiple '
          'connections, balancing cost and efficiency.'},
    {'table': {'align': 'll', 'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['High reliability — multiple paths prevent single points of failure', 'High setup '
       'cost — more cabling and configuration required'],
      ['Efficient data routing — dynamic routing ensures fast communication', 'Complex '
       'maintenance — managing multiple connections can be difficult'],
      ['Scalability — easy to expand by adding new nodes', 'Higher power consumption — '
       'wireless mesh networks require more resources'],
      ['Enhanced security — decentralized nature makes attacks harder', ''],
    ]}},
    {'h3': '5.2.3 Metropolitan Area Network (MAN)'},
    {'p': 'A wide area network limited to the area surrounding a city or town, covering a '
          'large group of buildings within a diameter of up to **50 km**. By interconnecting '
          'smaller networks within a large geographical area, information is easily '
          'disseminated throughout the network. Example: Guaranty Trust Bank in Lagos '
          'connecting all GTB branches in the Lagos area to a centralised server at the head '
          'office, using dedicated telephone lines, coaxial cable and wireless communication.'},
    {'table': {'cap': 'Advantages and disadvantages of networks', 'align': 'll',
      'head': ['Advantages', 'Disadvantages'], 'rows': [
      ['Sharing of peripheral devices — several users share printers, scanners and disk '
       'drives, keeping costs down', 'Duplication of data on files of different computers on '
       'the network'],
      ['Sharing of programs and data — a common database on shared storage, plus common '
       'software; files are easier to update on a server than on separate computers',
       'Difficulty in administration and control, especially for large combinations'],
      ['Better communication — information may be shared in real time; e-mailing is '
       'facilitated', 'Maintenance cost may be prohibitive'],
      ['Security of information — more readily backed up on networked storage; data '
       'integrity is easily ensured with a central database, and a single input updates data',
       'Need for compatibility of equipment in the network'],
      ['Access to databases — it is possible to tap into other external databases, private '
       'or public', 'Failure of the server may result in operational downtime'],
      ['', 'A cable break may stop the entire network'],
    ]}},
    {'h3': '5.2.4 LAN security issues'},
    {'p': 'The complexity of LANs makes a number of breaches possible: (a) passwords and '
          'unauthorised access; (b) computer viruses; (c) encryption.'},
    {'def': {'t': 'Password', 'd': 'a sequence of characters entered into a computer system to '
                  'gain access to the system, or to some part of it. Use of passwords should be '
                  'properly monitored and controlled so passwords are not leaked to or copied '
                  'by others, and should be changed regularly (possibly monthly) — their '
                  'objective is to restrict access to the LAN, or a resource on it, to only '
                  'authorised users.'}},
    {'def': {'t': 'Cryptography', 'd': 'used in information security to transform usable '
                  'information into a form unusable by anyone other than the authorised user — '
                  'a process called **encryption**. The encrypted information can be '
                  'transferred back to its original usable form by an authorised user who '
                  'possesses the cryptographic key — a process called **decryption**. Used to '
                  'protect information from unauthorised or accidental disclosure, while in '
                  'transit or storage.'}},
    {'p': 'Encryption and decryption use an **algorithm** and a **key**; the algorithm '
          'transforms data into cipher, and the key controls the algorithm — changing the key '
          'value changes the effect of the algorithm, so each key value gives a completely '
          'different conversion. Using appropriate software, the sending computer encrypts the '
          'message, and the receiving computer decrypts it; anyone intercepting the message '
          'without the key cannot decipher it.'},
    {'h3': '5.2.5 Protocol'},
    {'def': {'t': 'Protocol', 'd': 'the set of rules and procedures for exchanging information '
                  'between computers on the network, defining how the communication link is '
                  'established, how information is transmitted, and how errors are detected and '
                  'corrected. Using the same protocols, different types and makes of computers '
                  'can communicate with each other.'}},
    {'table': {'cap': 'Examples of protocols', 'align': 'll', 'head': ['Protocol', 'Description'],
      'rows': [
      ['**Ethernet**', 'The most widely used protocol for LANs.'],
      ['**Token ring**', 'Uses an electronic token to avoid transmission conflict, allowing '
       'only one device to transmit at a time.'],
      ['**FDDI**', 'Fiber Distributed Data Interface — a high-speed fibre-optic protocol.'],
      ['**TCP/IP**', 'Transmission Control Protocol and Internet Protocol — carries out the '
       'basic operations of the internet.'],
      ['**ATM**', 'Asynchronous Transfer Mode — developed for transmitting voice data and '
       'video over any type of media.'],
      ['**IPX**', 'Used for Novell Netware networks.'],
      ['**UDP**', 'User Data Protocol — used together with IP when small amounts of '
       'information are involved.'],
      ['**ICMP**', 'Internet Control Messages Protocol — defines a small number of messages '
       'used for diagnostic and management purposes.'],
      ['**HTTP**', 'Hypertext Transfer Protocol — used to access and download content from '
       'web pages. HTTPS is a secured HTTP.'],
      ['**POP**', 'Post Office Protocol — for the exchange of emails.'],
      ['**SMTP**', 'Simple Mail Transfer Protocol — the most common protocol for sending mail.'],
      ['**FTP**', 'File Transfer Protocol — a method for copying files over a network from one '
       'computer to another.'],
    ]}},
  ]},

  {'n': '5.3', 't': 'The Internet Protocol', 'b': [
    {'p': 'The Internet Protocol — the standard language of the Internet, **Transmission '
          'Control Protocol/Internet Protocol (TCP/IP)** — has been available since **1983**. '
          'It is the standardised set of guidelines that allows different computers on '
          'different networks to communicate with each other efficiently, no matter how they '
          'gained access to the Net.'},
    {'h3': '5.3.1 The 7-layer OSI model'},
    {'def': {'t': 'Open Systems Interconnection (OSI) model', 'd': 'a conceptual model that '
                  'characterizes and standardizes the communication functions of a '
                  'telecommunication or computing system, without regard to their underlying '
                  'internal structure and technology — defining a networking framework to '
                  'implement protocols in seven layers.'}},
    {'table': {'cap': 'The seven OSI layers', 'align': 'll', 'head': ['Layer', 'Function'],
      'rows': [
      ['**1. Physical**', 'Conveys the bit stream — electrical impulse, light or radio signal '
       '— through the network at the electrical and mechanical level; provides the hardware '
       'means of sending and receiving data on a carrier, including cables, cards and physical '
       'aspects.'],
      ['**2. Data Link**', 'Encodes and decodes data packets into bits; furnishes '
       'transmission-protocol knowledge and management, and handles errors in the physical '
       'layer, flow control and frame synchronization.'],
      ['**3. Network**', 'Provides addressing services and error handling.'],
      ['**4. Transport**', 'Provides transparent transfer of data between end systems, and '
       'ensures complete data transfer.'],
      ['**5. Session**', 'Establishes, manages and terminates connections between '
       'applications.'],
      ['**6. Presentation**', 'Transforms data into the form the application layer can '
       'accept.'],
      ['**7. Application**', 'Supports application and end-user processes; provides '
       'application services for file transfers, e-mail and other network software services.'],
    ]}},
  ]},

  {'n': '5.4', 't': 'The Internet', 'b': [
    {'def': {'t': 'The Internet', 'd': 'a network of networks — a series of networks using '
                  'very precise rules that allow any user to connect to, and use, any '
                  'available network or computer connected to it. Created by the US Department '
                  'of Defense in **1969** under the name **ARPAnet** (ARPA = Advanced Research '
                  'Project Agency), built to serve two purposes: to share research among '
                  'military, industry and university scholars; and to provide a system for '
                  'sustaining communication among military units in the event of nuclear '
                  'attack.'}},
    {'h3': '5.4.1 Using the Internet'},
    {'p': 'There are no formalised rules about how to behave on the Internet; over the years a '
          'code of conduct, sometimes called **network ethics**, has evolved. Rules governing '
          'the Internet rest with the **Internet Society** (a voluntary organisation) which, '
          'through the **Internet Architecture Board (IAB)**, sets standards and the rules for '
          'accessing and using addresses.'},
    {'p': 'The addressing system uses a process called the **Domain Name System (DNS)**. '
          'Internet addresses are numerical — **IP Addresses** (e.g. `128.116.24.3`) — but most '
          'users never see them directly, because the DNS provides a more meaningful, '
          'easier-to-remember name; the host computer converts a DNS name to an IP address in '
          'the background.'},
    {'p': 'A DNS name is made up of a **domain** and one or more **sub-domains** — e.g. '
          '`www.ed.ati.edu` uses the domain **edu** (educational institution) and has three '
          'sub-domains, **ati, ed, www**, each identifying a particular computer or network. '
          'Read backwards: the educational institution Accountancy Training Institute (ati), '
          'using the education (ed) computer, available on the web (www). The DNS is specific '
          'to a computer.'},
    {'table': {'cap': 'Popular domains', 'align': 'll', 'head': ['Domain', 'Meaning'], 'rows': [
      ['`.com` / `.co`', 'Commercial'],
      ['`.edu` / `.ac`', 'Educational (university)'],
      ['`.gov`', 'Governmental'],
      ['`.mil`', 'Military'],
      ['`.org`', 'Organisation'],
      ['`.net`', 'Network'],
    ]}},
    {'p': 'Because the Internet is worldwide, some addresses also include the country, e.g. '
          '`.ng` (Nigeria), `.us` (US), `.uk` (UK), `.gh` (Ghana).'},
    {'p': 'The **web** consists of an interconnected system of sites all over the world that '
          'can store information in multimedia form — sounds, photos, video, text — sharing a '
          'form consisting of a hypertext series of links connecting similar words and '
          'phrases.'},
    {'def': {'t': 'Hypertext', 'd': 'a system in which documents scattered across many '
                  'Internet sites are directly linked, so that a word or phrase in one document '
                  'becomes a connection to an entirely different document.'}},
    {'p': 'The format used on the web is **Hypertext Mark-up Language (HTML)**, which swaps '
          'information using **Hypertext Transfer Protocol (HTTP)**. To find a particular '
          'website, one needs its **URL (Uniform Resource Locator)** — an address that points '
          'to a specific resource on the web — reached via a **web browser**.'},
    {'p': 'Popular web browsers: Netscape Navigator, Microsoft Internet Explorer, Google '
          'Chrome, Mozilla Firefox, Microsoft Edge, Brave, Opera, Vivaldi, Safari, Tor Browser. '
          'Searching the Internet is done via a **search engine** (Google, Yahoo!, Bing, '
          'DuckDuckGo, Baidu, Yandex, Ecosia, Ask.com, etc.), typing a word or phrase to find '
          'related websites. The **Wireless Application Protocol (WAP)** allows mobile phones '
          'to interact with the web in a wide range of ways.'},
    {'h3': '5.4.2 Current uses of the Internet'},
    {'ol': [
      'Dissemination of information;',
      'Product/service development;',
      'Transaction processing — both business-to-business and business-to-consumer;',
      'Relationship enhancement;',
      'Recruitment and job search;',
      'Entertainment;',
      'Education; and',
      'Religion.',
    ]},
    {'h3': '5.4.3 Internet security issues'},
    {'p': 'Establishing organisational links to the Internet brings numerous security risks:'},
    {'ol': [
      'A virus on a single computer can easily spread through the network to all of the '
      'organisation\'s computers.',
      'Disaffected employees can deliberately damage valuable corporate data or systems, '
      'because the network may give them access to parts of the system they are not '
      'authorised to use.',
      'Where the organisation is linked to an external network, outsiders may gain access to '
      'steal information or damage the system.',
      'Employees may download inaccurate information, or imperfect or virus-ridden software, '
      'from external networks.',
      'Information transmitted between parts of the organisation may be intercepted — '
      '**encryption** may be used to check this, by scrambling data at one end and '
      'unscrambling it at the receiver\'s end.',
      'The communication link itself may break down or distort data.',
    ]},
  ]},

  {'n': '5.5', 't': 'Intranet and extranet', 'b': [
    {'h3': '5.5.1 Intranet'},
    {'def': {'t': 'Intranet', 'd': 'an internal corporate network that uses the infrastructure '
                  'and standards of the Internet and the World Wide Web, able to connect all '
                  'types of computers in an organisation.'}},
    {'p': 'A major intranet consideration is **security**: because the network is connected to '
          'external networks, outsiders without access rights may gain access to the corporate '
          'network. This is checked by installing security software called a **firewall**.'},
    {'def': {'t': 'Firewall', 'd': 'a security program that connects the intranet to external '
                  'networks such as the Internet, and blocks unauthorised traffic (including '
                  'unauthorised employees) from entering the intranet.'}},
    {'h3': '5.5.2 Extranet'},
    {'def': {'t': 'Extranet', 'd': 'a type of intranet that is accessible to outsiders, but '
                  'limited to only those with valid user identification numbers — a prospective '
                  'user must enter a valid identification number before access is granted.'}},
  ]},

  {'n': '5.6', 't': 'Data transmission media', 'b': [
    {'def': {'t': 'Transmission media', 'd': 'the physical materials and non-physical means '
                  'used to establish communication through which data is transmitted from one '
                  'computer/device to another. Two categories: **physical cabling media** and '
                  '**wireless media**.'}},
    {'h3': '5.6.1 Physical cabling media'},
    {'ul': [
      '**Twisted-pair cable** — pairs of plastic-coated copper wires twisted together to '
      'reduce electrical interference; two types (shielded and unshielded twisted pair). '
      'Inexpensive and easily installed; commonly used for telephone lines.',
      '**Coaxial cable** — a high-quality communication line: a copper wire conductor '
      'surrounded by an insulator. Not susceptible to electrical interference; transmits data '
      'faster over long distances; often used with computer networks.',
      '**Fibre-optic cable** — uses smooth hair-thin strands of glass or plastic to transmit '
      'data as pulses of light. Advantages over wire cables: substantial weight and size '
      'savings; reduced electrical and magnetic interference; increased transmission speed. '
      'Costs more than twisted pair/coaxial and can be difficult to install/modify; used for '
      'high-capacity telephone lines.',
    ]},
    {'h3': '5.6.2 Wireless media'},
    {'p': 'Wireless networks let devices communicate without physical cables — essential from '
          'home Wi-Fi to global mobile networks.'},
    {'h4': 'Types of wireless networks'},
    {'ol': [
      '**Wi-Fi (Wireless Fidelity)** — used for home, office and public internet access.',
      '**Cellular networks** — 3G, 4G LTE and 5G, providing mobile connectivity.',
      '**Bluetooth** — short-range communication for devices like headphones and smartwatches.',
      '**Satellite networks** — enable global communication, including GPS and internet access '
      'in remote areas.',
    ]},
    {'p': '**Advantages of wireless networks:** mobility (connect from anywhere within range); '
          'flexibility (easily scalable); reduced infrastructure costs (no extensive cabling); '
          'remote access (enables cloud computing and IoT applications).'},
    {'p': '**Challenges:** security (susceptible to hacking without proper encryption); '
          'interference (from other electronic devices and physical obstacles); bandwidth '
          'limitations (can be slower than wired, especially when congested); latency '
          '(wireless signals may delay real-time applications like gaming and video calls).'},
    {'p': '**Future developments:** 5G expansion (faster speeds, lower latency); Wi-Fi 7 '
          '(higher data transfer rates); IoT and smart cities; satellite internet (e.g. '
          'Starlink) for remote areas.'},
    {'h4': 'Examples of wireless media'},
    {'ul': [
      '**Microwaves** — radio waves providing high-speed transmission of voice and digital '
      'signal; limited to **line-of-sight** transmission (must travel in a straight line).',
      '**Carrier-connect radio** — used to transmit data between devices in the same area.',
      '**Infrared light** — infrared light beams transmit data between personal computer '
      'devices without a cable.',
    ]},
    {'note': 'Local wireless systems provide flexibility and portability, but are slower and '
             'more susceptible to interference than wired connections.'},
  ]},

  {'n': '5.7', 't': 'Mode of transmission', 'b': [
    {'ul': [
      '**Simplex transmission** — data flows through a channel in only **one direction**, e.g. '
      'radio and television transmission.',
      '**Half-duplex transmission** — signals pass through the channel in both directions, but '
      '**one direction at a time**, e.g. a walkie-talkie or radio phoning.',
      '**Duplex (full-duplex) transmission** — signals pass through the channel **in both '
      'directions at the same time**, e.g. found on computers.',
      '**Synchronous transmission** — high-speed digital transmission between sending and '
      'receiving stations at a **constant rate**, synchronised by a clock keeping the devices '
      'in step with each other.',
      '**Asynchronous transmission** — uses start and stop signals between blocks of '
      'characters rather than individual characters; one character is sent at a time — '
      'economical and efficient, but cannot cope with large quantities of data.',
    ]},
  ]},

  {'n': '5.8', 't': 'Data transmission equipment', 'b': [
    {'p': 'Equipment used during the communication of data and signals from one station to '
          'another:'},
    {'h4': '5.8.1 Modems'},
    {'def': {'t': 'Modem', 'd': 'communication equipment that converts a computer\'s digital '
                  'signals to analog signals and vice versa. "Modem" comes from '
                  '**mo**dulate — to change into an analog signal — and **dem**odulate — to '
                  'convert an analog signal to digital. Modems are needed at both the sending '
                  'and receiving ends of a transmission channel for data transmission to '
                  'occur.'}},
    {'h4': '5.8.2 Multiplexers (MUX)'},
    {'def': {'t': 'Multiplexer (MUX)', 'd': 'combines two or more input signals from several '
                  'devices into a single stream of data and transmits it over a communications '
                  'channel — increasing the efficiency of communication and reducing the cost '
                  'of using individual communication channels.'}},
    {'h4': '5.8.3 Front-End Processor (FEP)'},
    {'def': {'t': 'Front-End Processor (FEP)', 'd': 'a small computer attached to, and '
                  'dedicated to handling the communication requirements of, the central '
                  'computer — relieving the central computer to focus on processing data while '
                  'the FEP communicates it.'}},
    {'p': 'Other tasks of the FEP: (a) **polling** — checking attached terminals for data to be '
          'sent; (b) error-checking and correction; and (c) ensuring access security.'},
    {'h4': '5.8.4 Network Interface Card (NIC)'},
    {'def': {'t': 'Network Interface Card (NIC)', 'd': 'a circuit card that fits in an '
                  'expansion slot of a computer or other device (e.g. a printer), letting the '
                  'device connect to the network. Most NICs require a cable connection and have '
                  'connectors for different cable types; the NIC coordinates the transmission '
                  'and receipt of data and error-checks transmitted data.'}},
    {'h4': '5.8.5 Hub/switch'},
    {'def': {'t': 'Hub', 'd': 'a communication device used to connect a computer to the '
                  'network, directing information around the network to facilitate '
                  'communication between all connected devices.'}},
    {'def': {'t': 'Switch (concentrator)', 'd': 'a device that provides a central connection '
                  'point for cables from workstations, servers and peripherals — e.g. in a star '
                  'topology, twisted-pair wire runs from each workstation to a central switch. '
                  'Switches are inexpensive, so new installations now use them instead of hubs, '
                  'as they give better performance and faster data transmission.'}},
    {'h4': '5.8.6 Bridges'},
    {'def': {'t': 'Bridge', 'd': 'a combination of hardware and software used to connect '
                  'similar networks — e.g. connecting a company\'s separate accounting and '
                  'marketing LANs. A bridge monitors information traffic on both sides of the '
                  'network so it can pass packets to the correct location, and can accommodate '
                  'connection of different types of cabling.'}},
    {'h4': '5.8.7 Routers'},
    {'def': {'t': 'Router', 'd': 'an intelligent network-connecting device that sends or '
                  'routes communication traffic directly to the appropriate networks, and can '
                  'translate information from one network to another. It selects the best path '
                  'for a message based on destination address and origin, implements several '
                  'routing protocols, and can determine alternate routes in case of partial '
                  'network failure.'}},
    {'h4': '5.8.8 Gateway'},
    {'def': {'t': 'Gateway', 'd': 'a combination of hardware and software that allows users of '
                  'one network to access resources on a different type of network, by '
                  'performing the necessary protocol conversions to let incompatible systems '
                  'exchange data.'}},
    {'h4': '5.8.9 Repeaters'},
    {'def': {'t': 'Repeater', 'd': 'a device used to regenerate (amplify or restore) signals '
                  'in communication links — electrically amplifying a received signal and '
                  'rebroadcasting it, since a signal loses strength as it passes along a cable '
                  '(**attenuation**), which the repeater helps to overcome.'}},
  ]},

  {'n': '5.9', 't': 'Other applications of the Internet', 'b': [
    {'h3': '5.9.1 Electronic mail (e-mail)'},
    {'p': 'Electronic mail systems replace the movement of paper messages with the electronic '
          'transmission of coded, graphic or textual information; a mail can be sent to or '
          'received by several people at different locations and time zones, using computers '
          'or telephones. Information is "posted" by the sender to a central computer, which '
          'allocates disk storage as a "mailbox" for each user, and is later "collected" by the '
          'receiver using e-mail software. Each person needs an e-mail address (e.g. '
          '`mustapha@yahoo.com`), and typically a password protecting their inbox, outbox and '
          'filing system.'},
    {'p': '**Advantages of e-mail:** **speed** (transmission is electronic, almost '
          'instantaneous); **economy** (several times cheaper than fax or ordinary post); '
          '**efficiency** (a message is prepared once but transmitted to several people at '
          'different locations/time zones); **security** (access generally restricted by '
          'passwords); **attachments** can send documents, reports and memoranda.'},
    {'p': '**Shortcomings of e-mail:** the medium can lose the full import of a message, since '
          'users tend to be informal/casual; not suited to messages needing detailed '
          'discussion; likelihood of information overload; e-mails may be unduly delayed and '
          'virus infection is common.'},
    {'h3': '5.9.2 Social and business communication on the internet'},
    {'def': {'t': 'Website', 'd': 'a collection of related, interconnected web pages, '
                  'including multimedia content, typically identified with a common domain '
                  'name and published on at least one web server — an online presence for '
                  'individuals, businesses, organizations and communities. Websites can be '
                  '**static** (fixed content) or **dynamic** (interactive, regularly updated '
                  'content).'}},
    {'p': '**Key components of a website:** domain name (web address, e.g. `www.example.com`); '
          'web pages (sections of content — text, images, videos, links); hosting server '
          '(stores website files and makes them accessible online); navigation menu (helps '
          'users move between pages); user interface (design and layout ensuring usability).'},
    {'p': '**Types of websites:** **(1) personal websites** (blogs, portfolios, personal '
          'branding); **(2) business websites** (products, services, company details); '
          '**(3) e-commerce websites** (online stores); **(4) social media websites** (e.g. '
          'Facebook, Twitter); **(5) educational websites** (learning resources, courses, '
          'tutorials).'},
    {'def': {'t': 'Web page', 'd': 'what one sees on the screen after typing in a web address, '
                  'clicking a link, or putting a query into a search engine.'}},
    {'def': {'t': 'Blog', 'd': 'an online platform where individuals or groups regularly '
                  'publish content on various topics, in a personal or professional capacity, '
                  'covering subjects such as travel, technology, lifestyle, business, etc.'}},
    {'p': '**Key features of a blog:** regular updates (new posts added frequently); personal '
          'or professional voice; engagement (readers can comment/interact); chronological '
          'structure (most recent post first).'},
    {'p': '**Types of blogs:** **(1) personal blogs** (diary-like, personal stories); '
          '**(2) business blogs** (industry insights, updates, marketing content); '
          '**(3) niche blogs** (a specific topic — food, travel, tech, fashion); **(4) news '
          'blogs** (current events, politics, trends).'},
    {'h3': '5.9.3 Methods of interacting with the internet'},
    {'ul': [
      '**Browsing** — viewing information and documents from various websites and web pages '
      'casually, without a specific focus.',
      '**Surfing (web surfing)** — browsing the internet by going from one page to another '
      'using hyperlinks.',
      '**Uploading** — sending files and documents to the internet for authorised users to '
      'access.',
      '**Downloading** — extracting or getting information, files and documents from the '
      'internet for use, e.g. downloading messages sent to one\'s e-mail.',
    ]},
    {'h3': '5.9.4 Electronic Commerce (e-Commerce)'},
    {'def': {'t': 'Electronic commerce', 'd': '"trading on the Internet" — the use of the '
                  'Internet and websites in the sale of products or services; the application '
                  'of advanced technology to increase the effectiveness of commercial '
                  'practices. It allows businesses to reach millions of consumers worldwide '
                  'and extends trading time to seven days a week, around the clock. For '
                  'established companies, it reduces expensive sales/distribution workforces '
                  'and offers new marketing opportunities.'}},
    {'p': 'Anything convertible into digital form can be placed on a seller\'s site and '
          'downloaded onto a customer\'s PC — a large number of software products are '
          'distributed this way. Websites can provide sound, movement and interactivity, '
          'letting users drill down for more information, watch a product video, or get a '
          'virtual reality experience. First-time visitors are asked to register (name, '
          'address, e-mail, and possibly demographic data); on later visits they either type '
          'a username/password or, more usually, the website recognises them via a '
          '**cookie** — a small file containing a string of characters that uniquely '
          'identifies the computer. As users visit more often, the site learns more about them '
          'by recording what they click on — known as **clickstreams**.'},
    {'h3': '5.9.5 Electronic banking (e-banking)'},
    {'def': {'t': 'Electronic banking (e-banking)', 'd': 'engaging in banking activities by '
                  'means of computers and telecommunications. A bank may provide customers with '
                  'software and telecommunication facilities, including modems and special '
                  'codes to identify themselves online.'}},
    {'p': 'Without visiting the bank\'s premises, customers can request account balances, '
          'advise on transfers, and discuss account status online; the feature is also '
          'available on cellular phones, giving account information wherever one is.'},
    {'h3': '5.9.6 Electronic Data Interchange (EDI)'},
    {'def': {'t': 'Electronic Data Interchange (EDI)', 'd': 'the direct electronic exchange of '
                  'standard business documents — such as purchase orders, invoices and '
                  'shipping documents — between organisations\' computer systems. Requires '
                  'compatible computer systems between the organisations; used where a firm '
                  'engages in purchases and sales with other companies via electronic '
                  'communication rather than paper documents.'}},
    {'note': 'EDI places a great burden on auditors, because electronic transactions are '
             'difficult to verify.'},
    {'h3': '5.9.7 Telecommuting'},
    {'def': {'t': 'Telecommuting', 'd': 'employees working from their homes or other locations '
                  'outside their offices.'}},
    {'p': '**Advantages to employers:** less expense on office space and furniture; less '
          'office utility bills; engagement of scarce human resources not willing to take a '
          'full-time appointment; companies can engage personnel outside their localities, '
          'even in other countries; companies in high-security areas may keep prized staff '
          'off-site as part of talent management.'},
    {'p': '**Disadvantages to employers:** difficulty controlling employees; less security of '
          'data and confidential information; higher communication costs.'},
    {'p': '**Advantages to employees:** less time and expense travelling to/from work; more '
          'flexibility in working times; depending on the home environment, fewer '
          'interruptions; opportunities for workers who cannot find full-time employment '
          'feasible.'},
    {'p': '**Disadvantages to employees:** comfort in the home is compromised; some social '
          'rewards available from the office setting may be lost.'},
    {'h3': '5.9.8 The virtual office'},
    {'def': {'t': 'Virtual office', 'd': 'a non-permanent, mobile office run with computer and '
                  'communications technology — using pocket pagers, portable computers, fax '
                  'machines and various phone/network services, employees work from home, cars '
                  'and other locations rather than a central office.'}},
    {'h3': '5.9.9 Teleconferencing'},
    {'def': {'t': 'Teleconferencing', 'd': 'employees or business associates at different '
                  'locations hold joint meetings by means of video, audio and data '
                  'communications. One application of interest is teaching, where lecturers '
                  'lecture and answer questions from remote locations.'}},
    {'p': 'Teleconferencing lets companies save on transportation costs and reduce lost '
          'productivity, and lets a manager interact with different branches simultaneously. '
          'Major drawbacks: set-up costs and increased risk of electronic eavesdropping. '
          '**Teleconferencing can be:** (a) audio only; (b) video only; (c) or both.'},
    {'h4': 'Audio conferencing'},
    {'p': 'A communication tool letting multiple participants connect and collaborate remotely '
          'using voice calls; widely used in business meetings, virtual events, educational '
          'sessions and personal discussions.'},
    {'p': '**Technology and tools:** phone-based conferencing (traditional conference calls); '
          '**VoIP** (Voice over Internet Protocol — Zoom, Microsoft Teams, Google Meet); '
          'dedicated conference call systems (hardware-based, for large-scale meetings).'},
    {'p': '**Benefits:** cost-effective (eliminates travel expenses, saves time); accessibility '
          '(global participation without geographical restrictions); efficiency (speeds up '
          'decision-making, improves team collaboration); recording options (for reference and '
          'documentation).'},
    {'p': '**Challenges:** audio quality issues (background noise, poor connection, microphone '
          'problems); lack of visual interaction (no non-verbal cues); participant engagement '
          '(harder to keep everyone involved without visual elements).'},
    {'p': '**Best practices:** use high-quality audio equipment; mute when not speaking; keep '
          'meetings structured and time-efficient; use call recording/transcription for '
          'documentation.'},
    {'p': '**Considerations for selecting audio-conferencing facilities:** (1) audio quality '
          '(HD audio, noise reduction, echo cancellation); (2) user capacity (maximum '
          'participants supported); (3) ease of use (an intuitive interface); (4) integration '
          'options (with Office, Slack, CRM, cloud storage); (5) security and encryption '
          '(end-to-end encryption, password-protected meetings, authentication); (6) recording '
          'and transcription; (7) mobile and desktop compatibility (Windows, macOS, Android, '
          'iOS); (8) customization and controls (mute options, speaker controls, breakout '
          'rooms, admin settings).'},
    {'h3': '5.9.10 Social media platforms'},
    {'p': 'Examples: **Facebook** (create profiles, upload photos/video, send messages, keep '
          'in touch with friends/family/colleagues); **X, formerly Twitter** (microblogging — '
          'broadcasting short posts called tweets, historically limited to 140 characters due '
          'to the SMS delivery system, for friends/family/coworkers to stay connected via '
          'quick, frequent messages); **WhatsApp Messenger** (cross-platform instant messaging '
          'for exchanging text, image, video and audio messages free of charge); **Snapchat, '
          'TikTok, Telegram**.'},
    {'p': '**Advantages of social media platforms:** increased exposure/brand awareness; '
          'learning about your audience/target consumer (understanding what customers are '
          'saying); customer service (interacting with customers, top-notch service); feedback '
          '(a fast medium for customer feedback); new opportunities (to acquire new '
          'customers); competitive analysis (understanding competitors\' edge by visiting '
          'their pages).'},
    {'p': '**Disadvantages:** if not properly monitored, employees may waste employers\' time '
          'chatting with friends during work hours; exposes organisations to the prying eyes '
          'of competitors; fraudsters can attack an organisation\'s network through its social '
          'media pages.'},
  ]},

  {'n': '5.10', 't': 'Electronic payment platform', 'b': [
    {'h3': '5.10.1 Optical cards'},
    {'def': {'t': 'Optical card', 'd': 'a plastic, laser-recordable, wallet-type card used '
                  'with an optical-card reader, with capacity for about 2,000 M pages of data. '
                  'May be used as a health card, holding a person\'s medical history and '
                  'health-insurance information, as well as digital images such as X-rays and '
                  'electrocardiograms.'}},
    {'note': 'The volume of detail on the card means adequate backups must be ensured, '
             'otherwise loss of the card causes incalculable loss of information.'},
  ]},

  {'n': '5.11', 't': 'Cloud computing', 'b': [
    {'def': {'t': 'Cloud computing', 'd': 'internet-based computing, whereby shared resources, '
                  'software and information are provided to computers and other devices '
                  'on-demand, like a public utility — allowing consumers and businesses to use '
                  'applications without installation, and access personal files on any '
                  'computer with internet access. Enables much more efficient computing '
                  'through centralised storage, memory, processing and bandwidth.'}},
    {'p': 'Cloud services are broadly divided into three categories: **Infrastructure-as-a-'
          'Service (IaaS)**, **Platform-as-a-Service (PaaS)** and **Software-as-a-Service '
          '(SaaS)**. Made available on demand, typically by the minute or hour; users take as '
          'much or as little of a service as they want at any given time, and the service is '
          'fully managed by the provider (consumers only need a computer and internet '
          'service).'},
    {'h3': '5.11.1 Cloud computing technologies'},
    {'ul': [
      '**Software-as-a-Service (SaaS)** — previously, the end-user bought a licence and '
      'installed/ran the software from on-premises servers; on-demand, the end-user instead '
      'pays a subscription fee, and the software is hosted on the provider\'s servers, '
      'accessed over the internet. Examples: Salesforce.com, Google, NetSuite, Info '
      'Technologies, Canada Software.net.',
      '**Platform-as-a-Service (PaaS)** — products used to deploy applications; platforms '
      'serve as interfaces for users to access applications provided by partners or, in some '
      'cases, customers. Examples: salesforce.com platform, NetSuite, Amazon, Google, Sun '
      'Oracle, Microsoft.',
      '**Infrastructure-as-a-Service (IaaS)** — the backbone of the entire cloud computing '
      'concept; vendors provide the physical storage space and processing capabilities '
      'underlying all the other services. Major infrastructure vendors: Google (managed '
      'hosting, development environment), IBM (managed hosting), Terremark (managed hosting), '
      'Amazon.com (cloud storage), Rackspace Hosting (managed hosting and cloud computing).',
    ]},
    {'p': 'Cloud can be **private** or **public**. A **public cloud** sells services to anyone '
          'on the internet (e.g. Amazon Web Services, the largest public cloud provider). A '
          '**private cloud** is a proprietary network or data centre supplying hosted services '
          'to a limited number of people. When a service provider uses public cloud resources '
          'to create its private cloud, the result is a **virtual private cloud**.'},
    {'p': 'Traditional business applications are too complicated and expensive, requiring a '
          'data centre with office space, power, cooling, bandwidth, networks, servers, '
          'storage and a team of experts. Multiplied across dozens or hundreds of '
          'applications, even the biggest companies struggle to get the applications they '
          'need. Cloud computing runs applications on a shared data centre — login, customize '
          'and start using it.'},
    {'p': '**Advantages of cloud computing:**'},
    {'ol': [
      'Costs less — no need to pay for all the people, products and facilities to run '
      'applications.',
      'Services are more scalable, more secured and more reliable than most application '
      'software.',
      'Simple, with a huge impact on any business.',
      'Easily upgraded, gaining security and performance enhancements with new features.',
      'Does not eat up valuable IT resources.',
      'Users can avoid capital expenditure on hardware, software and services, paying a '
      'provider only for what they use.',
      'Immediate access to a broad range of applications.',
      'Enables users to access systems using a web browser, regardless of location or device.',
      'Security is often better than traditional systems, as providers devote resources many '
      'individual users cannot afford.',
    ]},
    {'p': '**Disadvantages of cloud computing:**'},
    {'ol': [
      'Downtime is one of the worst lapses of cloud computing.',
      'No cloud provider, even the best, can claim immunity to service outages.',
      'Cloud computing systems are internet-based, so access is fully dependent on internet '
      'connection.',
    ]},
    {'h3': '5.11.2 Cloud computing clients'},
    {'def': {'t': 'Cloud client', 'd': 'computer hardware and/or software that relies on cloud '
                  'computing for application delivery (i.e. cloud services) — examples include '
                  'computers, phones and other devices, operating systems and browsers.'}},
  ]},

  {'n': '5.12', 't': 'Chapter summary', 'b': [
    {'p': 'This chapter dealt with computer networks, office automation and computer crime. It '
          'began with the concepts of computer networks, major network configurations, and the '
          'various protocols that accompany them. Office automation was discussed with '
          'reference to a few key applications. Computer crime — viruses and worms — was also '
          'discussed. The chapter ended with issues in the management of Information '
          'Technology, including certain health issues.'},
  ]},

  {'n': '5.13', 't': 'End-of-chapter questions (study text)', 'b': [
    {'h3': 'Multiple-choice questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–17 with answers', 'open': True, 'q': [
      {'ol': [
        'Which of the following is NOT true for an extranet? (A) Network links that use '
        'internet technology  (B) Can connect the intranet of a business with the intranet of '
        'customers, suppliers or business partners  (C) Makes use of a browser  (D) All '
        'internet users are allowed access  (E) Enables a company to offer new kinds of '
        'interactive web-enabled service to its business partners',
        'A type of network topology that is a combination of some other network types is '
        'called … (A) Hybrid  (B) Star  (C) Hierarchical  (D) Bus  (E) Ring',
        'Two or more people may engage in online interactive conversation over the internet '
        'through the use of: (A) Usernet  (B) Hypermedia language  (C) Chat room  '
        '(D) Newsgroup  (E) Contact streaming',
        'In connection with the Web, the meaning of the acronym HTML is (A) Hypertext Markup '
        'Language  (B) Hypertext Makeup Language  (C) Hypertest Markup Language  '
        '(D) Hypertest Makeup Language  (E) Hypertext Make Language',
        'Which of the following is NOT a network configuration? (A) Star Network  (B) Ring '
        'network  (C) Circuit network  (D) Bus network  (E) Tree Network',
        'The data transmission phenomenon where data is transferred regularly with a clock '
        'signal is called (A) Asynchronous data transfer  (B) Simplex data transfer  '
        '(C) Duplex data transfer  (D) Synchronous data transfer  (E) Regular data transfer',
        'A cheaper alternative to the modem, which makes it possible to use an ordinary '
        'telephone handset for binary data transfer, is known as: (A) Modulator  '
        '(B) Demodulator  (C) Concentrator  (D) Multiplexer  (E) Acoustic coupler',
        'The process of visiting different websites without looking for anything of '
        'particular importance is called (A) Web visiting  (B) Web surfing  (C) Web searching  '
        '(D) Web going  (E) Web journeying',
        'Which of the following is NOT an advantage of duplicating evidence in a computer '
        'forensic investigation? (A) An additional step is added into the forensic process  '
        '(B) Ensures the original document is not subjected to alteration  (C) Ensures the '
        'original document is in the best possible state  (D) Allows examiners to apply '
        'various techniques where the best approach is not clear  (E) Permits multiple '
        'forensic computer specialists to work on data at the same time',
        'The network protocol used to exchange and manipulate files over a computer network is '
        'known as (A) SOAP  (B) HTTP  (C) IMAP  (D) SMTP  (E) FTP',
        'The reduction in the strength of signals during data transmission is called '
        '(A) Salesforce.com service  (B) Desktop services  (C) Amazon service  '
        '(D) Attenuation  (E) Bureau service',
        'In cloud computing, the various computer servers and data storage systems that create '
        'the computing services are referred to as: (A) Backend  (B) Cloud system  '
        '(C) Frontend  (D) Users\' hardware  (E) User software',
        'Which of the following is NOT a factor to consider when selecting a data transmission '
        'system? (A) Speed of transmission required  (B) Length of the transmission system  '
        '(C) Accuracy and reliability required  (D) Cost of each type of data transmission  '
        '(E) System protocol that is available',
        'An internal organisation network that provides access to data across enterprises as '
        'well as to selected outsiders is known as: (A) Internet  (B) Intranet  (C) Extranet  '
        '(D) LAN  (E) WAN',
        '… is a device that provides a central connection point for cables from workstations, '
        'servers and peripherals in a network. (A) Bridge  (B) Gateway  (C) Switch  '
        '(D) Multiplexor  (E) Modem',
        'A network hardware device used for segmenting a large network into two or more '
        'efficient networks is called … (A) Gateway  (B) Bridge  (C) Switch  (D) Hub  '
        '(E) Multiplexor',
        'Which of the following is NOT a transmission medium? (A) Twisted pair cable  '
        '(B) Coaxial cable  (C) Radio wave  (D) Fiber optic  (E) Switch',
      ]}],
      'a': [
      {'p': '**1.** D  **2.** A  **3.** C  **4.** A  **5.** C  **6.** D  **7.** E  **8.** B  '
            '**9.** A  **10.** E  **11.** D  **12.** A  **13.** B  **14.** C  **15.** C  '
            '**16.** B  **17.** E'}]}},
    {'h3': 'Short-answer questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–14 with answers', 'open': True, 'q': [
      {'ol': [
        'An electronic device that allows a single communication channel to carry '
        'simultaneously data transmission from many terminals is called …',
        'A global network of multimedia internet sites for information, education, e-commerce, '
        'etc. is known as …',
        'A technology model in which any or all resources, such as application software, '
        'processing power, data storage, etc., are delivered as a set of services via the '
        'internet is called …',
        'The electronic device that can be used to capture digital video for uploading to the '
        'web is called …',
        'A network topology where each end-user is linked to a central computer on which all '
        'other devices depend is called …',
        'A protocol which enables Web servers to communicate with each other over a network is '
        'called …',
        'An internet-based application used to search for information from any website on the '
        'internet is known as …',
        'A small piece of text stored on a user\'s computer by a web browser, to capture user '
        'details, is known as …',
        'Business-to-Business buying and selling of goods and services on the internet is one '
        'of the forms of …',
        'A computing technology where one computer system renders services to other computer '
        'systems is called …',
        'The technology that facilitates the transfer of electronic data/information from one '
        'place/person to another place/person is known as …',
        'A communication system which provides connection for systems with compatible '
        'protocol is called …',
        'A network that uses radio waves to transmit data/information from one node to '
        'another is called …',
        'SaaS is an acronym for …',
      ]}],
      'a': [
      {'ol': [
        '**Multiplexor/Multiplexer.**',
        '**World Wide Web/WWW.**',
        '**Cloud Computing.**',
        '**Webcam/Digital Camera.**',
        '**Star (topology).**',
        '**Hyper Text Transfer Protocol/HTTP.**',
        '**Search Engine.**',
        '**Cookie** (also accept Spyware).',
        '**Electronic Commerce/E-Commerce.**',
        '**Client–server.**',
        '**Electronic mail/email.**',
        '**Router.**',
        '**Wireless Network.**',
        '**Software-as-a-Service.**'],
      }]}},
    {'h3': 'Self-assessment questions'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–11 with answers', 'open': True, 'q': [
      {'ol': [
        'What is a computer network?',
        'Distinguish between a computer network topology and a computer network protocol.',
        'Explain briefly the term "office automation".',
        'What is videoconferencing?',
        'Define the term "computer virus".',
        'Explain briefly the term "Internet protocol".',
        'What is an extranet?',
        'Define the term "telecommuting".',
        'Describe two uses of a smart card.',
        'What is an electronic mail (e-mail)?',
        'Differentiate between Client-to-Server and Peer-to-Peer LAN.',
      ]}],
      'a': [
      {'ol': [
        '**A computer network is an interconnection of a number of computers and other '
        'shared devices (printers, scanners, disk controllers) for information processing and '
        'dissemination. Depending on geographical dispersion: a WAN spreads devices over a '
        'wide area (a country/continent); a MAN spreads them over a smaller area (a city '
        'suburb); a LAN spreads them over a limited area (a building or small campus). A LAN '
        'is one type of local network.**',
        '**Topology (configuration) is determined by the manner in which the devices making '
        'up the network are physically connected — the physical connection matters because a '
        'visual picture of a topology can differ entirely from the actual one. A network '
        'protocol, by contrast, is the set of rules and guidelines governing the manner in '
        'which messages are passed around the network.**',
        '**Office automation is the use of computers, micro-electronics and '
        'telecommunications technology to manage information resources automatically in an '
        'office, aiming to integrate departmental functions. The terms "electronic office" or '
        '"paperless office" describe the modern office environment — more varied office '
        'equipment is used, leading to minimal use of paper; organisations now use e-mail for '
        'internal and external communication, and the computer handles almost all office '
        'routines.**',
        '**Videoconferencing uses television, video and sound technology together with '
        'computers, to let people in different geographical locations see, hear and talk with '
        'one another. Webcam technology has made videoconferencing via the Internet a cheaper '
        'option than special equipment, and has led to video mail (V-mail), where video '
        'messages are sent, stored and retrieved like e-mail.**',
        '**A computer virus is a type of infectious/malicious coding designed to damage or '
        'compromise computer systems. It is parasitic — once it finds a host (e.g. a PC), it '
        'is released and replicates itself very quickly, typically infecting memory and/or '
        'backing storage; some cause no visible harm, others cause extreme havoc immediately.**',
        '**"Internet protocol" is the standard language of the Internet, Transmission Control '
        'Protocol/Internet Protocol (TCP/IP), available since 1983 — the standardised set of '
        'guidelines that lets different computers on different networks communicate '
        'efficiently, however they gained access to the Net.**',
        '**An extranet is a type of intranet accessible to outsiders, but limited to those '
        'with valid user identification numbers; a prospective user must enter a valid ID '
        'number before access is granted.**',
        '**Telecommuting involves employees working from their homes or other locations '
        'outside their offices. Advantages include the opportunity to engage workers who '
        'cannot find full-time employment feasible, and spending less on office space, '
        'overheads and furniture.**',
        '**A smart card is a wallet-type card containing a microprocessor and memory chip, '
        'used to input data. Uses: (i) a telephone debit card, where call duration is '
        'calculated on the chip and cost deducted from the balance; (ii) a medical history '
        'card, carrying a patient\'s medical information.**',
        '**Electronic mail replaces the movement of paper messages with electronic '
        'transmission of coded, graphic or textual information, sent to or received by '
        'several people at different locations/time zones using computers or telephones. '
        'Information is "posted" to a central computer, which allocates disk storage as a '
        '"mailbox", later "collected" by the receiver using e-mail software; each person needs '
        'an e-mail address.**',
        '**(a) A Client-to-Server LAN has requesting computers (clients) and devices that '
        'provide a service (servers); clients connect to a powerful server that stores shared '
        'programs and data — e.g. a database server stores data for the LAN, and a print '
        'server controls one or more printers, storing print output and sending it to the '
        'printer(s) one document at a time. (b) A Peer-to-Peer LAN has all computers '
        'communicating directly with each other, with no server — less expensive, effective '
        'for up to about 25 computers; each peer administers its own devices/resources, '
        'functions as both client and server, and there is no dedicated administrator — '
        'security is managed by each user.**'],
      }]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'Keep the five LAN topologies (star, ring, bus, tree, mesh) straight by their single '
   'points of failure: star fails at the server, ring/bus fail at any broken link, tree fails '
   'at the root node, mesh has no single point of failure at all. Know the transmission-'
   'equipment vocabulary cold — modem vs multiplexer vs FEP vs NIC vs hub/switch vs bridge vs '
   'router vs gateway vs repeater — the exam tests them as one-line "which device does X" '
   'questions. Also fix the five transmission modes (simplex, half-duplex, duplex, '
   'synchronous, asynchronous) and the three cloud service layers (IaaS/PaaS/SaaS) as ordered '
   'lists you can recite.',
 'errors': [
   'Confusing a bridge (connects similar networks) with a gateway (connects dissimilar '
   'networks, performing protocol conversion).',
   'Saying half-duplex allows simultaneous two-way transmission — it allows two-way '
   'transmission but only one direction at a time; that is full duplex.',
   'Treating "Internet" and "Web" as synonyms — the Internet is the underlying network of '
   'networks; the Web is the hypertext-linked collection of sites/pages that runs on top of '
   'it via HTTP/HTML.',
   'Mixing up an intranet (internal-only) with an extranet (an intranet opened to authorised '
   'outsiders via valid ID) — both differ from the fully public Internet.',
   'Assuming a switch and a hub do the same job equally well — a switch directs traffic '
   'intelligently to the intended device; a hub broadcasts to all connected devices, which is '
   'why switches have largely replaced hubs.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A network topology in which all devices connect to a central server, so that a '
         'broken link to one device does not disable the rest of the network, is a',
    'o': ['Ring network', 'Bus network', 'Star network', 'Mesh network', 'Tree network'],
    'a': 2,
    'w': 'In a star network, if a connection between one device and the server breaks, the '
         'rest of the network keeps functioning; but if the server itself fails, the whole '
         'network goes down.',
    'src': 'Chapter 5.2.2(a)', 'sec': '5.2'},
   {'q': 'The device that provides a central connection point for cables from workstations, '
         'servers and peripherals, and has largely replaced the hub because of better '
         'performance, is the',
    'o': ['Router', 'Gateway', 'Switch', 'Repeater', 'Bridge'],
    'a': 2,
    'w': 'A switch (concentrator) is the central connection point in, e.g., a star topology; '
         'switches are now preferred over hubs because they are cheaper and give faster data '
         'transmission.',
    'src': 'Chapter 5.8.5', 'sec': '5.8'},
   {'q': 'Which mode of transmission allows signals to travel in both directions but only one '
         'direction at a time, as in a walkie-talkie?',
    'o': ['Simplex', 'Half-duplex', 'Duplex', 'Synchronous', 'Asynchronous'],
    'a': 1,
    'w': 'Half-duplex is two-way but not simultaneous. Simplex is strictly one-way; duplex '
         '(full-duplex) is two-way and simultaneous.',
    'src': 'Chapter 5.7', 'sec': '5.7'},
   {'q': 'The cloud computing service layer that provides the physical storage space and '
         'processing capabilities underlying all other cloud services is',
    'o': ['Software-as-a-Service (SaaS)', 'Platform-as-a-Service (PaaS)',
          'Infrastructure-as-a-Service (IaaS)', 'Data-as-a-Service (DaaS)',
          'Network-as-a-Service (NaaS)'],
    'a': 2,
    'w': 'IaaS is described as "the backbone of the entire concept of cloud computing" — '
         'vendors supply the physical storage and processing capability that PaaS and SaaS '
         'are built on top of.',
    'src': 'Chapter 5.11.1', 'sec': '5.11'},
   {'q': 'A type of intranet that is accessible to outsiders, but limited to those with a '
         'valid user identification number, is called a(n)',
    'o': ['Internet', 'Extranet', 'WAN', 'Firewall', 'Virtual private cloud'],
    'a': 1,
    'w': 'An extranet opens part of a corporate intranet to authorised outsiders (e.g. '
         'suppliers or customers) who must supply valid identification, unlike the fully '
         'internal intranet or the fully public internet.',
    'src': 'Chapter 5.5.2', 'sec': '5.5'},
   {'q': 'A device used to regenerate (amplify and restore) a signal that has lost strength '
         '(attenuated) as it passes along a cable is a',
    'o': ['Multiplexer', 'Repeater', 'Bridge', 'Gateway', 'Front-End Processor'],
    'a': 1,
    'w': 'A repeater electrically amplifies a received signal and rebroadcasts it, overcoming '
         'attenuation. A multiplexer combines several input streams into one; a bridge '
         'connects similar networks; a gateway connects dissimilar ones.',
    'src': 'Chapter 5.8.9', 'sec': '5.8'},
  ],
  'theory': [
   {'q': 'Distinguish between a WAN, a MAN and a LAN, giving one distinguishing feature of '
         'each.',
    'marks': 6,
    'a': [
      {'ul': [
        '**WAN** — a communications network covering a wide geographical area, such as a '
        'region of a country or an entire country; e.g. the Internet links several WANs.',
        '**MAN** — covers a geographical area the size of a town, city suburb, or an entire '
        'city, up to about 50 km in diameter.',
        '**LAN** — a privately owned network confined to a small area, usually within a '
        'kilometre — a building, adjacent buildings, or a campus.']}],
    'src': 'Chapter 5.1.2', 'sec': '5.1'},
   {'q': 'Describe the star, ring and bus LAN topologies, stating one advantage and one '
         'disadvantage of each.',
    'marks': 9,
    'a': [
      {'ul': [
        '**Star** — all devices connect to a central server. Advantage: if a device\'s '
        'connection breaks, the rest of the network keeps working. Disadvantage: if the '
        'server fails, the whole network is inoperative.',
        '**Ring** — devices connected in a continuous loop, a peer-to-peer LAN with no '
        'server; a "bit token" grants permission to send. Advantage: messages flow one way, '
        'so there is no danger of collision. Disadvantage: a single broken connection can stop '
        'the entire network.',
        '**Bus** — all devices connect to a common channel, with collisions managed by '
        'CSMA/CD. Advantage: can be organised as client/server or peer-to-peer. Disadvantage: '
        'a broken connection can stop the network.']}],
    'src': 'Chapter 5.2.2', 'sec': '5.2'},
   {'q': '(a) What is a firewall, and why is it needed on an intranet? (b) Distinguish '
         'encryption from decryption.',
    'marks': 8,
    'a': [
      {'p': '(a) A **firewall** is a security program that connects the intranet to external '
            'networks such as the Internet and blocks unauthorised traffic (including '
            'unauthorised employees) from entering the intranet. It is needed because an '
            'intranet\'s connection to external networks means outsiders without access '
            'rights could otherwise reach the corporate network.'},
      {'p': '(b) **Encryption** is the transformation of usable information into a form '
            'unusable by anyone but the authorised user; **decryption** is transforming the '
            'encrypted information back into its original usable form, which only an '
            'authorised user possessing the cryptographic key can do.'}],
    'src': 'Chapter 5.5.1, 5.2.4', 'sec': '5.5'},
   {'q': 'List and briefly explain the five layers of the OSI model concerned with (i) the '
         'physical transmission of bits and (ii) the addressing and reliable transfer of data '
         '(i.e. layers 1–4), then name the remaining three layers.',
    'marks': 10,
    'a': [
      {'ol': [
        '**Physical (Layer 1)** — conveys the bit stream at the electrical/mechanical level.',
        '**Data Link (Layer 2)** — encodes/decodes packets into bits, manages transmission '
        'protocol, error handling, flow control and frame synchronization.',
        '**Network (Layer 3)** — provides addressing services and error handling.',
        '**Transport (Layer 4)** — provides transparent, complete transfer of data between '
        'end systems.']},
      {'p': 'The remaining three layers are **Session (5)**, **Presentation (6)** and '
            '**Application (7)**.'}],
    'src': 'Chapter 5.3.1', 'sec': '5.3'},
   {'q': 'Distinguish between telecommuting and the virtual office, and state any THREE '
         'advantages of telecommuting to the employer.',
    'marks': 9,
    'a': [
      {'p': '**Telecommuting** is employees working from home or another location outside '
            'the office, usually on a fixed remote arrangement. The **virtual office** is a '
            'non-permanent, mobile office run on computer and communications technology '
            '(pagers, portable computers, fax, phone/network services), letting employees '
            'work from homes, cars and other locations rather than a central office — a '
            'broader, more mobile concept than a single home-based telecommuting arrangement.'},
      {'h4': 'Advantages of telecommuting to the employer (any three)'},
      {'ol': [
        'Less expense on office space and furniture.',
        'Less office utility bills.',
        'Engagement of scarce human resources not willing to take full-time appointments.',
        'Companies can engage personnel outside their localities, even in other countries.']}],
    'src': 'Chapter 5.9.7, 5.9.8', 'sec': '5.9'},
  ]},
}
