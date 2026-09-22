CH = {
 'n': 9,
 't': 'Profit or Loss, Based on Sales',
 'brief': 'Cost price, selling price, profit and loss percentages (all on cost price), '
          'discounting, and the marked-price relationship.',
 'outcomes': [
   'Understand the meaning of cost price, selling price, profit and loss',
   'Calculate profit and loss percentages',
   'Understand the concept of discounting and its calculation',
   'Understand the concept of marked price and its calculation',
   'Understand the relationship among selling price, discount and marked price',
 ],
 'secs': [
  {'n': '9.1', 't': 'Introduction', 'b': [
    {'p': 'The branch of business mathematics that deals with the study of profit and loss in a '
          'business transaction is known as **profit and loss**. In the accounting world, the '
          'summary of a business\'s trading transactions showing whether it made a profit or '
          'loss during a period of account is found in the profit and loss account.'},
  ]},

  {'n': '9.2', 't': 'Concept of profit and loss', 'b': [
    {'p': 'The fundamental objective of any business is to make a profit. **Profit** is the '
          'amount gained by selling an item for more than its cost price; **loss** is the '
          'amount lost by selling an item for less than its cost price. The final selling price '
          'of a product is the difference between the marked price and the discount.'},
    {'def': {'t': 'Cost price (CP)', 'd': 'the price at which an item is purchased by the '
             'buyer, or the amount paid by a consumer to the wholesaler/manufacturer to acquire '
             'goods. It splits into **fixed cost** (constant, does not vary) and **variable '
             'cost** (varies with other factors and the number of units).'}},
    {'def': {'t': 'Selling price (SP)', 'd': 'the price at which an item is sold to the buyer '
             'by the seller — in effect, the sum of the cost price and the target gross '
             'profit.'}},
    {'p': 'When SP is greater than CP, the seller has made a **profit**; when SP is less than '
          'CP, the seller has incurred a **loss**. The comparison of CP with SP is always made '
          'first to know which applies.'},
    {'fbox': {'h': 'Profit and loss percentage (both on cost price)', 'rows': [
      {'lb': 'Profit %', 'tex': '\\text{Profit\\%} = \\frac{\\text{SP} - \\text{CP}}{\\text{CP}} '
             '\\times 100 = \\frac{\\text{Profit}}{\\text{CP}} \\times 100'},
      {'lb': 'Loss %', 'tex': '\\text{Loss\\%} = \\frac{\\text{CP} - \\text{SP}}{\\text{CP}} '
             '\\times 100 = \\frac{\\text{Loss}}{\\text{CP}} \\times 100'},
    ]}},
    {'note': 'If an item is sold at a profit of $x\\%$, then $\\text{SP} = (100+x)\\%$ of CP; if '
             'sold at a loss of $x\\%$, then $\\text{SP} = (100-x)\\%$ of CP.'},
    {'eg': {'tag': 'Study text', 't': 'Example 9.1 — a straight profit', 'open': True, 'q': [
      {'p': 'A petty trader bought an article for ₦1,500 and sold it for ₦1,800. Calculate the '
            'trader\'s profit or loss.'}],
      'a': [
      {'p': 'Since SP $>$ CP, the trader made a profit.'},
      {'tex': '\\text{Profit} = \\text{SP} - \\text{CP} = 1{,}800 - 1{,}500 = \\text{\\textnaira}300'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 9.2 — percentage loss', 'open': True, 'q': [
      {'p': 'A fruit seller bought 5 baskets of oranges at ₦1,200 per basket and sold them for '
            '₦1,100 per basket. Calculate the percentage loss.'}],
      'a': [
      {'tex': '\\text{CP} = 5 \\times 1{,}200 = \\text{\\textnaira}6{,}000 \\qquad '
              '\\text{SP} = 5 \\times 1{,}100 = \\text{\\textnaira}5{,}500'},
      {'p': 'Since CP $>$ SP, a loss was incurred:'},
      {'tex': '\\text{Loss} = 6{,}000 - 5{,}500 = 500 \\qquad '
              '\\text{Loss\\%} = \\frac{500}{6{,}000} \\times 100 = 8.33\\%'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 9.3 — selling price from a loss percentage',
      'open': True, 'q': [
      {'p': 'A motor spare-parts dealer buys a cooling fan for ₦12,000 and sells it at a loss of '
            '7.5%. What is the selling price?'}],
      'a': [
      {'p': 'CP is 100%; SP is $(100 - 7.5)\\% = 92.5\\%$ of CP.'},
      {'tex': '\\text{SP} = \\frac{\\text{CP} \\times 92.5}{100} = '
              '\\frac{12{,}000 \\times 92.5}{100} = \\text{\\textnaira}11{,}100'}]}},
  ]},

  {'n': '9.3', 't': 'Discounting', 'b': [
    {'def': {'t': 'Discount', 'd': 'a reduction given on the marked price of an item, usually '
             'to attract customers and increase sales; also given to clear out old inventory '
             'and create space for new stock, or to encourage early payment.'}},
    {'p': 'The price of a product **after** a discount is always taken as the selling price of '
          'the product.'},
    {'fbox': {'h': 'Discount formulas', 'rows': [
      {'lb': 'Discount from a rate', 'tex': '\\text{Discount} = \\text{Discount\\%} \\text{ of '
             'Marked price}'},
      {'lb': 'Discount from prices', 'tex': '\\text{Discount} = \\text{Marked price (MP)} - '
             '\\text{Actual selling price (SP)}'},
      {'lb': 'Discount percentage', 'tex': '\\text{Discount\\%} = \\frac{\\text{Discount}}'
             '{\\text{Marked price}} \\times 100'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 9.4 — discount percentage from prices',
      'open': True, 'q': [
      {'p': 'A bicycle marked at ₦25,000 was sold for ₦23,000. Calculate the discount percent '
            'given by the seller.'}],
      'a': [
      {'tex': '\\text{Discount} = 25{,}000 - 23{,}000 = \\text{\\textnaira}2{,}000'},
      {'tex': '\\text{Discount\\%} = \\frac{2{,}000}{25{,}000} \\times 100 = 8\\%'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 9.5 — discount amount from a rate', 'open': True,
      'q': [
      {'p': 'A wedding gown marked at ₦45,000 was sold at a discount of 15%. Calculate the '
            'discount given.'}],
      'a': [
      {'tex': '\\text{Discount} = \\frac{15 \\times 45{,}000}{100} = \\text{\\textnaira}6{,}750'}]}},
  ]},

  {'n': '9.4', 't': 'Marked price', 'b': [
    {'def': {'t': 'Marked price (MP)', 'd': 'the price quoted on a product, appearing as a '
             'label — also called market price, retail price or list price. It is the price on '
             'which discount is normally given, and is set at a specific percentage above the '
             'cost price. It may or may not equal the selling price: if a product is sold at '
             'its marked price, MP and SP are the same and no discount was offered.'}},
    {'tex': '\\text{Marked price (MP)} = \\text{Selling price (SP)} + \\text{Discount}',
     'tag': '(9.1)'},
    {'eg': {'tag': 'Study text', 't': 'Example 9.6 — marked price from a selling price and a '
      'discount rate', 'open': True, 'q': [
      {'p': 'A dress is sold for ₦9,000 after a discount of 10% is allowed. Calculate its '
            'marked price.'}],
      'a': [
      {'p': 'Let MP be the marked price. $\\text{MP} = \\text{SP} + 10\\%$ of MP:'},
      {'tex': '\\text{MP} = 9{,}000 + 0.1\\,\\text{MP} \\;\\Rightarrow\\; 0.9\\,\\text{MP} = '
              '9{,}000 \\;\\Rightarrow\\; \\text{MP} = \\frac{9{,}000}{0.9} = '
              '\\text{\\textnaira}10{,}000'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 9.7 — marked price from a cost, a profit rate '
      'and a discount rate', 'open': True, 'q': [
      {'p': 'A retailer allows a discount of 15% on a product to customers and still makes a '
            'profit of 25%. Calculate the marked price of the product, which costs the retailer '
            '₦2,500.'}],
      'a': [
      {'p': 'First find the selling price the 25% profit requires:'},
      {'tex': '\\text{SP} = \\frac{\\text{CP}(100+25)}{100} = \\frac{2{,}500 \\times 125}{100} '
              '= \\text{\\textnaira}3{,}125'},
      {'p': 'That SP must also equal marked price less a 15% discount, $\\text{SP} = 0.85\\,'
            '\\text{MP}$:'},
      {'tex': '\\text{MP} = \\frac{3{,}125}{0.85} = \\text{\\textnaira}3{,}676.47'}]}},
  ]},

  {'n': '9.5', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§9.2 Concept of profit and loss** — CP and SP defined; profit if $\\text{SP}>\\text{CP}$, '
      'loss if $\\text{SP}<\\text{CP}$; $\\text{Profit\\%}=(\\text{SP}-\\text{CP})/\\text{CP}'
      '\\times100$, $\\text{Loss\\%}=(\\text{CP}-\\text{SP})/\\text{CP}\\times100$ — **both on '
      'cost price**. At a profit of $x\\%$, $\\text{SP}=(100+x)\\%$ of CP; at a loss of $x\\%$, '
      '$\\text{SP}=(100-x)\\%$ of CP.',
      '**§9.3 Discounting** — a reduction on the marked price; '
      '$\\text{Discount}=\\text{Discount\\%}\\times\\text{MP}=\\text{MP}-\\text{SP}$; '
      '$\\text{Discount\\%}=\\text{Discount}/\\text{MP}\\times100$. The price after discount '
      '**is** the selling price.',
      '**§9.4 Marked price** — set at a percentage above cost; '
      '$\\text{MP}=\\text{SP}+\\text{Discount}$. Where both a profit rate (on cost) and a '
      'discount rate (on MP) are given, find SP from CP and the profit rate first, then MP from '
      'SP and the discount rate.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Cost price (CP)** — the price paid to acquire the item; **fixed cost** (constant) plus '
      '**variable cost** (varies with output/other factors).',
      '**Selling price (SP)** — the price the item is actually sold for; $=\\text{CP}+$ target '
      'gross profit.',
      '**Profit** — the excess of SP over CP. **Loss** — the shortfall of SP below CP.',
      '**Profit % / Loss %** — profit or loss as a percentage of **cost price**.',
      '**Discount** — a rebate off the marked price.',
      '**Marked price (MP)** — the labelled price, also called market price, retail price or '
      'list price; the base on which discount is calculated.',
    ]},
    {'fbox': {'h': 'Every formula in this chapter', 'rows': [
      {'lb': 'Profit', 'tex': '\\text{Profit} = \\text{SP} - \\text{CP}'},
      {'lb': 'Loss', 'tex': '\\text{Loss} = \\text{CP} - \\text{SP}'},
      {'lb': 'Profit %', 'tex': '\\text{Profit\\%} = \\dfrac{\\text{SP}-\\text{CP}}{\\text{CP}} '
             '\\times 100'},
      {'lb': 'Loss %', 'tex': '\\text{Loss\\%} = \\dfrac{\\text{CP}-\\text{SP}}{\\text{CP}} '
             '\\times 100'},
      {'lb': 'SP from CP and profit $x\\%$', 'tex': '\\text{SP} = \\dfrac{(100+x)}{100}\\,'
             '\\text{CP}'},
      {'lb': 'SP from CP and loss $x\\%$', 'tex': '\\text{SP} = \\dfrac{(100-x)}{100}\\,'
             '\\text{CP}'},
      {'lb': 'Discount', 'tex': '\\text{Discount} = \\text{MP} - \\text{SP} = '
             '\\text{Discount\\%} \\times \\text{MP}'},
      {'lb': 'Discount %', 'tex': '\\text{Discount\\%} = \\dfrac{\\text{Discount}}{\\text{MP}} '
             '\\times 100'},
      {'lb': 'Marked price identity', 'tex': '\\text{MP} = \\text{SP} + \\text{Discount}'},
    ]}},
  ]},

  {'n': '9.6', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'A storekeeper bought a used car for ₦90,000 and sold it for ₦81,000. What is the '
        'storekeeper\'s profit or loss %? (A) 9% loss  (B) 9% profit  (C) 10% loss  '
        '(D) 10% profit  (E) 15% profit',
        'Which of the following represents the relationship among marked price (MP), selling '
        'price (SP) and discount (D)? (A) SP = MP − D  (B) MP = SP − D  (C) SP = MP + D  '
        '(D) MP = SP − D  (E) D = MP − SP',
        'A fruit seller sold a basket of oranges for ₦3,000 at a profit of 10%. What is the cost '
        'price of the basket of oranges? (A) ₦300  (B) ₦700  (C) ₦2,700  (D) ₦2,727  (E) ₦3,300',
        'The formula to find the selling price (SP) of an item, given the cost price (CP) and '
        'the loss% (say $x\\%$), is (A) $\\text{SP}=(100+x)\\%$ of CP  '
        '(B) $\\text{SP}=(100-x)\\%$ of CP  (C) $\\text{SP}=x\\%$ of CP  '
        '(D) $\\text{SP}=\\text{CP}+(100-x)\\%$ of CP  '
        '(E) $\\text{SP}=\\text{CP}-(100+x)\\%$ of CP',
        'A dozen crates of egg at marked price ₦8,000 are available at a discount of 10%. How '
        'many crates of eggs can be bought for ₦2,400? (A) 2  (B) 4  (C) 6  (D) 8  (E) 10',
      ]},
      {'p': 'Short answer:'},
      {'ol': [
        'The marked price of an item is also known as …',
        'A trader is said to have incurred a loss by selling a product if the selling price is '
        '… the cost price.',
        'Discount is the reduction given on the … of an item.',
        'The selling price of a product is the difference between the … and … .',
        'When the marked price of a product equals its selling price then … was given on the '
        'product.',
      ]}],
      'a': [
      {'ol': [
        '**C — 10% loss.** $(90{,}000-81{,}000)/90{,}000 \\times 100 = 10\\%$.',
        '**A — SP = MP − D.**',
        '**E — ₦3,300.** $\\text{CP} = \\dfrac{100}{110}\\times3{,}000 = 2{,}727.27$ — the study '
        'text\'s own printed answer is E; the more precise arithmetic gives ₦2,727 (option D), '
        'so double-check this one against your own working.',
        '**B — $\\text{SP}=(100-x)\\%$ of CP.**',
        '**B — 4.** Discounted price per dozen $= 8{,}000\\times0.9 = 7{,}200$, i.e. ₦600/crate; '
        '$2{,}400\\div600=4$ crates.',
      ]},
      {'ol': [
        'Market price, retail price or list price.',
        'Less than.',
        'Marked price (market price / retail price / list price).',
        'Marked price and discount (in that order).',
        'No discount.',
      ]}]}},
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
 ],
 'focus':
   'One or two Section A marks nearly every diet: a straight profit/loss % on cost, a discount '
   'percentage, or working back from a stated profit and discount rate to find the marked price '
   '(Example 9.7\'s pattern — find SP from CP first, then MP from SP). Always confirm a stated '
   'percentage is on **cost price**, since this chapter never expresses profit or loss on sales.',
 'errors': [
   'Expressing profit or loss as a percentage of selling price instead of cost price.',
   'Confusing marked price with selling price when no discount is stated.',
   'Applying the discount rate to the selling price instead of the marked price.',
   'In a combined profit-then-discount question, solving for MP before first finding SP from CP.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Goods costing ₦60,000 are sold at a profit of 20% on cost. The selling price is',
    'o': ['₦48,000', '₦72,000', '₦75,000', '₦12,000', '₦50,000'],
    'a': 1,
    'w': 'Profit % in this chapter is always on cost price, so add 20% of ₦60,000 to the cost.',
    'calc': '\\text{SP} = 60{,}000 \\times 1.20 = \\text{\\textnaira}72{,}000',
    'src': 'Chapter 9.2', 'sec': '9.2'},
   {'q': 'An article costing ₦2,500 is sold for ₦2,000. The loss as a percentage of cost is',
    'o': ['25%', '20%', '15%', '10%', '80%'],
    'a': 1,
    'w': 'The loss is ₦500, expressed on the cost price of ₦2,500.',
    'calc': '\\text{Loss\\%} = \\frac{500}{2{,}500} \\times 100 = 20\\%',
    'src': 'Chapter 9.2', 'sec': '9.2'},
   {'q': 'A television marked at ₦150,000 is sold for ₦127,500. The discount percentage is',
    'o': ['15%', '17.6%', '22.5%', '12.5%', '10%'],
    'a': 0,
    'w': 'Discount = MP − SP, expressed as a percentage of MP.',
    'calc': '\\text{Discount\\%} = \\frac{150{,}000-127{,}500}{150{,}000} \\times 100 = 15\\%',
    'src': 'Chapter 9.3', 'sec': '9.3'},
   {'q': 'A shirt is sold for ₦6,000 after a discount of 20% is allowed on the marked price. '
         'The marked price was',
    'o': ['₦7,200', '₦7,500', '₦6,500', '₦4,800', '₦8,000'],
    'a': 1,
    'w': '$\\text{MP} = \\text{SP} + 20\\%$ of MP, so $0.8\\,\\text{MP} = \\text{SP}$.',
    'calc': '\\text{MP} = \\frac{6{,}000}{0.8} = \\text{\\textnaira}7{,}500',
    'src': 'Chapter 9.4', 'sec': '9.4'},
   {'q': 'A retailer allows a discount of 10% on an item and still makes a profit of 15% on a '
         'cost of ₦4,000. The marked price is approximately',
    'o': ['₦4,600', '₦5,111', '₦5,111.11', '₦4,400', '₦5,000'],
    'a': 2,
    'w': 'First find SP from CP and the profit rate, then MP from SP and the discount rate.',
    'calc': '\\text{SP} = 4{,}000 \\times 1.15 = 4{,}600; \\quad '
            '\\text{MP} = \\frac{4{,}600}{0.9} = \\text{\\textnaira}5{,}111.11',
    'src': 'Chapter 9.4', 'sec': '9.4'},
  ],
  'theory': [
   {'q': 'A trader buys goods for ₦18,000 and wishes to mark them up so that, after allowing a '
         'discount of 10% on the marked price, he still makes a profit of 25% on cost. '
         'Calculate (a) the required selling price and (b) the marked price.',
    'marks': 6,
    'a': [
      {'h4': '(a) Selling price required'},
      {'tex': '\\text{SP} = \\text{CP} \\times \\frac{100+25}{100} = 18{,}000 \\times 1.25 = '
              '\\text{\\textnaira}22{,}500'},
      {'h4': '(b) Marked price'},
      {'p': 'The selling price is the marked price less the 10% discount, so '
            '$\\text{SP} = 0.9\\,\\text{MP}$:'},
      {'tex': '\\text{MP} = \\frac{22{,}500}{0.9} = \\text{\\textnaira}25{,}000'},
      {'note': 'Always find the required **selling price** from cost and profit% first; only '
               'then work back to the **marked price** using the discount%, exactly as in the '
               'study text\'s own Example 9.7.'}],
    'src': 'Chapter 9.4', 'sec': '9.4'},
  ]},
}
