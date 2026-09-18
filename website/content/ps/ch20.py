CH = {
 'n': 20,
 't': 'Investment/Project Appraisal in the Public Sector',
 'brief': 'Why public sector investment needs formal appraisal, and the three examinable '
          'methods — Accounting Rate of Return, Payback Period and Net Present Value — each '
          'fully worked.',
 'outcomes': [
   'State the reasons for investment/project appraisal in the public sector',
   'Compute and apply the Accounting Rate of Return (ARR)',
   'Compute and apply the Payback Period (PBP)',
   'Compute and apply the Net Present Value (NPV)',
   'Advise on project selection using each method',
 ],
 'secs': [
  {'n': '20.1', 't': 'Rationale for investment appraisal', 'b': [
    {'p': 'Where investment resources are scarce, as in most developing countries, rational '
          'allocation of capital is of the greatest importance. For a developing country to '
          'be assured that resources used on a given project have no better alternative use, '
          'in terms of the country\'s objectives, practical project appraisal is required. '
          'National governments guide investment patterns either by direct public sector '
          'investment, or by controlling private investment.'},
    {'p': 'To provide rational guidance, government must formulate and evaluate investment '
          'projects so that alternatives can be compared in terms of their contribution to '
          'national objectives. Evaluation is needed because a choice must be made among '
          'alternatives, and a clearly stated objective is essential — both as a basis for '
          'rational choice, and because without one there is no criterion to test whether a '
          'proposed action is desirable.'},
    {'key': 'Public sector project appraisal is **not** a set of techniques applied '
            'mechanically — it is an approach that must be interpreted analytically.'},
  ]},

  {'n': '20.2', 't': 'Methods of investment appraisal', 'b': [
    {'def': {'t': 'Investment appraisal', 'd': 'a technique aimed at finding the least '
                  'possible cost of an investment and the maximum economic benefits that may '
                  'accrue from committing resources to it.'}},
    {'p': 'Appraisal techniques broadly classify into **discounted cash flow (DCF)** and '
          '**non-discounted cash flow (NDCF)** methods. This syllabus covers only three:'},
    {'ol': [
      '**Accounting Rate of Return (ARR)**;',
      '**Pay-Back Period (PBP)**;',
      '**Discounted Cash Flow (DCF) using Net Present Value (NPV)**.',
    ]},
  ]},

  {'n': '20.3', 't': 'Accounting rate of return (ARR)', 'b': [
    {'def': {'t': 'Accounting Rate of Return (ARR)', 'd': 'the return on initial outlay, or '
                  'return on average capital.'}},
    {'tex': 'ARR = \\dfrac{Average\\ Annual\\ Accounting\\ Profit}{Average\\ Investment}',
      'nt': 'Average investment = (Initial investment + Residual value) / 2. Profit is '
            '"accounting profit" — income less all necessary expenses incurred in earning it, '
            'including depreciation.'},
    {'key': '**Decision rule:** pick the option with the **highest** rate of return.'},
    {'p': '**Advantages of ARR:**'},
    {'ol': [
      'Considers the profits of a project throughout its useful life;',
      'Simple to calculate and understand;',
      'Facilitates expenditure follow-up, due to more readily available data on accounting '
      'records.',
    ]},
    {'p': '**Disadvantages of ARR:**'},
    {'ol': [
      'Does not take into account the time value of money;',
      'Ignores that profits from different projects may accrue at an uneven rate;',
      'Fails to cater for risks and uncertainties.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Illustration 1 — ARR, Agbede Local Government Council', 'open': True, 'q': [
      {'p': 'Agbede Local Government Council supplies the following data on three projects:'},
      {'table': {'align': 'llll', 'head': ['Year', 'X1 (N)', 'X2 (N)', 'X3 (N)'], 'rows': [
        ['1', '1,000', '500', '5,000'],
        ['2', '2,000', '1,500', '4,000'],
        ['3', '4,000', '2,000', '500'],
        ['4', '5,000', '2,500', '1,000'],
        ['Initial investment', '15,000', '10,000', '15,000'],
        ['Residual value', '1,000', '1,000', '2,000'],
      ]}},
      {'p': 'Using the Accounting Rate of Return, in which project should Agbede Local '
            'Government Council invest?'}],
      'a': [
      {'table': {'cap': 'Computation of ARR', 'align': 'llll', 'head': ['', 'X1', 'X2', 'X3'],
        'rows': [
        ['Total accounting profit (4 years)', 'N12,000', 'N6,500', 'N10,500'],
        ['Average annual accounting profit (÷4)', 'N3,000', 'N1,625', 'N2,625'],
        ['Initial investment + residual value', 'N16,000', 'N11,000', 'N17,000'],
        ['Average investment (÷2)', 'N8,000', 'N5,500', 'N8,500'],
        ['ARR = Avg. profit / Avg. investment', '0.38', '0.30', '0.31'],
        ['ARR (%)', '**38%**', '30%', '31%'],
      ]}},
      {'p': '**Agbede Local Government Council should invest in Project X1**, which has the '
            'highest accounting rate of return of 38%.'}]}},
  ]},

  {'n': '20.4', 't': 'Pay-back period (PBP) method', 'b': [
    {'def': {'t': 'Pay-back period', 'd': 'the time an investment takes to recoup the amount '
                  'of money invested in a project, focusing only on **cash flow**, not '
                  'profit.'}},
    {'key': 'The **shorter** the payback period, the more preferable the project. A project '
            'is undertaken only if its payback period is shorter than, or at worst equal to, '
            'the maximum set standard. For a single project, payback is compared with a set '
            'standard; for **mutually exclusive** projects, they are ranked and the one with '
            'the **shortest** payback period is selected.'},
    {'p': '**Advantages of PBP:**'},
    {'ol': [
      'A useful measure of liquidity, since it selects projects offering the hope of '
      'immediate cash recoupment;',
      'May be used as a safeguard against risk, particularly if risk increases as payback '
      'lengthens;',
      'Simple to calculate and understand;',
      'Popular for public project evaluation, where liquidity predominates over '
      'profitability;',
      'Serves as a useful screen for evaluating all projects; and',
      'Uses cash flows rather than accounting profits to appraise.',
    ]},
    {'p': '**Disadvantages of PBP:**'},
    {'ol': [
      'Does not consider the time value of money;',
      'Ignores variations in the timing of cash inflows within the payback period;',
      'Cash inflows outside the payback period are ignored; and',
      'Does not take risks and uncertainties into consideration.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Illustration 2 — payback period, Omidan Local '
      'Government Council', 'open': True, 'q': [
      {'p': 'Omidan Local Government Council is considering three projects:'},
      {'table': {'align': 'llll', 'head': ['', 'B1 (N)', 'B2 (N)', 'B3 (N)'], 'rows': [
        ['Initial investment', '100,000', '150,000', '180,000'],
        ['Year 1 inflow', '70,000', '10,000', '50,000'],
        ['Year 2 inflow', '30,000', '20,000', '60,000'],
        ['Year 3 inflow', '20,000', '10,000', '80,000'],
        ['Year 4 inflow', '10,000', '40,000', '90,000'],
      ]}},
      {'p': 'Using the payback period method, advise which project should be selected.'}],
      'a': [
      {'table': {'cap': 'Cumulative recovery of initial investment', 'align': 'llll',
        'head': ['', 'B1', 'B2', 'B3'], 'rows': [
        ['Initial investment', '(100,000)', '(150,000)', '(180,000)'],
        ['After Year 1 inflow', '(30,000)', '(140,000)', '(130,000)'],
        ['After Year 2 inflow', 'NIL — recovered', '(120,000)', '(70,000)'],
        ['After Year 3 inflow', '—', '(110,000)', '10,000 — recovered'],
        ['After Year 4 inflow', '—', '(70,000) unrelieved', '—'],
      ]}},
      {'p': '**Project B1** paid off its initial capital in **Year 2**. **Project B2** could '
            'not generate enough cash inflows across all four years, leaving N70,000 '
            'unrelieved — it should be **dropped completely**. **Project B3** paid off in '
            'approximately **2.88 years**. B1 is therefore more profitable than B3.'}]}},
  ]},

  {'n': '20.5', 't': 'Net present value (NPV)', 'b': [
    {'def': {'t': 'Net Present Value (NPV)', 'd': 'the present-value equivalent of the cash '
                  'inflows and outflows from a project, discounted at a particular (given) '
                  'cost of capital — the firm/corporation\'s **opportunity cost of capital**, '
                  'equal to its required rate of return.'}},
    {'key': '**Decision rule:** a project is acceptable if it has a **positive** NPV, and '
            'rejected if it has a **negative** NPV — in total, the present value of cash '
            'inflows should exceed that of cash outflows. For **mutually exclusive** '
            'projects, rank them and select the one with the **highest** NPV.'},
    {'tex': 'NPV = \\dfrac{C_1}{(1+K)} + \\dfrac{C_2}{(1+K)^2} + \\dfrac{C_3}{(1+K)^3} + \\cdots + \\dfrac{C_n}{(1+K)^n} - C_0',
      'nt': 'C = cash inflows in each year; K = the opportunity cost of capital (discount '
            'rate); C₀ = the initial cost of the investment; n = the project\'s expected '
            'life.'},
    {'p': '**Advantages of NPV:**'},
    {'ol': [
      'Timing of cash flows is considered; and',
      'Cash flows over the entire life of the project are taken into consideration.',
    ]},
    {'p': '**Disadvantages of NPV:**'},
    {'ol': [
      'Management is obliged to determine the appropriate cost of capital to use;',
      'Not suitable where a capital rationing situation exists; and',
      'Assumes cash inflows will occur as predicted, which may not necessarily be so.',
    ]},
    {'eg': {'tag': 'Study text', 't': 'Illustration 3 — NPV, Yabus Local Government Council', 'open': True, 'q': [
      {'p': 'Yabus Local Government Council is choosing among Projects T, M and X, cost of '
            'capital 10%:'},
      {'table': {'align': 'llll', 'head': ['', 'Project T (N)', 'Project M (N)', 'Project X '
        '(N)'], 'rows': [
        ['Initial investment', '100,000', '180,000', '150,000'],
        ['Year 1', '40,000', '10,000', '50,000'],
        ['Year 2', '50,000', '30,000', '10,000'],
        ['Year 3', '60,000', '50,000', '90,000'],
        ['Year 4', '70,000', '70,000', '10,000'],
        ['Year 5', '80,000', '120,000', '40,000'],
      ]}},
      {'p': 'Discount factors at 10%: Year 1 — 0.9090; Year 2 — 0.8264; Year 3 — 0.7513; '
            'Year 4 — 0.6830; Year 5 — 0.6209. Advise which project is most viable.'}],
      'a': [
      {'table': {'cap': 'Project T — NPV computation', 'align': 'llll',
        'head': ['Year', 'Cash flow (N)', 'DF (10%)', 'DCF (N)'], 'rows': [
        ['0', '(100,000)', '1.0000', '(100,000)'],
        ['1', '40,000', '0.9090', '36,360'],
        ['2', '50,000', '0.8264', '41,320'],
        ['3', '60,000', '0.7513', '45,078'],
        ['4', '70,000', '0.6830', '47,810'],
        ['5', '80,000', '0.6209', '49,672'],
        ['**NPV**', '', '', '**120,240**'],
      ]}},
      {'table': {'cap': 'Project M — NPV computation', 'align': 'llll',
        'head': ['Year', 'Cash flow (N)', 'DF (10%)', 'DCF (N)'], 'rows': [
        ['0', '(180,000)', '1.0000', '(180,000)'],
        ['1', '10,000', '0.9090', '9,090'],
        ['2', '30,000', '0.8264', '24,792'],
        ['3', '50,000', '0.7513', '37,565'],
        ['4', '70,000', '0.6830', '47,810'],
        ['5', '120,000', '0.6209', '74,508'],
        ['**NPV**', '', '', '**13,765**'],
      ]}},
      {'table': {'cap': 'Project X — NPV computation', 'align': 'llll',
        'head': ['Year', 'Cash flow (N)', 'DF (10%)', 'DCF (N)'], 'rows': [
        ['0', '(150,000)', '1.0000', '(150,000)'],
        ['1', '50,000', '0.9090', '45,450'],
        ['2', '10,000', '0.8264', '8,264'],
        ['3', '90,000', '0.7513', '67,617'],
        ['4', '10,000', '0.6830', '6,830'],
        ['5', '40,000', '0.6209', '24,836'],
        ['**NPV**', '', '', '**2,997**'],
      ]}},
      {'p': '**Yabus Local Government Council is advised to invest in Project T**, which has '
            'the highest NPV of N120,240. Projects M and X have NPVs of N13,765 and N2,997 '
            'respectively.'}]}},
  ]},

  {'n': '20.6', 't': 'Chapter review', 'b': [
    {'p': 'It is essential for an organisation, public or private, to make investment '
          'decisions where it faces limited resources with alternative uses. Different '
          'techniques of investment appraisal — ARR, PBP and NPV — can be employed to arrive '
          'at the best course of action.'},
  ]},

  {'n': '20.7', 't': 'End of chapter review questions', 'b': [
    {'h3': 'Section A'},
    {'eg': {'tag': 'Study text', 't': 'Questions 1–8 with answers', 'open': True, 'q': [
      {'ol': [
        'The following are advantages of the Accounting Rate of Return: (i) It considers the '
        'profits of a project throughout its useful life (ii) It is simple to calculate and '
        'understand (iii) It facilitates expenditure follow-up due to more readily available '
        'data on accounting records (iv) It takes into account the time value of money. '
        '(A) (i) & (iii)  (B) (i) & (ii)  (C) (ii) & (iii)  (D) (i)–(iv)  (E) (i)–(iii)',
        'The following are disadvantages of Pay-back period, EXCEPT ONE: (A) It does not '
        'consider the time value of money  (B) It ignores variations in the timing of cash '
        'inflow within the payback period  (C) The approach uses cash flows rather than '
        'accounting profits to appraise  (D) Cash inflows outside the payback period are '
        'ignored  (E) It does not take into consideration risks and uncertainties',
        'The formula for the computation of the Net Present Value is NPV = C1/(1+K) + '
        'C2/(1+K)² + C3/(1+K)³ + … + Cn/(1+K)ⁿ − C0. What does C represent? (A) The '
        'opportunity cost of capital  (B) The initial cost of investment  (C) The project\'s '
        'expected life  (D) Cash inflows  (E) None of the above',
        'The disadvantages associated with the use of net present value include the '
        'following: (i) timing of cash flows is considered (ii) there is the obligation for '
        'management to determine the appropriate cost of capital to use (iii) there is the '
        'assumption that the cash inflows will come as predicted, which may not necessarily '
        'be so. (A) (i)–(iii)  (B) (i) & (ii)  (C) (i)–(iv)  (D) (ii)–(iv)  (E) None of the '
        'above',
        'In using the Accounting Rate of Return as an investment appraisal method, the '
        'decision rule is to pick the option which gives the ……………….',
        'When using the Pay-back period method, for mutually exclusive projects, they are '
        'ranked and the one with the ………….. period is selected.',
        'The appropriate discount rate chosen for the Net Present Value method is the firm\'s '
        'or corporation\'s …………',
        'The decision criterion applicable under the NPV method is that a project is '
        'acceptable if it has a ………….. NPV.',
      ]}],
      'a': [
      {'p': '**1.** E  **2.** C  **3.** D  **4.** D  **5.** Highest rate of return  '
            '**6.** Shortest pay-back  **7.** Opportunity cost of capital  '
            '**8.** Positive'}]}},
    {'h3': 'Section B'},
    {'eg': {'tag': 'Study text', 't': 'Question 1 — Omuro Local Government Council: PBP, NPV '
      'and ARR compared', 'open': True, 'q': [
      {'p': 'Omuro Local Government Council is considering Projects A, B and C:'},
      {'table': {'align': 'llll', 'head': ['', 'Project A (N)', 'Project B (N)', 'Project C '
        '(N)'], 'rows': [
        ['Initial investment', '15,000', '20,000', '20,000'],
        ['Residual value', '1,000', '1,000', '1,000'],
        ['Year 1 inflow', '6,000', '10,000', '1,000'],
        ['Year 2 inflow', '7,000', '10,000', '6,000'],
        ['Year 3 inflow', '8,000', '1,000', '10,000'],
        ['Year 4 inflow', '9,000', '1,000', '20,000'],
      ]}},
      {'p': 'Cost of capital is 10%. Using the Payback Period, Net Present Value and '
            'Accounting Rate of Return methods, advise which project should be selected '
            'under each.'}],
      'a': [
      {'h4': '(i) Payback period method'},
      {'p': '**Project B** was able to offset its initial capital injected in **2 years**, '
            'so it should be selected in preference to A. **Project C should be rejected** — '
            'it does not recover its outlay within the years shown.'},
      {'h4': '(ii) Net Present Value method'},
      {'table': {'align': 'llll', 'head': ['Year', 'Project A DCF (N)', 'Project B DCF (N)',
        'Project C DCF (N)'], 'rows': [
        ['0', '(15,000)', '(20,000)', '(20,000)'],
        ['1', '5,454', '9,090', '909'],
        ['2', '5,785', '8,264', '4,958'],
        ['3', '6,010', '751', '7,513'],
        ['4', '6,147', '683', '13,660'],
        ['Residual value', '683', '683', '683'],
        ['**NPV**', '**9,079**', '**(529)**', '**7,723**'],
      ]}},
      {'p': 'The Council is advised to invest in **Project A**, with the highest NPV of '
            'N9,079. **Project B has a negative NPV of N(529)** and is completely rejected. '
            '**Project C**, with a positive NPV of N7,723, is acceptable after A.'},
      {'h4': '(iii) Accounting rate of return method'},
      {'table': {'align': 'llll', 'head': ['', 'Project A', 'Project B', 'Project C'], 'rows': [
        ['Depreciation p.a. = (Cost − Residual)/4', 'N3,500', 'N4,750', 'N4,750'],
        ['Average annual accounting profit', 'N4,000', 'N750', 'N5,000'],
        ['Average investment = (Cost + Residual)/2', 'N8,000', 'N10,500', 'N10,500'],
        ['ARR', '0.50 or **50%**', '0.0714 or 7.14%', '0.4762 or 47.62%'],
      ]}},
      {'p': 'The Council should invest in **Project A**, with the highest ARR of '
            'approximately 50%. **Project C** ranks second, **Project B** third.'}]}},
  ]},
 ],
 'formulas': [
   {'lb': 'Accounting Rate of Return (ARR)', 'tex': 'ARR = \\dfrac{Average\\ Annual\\ Accounting\\ Profit}{Average\\ Investment}', 'nt': 'Average investment = (Initial investment + Residual value) / 2. Pick the option with the highest ARR.'},
   {'lb': 'Net Present Value (NPV)', 'tex': 'NPV = \\sum_{t=1}^{n} \\dfrac{C_t}{(1+K)^t} - C_0', 'nt': 'K = opportunity cost of capital; C0 = initial outlay. Accept if NPV > 0; for mutually exclusive projects, pick the highest NPV.'},
 ],
 'focus':
   'Practise all three methods on the same set of cash flows until switching between them is '
   'automatic — ARR wants average accounting profit over average investment (pick highest); '
   'PBP wants the year cumulative inflows first cover the outlay (pick shortest); NPV wants '
   'discounted cash flows minus the initial outlay (pick highest, but only if positive). '
   'Watch for questions that quietly include a **residual value**, discounted in its own '
   'right in the NPV working and added into the "investment" figure for ARR.',
 'errors': [
   'Forgetting to discount the residual value in an NPV computation — it is a cash inflow '
   'in the final year (or its own row) and must be multiplied by that year\'s discount '
   'factor, not added at face value.',
   'Ranking projects on payback period alone when the question asks for NPV or ARR — each '
   'method can give a different preferred project, and the decision rule differs (shortest '
   'time vs highest return vs highest discounted value).',
   'Using total inflows instead of average annual accounting profit in the ARR numerator, or '
   'forgetting to add the residual value into the average investment denominator.',
   'Treating a negative NPV project as merely "less good" — under the NPV decision rule it '
   'must be rejected outright, not just ranked lower.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Under the Accounting Rate of Return method, average investment is calculated as',
    'o': ['Initial investment only', '(Initial investment + Residual value) / 2',
          'Total accounting profit / number of years', 'Initial investment − Residual value',
          'Average annual cash inflow'],
    'a': 1,
    'w': 'Average investment averages the initial outlay and what is left over (residual '
         'value) at the end of the project\'s life.',
    'src': 'Chapter 20.3', 'sec': '20.3'},
   {'q': 'A project with an initial outlay of N200,000 recovers N90,000 in Year 1, N80,000 '
         'in Year 2 and N70,000 in Year 3. Under the payback period method, in which year is '
         'the outlay recovered?',
    'o': ['Year 1', 'Year 2', 'Year 3', 'It is never recovered', 'Cannot be determined'],
    'a': 2,
    'w': 'Cumulative inflows: Year 1 = 90,000 (200,000 − 90,000 = 110,000 outstanding); '
         'Year 2 = 170,000 (30,000 outstanding); Year 3 brings cumulative inflows to '
         '240,000, exceeding the 200,000 outlay partway through the year — so payback falls '
         'within Year 3.',
    'src': 'Chapter 20.4', 'sec': '20.4'},
   {'q': 'Under the Net Present Value decision rule, a project should be',
    'o': ['Accepted only if its IRR exceeds its ARR', 'Accepted if its NPV is positive, '
          'rejected if negative', 'Accepted regardless of the sign of its NPV, provided the '
          'payback is short', 'Ranked only by its undiscounted total cash inflow',
          'Accepted only if its NPV equals exactly zero'],
    'a': 1,
    'w': 'A positive NPV means the discounted inflows exceed the discounted outflows '
         '(including the initial outlay), making the project acceptable; a negative NPV '
         'means it should be rejected.',
    'src': 'Chapter 20.5', 'sec': '20.5'},
  ],
  'theory': [
   {'q': 'A Local Government invests N50,000 in a project with a residual value of N5,000 '
         'after 4 years, generating accounting profits of N8,000, N10,000, N12,000 and '
         'N14,000 in years 1–4. Calculate the Accounting Rate of Return.',
    'marks': 6,
    'a': [
      {'p': 'Total accounting profit = 8,000 + 10,000 + 12,000 + 14,000 = **N44,000**. '
            'Average annual accounting profit = 44,000 / 4 = **N11,000**.'},
      {'p': 'Average investment = (50,000 + 5,000) / 2 = **N27,500**.'},
      {'tex': 'ARR = \\dfrac{11{,}000}{27{,}500} = 0.40\\ or\\ 40\\%'}],
    'src': 'Chapter 20.3', 'sec': '20.3'},
   {'q': 'A project costs N120,000 and is expected to generate cash inflows of N50,000, '
         'N45,000, N40,000 and N35,000 in years 1–4. Using discount factors of 0.9091, '
         '0.8264, 0.7513 and 0.6830 at 10%, calculate the NPV and advise whether the project '
         'should be accepted.',
    'marks': 10,
    'a': [
      {'table': {'align': 'llll', 'head': ['Year', 'Cash flow (N)', 'DF (10%)', 'DCF (N)'],
        'rows': [
        ['0', '(120,000)', '1.0000', '(120,000)'],
        ['1', '50,000', '0.9091', '45,455'],
        ['2', '45,000', '0.8264', '37,188'],
        ['3', '40,000', '0.7513', '30,052'],
        ['4', '35,000', '0.6830', '23,905'],
        ['**NPV**', '', '', '**16,600**'],
      ]}},
      {'p': 'Since the NPV is **positive (N16,600)**, the project should be **accepted**.'}],
    'src': 'Chapter 20.5', 'sec': '20.5'},
   {'q': 'State any three advantages and three disadvantages of the Payback Period method of '
         'investment appraisal.',
    'marks': 6,
    'a': [
      {'h4': 'Advantages (any three)'},
      {'ul': ['A useful measure of liquidity, selecting projects with hope of quick cash '
        'recoupment.', 'Simple to calculate and understand.', 'Popular in public project '
        'evaluation, where liquidity predominates over profitability.', 'Uses cash flows, '
        'not accounting profits, to appraise.']},
      {'h4': 'Disadvantages (any three)'},
      {'ul': ['Does not consider the time value of money.', 'Ignores variations in the '
        'timing of cash inflows within the payback period.', 'Cash inflows outside the '
        'payback period are ignored.', 'Does not take risk and uncertainty into account.']}],
    'src': 'Chapter 20.4', 'sec': '20.4'},
  ]},
}
