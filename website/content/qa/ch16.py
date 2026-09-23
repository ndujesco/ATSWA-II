CH = {
 'n': 16,
 't': 'Inventory and Production Control',
 'brief': 'The meaning and motives for holding inventory, the four types of inventory cost, and '
          'the derivation and calculation of the Economic Order Quantity (EOQ).',
 'outcomes': [
   'Explain the meaning and functions of inventory',
   'Understand the basic concepts in inventory control',
   'Distinguish between deterministic and stochastic inventory models',
   'Calculate the Economic Order Quantity (EOQ) under various situations',
 ],
 'secs': [
  {'n': '16.1', 't': 'Introduction', 'b': [
    {'p': 'Inventory control — also called **inventory management** — is a process whereby the '
          'stock levels of goods, products or materials in a company are managed and regulated. '
          'Its goal is to balance supply and demand, minimise cost and maximise efficiency.'},
  ]},

  {'n': '16.2', 't': 'The concept of an inventory', 'b': [
    {'p': 'Inventory control is an operations research model that deals with delivering the '
          'right quantity of goods, of the right quality, to the right place, at the right time. '
          'It explains how to identify the order quantity that minimises the relevant costs for '
          'a given annual demand — establishing the concept of **Economic Order Quantity (EOQ)**.'},
    {'p': 'Inventory could mean a list of items in a shop, house or company, or the stock of '
          'items available in an organisation — raw materials, partly finished products or '
          'finished products. Inventory taking also means stock taking.'},
    {'h4': 'Three motives for holding stock'},
    {'ol': [
      '**Transaction motive** — to meet demand at any given time. The quantity demanded is '
      'known with certainty, and replenishment on stock-out is immediate.',
      '**Precautionary motive** — to avoid loss of sales due to uncertainties. Buffer or safety '
      'stocks are held so as not to run out of supply.',
      '**Speculative motive** — in anticipation of a shortage from the supplier, or a price '
      'increase by the supplier; current stock may be increased.',
    ]},
  ]},

  {'n': '16.3', 't': 'Reasons for keeping inventory in a typical company', 'b': [
    {'p': 'Keeping an inventory is the same thing as holding stock. The reasons include:'},
    {'ol': [
      'acting as a buffer for variations in demand and usage;',
      'taking advantage of quantity discounts by buying in bulk;',
      'taking advantage of seasonal and price fluctuations;',
      'keeping to the barest minimum the delay in the production process that lack of raw '
      'materials may cause;',
      'taking advantage of inflation or possible shortages; and',
      'ensuring no stock-outs.',
    ]},
    {'p': 'The main objective of inventory control is to maintain stock levels so as to '
          'minimise total inventory costs. Two main factors must be established — **when to '
          'order** and **what quantity to order**.'},
  ]},

  {'n': '16.4', 't': 'Different types of inventory cost', 'b': [
    {'p': 'Four types of inventory cost are considered:'},
    {'h4': '(a) Holding costs (carrying costs)'},
    {'ul': [
      'cost of capital tied up, including interest on such capital;',
      'handling and storage costs;', 'insurance and security costs;',
      'loss on deterioration and/or obsolescence;',
      'stock taking, auditing and perpetual inventory costs; and',
      'loss due to pilferage and vermin damage.',
    ]},
    {'h4': '(b) Ordering or procuring costs'},
    {'p': 'All costs relating to the placement of orders for stock, whether internal or '
          'external:'},
    {'ul': [
      'administrative costs of the departments placing and receiving orders;',
      'transport costs; and',
      'production set-up costs where goods are manufactured internally — planning, preparing '
      'machinery and the workforce for each production run.',
    ]},
    {'h4': '(c) Shortage or stock-out costs'},
    {'p': 'Where a company runs out of stock it normally incurs a loss, through:'},
    {'ul': [
      'loss of customers;', 'loss of sale and the contribution earned from the sale;',
      'loss on production stoppages; and', 'loss on emergency purchase of stock at a higher '
      'price.',
    ]},
    {'note': 'Of these four, loss of customers and loss of sale are **external**; loss on '
             'production stoppages is **internal**.'},
    {'h4': '(d) Material or stock costs'},
    {'p': 'The supplier\'s price, or the direct cost of production — relevant especially when '
          'bulk-purchase discounts are available, or savings in direct production cost are '
          'possible with longer batch runs.'},
    {'h4': 'Definition of terminologies'},
    {'ul': [
      '**Lead time (procurement time)** — the time, in days/weeks/months, between ordering and '
      'eventual delivery. A lead time of one week means one week elapses between placing the '
      'order and its supply.',
      '**Physical stock** — the number of items physically in stock at the time of inventory.',
      '**Free stock** — physical stock, plus awaiting orders, less unfulfilled demands.',
      '**Maximum stock** — the selected stock level indicating that stocks have risen too high.',
      '**Stock-outs** — a situation where there is demand for an item but the warehouse is out '
      'of stock (e.g. four stock-outs means there is demand for 12 items but only 8 are '
      'available).',
      '**Buffer stock (safety stock / minimum stock)** — the level indicating that stock has '
      'gone too low; held to safeguard against stock-outs.',
      '**Economic Order Quantity (EOQ)** or **Economic Batch Quantity (EBQ)** — the ordering '
      'quantity of an item of stock which minimises the costs involved.',
      '**Re-order quantity** — the number of units of an item in one order.',
      '**Re-order level** — the level of stock at which a new order for more units should be '
      'placed.',
      '**Demand** — the number of units of stock required within a particular period of time.',
    ]},
    {'note': 'Average stock $= Q/2$, where $Q$ is the reorder quantity — illustrated in the '
             'study text by a simple stock diagram in which stock rises to a peak on delivery '
             'and falls in a straight line to the reorder level as it is used up (safety stock '
             'included).'},
  ]},

  {'n': '16.5', 't': 'The Economic Order Quantity (EOQ)', 'b': [
    {'p': 'The basic concept of EOQ involves an optimisation process, normally used in inventory '
          'management, to minimise total inventory cost. This way, inventory costs are '
          'minimised, supply-chain efficiency is improved, and other quantities are optimised.'},
    {'h4': 'Underlying assumptions of the EOQ model'},
    {'ol': [
      'Rates of demand are known;', 'Stock-holding cost is known and constant;',
      'Price per unit is known and constant;', 'No stock-outs are allowed;',
      'Ordering cost is known and constant; and',
      'No part-delivery — the ordered batch is delivered all at once.',
    ]},
    {'p': 'Notation: $d$ = the annual demand; $Q$ = the re-order quantity; $c$ = the ordering '
          'cost for a single order; $h$ = the cost of holding a unit of stock for one year.'},
    {'h4': 'Derivation of the EOQ formula'},
    {'p': 'The total cost per annum is'},
    {'tex': 'T = \\frac{cd}{Q} + \\frac{Qh}{2}'},
    {'p': 'Minimising $T$ with respect to $Q$ (differentiating and setting $dT/dQ=0$ at the '
          'turning point):'},
    {'tex': '\\frac{dT}{dQ} = -\\frac{cd}{Q^2} + \\frac{h}{2} = 0 \\;\\Rightarrow\\; '
            '\\frac{cd}{Q^2} = \\frac{h}{2} \\;\\Rightarrow\\; Q^2h = 2cd \\;\\Rightarrow\\; '
            'Q = \\sqrt{\\frac{2cd}{h}}'},
    {'p': 'Since $Q$ is a function of positive constants ($c,d,h>0$), $d^2T/dQ^2 = 2cd/Q^3 > 0$, '
          'confirming $T$ is a **minimum** at this $Q$.'},
    {'fbox': {'h': 'Derived quantities', 'rows': [
      {'lb': 'Economic order quantity', 'tex': 'Q = \\sqrt{\\dfrac{2cd}{h}}'},
      {'lb': 'Number of orders in a year', 'tex': '\\dfrac{d}{Q}'},
      {'lb': 'Ordering cost in a year', 'tex': 'c \\cdot \\dfrac{d}{Q}'},
      {'lb': 'Average stock', 'tex': '\\dfrac{Q}{2}'},
      {'lb': 'Holding cost per annum', 'tex': 'h \\cdot \\dfrac{Q}{2}'},
      {'lb': 'Length of inventory cycle',
       'tex': '\\dfrac{52Q}{d} \\text{ weeks, or } \\dfrac{12Q}{d} \\text{ months}'},
      {'lb': 'Total cost per annum', 'tex': '\\dfrac{cd}{Q} + \\dfrac{Qh}{2}'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 16.1 — orders, cycle length and total cost',
      'open': True, 'q': [
      {'p': 'The demand for an item is 60,000 per annum. The cost of an order is ₦25 and the '
            'holding cost per item is ₦2 per annum. Find (a) the number of orders per year and '
            'the associated ordering cost, (b) the length of the inventory cycle, (c) the total '
            'cost per annum.'}],
      'a': [
      {'tex': 'Q = \\sqrt{\\frac{2cd}{h}} = \\sqrt{\\frac{2 \\times 25 \\times 60{,}000}{2}} '
              '= \\sqrt{1{,}500{,}000} \\approx 1{,}225 \\text{ items}'},
      {'p': '**(a)** Number of orders per year $= d/Q = 60{,}000/1{,}225 \\approx 49$ orders; '
            'associated ordering cost $= 49 \\times 25 = ₦1{,}225$.'},
      {'p': '**(b)** Length of inventory cycle $= 52/49 \\approx 1.06$ weeks.'},
      {'p': '**(c)** As printed in the study text: total cost per annum '
            '$= (25 \\times 49) + \\dfrac{60{,}000 \\times 2}{2} = 1{,}225 + 60{,}000 = ₦61{,}225$.'},
      {'warn': 'The study text\'s own second term here uses $\\dfrac{dh}{2}$ (annual demand '
               '$\\times$ holding cost $\\div 2$) rather than the derived $\\dfrac{Qh}{2}$ '
               '(average **stock** $\\times$ holding cost) the formula box above defines — '
               'using $Q/2 \\times h \\approx 613 \\times 2 \\approx ₦1{,}225$ instead would give '
               'a total nearer ₦2,450. This looks like a slip in the source\'s own worked '
               'answer. The method (ordering cost $+$ holding cost) is right; verify which term '
               'your own question actually wants before copying the ₦61,225 figure.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 16.2 — EOQ, ordering, holding and total cost',
      'open': True, 'q': [
      {'p': 'A company uses 120,000 units of Material X each year, costing ₦300 per unit. The '
            'cost of placing an order is ₦6,500. The annual holding cost is 10% of the purchase '
            'price of a unit. Determine (i) the EOQ, (ii) annual ordering cost, (iii) annual '
            'holding cost, (iv) total annual cost.'}],
      'a': [
      {'p': 'Here the study text labels the quantities $C_o$ (fixed cost per order), $C_H$ '
            '(holding cost per unit), $D$ (annual demand) — the same formula as before, '
            'relabelled.'},
      {'tex': 'C_H = 10\\% \\times 300 = ₦30 \\qquad Q = \\sqrt{\\frac{2C_oD}{C_H}} '
              '= \\sqrt{\\frac{2 \\times 6{,}500 \\times 120{,}000}{30}} \\approx 7{,}211.1 '
              '\\text{ units}'},
      {'tex': '\\text{(ii) Annual ordering cost} = \\frac{D}{Q} \\times C_o '
              '= \\frac{120{,}000}{7{,}211.1} \\times 6{,}500 \\approx ₦108{,}166'},
      {'tex': '\\text{(iii) Annual holding cost} = \\frac{Q}{2} \\times C_H '
              '\\approx \\frac{7{,}211.1}{2} \\times 30 \\approx ₦108{,}166'},
      {'p': '**(iv)** Total annual cost that is minimised by the EOQ '
            '$= 108{,}166 + 108{,}166 = ₦216{,}332$. Adding the annual purchase price '
            '($120{,}000 \\times 300 = ₦36{,}000{,}000$), the grand total annual cost is '
            '$₦216{,}332 + ₦36{,}000{,}000 = ₦36{,}216{,}332$.'},
      {'key': 'Notice that in both examples the **ordering cost equals the holding cost** at '
              'the EOQ — confirmed directly by the derivation above, since $Q$ was chosen '
              'precisely to make $cd/Q = Qh/2$.'}]}},
  ]},

  {'n': '16.6', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§16.1–16.2 Introduction and concept** — inventory control balances supply and demand '
      'to minimise cost; three motives for holding stock: transaction, precautionary, '
      'speculative.',
      '**§16.3 Reasons for keeping inventory** — buffer for demand variation; quantity '
      'discounts; seasonal/price fluctuations; avoiding production delay; hedging inflation/'
      'shortages; avoiding stock-outs.',
      '**§16.4 Types of cost** — holding (carrying), ordering (procuring), shortage '
      '(stock-out), and material/stock costs — plus the full glossary of terms (lead time, '
      'physical/free/maximum stock, stock-outs, buffer stock, EOQ/EBQ, reorder quantity/level, '
      'demand).',
      '**§16.5 EOQ** — derived by calculus from $T=cd/Q+Qh/2$, giving $Q=\\sqrt{2cd/h}$; at '
      'this $Q$, ordering cost always equals holding cost. Six assumptions: known demand, '
      'known/constant holding cost, known/constant unit price, no stock-outs, known/constant '
      'ordering cost, no part-delivery.',
    ]},
    {'h3': 'Notation'},
    {'p': '$d$ = annual demand; $Q$ = re-order quantity; $c$ = ordering cost per order; $h$ = '
          'holding cost per unit per year (some worked examples relabel these $D$, $Q$, '
          '$C_o$, $C_H$ — same formula).'},
  ]},
 ],
 'formulas': [
  {'lb': 'Economic order quantity', 'tex': 'Q = \\sqrt{\\frac{2cd}{h}}'},
  {'lb': 'Number of orders per annum', 'tex': '\\frac{d}{Q}'},
  {'lb': 'Ordering cost per annum', 'tex': 'c \\cdot \\frac{d}{Q}'},
  {'lb': 'Average stock', 'tex': '\\frac{Q}{2}'},
  {'lb': 'Holding cost per annum', 'tex': 'h \\cdot \\frac{Q}{2}'},
  {'lb': 'Total cost per annum', 'tex': '\\frac{cd}{Q} + \\frac{Qh}{2}'},
  {'lb': 'Length of inventory cycle (weeks)', 'tex': '\\frac{52Q}{d}'},
 ],
 'focus':
   'A dependable Section A/B source: derive or quote the EOQ formula, compute the number of '
   'orders, the ordering/holding cost and the total annual cost. The examiner sometimes swaps '
   'notation between examples ($c,d,h$ vs $C_o, D, C_H$) — read which letter means what before '
   'substituting.',
 'errors': [
   'Forgetting the square root, or the 2 in the numerator.',
   'Using $Q$ instead of $Q/2$ for average stock and holding cost.',
   'Mixing time periods — annual demand with a cost stated for a different period.',
   'Not checking that ordering cost equals holding cost at the computed EOQ.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Annual demand is 3,600 units, the cost of an order is ₦16 and holding cost per unit '
         'is ₦2 per annum. The number of orders per year is',
    'o': ['240', '15', '225', '220', '25'],
    'a': 1,
    'w': 'Find $Q$ first, then divide demand by $Q$.',
    'calc': 'Q = \\sqrt{\\frac{2(16)(3{,}600)}{2}} = \\sqrt{57{,}600} = 240 \\Rightarrow '
            '\\frac{3{,}600}{240} = 15',
    'src': 'Chapter 16.5', 'sec': '16.5'},
   {'q': 'At the Economic Order Quantity,', 'o': ['ordering cost is minimised',
          'ordering cost equals holding cost', 'holding cost is minimised',
          'purchase cost is minimised', 'the number of orders is minimised'],
    'a': 1,
    'w': 'The EOQ is derived precisely by setting the marginal ordering cost equal to the '
         'marginal holding cost.',
    'src': 'Chapter 16.5', 'sec': '16.5'},
   {'q': 'Which of these is NOT a reason for holding stock, per the study text?',
    'o': ['To take advantage of quantity discount', 'To act as a buffer for demand variation',
          'To ensure the store is filled up at all times', 'To take advantage of inflation',
          'To ensure no stock-outs'],
    'a': 2,
    'w': 'Keeping the store "filled up at all times" is not one of the six listed reasons — '
         'stock is held for specific, costed reasons, not for its own sake.',
    'src': 'Chapter 16.3', 'sec': '16.3'},
   {'q': 'Given annual demand 50,000, reorder quantity 2,000, ordering cost ₦20 per order and '
         'holding cost ₦2 per item per annum, the total cost per annum is',
    'o': ['₦2,500', '₦4,000', '₦500', '₦2,000', '₦52,000'],
    'a': 0,
    'w': 'Total cost $= (d/Q)c + (Q/2)h$.',
    'calc': '\\frac{50{,}000}{2{,}000}(20) + \\frac{2{,}000}{2}(2) = 500 + 2{,}000 = ₦2{,}500',
    'src': 'Chapter 16.5', 'sec': '16.5'},
   {'q': 'A stock-out is a situation where', 'o': ['no item is ever stocked',
          'the store deliberately holds zero stock', 'there is demand for an item but it is '
          'not in store', 'a customer cancels an order', 'stock is being counted'],
    'a': 2,
    'w': 'A stock-out means demand exists but the warehouse cannot meet it.',
    'src': 'Chapter 16.4', 'sec': '16.4'},
  ],
  'theory': [
   {'q': 'Explain the three motives for holding stock, and state the four types of inventory '
         'cost with two examples of each.',
    'marks': 10,
    'a': [
      {'h4': 'The three motives'},
      {'ol': [
        '**Transaction motive** — demand is known with certainty and replenishment on '
        'stock-out is immediate.',
        '**Precautionary motive** — buffer/safety stock held to avoid lost sales from '
        'uncertainty.',
        '**Speculative motive** — stock increased in anticipation of a supply shortage or a '
        'price rise.',
      ]},
      {'h4': 'The four types of inventory cost'},
      {'table': {'head': ['Cost', 'Examples'], 'align': 'll', 'rows': [
        ['Holding (carrying)', 'Interest on capital tied up; insurance and security costs'],
        ['Ordering (procuring)', 'Administrative cost of placing orders; transport costs'],
        ['Shortage (stock-out)', 'Loss of customers; loss on emergency purchase at a higher '
         'price'],
        ['Material / stock cost', "The supplier's price, or the direct cost of production"],
      ]}}],
    'src': 'Chapter 16.2, 16.4', 'sec': '16.4'},
  ]},
}
