CH = {
 'n': 17,
 't': 'Network Analysis',
 'brief': 'Drawing an Arrow-on-Node network from a table of activities, the forward and '
          'backward passes, the critical path, and the three types of float.',
 'outcomes': [
   'Explain the concept of Network Analysis',
   'Define Activity, Event and Dummy Activity',
   'Draw a network diagram',
   'Identify the paths in a network diagram and calculate their durations',
   'Identify the critical path and the critical activities',
   'Calculate the shortest time for the completion of a project',
   'Calculate the Earliest Start Time (EST), Latest Start Time (LST), Earliest Finish Time '
   '(EFT) and Latest Finish Time (LFT) for an activity',
   'Calculate floats and interpret their values',
 ],
 'secs': [
  {'n': '17.1', 't': 'Introduction and terms', 'b': [
    {'p': 'Network analysis is an Operations Research method for managing large projects '
          'optimally — a technique for planning, scheduling and controlling projects such as '
          'setting up a new business, construction projects, maintenance of buildings and '
          'machines, or personnel training. Its primary objective is to complete the project '
          'within the minimum time. The project manager decides on the project\'s "flow '
          'diagram" by identifying: the tasks that must be done first before others can start '
          '(preceding tasks); the tasks that can be done simultaneously; and the tasks that are '
          '"crucial" to the project.'},
    {'def': {'t': 'Activity', 'd': 'a task, represented by an arrowed line running left to '
                  'right (not drawn to scale) between two events. It consumes time and '
                  'resources — e.g. "prepare a set of accounts".'}},
    {'def': {'t': 'Event', 'd': 'the start and/or completion of an activity, represented by a '
                  'circle called a **node**, usually numbered.'}},
    {'def': {'t': 'Dummy activity', 'd': 'an activity of "circumstance", represented by a '
                  'dotted line. It consumes **neither time nor resources**, and exists only to '
                  'ensure the rules for drawing a network diagram are not violated — in '
                  'particular, so that two different activities never share the same starting '
                  'and finishing nodes.'}},
    {'def': {'t': 'Path', 'd': 'a sequence of activities that takes one from the start to the '
                  'end of the network.'}},
  ]},

  {'n': '17.2', 't': 'Critical Path Analysis (CPA) and drawing the network', 'b': [
    {'def': {'t': 'Critical path', 'd': 'the path of a network with the **longest** duration — '
                  'this gives the shortest time within which the whole project can be '
                  'completed. There can be more than one critical path in a network.'}},
    {'def': {'t': 'Critical activities', 'd': 'the activities on the critical path. There must '
                  'be no delay in starting or finishing them, or the whole project\'s duration '
                  'is extended.'}},
    {'h4': 'Rules for drawing an Arrow-on-Node (A-O-N) network diagram'},
    {'ul': [
      'All activities, with their durations, must be known or estimated.',
      'The logical sequence of activities must be established — which must be done one after '
      'the other (preceding activities), and which can be done simultaneously.',
      'Every activity must contribute to the progression of the project, or be discarded.',
      'A network diagram must have **one** starting event and **one** finishing event.',
      'A-O-N is the only type of network diagram this study text uses.',
    ]},
    {'note': 'When drawing a network, work one step at a time rather than looking at the whole '
             'network at once; use a pencil so mistakes are easily erased. Start with the '
             'activity (or activities) that has no preceding activity, then follow through the '
             'given information.'},
    {'eg': {'tag': 'Study text', 't': 'Example 17.1 — a first network diagram', 'open': True,
      'q': [
      {'p': 'The activities of a project are:'},
      {'table': {'align': 'll', 'head': ['Activity', 'Preceding activity'], 'rows': [
        ['A', '—'], ['B', '—'], ['C', 'B'], ['D', 'C'], ['E', 'A'], ['F', 'E'],
      ]}},
      {'p': 'Draw the A-O-N network diagram for the project.'}],
      'a': [
      {'p': 'A and B have no preceding activity, so both start at the initial node. A is '
            'followed by E then F; B is followed by C then D.'},
      {'p': 'The paths of the network are: **B, C, D** and **A, E, F**.'},
      {'note': 'The arrows on every activity must be directed (pointing from tail to head), or '
               'the diagram is meaningless.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 17.2 — when a dummy activity is needed',
      'open': True, 'q': [
      {'p': 'In Example 17.1, if C is preceded by **both A and B**, and F is preceded by '
            '**both C and E**, draw the corresponding network diagram.'}],
      'a': [
      {'p': 'A dummy activity is now necessary, linking A into C\'s starting node, so that A '
            'and B do not share the same head node for their different activities.'},
      {'p': 'The paths of the network are now: **A, E, F**; **A, Dummy, C, D**; **B, C, D**; '
            'and **B, C, Dummy, F**.'}]}},
  ]},

  {'n': '17.3', 't': 'The critical path and its associated duration', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Example 17.3 — finding the critical path', 'open': True,
      'q': [
      {'p': 'The following activities, with their durations, are needed to complete a '
            'project.'},
      {'table': {'align': 'llr', 'head': ['Activity', 'Preceding activity', 'Duration (weeks)'],
        'rows': [
        ['A', '—', '4'], ['B', 'A', '6'], ['C', 'A', '3'], ['D', 'B, C', '5'],
        ['E', 'A', '7'], ['F', 'D', '1'], ['G', 'D', '4'], ['H', 'E, F', '6'],
      ]}},
      {'ol': [
        'Draw the A-O-N network diagram for the project.',
        'Identify all the paths and calculate the duration of each.',
        'Identify the critical activities, the critical path, and its duration.',
      ]}],
      'a': [
      {'p': '**(b) Every path and its duration:**'},
      {'table': {'align': 'lr', 'head': ['Path', 'Duration'], 'rows': [
        ['A, B, E, H', '4+6+7+6 = 23 weeks'],
        ['A, C, D, G', '4+3+5+4 = 16 weeks'],
        ['A, C, D, F, H', '4+3+5+1+6 = 19 weeks'],
        ['A, B, Dummy, D, G', '4+6+0+5+4 = 19 weeks'],
        ['A, B, Dummy, D, F, H', '4+6+0+5+1+6 = 22 weeks'],
      ]}},
      {'p': '**(c)** The **critical path is A, B, E, H**, with a duration of **23 weeks** — the '
            'longest of all the paths, and so the project\'s duration.'}]}},
  ]},

  {'n': '17.4', 't': 'The three types of float', 'b': [
    {'def': {'t': 'Float', 'd': 'the amount of spare time associated with an activity. Only '
                  '**non-critical** activities have floats — such activities can start late '
                  'and/or take longer than specified without affecting the project\'s '
                  'duration.'}},
    {'ul': [
      '**Total float** — the amount of time an activity\'s duration could be extended by, '
      'without affecting the **project** duration.',
      '**Free float** — the amount of time an activity\'s duration can be extended by, without '
      'affecting the **commencement of subsequent activities**.',
      '**Independent float** — the amount of time an activity\'s duration can be extended by, '
      'without affecting the time available for **either** succeeding **or** preceding '
      'activities.',
    ]},
    {'h4': 'Earliest Start Time (EST) and Latest Start Time (LST)'},
    {'p': 'The **EST** is the earliest possible time a succeeding activity can start; the '
          '**LST** is the latest possible time a preceding activity must be completed by, so as '
          'not to increase the project duration.'},
    {'steps': [
      '**Forward pass (ESTs).** Start at the zero event and work forward. The EST of a head '
      'event is the sum of the EST of the tail event and the linking activity\'s duration. '
      'Where two or more activities share a head event, take the **largest** time. The EST at '
      'the finish event gives the project duration.',
      '**Backward pass (LSTs).** Start at the finish event, using its EST as its LST, and work '
      'backwards. Deduct each activity\'s duration from the previous LST. Where two or more '
      'LSTs are possible for an event, take the **smallest** time.',
    ]},
    {'key': 'Along the critical path, the EST and LST of every event are **equal** — this is '
            'itself a second way of identifying the critical path.'},
    {'p': 'The **Earliest Finish Time (EFT)** and **Latest Finish Time (LFT)** of an activity '
          'are read directly from its head node: EFT is the smaller of the two figures at that '
          'node, LFT the larger. Consequently, the EST of an activity is the EFT of its '
          'preceding activity, and the LST of an activity is the LFT of its preceding '
          'activity.'},
    {'fbox': {'h': 'The three floats', 'rows': [
      {'lb': 'Total float', 'tex': 'TF = LFT - EST - D'},
      {'lb': 'Free float', 'tex': 'FF = EFT - EST - D'},
      {'lb': 'Independent float', 'tex': 'IF = EFT - LST - D'},
    ]}},
    {'note': 'All floats of the critical activities are zero — confirming that only '
             'non-critical activities have floats.'},
    {'eg': {'tag': 'Study text', 't': 'Example 17.4 — ESTs, LSTs and all three floats',
      'open': True, 'q': [
      {'p': 'Using the network of Example 17.3, calculate the ESTs, LSTs, and all three floats '
            'for every activity.'}],
      'a': [
      {'h4': 'Forward pass (ESTs, by event)'},
      {'table': {'align': 'lp{34ch}r', 'head': ['Event', 'Working', 'EST'], 'rows': [
        ['1', '0 + 4', '4'],
        ['2', '4 + 6', '10'],
        ['3', 'larger of $4+3=7$ and $10+0$ (dummy)', '10'],
        ['4', '10 + 5', '15'],
        ['5', 'larger of $10+7=17$ and $15+1=16$', '17'],
        ['6', 'larger of $15+4=19$ and $17+6=23$', '23'],
      ]}},
      {'h4': 'Backward pass (LSTs, by event)'},
      {'table': {'align': 'lp{34ch}r', 'head': ['Event', 'Working', 'LST'], 'rows': [
        ['6', 'equals its EST', '23'],
        ['5', '23 − 6', '17'],
        ['4', 'smaller of $23-4=19$ and $17-1=16$', '16'],
        ['3', 'smaller of $16-5=11$ and $10-0=10$', '10'],
        ['2', '10 − 6', '4'],
        ['1', '10 − 6', '4'],
        ['0', '4 − 4', '0'],
      ]}},
      {'p': 'Events 0, 1, 2, 5 and 6 have equal EST and LST, confirming they lie on the '
            'critical path.'},
      {'h4': 'EFT, LFT and the three floats, by activity'},
      {'table': {'align': 'lrrrrrrrr',
        'head': ['Activity', 'EST', 'LST', 'EFT', 'LFT', 'D', 'TF', 'FF', 'IF'], 'rows': [
        ['A', '0', '0', '4', '4', '4', '0', '0', '0'],
        ['B', '4', '4', '10', '10', '6', '0', '0', '0'],
        ['C', '4', '4', '10', '10', '3', '3', '3', '3'],
        ['D', '10', '10', '15', '16', '5', '1', '0', '0'],
        ['E', '10', '10', '17', '17', '7', '0', '0', '0'],
        ['F', '15', '16', '17', '17', '1', '1', '1', '0'],
        ['G', '15', '16', '23', '23', '4', '4', '4', '3'],
        ['H', '17', '17', '23', '23', '6', '0', '0', '0'],
      ]}},
      {'note': 'Every critical activity (A, B, E, H) has zero of all three floats. C has the '
               'same total, free **and** independent float (3 weeks) since it sits alone '
               'between two events whose own EST/LST already match; D and F each have total '
               'float but zero free/independent float, since their slack is "borrowed" by the '
               'rest of their non-critical chain; G, uniquely, has independent float **less '
               'than** its total/free float.'}]}},
  ]},

  {'n': '17.5', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§17.1 Terms** — activity (arrow, consumes time/resources); event/node (circle, no '
      'duration); dummy activity (dotted arrow, consumes neither time nor resources, used only '
      'to avoid two activities sharing both a start and end node); path (a start-to-end '
      'sequence of activities).',
      '**§17.2 CPA and drawing the network** — critical path = the **longest** path (there can '
      'be more than one); critical activities = those on it, with zero tolerance for delay. '
      'A-O-N rules: known/estimated durations; correct logical sequence; every activity '
      'contributes; one start event and one finish event.',
      '**§17.3 The critical path\'s duration** — list every path, sum each one\'s activity '
      'durations, and take the longest as the critical path and the project duration.',
      '**§17.4 The three floats** — total float (delay tolerance for the project duration), '
      'free float (delay tolerance before it affects the next activity\'s start), independent '
      'float (delay tolerance affecting neither the preceding nor a succeeding activity). '
      'Forward pass takes the **largest** EST where paths converge; backward pass takes the '
      '**smallest** LST where paths diverge. $TF=LFT-EST-D$; $FF=EFT-EST-D$; $IF=EFT-LST-D$. '
      'On the critical path, every float is zero.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Network analysis** — an OR technique for planning, scheduling and controlling '
      'projects.',
      '**Activity** — a task consuming time and resources; an arrow.',
      '**Event (node)** — the start/finish of one or more activities; a circle; no duration.',
      '**Dummy activity** — a zero-time, zero-resource logical link; a dotted arrow.',
      '**Path** — a start-to-end sequence of activities.',
      '**Critical path** — the longest path; fixes the project duration.',
      '**Critical activities** — activities on the critical path; zero float.',
      '**EST / LST** — earliest / latest start time of an activity.',
      '**EFT / LFT** — earliest / latest finish time of an activity, read from its head node.',
      '**Total, free and independent float** — the three measures of an activity\'s spare '
      'time, as defined in §17.4.',
    ]},
    {'h3': 'A. Forward and backward pass'},
    {'fbox': {'h': 'Event times', 'rows': [
      {'lb': 'Forward pass (EST of a head event)',
       'tex': 'EST_{\\text{head}} = \\max\\big(EST_{\\text{tail}} + D\\big)'},
      {'lb': 'Backward pass (LST of a tail event)',
       'tex': 'LST_{\\text{tail}} = \\min\\big(LST_{\\text{head}} - D\\big)'},
    ]}},
    {'h3': 'B. The three floats'},
    {'fbox': {'h': 'Float (activity EST/LST from the tail node, EFT/LFT from the head node)',
      'rows': [
      {'lb': 'Total float', 'tex': 'TF = LFT - EST - D'},
      {'lb': 'Free float', 'tex': 'FF = EFT - EST - D'},
      {'lb': 'Independent float', 'tex': 'IF = EFT - LST - D'},
    ]}},
  ]},

  {'n': '17.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'In a network diagram, two different activities must not have (A) the same duration  '
        '(B) the same starting nodes  (C) the same finishing nodes  (D) the same starting and '
        'finishing nodes  (E) the same preceding activity',
      ]},
      {'p': 'A project has activities A (5 weeks, no predecessor), B (4 weeks, no predecessor), '
            'C (3 weeks, after a dummy activity of A), D (4 weeks, after A), E (2 weeks, after '
            'the dummy and B), G (3 weeks, after D and E). Use this to answer questions 2 and '
            '3.'},
      {'ol': [
        'The shortest time within which the project can be completed is (A) 12 weeks  '
        '(B) 14 weeks  (C) 10 weeks  (D) 11 weeks  (E) 15 weeks',
        'The number of paths of the network is (A) 2  (B) 4  (C) 3  (D) 5  (E) 6',
        'In a network diagram, the critical activities have (A) free float only  '
        '(B) independent float and free float  (C) independent float only  (D) total float  '
        '(E) no float',
        'The primary objective of a Network Analysis is to ……… a project within the ……… time.',
        'A dummy activity neither consumes ……… nor ……… .',
        'The critical path of a network is the path with the ……… duration.',
        'A Network diagram can be drawn using events on the ……… and events on the ……… .',
        'The calculation of the latest start time (LST) is also referred to as the ……… pass.',
        'The float of an activity is the amount of ……… time associated with the activity.',
      ]}],
      'a': [
      {'ol': [
        '**D** — two different activities must not share the same starting **and** finishing '
        'nodes (a dummy activity is used to prevent this).',
        '**E — 15 weeks.** The four paths are A-D-G (12 weeks), A-Dummy-C-F (12 weeks), '
        'A-D-E-F (15 weeks) and B-C-F (14 weeks); the longest is 15 weeks.',
        '**B — 4 paths** (see the workings for Q2).',
        '**E — no float.** Critical activities have zero of every type of float.',
        '**Complete, minimum** (in that order).',
        '**Time, resources** (or vice versa).',
        '**Longest.**',
        '**Arrow …, node** (i.e. events on the arrow-on-node convention).',
        '**Backward** pass.',
        '**Spare** time.',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Forward pass — earliest start of a head event',
   'tex': 'EST_{\\text{head}} = \\max\\big(EST_{\\text{tail}} + D\\big)'},
  {'lb': 'Backward pass — latest start of a tail event',
   'tex': 'LST_{\\text{tail}} = \\min\\big(LST_{\\text{head}} - D\\big)'},
  {'lb': 'Total float', 'tex': 'TF = LFT - EST - D'},
  {'lb': 'Free float', 'tex': 'FF = EFT - EST - D'},
  {'lb': 'Independent float', 'tex': 'IF = EFT - LST - D'},
 ],
 'focus':
   'A regular Section B question, and one of the most reliably scored. The table of activities '
   'is given, and the marks follow the method: network diagram, forward pass, backward pass, '
   'the three floats, critical path, duration. Present the passes in a table even if you also '
   'draw the network — the examiner can then follow the arithmetic. Remember EST/LST of an '
   'activity come from its **tail** node, EFT/LFT from its **head** node.',
 'errors': [
   'Taking the minimum on the forward pass or the maximum on the backward pass — it is the '
   'reverse.',
   'Identifying the shortest path as critical instead of the longest.',
   'Confusing total, free and independent float — they use different combinations of EST, '
   'LST, EFT and LFT.',
   'Giving a dummy activity a duration, or omitting one where two activities would otherwise '
   'share both start and end events.',
   'Reading EST/LST from the wrong end of an activity\'s arrow (they belong to the tail node, '
   'not the head node).',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The critical path in a network is',
    'o': ['the shortest path through the network', 'the longest path through the network',
          'the path with the most activities', 'the path with the greatest total float',
          'the path with the fewest dummy activities'],
    'a': 1,
    'w': 'The longest path determines the project duration and has zero float throughout.',
    'src': 'Chapter 17.2', 'sec': '17.2'},
   {'q': 'An activity has EST = 8, EFT = 13, LST = 11 and LFT = 16, with a duration of 5. Its '
         'total float is',
    'o': ['2 weeks', '3 weeks', '5 weeks', '8 weeks', 'nil'],
    'a': 1,
    'w': 'Total float is $LFT-EST-D$.',
    'calc': 'TF = 16 - 8 - 5 = 3',
    'src': 'Chapter 17.4', 'sec': '17.4'},
   {'q': 'A dummy activity in a network',
    'o': ['consumes resources but no time', 'consumes neither time nor resources',
          'consumes time but no resources', 'is always on the critical path',
          'has the longest duration'],
    'a': 1,
    'w': 'A dummy exists only to preserve the rule that no two activities share both a start '
         'and end node. Its duration is zero.',
    'src': 'Chapter 17.1', 'sec': '17.1'},
   {'q': 'On the forward pass, where several activities converge on an event, the earliest '
         'event time is',
    'o': ['the smallest of the earliest finishes', 'the largest of the earliest finishes',
          'the average of the earliest finishes', 'the sum of the earliest finishes',
          'always zero'],
    'a': 1,
    'w': 'Every converging activity must be complete before the event is reached, so the '
         'latest arrival governs.',
    'src': 'Chapter 17.4', 'sec': '17.4'},
   {'q': 'Only activities with zero float are',
    'o': ['dummy activities', 'critical activities', 'the first activities in a network',
          'the last activities in a network', 'activities with the shortest duration'],
    'a': 1,
    'w': 'By definition, critical activities cannot be delayed at all without delaying the '
         'whole project, so all three of their floats are zero.',
    'src': 'Chapter 17.4', 'sec': '17.4'},
  ],
  'theory': [
   {'q': 'The following activities make up a project: A (no predecessor, 4 weeks); B (no '
         'predecessor, 7 weeks); C (after A, 6 weeks); D (after A, 3 weeks); E (after B and C, '
         '5 weeks); F (after D, 4 weeks); G (after E and F, 2 weeks). (a) Calculate the EST and '
         'LST of every event. (b) State the project duration and the critical path. (c) '
         'Calculate the total float of each activity.',
    'marks': 15,
    'a': [
      {'h4': '(a) Forward and backward pass, by event'},
      {'p': 'Number the events 0 (start), 1 (after A), 2 (after B), 3 (after C, joining with '
            'B\'s path), 4 (after D), 5 (after E and F), 6 (finish, after G).'},
      {'table': {'align': 'lrr', 'head': ['Event', 'EST', 'LST'], 'rows': [
        ['0', '0', '0'],
        ['1 (after A)', '4', '4'],
        ['2 (after B)', '7', '10'],
        ['3 (after C)', '10', '10'],
        ['4 (after D)', '7', '11'],
        ['5 (after E, F)', '15', '15'],
        ['6 (after G)', '17', '17'],
      ]}},
      {'h4': '(b) Duration and critical path'},
      {'p': 'The project duration is **17 weeks**. Events 0, 1, 3, 5 and 6 have equal EST and '
            'LST, giving the critical path **A → C → E → G** '
            '$= 4+6+5+2 = 17$ weeks.'},
      {'h4': '(c) Total float'},
      {'table': {'align': 'lrrrrr',
        'head': ['Activity', 'EST', 'LST', 'EFT', 'LFT', 'TF'], 'rows': [
        ['A', '0', '0', '4', '4', '0'],
        ['B', '0', '3', '7', '10', '3'],
        ['C', '4', '4', '10', '10', '0'],
        ['D', '4', '8', '7', '11', '4'],
        ['E', '10', '10', '15', '15', '0'],
        ['F', '7', '11', '15', '15', '4'],
        ['G', '15', '15', '17', '17', '0'],
      ]}},
      {'p': 'B has 3 weeks of float; D and F each have 4 weeks (shared along the non-critical '
            'chain A–D–F); the four critical activities (A, C, E, G) have none.'}],
    'src': 'Chapter 17.4', 'sec': '17.4'},
  ]},
}
