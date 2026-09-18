CH = {
 'n': 16,
 't': 'Inventory and Production Control',
 'brief': 'The costs of holding inventory, the economic order quantity and its assumptions, '
          'the economic batch quantity, reorder levels and buffer stock, and the evaluation of '
          'quantity discounts.',
 'outcomes': [
   'Identify the costs relevant to an inventory decision',
   'Derive and apply the economic order quantity',
   'Compute total inventory cost at any order size',
   'Apply the economic batch quantity where replenishment is gradual',
   'Compute reorder level, buffer stock and maximum and minimum levels',
   'Evaluate whether a quantity discount should be accepted',
 ],
 'secs': [
  {'n': '16.1', 't': 'The costs of inventory', 'b': [
    {'table': {'align': 'lll', 'head': ['Cost', 'Behaviour', 'Examples'], 'rows': [
      ['**Ordering (set-up) cost**', 'Fixed per order; total rises with the number of orders',
       'Requisitioning, placing the order, transport, receiving and inspection; machine set-up '
       'for a production batch'],
      ['**Holding (carrying) cost**', 'Per unit per period; total rises with order size',
       'Interest on capital tied up, storage, insurance, obsolescence, deterioration, pilferage'],
      ['**Purchase (acquisition) cost**', 'Per unit; constant unless discounts apply',
       'Invoice price of the goods'],
      ['**Stockout (shortage) cost**', 'Arises when demand cannot be met',
       'Lost contribution, emergency purchases, idle time, loss of customer goodwill'],
    ]}},
    {'key': 'Ordering cost and holding cost move in **opposite** directions as the order size '
            'changes: large orders mean few orders (low ordering cost) but high average '
            'inventory (high holding cost). The economic order quantity is the size at which '
            'their total is least — which, for the basic model, is exactly where the two are '
            'equal.'},
    {'p': 'Purchase cost is normally irrelevant to the *size* of the order, because the same '
          'annual quantity is bought whatever the order size. It becomes relevant only when a '
          'quantity discount changes the unit price.'},
  ]},

  {'n': '16.2', 't': 'The economic order quantity', 'b': [
    {'fbox': {'h': 'EOQ and related quantities', 'rows': [
      {'lb': 'Economic order quantity',
       'tex': 'Q^{*} = \\sqrt{\\frac{2 D C_o}{C_h}}'},
      {'lb': 'Number of orders per year',
       'tex': 'N = \\frac{D}{Q}'},
      {'lb': 'Annual ordering cost',
       'tex': '\\frac{D}{Q} \\times C_o'},
      {'lb': 'Annual holding cost',
       'tex': '\\frac{Q}{2} \\times C_h'},
      {'lb': 'Total relevant cost',
       'tex': 'TC = \\frac{D}{Q}C_o + \\frac{Q}{2}C_h'},
      {'lb': 'Minimum total cost',
       'tex': 'TC^{*} = \\sqrt{2 D C_o C_h}'},
      {'lb': 'Length of the order cycle',
       'tex': '\\frac{Q^{*}}{D} \\times 365 \\text{ days}'},
    ]}},
    {'p': 'where $D$ is annual demand in units, $C_o$ the cost of placing one order, and $C_h$ '
          'the cost of holding one unit for one year. Average inventory is $Q/2$ because stock '
          'falls evenly from $Q$ at delivery to zero just before the next.'},
    {'h4': 'Assumptions of the basic model'},
    {'ul': [
      'Demand is known, constant and continuous throughout the year.',
      'The lead time is known and constant.',
      'Replenishment is instantaneous — the whole order arrives at once.',
      'The unit purchase price is constant; no quantity discounts.',
      'Ordering cost per order and holding cost per unit per year are constant.',
      'No stockouts are permitted, so no shortage cost enters the model.',
    ]},
    {'eg': {'t': 'Computing the EOQ', 'q': [
      {'p': 'Bello Trading Company uses 10,000 units of a component each year. The cost of '
            'placing an order is ₦400 and the cost of holding one unit for a year is ₦8. '
            'Compute (a) the economic order quantity; (b) the number of orders per year; '
            '(c) the total annual inventory cost; (d) the length of the order cycle, assuming '
            'a 250-day working year.'}],
      'a': [
      {'p': '**(a)**'},
      {'tex': 'Q^{*} = \\sqrt{\\frac{2DC_o}{C_h}} = \\sqrt{\\frac{2 \\times 10{,}000 '
              '\\times 400}{8}} = \\sqrt{\\frac{8{,}000{,}000}{8}} = \\sqrt{1{,}000{,}000} '
              '= 1{,}000 \\text{ units}'},
      {'p': '**(b)**'},
      {'tex': 'N = \\frac{D}{Q^{*}} = \\frac{10{,}000}{1{,}000} = 10 \\text{ orders per year}'},
      {'p': '**(c)**'},
      {'table': {'align': 'lr', 'head': ['Cost', 'Amount (₦)'], 'rows': [
        ['Ordering: $(10{,}000 \\div 1{,}000) \\times 400$', '4,000'],
        ['Holding: $(1{,}000 \\div 2) \\times 8$', '4,000'],
        ['Total relevant cost', '8,000'],
      ]}},
      {'p': 'Confirming with the direct formula:'},
      {'tex': 'TC^{*} = \\sqrt{2DC_oC_h} = \\sqrt{2(10{,}000)(400)(8)} '
              '= \\sqrt{64{,}000{,}000} = ₦8{,}000'},
      {'p': '**(d)**'},
      {'tex': '\\text{Cycle} = \\frac{1{,}000}{10{,}000} \\times 250 = 25 \\text{ working days}'},
      {'key': 'Notice that ordering cost and holding cost are both ₦4,000. **At the EOQ the two '
              'are always equal** — a one-second check on any EOQ answer. If they differ, the '
              'quantity is not the EOQ.'}]}},
    {'eg': {'t': 'Cost of departing from the EOQ', 'q': [
      {'p': 'Using the data above, compute the total inventory cost if the company instead '
            'ordered 2,000 units at a time, and comment.'}],
      'a': [
      {'tex': 'TC = \\frac{10{,}000}{2{,}000}(400) + \\frac{2{,}000}{2}(8) = 2{,}000 + 8{,}000 '
              '= ₦10{,}000'},
      {'p': 'The cost is ₦2,000 (25%) higher than the optimum. Note, however, that doubling the '
            'order quantity raised total cost by only a quarter: the total-cost curve is '
            '**flat near the optimum**, so a moderate departure from the EOQ — to a round '
            'pallet quantity, say — costs little. This is one of the model\'s more useful '
            'practical properties.'}]}},
  ]},

  {'n': '16.3', 't': 'Gradual replenishment: the economic batch quantity', 'b': [
    {'p': 'Where the items are manufactured rather than bought in, they arrive gradually at the '
          'production rate $p$ while being consumed at the demand rate $d$. Stock therefore '
          'builds up at $(p - d)$ and never reaches the full batch size, so average inventory '
          'is lower and larger batches become economic.'},
    {'fbox': {'h': 'Economic batch quantity', 'rows': [
      {'lb': 'Batch size',
       'tex': 'Q^{*} = \\sqrt{\\frac{2 D C_s}{C_h\\left(1 - \\dfrac{d}{p}\\right)}}'},
      {'lb': 'Maximum inventory',
       'tex': 'Q\\left(1 - \\frac{d}{p}\\right)'},
      {'lb': 'Average inventory',
       'tex': '\\frac{Q}{2}\\left(1 - \\frac{d}{p}\\right)'},
    ]}},
    {'eg': {'t': 'Economic batch quantity', 'q': [
      {'p': 'A component is used at 4,000 units a year and can be produced at 20,000 units a '
            'year. Set-up cost per batch is ₦1,000 and holding cost ₦4 per unit per year. '
            'Compute the economic batch quantity and the maximum inventory level.'}],
      'a': [
      {'tex': '1 - \\frac{d}{p} = 1 - \\frac{4{,}000}{20{,}000} = 1 - 0.2 = 0.8'},
      {'tex': 'Q^{*} = \\sqrt{\\frac{2(4{,}000)(1{,}000)}{4 \\times 0.8}} '
              '= \\sqrt{\\frac{8{,}000{,}000}{3.2}} = \\sqrt{2{,}500{,}000} = 1{,}581 '
              '\\text{ units}'},
      {'tex': '\\text{Maximum inventory} = 1{,}581 \\times 0.8 = 1{,}265 \\text{ units}'},
      {'note': 'Without the gradual-replenishment adjustment the EOQ would be '
               '$\\sqrt{2(4{,}000)(1{,}000)/4} = 1{,}414$ units. Gradual delivery lowers the '
               'effective holding cost, so the economic batch is larger.'}]}},
  ]},

  {'n': '16.4', 't': 'Control levels', 'b': [
    {'fbox': {'h': 'Stock control levels', 'rows': [
      {'lb': 'Reorder level',
       'tex': '\\text{Max usage} \\times \\text{Max lead time}'},
      {'lb': 'Reorder level (with buffer stock)',
       'tex': '(\\text{Average usage} \\times \\text{Lead time}) + \\text{Buffer stock}'},
      {'lb': 'Minimum (buffer) level',
       'tex': '\\text{ROL} - (\\text{Average usage} \\times \\text{Average lead time})'},
      {'lb': 'Maximum level',
       'tex': '\\text{ROL} + Q^{*} - (\\text{Min usage} \\times \\text{Min lead time})'},
      {'lb': 'Average inventory',
       'tex': '\\text{Buffer stock} + \\frac{Q^{*}}{2}'},
    ]}},
    {'eg': {'t': 'Setting the control levels', 'q': [
      {'p': 'Continuing the Bello example ($D = 10{,}000$, $Q^{*} = 1{,}000$, 250-day year), '
            'usage varies between 30 and 50 units a day and the lead time between 4 and 6 days. '
            'Compute the reorder level, the minimum level and the maximum level.'}],
      'a': [
      {'p': 'Average daily usage is $10{,}000 \\div 250 = 40$ units; average lead time is 5 '
            'days.'},
      {'tex': '\\text{Reorder level} = 50 \\times 6 = 300 \\text{ units}'},
      {'tex': '\\text{Minimum level} = 300 - (40 \\times 5) = 300 - 200 = 100 \\text{ units}'},
      {'tex': '\\text{Maximum level} = 300 + 1{,}000 - (30 \\times 4) = 1{,}300 - 120 '
              '= 1{,}180 \\text{ units}'},
      {'p': 'The **buffer (safety) stock** of 100 units is the cushion against usage or lead '
            'time running above average. Average inventory is therefore $100 + 1{,}000/2 = 600$ '
            'units rather than 500, and annual holding cost $600 \\times 8 = ₦4{,}800$ rather '
            'than ₦4,000. The extra ₦800 is the price of the protection.'}]}},
  ]},

  {'n': '16.5', 't': 'Quantity discounts', 'b': [
    {'p': 'A discount makes purchase price relevant, so the EOQ formula alone no longer '
          'answers the question. The method is to compute the **total annual cost including '
          'purchases** at the EOQ and at each discount threshold, and choose the lowest.'},
    {'steps': [
      'Compute the EOQ ignoring discounts, and the total cost at that quantity including '
      'purchase cost.',
      'For each discount level, take the **smallest order quantity that earns the discount**, '
      'unless the EOQ already exceeds it.',
      'Compute the total annual cost at each of those quantities: purchases + ordering + '
      'holding.',
      'Select the order quantity with the lowest total.',
    ]},
    {'eg': {'t': 'Evaluating a discount', 'q': [
      {'p': 'Bello Trading (D = 10,000 units, $C_o$ = ₦400, $C_h$ = ₦8, EOQ = 1,000) currently '
            'pays ₦100 per unit. The supplier now offers a 2% discount on orders of 2,000 units '
            'or more. Should the offer be accepted?'}],
      'a': [
      {'table': {'align': 'lrr',
        'head': ['', 'Order 1,000 (EOQ)', 'Order 2,000 (discount)'], 'rows': [
        ['Unit price (₦)', '100.00', '98.00'],
        ['Purchases: $10{,}000 \\times$ price', '1,000,000', '980,000'],
        ['Ordering: $(10{,}000 \\div Q) \\times 400$', '4,000', '2,000'],
        ['Holding: $(Q \\div 2) \\times 8$', '4,000', '8,000'],
        ['**Total annual cost (₦)**', '**1,008,000**', '**990,000**'],
      ]}},
      {'p': 'Ordering 2,000 units at a time saves **₦18,000 a year**, so the discount should be '
            '**accepted**. The saving on purchases (₦20,000) and on ordering (₦2,000) more than '
            'covers the additional ₦4,000 of holding cost.'},
      {'warn': 'Two refinements are often required. First, if holding cost is stated as a '
               '**percentage of purchase price** rather than a fixed naira amount, it falls '
               'with the discount and must be recomputed at the lower price. Second, the '
               'financial saving should be weighed against the non-financial consequences of '
               'holding twice the stock: more storage space, greater exposure to obsolescence '
               'and deterioration, and more capital tied up.'}]}},
  ]},

  {'n': '16.6', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§16.1 The costs of inventory** — ordering/set-up cost (fixed per order, total rises '
      'with the *number* of orders); holding/carrying cost (per unit per period, total rises '
      'with order *size*); purchase cost (irrelevant to order size unless discounts apply); '
      'stockout cost (lost contribution, emergency buys, goodwill). Ordering and holding cost '
      'move in **opposite** directions as order size changes — EOQ minimises their total.',
      '**§16.2 The economic order quantity** — $Q^*=\\sqrt{2DC_o/C_h}$; average inventory '
      '$=Q/2$; $TC=(D/Q)C_o+(Q/2)C_h$; minimum total cost '
      '$TC^*=\\sqrt{2DC_oC_h}$. **At the EOQ, ordering cost always equals holding cost** — the '
      'one-second check on any EOQ answer. Assumptions: known constant demand and lead time, '
      'instantaneous replenishment, constant unit price (no discounts), no stockouts allowed. '
      'The total-cost curve is **flat near the optimum**, so a moderate departure from the '
      'exact EOQ (e.g. to a round pallet size) costs relatively little.',
      '**§16.3 Gradual replenishment (economic batch quantity)** — used when items are '
      '**produced**, not bought, so they arrive at production rate $p$ while being consumed at '
      'demand rate $d$; $Q^*=\\sqrt{2DC_s/(C_h(1-d/p))}$, maximum inventory '
      '$=Q(1-d/p)$, average $=\\,(Q/2)(1-d/p)$. Gradual delivery lowers effective holding '
      'cost, so the economic batch is **larger** than the plain EOQ would be for the same data.',
      '**§16.4 Control levels** — reorder level $=$ max usage $\\times$ max lead time (or '
      'average usage $\\times$ lead time $+$ buffer stock); minimum/buffer level $=$ ROL $-$ '
      '(average usage $\\times$ average lead time); maximum level $=$ ROL $+Q^*-$ (min usage '
      '$\\times$ min lead time); average inventory $=$ buffer stock $+Q^*/2$. Buffer stock is '
      'the cushion against usage or lead time running above average, and it raises average '
      'inventory (and so holding cost) above the plain $Q^*/2$ figure.',
      '**§16.5 Quantity discounts** — a discount makes purchase price relevant, so compare '
      '**total annual cost including purchases** (purchases $+$ ordering $+$ holding) at the '
      'EOQ and at the smallest order quantity earning each discount threshold, and pick the '
      'lowest overall — never rely on the EOQ formula alone once a discount is offered.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Inventory / stock** — goods held for production or sale.',
      '**Motives for holding stock** — *transaction* (meet expected demand), *precautionary* '
      '(buffer against variation in demand or lead time), *speculative* (expected price rise).',
      '**Holding (carrying) cost $C_h$** — cost of keeping one unit in stock for one year: '
      'storage, insurance, obsolescence, deterioration, capital tied up.',
      '**Ordering (procurement / set-up) cost $C_o$** — cost of placing one order (or one '
      'production set-up), independent of order size.',
      '**Stock-out (shortage) cost** — cost of running out: lost sales, idle production, '
      'goodwill.',
      '**Purchase cost** — price $\\times$ annual demand; relevant only when it varies '
      '(quantity discounts).',
      '**Annual demand / usage $D$**.',
      '**Lead time** — the delay between placing an order and receiving it.',
      '**Economic order quantity (EOQ) $Q^{*}$** — the order size that minimises total annual '
      'ordering + holding cost.',
      '**Economic batch quantity (EBQ)** — the EOQ analogue when stock is replenished '
      'gradually at production rate $p$ while being used at rate $d$.',
      '**Buffer (safety) stock $B$** — stock held to cover demand above average during the '
      'lead time.',
      '**Reorder level (ROL)** — the stock level that triggers a new order.',
      '**Maximum / minimum stock level** — control limits used to flag over- and '
      'under-stocking.',
    ]},
    {'h3': 'EOQ model assumptions'},
    {'ul': [
      'demand is known and constant; holding cost per unit is known and constant; ordering '
      'cost per order is known and constant; no stock-outs allowed; the whole order is '
      'delivered at once (no part-delivery); no quantity discounts (basic model).',
    ]},
    {'h3': 'A. EOQ and total cost'},
    {'fbox': {'h': 'EOQ', 'rows': [
      {'lb': 'Total relevant annual cost',
       'tex': 'TC = \\underbrace{\\dfrac{D}{Q}\\,C_o}_{\\text{ordering}} + '
              '\\underbrace{\\dfrac{Q}{2}\\,C_h}_{\\text{holding}}'},
      {'lb': 'EOQ (minimises TC)',
       'tex': 'Q^{*} = \\sqrt{\\dfrac{2 D C_o}{C_h}}'},
      {'lb': 'Minimum total cost',
       'tex': 'TC^{*} = \\sqrt{2 D C_o C_h} \\quad (\\text{ordering cost} = \\text{holding '
              'cost at } Q^{*})'},
      {'lb': 'Number of orders per year', 'tex': 'N = \\dfrac{D}{Q^{*}}'},
      {'lb': 'Time between orders (cycle length)',
       'tex': 't = \\dfrac{Q^{*}}{D} \\ (\\text{years})'},
    ]}},
    {'h3': 'B. Economic batch quantity (gradual replenishment)'},
    {'tex': 'Q^{*} = \\sqrt{\\dfrac{2 D C_s}{C_h\\left(1 - \\dfrac{d}{p}\\right)}} '
            '\\qquad (C_s = \\text{set-up cost}, \\ d = \\text{usage rate}, \\ '
            'p = \\text{production rate})'},
    {'h3': 'C. Control levels'},
    {'fbox': {'h': 'Stock control levels', 'rows': [
      {'lb': 'Reorder level',
       'tex': '\\text{ROL} = \\text{Max usage} \\times \\text{Max lead time}'},
      {'lb': 'Minimum (buffer) level',
       'tex': '\\text{Min level} = \\text{ROL} - (\\text{Avg usage} \\times \\text{Avg lead '
              'time})'},
      {'lb': 'Maximum level',
       'tex': '\\text{Max level} = \\text{ROL} + Q^{*} - (\\text{Min usage} \\times '
              '\\text{Min lead time})'},
      {'lb': 'Reorder quantity', 'tex': 'Q^{*} \\text{ (the EOQ)}'},
      {'lb': 'Average stock (with buffer)',
       'tex': '\\bar{S} = B + \\dfrac{Q^{*}}{2}'},
    ]}},
    {'h3': 'D. Quantity discounts'},
    {'ol': [
      'Compute $TC$ at the EOQ (at the normal price): ordering + holding + purchase cost '
      '$= \\dfrac{D}{Q^{*}}C_o + \\dfrac{Q^{*}}{2}C_h + PD$.',
      'For each discount price, compute $TC$ at the **minimum quantity** that earns that '
      'discount (holding cost uses the discounted unit cost).',
      'Accept the discount only if its total cost (including the lower purchase cost) is less.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': 'Economic order quantity',
   'tex': 'Q^{*} = \\sqrt{\\frac{2DC_o}{C_h}}'},
  {'lb': 'Total relevant cost',
   'tex': 'TC = \\frac{D}{Q}C_o + \\frac{Q}{2}C_h'},
  {'lb': 'Minimum total cost', 'tex': 'TC^{*} = \\sqrt{2DC_oC_h}'},
  {'lb': 'Economic batch quantity',
   'tex': 'Q^{*} = \\sqrt{\\frac{2DC_s}{C_h(1 - d/p)}}'},
  {'lb': 'Reorder level',
   'tex': '\\text{Max usage} \\times \\text{Max lead time}'},
  {'lb': 'Minimum level',
   'tex': '\\text{ROL} - (\\text{Avg usage} \\times \\text{Avg lead time})'},
  {'lb': 'Maximum level',
   'tex': '\\text{ROL} + Q^{*} - (\\text{Min usage} \\times \\text{Min lead time})'},
  {'lb': 'Average inventory with buffer',
   'tex': 'B + \\frac{Q^{*}}{2}'},
 ],
 'focus':
   'One or two Section A marks on the EOQ formula or a reorder level, and a Section B question '
   'in perhaps half the diets, usually EOQ plus a discount evaluation plus a discussion of the '
   'assumptions. The formula itself is given credit only once; the marks are in the total-cost '
   'table and the assumptions, so never stop at the square root.',
 'errors': [
   'Using $Q$ rather than $Q/2$ for average inventory.',
   'Forgetting to square-root, or omitting the 2 in the numerator.',
   'Mixing time periods — annual demand with a monthly holding cost.',
   'Including purchase cost in the basic EOQ computation, where it is irrelevant.',
   'Excluding purchase cost from a discount evaluation, where it is the whole point.',
   'Using the EOQ quantity rather than the discount threshold when testing a discount level.',
   'Forgetting to add buffer stock to average inventory when computing holding cost.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Annual demand is 8,000 units, ordering cost ₦250 per order and holding cost ₦4 per '
         'unit per year. The economic order quantity is',
    'o': ['500 units', '1,000 units', '2,000 units', '1,414 units', '600 units'],
    'a': 1,
    'w': 'Substitute directly into the EOQ formula.',
    'calc': 'Q^{*} = \\sqrt{\\frac{2(8{,}000)(250)}{4}} = \\sqrt{1{,}000{,}000} = 1{,}000',
    'src': 'Chapter 16.2', 'sec': '16.2'},
   {'q': 'At the economic order quantity,',
    'o': ['ordering cost is minimised', 'ordering cost equals holding cost',
          'holding cost is minimised', 'purchase cost is minimised',
          'the number of orders is minimised'],
    'a': 1,
    'w': 'The two costs move in opposite directions; their sum is least where they are equal.',
    'src': 'Chapter 16.2', 'sec': '16.2'},
   {'q': 'Maximum usage is 60 units a day and the maximum lead time 8 days. The reorder level '
         'is',
    'o': ['68 units', '480 units', '420 units', '240 units', '52 units'],
    'a': 1,
    'w': 'The reorder level must cover the worst case: highest usage over the longest lead '
         'time.',
    'calc': '\\text{ROL} = 60 \\times 8 = 480 \\text{ units}',
    'src': 'Chapter 16.4', 'sec': '16.4'},
   {'q': 'Which of the following is NOT an assumption of the basic EOQ model?',
    'o': ['Demand is constant and known', 'Lead time is constant',
          'Quantity discounts are available', 'Replenishment is instantaneous',
          'Holding cost per unit is constant'],
    'a': 2,
    'w': 'The basic model assumes a constant unit price. Discounts require the extended '
         'analysis of total cost including purchases.',
    'src': 'Chapter 16.2', 'sec': '16.2'},
   {'q': 'If annual demand doubles, all other costs remaining unchanged, the economic order '
         'quantity',
    'o': ['doubles', 'increases by about 41%', 'halves', 'is unchanged',
          'increases by 100 units'],
    'a': 1,
    'w': 'Demand is under a square root, so the EOQ rises by $\\sqrt{2} = 1.414$ — an increase '
         'of about 41%, not 100%.',
    'src': 'Chapter 16.2', 'sec': '16.2'},
   {'q': 'A firm orders 400 units at a time against annual demand of 4,800 units, with '
         'ordering cost ₦150 and holding cost ₦5 per unit per year. Its total relevant cost is',
    'o': ['₦1,800', '₦2,800', '₦2,000', '₦3,800', '₦1,000'],
    'a': 1,
    'w': 'Add the ordering cost for 12 orders to the holding cost on average inventory of 200 '
         'units.',
    'calc': 'TC = \\frac{4{,}800}{400}(150) + \\frac{400}{2}(5) = 1{,}800 + 1{,}000 = ₦2{,}800',
    'src': 'Chapter 16.2', 'sec': '16.2'},
  ],
  'theory': [
   {'q': 'Ogunsanya Nigeria Limited uses 24,000 units of a raw material each year. The cost of '
         'placing and processing an order is ₦750 and the cost of holding one unit in store for '
         'a year is ₦20. The material costs ₦150 per unit. The supplier has offered a discount '
         'of 3% on orders of 3,000 units or more. (a) Compute the economic order quantity and '
         'the total relevant cost at that quantity. (b) Advise whether the discount should be '
         'accepted, supporting your advice with computations. (c) State four assumptions of the '
         'EOQ model and comment on their realism.',
    'marks': 15,
    'a': [
      {'h4': '(a) Economic order quantity'},
      {'tex': 'Q^{*} = \\sqrt{\\frac{2DC_o}{C_h}} = \\sqrt{\\frac{2 \\times 24{,}000 '
              '\\times 750}{20}} = \\sqrt{\\frac{36{,}000{,}000}{20}} = \\sqrt{1{,}800{,}000}'},
      {'tex': 'Q^{*} = 1{,}341.64 \\approx 1{,}342 \\text{ units}'},
      {'p': 'Total relevant cost at the EOQ:'},
      {'table': {'align': 'lr', 'head': ['Cost', 'Amount (₦)'], 'rows': [
        ['Ordering: $(24{,}000 \\div 1{,}342) \\times 750$', '13,413'],
        ['Holding: $(1{,}342 \\div 2) \\times 20$', '13,420'],
        ['Total relevant cost', '26,833'],
      ]}},
      {'p': 'Or directly, $TC^{*} = \\sqrt{2DC_oC_h} = \\sqrt{2(24{,}000)(750)(20)} '
            '= \\sqrt{720{,}000{,}000} = ₦26{,}833$. The two cost elements are almost equal, '
            'as they must be at the EOQ; the small difference is rounding to a whole number of '
            'units.'},
      {'h4': '(b) Evaluation of the discount'},
      {'p': 'The discount makes purchase cost relevant, so the comparison must be of **total '
            'annual cost including purchases**. The discounted price is '
            '$150 \\times 0.97 = ₦145.50$. The relevant order quantity for the discount is the '
            'threshold of 3,000 units, since ordering more than the minimum needed would only '
            'add holding cost.'},
      {'table': {'align': 'lrr',
        'head': ['', 'Order 1,342 (EOQ)', 'Order 3,000 (discount)'], 'rows': [
        ['Unit price (₦)', '150.00', '145.50'],
        ['Purchases: $24{,}000 \\times$ price', '3,600,000', '3,492,000'],
        ['Ordering: $(24{,}000 \\div Q) \\times 750$', '13,413', '6,000'],
        ['Holding: $(Q \\div 2) \\times 20$', '13,420', '30,000'],
        ['**Total annual cost (₦)**', '**3,626,833**', '**3,528,000**'],
      ]}},
      {'p': 'Ordering 3,000 units at a time reduces total annual cost by '
            '$3{,}626{,}833 - 3{,}528{,}000 = ₦98{,}833$. The **discount should be accepted**.'},
      {'p': 'The reason is clear from the components: the saving on purchases is ₦108,000 and '
            'on ordering ₦7,413, a total of ₦115,413, against additional holding cost of only '
            '₦16,580. Where the purchase price is large relative to the holding cost — as here, '
            '₦150 against ₦20 — even a small percentage discount will usually outweigh the '
            'extra carrying cost.'},
      {'p': 'Two qualifications should accompany the advice. If the holding cost of ₦20 is in '
            'substance a percentage of the purchase price, it would fall to about ₦19.40 at the '
            'discounted price, making the case marginally stronger still. Against that, average '
            'inventory rises from 671 to 1,500 units, which requires storage space and '
            'increases exposure to obsolescence, deterioration and pilferage — factors the model '
            'does not price.'},
      {'h4': '(c) Assumptions and their realism'},
      {'ol': [
        '**Demand is known, constant and even throughout the year.** Rarely true. Most demand '
        'is seasonal or uncertain, which is precisely why buffer stock is held — a quantity the '
        'basic model does not contemplate at all.',
        '**Lead time is known and constant.** Suppliers are late, especially where imports and '
        'clearing are involved. Variable lead time is the second reason for buffer stock.',
        '**Replenishment is instantaneous.** Reasonable for bought-in goods delivered in one '
        'consignment, but false for manufactured items, where the economic batch quantity '
        'model with its $(1 - d/p)$ adjustment is required.',
        '**Costs are constant and known.** Ordering cost per order and holding cost per unit '
        'are treated as fixed, but in practice much of the ordering cost is a share of '
        'departmental salaries that would not change with one more order, and holding cost '
        'depends on an interest rate and a valuation of storage space that are both estimates.',
        '**No stockouts occur and no quantity discounts are available.** Both are relaxed in '
        'extended versions of the model, as part (b) illustrates for discounts.',
      ]},
      {'p': 'Despite these assumptions the model remains useful, for two reasons. Its total-cost '
            'curve is very flat near the optimum, so an order quantity rounded to a practical '
            'figure costs little extra; and the discipline of identifying ordering and holding '
            'costs separately often improves inventory management more than the resulting '
            'number does.'}],
    'src': 'Chapter 16.2, 16.5', 'sec': '16.2'},
  ]},
}
