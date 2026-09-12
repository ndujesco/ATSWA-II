CH = {
 'n': 9,
 't': 'Profit or Loss Based on Cost or Selling Price',
 'brief': 'Mark-up and margin and the conversion between them, trade and cash discounts, '
          'commission, and the use of a margin to reconstruct cost of sales.',
 'outcomes': [
   'Distinguish mark-up (on cost) from margin (on selling price)',
   'Convert a mark-up to a margin and back',
   'Compute selling price, cost and profit from any one of them plus a percentage',
   'Apply trade and cash discounts in the right order',
   'Use a gross profit percentage to reconstruct cost of sales or closing inventory',
 ],
 'secs': [
  {'n': '9.1', 't': 'Mark-up and margin', 'b': [
    {'p': 'Both express the same profit as a percentage, but of different bases. Getting the '
          'base wrong is the single largest source of lost marks in this chapter and in the '
          'inventory questions of Financial Accounting.'},
    {'def': {'t': 'Mark-up',
             'd': 'Gross profit as a percentage of **cost**. A 25% mark-up on a cost of ₦100 '
                  'gives a profit of ₦25 and a selling price of ₦125.'}},
    {'def': {'t': 'Margin',
             'd': 'Gross profit as a percentage of **selling price**. A 25% margin on a selling '
                  'price of ₦100 gives a profit of ₦25 and a cost of ₦75.'}},
    {'fbox': {'h': 'The relationships', 'rows': [
      {'lb': 'Mark-up', 'tex': 'm = \\frac{\\text{Gross profit}}{\\text{Cost}} \\times 100'},
      {'lb': 'Margin', 'tex': 'g = \\frac{\\text{Gross profit}}{\\text{Sales}} \\times 100'},
      {'lb': 'Mark-up to margin', 'tex': 'g = \\frac{m}{1 + m}'},
      {'lb': 'Margin to mark-up', 'tex': 'm = \\frac{g}{1 - g}'},
      {'lb': 'From cost', 'tex': '\\text{Selling price} = \\text{Cost} \\times (1 + m)'},
      {'lb': 'From selling price', 'tex': '\\text{Cost} = \\text{Selling price} \\times (1 - g)'},
    ]}},
    {'key': 'The arithmetic trick is to think in **thirds and quarters of a common whole**. A '
            'mark-up of $\\frac{1}{4}$ on cost means cost 4, profit 1, sales 5 — so the margin '
            'is $\\frac{1}{5}$. A margin of $\\frac{1}{4}$ means sales 4, profit 1, cost 3 — so '
            'the mark-up is $\\frac{1}{3}$. Set out cost : profit : sales and read off whichever '
            'ratio is wanted.'},
    {'eg': {'t': 'Converting between the two', 'q': [
      {'p': 'Goods costing ₦40,000 are sold at a mark-up of 25%. Determine the selling price, '
            'the gross profit and the gross margin.'}],
      'a': [
      {'tex': '\\text{Gross profit} = 40{,}000 \\times 0.25 = ₦10{,}000'},
      {'tex': '\\text{Selling price} = 40{,}000 + 10{,}000 = ₦50{,}000'},
      {'tex': '\\text{Margin} = \\frac{10{,}000}{50{,}000} \\times 100 = 20\\%'},
      {'p': 'Or directly from the formula:'},
      {'tex': 'g = \\frac{m}{1+m} = \\frac{0.25}{1.25} = 0.20 = 20\\%'},
      {'note': 'A 25% mark-up is **not** a 25% margin. The mark-up is always the larger of the '
               'two, because it is a percentage of the smaller base.'}]}},
  ]},

  {'n': '9.2', 't': 'Working back from sales', 'b': [
    {'p': 'Questions frequently give the sales figure and the margin and ask for the cost of '
          'sales — the standard route to a closing inventory figure when the inventory itself '
          'has been destroyed or not counted.'},
    {'eg': {'t': 'Reconstructing cost of sales', 'q': [
      {'p': 'Sales for the year were ₦2,400,000 and the gross margin was 30%. Compute the gross '
            'profit, the cost of sales, and the equivalent mark-up on cost.'}],
      'a': [
      {'tex': '\\text{Gross profit} = 2{,}400{,}000 \\times 0.30 = ₦720{,}000'},
      {'tex': '\\text{Cost of sales} = 2{,}400{,}000 - 720{,}000 = ₦1{,}680{,}000'},
      {'p': 'Or directly: $\\text{Cost} = \\text{Sales} \\times (1 - g) = 2{,}400{,}000 '
            '\\times 0.70 = ₦1{,}680{,}000$.'},
      {'tex': 'm = \\frac{720{,}000}{1{,}680{,}000} \\times 100 = 42.86\\%'},
      {'p': 'Which agrees with $m = \\dfrac{g}{1-g} = \\dfrac{0.30}{0.70} = 0.4286$.'}]}},
    {'eg': {'t': 'Estimating inventory lost in a fire', 'q': [
      {'p': 'A trader\'s warehouse was destroyed by fire on 30 September. The records show '
            'opening inventory ₦300,000, purchases to the date of the fire ₦1,500,000 and sales '
            '₦1,800,000. The gross margin has consistently been 25%. Goods with a salvage value '
            'of ₦60,000 were recovered. Compute the amount of the insurance claim.'}],
      'a': [
      {'p': 'Cost of sales is found from the margin:'},
      {'tex': '\\text{Cost of sales} = 1{,}800{,}000 \\times (1 - 0.25) = ₦1{,}350{,}000'},
      {'p': 'Goods available for sale, then the balancing figure for inventory at the date of '
            'the fire:'},
      {'stmt': {'t': 'Inventory at date of fire', 'rows': [
        ['Opening inventory', 300000],
        ['Add: Purchases', 1500000],
        ['Goods available for sale@sub', 1800000],
        ['Less: Cost of sales', -1350000],
        ['Inventory at 30 September@tot', 450000],
      ]}},
      {'stmt': {'t': 'Insurance claim', 'rows': [
        ['Inventory destroyed', 450000],
        ['Less: Salvage value recovered', -60000],
        ['Amount of claim@tot', 390000],
      ]}},
      {'note': 'The coincidence that goods available for sale (₦1,800,000) equals sales '
               '(₦1,800,000) is accidental and does not affect the method. The logic is always: '
               'opening + purchases − cost of sales = closing.'}]}},
  ]},

  {'n': '9.3', 't': 'Discounts and commission', 'b': [
    {'ul': [
      '**Trade discount** — a reduction off the list price given to a customer in the trade. It '
      'is deducted before the invoice is raised and never appears in the accounts.',
      '**Cash (settlement) discount** — a reduction for prompt payment, applied to the invoice '
      'value, i.e. **after** trade discount.',
      '**Quantity discount** — a trade discount whose rate rises with the order size.',
    ]},
    {'warn': 'The two discounts are applied in sequence, not added. A 15% trade discount '
             'followed by a 2.5% cash discount is a total reduction of $1 - (0.85 \\times '
             '0.975) = 17.125\\%$, not 17.5%.'},
    {'eg': {'t': 'Trade then cash discount', 'q': [
      {'p': 'Goods with a list price of ₦500,000 are sold subject to a trade discount of 15%. '
            'The customer pays within the settlement period and takes a further cash discount '
            'of 2.5%. Compute the invoice value and the amount actually received.'}],
      'a': [
      {'tex': '\\text{Invoice value} = 500{,}000 \\times (1 - 0.15) = ₦425{,}000'},
      {'tex': '\\text{Cash received} = 425{,}000 \\times (1 - 0.025) = ₦414{,}375'},
      {'p': 'The cash discount of ₦10,625 is a charge in profit or loss; the trade discount of '
            '₦75,000 is recorded nowhere — sales are simply recognised at ₦425,000.'}]}},
    {'eg': {'t': 'Commission on a sliding scale', 'q': [
      {'p': 'A sales representative earns commission of 5% on the first ₦2,000,000 of sales and '
            '8% on sales above that figure. Compute the commission on sales of ₦3,500,000.'}],
      'a': [
      {'tex': '\\text{On the first } ₦2{,}000{,}000: \\quad 2{,}000{,}000 \\times 0.05 '
              '= ₦100{,}000'},
      {'tex': '\\text{On the excess } ₦1{,}500{,}000: \\quad 1{,}500{,}000 \\times 0.08 '
              '= ₦120{,}000'},
      {'tex': '\\text{Total commission} = 100{,}000 + 120{,}000 = ₦220{,}000'},
      {'note': 'A sliding scale applies each rate only to its own band. Applying 8% to the whole '
               '₦3,500,000 would give ₦280,000 and is the standard trap.'}]}},
  ]},

  {'n': '9.4', 't': 'Losses', 'b': [
    {'p': 'A loss is handled identically, with a negative profit. Note that a given percentage '
          'loss on cost is a **larger** percentage of selling price, because the selling price '
          'is now the smaller figure — the reverse of the profit case.'},
    {'eg': {'t': 'Loss on cost and on selling price', 'q': [
      {'p': 'Goods costing ₦80,000 are sold at a loss of 12.5% on cost. Compute the selling '
            'price and express the loss as a percentage of selling price.'}],
      'a': [
      {'tex': '\\text{Loss} = 80{,}000 \\times 0.125 = ₦10{,}000'},
      {'tex': '\\text{Selling price} = 80{,}000 - 10{,}000 = ₦70{,}000'},
      {'tex': '\\text{Loss on selling price} = \\frac{10{,}000}{70{,}000} \\times 100 '
              '= 14.29\\%'}]}},
  ]},

  {'n': '9.5', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'note': 'The study text works **profit % and loss % on cost price** throughout (not on '
             'sales). "Mark-up on cost" in §9.1 is the same thing as the study text\'s '
             '"profit %"; "margin" is the sales-based version this chapter adds for the '
             'inventory questions of Financial Accounting.'},
    {'h3': 'All the terms'},
    {'ul': [
      '**Cost price (CP)** — the price the buyer pays to acquire the item. Made up of **fixed '
      'cost** (constant) and **variable cost** (varies with output / other factors).',
      '**Selling price (SP)** — the price at which the item is actually sold; $= \\text{CP} + '
      '\\text{target gross profit}$.',
      '**Profit / gain** — the excess of SP over CP ($\\text{SP} > \\text{CP}$).',
      '**Loss** — the shortfall of SP below CP ($\\text{SP} < \\text{CP}$).',
      '**Profit % / loss %** — profit or loss as a percentage **of cost price**.',
      '**Marked price (MP)** — the price labelled/quoted on the product; also called *market '
      'price, retail price, list price*. Discount is calculated on this. Set at a percentage '
      'above cost.',
      '**Discount** — a rebate off the marked price to attract customers or clear old stock; '
      'the price after discount **is** the selling price.',
      '**Discount %** — discount as a percentage of the marked price.',
      '**Mark-up** — gross profit as a percentage of **cost** (this chapter, §9.1).',
      '**Margin** — gross profit as a percentage of **selling price** (this chapter, §9.1).',
      '**Trade discount** — a reduction off list price for the trade, deducted *before* '
      'invoicing. **Cash (settlement) discount** — a reduction for prompt payment, on the '
      'invoiced amount.',
    ]},
    {'h3': 'A. Profit and loss (study text — all on cost price)'},
    {'fbox': {'h': 'Profit / loss', 'rows': [
      {'lb': 'Profit', 'tex': '\\text{Profit} = \\text{SP} - \\text{CP} \\quad (\\text{SP} > '
              '\\text{CP})'},
      {'lb': 'Loss', 'tex': '\\text{Loss} = \\text{CP} - \\text{SP} \\quad (\\text{CP} > '
              '\\text{SP})'},
      {'lb': 'Profit percentage',
       'tex': '\\text{Profit\\%} = \\dfrac{\\text{SP} - \\text{CP}}{\\text{CP}} \\times 100 '
              '= \\dfrac{\\text{Profit}}{\\text{CP}} \\times 100'},
      {'lb': 'Loss percentage',
       'tex': '\\text{Loss\\%} = \\dfrac{\\text{CP} - \\text{SP}}{\\text{CP}} \\times 100 '
              '= \\dfrac{\\text{Loss}}{\\text{CP}} \\times 100'},
      {'lb': 'SP from CP and profit $x\\%$',
       'tex': '\\text{SP} = \\dfrac{(100 + x)}{100} \\times \\text{CP}'},
      {'lb': 'SP from CP and loss $x\\%$',
       'tex': '\\text{SP} = \\dfrac{(100 - x)}{100} \\times \\text{CP}'},
      {'lb': 'CP from SP and profit $x\\%$',
       'tex': '\\text{CP} = \\dfrac{100}{100 + x} \\times \\text{SP}'},
      {'lb': 'CP from SP and loss $x\\%$',
       'tex': '\\text{CP} = \\dfrac{100}{100 - x} \\times \\text{SP}'},
    ]}},
    {'h3': 'B. Discount and marked price'},
    {'fbox': {'h': 'Discount / marked price', 'rows': [
      {'lb': 'Discount from a rate', 'tex': '\\text{Discount} = \\text{Discount\\%} \\times '
              '\\text{MP}'},
      {'lb': 'Discount from prices', 'tex': '\\text{Discount} = \\text{MP} - \\text{SP}'},
      {'lb': 'Discount percentage',
       'tex': '\\text{Discount\\%} = \\dfrac{\\text{Discount}}{\\text{MP}} \\times 100'},
      {'lb': 'The key identity', 'tex': '\\text{MP} = \\text{SP} + \\text{Discount}'},
      {'lb': 'SP after a discount rate $d\\%$',
       'tex': '\\text{SP} = \\text{MP}\\,(1 - d) = \\dfrac{(100 - d)}{100} \\times \\text{MP}'},
      {'lb': 'MP from SP and discount rate $d\\%$',
       'tex': '\\text{MP} = \\dfrac{\\text{SP}}{1 - d}'},
      {'lb': 'MP giving profit $x\\%$ **and** discount $d\\%$ on cost $C$',
       'tex': '\\text{MP} = \\dfrac{C\\,(1 + \\tfrac{x}{100})}{1 - \\tfrac{d}{100}} '
              '\\quad \\left(\\text{since } \\text{SP} = C(1+\\tfrac{x}{100}) = '
              '\\text{MP}(1-\\tfrac{d}{100})\\right)'},
    ]}},
    {'h3': 'C. Mark-up and margin (§9.1)'},
    {'fbox': {'h': 'Mark-up / margin', 'rows': [
      {'lb': 'Mark-up (on cost)',
       'tex': 'm = \\dfrac{\\text{Gross profit}}{\\text{Cost}}'},
      {'lb': 'Margin (on sales)',
       'tex': 'g = \\dfrac{\\text{Gross profit}}{\\text{Sales}}'},
      {'lb': 'Mark-up → margin', 'tex': 'g = \\dfrac{m}{1 + m}'},
      {'lb': 'Margin → mark-up', 'tex': 'm = \\dfrac{g}{1 - g}'},
      {'lb': 'Selling price from cost', 'tex': '\\text{SP} = \\text{Cost}\\,(1 + m)'},
      {'lb': 'Cost from selling price', 'tex': '\\text{Cost} = \\text{SP}\\,(1 - g)'},
      {'lb': 'Cost of sales identity',
       'tex': '\\text{Opening inventory} + \\text{Purchases} - \\text{Closing inventory} '
              '= \\text{Cost of sales}'},
    ]}},
  ]},
 ],
 'formulas': [
  {'lb': 'Profit', 'tex': '\\text{Profit} = \\text{SP} - \\text{CP}'},
  {'lb': 'Loss', 'tex': '\\text{Loss} = \\text{CP} - \\text{SP}'},
  {'lb': 'Profit % (on cost)',
   'tex': '\\text{Profit\\%} = \\frac{\\text{SP} - \\text{CP}}{\\text{CP}} \\times 100'},
  {'lb': 'Loss % (on cost)',
   'tex': '\\text{Loss\\%} = \\frac{\\text{CP} - \\text{SP}}{\\text{CP}} \\times 100'},
  {'lb': 'SP given CP and profit $x\\%$', 'tex': '\\text{SP} = \\frac{100 + x}{100}\\,\\text{CP}'},
  {'lb': 'SP given CP and loss $x\\%$', 'tex': '\\text{SP} = \\frac{100 - x}{100}\\,\\text{CP}'},
  {'lb': 'Discount from rate', 'tex': '\\text{Discount} = \\text{Discount\\%} \\times \\text{MP}'},
  {'lb': 'Discount from prices', 'tex': '\\text{Discount} = \\text{MP} - \\text{SP}'},
  {'lb': 'Discount %',
   'tex': '\\text{Discount\\%} = \\frac{\\text{Discount}}{\\text{MP}} \\times 100'},
  {'lb': 'Marked price identity', 'tex': '\\text{MP} = \\text{SP} + \\text{Discount}'},
  {'lb': 'SP after discount $d\\%$', 'tex': '\\text{SP} = \\text{MP}\\,(1 - d)'},
  {'lb': 'MP from SP and discount $d\\%$', 'tex': '\\text{MP} = \\frac{\\text{SP}}{1 - d}'},
  {'lb': 'Mark-up (on cost)', 'tex': 'm = \\frac{\\text{GP}}{\\text{Cost}}'},
  {'lb': 'Margin (on sales)', 'tex': 'g = \\frac{\\text{GP}}{\\text{Sales}}'},
  {'lb': 'Mark-up to margin', 'tex': 'g = \\frac{m}{1+m}'},
  {'lb': 'Margin to mark-up', 'tex': 'm = \\frac{g}{1-g}'},
  {'lb': 'Selling price from cost', 'tex': 'S = C(1 + m)'},
  {'lb': 'Cost from selling price', 'tex': 'C = S(1 - g)'},
  {'lb': 'Cost of sales identity',
   'tex': '\\text{Opening} + \\text{Purchases} - \\text{Closing} = \\text{Cost of sales}'},
 ],
 'focus':
   'One or two Section A marks nearly every diet, usually a straight mark-up-to-margin '
   'conversion or a selling price from a cost. The material reappears in Financial Accounting '
   'in incomplete-records and fire-claim questions, so the reconstruction of cost of sales from '
   'a margin is worth more practice than its own chapter weighting suggests.',
 'errors': [
   'Treating a mark-up percentage as though it were a margin, or the reverse.',
   'Adding trade and cash discount percentages instead of applying them in sequence.',
   'Applying the top commission rate to the whole of sales rather than to the excess band.',
   'Recording trade discount in the ledger; it never enters the accounts.',
   'Forgetting that a percentage loss on cost is a larger percentage of selling price.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Goods costing ₦60,000 are sold at a mark-up of 20%. The selling price is',
    'o': ['₦48,000', '₦72,000', '₦75,000', '₦12,000', '₦50,000'],
    'a': 1,
    'w': 'Mark-up is a percentage of cost, so add 20% of ₦60,000 to the cost.',
    'calc': 'S = 60{,}000 \\times 1.20 = ₦72{,}000',
    'src': 'Chapter 9.1'},
   {'q': 'A mark-up of 25% on cost is equivalent to a margin on selling price of',
    'o': ['25%', '20%', '33⅓%', '30%', '75%'],
    'a': 1,
    'w': 'Cost 4, profit 1, sales 5, so the profit is one fifth of sales.',
    'calc': 'g = \\frac{m}{1+m} = \\frac{0.25}{1.25} = 0.20 = 20\\%',
    'src': 'Chapter 9.1'},
   {'q': 'Sales are ₦900,000 and the gross margin is 20%. The cost of sales is',
    'o': ['₦180,000', '₦720,000', '₦750,000', '₦1,080,000', '₦680,000'],
    'a': 1,
    'w': 'Cost of sales is the complement of the margin applied to sales.',
    'calc': '\\text{Cost of sales} = 900{,}000 \\times 0.80 = ₦720{,}000',
    'src': 'Chapter 9.2'},
   {'q': 'A margin of 20% on selling price corresponds to a mark-up on cost of',
    'o': ['20%', '25%', '16⅔%', '80%', '125%'],
    'a': 1,
    'w': 'Sales 5, profit 1, cost 4, so the profit is one quarter of cost.',
    'calc': 'm = \\frac{g}{1-g} = \\frac{0.20}{0.80} = 0.25 = 25\\%',
    'src': 'Chapter 9.1'},
   {'q': 'Goods listed at ₦200,000 carry a trade discount of 10% and a cash discount of 5%. '
         'The amount received on prompt payment is',
    'o': ['₦170,000', '₦171,000', '₦180,000', '₦190,000', '₦185,000'],
    'a': 1,
    'w': 'Apply the discounts in sequence: trade discount first to give the invoice value, then '
         'cash discount on that value.',
    'calc': '200{,}000 \\times 0.90 \\times 0.95 = 180{,}000 \\times 0.95 = ₦171{,}000',
    'src': 'Chapter 9.3'},
   {'q': 'An article costing ₦2,500 is sold for ₦2,000. The loss as a percentage of cost is',
    'o': ['25%', '20%', '15%', '10%', '80%'],
    'a': 1,
    'w': 'The loss is ₦500; expressed on cost the base is ₦2,500.',
    'calc': '\\frac{500}{2{,}500} \\times 100 = 20\\%',
    'src': 'Chapter 9.4'},
  ],
  'theory': [
   {'q': 'Distinguish between mark-up and margin, and explain why the distinction matters when '
         'the closing inventory of a business has to be estimated rather than counted.',
    'marks': 8,
    'a': [
      {'h4': 'The distinction'},
      {'p': 'Both express gross profit as a percentage, but they use different denominators.'},
      {'table': {'align': 'lll', 'head': ['', 'Mark-up', 'Margin'], 'rows': [
        ['Base', 'Cost', 'Selling price'],
        ['Formula', '$\\text{GP} \\div \\text{Cost}$', '$\\text{GP} \\div \\text{Sales}$'],
        ['On GP ₦25, cost ₦100', '25%', '20%'],
        ['Relative size', 'Always the larger', 'Always the smaller'],
      ]}},
      {'p': 'Because cost is smaller than selling price whenever a profit is made, the same '
            'naira of profit is always a larger percentage of cost than of sales. The two are '
            'linked by:'},
      {'tex': 'g = \\frac{m}{1+m} \\qquad\\text{and}\\qquad m = \\frac{g}{1-g}'},
      {'h4': 'Why it matters for estimated inventory'},
      {'p': 'Closing inventory has to be estimated where there has been a fire or theft, where '
            'records are incomplete, or where an interim figure is needed without a physical '
            'count. The method relies on the cost of sales identity:'},
      {'tex': '\\text{Opening inventory} + \\text{Purchases} - \\text{Closing inventory} '
              '= \\text{Cost of sales}'},
      {'p': 'rearranged to give closing inventory as the balancing figure. Cost of sales itself '
            'is not known directly; it is derived from sales using the profit percentage. If '
            'the percentage is a **margin**, cost of sales is $\\text{Sales} \\times (1 - g)$. '
            'If it is a **mark-up**, cost of sales is $\\text{Sales} \\div (1 + m)$.'},
      {'p': 'Using the wrong one produces a wrong cost of sales, and because closing inventory '
            'is the balancing figure the whole of that error lands on the inventory. On sales '
            'of ₦1,000,000 with a stated 25%, treating a mark-up as a margin gives cost of '
            'sales of ₦750,000 instead of ₦800,000 — an inventory figure overstated by '
            '₦50,000, and an insurance claim or a set of accounts overstated by the same '
            'amount.'},
      {'note': 'When a question says only "profit of 25% on sales" or "25% on cost", the '
               'preposition is doing all the work. Underline it before starting the '
               'computation.'}],
    'src': 'Chapter 9.1–9.2'},
  ]},
}
