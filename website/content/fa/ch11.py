CH = {
 'n': 11,
 't': 'Partnership Accounts II: Changes in the Firm',
 'brief': 'Goodwill, admission, retirement and death, revaluation of assets, amalgamation, '
          'dissolution and conversion to a company.',
 'outcomes': [
   'Explain the nature of goodwill and the methods of valuing it',
   'Account for goodwill on admission and retirement, with and without a goodwill account',
   'Prepare a revaluation account and share the surplus or deficit',
   'Account for the retirement or death of a partner',
   'Prepare a realisation account on dissolution and apply the rule in Garner v Murray',
 ],
 'secs': [
  {'n': '11.1', 't': 'Goodwill', 'b': [
    {'def': {'t': 'Goodwill', 'd': 'the excess of the value of a business as a whole over the fair '
                  'value of its separable net assets — the benefit of reputation, connection, '
                  'location, skilled staff and established custom.'}},
    {'h3': 'Methods of valuation'},
    {'table': {'head': ['Method', 'Formula'], 'align': 'll', 'rows': [
      ['Purchase of average profits',
       '$\\text{Goodwill} = \\text{Average annual profit} \\times n \\text{ years}$'],
      ['Purchase of super profits',
       '$\\text{Goodwill} = \\text{Super profit} \\times n$'],
      ['Capitalisation of super profits',
       '$\\text{Goodwill} = \\dfrac{\\text{Super profit}}{\\text{Normal rate of return}}$'],
      ['Annuity method',
       '$\\text{Goodwill} = \\text{Super profit} \\times \\text{annuity factor}$'],
      ['Percentage of turnover', '$\\text{Goodwill} = x\\% \\times \\text{annual turnover}$'],
    ]}},
    {'tex': '\\text{Super profit} = \\text{Average profit} - \\bigl(\\text{Capital employed} '
            '\\times \\text{Normal rate of return}\\bigr)', 'tag': '(11.1)'},
    {'eg': {'t': 'Valuing goodwill three ways', 'q': [
      {'p': 'A firm\'s profits for the last four years were ₦4,200,000, ₦4,800,000, ₦5,400,000 '
            'and ₦5,600,000. Capital employed is ₦24,000,000 and the normal return in the '
            'industry is 15%. Value goodwill at (a) three years\' purchase of average profits, '
            '(b) two years\' purchase of super profits, (c) capitalisation of super profits.'}],
      'a': [
      {'tex': '\\text{Average profit} = \\frac{4{,}200{,}000 + 4{,}800{,}000 + 5{,}400{,}000 '
              '+ 5{,}600{,}000}{4} = ₦5{,}000{,}000'},
      {'p': '**(a)** $5{,}000{,}000 \\times 3 = ₦15{,}000{,}000$.'},
      {'tex': '\\text{Normal profit} = 0.15 \\times 24{,}000{,}000 = ₦3{,}600{,}000'},
      {'tex': '\\text{Super profit} = 5{,}000{,}000 - 3{,}600{,}000 = ₦1{,}400{,}000'},
      {'p': '**(b)** $1{,}400{,}000 \\times 2 = ₦2{,}800{,}000$.'},
      {'tex': '\\textbf{(c)}\\quad \\text{Goodwill} = \\frac{1{,}400{,}000}{0.15} '
              '= ₦9{,}333{,}333'},
      {'note': 'Three defensible answers from the same facts, which is exactly why the method '
               'must be stated. Always say which method you used; the marks follow the method, '
               'not the number.'}]}},
  ]},

  {'n': '11.2', 't': 'Goodwill on admission', 'b': [
    {'p': 'A new partner buys a share of future profits that the existing partners were enjoying. '
          'Goodwill must be credited to the **old** partners in the **old** ratio, and if no '
          'goodwill account is to remain, written back against **all** partners in the **new** ratio.'},
    {'steps': [
      'Raise goodwill: **Dr** Goodwill, **Cr** old partners\' capital accounts in the **old** ratio.',
      'Write goodwill off: **Dr** all partners\' capital accounts in the **new** ratio, '
      '**Cr** Goodwill.',
    ]},
    {'p': 'The net effect is that the incoming partner is charged, and the old partners '
          'compensated, for the share of goodwill transferred. That net amount is the '
          '**sacrifice**.'},
    {'tex': '\\text{Sacrifice ratio} = \\text{Old share} - \\text{New share}', 'tag': '(11.2)'},
    {'eg': {'t': 'Admission with goodwill written off', 'q': [
      {'p': 'Gbenga and Halima share profits 3 : 2 with capitals of ₦9,000,000 and ₦6,000,000. '
            'They admit Ibrahim, who brings ₦5,000,000 as capital, for a one-fifth share, '
            'Gbenga and Halima continuing to share the remainder in their old ratio. Goodwill is '
            'valued at ₦7,500,000 and is not to remain in the books. Show the capital accounts.'}],
      'a': [
      {'h4': 'W1 — the new ratio'},
      {'p': 'Ibrahim takes $\\tfrac15$, leaving $\\tfrac45$ for Gbenga and Halima in 3 : 2:'},
      {'tex': '\\text{Gbenga} = \\frac35 \\times \\frac45 = \\frac{12}{25}, \\qquad '
              '\\text{Halima} = \\frac25 \\times \\frac45 = \\frac{8}{25}, \\qquad '
              '\\text{Ibrahim} = \\frac15 = \\frac{5}{25}'},
      {'p': 'New ratio 12 : 8 : 5.'},
      {'h4': 'W2 — goodwill raised and written off'},
      {'table': {'align': 'lrrr', 'head': ['', 'Gbenga (₦)', 'Halima (₦)', 'Ibrahim (₦)'], 'rows': [
        ['Raised in old ratio 3 : 2', '4,500,000', '3,000,000', '—'],
        ['Written off in new ratio 12 : 8 : 5', '(3,600,000)', '(2,400,000)', '(1,500,000)'],
        ['Net credit / (charge)', '900,000', '600,000', '(1,500,000)', '@tot'],
      ]}},
      {'h4': 'Capital accounts'},
      {'table': {'align': 'lrrr', 'head': ['', 'Gbenga (₦)', 'Halima (₦)', 'Ibrahim (₦)'], 'rows': [
        ['Balance b/d', '9,000,000', '6,000,000', '—'],
        ['Cash introduced', '—', '—', '5,000,000'],
        ['Net goodwill adjustment (W2)', '900,000', '600,000', '(1,500,000)'],
        ['Balance c/d', '9,900,000', '6,600,000', '3,500,000', '@tot'],
      ]}},
      {'note': 'Ibrahim effectively paid ₦1,500,000 for his one-fifth share of goodwill '
               '($\\tfrac15 \\times 7{,}500{,}000$), and the old partners received it in their '
               'sacrifice ratio. Where the question instead says goodwill is to **remain** in the '
               'books, stop after the first step and show goodwill of ₦7,500,000 as an intangible '
               'asset.'}]}},
  ]},

  {'n': '11.3', 't': 'Revaluation of assets', 'b': [
    {'p': 'A change in the firm crystallises gains and losses that accrued while the old partners '
          'were in place, so assets and liabilities are revalued and the surplus or deficit shared '
          'in the **old** ratio before the change takes effect.'},
    {'tacc': {'t': 'Revaluation account', 'dr': [
        ['Decrease in asset values', ''], ['Increase in liabilities', ''],
        ['Provision for doubtful debts created', ''],
        ['Profit on revaluation to old partners', '']],
      'cr': [['Increase in asset values', ''], ['Decrease in liabilities', ''],
             ['Provisions no longer required', ''], ['Loss on revaluation to old partners', '']]}},
    {'key': 'Old ratio, always. The whole purpose of the revaluation is to settle the position as '
            'it stood **before** the new arrangement, so the incoming partner takes no part in it.'},
  ]},

  {'n': '11.4', 't': 'Retirement and death', 'b': [
    {'p': 'On retirement the outgoing partner is credited with everything due and the balance is '
          'either paid out or transferred to a loan account.'},
    {'steps': [
      'Revalue assets and liabilities; share the surplus in the old ratio.',
      'Credit the retiring partner with a share of goodwill in the old ratio.',
      'Transfer the balance on the current account to the capital account.',
      'Credit any share of profit to the date of retirement.',
      'Pay the total, or transfer it to a loan account bearing interest.',
    ]},
    {'p': 'On **death**, the same steps apply, with the balance payable to the deceased\'s estate. '
          'Where the firm holds a **joint life policy**, the sum received is credited to the '
          'partners in the profit sharing ratio and provides the cash to settle the estate.'},
    {'tex': '\\text{Gaining ratio} = \\text{New share} - \\text{Old share}', 'tag': '(11.3)'},
    {'p': 'The continuing partners bear the retiring partner\'s goodwill in their **gaining** '
          'ratio, which is the mirror image of the sacrifice ratio on an admission.'},
  ]},

  {'n': '11.5', 't': 'Dissolution and the rule in Garner v Murray', 'b': [
    {'p': 'On dissolution the assets are realised, the liabilities paid, and whatever remains is '
          'returned to the partners. Everything runs through a **realisation account**.'},
    {'tacc': {'t': 'Realisation account', 'dr': [
        ['Assets at book value (except cash)', ''], ['Realisation expenses', ''],
        ['Liabilities paid at more than book value', ''],
        ['Profit on realisation to partners', '']],
      'cr': [['Provisions and accumulated depreciation', ''], ['Cash from sale of assets', ''],
             ['Assets taken over by partners', ''], ['Liabilities taken over by partners', ''],
             ['Loss on realisation to partners', '']]}},
    {'h3': 'Order of application of the proceeds'},
    {'ol': [
      'External liabilities and the costs of realisation.',
      'Partners\' loans and advances beyond capital.',
      'Partners\' capital accounts.',
      'Any residue in the profit sharing ratio.',
    ]},
    {'h3': 'Garner v Murray'},
    {'p': 'Where a partner\'s capital account is in deficit and that partner is **insolvent**, the '
          'deficiency is borne by the solvent partners in the ratio of their **last agreed capital '
          'balances** — not in the profit sharing ratio.'},
    {'eg': {'t': 'Applying Garner v Murray', 'q': [
      {'p': 'On dissolution, after all adjustments, the capital accounts stood at: J ₦4,000,000 '
            'credit; K ₦2,000,000 credit; L ₦900,000 debit. L is insolvent and can pay nothing. '
            'Profits were shared equally. Show the final distribution.'}],
      'a': [
      {'p': 'L\'s deficiency of ₦900,000 is borne by J and K in the ratio of their capitals, '
            '4,000,000 : 2,000,000 = 2 : 1:'},
      {'tex': 'J = \\frac{2}{3} \\times 900{,}000 = ₦600{,}000 \\qquad '
              'K = \\frac{1}{3} \\times 900{,}000 = ₦300{,}000'},
      {'table': {'align': 'lrr', 'head': ['', 'J (₦)', 'K (₦)'], 'rows': [
        ['Capital balance', '4,000,000', '2,000,000'],
        ["Share of L's deficiency", '(600,000)', '(300,000)'],
        ['Cash received', '3,400,000', '1,700,000', '@tot'],
      ]}},
      {'warn': 'Had the deficiency been shared **equally** (the profit sharing ratio) each would '
               'have borne ₦450,000. The rule exists precisely because the profit sharing ratio is '
               'the wrong basis: a partner who put in more capital has more at risk and, on the '
               'reasoning in the case, bears the loss in proportion to that capital.'}]}},
  ]},

  {'n': '11.6', 't': 'Amalgamation and conversion to a company', 'b': [
    {'p': 'On **amalgamation** two firms combine. Each firm revalues, closes its books through a '
          'realisation account, and the new firm opens with the agreed values and the agreed '
          'capitals. The mechanics are those of a dissolution followed by a formation.'},
    {'p': 'On **conversion to a company**, the partnership sells its business to the company. The '
          'realisation account is credited with the **purchase consideration**, which may be cash, '
          'shares, debentures, or a combination.'},
    {'tex': '\\text{Purchase consideration} = \\text{Cash} + \\text{Shares at issue value} '
            '+ \\text{Debentures}'},
    {'p': 'The profit or loss on realisation is shared in the profit sharing ratio, and the '
          'consideration is then distributed to the partners in settlement of their capital '
          'accounts. Shares are usually divided in the final capital account ratio, which need '
          'not equal the profit sharing ratio.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Super profit',
   'tex': '\\text{Super profit} = \\text{Average profit} - (\\text{Capital employed} \\times r)'},
  {'lb': 'Goodwill by capitalisation of super profits',
   'tex': '\\text{Goodwill} = \\frac{\\text{Super profit}}{r}'},
  {'lb': 'Sacrifice ratio (admission)',
   'tex': '\\text{Sacrifice} = \\text{Old share} - \\text{New share}'},
  {'lb': 'Gaining ratio (retirement)',
   'tex': '\\text{Gain} = \\text{New share} - \\text{Old share}'},
  {'lb': 'Garner v Murray',
   'tex': '\\text{Share of deficiency} = \\text{Deficiency} \\times '
          '\\frac{\\text{Partner\'s last agreed capital}}{\\text{Total solvent capitals}}'},
 ],
 'focus':
   'Alternates with Chapter 10 as the partnership question, and when it appears it is worth the '
   'full 12–15 marks. Admission with goodwill and revaluation is the most common form; dissolution '
   'with Garner v Murray is the next. Learn the two-step goodwill treatment (raise in the old '
   'ratio, write off in the new) as a reflex, and always compute the new ratio explicitly before '
   'touching any figures.',
 'errors': [
   'Writing goodwill off in the old ratio instead of the new.',
   'Sharing a revaluation surplus in the new ratio — it belongs to the old partners.',
   'Applying Garner v Murray in the profit sharing ratio rather than the capital ratio.',
   'Forgetting to transfer current account balances to capital accounts before a dissolution.',
   'Omitting cash and bank from the realisation account when they should be omitted, or including '
   'them when the question says the bank balance is realised.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Average profit is ₦3,600,000, capital employed ₦18,000,000 and the normal rate of '
         'return 12%. Super profit is',
    'o': ['₦2,160,000', '₦1,440,000', '₦3,600,000', '₦432,000', '₦1,800,000'],
    'a': 1,
    'w': 'Super profit is the excess of actual profit over the normal return on capital employed.',
    'calc': '3{,}600{,}000 - (0.12 \\times 18{,}000{,}000) = 3{,}600{,}000 - 2{,}160{,}000 '
            '= 1{,}440{,}000',
    'src': 'Chapter 11.1'},
   {'q': 'Yemi and Dele share profits 1 : 2. They admit Ade, who is entitled to one-fifth of '
         'profits, the others continuing to share the balance in their old ratio. The new ratio is',
    'o': ['1 : 2 : 1', '4 : 8 : 3', '3 : 6 : 5', '2 : 4 : 1', '1 : 1 : 1'],
    'a': 1,
    'w': 'Ade takes 1/5, leaving 4/5 shared 1 : 2. Yemi gets 1/3 × 4/5 = 4/15 and Dele 2/3 × 4/5 '
         '= 8/15; Ade is 1/5 = 3/15. So 4 : 8 : 3.',
    'calc': '\\text{Yemi} = \\frac{4}{15}, \\quad \\text{Dele} = \\frac{8}{15}, \\quad '
            '\\text{Ade} = \\frac{3}{15}',
    'src': 'Chapter 11.2'},
   {'q': 'A surplus arising on the revaluation of assets when a new partner is admitted is '
         'credited to',
    'o': ['all partners in the new ratio', 'the old partners in the old ratio',
          'the new partner only', 'all partners equally',
          'a revaluation reserve that is never distributed'],
    'a': 1,
    'w': 'The surplus accrued while only the old partners were in the firm, so it belongs to them '
         'in the ratio in which they then shared profits.',
    'src': 'Chapter 11.3'},
   {'q': 'Under the rule in Garner v Murray, the deficiency of an insolvent partner is borne by '
         'the solvent partners in the ratio of',
    'o': ['their profit sharing ratio', 'their last agreed capital balances', 'their drawings',
          'their current account balances', 'equal shares'],
    'a': 1,
    'w': 'The rule requires the deficiency to be shared in the ratio of the solvent partners\' '
         'last agreed capitals, not in the profit sharing ratio.',
    'src': 'Chapter 11.5'},
   {'q': 'On the dissolution of a partnership, the debit balance remaining on the realisation '
         'account represents',
    'o': ['a profit on realisation', 'a loss on realisation', 'cash still to be collected',
          'goodwill written off', 'amounts due to creditors'],
    'a': 1,
    'w': 'The realisation account is debited with book values and credited with proceeds. A debit '
         'balance means the assets realised less than their book value — a loss, shared in the '
         'profit sharing ratio.',
    'src': 'Chapter 11.5'},
  ],
  'theory': [
   {'q': 'Explain the nature of goodwill and describe FOUR methods by which it may be valued.',
    'marks': 8,
    'a': [
      {'p': '**Nature.** Goodwill is the excess of the value of a business taken as a whole over '
            'the aggregate fair value of its separable net assets. It arises from reputation, '
            'established customer connection, favourable location, skilled and stable staff, '
            'trade names and efficient management. It is an intangible asset which is inseparable '
            'from the business, cannot be sold on its own, and fluctuates in value with the '
            'fortunes of the firm. Under IAS 38 **internally generated goodwill is never '
            'recognised**; it is recorded only where it has been purchased.'},
      {'h4': 'Methods of valuation'},
      {'ol': [
        '**Purchase of average profits** — goodwill equals the average annual profit of an agreed '
        'number of past years multiplied by an agreed number of years\' purchase.',
        '**Purchase of super profits** — super profit is the excess of average profit over the '
        'normal return on capital employed; goodwill is that super profit multiplied by an agreed '
        'number of years.',
        '**Capitalisation of super profits** — goodwill is the super profit divided by the normal '
        'rate of return, which values the super profit as a perpetuity.',
        '**Annuity method** — the super profit is treated as an annuity for a fixed number of '
        'years and discounted to present value using an annuity factor.',
        '**Percentage of turnover** — common in professional practices, where goodwill is taken '
        'as an agreed percentage of annual gross fees.']},
      {'note': 'Every method gives a different figure from the same facts, so the method used must '
               'be agreed between the partners and stated in the answer.'}],
    'src': 'Chapter 11.1'},
  ]},
}
