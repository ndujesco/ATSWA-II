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
    {'note': 'In the **new company\'s own books** (the acquirer\'s side, not the partnership\'s), '
             'the entry when the purchase consideration is paid is: **Dr** the Assets account(s) '
             'taken over, with any goodwill on acquisition; **Cr** Cash/Bank, Share Capital and '
             'Share Premium, for the consideration given.'},
  ]},

  {'n': '11.7', 't': 'The study text\'s worked illustrations', 'b': [
    {'p': 'The seven illustrations the study text works through, covering goodwill on admission, '
          'revaluation, retirement, amalgamation, dissolution with Garner v Murray, and '
          'conversion to a company. Questions are reproduced faithfully; several of the printed '
          'T-accounts are corrupted in the scan and have been rebuilt so they cross-cast.'},
    {'eg': {'tag': 'Illustration 11.1', 't': 'Panyin and Kakrah admit Olu — goodwill in and out '
      'of the books', 'open': True, 'q': [
      {'p': 'Panyin and Kakrah share profits and losses equally. Capital accounts: Panyin '
            '₵25,000,000; Kakrah ₵15,000,000. On 1 September 2024 they admit Olu, agreeing a new '
            'ratio of 2/5 : 2/5 : 1/5 for Panyin, Kakrah and Olu. Goodwill is valued at '
            '₵18,000,000 but is not recorded in the books. Olu pays ₵35,000,000 into the firm\'s '
            'bank account as capital. Show the entries (a) if goodwill is to remain in the books, '
            '(b) if goodwill is not to remain.'}],
      'a': [
      {'h4': '(a) Goodwill to remain'},
      {'p': 'Raise goodwill in the **old** (equal) ratio only: **Dr** Goodwill ₵18,000; '
            '**Cr** Panyin ₵9,000, Kakrah ₵9,000. Goodwill of ₵18,000 stays on the statement of '
            'financial position as an intangible asset. Olu is not credited.'},
      {'tacc': {'t': 'Partners\' Capital Accounts (₵\'000)', 'dr': [
          ['Panyin — Balance c/d', 34000], ['Kakrah — Balance c/d', 24000],
          ['Olu — Balance c/d', 35000]],
        'cr': [['Panyin — Balance b/d', 25000], ['Panyin — Goodwill', 9000],
               ['Kakrah — Balance b/d', 15000], ['Kakrah — Goodwill', 9000],
               ['Olu — Bank', 35000]]}},
      {'h4': '(b) Goodwill not to remain'},
      {'p': 'Raise in the old ratio, then write off in the **new** ratio: **Dr** Panyin ₵7,200, '
            'Kakrah ₵7,200, Olu ₵3,600; **Cr** Goodwill ₵18,000.'},
      {'tacc': {'t': 'Partners\' Capital Accounts (₵\'000)', 'dr': [
          ['Panyin — Goodwill written off', 7200], ['Kakrah — Goodwill written off', 7200],
          ['Olu — Goodwill written off', 3600],
          ['Panyin — Balance c/d', 26800], ['Kakrah — Balance c/d', 16800],
          ['Olu — Balance c/d', 31400]],
        'cr': [['Panyin — Balance b/d', 25000], ['Panyin — Goodwill', 9000],
               ['Kakrah — Balance b/d', 15000], ['Kakrah — Goodwill', 9000],
               ['Olu — Bank', 35000]]}},
      {'note': 'Net effect: Olu is charged ₵3,600 (his 1/5 of ₵18,000) and Panyin and Kakrah are '
               'each left ₵1,800 better off — that ₵3,600 is the goodwill Olu has bought into. '
               'The study text\'s printed part (a) mistakenly credits ₵9,000 of goodwill to Olu '
               'as well and then fails to cross-cast; the version above is correct.'}]}},
    {'eg': {'tag': 'Illustration 11.2', 't': 'Mensah and Babatunde — revaluation on admission',
      'open': True, 'q': [
      {'p': 'This is the same question, with the same figures, as **Illustration 10.3** '
            '(Chapter 10 §10.6): Mensah and Babatunde revalue their assets before admitting '
            'Shola — freehold property up to ₵9,500 (₵\'000), plant & machinery down to ₵1,425, '
            'motor vehicles down to ₵1,140, a 2½% allowance for doubtful debts on receivables of '
            '₵1,140, and creditors of ₵4,485 settled for ₵3,000.'}],
      'a': [
      {'p': 'The revaluation account shows a **profit of ₵5,446,500**, shared equally: '
            'Mensah ₵2,723,250 and Babatunde ₵2,723,250, taking each partner\'s capital to '
            '₵7,523,250. The full working — the journal entries, the revaluation account and the '
            'capital accounts — is set out in Chapter 10 §10.6, Illustration 10.3.'},
      {'key': 'On any change in the firm, the revaluation surplus or deficit is shared in the '
              '**old** ratio, because it accrued while only the old partners were in place.'}]}},
    {'eg': {'tag': 'Illustration 11.3', 't': 'Gyamfi and Lawal admit Ekiti', 'open': True, 'q': [
      {'p': 'Gyamfi and Lawal share equally. They admit Ekiti, who contributes ₦65,000 as '
            'capital, agreeing a new ratio of Gyamfi 2/5, Lawal 2/5, Ekiti 1/5. The statement of '
            'financial position at the date of admission (₦\'000):'},
      {'table': {'align': 'lrlr', 'head': ['', '₦\'000', '', '₦\'000'], 'rows': [
        ['Capital — Gyamfi', '75,000', 'Plant & machinery', '120,000'],
        ['Capital — Lawal', '75,000', 'Motor vehicle', '65,000'],
        ['Current — Gyamfi', '20,000', 'Inventory', '45,000'],
        ['Current — Lawal', '30,000', 'Receivables', '58,000'],
        ['Payables', '52,000', 'Cash', '4,000'],
        ['Overdraft', '40,000', '', ''],
        ['', '292,000', '', '292,000'],
      ]}},
      {'p': 'On admission: (1) revaluations — plant & machinery ₦250,000, motor vehicle ₦80,000, '
            'inventory ₦40,000, receivables ₦45,000; (2) goodwill estimated at ₦45,000, not to '
            'be kept in the books; (3) suppliers granted a discount of ₦6,000. Prepare (a) the '
            'Revaluation Account, (b) the Partners\' Capital Accounts, (c) the statement of '
            'financial position immediately after admission.'}],
      'a': [
      {'tacc': {'t': 'Revaluation Account (₦\'000)', 'dr': [
          ['Inventory (45,000 → 40,000)', 5000], ['Receivables (58,000 → 45,000)', 13000],
          ['Capital — Gyamfi (1/2)', 89000], ['Capital — Lawal (1/2)', 89000],
          ['', 196000, '@tot']],
        'cr': [['Plant & machinery (120,000 → 250,000)', 130000],
               ['Motor vehicle (65,000 → 80,000)', 15000],
               ['Goodwill', 45000], ['Suppliers — discount', 6000], ['', 196000, '@tot']]}},
      {'p': 'Profit on revaluation ₦178,000, shared equally (old ratio). Goodwill of ₦45,000 is '
            'then written off in the **new** ratio 2 : 2 : 1 — Gyamfi ₦18,000, Lawal ₦18,000, '
            'Ekiti ₦9,000.'},
      {'tacc': {'t': 'Partners\' Capital Accounts (₦\'000)', 'dr': [
          ['Gyamfi — Goodwill written off', 18000], ['Lawal — Goodwill written off', 18000],
          ['Ekiti — Goodwill written off', 9000],
          ['Gyamfi — Balance c/d', 146000], ['Lawal — Balance c/d', 146000],
          ['Ekiti — Balance c/d', 56000]],
        'cr': [['Gyamfi — Balance b/d', 75000], ['Gyamfi — Revaluation', 89000],
               ['Lawal — Balance b/d', 75000], ['Lawal — Revaluation', 89000],
               ['Ekiti — Bank', 65000]]}},
      {'stmt': {'t': 'Statement of financial position immediately after admission (₦\'000)',
        'rows': [
        'Non-current assets',
        ['Plant & machinery', 250000], ['Motor vehicle', 80000], ['', 330000, '@t'],
        '@gap',
        'Current assets',
        ['Inventory', 40000], ['Receivables', 45000], ['Bank and cash (4,000 + 65,000)', 69000],
        ['', 154000, '@t'],
        ['Less current liabilities — Payables 46,000; Overdraft 40,000', -86000],
        ['Net assets', 398000, '@tt'],
        '@gap',
        'Financed by',
        ['Capital — Gyamfi 146,000; Lawal 146,000; Ekiti 56,000', 348000],
        ['Current accounts — Gyamfi 20,000; Lawal 30,000', 50000],
        ['', 398000, '@tt'],
      ]}},
      {'note': 'Total assets ₦484,000 = net assets ₦398,000 + current liabilities ₦86,000. The '
               'printed study-text solution adds a spurious current-account column for Ekiti; a '
               'newly admitted partner has no opening current account.'}]}},
    {'eg': {'tag': 'Illustration 11.4', 't': 'Yekini, Olu and Essien — Olu retires', 'open': True,
      'q': [
      {'p': 'Yekini, Olu and Essien share profits 4 : 3 : 3. Olu retires on 31 December 2023. '
            'The statement of financial position at 31/12/2023 (₵m): freehold land & buildings '
            '540; machinery 180; office equipment 45; motor vehicles 105 (₵870). Current assets '
            '— inventory 100; receivable 125; bank 23 (₵248). Current liabilities — payables 158; '
            'bank overdraft 30 (₵188). Capital accounts — Yekini 420; Olu 300; Essien 210.'},
      {'p': 'The accounts do not yet reflect: (i) interest on drawings of ₵60m each, chargeable '
            'at 5%; (ii) interest on capital at 6% on balances of Yekini ₵210m, Olu ₵150m, Essien '
            '₵105m; (iii) Olu received ₵24m by cheque immediately; (iv) goodwill valued at ₵300m, '
            'to be kept in the books; (v) revaluations — freehold ₵600m, machinery ₵240m, office '
            'equipment ₵35m, motor vehicles ₵156m; discount from creditors ₵27m; 20% of '
            'receivables irrecoverable; 15% of inventory obsolete. The balance due to Olu is kept '
            'in the firm as a loan. Prepare the Revaluation Account, the Partners\' Capital '
            'Accounts and the adjusted statement of financial position.'}],
      'a': [
      {'tacc': {'t': 'Revaluation Account (₵m)', 'dr': [
          ['Office equipment (45 → 35)', 10], ['Receivables (20% × 125)', 25],
          ['Inventory (15% × 100)', 15],
          ['Capital — Yekini (4/10)', 179.2], ['Capital — Olu (3/10)', 134.4],
          ['Capital — Essien (3/10)', 134.4], ['', 498, '@tot']],
        'cr': [['Freehold land & buildings (540 → 600)', 60], ['Machinery (180 → 240)', 60],
               ['Motor vehicles (105 → 156)', 51], ['Goodwill', 300],
               ['Payables — discount', 27], ['', 498, '@tot']]}},
      {'p': 'Profit on revaluation ₵448m, shared 4 : 3 : 3. The interest adjustments net to a '
            '**deficit** of ₵18.9m (interest on drawings ₵9m less interest on capital ₵27.9m), '
            'also shared 4 : 3 : 3 — Yekini ₵7.56m, Olu ₵5.67m, Essien ₵5.67m as debits.'},
      {'tacc': {'t': 'Partners\' Capital Accounts (₵m)', 'dr': [
          ['Yekini — Interest on drawings', 3.0], ['Olu — Interest on drawings', 3.0],
          ['Essien — Interest on drawings', 3.0],
          ['Olu — Bank', 24.0],
          ['Yekini — Income distribution (deficit)', 7.56],
          ['Olu — Income distribution (deficit)', 5.67],
          ['Essien — Income distribution (deficit)', 5.67],
          ['Yekini — Balance c/d', 601.24], ['Olu — Balance c/d (to loan account)', 410.73],
          ['Essien — Balance c/d', 342.03]],
        'cr': [['Yekini — Balance b/d', 420.0], ['Olu — Balance b/d', 300.0],
               ['Essien — Balance b/d', 210.0],
               ['Yekini — Revaluation', 179.2], ['Olu — Revaluation', 134.4],
               ['Essien — Revaluation', 134.4],
               ['Yekini — Interest on capital', 12.6], ['Olu — Interest on capital', 9.0],
               ['Essien — Interest on capital', 6.3]]}},
      {'stmt': {'t': 'Adjusted statement of financial position at 31/12/2023 — Yekini, Essien & Co '
        '(₵m)', 'rows': [
        'Non-current assets',
        ['Goodwill', 300], ['Freehold land & buildings', 600], ['Machinery', 240],
        ['Motor vehicles', 156], ['Office equipment', 35], ['', 1331, '@t'],
        '@gap',
        'Current assets',
        ['Inventory (100 − 15)', 85], ['Receivable (125 − 25)', 100], ['', 185, '@t'],
        ['Less current liabilities — Payable 131; Bank overdraft 31', -162],
        ['', 1354, '@t'],
        ['Less non-current liability — Loan from Olu', -410.73],
        ['', 943.27, '@tt'],
        '@gap',
        'Capital accounts',
        ['Yekini', 601.24], ['Essien', 342.03], ['', 943.27, '@tt'],
      ]}}]}},
    {'eg': {'tag': 'Illustration 11.5', 't': 'Egapate & Co and ShoBoafo & Co amalgamate',
      'open': True, 'q': [
      {'p': 'Eghan and Adepate (firm Egapate & Co) share equally. Shola and Boafo (firm ShoBoafo '
            '& Co) share 3/5 : 2/5. They amalgamate as **Ega Sho & Co**, sharing Eghan 25%, '
            'Adepate 30%, Shola 25%, Boafo 20%.'},
      {'table': {'align': 'lrr', 'head': ['(₵m)', 'Egapate', 'ShoBoafo'], 'rows': [
        ['Non-current assets', '120', '160'],
        ['Inventory', '8', '24'],
        ['Cash', '10', '5'],
        ['', '138', '189'],
        ['Capital — Eghan / Shola', '100', '99'],
        ['Capital — Adepate / Boafo', '38', '90'],
      ]}},
      {'p': 'On amalgamation the assets are revalued (₵m): non-current assets — Egapate 180, '
            'ShoBoafo 200; inventory — Egapate 12, ShoBoafo 16; goodwill — Egapate 80, ShoBoafo '
            '320. The new firm will not show goodwill. Capitals in the new firm are to be Eghan '
            '₵100m, Adepate ₵150m, Shola ₵300m, Boafo ₵250m. Prepare (a) the Capital Accounts, '
            '(b) the opening statement of financial position of Ega Sho & Co.'}],
      'a': [
      {'tacc': {'t': 'Revaluation account — Egapate & Co (₵m)', 'dr': [
          ['Capital — Eghan', 72], ['Capital — Adepate', 72], ['', 144, '@tot']],
        'cr': [['Non-current assets (120 → 180)', 60], ['Inventory (8 → 12)', 4],
               ['Goodwill', 80], ['', 144, '@tot']]}},
      {'tacc': {'t': 'Revaluation account — ShoBoafo & Co (₵m)', 'dr': [
          ['Inventory (24 → 16)', 8], ['Capital — Shola (3/5)', 211.2],
          ['Capital — Boafo (2/5)', 140.8], ['', 360, '@tot']],
        'cr': [['Non-current assets (160 → 200)', 40], ['Goodwill', 320], ['', 360, '@tot']]}},
      {'p': 'Total goodwill ₵400m is written off against all four partners in the **new** ratio '
            '25 : 30 : 25 : 20 — Eghan ₵100m, Adepate ₵120m, Shola ₵100m, Boafo ₵80m. Each '
            'partner then pays in (or draws) cash to reach the agreed new capital.'},
      {'tacc': {'t': 'Partners\' Capital Account (₵m)', 'dr': [
          ['Goodwill written off — Eghan', 100], ['Goodwill written off — Adepate', 120],
          ['Goodwill written off — Shola', 100], ['Goodwill written off — Boafo', 80],
          ['Balance c/d — Eghan', 100], ['Balance c/d — Adepate', 150],
          ['Balance c/d — Shola', 300], ['Balance c/d — Boafo', 250]],
        'cr': [['Balance b/f — Eghan', 100], ['Balance b/f — Adepate', 38],
               ['Balance b/f — Shola', 99], ['Balance b/f — Boafo', 90],
               ['Revaluation — Eghan', 72], ['Revaluation — Adepate', 72],
               ['Revaluation — Shola', 211.2], ['Revaluation — Boafo', 140.8],
               ['Bank — Eghan', 28], ['Bank — Adepate', 160],
               ['Bank — Shola', 89.8], ['Bank — Boafo', 99.2]]}},
      {'stmt': {'t': 'Opening statement of financial position — Ega Sho & Co (₵m)', 'rows': [
        ['Non-current assets (180 + 200)', 380],
        ['Inventories (12 + 16)', 28],
        ['Cash (10 + 5 + 377 introduced)', 392],
        ['', 800, '@tt'],
        '@gap',
        'Capital accounts',
        ['Eghan', 100], ['Adepate', 150], ['Shola', 300], ['Boafo', 250], ['', 800, '@tt'],
      ]}}]}},
    {'eg': {'tag': 'Illustration 11.6', 't': 'John, David and Ajomale — dissolution', 'open': True,
      'q': [
      {'p': 'John, David and Ajomale share profits 2 : 2 : 1. Balances at dissolution (₵m): '
            'leasehold properties 550; motor vehicles 220; furniture & fittings 150; inventories '
            '420; receivables 350; trade payables 390; bank overdraft 91; loan from Amogu 305; '
            'capital — John 255, David 200, Ajomale 275; current accounts — John 75, David 50, '
            'Ajomale 49.'},
      {'p': 'John took over one vehicle (book value ₵80m) at a valuation of ₵150m. Ajomale took '
            'over half the inventory for ₵250m. The leasehold properties, the remaining vehicle '
            'and the fixtures & fittings realised ₵720m; receivables realised ₵320m. After '
            'paying the trade payables in full, the partners settled their capital accounts. '
            'Prepare the Realisation Account, the Bank Account and the Partners\' Capital '
            'Accounts.'}],
      'a': [
      {'tacc': {'t': 'Realisation Account (₵m)', 'dr': [
          ['Leasehold properties', 550], ['Motor vehicles', 220],
          ['Furniture & fittings', 150], ['Receivables', 350], ['Inventories', 420],
          ['', 1690, '@tot']],
        'cr': [['Capital — John (vehicle taken over)', 150],
               ['Capital — Ajomale (inventory taken over)', 250],
               ['Bank — sundry assets', 720], ['Bank — receivables', 320],
               ['Loss — John (2/5)', 100], ['Loss — David (2/5)', 100],
               ['Loss — Ajomale (1/5)', 50], ['', 1690, '@tot']]}},
      {'tacc': {'t': 'Partners\' Capital Accounts (₵m)', 'dr': [
          ['John — Asset taken over', 150], ['Ajomale — Asset taken over', 250],
          ['John — Realisation loss', 100], ['David — Realisation loss', 100],
          ['Ajomale — Realisation loss', 50],
          ['John — Bank', 80], ['David — Bank', 150], ['Ajomale — Bank', 24]],
        'cr': [['John — Balance b/d', 255], ['David — Balance b/d', 200],
               ['Ajomale — Balance b/d', 275],
               ['John — Current account', 75], ['David — Current account', 50],
               ['Ajomale — Current account', 49]]}},
      {'tacc': {'t': 'Bank Account (₵m)', 'dr': [
          ['Sundry assets', 720], ['Receivables', 320], ['', 1040, '@tot']],
        'cr': [['Balance b/d (overdraft)', 91], ['Loan from Amogu', 305],
               ['Trade payables', 390],
               ['Capital — John', 80], ['Capital — David', 150], ['Capital — Ajomale', 24],
               ['', 1040, '@tot']]}},
      {'note': 'Loss on realisation ₵250m = book value of assets ₵1,690m less amounts recovered '
               '(₵150 + ₵250 + ₵720 + ₵320 = ₵1,440m). Every partner ends with a credit balance '
               'and is paid out — John ₵80m, David ₵150m, Ajomale ₵24m.'}]}},
    {'eg': {'tag': 'Illustration 11.7', 't': 'Olu, Mosho and Aryee — conversion to a company',
      'open': True, 'q': [
      {'p': 'Olu, Mosho and Aryee share profits 5 : 3 : 2. On 1 January 2022 they convert the '
            'business into Olumosho Ltd. Statement of financial position at 31 December 2021 '
            '(₵\'000): capital — Olu 36,000, Mosho 24,000, Aryee 18,000; current accounts — Olu '
            '1,560, Mosho 1,920, Aryee 840; partners\' loans 6,000. Assets — freehold buildings '
            '36,000; vehicles 14,400; equipment 7,500; inventories 18,375; receivables 14,445; '
            'bank 6,600; less payables 9,000 (net ₵88,320).'},
      {'p': 'Apart from the cash and one vehicle, all assets and liabilities are taken over by '
            'the company. Aryee took over one vehicle at a valuation of ₵6,000,000. The purchase '
            'consideration is: freehold buildings ₵69,000; vehicle ₵7,200; equipment ₵4,800; '
            'inventories ₵12,000; receivable ₵13,800; goodwill ₵24,000 (₵130,800) less trade '
            'payables ₵9,000 = **₵121,800**, satisfied by fully paid ₵1,000 shares. Realisation '
            'expenses were ₵5,000,000. Close the books of the partnership.'}],
      'a': [
      {'tacc': {'t': 'Realisation Account (₵\'000)', 'dr': [
          ['Realisation expenses', 5000], ['Freehold buildings', 36000], ['Vehicles', 14400],
          ['Equipment', 7500], ['Inventories', 18375], ['Receivables', 14445],
          ['Profit — Olu (5/10)', 20540], ['Profit — Mosho (3/10)', 12324],
          ['Profit — Aryee (2/10)', 8216], ['', 136800, '@tot']],
        'cr': [['Capital — Aryee (vehicle taken over)', 6000],
               ['Olumosho Ltd — purchase consideration', 121800],
               ['Trade payables (assumed by company)', 9000], ['', 136800, '@tot']]}},
      {'p': 'Profit on realisation ₵41,080 (₵\'000), shared 5 : 3 : 2. The ₵121,800 of shares is '
            'divided in the profit sharing ratio — Olu ₵60,900, Mosho ₵36,540, Aryee ₵24,360.'},
      {'tacc': {'t': 'Partners\' Capital Accounts (₵\'000)', 'dr': [
          ['Aryee — Vehicle taken over', 6000],
          ['Olu — Shares in Olumosho Ltd', 60900], ['Mosho — Shares in Olumosho Ltd', 36540],
          ['Aryee — Shares in Olumosho Ltd', 24360],
          ['Mosho — Bank', 1704]],
        'cr': [['Olu — Balance b/d', 36000], ['Mosho — Balance b/d', 24000],
               ['Aryee — Balance b/d', 18000],
               ['Olu — Current account', 1560], ['Mosho — Current account', 1920],
               ['Aryee — Current account', 840],
               ['Olu — Realisation profit', 20540], ['Mosho — Realisation profit', 12324],
               ['Aryee — Realisation profit', 8216],
               ['Olu — Bank', 2800], ['Aryee — Bank', 3304]]}},
      {'tacc': {'t': 'Bank Account (₵\'000)', 'dr': [
          ['Balance b/f', 6600], ['Capital — Olu', 2800], ['Capital — Aryee', 3304],
          ['', 12704, '@tot']],
        'cr': [['Realisation expenses', 5000], ['Partners\' loan accounts', 6000],
               ['Capital — Mosho', 1704], ['', 12704, '@tot']]}},
      {'note': 'Olu and Aryee pay cash **in** (₵2,800 and ₵3,304) because their share of the '
               'consideration exceeds the balance on their accounts; Mosho draws ₵1,704 out. The '
               'partners\' loans of ₵6,000 are repaid from the bank.'}]}},
  ]},

  {'n': '11.8', 't': 'End-of-chapter questions (study text)', 'b': [
    {'p': 'The study text\'s multiple-choice and short-answer set, with its answer key and the '
          'tutorial workings for the first two.'},
    {'eg': {'tag': 'Study text Q1–Q7', 't': 'Questions with the study text\'s answers', 'open': True,
      'q': [
      {'p': '**Questions 1 and 2.** Shola and Bada are in partnership sharing profits 2 : 3. On '
            '1 September 2021 a new partner, Carol, joins, introducing ₦24m capital. At that '
            'date: goodwill is valued at ₦80m; the new profit-sharing ratio is 3 : 6 : 1; '
            'property is revalued upwards by ₦70m. Shola had a credit balance of ₦90m before the '
            'adjustments. Goodwill is not retained.'},
      {'ol': [
        'Calculate the total amount of goodwill and revaluation surplus credited to Bada\'s '
        'capital account. (A) ₦32m  (B) ₦42m  (C) ₦48m  (D) ₦60m  (E) ₦90m',
        'What is the balance on Shola\'s capital account after all adjustments? (A) ₦112m  '
        '(B) ₦118m  (C) ₦126m  (D) ₦136m  (E) ₦150m',
      ]},
      {'p': '**Questions 3 and 4.** Joe, Okon and Koko were in partnership sharing profits '
            '1 : 1 : 2. After dissolution and closing all accounts the capital balances were: '
            'Joe ₦40m credit; Okon ₦60m credit; Koko ₦50m debit.'},
      {'ol': [
        'State how Koko\'s debit balance should be accounted for if he is **not** insolvent.',
        'How much would Joe contribute to Koko\'s deficiency, assuming Koko **is** insolvent?',
        'When a partnership is converted to a company, the purchase consideration could be in '
        'the form of (i) cash and (ii) …',
        'What is the accounting entry for an asset taken over by a partner when a partnership is '
        'dissolved? And when a partner retires, the balance on his capital account after all '
        'adjustments is transferred to … account.',
      ]}],
      'a': [
      {'ol': [
        '**(B) ₦42m.** Bada\'s share of goodwill $= \\tfrac35 \\times 80 = 48$; share of the '
        'revaluation surplus $= \\tfrac35 \\times 70 = 42$; total credited ₦90m. Goodwill is '
        'then written back in the new ratio $\\tfrac{6}{10} \\times 80 = 48$, so the **net** '
        'credit is $90 - 48 = ₦42\\text{m}$.',
        '**(C) ₦126m.** Shola: opening ₦90m; $+ \\tfrac25 \\times 80 = 32$ (goodwill); '
        '$+ \\tfrac25 \\times 70 = 28$ (surplus); $- \\tfrac{3}{10} \\times 80 = 24$ (goodwill '
        'written back) $= ₦126\\text{m}$.',
        'Koko pays ₦50m into the firm — the deficit is settled from the surplus in his private '
        'estate.',
        '**₦20m.** Under Garner v Murray the solvent partners bear the deficiency in the ratio '
        'of their last agreed capitals, Joe ₦40m : Okon ₦60m. Joe\'s share $= \\tfrac{40}{100} '
        '\\times 50 = ₦20\\text{m}$.',
        'Shares (ordinary share capital) — and/or debentures/loan notes.',
        '**Dr** the partner\'s capital account, **Cr** the realisation account. On retirement '
        'the residual balance is transferred to a **loan account** if it stays in the firm, or '
        'paid through the **bank** if settled at once (the study text\'s key gives "Bank '
        'account").'],
      }]}},
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
    'src': 'Chapter 11.1', 'sec': '11.1'},
   {'q': 'Yemi and Dele share profits 1 : 2. They admit Ade, who is entitled to one-fifth of '
         'profits, the others continuing to share the balance in their old ratio. The new ratio is',
    'o': ['1 : 2 : 1', '4 : 8 : 3', '3 : 6 : 5', '2 : 4 : 1', '1 : 1 : 1'],
    'a': 1,
    'w': 'Ade takes 1/5, leaving 4/5 shared 1 : 2. Yemi gets 1/3 × 4/5 = 4/15 and Dele 2/3 × 4/5 '
         '= 8/15; Ade is 1/5 = 3/15. So 4 : 8 : 3.',
    'calc': '\\text{Yemi} = \\frac{4}{15}, \\quad \\text{Dele} = \\frac{8}{15}, \\quad '
            '\\text{Ade} = \\frac{3}{15}',
    'src': 'Chapter 11.2', 'sec': '11.2'},
   {'q': 'A surplus arising on the revaluation of assets when a new partner is admitted is '
         'credited to',
    'o': ['all partners in the new ratio', 'the old partners in the old ratio',
          'the new partner only', 'all partners equally',
          'a revaluation reserve that is never distributed'],
    'a': 1,
    'w': 'The surplus accrued while only the old partners were in the firm, so it belongs to them '
         'in the ratio in which they then shared profits.',
    'src': 'Chapter 11.3', 'sec': '11.3'},
   {'q': 'Under the rule in Garner v Murray, the deficiency of an insolvent partner is borne by '
         'the solvent partners in the ratio of',
    'o': ['their profit sharing ratio', 'their last agreed capital balances', 'their drawings',
          'their current account balances', 'equal shares'],
    'a': 1,
    'w': 'The rule requires the deficiency to be shared in the ratio of the solvent partners\' '
         'last agreed capitals, not in the profit sharing ratio.',
    'src': 'Chapter 11.5', 'sec': '11.5'},
   {'q': 'On the dissolution of a partnership, the debit balance remaining on the realisation '
         'account represents',
    'o': ['a profit on realisation', 'a loss on realisation', 'cash still to be collected',
          'goodwill written off', 'amounts due to creditors'],
    'a': 1,
    'w': 'The realisation account is debited with book values and credited with proceeds. A debit '
         'balance means the assets realised less than their book value — a loss, shared in the '
         'profit sharing ratio.',
    'src': 'Chapter 11.5', 'sec': '11.5'},
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
    'src': 'Chapter 11.1', 'sec': '11.1'},
  ]},
}
