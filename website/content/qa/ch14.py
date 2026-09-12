CH = {
 'n': 14,
 't': 'Introduction to Operations Research',
 'brief': 'The nature and history of operations research, the stages of an OR study, the types '
          'of model used, the main techniques and where each applies, and the benefits and '
          'limitations of the approach.',
 'outcomes': [
   'Define operations research and explain its essential characteristics',
   'Describe the stages of an operations research study',
   'Classify models as iconic, analogue or symbolic, and as deterministic or stochastic',
   'Match the principal OR techniques to the problems they solve',
   'Discuss the benefits and limitations of operations research',
 ],
 'secs': [
  {'n': '14.1', 't': 'What operations research is', 'b': [
    {'def': {'t': 'Operations research',
             'd': 'The application of scientific method — in particular mathematical and '
                  'statistical modelling — to the analysis of complex operational problems, in '
                  'order to provide managers with a quantitative basis for decisions.'}},
    {'p': 'The discipline grew out of the Second World War, when interdisciplinary teams of '
          'scientists were asked to improve the effectiveness of military operations: convoy '
          'sizes, radar deployment, bombing patterns. After 1945 the same methods were carried '
          'into industry, and the growth of computing from the 1960s made large-scale models '
          'practicable. It is variously known as operational research, management science and '
          'decision science.'},
    {'h4': 'Characteristics'},
    {'ul': [
      '**System orientation.** The problem is viewed as part of a whole. A decision that '
      'optimises one department may damage the organisation — minimising inventory cost at the '
      'cost of stockouts in production is the classic example.',
      '**Interdisciplinary team approach.** Accountants, engineers, statisticians and '
      'operational managers bring different views of the same problem.',
      '**Scientific method.** Observation, hypothesis, model construction, testing against '
      'data, and revision.',
      '**Quantitative basis for decisions.** The output is a number or a policy, not an '
      'opinion.',
      '**Use of models.** The real system is represented by an abstraction that can be '
      'manipulated safely and cheaply.',
      '**Search for an optimum.** OR seeks the best feasible solution, not merely a workable '
      'one — subject to the constraints actually faced.',
      '**Decision support, not decision replacement.** The model informs the manager, who '
      'retains responsibility for factors the model omits.',
    ]},
  ]},

  {'n': '14.2', 't': 'Stages of an OR study', 'b': [
    {'steps': [
      '**Formulate the problem.** Identify the decision-maker, the objective, the decision '
      'variables under his control, the constraints, and the measure of effectiveness. This is '
      'the hardest stage and the one most often skimped.',
      '**Construct the model.** Express the objective and the constraints as mathematical '
      'relationships among the variables — for example a linear objective function subject to '
      'linear inequalities.',
      '**Collect data and derive a solution.** Obtain the parameter values and solve the model '
      'analytically, by an algorithm such as the simplex method, or by simulation.',
      '**Test the model and the solution (validation).** Check the model against historical '
      'data: does it reproduce known outcomes? Perform sensitivity analysis to see how far the '
      'solution depends on uncertain parameters.',
      '**Establish controls over the solution.** Identify the parameters that would change the '
      'decision if they moved, and set up monitoring so that the model is revisited when they '
      'do.',
      '**Implement the solution.** Convert the result into operating instructions, secure the '
      'co-operation of the people who must follow them, and review performance in operation.',
    ]},
    {'note': 'Examiners very often ask for these stages by name. Learn them as a sequence with '
             'a one-line explanation each; the marks are given for the explanation, not the '
             'list.'},
  ]},

  {'n': '14.3', 't': 'Types of model', 'b': [
    {'h4': 'By degree of abstraction'},
    {'table': {'align': 'lll', 'head': ['Type', 'Description', 'Example'], 'rows': [
      ['**Iconic**', 'A physical, scaled representation that looks like the real thing',
       'A scale model of a factory layout; a globe'],
      ['**Analogue**', 'Uses one property to represent another',
       'An organisation chart; a graph; a thermometer'],
      ['**Symbolic (mathematical)**', 'Uses symbols and equations; the most abstract and the '
       'most flexible', 'A linear programme; the EOQ formula'],
    ]}},
    {'h4': 'By treatment of uncertainty'},
    {'ul': [
      '**Deterministic** — every parameter is known with certainty. Linear programming, EOQ '
      'in its basic form, critical path analysis.',
      '**Stochastic (probabilistic)** — one or more parameters is a random variable. Queueing '
      'theory, simulation, PERT, decision trees.',
    ]},
    {'h4': 'By other criteria'},
    {'ul': [
      '**Static** (a single point in time) against **dynamic** (evolving over periods).',
      '**Descriptive** (shows what happens, e.g. simulation) against **normative or '
      'optimising** (shows what should be done, e.g. linear programming).',
      '**Analytical** (solved by formula) against **numerical or iterative** (solved by '
      'repeated computation, e.g. the simplex method).',
    ]},
  ]},

  {'n': '14.4', 't': 'The principal techniques', 'b': [
    {'table': {'align': 'lll',
      'head': ['Technique', 'Problem it addresses', 'Chapter'], 'rows': [
      ['Linear programming', 'Allocating scarce resources among competing uses to maximise '
       'contribution or minimise cost', '15'],
      ['Inventory control (EOQ)', 'How much to order and when, balancing ordering against '
       'holding cost', '16'],
      ['Network analysis (CPM/PERT)', 'Scheduling the activities of a project and identifying '
       'those that control its duration', '17'],
      ['Replacement analysis', 'When to replace an asset that deteriorates, or a population of '
       'items that fail', '18'],
      ['Transportation and assignment', 'Distributing goods from sources to destinations, and '
       'allocating jobs to workers, at least cost', '19'],
      ['Simulation', 'Systems too complex or too uncertain for an analytical solution', '20'],
      ['Queueing theory', 'Balancing the cost of service capacity against the cost of waiting',
       '—'],
      ['Decision theory', 'Choosing among alternatives under risk or uncertainty', '7'],
      ['Game theory', 'Decisions where the outcome depends on a competitor\'s response', '—'],
      ['Markov analysis', 'Systems moving between states with fixed transition probabilities, '
       'such as brand switching or receivables ageing', '—'],
    ]}},
  ]},

  {'n': '14.5', 't': 'Benefits and limitations', 'b': [
    {'h4': 'Benefits'},
    {'ul': [
      '**Better decisions.** Choices rest on analysis of the actual constraints rather than on '
      'intuition or precedent.',
      '**Better co-ordination.** A model spanning several departments exposes the effect of one '
      'department\'s decisions on another.',
      '**Better control.** Standards produced by the model give management a yardstick against '
      'which to measure operations.',
      '**Better systems.** The discipline of building the model frequently reveals that data '
      'are not collected, or that the objective was never clearly stated.',
      '**Cost saving.** Alternatives are tested on the model rather than on the real system, '
      'which is cheaper and carries no operational risk.',
    ]},
    {'h4': 'Limitations'},
    {'ul': [
      '**Cost and time.** Building, validating and maintaining a model is expensive, and for a '
      'small or one-off problem the cost may exceed the benefit.',
      '**Simplifying assumptions.** Linearity, certainty, constant demand and independence are '
      'assumed for tractability and are often false. The solution is optimal for the model, not '
      'necessarily for the world.',
      '**Data dependence.** Results are only as good as the parameters. Where costs are '
      'estimated or demand forecast, apparent precision is misleading.',
      '**Intangible factors.** Staff morale, customer goodwill, reputation and legal or ethical '
      'constraints resist quantification and are therefore usually left out.',
      '**Communication gap.** Managers may not understand the model and so distrust its output, '
      'while analysts may not understand the operation.',
      '**Resistance to implementation.** A technically sound solution that ignores the people '
      'who must operate it will fail.',
    ]},
    {'key': 'The standard examination answer on limitations should end with a balancing '
            'sentence: OR does not replace managerial judgement, it informs it. The model '
            'handles the quantifiable, and the manager weighs that against the factors no model '
            'contains.'},
  ]},

  {'n': '14.6', 't': 'Worksheet summary — definitions and key lists', 'b': [
    {'note': 'This chapter has no formulae of its own; it is defined vocabulary and lists.'},
    {'h3': 'All the terms'},
    {'ul': [
      '**Operations research (OR)** — the application of scientific method (especially '
      'mathematical modelling) to management problems, to help decision-making. Also called '
      '*operational research* / *management science*.',
      '**Model** — a simplified representation of a real system.',
      '**Iconic model** — a physical scaled likeness (a prototype, a scale building).',
      '**Analogue model** — one property represents another (a graph, a hydraulic model of an '
      'economy).',
      '**Symbolic (mathematical) model** — variables and equations (an LP, an EOQ formula).',
      '**Deterministic model** — no probabilities; inputs known with certainty.',
      '**Stochastic (probabilistic) model** — contains random variables.',
      '**Decision variables** — what the decision-maker controls. **Objective function** — the '
      'quantity to be maximised or minimised. **Constraints** — the limits on the variables. '
      '**Parameters** — fixed known values.',
      '**Feasible solution** — one satisfying all constraints. **Optimal solution** — the '
      'feasible solution with the best objective value.',
    ]},
    {'h3': 'Stages of an OR study'},
    {'ol': [
      'Formulate the problem (define objective, variables, constraints).',
      'Construct the model.',
      'Derive a solution from the model.',
      'Test the model and the solution (validation).',
      'Establish controls over the solution.',
      'Implement the solution.',
    ]},
    {'h3': 'The principal OR techniques (technique → problem)'},
    {'ul': [
      'Linear programming — allocating scarce resources to maximise profit / minimise cost',
      'Transportation & assignment — least-cost distribution / one-to-one allocation',
      'Network analysis (CPM / PERT) — project planning, scheduling and control',
      'Inventory control (EOQ / EBQ) — how much to order and when',
      'Replacement analysis — when to replace equipment',
      'Queuing (waiting-line) theory — service-level vs cost of waiting',
      'Simulation — modelling complex stochastic systems numerically',
      'Decision theory — choosing under risk / uncertainty (expected value, decision trees)',
      'Game theory — competitive decision situations',
      'Dynamic programming — multi-stage decision problems',
    ]},
    {'h3': 'Benefits and limitations (one line each)'},
    {'ul': [
      '**Benefits** — structured analysis; better use of resources; quantified comparison of '
      'options; improved decisions; identifies the critical factors.',
      '**Limitations** — a model only captures the quantifiable; data may be poor or costly; '
      'expensive and time-consuming; assumptions may not hold; does not replace managerial '
      'judgement, only informs it.',
    ]},
  ]},
 ],
 'formulas': [],
 'focus':
   'One or two Section A marks on definitions, the stages of a study, or the classification of '
   'models. It also supplies the discussion part of a Section B question whose calculation is '
   'drawn from a later chapter — typically "state the assumptions of the model you have used" '
   'or "comment on the limitations of your solution". Those parts are pure recall and should '
   'never be left blank.',
 'errors': [
   'Confusing analogue models with iconic models; an organisation chart is analogue, a scale '
   'model is iconic.',
   'Listing the stages of an OR study without explaining any of them.',
   'Describing OR as replacing management decision-making rather than supporting it.',
   'Omitting validation and implementation, which are the two stages examiners most often '
   'test.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A model that uses one property to represent another, such as a graph or an '
         'organisation chart, is described as',
    'o': ['iconic', 'analogue', 'symbolic', 'stochastic', 'normative'],
    'a': 1,
    'w': 'Analogue models substitute one property for another. Iconic models physically '
         'resemble the original; symbolic models use equations.',
    'src': 'Chapter 14.3'},
   {'q': 'Which of the following is a deterministic model?',
    'o': ['Simulation', 'Linear programming', 'Queueing theory', 'PERT', 'Markov analysis'],
    'a': 1,
    'w': 'Linear programming assumes all coefficients are known with certainty. The others all '
         'involve random variables.',
    'src': 'Chapter 14.3'},
   {'q': 'Operations research first developed as a discipline during',
    'o': ['the Industrial Revolution', 'the Second World War', 'the 1970s oil crisis',
          'the dot-com era', 'the Great Depression'],
    'a': 1,
    'w': 'Interdisciplinary teams were formed to improve military operations, and the methods '
         'were carried into industry after 1945.',
    'src': 'Chapter 14.1'},
   {'q': 'In an operations research study, checking the model against historical data to see '
         'whether it reproduces known outcomes is called',
    'o': ['formulation', 'validation', 'implementation', 'optimisation', 'sensitivity'],
    'a': 1,
    'w': 'Validation tests whether the model is an adequate representation before its output '
         'is relied on.',
    'src': 'Chapter 14.2'},
   {'q': 'The technique most appropriate for allocating scarce resources among competing '
         'products to maximise contribution is',
    'o': ['network analysis', 'linear programming', 'simulation',
          'the economic order quantity model', 'replacement analysis'],
    'a': 1,
    'w': 'Linear programming maximises a linear objective subject to linear resource '
         'constraints.',
    'src': 'Chapter 14.4'},
  ],
  'theory': [
   {'q': 'Define operations research and outline the stages involved in an operations research '
         'study. State four limitations of the approach.',
    'marks': 15,
    'a': [
      {'h4': 'Definition'},
      {'p': 'Operations research is the application of scientific method, and in particular of '
            'mathematical and statistical modelling, to the analysis of complex operational '
            'problems, so as to give management a quantitative basis for decision-making. It is '
            'characterised by a systems view of the problem, an interdisciplinary team, the use '
            'of models in place of experiment on the real system, and a search for the optimal '
            'feasible solution rather than merely an acceptable one.'},
      {'h4': 'Stages of a study'},
      {'ol': [
        '**Formulation of the problem.** The analyst identifies who the decision-maker is, what '
        'objective is to be pursued, which variables are under the decision-maker\'s control, '
        'what constraints bind, and what measure of effectiveness will be used. A problem badly '
        'formulated cannot be rescued by good mathematics later.',
        '**Construction of the model.** The relationships among the variables are expressed '
        'mathematically — an objective function to be maximised or minimised, subject to a set '
        'of constraints. Simplifying assumptions are made deliberately and recorded.',
        '**Deriving a solution.** Data are collected for the parameters and the model is solved, '
        'either analytically by formula, by an iterative algorithm such as the simplex method, '
        'or numerically by simulation where no closed-form solution exists.',
        '**Testing the model and evaluating the solution (validation).** The model is run '
        'against historical data to see whether it reproduces outcomes already known. '
        'Sensitivity analysis establishes how far the recommended solution depends on '
        'parameters that were estimated.',
        '**Establishing controls over the solution.** The parameters whose movement would change '
        'the decision are identified and monitored, so that the model can be revised when '
        'conditions change rather than being applied indefinitely.',
        '**Implementation.** The solution is translated into operating instructions, the staff '
        'who must apply it are trained and their co-operation secured, and performance is '
        'reviewed in operation. Many technically sound studies fail at this stage.',
      ]},
      {'h4': 'Limitations'},
      {'ul': [
        '**Simplifying assumptions.** Models assume linearity, certainty, constant rates and '
        'independence in order to remain solvable. Where those assumptions do not hold, the '
        'solution is optimal for the model but not necessarily for the real system.',
        '**Dependence on data quality.** The output can be no more reliable than the parameters '
        'fed in. Where costs are apportioned estimates or demand is a forecast, a solution '
        'quoted to four significant figures conveys a false impression of precision.',
        '**Cost and time.** Model building, data collection, validation and maintenance require '
        'skilled staff and computing resources. For a small or non-recurring problem the cost '
        'of the study may exceed the value of the improved decision.',
        '**Omission of intangible factors.** Staff morale, industrial relations, customer '
        'goodwill, environmental impact and legal or ethical considerations do not enter a '
        'mathematical objective function, yet may be decisive.',
        '**The communication gap and resistance to change.** Managers who do not understand the '
        'model may distrust its recommendations, and staff whose working practices are altered '
        'may resist implementation.',
      ]},
      {'p': 'These limitations argue for using operations research as an aid to judgement rather '
            'than a substitute for it. The model quantifies what can be quantified; the manager '
            'weighs that result against everything the model necessarily left out.'}],
    'src': 'Chapter 14.1–14.5'},
  ]},
}
