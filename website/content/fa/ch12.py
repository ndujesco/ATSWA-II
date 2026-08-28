CH = {
 'n': 12,
 't': 'Accounting for Inventories (IAS 2)',
 'brief': 'What cost includes, the FIFO and weighted average cost formulas, net realisable value, '
          'the periodic and perpetual systems, and inventory lost or counted after the year end.',
 'outcomes': [
   'Determine the cost of inventory under IAS 2',
   'Value inventory using FIFO and weighted average cost, periodic and perpetual',
   'Apply the lower of cost and net realisable value rule item by item',
   'Compute inventory lost in a fire or theft',
   'Adjust a count taken before or after the reporting date',
 ],
 'secs': [
  {'n': '12.1', 't': 'The cost of inventory', 'b': [
    {'p': 'IAS 2 says cost comprises all **costs of purchase**, **costs of conversion** and other '
          'costs incurred in bringing the inventories to their present location and condition.'},
    {'table': {'head': ['Include', 'Exclude — expense as incurred'], 'align': 'll', 'rows': [
      ['Purchase price', 'Abnormal waste of materials, labour or overheads'],
      ['Import duties and non-refundable taxes', 'Storage costs, unless necessary before a further stage'],
      ['Transport and handling inwards', 'Administrative overheads not related to production'],
      ['Direct labour and direct expenses', 'Selling and distribution costs'],
      ['Fixed and variable production overheads', 'Recoverable VAT'],
      ['', 'Settlement discounts (a financing item)'],
    ], 'note': 'Trade discounts and rebates are deducted in arriving at cost; settlement '
               'discounts are not.'}},
    {'key': 'Fixed production overheads are absorbed on the basis of **normal capacity**, not '
            'actual output. In a period of low production the unabsorbed overhead is expensed '
            'rather than being buried in inventory.'},
  ]},

  {'n': '12.2', 't': 'Cost formulas', 'b': [
    {'p': 'IAS 2 permits **specific identification** for items that are not ordinarily '
          'interchangeable, and otherwise **FIFO** or **weighted average cost**. '
          '**LIFO is prohibited** under IFRS — a point examined regularly.'},
    {'h3': 'FIFO — first in, first out'},
    {'p': 'The earliest purchases are assumed sold first, so closing inventory is valued at the '
          'most recent prices. In a period of rising prices FIFO gives the **highest** closing '
          'inventory, the **lowest** cost of sales and therefore the **highest** profit.'},
    {'h3': 'Weighted average cost'},
    {'tex': '\\text{AVCO} = \\frac{\\text{Total cost of goods available}}'
            '{\\text{Total units available}}', 'tag': '(12.1)'},
    {'p': 'Under the **periodic** system this is computed once at the period end. Under the '
          '**perpetual** system a new average is struck after every purchase, which is the more '
          'demanding computation and the one examiners prefer.'},
    {'eg': {'t': 'FIFO and AVCO compared', 'q': [
      {'p': 'The following movements occurred in the month of March:'},
      {'table': {'align': 'llrr', 'head': ['Date', 'Movement', 'Units', 'Unit cost (₦)'], 'rows': [
        ['1 March', 'Opening inventory', '200', '500'],
        ['6 March', 'Purchase', '300', '540'],
        ['12 March', 'Sale', '(400)', ''],
        ['18 March', 'Purchase', '250', '580'],
        ['25 March', 'Sale', '(200)', ''],
      ]}},
      {'p': 'Value the closing inventory and the cost of sales under (a) FIFO and (b) weighted '
            'average cost on a perpetual basis.'}],
      'a': [
      {'p': 'Units available $= 200 + 300 + 250 = 750$; units sold $= 400 + 200 = 600$; closing '
            'inventory $= 150$ units.'},
      {'h4': '(a) FIFO'},
      {'table': {'align': 'llr', 'head': ['Date', 'Working', 'Amount (₦)'], 'rows': [
        ['12 Mar sale', '200 @ 500 = 100,000; 200 @ 540 = 108,000', '208,000'],
        ['25 Mar sale', '100 @ 540 = 54,000; 100 @ 580 = 58,000', '112,000'],
        ['Cost of sales', '', '320,000', '@tot'],
        ['Closing inventory', '150 @ 580', '87,000', '@tot'],
      ]}},
      {'p': 'Check: goods available $= 100{,}000 + 162{,}000 + 145{,}000 = ₦407{,}000$, and '
            '$407{,}000 - 320{,}000 = ₦87{,}000$. ✓'},
      {'h4': '(b) Weighted average, perpetual'},
      {'table': {'align': 'lrrrr',
        'head': ['Date', 'Units', 'Value (₦)', 'Average (₦)', 'Cost of sale (₦)'], 'rows': [
        ['1 Mar balance', '200', '100,000', '500', ''],
        ['6 Mar purchase', '300', '162,000', '', ''],
        ['Balance', '500', '262,000', '524.00', ''],
        ['12 Mar sale 400', '(400)', '(209,600)', '524.00', '209,600'],
        ['Balance', '100', '52,400', '524.00', ''],
        ['18 Mar purchase', '250', '145,000', '', ''],
        ['Balance', '350', '197,400', '564.00', ''],
        ['25 Mar sale 200', '(200)', '(112,800)', '564.00', '112,800'],
        ['Closing inventory', '150', '84,600', '564.00', '322,400', '@tot'],
      ]}},
      {'p': 'New average after 6 March: $\\dfrac{262{,}000}{500} = ₦524$. After 18 March: '
            '$\\dfrac{52{,}400 + 145{,}000}{350} = \\dfrac{197{,}400}{350} = ₦564$.'},
      {'h4': 'Comparison'},
      {'table': {'align': 'lrr', 'head': ['', 'FIFO (₦)', 'AVCO (₦)'], 'rows': [
        ['Closing inventory', '87,000', '84,600'],
        ['Cost of sales', '320,000', '322,400'],
        ['Difference in profit', '', '2,400 lower under AVCO'],
      ]}},
      {'note': 'With prices rising, FIFO leaves the newest, dearest units in inventory, so '
               'closing inventory is higher and cost of sales lower. Both methods are acceptable '
               'under IAS 2; what matters is applying the chosen one consistently.'}]}},
  ]},

  {'n': '12.3', 't': 'Net realisable value', 'b': [
    {'tex': '\\text{NRV} = \\text{Estimated selling price} - \\text{Estimated costs of completion} '
            '- \\text{Estimated costs necessary to make the sale}', 'tag': '(12.2)'},
    {'p': 'Inventory is carried at the **lower of cost and net realisable value**, and — this is '
          'where the marks are — the comparison is made **item by item** (or by group of similar '
          'items), never on the total.'},
    {'eg': {'t': 'Lower of cost and NRV', 'q': [
      {'p': 'Value the following closing inventory.'},
      {'table': {'align': 'lrrr',
        'head': ['Item', 'Cost (₦)', 'Selling price (₦)', 'Selling costs (₦)'], 'rows': [
        ['A', '840,000', '1,100,000', '60,000'],
        ['B', '520,000', '540,000', '80,000'],
        ['C', '390,000', '460,000', '25,000'],
        ['D', '1,250,000', '1,180,000', '90,000'],
      ]}}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['Item', 'Cost (₦)', 'NRV (₦)', 'Lower (₦)'], 'rows': [
        ['A', '840,000', '1,040,000', '840,000'],
        ['B', '520,000', '460,000', '460,000'],
        ['C', '390,000', '435,000', '390,000'],
        ['D', '1,250,000', '1,090,000', '1,090,000'],
        ['Total', '3,000,000', '3,025,000', '2,780,000', '@tot'],
      ]}},
      {'p': 'Closing inventory is **₦2,780,000**, and the write-down of ₦220,000 is charged to '
            'cost of sales.'},
      {'warn': 'Comparing the totals would give ₦3,000,000 — the lower of ₦3,000,000 and '
               '₦3,025,000 — and would overstate inventory by ₦220,000. The gains on A and C are '
               'not permitted to offset the losses on B and D. This is the single most examined '
               'point in the chapter.'}]}},
    {'h3': 'When does NRV fall below cost?'},
    {'ul': ['Physical damage or deterioration.', 'Obsolescence, or a change in fashion or technology.',
            'A fall in the market selling price.', 'An increase in the estimated costs to complete.',
            'A marketing or distribution error leaving unsaleable stock.']},
  ]},

  {'n': '12.4', 't': 'Periodic and perpetual systems', 'b': [
    {'table': {'head': ['', 'Periodic', 'Perpetual'], 'align': 'lll', 'rows': [
      ['Inventory record', 'Counted at the period end only', 'Updated after every movement'],
      ['Cost of sales', 'Derived: opening + purchases − closing', 'Recorded as each sale is made'],
      ['Losses and theft', 'Buried in cost of sales, invisible', 'Revealed as a difference on count'],
      ['Cost to run', 'Low', 'Higher, but automated by modern systems'],
      ['Suits', 'Many low-value items', 'Fewer, higher-value items'],
    ]}},
    {'tex': '\\text{Cost of sales} = \\text{Opening inventory} + \\text{Purchases} '
            '- \\text{Closing inventory}', 'tag': '(12.3)'},
  ]},

  {'n': '12.5', 't': 'Inventory lost, and the cut-off', 'b': [
    {'p': 'Where inventory is destroyed and no count exists, work backwards from the gross profit '
          'percentage. This is exactly the incomplete records technique of Chapter 6.'},
    {'tex': '\\text{Inventory lost} = \\bigl(\\text{Opening inventory} + \\text{Purchases}\\bigr) '
            '- \\text{Cost of goods sold} - \\text{Salvaged inventory}', 'tag': '(12.4)'},
    {'eg': {'t': 'Inventory destroyed by fire', 'q': [
      {'p': 'A fire on 30 September destroyed most of the inventory of Kudi Stores. Records show: '
            'inventory at 1 January ₦2,400,000; purchases to 30 September ₦18,600,000; sales to '
            '30 September ₦24,000,000. The business consistently earns a gross margin of 25%. '
            'Inventory salvaged was valued at ₦380,000. Compute the loss.'}],
      'a': [
      {'tex': '\\text{Cost of goods sold} = 0.75 \\times 24{,}000{,}000 = ₦18{,}000{,}000'},
      {'stmt': {'t': 'Inventory destroyed', 'rows': [
        ['Opening inventory', 2400000],
        ['Purchases', 18600000],
        ['Goods available for sale', 21000000, '@t'],
        ['Less cost of goods sold (75% of sales)', -18000000],
        ['Inventory that should have been on hand', 3000000, '@t'],
        ['Less inventory salvaged', -380000],
        ['Inventory destroyed by fire', 2620000, '@tt'],
      ]}},
      {'note': 'A 25% **margin** means cost of sales is 75% of sales. Had the question said a 25% '
               '**mark-up**, cost of sales would have been $\\tfrac{100}{125} = 80\\%$ of sales, '
               'giving ₦19,200,000 and a loss of ₦1,420,000. Read the word.'}]}},
    {'h3': 'Cut-off'},
    {'p': 'Where the physical count is taken on a date other than the reporting date, adjust '
          'backwards or forwards for the movements in between.'},
    {'table': {'head': ['Count taken', 'Adjustment to reach the year-end figure'], 'align': 'll',
     'rows': [
      ['**After** the year end', 'Add goods sold in between (at cost); deduct goods purchased in between'],
      ['**Before** the year end', 'Deduct goods sold in between (at cost); add goods purchased in between'],
    ]}},
    {'p': 'Also adjust for goods **on sale or return** not yet sold (still ours, include at cost), '
          'goods held on **consignment** for others (exclude), and goods in transit where the '
          'risks and rewards have passed (include).'},
  ]},
 ],
 'formulas': [
  {'lb': 'Weighted average cost',
   'tex': '\\text{AVCO} = \\frac{\\text{Cost of goods available}}{\\text{Units available}}'},
  {'lb': 'Net realisable value',
   'tex': '\\text{NRV} = \\text{Selling price} - \\text{Costs to complete} - \\text{Selling costs}'},
  {'lb': 'Cost of sales',
   'tex': '\\text{COS} = \\text{Opening inventory} + \\text{Purchases} - \\text{Closing inventory}'},
  {'lb': 'Inventory lost',
   'tex': '\\text{Lost} = \\text{Opening} + \\text{Purchases} - \\text{COS} - \\text{Salvage}'},
 ],
 'focus':
   'Almost always in Section A as two or three questions — a FIFO or AVCO computation, an NRV '
   'comparison, and the fact that LIFO is prohibited. In Section B it appears as a part of a '
   'final-accounts question or as a standalone inventory valuation with a fire loss. The '
   'item-by-item NRV rule is the highest-yield single fact in the chapter.',
 'errors': [
   'Comparing total cost with total NRV instead of item by item.',
   'Using LIFO, which IAS 2 prohibits.',
   'Including selling and distribution costs, or storage of finished goods, in the cost of inventory.',
   'Deducting a settlement discount in arriving at cost.',
   'Confusing margin with mark-up when working back to cost of sales in a fire-loss question.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Under IAS 2, inventories are measured at',
    'o': ['cost', 'net realisable value', 'the lower of cost and net realisable value',
          'the higher of cost and net realisable value', 'replacement cost'],
    'a': 2,
    'w': 'The lower of the two, applied item by item or by group of similar items. This applies '
         'prudence: an asset is not carried above the amount expected to be recovered from it.',
    'src': 'Chapter 12.3'},
   {'q': 'An item of inventory cost ₦1,000. Its selling price has fallen to ₦800 and ₦100 of '
         'costs will be incurred before it can be sold. Its net realisable value is',
    'o': ['₦1,000', '₦900', '₦800', '₦700', '₦600'],
    'a': 3,
    'w': 'NRV is the estimated selling price less the costs necessary to make the sale. The item '
         'is written down from ₦1,000 to ₦700, a loss of ₦300.',
    'calc': '\\text{NRV} = 800 - 100 = 700',
    'src': 'Chapter 12.3'},
   {'q': 'Which cost formula is NOT permitted by IAS 2?',
    'o': ['First in, first out', 'Weighted average cost', 'Specific identification',
          'Last in, first out', 'Standard cost, where it approximates actual cost'],
    'a': 3,
    'w': 'LIFO was withdrawn because it rarely reflects the physical flow of goods and, in a '
         'period of rising prices, leaves obsolete costs in the statement of financial position.',
    'src': 'Chapter 12.2'},
   {'q': 'Opening inventory ₦900,000; purchases ₦7,200,000; sales ₦9,600,000; gross margin 30%. '
         'Closing inventory is',
    'o': ['₦1,380,000', '₦1,200,000', '₦2,100,000', '₦1,020,000', '₦1,500,000'],
    'a': 1,
    'w': 'Cost of sales is 70% of sales, and closing inventory is the balancing figure in the '
         'cost of sales computation.',
    'calc': '\\text{COS} = 0.70 \\times 9{,}600{,}000 = 6{,}720{,}000; \\quad '
            '900{,}000 + 7{,}200{,}000 - 6{,}720{,}000 = 1{,}380{,}000',
    'src': 'Chapter 12.5'},
   {'q': 'In a period of rising prices, compared with weighted average cost, FIFO gives',
    'o': ['a lower closing inventory and a lower profit',
          'a higher closing inventory and a higher profit',
          'a higher closing inventory and a lower profit',
          'the same closing inventory and the same profit',
          'a lower closing inventory and a higher profit'],
    'a': 1,
    'w': 'FIFO leaves the most recent, dearest purchases in inventory. Higher closing inventory '
         'means lower cost of sales, and therefore higher reported profit.',
    'src': 'Chapter 12.2'},
   {'q': 'Which of the following should be included in the cost of inventory?',
    'o': ['Storage costs of finished goods', 'Selling and distribution costs',
          'Import duties on raw materials', 'Abnormal wastage of materials',
          'General administrative overheads'],
    'a': 2,
    'w': 'Import duties are a cost of purchase and are directly attributable to bringing the '
         'inventory to its present location and condition. The other four are all expensed as '
         'incurred under IAS 2.',
    'src': 'Chapter 12.1'},
  ],
  'theory': [
   {'q': 'State the costs that should be included in, and excluded from, the cost of inventories '
         'under IAS 2, and explain how net realisable value is determined and applied.',
    'marks': 10,
    'a': [
      {'h4': 'Included'},
      {'ul': [
        'The **purchase price**, net of trade discounts and rebates.',
        '**Import duties** and other non-refundable taxes.',
        '**Transport, handling and other costs** directly attributable to acquisition.',
        '**Costs of conversion** — direct labour and direct expenses.',
        '**Production overheads**, both variable and fixed, the fixed element absorbed on the '
        'basis of **normal capacity**.',
        'Other costs incurred in bringing the inventories to their present location and condition.']},
      {'h4': 'Excluded, and expensed as incurred'},
      {'ul': [
        '**Abnormal** amounts of wasted material, labour or overhead.',
        '**Storage costs**, unless necessary in the production process before a further stage.',
        '**Administrative overheads** that do not contribute to bringing inventories to their '
        'present location and condition.',
        '**Selling and distribution costs**.',
        'Recoverable taxes and settlement discounts.']},
      {'h4': 'Net realisable value'},
      {'p': 'NRV is the estimated selling price in the ordinary course of business less the '
            'estimated costs of completion and the estimated costs necessary to make the sale:'},
      {'tex': '\\text{NRV} = \\text{Selling price} - \\text{Costs to complete} - '
              '\\text{Costs to sell}'},
      {'p': 'Inventories are carried at the **lower of cost and NRV**. The comparison is made for '
            'each item separately, or for groups of similar items, and **never on the total** — '
            'to do otherwise would let unrealised gains on some items offset losses on others. '
            'Any write-down is recognised as an expense in the period. If the circumstances that '
            'caused a write-down cease to exist, the write-down is reversed, but only up to the '
            'original cost.'}],
    'src': 'Chapter 12.3'},
  ]},
}
