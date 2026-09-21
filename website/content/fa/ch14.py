CH = {
 'n': 14,
 't': 'Preparing Financial Statements for Corporate Entities',
 'brief': 'The published statement of profit or loss and statement of financial position, and '
          'the statement of cash flows under IAS 7 by both the direct and the indirect method.',
 'outcomes': [
   'Prepare a statement of profit or loss and other comprehensive income',
   'Prepare a statement of financial position in the required format',
   'Classify cash flows as operating, investing or financing',
   'Prepare a statement of cash flows by the indirect method',
   'Prepare a statement of cash flows by the direct method',
   'State the uses and limitations of the statement of cash flows',
 ],
 'secs': [
  {'n': '14.1', 't': 'The statement of profit or loss', 'b': [
    {'p': 'A **complete set of financial statements** under IAS 1 comprises: a statement of '
          'financial position; a statement of profit or loss and other comprehensive income; a '
          'statement of changes in equity; a statement of cash flows; and **notes to the '
          'financial statements**, comprising significant accounting policies and other '
          'explanatory information. Proposed (not-yet-declared) dividends are disclosed only in '
          'the **notes**, not recognised as a liability, since they are not an obligation at the '
          'reporting date.'},
    {'stmt': {'t': 'Statement of profit or loss and other comprehensive income',
      'sub': 'for the year ended 31 December 2024 (₦\'000)', 'rows': [
      ['Revenue', 486000],
      ['Cost of sales', -292000],
      ['Gross profit', 194000, '@t'],
      ['Other income', 6500],
      ['Distribution costs', -41000],
      ['Administrative expenses', -58000],
      ['Operating profit', 101500, '@t'],
      ['Finance costs', -12000],
      ['Profit before tax', 89500, '@t'],
      ['Income tax expense', -27400],
      ['Profit for the year', 62100, '@tt'],
      '@gap',
      'Other comprehensive income',
      ['Gain on revaluation of property (not reclassified)', 19000],
      ['Total comprehensive income for the year', 81100, '@tt'],
    ]}},
    {'p': 'Expenses may be analysed **by function** (cost of sales, distribution, administrative) '
          'as above, or **by nature** (raw materials, employee benefits, depreciation). Where the '
          'by-function format is used, IAS 1 requires additional disclosure of depreciation, '
          'amortisation and employee benefits expense in the notes.'},
    {'key': 'Items in **other comprehensive income** are split into those that will later be '
            'reclassified to profit or loss and those that will not. A revaluation surplus is '
            'never reclassified; a foreign exchange difference on a foreign operation is.'},
  ]},

  {'n': '14.2', 't': 'The statement of financial position', 'b': [
    {'stmt': {'t': 'Statement of financial position',
      'sub': 'as at 31 December 2024 (₦\'000)', 'rows': [
      'Assets',
      'Non-current assets',
      ['Property, plant and equipment', 281280],
      ['Intangible assets', 24000],
      ['Investments', 15000],
      ['', 320280, '@t'],
      'Current assets',
      ['Inventories', 46500],
      ['Trade and other receivables', 58200],
      ['Prepayments', 3400],
      ['Cash and cash equivalents', 21600],
      ['', 129700, '@t'],
      ['Total assets', 449980, '@tt'],
      '@gap',
      'Equity and liabilities',
      'Equity',
      ['Ordinary share capital', 200000],
      ['Share premium', 30000],
      ['Revaluation surplus', 36457],
      ['Retained earnings', 89523],
      ['', 355980, '@t'],
      'Non-current liabilities',
      ['10% loan notes', 40000],
      'Current liabilities',
      ['Trade and other payables', 26600],
      ['Accruals', 3400],
      ['Current tax payable', 24000],
      ['', 54000, '@t'],
      ['Total equity and liabilities', 449980, '@tt'],
    ]}},
    {'p': 'An asset is **current** if it is expected to be realised within twelve months or within '
          'the normal operating cycle, is held for trading, or is cash. Everything else is '
          'non-current. The same test, mirrored, applies to liabilities.'},
    {'warn': 'The heading matters. A statement of financial position is **as at** a date; a '
             'statement of profit or loss is **for the year ended**. Presentation marks are '
             'awarded for the heading, the currency unit and the comparatives.'},
  ]},

  {'n': '14.3', 't': 'The statement of cash flows: classification', 'b': [
    {'table': {'head': ['Activity', 'Includes'], 'align': 'll', 'rows': [
      ['**Operating**', 'Cash from customers; cash to suppliers and employees; interest and tax '
       'paid (or classified consistently elsewhere); the principal revenue-producing activities'],
      ['**Investing**', 'Purchase and sale of property, plant and equipment and of intangibles; '
       'purchase and sale of investments; interest and dividends received; loans made to others'],
      ['**Financing**', 'Proceeds of issuing shares and loan notes; repayment of borrowings; '
       'dividends paid; payments on lease liabilities'],
    ]}},
    {'note': 'IAS 7 allows interest paid to sit in operating or financing, and interest and '
             'dividends received in operating or investing, provided the classification is applied '
             'consistently and disclosed. Say which you have chosen.'},
    {'def': {'t': 'Cash equivalents', 'd': 'short-term, highly liquid investments readily '
                  'convertible to known amounts of cash and subject to an insignificant risk of '
                  'changes in value — normally with a maturity of three months or less from the '
                  'date of acquisition.'}},
  ]},

  {'n': '14.4', 't': 'The indirect method', 'b': [
    {'p': 'Start from profit before tax and strip out everything that is not an operating cash '
          'flow. There are three groups of adjustment and they always come in the same order.'},
    {'steps': [
      '**Non-cash items** charged or credited in arriving at profit: add back depreciation, '
      'amortisation, impairment and losses on disposal; deduct profits on disposal.',
      '**Items classified elsewhere**: add back finance costs and deduct investment income, '
      'because they belong to financing and investing.',
      '**Movements in working capital**: an increase in inventories or receivables is a cash '
      'outflow; an increase in payables is a cash inflow. Reverse the signs for decreases.',
    ]},
    {'key': 'The working capital rule in one line: **assets up, cash down; liabilities up, cash '
            'up.** If you can recite that you will never get a sign wrong.'},
    {'eg': {'t': 'Statement of cash flows, indirect method', 'q': [
      {'p': 'From the following, prepare the statement of cash flows for the year ended 31 '
            'December 2024.'},
      {'table': {'align': 'lrr', 'head': ['(₦\'000)', '2024', '2023'], 'rows': [
        ['Property, plant and equipment (carrying amount)', '281,280', '288,925'],
        ['Inventories', '46,500', '39,800'],
        ['Trade receivables', '58,200', '61,400'],
        ['Cash and cash equivalents', '93,195', '9,750'],
        ['Trade payables', '26,600', '22,900'],
        ['Current tax payable', '24,000', '19,500'],
        ['10% loan notes', '40,000', '55,000'],
        ['Share capital', '200,000', '160,000'],
        ['Share premium', '30,000', '18,000'],
        ['Retained earnings', '89,523', '55,423'],
      ]}},
      {'ul': [
        'Profit before tax was ₦89,500,000 and the tax charge ₦27,400,000.',
        'Depreciation for the year was ₦29,645,000.',
        'Plant with a carrying amount of ₦6,000,000 was sold for ₦7,400,000.',
        'Finance costs of ₦12,000,000 were charged and paid.',
        'Dividends of ₦28,000,000 were paid.',
      ]}],
      'a': [
      {'h4': 'W1 — additions to property, plant and equipment'},
      {'stmt': {'rows': [
        ['Carrying amount at 1 January', 288925],
        ['Less depreciation', -29645],
        ['Less carrying amount of disposal', -6000],
        ['', 253280, '@t'],
        ['Carrying amount at 31 December', 281280],
        ['Additions (balancing figure)', 28000, '@tt'],
      ]}},
      {'h4': 'W2 — tax paid'},
      {'stmt': {'rows': [
        ['Liability at 1 January', 19500],
        ['Charge for the year', 27400],
        ['', 46900, '@t'],
        ['Liability at 31 December', -24000],
        ['Tax paid', 22900, '@tt'],
      ]}},
      {'h4': 'Statement of cash flows'},
      {'stmt': {'t': 'Statement of cash flows',
        'sub': 'for the year ended 31 December 2024 (₦\'000)', 'rows': [
        'Cash flows from operating activities',
        ['Profit before tax', 89500],
        ['Adjustments for:', ''],
        ['Depreciation', 29645],
        ['Profit on disposal of plant', -1400],
        ['Finance costs', 12000],
        ['Operating profit before working capital changes', 129745, '@t'],
        ['Increase in inventories', -6700],
        ['Decrease in trade receivables', 3200],
        ['Increase in trade payables', 3700],
        ['Cash generated from operations', 129945, '@t'],
        ['Interest paid', -12000],
        ['Income tax paid (W2)', -22900],
        ['Net cash from operating activities', 95045, '@tt'],
        '@gap',
        'Cash flows from investing activities',
        ['Purchase of property, plant and equipment (W1)', -28000],
        ['Proceeds from sale of plant', 7400],
        ['Net cash used in investing activities', -20600, '@tt'],
        '@gap',
        'Cash flows from financing activities',
        ['Proceeds of share issue (40,000 + 12,000)', 52000],
        ['Repayment of loan notes', -15000],
        ['Dividends paid', -28000],
        ['Net cash from financing activities', 9000, '@tt'],
        '@gap',
        ['Net increase in cash and cash equivalents', 83445, '@t'],
        ['Cash and cash equivalents at 1 January', 9750],
        ['Cash and cash equivalents at 31 December', 93195, '@tt'],
      ]}},
      {'key': 'The closing figure of ₦93,195,000 agrees with the cash in the statement of '
               'financial position, so the statement articulates. **Always finish with this '
               'check** — it catches a sign error or an omitted working in seconds. If it fails, '
               'say so and state the difference rather than forcing a balancing figure; examiners '
               'give credit for the check itself.'},
      {'note': 'On the profit on disposal: the whole ₦7,400,000 of proceeds is an **investing** '
               'inflow, so the ₦1,400,000 profit already inside operating profit must be taken '
               'out, or it would be counted twice. A **loss** on disposal is added back for the '
               'same reason.'}]}},
  ]},

  {'n': '14.5', 't': 'The direct method', 'b': [
    {'p': 'The direct method reports the actual operating receipts and payments. IAS 7 encourages '
          'it because it is more informative, but the indirect method is far more common in '
          'practice because the data is easier to extract.'},
    {'tex': '\\text{Cash from customers} = \\text{Revenue} + \\text{Opening receivables} '
            '- \\text{Closing receivables}'},
    {'tex': '\\text{Cash to suppliers} = \\text{Purchases} + \\text{Opening payables} '
            '- \\text{Closing payables}'},
    {'tex': '\\text{Purchases} = \\text{Cost of sales} + \\text{Closing inventory} '
            '- \\text{Opening inventory}'},
    {'eg': {'t': 'Operating section, direct method', 'q': [
      {'p': 'Using the data above, with revenue ₦486,000,000 and cost of sales ₦292,000,000, '
            'compute cash received from customers and cash paid to suppliers.'}],
      'a': [
      {'tex': '\\text{From customers} = 486{,}000 + 61{,}400 - 58{,}200 = ₦489{,}200\\text{k}'},
      {'tex': '\\text{Purchases} = 292{,}000 + 46{,}500 - 39{,}800 = ₦298{,}700\\text{k}'},
      {'tex': '\\text{To suppliers} = 298{,}700 + 22{,}900 - 26{,}600 = ₦295{,}000\\text{k}'},
      {'note': 'The two methods must give the same **net cash from operating activities**. Only '
               'the presentation of the operating section differs; investing and financing are '
               'identical.'}]}},
  ]},

  {'n': '14.6', 't': 'Uses and limitations', 'b': [
    {'h3': 'Why users want it'},
    {'ul': [
      'Cash is harder to manipulate than profit, since it is not affected by accounting policy '
      'choices on depreciation, inventory or provisions.',
      'It shows whether operations actually generate cash, or whether reported profit is being '
      'funded by borrowing.',
      'It shows the entity\'s capacity to pay dividends, service debt and fund investment.',
      'It explains the difference between profit and the movement in the bank balance.',
    ]},
    {'h3': 'Limitations'},
    {'ul': [
      'It is **historic** — it says what happened, not what will happen.',
      'It **ignores non-cash transactions** such as acquiring an asset under a lease or issuing '
      'shares for a business, which may be very significant. These must be disclosed separately.',
      'Cash can be **manipulated by timing** — delaying supplier payments just before the year end '
      'flatters operating cash flow.',
      'It gives no measure of **profitability**, so it must be read with the other statements, '
      'not instead of them.',
    ]},
  ]},
 ],
 'formulas': [
  {'lb': 'Cash received from customers',
   'tex': '\\text{Receipts} = \\text{Revenue} + \\text{Opening receivables} '
          '- \\text{Closing receivables}'},
  {'lb': 'Purchases from cost of sales',
   'tex': '\\text{Purchases} = \\text{COS} + \\text{Closing inventory} - \\text{Opening inventory}'},
  {'lb': 'Cash paid to suppliers',
   'tex': '\\text{Payments} = \\text{Purchases} + \\text{Opening payables} '
          '- \\text{Closing payables}'},
  {'lb': 'Tax paid',
   'tex': '\\text{Paid} = \\text{Opening liability} + \\text{Charge} - \\text{Closing liability}'},
  {'lb': 'Additions to non-current assets',
   'tex': '\\text{Additions} = \\text{Closing CA} - \\text{Opening CA} + \\text{Depreciation} '
          '+ \\text{CA of disposals}'},
 ],
 'focus':
   'The statement of cash flows is one of the two or three most likely Section B questions, worth '
   'the full 15 marks. The marks sit in the workings — additions to non-current assets, tax paid, '
   'dividends paid — at least as much as in the statement itself, so set every one out separately '
   'and label it. Learn the indirect method as a fixed skeleton and fill in the numbers; do not '
   'try to reason it out from scratch under time pressure.',
 'errors': [
   'Getting the working capital signs backwards. Assets up means cash down.',
   'Leaving a profit on disposal inside operating cash flow as well as counting the proceeds in '
   'investing, so double-counting it.',
   'Using the tax charge instead of the tax paid.',
   'Putting dividends paid in operating activities. IAS 7 permits operating or financing, but '
   'financing is the normal presentation and the question usually expects it.',
   'Forgetting to reconcile the closing cash figure to the statement of financial position.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'In a statement of cash flows prepared by the indirect method, an increase in '
         'inventories is',
    'o': ['added to profit before tax', 'deducted from profit before tax',
          'shown as an investing outflow', 'shown as a financing outflow', 'ignored'],
    'a': 1,
    'w': 'Cash has been spent building up inventory, so it is a cash outflow: an increase in a '
         'current asset is deducted.',
    'src': 'Chapter 14.4', 'sec': '14.4'},
   {'q': 'Tax payable was ₦18,000,000 at the start of the year and ₦21,000,000 at the end. The '
         'charge for the year was ₦25,000,000. Tax paid during the year was',
    'o': ['₦25,000,000', '₦22,000,000', '₦28,000,000', '₦21,000,000', '₦18,000,000'],
    'a': 1,
    'w': 'Open a tax T-account: opening liability plus the charge, less the closing liability, '
         'gives the cash paid.',
    'calc': '18{,}000{,}000 + 25{,}000{,}000 - 21{,}000{,}000 = 22{,}000{,}000',
    'src': 'Chapter 14.4', 'sec': '14.4'},
   {'q': 'Which of the following is a financing activity under IAS 7?',
    'o': ['Purchase of a delivery vehicle', 'Receipt of a dividend from an investment',
          'Repayment of a bank loan', 'Payment of wages',
          'Sale of goods to a customer'],
    'a': 2,
    'w': 'Financing activities change the size and composition of the contributed equity and '
         'borrowings. Repaying a loan does exactly that.',
    'src': 'Chapter 14.3', 'sec': '14.3'},
   {'q': 'An asset with a carrying amount of ₦4,000,000 was sold for ₦5,200,000. In the statement '
         'of cash flows the correct treatment is',
    'o': ['₦5,200,000 investing inflow, and ₦1,200,000 deducted in the operating section',
          '₦1,200,000 investing inflow only',
          '₦4,000,000 investing inflow, and ₦1,200,000 added in the operating section',
          '₦5,200,000 investing inflow, and ₦1,200,000 added in the operating section',
          'no entry, as no cash moved'],
    'a': 0,
    'w': 'The full proceeds are the investing inflow. The ₦1,200,000 profit is already inside '
         'profit before tax, so it must be removed from the operating section to avoid counting '
         'the same cash twice.',
    'src': 'Chapter 14.4', 'sec': '14.4'},
   {'q': 'Revenue was ₦12,000,000. Receivables fell from ₦2,100,000 to ₦1,650,000. Cash received '
         'from customers was',
    'o': ['₦11,550,000', '₦12,450,000', '₦12,000,000', '₦10,350,000', '₦13,650,000'],
    'a': 1,
    'w': 'A fall in receivables means more cash was collected than was invoiced in the year.',
    'calc': '12{,}000{,}000 + 2{,}100{,}000 - 1{,}650{,}000 = 12{,}450{,}000',
    'src': 'Chapter 14.5', 'sec': '14.5'},
   {'q': 'Which of the following is a limitation of the statement of cash flows?',
    'o': ['It is easily manipulated by the choice of depreciation method',
          'It omits non-cash transactions such as assets acquired under a lease',
          'It does not show the cash position at the year end',
          'It is not required by any accounting standard',
          'It cannot be prepared without a full ledger'],
    'a': 1,
    'w': 'Significant non-cash transactions do not appear in the statement at all and must be '
         'disclosed separately. Independence from depreciation policy is a strength, not a '
         'limitation.',
    'src': 'Chapter 14.6', 'sec': '14.6'},
  ],
  'theory': [
   {'q': 'Explain the difference between the direct and the indirect methods of presenting cash '
         'flows from operating activities, and state THREE uses and THREE limitations of the '
         'statement of cash flows.',
    'marks': 10,
    'a': [
      {'h4': 'The two methods'},
      {'p': 'The **direct method** discloses the major classes of gross cash receipts and gross '
            'cash payments — cash received from customers, cash paid to suppliers and employees, '
            'interest paid, tax paid. It shows where the cash actually came from and went to.'},
      {'p': 'The **indirect method** starts from profit before tax and adjusts it for non-cash '
            'items (depreciation, amortisation, profits and losses on disposal), for items '
            'classified as investing or financing (finance costs, investment income), and for '
            'movements in working capital.'},
      {'p': 'Both give the **same net cash from operating activities**; only the operating section '
            'differs in presentation. IAS 7 encourages the direct method as more useful, but the '
            'indirect method predominates because the information is easier to extract from the '
            'ledger.'},
      {'h4': 'Uses'},
      {'ol': ['It shows whether operations generate enough cash to sustain the business, pay '
              'dividends and service debt.',
              'Cash is less susceptible to accounting policy choices than profit, so it is a more '
              'objective measure of performance.',
              'It explains why profit and the movement in cash differ, which is often the most '
              'important question a user has.',
              'It helps assess liquidity, solvency and financial adaptability.']},
      {'h4': 'Limitations'},
      {'ol': ['It is historical and gives no direct indication of future cash flows.',
              'It excludes significant non-cash transactions, such as acquiring assets under a '
              'lease or issuing shares as consideration for a business.',
              'It can be flattered by timing — deferring payments to suppliers until after the '
              'year end improves operating cash flow without improving the business.',
              'It says nothing about profitability, so it must be read alongside the other '
              'primary statements.']}],
    'src': 'Chapter 14.5', 'sec': '14.5'},
  ]},
}
