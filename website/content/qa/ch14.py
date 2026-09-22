CH = {
 'n': 14,
 't': 'Introduction to Operations Research',
 'brief': 'Why decision-making needs an objective, scientific method; the stages of an operations '
          'research (OR) study, from identifying the problem to implementation; and where OR is '
          'relevant in business, including to the accountant.',
 'outcomes': [
   'Understand the concept of operations research (OR)',
   'Understand the major stages in an OR study',
   'Know the various situations where OR can be applied',
 ],
 'secs': [
  {'n': '14.1', 't': 'Introduction', 'b': [
    {'p': 'Decision-making is a day-to-day activity: individuals, societies, government and '
          'business organisations all make decisions, in order to benefit the decision-maker and, '
          'in most cases, those the decision affects.'},
    {'p': 'A problem must exist before a decision is made. Decision-making is a **response to an '
          'identified problem** — a problem that arises from a discrepancy between existing '
          'conditions and the organisation\'s set objectives. Making a decision requires weighing '
          'a lot of factors, to ensure the decision is the best one both under existing conditions '
          'and for the near future.'},
    {'p': 'Decision-making is not an easy task. A manager confronted with a problem has to decide '
          'a course of action, taking on some risk, since there is always some uncertainty '
          '(however little) about the consequences — and will want to reduce that risk to the '
          'barest minimum.'},
    {'key': 'There is therefore a need for a method that assists in making decisions that are '
            '**objective and scientific**. That method is called **Operations Research**.'},
  ]},

  {'n': '14.2', 't': 'The stages and relevance of operations research', 'b': [
    {'h3': 'Main stages of OR'},
    {'steps': [
      '**Identification of problems and objectives.** The problem for which a decision is '
      'sought must first be defined, and the objectives clearly spelt out.',
      '**Identification of variables.** Both the **controllable (decision) variables** and the '
      '**uncontrollable variables** of the system must be identified. The constraints on the '
      'variables and the system are taken into account, and the "bounds" of the system and the '
      'options open must also be established.',
      '**Construction of a model.** The central aspect of an OR project — a model is needed '
      'because it is impossible to experiment with the real-life situation. A suitable model '
      'must specify quantitative relationships for the objective and constraints of the problem '
      'in terms of the controllable variables, and it must be decided whether the system is to '
      'be treated as **deterministic** or **probabilistic**.',
      '**Solution of the model.** Once built, various mathematical methods are used to '
      'manipulate the model to obtain a solution — an **optimal** solution where an analytic '
      'solution is possible, or only a **"good"** solution where a simulation or heuristic '
      'model is used.',
      '**Testing the model.** The model and its solution are validated to see whether the model '
      'can reliably predict the actual system\'s performance, reacting to change the way the '
      'real system does. Past data for the system may be used for this: the model may be '
      'considered valid if, under similar input conditions, it reproduces the system\'s past '
      'performance to a reasonable extent.',
      '**Implementation.** Those who will implement the result should ideally be part of the OR '
      'team; if not, the team should remain on hand to advise if difficulties arise during '
      'implementation. A set of operating instructions may be necessary.',
    ]},
    {'h4': 'Model types met in constructing a model'},
    {'p': 'A model can be **mathematical** or **heuristic**. Mathematical models are mostly used '
          'for OR, on the assumption that all the relevant variables are quantifiable, so the '
          'model becomes a mathematical function describing the system under study. Some '
          'mathematical models are:'},
    {'table': {'align': 'll', 'head': ['Model', 'Concerned with'], 'rows': [
      ['**Allocation models**', 'Sharing scarce resources among various competing activities '
       '— linear programming, transportation and assignment are examples'],
      ['**Inventory models**', 'Policies for holding stocks of finished goods, ordering '
       'quantities and re-order level'],
      ['**Queuing models**', 'Arrivals at, and departures from, service points, and the '
       'resulting queues of customers waiting for service'],
      ['**Replacement models**', 'Determining an optimal policy for replacing "failed" items'],
      ['**Simulation models**', 'Based on the probabilities of certain input values taking on '
       '(imitating) a particular value — random numbers are used most of the time'],
    ]}},
    {'note': 'Allocation models and inventory models are treated in detail in the chapters that '
             'follow; queuing, replacement and simulation models — beyond queuing, which is '
             'outside the scope of this study pack — are also developed later.'},
    {'p': '**Heuristic models** are models that employ intuitive rules to generate new '
          'strategies, which hopefully will yield improved solutions.'},
    {'h3': 'Relevance of OR'},
    {'p': 'OR has a very wide area of application in business, engineering, industry, government '
          'and science. It will always be relevant in any situation where resources do not meet '
          'the needs or requirements — and even where resources are enough, there is still a need '
          'to allocate them in the best (an **optimal**) way.'},
    {'ul': [
      'In **production planning**, OR may be used to allocate materials to production schedules '
      'in an optimal way; in **transportation problems**, to decide on the best routes — those '
      'with minimum cost.',
      'An **accountant** may apply OR to investment decisions where the funds available are not '
      'sufficient for all available projects — **capital rationing**.',
      'An accountant can also apply OR in any situation calling for **cost-benefit analysis**.',
    ]},
  ]},

  {'n': '14.3', 't': 'Worksheet summary — every stage and model type', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§14.1 Introduction** — decision-making is a response to an identified problem (a '
      'discrepancy between existing conditions and the organisation\'s objectives); it is '
      'risky and uncertain, so an **objective and scientific method** is needed — that method '
      'is Operations Research.',
      '**§14.2 Stages** — (1) identify problems and objectives; (2) identify controllable and '
      'uncontrollable variables, constraints and bounds; (3) construct a model (mathematical or '
      'heuristic; deterministic or probabilistic) — mathematical models include allocation, '
      'inventory, queuing, replacement and simulation models; (4) solve the model — optimal '
      '(analytic) or "good" (simulation/heuristic); (5) test the model against past data to '
      'validate it; (6) implement, ideally with the implementers on the OR team.',
      '**Relevance** — wide application across business, engineering, industry, government and '
      'science; relevant wherever resources don\'t meet needs, or must still be optimally '
      'allocated even where sufficient. Accountant\'s own uses: **capital rationing** and '
      '**cost-benefit analysis**.',
    ]},
    {'h3': 'The five mathematical model types, at a glance'},
    {'ul': [
      'Allocation — scarce resources among competing activities (LP, transportation, '
      'assignment)',
      'Inventory — stockholding policy, order quantity, re-order level',
      'Queuing — arrivals/departures at service points',
      'Replacement — optimal policy for replacing failed items',
      'Simulation — imitates input-value probabilities, using random numbers',
    ]},
  ]},

  {'n': '14.4', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'Decision-making is important in order to (A) Make profit for a business (B) Solve an '
        'identified problem (C) Please the customers (D) Perform a task (E) Please the '
        'management',
        'A simulation model is a (A) Mathematical model (B) Probabilistic model (C) Non-'
        'mathematical model (D) Constant model (E) Non-probabilistic model',
        'Operations Research is relevant because (A) Resources do not always merge the needs '
        '(B) Resources have to be allocated (C) All activities have to be taken care of '
        '(D) In any operation, research is important (E) Resources have to be allocated in an '
        'optimal way',
        'One of the following is NOT a mathematical model (A) Allocation model (B) Inventory '
        'model (C) Queuing model (D) Additive model (E) Replacement model',
        'Operations Research is a method which assists in making decisions that are '
        '…................. and …………….',
        'A model should specify quantitative relationships for the ……..…… and ……….. of the '
        'problem in terms of controllable variables.',
        'In the financial circle, OR is used for ……................... rationing.',
        'In OR, the transportation problem can also be referred to as an ……........... problem.',
        'OR assists to reduce the ……................. involved in decision-making.',
        'OR will always be relevant in any situation where ……................. do not merge the '
        'needs.',
      ]}],
      'a': [
      {'ol': [
        '**B** — decision-making exists to solve an identified problem.',
        '**A** — a simulation model is a mathematical model, based on the probabilities of '
        'input values.',
        '**E** — resources have to be allocated in an optimal way.',
        '**D** — "additive model" is not one of the five mathematical models (allocation, '
        'inventory, queuing, replacement, simulation).',
        '**Objective and scientific** (either order).',
        '**Objective and constraints.**',
        '**Capital** rationing.',
        '**Allocation** problem.',
        '**Risks.**',
        '**Resources.**',
      ]}]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'One or two Section A marks on the stages of an OR study, the five mathematical model types, '
   'or the accountant\'s own use of OR (capital rationing, cost-benefit analysis). Learn the six '
   'stages as a sequence — identify problem/objectives, identify variables, construct the model, '
   'solve it, test it, implement it — since past questions test them both as a list and as '
   'fill-in-the-blank fragments of it.',
 'errors': [
   'Treating "identification of problems" and "identification of variables" as one stage rather '
   'than two separate ones.',
   'Forgetting that a simulation model, despite imitating real-world randomness, is still '
   'classed as a **mathematical** model in this chapter.',
   'Confusing "allocation" (scarce resources among competing activities) with "additive", which '
   'is not one of the five named mathematical model types.',
   'Missing the accountant-specific relevance points: capital rationing and cost-benefit '
   'analysis.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The central aspect of an OR project, needed because it is impossible to experiment '
         'with the real-life situation, is',
    'o': ['identification of variables', 'construction of a model', 'testing the model',
          'implementation', 'identification of the problem'],
    'a': 1,
    'w': 'A model represents the system so it can be manipulated safely; the study text calls '
         'this "the central aspect of an OR project."',
    'src': 'Chapter 14.2', 'sec': '14.2'},
   {'q': 'Where an analytic solution to an OR model is not possible and a simulation or '
         'heuristic model is used instead, the result obtained can only be described as a',
    'o': ['optimal solution', '"good" solution', 'deterministic solution', 'feasible region',
          'controllable variable'],
    'a': 1,
    'w': 'Analytic solutions give an optimal solution; simulation/heuristic models give only a '
         '"good" solution.',
    'src': 'Chapter 14.2', 'sec': '14.2'},
   {'q': 'Which of the following is one of the five mathematical models named in this chapter?',
    'o': ['Additive model', 'Regression model', 'Queuing model', 'Correlation model',
          'Index model'],
    'a': 2,
    'w': 'The five are allocation, inventory, queuing, replacement and simulation models.',
    'src': 'Chapter 14.2', 'sec': '14.2'},
   {'q': 'An accountant is most likely to apply operations research to investment decisions '
         'where available funds are insufficient for all worthwhile projects — this is called',
    'o': ['cost-benefit analysis', 'capital rationing', 'replacement analysis',
          'sensitivity analysis', 'queuing analysis'],
    'a': 1,
    'w': 'The study text names capital rationing as one of the accountant\'s own applications '
         'of OR.',
    'src': 'Chapter 14.2', 'sec': '14.2'},
  ],
  'theory': [
   {'q': 'Outline the main stages involved in an operations research study, and state two '
         'situations in which an accountant may apply operations research.',
    'marks': 10,
    'a': [
      {'ol': [
        '**Identification of problems and objectives** — the problem for which a decision is '
        'sought is defined, and the objectives clearly spelt out.',
        '**Identification of variables** — the controllable and uncontrollable variables, '
        'constraints and "bounds" of the system are established.',
        '**Construction of a model** — a mathematical (or heuristic) model is built, specifying '
        'quantitative relationships for the objective and constraints, and deciding whether the '
        'system is deterministic or probabilistic.',
        '**Solution of the model** — mathematical methods are applied to obtain an optimal '
        'solution (or, for simulation/heuristic models, a "good" solution).',
        '**Testing the model** — the model and its solution are validated against past data, to '
        'check it can reliably predict the system\'s actual performance.',
        '**Implementation** — the result is put into effect, ideally with those who will '
        'implement it included in the OR team, supported by a set of operating instructions.',
      ]},
      {'h4': 'Two accountant applications'},
      {'ul': [
        '**Capital rationing** — applying OR to investment decisions where the funds available '
        'are not sufficient for all the projects available.',
        '**Cost-benefit analysis** — applying OR to any situation calling for a comparison of '
        'costs and benefits.',
      ]}],
    'src': 'Chapter 14.2', 'sec': '14.2'},
  ]},
}
