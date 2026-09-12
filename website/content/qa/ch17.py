CH = {
 'n': 17,
 't': 'Network Analysis',
 'brief': 'Drawing an activity network, the forward and backward passes, the critical path, '
          'total and free float, and PERT with three time estimates.',
 'outcomes': [
   'Draw a network from a table of activities and their predecessors',
   'Use dummy activities correctly',
   'Carry out the forward pass to find earliest event times and the project duration',
   'Carry out the backward pass to find latest event times',
   'Identify the critical path and compute total and free float',
   'Apply PERT to estimate expected duration and the probability of meeting a deadline',
 ],
 'secs': [
  {'n': '17.1', 't': 'Terms and conventions', 'b': [
    {'ul': [
      '**Activity** — a task consuming time and resources; drawn as an arrow.',
      '**Event (node)** — a point in time marking the start or finish of activities; drawn as '
      'a circle. Events have no duration.',
      '**Dummy activity** — a broken arrow of zero duration, used to show a dependency without '
      'consuming time, or to give two parallel activities distinct end events.',
      '**Network** — the diagram as a whole, showing every activity and its dependencies. It '
      'has one start event and one end event, and contains no loops.',
      '**Critical path** — the longest path through the network. It determines the project '
      'duration, and every activity on it has zero float.',
      '**Float (slack)** — the amount by which a non-critical activity may be delayed without '
      'delaying something else.',
    ]},
    {'key': 'The **longest** path is the critical one, not the shortest. It is the path that '
            'cannot absorb any delay: every day lost on it is a day lost to the project.'},
  ]},

  {'n': '17.2', 't': 'The forward and backward passes', 'b': [
    {'fbox': {'h': 'Passes and float', 'rows': [
      {'lb': 'Forward pass — earliest start',
       'tex': 'ES_j = \\max\\big(ES_i + d_{ij}\\big)'},
      {'lb': 'Earliest finish', 'tex': 'EF = ES + d'},
      {'lb': 'Backward pass — latest finish',
       'tex': 'LF_i = \\min\\big(LF_j - d_{ij}\\big)'},
      {'lb': 'Latest start', 'tex': 'LS = LF - d'},
      {'lb': 'Total float',
       'tex': 'TF = LF - EF = LS - ES'},
      {'lb': 'Free float',
       'tex': 'FF = ES_{\\text{(next)}} - EF'},
      {'lb': 'Independent float',
       'tex': 'IF = ES_{\\text{(next)}} - LF_{\\text{(previous)}} - d'},
    ]}},
    {'steps': [
      '**Forward pass.** Start at time 0 and work left to right. Where several activities '
      'converge on an event, take the **largest** earliest finish — all predecessors must be '
      'complete.',
      'The earliest time at the final event is the **project duration**.',
      '**Backward pass.** Set the latest time at the final event equal to the project duration '
      'and work right to left. Where several activities leave an event, take the **smallest** '
      'latest start.',
      'Compute total float for each activity as $LS - ES$. Activities with zero float form the '
      'critical path.',
    ]},
    {'warn': 'Forward pass takes the **maximum**, backward pass the **minimum**. Reversing them '
             'is the most frequent error in this chapter and destroys the whole answer, because '
             'every subsequent float depends on it.'},

    {'eg': {'t': 'A complete network analysis', 'q': [
      {'p': 'A project consists of the following activities:'},
      {'table': {'align': 'lll', 'head': ['Activity', 'Preceded by', 'Duration (weeks)'],
        'rows': [
        ['A', '—', '5'],
        ['B', '—', '3'],
        ['C', 'A', '4'],
        ['D', 'B', '6'],
        ['E', 'A', '2'],
        ['F', 'C, D', '5'],
        ['G', 'E', '3'],
      ]}},
      {'p': 'Determine the project duration, the critical path, and the total and free float '
            'of each activity.'}],
      'a': [
      {'h4': 'Forward pass'},
      {'p': 'A and B both start at time 0. C and E follow A ($ES = 5$); D follows B '
            '($ES = 3$). F needs both C ($EF = 9$) and D ($EF = 9$), so $ES_F = \\max(9, 9) '
            '= 9$.'},
      {'table': {'align': 'lrrr', 'head': ['Activity', 'Duration', 'ES', 'EF'], 'rows': [
        ['A', '5', '0', '5'],
        ['B', '3', '0', '3'],
        ['C', '4', '5', '9'],
        ['D', '6', '3', '9'],
        ['E', '2', '5', '7'],
        ['F', '5', '9', '14'],
        ['G', '3', '7', '10'],
      ]}},
      {'p': 'The project duration is the largest earliest finish, '
            '$\\max(14, 10) = \\textbf{14 weeks}$.'},
      {'h4': 'Backward pass'},
      {'p': 'Both F and G finish the project, so both have $LF = 14$. Working back: '
            '$LS_F = 14 - 5 = 9$, so C and D must each finish by week 9. A precedes both C '
            '($LS = 5$) and E ($LS = 9$), so $LF_A = \\min(5, 9) = 5$.'},
      {'table': {'align': 'lrrrrr',
        'head': ['Activity', 'Duration', 'ES', 'EF', 'LS', 'LF'], 'rows': [
        ['A', '5', '0', '5', '0', '5'],
        ['B', '3', '0', '3', '0', '3'],
        ['C', '4', '5', '9', '5', '9'],
        ['D', '6', '3', '9', '3', '9'],
        ['E', '2', '5', '7', '9', '11'],
        ['F', '5', '9', '14', '9', '14'],
        ['G', '3', '7', '10', '11', '14'],
      ]}},
      {'h4': 'Float and the critical path'},
      {'table': {'align': 'lrrl',
        'head': ['Activity', 'Total float', 'Free float', 'Comment'], 'rows': [
        ['A', '0', '0', 'Critical'],
        ['B', '0', '0', 'Critical'],
        ['C', '0', '0', 'Critical'],
        ['D', '0', '0', 'Critical'],
        ['E', '4', '0', 'Float belongs to the path E–G'],
        ['F', '0', '0', 'Critical'],
        ['G', '4', '4', 'Float is entirely its own'],
      ]}},
      {'p': 'There are **two critical paths**, each of 14 weeks:'},
      {'tex': 'A \\to C \\to F = 5 + 4 + 5 = 14 \\qquad B \\to D \\to F = 3 + 6 + 5 = 14'},
      {'note': 'Compare E and G. Both have four weeks of total float, but E\'s **free float is '
               'zero**: delaying E by even one week pushes G back, because G starts as soon as '
               'E finishes. G\'s free float is the full four weeks, since nothing follows it. '
               'Total float is shared along a chain; free float belongs to the individual '
               'activity. A question asking "which activity can be delayed without affecting '
               'any other activity" is asking for **free** float.'},
      {'key': 'Two critical paths mean the project has no slack anywhere on either. To shorten '
              'the project, either shorten F (which is on both paths) or shorten one activity '
              'on each path simultaneously — shortening A alone achieves nothing, because '
              'B–D–F still takes 14 weeks.'}]}},
  ]},

  {'n': '17.3', 't': 'PERT: three time estimates', 'b': [
    {'p': 'Critical path analysis assumes each duration is known. **PERT** (Programme '
          'Evaluation and Review Technique) treats duration as uncertain, using three '
          'estimates for each activity: **optimistic** $a$, **most likely** $m$, and '
          '**pessimistic** $b$.'},
    {'fbox': {'h': 'PERT formulae', 'rows': [
      {'lb': 'Expected duration',
       'tex': 't_e = \\frac{a + 4m + b}{6}'},
      {'lb': 'Variance of an activity',
       'tex': '\\sigma^2 = \\left(\\frac{b - a}{6}\\right)^{2}'},
      {'lb': 'Project variance',
       'tex': '\\sigma_p^2 = \\sum \\sigma^2 \\ \\text{(critical activities only)}'},
      {'lb': 'Probability of meeting a target date',
       'tex': 'z = \\frac{T_s - T_e}{\\sigma_p}'},
    ]}},
    {'p': 'The weights $1 : 4 : 1$ give the most likely estimate four times the influence of '
          'the extremes, which corresponds to a beta distribution. Activity variances are '
          'added — but only along the **critical path**, and only because the activities are '
          'assumed independent.'},
    {'eg': {'t': 'PERT computation', 'q': [
      {'p': 'The critical path of a project consists of three activities with the following '
            'estimates (in weeks):'},
      {'table': {'align': 'lrrr',
        'head': ['Activity', 'Optimistic $a$', 'Most likely $m$', 'Pessimistic $b$'], 'rows': [
        ['P', '2', '4', '6'],
        ['Q', '3', '5', '13'],
        ['R', '4', '6', '8'],
      ]}},
      {'p': 'Compute the expected project duration and the probability of completing within 18 '
            'weeks.'}],
      'a': [
      {'table': {'align': 'lrr',
        'head': ['Activity', 'Expected time $t_e$', 'Variance $\\sigma^2$'], 'rows': [
        ['P', '$(2 + 16 + 6)/6 = 4.00$', '$(4/6)^2 = 0.444$'],
        ['Q', '$(3 + 20 + 13)/6 = 6.00$', '$(10/6)^2 = 2.778$'],
        ['R', '$(4 + 24 + 8)/6 = 6.00$', '$(4/6)^2 = 0.444$'],
        ['**Total**', '**16.00**', '**3.667**'],
      ]}},
      {'tex': 'T_e = 16 \\text{ weeks}, \\qquad \\sigma_p = \\sqrt{3.667} = 1.915 \\text{ weeks}'},
      {'tex': 'z = \\frac{T_s - T_e}{\\sigma_p} = \\frac{18 - 16}{1.915} = 1.04'},
      {'p': 'From normal tables, the area to the left of $z = 1.04$ is 0.8508.'},
      {'p': 'There is therefore approximately an **85% probability** of completing the project '
            'within 18 weeks.'},
      {'note': 'Note that activity Q has by far the largest variance (2.778 of the total '
               '3.667), entirely because its pessimistic estimate of 13 weeks is so far above '
               'its most likely 5. Q is where the project risk lies, and where management '
               'attention and contingency should be directed — even though its expected '
               'duration is unremarkable.'}]}},
  ]},

  {'n': '17.4', 't': 'Uses and limitations', 'b': [
    {'h4': 'Uses'},
    {'ul': [
      'Identifies the activities that control the project duration, so management effort can '
      'be concentrated where it matters.',
      'Quantifies the effect of a delay, and shows how much delay each non-critical activity '
      'can absorb.',
      'Supports **crashing** decisions: where a project must be shortened, the analysis shows '
      'which activity to accelerate and at what cost per week saved.',
      'Assists resource scheduling and smoothing, by showing where activities can be moved '
      'within their float.',
      'Provides a framework for progress reporting and control during execution.',
    ]},
    {'h4': 'Limitations'},
    {'ul': [
      'Durations are estimates. In CPM they are treated as certain; PERT allows for '
      'uncertainty but assumes a particular distribution and that activities are independent.',
      'The basic model ignores **resource constraints** — it assumes activities scheduled in '
      'parallel can actually be staffed and equipped in parallel.',
      'The probability calculation considers only the critical path, so a near-critical path '
      'with high variance may in fact be the one that overruns.',
      'The network must be redrawn when the logic changes, and large projects require software.',
      'Cost is not modelled in the basic network; a separate cost-schedule analysis is needed.',
    ]},
  ]},

  {'n': '17.5', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'All the terms'},
    {'ul': [
      '**Network analysis / CPM / PERT** — techniques for planning, scheduling and '
      'controlling projects.',
      '**Activity** — a task that consumes time and resources; drawn as an arrow.',
      '**Event (node)** — the start or finish of one or more activities; drawn as a circle; '
      'consumes no time.',
      '**Dummy activity** — a logical link that consumes no time and no resources; a dotted '
      'arrow; used to show dependency or to keep activities uniquely identified.',
      '**Preceding / succeeding activities** — those that must finish before / can start after '
      'a given activity.',
      '**Path** — a sequence of activities from start to end; its **duration** is the sum of '
      'its activity times.',
      '**Critical path** — the path with the **longest** duration; it fixes the shortest time '
      'to complete the project. (There can be more than one.)',
      '**Critical activities** — activities on the critical path; any delay to one delays the '
      'whole project (their float is zero).',
      '**EST / EFT** — earliest start / finish time of an activity (from the forward pass).',
      '**LST / LFT** — latest start / finish time without delaying the project (backward '
      'pass).',
      '**Float (slack)** — spare time on a non-critical activity.',
      '**PERT** — network analysis with three time estimates per activity, giving an expected '
      'duration and a variance.',
    ]},
    {'h3': 'A. Forward and backward passes'},
    {'fbox': {'h': 'Event / activity times', 'rows': [
      {'lb': 'Forward pass (earliest)',
       'tex': 'E_j = \\max_{i}\\{E_i + d_{ij}\\} \\qquad EFT = EST + d'},
      {'lb': 'Backward pass (latest)',
       'tex': 'L_i = \\min_{j}\\{L_j - d_{ij}\\} \\qquad LST = LFT - d'},
      {'lb': 'Project duration', 'tex': '= E_{\\text{end}} = \\text{length of the critical '
              'path}'},
    ]}},
    {'h3': 'B. The three floats'},
    {'fbox': {'h': 'Float', 'rows': [
      {'lb': 'Total float',
       'tex': 'TF = LFT - EFT = LST - EST = L_j - E_i - d_{ij}'},
      {'lb': 'Free float',
       'tex': 'FF = E_j - E_i - d_{ij} \\quad (\\text{delay without affecting the next '
              'activity\'s EST})'},
      {'lb': 'Independent float',
       'tex': 'IF = E_j - L_i - d_{ij} \\quad (\\text{floor 0; delay affecting nothing '
              'either side})'},
    ]}},
    {'note': 'On the critical path every float is zero. $FF \\le TF$ and $IF \\le FF$.'},
    {'h3': 'C. PERT with three time estimates'},
    {'fbox': {'h': 'PERT', 'rows': [
      {'lb': 'Expected activity time',
       'tex': 't_e = \\dfrac{a + 4m + b}{6}',
       'nt': '$a$ = optimistic, $m$ = most likely, $b$ = pessimistic time.'},
      {'lb': 'Activity variance',
       'tex': '\\sigma^{2} = \\left(\\dfrac{b - a}{6}\\right)^{2}'},
      {'lb': 'Project duration', 'tex': 'T_e = \\sum_{\\text{critical}} t_e'},
      {'lb': 'Project variance / SD',
       'tex': '\\sigma_p^{2} = \\sum_{\\text{critical}} \\sigma^{2}, \\qquad '
              '\\sigma_p = \\sqrt{\\sigma_p^{2}}'},
      {'lb': 'Probability of finishing by a scheduled date $T_s$',
       'tex': 'z = \\dfrac{T_s - T_e}{\\sigma_p} \\ \\Rightarrow \\ \\text{read } P(Z \\le z) '
              '\\text{ from the normal table}'},
    ]}},
    {'h3': 'D. Crashing (time–cost trade-off)'},
    {'tex': '\\text{Cost slope} = \\dfrac{\\text{crash cost} - \\text{normal cost}}'
            '{\\text{normal time} - \\text{crash time}} \\quad (\\text{extra cost per period '
            'saved; crash the cheapest critical activity first})'},
  ]},
 ],
 'formulas': [
  {'lb': 'Earliest start (forward pass)',
   'tex': 'ES_j = \\max(ES_i + d_{ij})'},
  {'lb': 'Latest finish (backward pass)',
   'tex': 'LF_i = \\min(LF_j - d_{ij})'},
  {'lb': 'Activity times',
   'tex': 'EFT = EST + d, \\qquad LST = LFT - d'},
  {'lb': 'Total float', 'tex': 'TF = LFT - EFT = LST - EST'},
  {'lb': 'Free float', 'tex': 'FF = E_j - E_i - d_{ij}'},
  {'lb': 'Independent float', 'tex': 'IF = E_j - L_i - d_{ij} \\ (\\ge 0)'},
  {'lb': 'PERT expected time',
   'tex': 't_e = \\frac{a + 4m + b}{6}'},
  {'lb': 'PERT activity variance',
   'tex': '\\sigma^2 = \\left(\\frac{b-a}{6}\\right)^2'},
  {'lb': 'Project standard deviation',
   'tex': '\\sigma_p = \\sqrt{\\textstyle\\sum_{\\text{critical}} \\sigma^2}'},
  {'lb': 'Probability of meeting a date',
   'tex': 'z = \\frac{T_s - T_e}{\\sigma_p}'},
  {'lb': 'Crash cost slope',
   'tex': '\\frac{\\text{crash cost} - \\text{normal cost}}{\\text{normal time} - '
          '\\text{crash time}}'},
 ],
 'focus':
   'A regular Section B question, and one of the most reliably scored. The table of activities '
   'is given, and the marks follow the method: network diagram, forward pass, backward pass, '
   'float table, critical path, duration. PERT appears less often but the $t_e$ formula is '
   'common in Section A. Present the passes in a table even if you also draw the network — the '
   'examiner can then follow the arithmetic.',
 'errors': [
   'Taking the minimum on the forward pass or the maximum on the backward pass.',
   'Identifying the shortest path as critical instead of the longest.',
   'Confusing total float with free float.',
   'Giving a dummy activity a duration, or omitting one where two activities share both start '
   'and end events.',
   'Adding variances along the whole network rather than only along the critical path.',
   'Using the most likely time instead of $t_e$ in a PERT network.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The critical path in a network is',
    'o': ['the shortest path through the network', 'the longest path through the network',
          'the path with the most activities', 'the path with the greatest total float',
          'the path with the fewest dummy activities'],
    'a': 1,
    'w': 'The longest path determines the project duration and has zero float throughout.',
    'src': 'Chapter 17.1'},
   {'q': 'An activity has ES = 8, EF = 13, LS = 11 and LF = 16. Its total float is',
    'o': ['2 days', '3 days', '5 days', '8 days', 'nil'],
    'a': 1,
    'w': 'Total float is $LS - ES$, equivalently $LF - EF$.',
    'calc': 'TF = 11 - 8 = 3 \\quad(\\text{or } 16 - 13 = 3)',
    'src': 'Chapter 17.2'},
   {'q': 'Using PERT with $a = 3$, $m = 6$ and $b = 15$ days, the expected duration is',
    'o': ['6 days', '7 days', '8 days', '9 days', '24 days'],
    'a': 1,
    'w': 'Weight the most likely estimate four times and divide the total by six.',
    'calc': 't_e = \\frac{3 + 4(6) + 15}{6} = \\frac{42}{6} = 7',
    'src': 'Chapter 17.3'},
   {'q': 'A dummy activity in a network',
    'o': ['consumes resources but no time', 'consumes neither time nor resources',
          'consumes time but no resources', 'is always on the critical path',
          'has the longest duration'],
    'a': 1,
    'w': 'A dummy exists only to express a dependency or to separate two activities sharing '
         'the same start and end events. Its duration is zero.',
    'src': 'Chapter 17.1'},
   {'q': 'On the forward pass, where several activities converge on an event, the earliest '
         'event time is',
    'o': ['the smallest of the earliest finishes', 'the largest of the earliest finishes',
          'the average of the earliest finishes', 'the sum of the earliest finishes',
          'always zero'],
    'a': 1,
    'w': 'Every converging activity must be complete before the event is reached, so the '
         'latest arrival governs.',
    'src': 'Chapter 17.2'},
   {'q': 'If three activities on the critical path have variances of 1.0, 2.25 and 0.75, the '
         'standard deviation of the project duration is',
    'o': ['4.00', '2.00', '1.50', '4.00 weeks squared', '3.00'],
    'a': 1,
    'w': 'Add the variances, then take the square root — variances add, standard deviations '
         'do not.',
    'calc': '\\sigma_p = \\sqrt{1.0 + 2.25 + 0.75} = \\sqrt{4} = 2.0',
    'src': 'Chapter 17.3'},
  ],
  'theory': [
   {'q': 'The following activities make up a construction project:\n\nA (no predecessor, 4 '
         'weeks); B (no predecessor, 7 weeks); C (after A, 6 weeks); D (after A, 3 weeks); '
         'E (after B and C, 5 weeks); F (after D, 4 weeks); G (after E and F, 2 weeks).\n\n'
         '(a) Determine the earliest and latest start and finish times of each activity. '
         '(b) State the project duration and the critical path. (c) Compute the total float of '
         'each activity. (d) The contractor is offered a bonus for finishing in 15 weeks. '
         'Advise whether this is achievable and what would be required.',
    'marks': 15,
    'a': [
      {'h4': '(a) Forward and backward passes'},
      {'p': '**Forward pass.** A and B start at week 0. C and D follow A, so both start at '
            'week 4. E requires both B ($EF = 7$) and C ($EF = 10$), so $ES_E = \\max(7, 10) '
            '= 10$. F follows D ($EF = 7$). G requires E ($EF = 15$) and F ($EF = 11$), so '
            '$ES_G = \\max(15, 11) = 15$.'},
      {'p': '**Backward pass.** The project ends at week 17, so $LF_G = 17$ and $LS_G = 15$. '
            'Both E and F must finish by week 15. A precedes C ($LS = 4$) and D ($LS = 8$), so '
            '$LF_A = \\min(4, 8) = 4$.'},
      {'table': {'align': 'lrrrrrr',
        'head': ['Activity', 'Duration', 'ES', 'EF', 'LS', 'LF', 'Total float'], 'rows': [
        ['A', '4', '0', '4', '0', '4', '0'],
        ['B', '7', '0', '7', '3', '10', '3'],
        ['C', '6', '4', '10', '4', '10', '0'],
        ['D', '3', '4', '7', '8', '11', '4'],
        ['E', '5', '10', '15', '10', '15', '0'],
        ['F', '4', '7', '11', '11', '15', '4'],
        ['G', '2', '15', '17', '15', '17', '0'],
      ]}},
      {'h4': '(b) Duration and critical path'},
      {'p': 'The project duration is **17 weeks**. The critical path consists of the activities '
            'with zero total float:'},
      {'tex': 'A \\to C \\to E \\to G = 4 + 6 + 5 + 2 = 17 \\text{ weeks}'},
      {'p': 'For comparison, the other paths are $B \\to E \\to G = 14$ weeks and '
            '$A \\to D \\to F \\to G = 13$ weeks, both shorter.'},
      {'h4': '(c) Total float'},
      {'p': 'Shown in the final column above. B has 3 weeks of float, D and F 4 weeks each '
            '(shared along the path A–D–F, since delaying D by four weeks consumes the whole of '
            'F\'s float too), and the four critical activities have none.'},
      {'h4': '(d) The 15-week bonus'},
      {'p': 'Finishing in 15 weeks requires the project to be shortened by **2 weeks**, and '
            'since only the critical path determines the duration, the saving must come from '
            'A, C, E or G. Crashing a non-critical activity such as B, D or F would cost money '
            'and achieve nothing.'},
      {'p': 'Two weeks would have to be taken out of the critical path — for example two weeks '
            'off C, or one week each off C and E — by working overtime, adding labour or plant, '
            'or overlapping activities where the technical logic permits.'},
      {'p': 'Two cautions apply:'},
      {'ul': [
        '**The critical path may shift.** The next-longest path, $B \\to E \\to G$, takes 14 '
        'weeks. If the two weeks are taken from C alone, path A–C–E–G falls to 15 weeks while '
        'B–E–G stays at 14, so the target is met and B becomes critical at only one week of '
        'float. But a further reduction beyond 14 weeks would require B to be shortened as '
        'well. Any crashing exercise must be re-run through the network after each reduction.',
        '**The bonus must exceed the crash cost.** The decision rests on comparing the bonus '
        'with the incremental cost of shortening the two weeks, taking the cheapest critical '
        'activity first. If overtime, additional plant hire and the loss of efficiency come to '
        'more than the bonus, the contractor should decline it and complete in 17 weeks.',
      ]},
      {'p': '**Advice:** 15 weeks is achievable, since only two weeks need be recovered from a '
            'critical path that has four activities on it. The contractor should obtain crash '
            'costs per week for A, C, E and G, select the two cheapest weeks, verify by '
            're-running the network that no other path becomes binding, and accept the bonus '
            'only if it exceeds that cost.'}],
    'src': 'Chapter 17.2'},
  ]},
}
