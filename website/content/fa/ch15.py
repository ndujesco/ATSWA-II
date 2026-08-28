CH = {
 'n': 15,
 't': 'Interpretation of Financial Statements',
 'brief': 'Ratio analysis: profitability, efficiency, liquidity, gearing and investor ratios, what '
          'each one is really telling you, and what ratios cannot tell you at all.',
 'outcomes': [
   'Compute the principal profitability, efficiency, liquidity, gearing and investor ratios',
   'Interpret a movement in a ratio rather than merely reporting it',
   'Explain the relationship between ROCE, margin and asset turnover',
   'Apply horizontal, vertical and inter-company analysis',
   'State the limitations of ratio analysis',
 ],
 'secs': [
  {'n': '15.1', 't': 'Tools of analysis', 'b': [
    {'ul': [
      '**Horizontal (trend) analysis** — the same line item compared across periods, often '
      'indexed to a base year of 100.',
      '**Vertical (common size) analysis** — every line expressed as a percentage of a base: '
      'revenue for the statement of profit or loss, total assets for the statement of financial '
      'position. It makes entities of different sizes comparable.',
      '**Ratio analysis** — relationships between figures.',
      '**Inter-company and inter-firm comparison** — against a competitor or an industry average.',
    ]},
    {'key': 'A ratio on its own means nothing. It acquires meaning only against a **comparator**: '
            'the prior year, a competitor, an industry average, or a budget. Every interpretation '
            'answer should name the comparator being used.'},
  ]},

  {'n': '15.2', 't': 'Profitability', 'b': [
    {'fbox': {'h': 'Profitability ratios', 'rows': [
      {'lb': 'Gross profit margin',
       'tex': '\\frac{\\text{Gross profit}}{\\text{Revenue}} \\times 100',
       'nt': 'Moves with selling prices, purchase costs and sales mix.'},
      {'lb': 'Operating (net) profit margin',
       'tex': '\\frac{\\text{Operating profit}}{\\text{Revenue}} \\times 100',
       'nt': 'A gap between this and the gross margin points at overheads.'},
      {'lb': 'Return on capital employed (ROCE)',
       'tex': '\\frac{\\text{Operating profit}}{\\text{Capital employed}} \\times 100',
       'nt': 'Capital employed = equity + non-current liabilities, or total assets − current liabilities.'},
      {'lb': 'Return on equity (ROE)',
       'tex': '\\frac{\\text{Profit after tax and preference dividend}}{\\text{Ordinary '
              'shareholders\' funds}} \\times 100'},
      {'lb': 'Return on assets',
       'tex': '\\frac{\\text{Operating profit}}{\\text{Total assets}} \\times 100'},
    ]}},
    {'p': 'ROCE is the primary measure of performance, and it decomposes into two ratios that '
          'together explain any change in it:'},
    {'tex': '\\underbrace{\\frac{\\text{Operating profit}}{\\text{Capital employed}}}'
            '_{\\text{ROCE}} = \\underbrace{\\frac{\\text{Operating profit}}{\\text{Revenue}}}'
            '_{\\text{margin}} \\times \\underbrace{\\frac{\\text{Revenue}}'
            '{\\text{Capital employed}}}_{\\text{asset turnover}}', 'tag': '(15.1)'},
    {'note': 'This identity is worth marks on its own. A supermarket earns its ROCE through high '
             'asset turnover on a thin margin; a jeweller through a fat margin on slow turnover. '
             'Both can reach the same ROCE, and saying so shows you understand the business '
             'rather than the arithmetic.'},
  ]},

  {'n': '15.3', 't': 'Efficiency', 'b': [
    {'fbox': {'h': 'Efficiency (activity) ratios', 'rows': [
      {'lb': 'Inventory turnover',
       'tex': '\\frac{\\text{Cost of sales}}{\\text{Average inventory}} \\text{ times}'},
      {'lb': 'Inventory days',
       'tex': '\\frac{\\text{Average inventory}}{\\text{Cost of sales}} \\times 365'},
      {'lb': 'Receivables collection period',
       'tex': '\\frac{\\text{Trade receivables}}{\\text{Credit sales}} \\times 365 \\text{ days}'},
      {'lb': 'Payables payment period',
       'tex': '\\frac{\\text{Trade payables}}{\\text{Credit purchases}} \\times 365 \\text{ days}'},
      {'lb': 'Asset turnover',
       'tex': '\\frac{\\text{Revenue}}{\\text{Capital employed}} \\text{ times}'},
    ]}},
    {'tex': '\\text{Working capital (cash operating) cycle} = \\text{Inventory days} '
            '+ \\text{Receivables days} - \\text{Payables days}', 'tag': '(15.2)'},
    {'p': 'The cycle is the number of days between paying for goods and being paid for them. The '
          'longer it is, the more working capital the business must finance.'},
    {'warn': 'Use **cost of sales** for inventory ratios and **credit sales** for the collection '
             'period. Using revenue for inventory days is a standard error and inflates the '
             'answer by the whole gross margin.'},
  ]},

  {'n': '15.4', 't': 'Liquidity and gearing', 'b': [
    {'fbox': {'h': 'Liquidity and gearing', 'rows': [
      {'lb': 'Current ratio',
       'tex': '\\frac{\\text{Current assets}}{\\text{Current liabilities}} : 1'},
      {'lb': 'Acid test (quick) ratio',
       'tex': '\\frac{\\text{Current assets} - \\text{Inventory}}{\\text{Current liabilities}} : 1',
       'nt': 'Inventory is the least liquid current asset, so it is stripped out.'},
      {'lb': 'Gearing (debt to equity)',
       'tex': '\\frac{\\text{Long-term debt}}{\\text{Equity}} \\times 100'},
      {'lb': 'Gearing (debt to capital employed)',
       'tex': '\\frac{\\text{Long-term debt}}{\\text{Debt} + \\text{Equity}} \\times 100'},
      {'lb': 'Interest cover',
       'tex': '\\frac{\\text{Profit before interest and tax}}{\\text{Finance costs}} '
              '\\text{ times}'},
    ]}},
    {'p': 'A current ratio around 2 : 1 and an acid test around 1 : 1 are conventional rules of '
          'thumb, but they are only that. A supermarket sells for cash and buys on credit, so it '
          'operates safely on an acid test well below 1 : 1.'},
    {'note': 'High gearing magnifies returns to equity in good years and losses in bad ones, and '
             'raises the risk of not meeting interest. Interest cover below about 3 times is '
             'generally regarded as uncomfortable.'},
  ]},

  {'n': '15.5', 't': 'Investor ratios', 'b': [
    {'fbox': {'h': 'Investor ratios', 'rows': [
      {'lb': 'Earnings per share',
       'tex': '\\text{EPS} = \\frac{\\text{Profit after tax and preference dividend}}'
              '{\\text{Weighted average number of ordinary shares}}'},
      {'lb': 'Price/earnings ratio',
       'tex': '\\text{P/E} = \\frac{\\text{Market price per share}}{\\text{EPS}}',
       'nt': 'A high P/E signals the market expects growth.'},
      {'lb': 'Dividend per share',
       'tex': '\\text{DPS} = \\frac{\\text{Ordinary dividend}}{\\text{Number of ordinary shares}}'},
      {'lb': 'Dividend cover',
       'tex': '\\frac{\\text{EPS}}{\\text{DPS}} \\text{ times}'},
      {'lb': 'Dividend yield',
       'tex': '\\frac{\\text{DPS}}{\\text{Market price per share}} \\times 100'},
    ]}},
  ]},

  {'n': '15.6', 't': 'A worked interpretation', 'b': [
    {'eg': {'t': 'Computing and interpreting', 'q': [
      {'p': 'The summarised results of Bayo Plc are:'},
      {'table': {'align': 'lrr', 'head': ['(₦\'000)', '2024', '2023'], 'rows': [
        ['Revenue (all on credit)', '48,000', '40,000'],
        ['Cost of sales', '33,600', '26,000'],
        ['Operating profit', '5,760', '5,600'],
        ['Finance costs', '960', '480'],
        ['Inventory', '5,600', '3,900'],
        ['Trade receivables', '9,200', '6,300'],
        ['Cash', '400', '1,900'],
        ['Trade payables', '6,100', '4,700'],
        ['Equity', '24,000', '22,000'],
        ['Long-term loans', '12,000', '6,000'],
      ]}},
      {'p': 'Compute the gross margin, ROCE, current ratio, acid test, receivables days, '
            'inventory days and gearing for both years, and comment.'}],
      'a': [
      {'table': {'align': 'lrrl', 'head': ['Ratio', '2024', '2023', 'Working (2024)'], 'rows': [
        ['Gross margin', '30.0%', '35.0%', '(48,000 − 33,600) ÷ 48,000'],
        ['Operating margin', '12.0%', '14.0%', '5,760 ÷ 48,000'],
        ['ROCE', '16.0%', '20.0%', '5,760 ÷ (24,000 + 12,000)'],
        ['Asset turnover', '1.33×', '1.43×', '48,000 ÷ 36,000'],
        ['Current ratio', '2.49 : 1', '2.57 : 1', '(5,600 + 9,200 + 400) ÷ 6,100'],
        ['Acid test', '1.57 : 1', '1.74 : 1', '(9,200 + 400) ÷ 6,100'],
        ['Receivables days', '70 days', '57 days', '9,200 ÷ 48,000 × 365'],
        ['Inventory days', '61 days', '55 days', '5,600 ÷ 33,600 × 365'],
        ['Gearing (D/E)', '50.0%', '27.3%', '12,000 ÷ 24,000'],
        ['Interest cover', '6.0×', '11.7×', '5,760 ÷ 960'],
      ]}},
      {'h4': 'Comment'},
      {'p': '**Profitability has fallen despite revenue growing 20%.** The gross margin dropped '
            'five points, which means the extra revenue was bought with price cuts or was hit by '
            'rising input costs. Because the operating margin fell by only two points, overheads '
            'were actually controlled better than sales prices were — the problem is at the '
            'trading level, not the overhead level.'},
      {'p': '**ROCE fell from 20% to 16%,** and identity (15.1) shows why: margin fell from 14% to '
            '12% and asset turnover from 1.43 to 1.33. Both components deteriorated, so the '
            'additional capital raised has not yet earned what the existing capital was earning.'},
      {'p': '**Liquidity looks adequate but is deteriorating.** The current ratio is broadly '
            'stable, but that conceals the real movement: cash fell from ₦1.9m to ₦0.4m while '
            'inventory and receivables both rose sharply. Receivables days rose 13 days and '
            'inventory days 6 days — working capital is absorbing the cash that the extra sales '
            'generated.'},
      {'p': '**Financial risk has risen materially.** Gearing nearly doubled and interest cover '
            'halved from 11.7 to 6.0 times. Cover is still comfortable, but the direction is what '
            'matters: another year like this one would take it close to the level at which '
            'lenders become anxious.'},
      {'note': 'Notice the shape of a good interpretation answer. Each paragraph **names the '
               'movement, quantifies it, and offers a business reason for it**. Simply listing '
               '"gross margin fell from 35% to 30%" earns the computation mark but not the '
               'interpretation mark, and interpretation is usually where half the marks are.'}]}},
  ]},

  {'n': '15.7', 't': 'Limitations of ratio analysis', 'b': [
    {'ol': [
      'Ratios are based on **historical** figures and say nothing directly about the future.',
      'Financial statements reflect **accounting policy choices** — depreciation method, '
      'inventory formula, revaluation policy — so two entities may not be comparable.',
      'A statement of financial position is a **snapshot at one date** and may be unrepresentative, '
      'especially in a seasonal business, and may have been window-dressed.',
      'They ignore **non-financial factors**: quality of management, staff morale, customer '
      'loyalty, brand strength, regulatory risk.',
      '**Inflation** distorts comparisons over time, since assets are carried at different price levels.',
      'Different entities **define** ratios differently (capital employed especially), so '
      'published comparisons must be read carefully.',
      'A **diversified** group\'s aggregate ratios may describe no actual business it operates.',
      'They show **what** has happened, not **why**; the cause must come from elsewhere.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': 'Gross profit margin', 'tex': '\\frac{\\text{Gross profit}}{\\text{Revenue}} \\times 100'},
  {'lb': 'Return on capital employed',
   'tex': '\\text{ROCE} = \\frac{\\text{Operating profit}}{\\text{Equity} + \\text{Non-current '
          'liabilities}} \\times 100'},
  {'lb': 'ROCE decomposition',
   'tex': '\\text{ROCE} = \\text{Operating margin} \\times \\text{Asset turnover}'},
  {'lb': 'Current ratio',
   'tex': '\\frac{\\text{Current assets}}{\\text{Current liabilities}}'},
  {'lb': 'Acid test',
   'tex': '\\frac{\\text{Current assets} - \\text{Inventory}}{\\text{Current liabilities}}'},
  {'lb': 'Receivables days',
   'tex': '\\frac{\\text{Trade receivables}}{\\text{Credit sales}} \\times 365'},
  {'lb': 'Inventory days',
   'tex': '\\frac{\\text{Inventory}}{\\text{Cost of sales}} \\times 365'},
  {'lb': 'Working capital cycle',
   'tex': '\\text{Inventory days} + \\text{Receivables days} - \\text{Payables days}'},
  {'lb': 'Gearing', 'tex': '\\frac{\\text{Long-term debt}}{\\text{Equity}} \\times 100'},
  {'lb': 'Interest cover', 'tex': '\\frac{\\text{PBIT}}{\\text{Finance costs}}'},
  {'lb': 'Earnings per share',
   'tex': '\\text{EPS} = \\frac{\\text{Profit after tax and preference dividend}}'
          '{\\text{Weighted average ordinary shares}}'},
 ],
 'focus':
   'A regular Section B question, and an unusually forgiving one because half the marks are for '
   'commentary that does not depend on getting every ratio right. Compute the ratios, then write '
   'a paragraph per group naming the movement, quantifying it and giving a business reason. Learn '
   'the ROCE decomposition — it turns a list of numbers into an argument. Section A tests single '
   'ratio computations and the definition of capital employed.',
 'errors': [
   'Using revenue instead of cost of sales in inventory ratios.',
   'Reporting a ratio without a comparator, so there is nothing to interpret.',
   'Listing movements without explaining them. "Gross margin fell" is not interpretation.',
   'Using total liabilities rather than long-term debt in gearing without saying so.',
   'Computing receivables days on total revenue when the question distinguishes cash and credit sales.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Revenue is ₦500,000,000 and gross profit ₦200,000,000. The gross profit margin is',
    'o': ['20%', '25%', '40%', '60%', '250%'],
    'a': 2,
    'w': 'Gross profit margin expresses gross profit as a percentage of revenue.',
    'calc': '\\frac{200{,}000{,}000}{500{,}000{,}000} \\times 100 = 40\\%',
    'src': 'Chapter 15.2'},
   {'q': 'Current assets ₦8,400,000, of which inventory ₦3,200,000; current liabilities '
         '₦4,000,000. The acid test ratio is',
    'o': ['2.10 : 1', '1.30 : 1', '0.80 : 1', '1.05 : 1', '2.63 : 1'],
    'a': 1,
    'w': 'The acid test excludes inventory, the least liquid current asset.',
    'calc': '\\frac{8{,}400{,}000 - 3{,}200{,}000}{4{,}000{,}000} = \\frac{5{,}200{,}000}'
            '{4{,}000{,}000} = 1.30',
    'src': 'Chapter 15.4'},
   {'q': 'Operating profit is ₦9,000,000, revenue ₦60,000,000 and capital employed ₦45,000,000. '
         'ROCE is',
    'o': ['15%', '20%', '13.3%', '75%', '6.7%'],
    'a': 1,
    'w': 'ROCE is operating profit over capital employed. Note the decomposition: margin 15% × '
         'asset turnover 1.33 = 20%.',
    'calc': '\\frac{9{,}000{,}000}{45{,}000{,}000} \\times 100 = 20\\%',
    'src': 'Chapter 15.2'},
   {'q': 'Trade receivables are ₦7,300,000 and credit sales ₦36,500,000. The collection period is',
    'o': ['20 days', '50 days', '73 days', '146 days', '5 days'],
    'a': 2,
    'w': 'Receivables days measures how long customers take to pay.',
    'calc': '\\frac{7{,}300{,}000}{36{,}500{,}000} \\times 365 = 73 \\text{ days}',
    'src': 'Chapter 15.3'},
   {'q': 'Inventory days are 48, receivables days 62 and payables days 39. The working capital '
         'cycle is',
    'o': ['149 days', '71 days', '25 days', '53 days', '101 days'],
    'a': 1,
    'w': 'The cycle is the time between paying suppliers and being paid by customers.',
    'calc': '48 + 62 - 39 = 71 \\text{ days}',
    'src': 'Chapter 15.3'},
   {'q': 'Which of the following is NOT a limitation of ratio analysis?',
    'o': ['Ratios are based on historical information',
          'Different entities may use different accounting policies',
          'Ratios summarise relationships in a single figure that is easy to compare',
          'Ratios ignore non-financial factors such as management quality',
          'A statement of financial position may be unrepresentative of the year'],
    'a': 2,
    'w': 'Reducing a relationship to one comparable figure is the point of a ratio — it is the '
         'principal advantage, not a limitation.',
    'src': 'Chapter 15.7'},
  ],
  'theory': [
   {'q': 'Explain the relationship between return on capital employed, profit margin and asset '
         'turnover, and explain how two businesses in different industries can earn the same ROCE '
         'by different routes.',
    'marks': 6,
    'a': [
      {'p': 'Return on capital employed decomposes into two ratios whose product it is:'},
      {'tex': '\\frac{\\text{Operating profit}}{\\text{Capital employed}} = '
              '\\frac{\\text{Operating profit}}{\\text{Revenue}} \\times '
              '\\frac{\\text{Revenue}}{\\text{Capital employed}}'},
      {'p': 'Revenue cancels, so the identity holds exactly. **Margin** measures how much profit '
            'each naira of sales produces; **asset turnover** measures how much sales each naira '
            'of capital produces. A change in ROCE must be traceable to one or both.'},
      {'p': '**A supermarket** operates on a very thin margin — perhaps 3% — but turns its capital '
            'over many times a year because inventory moves quickly and customers pay in cash. '
            'Margin 3% × turnover 6 gives ROCE of 18%.'},
      {'p': '**A jeweller** carries slow-moving, high-value inventory and turns capital over less '
            'than once a year, but earns a margin of perhaps 25%. Margin 25% × turnover 0.72 gives '
            'ROCE of 18% as well.'},
      {'p': 'The two businesses are equally profitable on capital, but the routes are opposite, '
            'and the strategic implications differ entirely: the supermarket must protect volume, '
            'the jeweller must protect price. This is why ROCE should always be analysed into its '
            'components rather than reported alone.'}],
    'src': 'Chapter 15.2'},
   {'q': 'State SIX limitations of ratio analysis as a means of interpreting financial statements.',
    'marks': 6,
    'a': [{'ol': [
      '**Historical basis** — ratios describe what has already happened and are not necessarily a '
      'guide to future performance.',
      '**Accounting policy differences** — depreciation methods, inventory cost formulas and '
      'revaluation policies differ between entities, so ratios may not be comparable.',
      '**Snapshot problem** — a statement of financial position shows one date only, which may be '
      'unrepresentative in a seasonal business and may have been window-dressed.',
      '**Non-financial factors ignored** — management quality, staff morale, brand strength, '
      'customer loyalty and regulatory risk do not appear in any ratio.',
      '**Inflation** — comparing figures across years, or assets bought at different times, '
      'compares amounts measured in units of different purchasing power.',
      '**Definitional inconsistency** — capital employed, gearing and even profit are defined '
      'differently by different analysts, so published comparisons must be read with care.',
      '**Diversified entities** — a group\'s aggregate ratios may not describe any of the '
      'businesses it actually operates.',
      '**No causes** — ratios identify that something changed, not why; the explanation must come '
      'from outside the statements.']}],
    'src': 'Chapter 15.7'},
  ]},
}
