CH = {
 'n': 12,
 't': 'Mathematics of Finance',
 'brief': 'Sequences and series (AP and GP), simple and compound interest applied to business, '
          'and Net Present Value (NPV) and Internal Rate of Return (IRR).',
 'outcomes': [
   'Define sequences and series',
   'Identify Arithmetic Progression (AP) and Geometric Progression (GP)',
   'Find the nth term and sum of the first n terms of an AP and a GP',
   'Understand simple interest and compound interest',
   'Define and understand annuities',
   'Calculate Present Value (PV), NPV and IRR',
   'Apply all of the above to economic and business problems',
 ],
 'secs': [
  {'n': '12.1', 't': 'Sequences and series', 'b': [
    {'def': {'t': 'Sequence', 'd': 'a set of numbers that follow a definite pattern — e.g. '
                  '7, 12, 17, 22, ... (each term is the one before it, plus 5), or 256, 64, 16, '
                  '4, ... (each term is the one before it, divided by 4).'}},
    {'def': {'t': 'Series', 'd': 'the sum obtained when the terms of a sequence are connected by '
                  'plus or minus signs — e.g. $7+12+17+22+\\cdots$.'}},
  ]},

  {'n': '12.2', 't': 'Arithmetic Progression (AP)', 'b': [
    {'def': {'t': 'Arithmetic Progression', 'd': 'a sequence in which each term increases or '
                  'decreases from the one before it by a constant number, called the **common '
                  'difference** $d$. The first term is $a$.'}},
    {'p': 'An AP has the general form $a,\\ a+d,\\ a+2d,\\ a+3d, \\ldots$, so the $n$th term is '
          '$a+(n-1)d$.'},
    {'fbox': {'h': 'Arithmetic Progression', 'rows': [
      {'lb': '$n$th term', 'tex': 'T_n = a + (n-1)d'},
      {'lb': 'Sum of the first $n$ terms',
       'tex': 'S_n = \\frac{n}{2}\\{2a+(n-1)d\\} = \\frac{n}{2}(a+l)',
       'nt': '$l$ is the last term.'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.1 — nth term, sum, and finding n', 'open': True,
      'q': [
      {'ol': [
        'Find the 12th term of the AP $7, 13, 19, 25, \\ldots$',
        'Find the difference between the 8th and 52nd terms of the AP $210, 205, 200, \\ldots$',
        'Find the sum of the first 10 terms of the APs in (a) and (b).',
        'How many terms of the series $15+18+21+\\cdots$ are needed to obtain a sum of 870?',
      ]}],
      'a': [
      {'p': '**(a)** $a=7$, $d=6$, $n=12$: $T_{12}=7+(12-1)6=73$.'},
      {'p': '**(b)** $a=210$, $d=-5$: $T_8=210+7(-5)=175$; $T_{52}=210+51(-5)=-45$. Difference '
            '$=175-(-45)=220$.'},
      {'p': '**(c)** For (a): $S_{10}=\\frac{10}{2}\\{2(7)+9(6)\\}=340$. For (b): '
            '$S_{10}=\\frac{10}{2}\\{2(210)+9(-5)\\}=1{,}875$.'},
      {'p': '**(d)** $a=15$, $d=3$, $S_n=870$: $870=\\frac{n}{2}\\{30+(n-1)3\\}$, which reduces '
            'to $n^2+9n-580=0$, i.e. $(n-20)(n+29)=0$. Since $n$ cannot be negative, '
            '$n=20$.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.2 — a salary and gratuity AP', 'open': True,
      'q': [
      {'p': 'Mr. Emeka earns ₦240,000 per annum with an annual constant increment of ₦25,000.'},
      {'ol': [
        'How much will his annual salary be in the eighth year?',
        'What will his monthly salary be during the 15th year?',
        'If he retires after 30 years, and his gratuity is 250% of his terminal annual salary, '
        'how much will he be paid as gratuity?',
      ]}],
      'a': [
      {'p': '$a=240{,}000$, $d=25{,}000$.'},
      {'p': '**(a)** $T_8=240{,}000+7(25{,}000)=\\text{\\textnaira}415{,}000$.'},
      {'p': '**(b)** $T_{15}=240{,}000+14(25{,}000)=\\text{\\textnaira}590{,}000$ a year, so '
            'monthly $=590{,}000/12=\\text{\\textnaira}49{,}166.67$.'},
      {'p': '**(c)** $T_{30}=240{,}000+29(25{,}000)=\\text{\\textnaira}965{,}000$ (terminal '
            'salary). Gratuity $=250\\%\\times965{,}000=\\text{\\textnaira}2{,}412{,}500$.'}]}},
  ]},

  {'n': '12.3', 't': 'Geometric Progression (GP)', 'b': [
    {'def': {'t': 'Geometric Progression', 'd': 'a sequence in which each term increases or '
                  'decreases from the one before it by a constant ratio, called the **common '
                  'ratio** $r$. The first term is $a$.'}},
    {'p': 'A GP has the general form $a,\\ ar,\\ ar^2,\\ ar^3,\\ldots$, so the $n$th term is '
          '$ar^{n-1}$.'},
    {'fbox': {'h': 'Geometric Progression', 'rows': [
      {'lb': '$n$th term', 'tex': 'T_n = ar^{\\,n-1}'},
      {'lb': 'Sum of the first $n$ terms ($r<1$)', 'tex': 'S_n = \\frac{a(1-r^n)}{1-r}'},
      {'lb': 'Sum of the first $n$ terms ($r>1$)', 'tex': 'S_n = \\frac{a(r^n-1)}{r-1}'},
      {'lb': 'Sum to infinity ($|r|<1$)', 'tex': 'S_\\infty = \\frac{a}{1-r}',
       'nt': 'As $n\\to\\infty$ with $r<1$, $r^n\\to0$, so $S_n$ converges to this value.'},
    ]}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.3 — nth term, sum, and sum to infinity',
      'open': True, 'q': [
      {'ol': [
        'Find the 7th term of the GP $8, 16, 32, \\ldots$',
        'Find the 6th term of the GP $243, 81, 27, \\ldots$',
        'Find the sum of the first 15 terms of the GPs in (a) and (b).',
        'Find the sum to infinity for the GPs in (a) and (b).',
      ]}],
      'a': [
      {'p': '**(a)** $a=8$, $r=2$: $T_7=8(2)^6=512$.'},
      {'p': '**(b)** $a=243$, $r=1/3$: $T_6=243(1/3)^5=1$.'},
      {'p': '**(c)(i)** $r=2>1$: $S_{15}=\\dfrac{8(2^{15}-1)}{2-1}=262{,}136$.'},
      {'p': '**(c)(ii)** $r=1/3<1$: $S_{15}=\\dfrac{243(1-(1/3)^{15})}{1-1/3}=364.5$.'},
      {'p': '**(d)(i)** $r=2$: no sum to infinity exists, since $S_\\infty$ requires $|r|<1$.'},
      {'p': '**(d)(ii)** $r=1/3$: $S_\\infty=\\dfrac{243}{1-1/3}=364.5$ — note this already '
            'equals $S_{15}$, i.e. the series has effectively converged by $n=15$.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.7 — the same asset, two depreciation methods',
      'open': True, 'q': [
      {'p': 'GODSLOVE Enterprises purchased a machine for ₦930,000, expected to last 25 years, '
            'with a scrap value of ₦65,000.'},
      {'ol': [
        'How much should be provided each year if depreciation is on the straight-line method?',
        'What depreciation rate is required if depreciation is on the reducing-balance method?',
      ]}],
      'a': [
      {'note': 'The number of terms is **one more** than the number of years, because the cost '
               'is the value at the start of year 1 and the scrap value is at the end of the '
               'final year: $a=930{,}000$, $n=26$.'},
      {'p': '**(a) Straight line — an AP.** $65{,}000=a+(n-1)d=930{,}000+25d$, so '
            '$d=\\dfrac{65{,}000-930{,}000}{25}=-\\text{\\textnaira}34{,}600$ (provide '
            '₦34,600 a year).'},
      {'p': '**(b) Reducing balance — a GP.** $65{,}000=ar^{n-1}=930{,}000\\,r^{25}$, so '
            '$r=(65{,}000/930{,}000)^{1/25}=0.90$. The depreciation rate is $1-0.90=10\\%$.'}]}},
  ]},

  {'n': '12.4', 't': 'Simple interest', 'b': [
    {'def': {'t': 'Simple interest', 'd': 'the interest that accrues on the principal (the '
                  'original money invested or borrowed) for the period for which the money is '
                  'invested or borrowed. If $P$ is the principal, $r$ the rate of interest and '
                  '$n$ the number of periods, $I = Prn$; the amount at the end of period $n$ is '
                  '$A_n = P+I = P(1+rn)$.'}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.8 — interest, amount, and time to triple',
      'open': True, 'q': [
      {'ol': [
        'What is the interest that will accrue on ₦25,000 at 12% simple interest at the end of '
        '15 years, and how much will it amount to?',
        'How long will it take money to triple itself at 9.5% simple interest?',
      ]}],
      'a': [
      {'p': '**(a)** $I=Prn=25{,}000(0.12)(15)=\\text{\\textnaira}45{,}000$. Amount '
            '$=A_{15}=25{,}000+45{,}000=\\text{\\textnaira}70{,}000$ (equivalently '
            '$25{,}000\\{1+(0.12)(15)\\}$).'},
      {'p': '**(b)** For $P$ to become $3P$: $3P=P(1+rn)$, so $3=1+0.095n$, giving '
            '$n=\\dfrac{2}{0.095}=21.05$ years.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.9 — present value under simple interest',
      'open': True, 'q': [
      {'p': 'Mohammed wants to buy a house for ₦1.80m in 5 years\' time. The interest rate is a '
            'constant 10% per annum, simple interest. How much should he invest now?'}],
      'a': [
      {'tex': 'A_n = P(1+rn) \\;\\Rightarrow\\; P = \\frac{A_n}{1+rn}'},
      {'tex': 'P = \\frac{1.80\\text{m}}{1+(0.10)(5)} = \\frac{1.80\\text{m}}{1.5} = '
              '\\text{\\textnaira}1.20\\text{m}'},
      {'note': '₦1.20m is the **present value** of ₦1.80m under these conditions — equivalently, '
               'the present value of ₦1.80m at 10% simple interest over 5 years.'}]}},
  ]},

  {'n': '12.5', 't': 'Compound interest', 'b': [
    {'def': {'t': 'Compound interest', 'd': 'interest calculated on the principal **and** on '
                  'interest already earned — "multi-stage single-period simple interest". The '
                  'interest for one period is added to the principal to form the new principal '
                  'for the next period, and so on. It is the type of interest commonly used by '
                  'banks and financial institutions.'}},
    {'fbox': {'h': 'Compound interest', 'rows': [
      {'lb': 'Amount after $n$ periods', 'tex': 'A_n = P(1+r)^n'},
      {'lb': 'Present value', 'tex': 'P = \\frac{A_n}{(1+r)^n}',
       'nt': 'This rearrangement is the basis of every discounted cash flow (DCF) technique, '
             'including NPV.'},
    ]}},
    {'note': 'The accrued amount under compound interest is always **more** than under simple '
             'interest, because simple interest is charged repeatedly on the same, unchanging '
             'principal, while compound interest is charged on a principal that itself grows '
             'each period.'},
    {'eg': {'tag': 'Study text', 't': 'Example 12.10 — building up the amount year by year',
      'open': True, 'q': [
      {'p': 'How much will ₦200,000 amount to at 8% per annum compound interest over 5 '
            'years?'}],
      'a': [
      {'table': {'align': 'lrrr', 'head': ['Year', 'Principal (₦)', 'Interest (₦)', 'Amount (₦)'],
        'rows': [
        ['1', '200,000.0', '16,000.0', '216,000.0'],
        ['2', '216,000.0', '17,280.0', '233,280.0'],
        ['3', '233,280.0', '18,662.4', '251,942.4'],
        ['4', '251,942.4', '20,155.4', '272,097.8'],
        ['5', '272,097.8', '21,767.8', '293,865.6'],
      ]}},
      {'p': 'The required amount is **₦293,865.60**. By contrast, at simple interest '
            '$A_5=200{,}000\\{1+(0.08)(5)\\}=\\text{\\textnaira}280{,}000$ — less than the '
            'compound-interest amount, as expected.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.11 — the compound interest formula direct',
      'open': True, 'q': [
      {'ol': [
        'Use the compound interest formula to calculate the amount for Example 12.10.',
        'What compound interest rate is required to obtain ₦230,000 after 6 years from an '
        'initial principal of ₦120,000?',
        'How long will it take a sum of money to triple itself at 9.5% compound interest?',
        'How much will ₦250,000 amount to in 3 years if the interest rate is 12% per annum, '
        'compounded quarterly?',
      ]}],
      'a': [
      {'p': '**(a)** $A_5=200{,}000(1.08)^5=200{,}000(1.469328)=\\text{\\textnaira}293{,}865.60$ '
            '— matches Example 12.10.'},
      {'p': '**(b)** $230{,}000=120{,}000(1+r)^6 \\Rightarrow (1+r)^6=1.916667 \\Rightarrow '
            '1+r=1.916667^{1/6}=1.1145$, so $r\\approx11.5\\%$.'},
      {'p': '**(c)** $3P=P(1.095)^n \\Rightarrow n=\\dfrac{\\log3}{\\log1.095}=12.11$ years — '
            'markedly less than the 21.05 years needed under **simple** interest (Example 12.8) '
            'for the same 9.5% rate to triple a sum.'},
      {'p': '**(d)** Quarterly compounding over 3 years: $r=0.12/4=0.03$ per quarter, '
            '$n=4\\times3=12$ quarters. $A_{12}=250{,}000(1.03)^{12}=\\text{\\textnaira}'
            '356{,}440.22$.'}]}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.12 — present value under compound interest',
      'open': True, 'q': [
      {'p': 'Calculate the sum of money that needs to be invested now at 9% compound interest '
            'to yield ₦320,000 at the end of 8 years.'}],
      'a': [
      {'tex': 'P = \\frac{A_n}{(1+r)^n} = \\frac{320{,}000}{(1.09)^8} = '
              '\\text{\\textnaira}160{,}597.21'},
      {'note': '₦160,597.21 is the present value of ₦320,000 under these conditions.'}]}},
  ]},

  {'n': '12.6', 't': 'Annuities', 'b': [
    {'def': {'t': 'Annuity', 'd': 'a sequence of constant cash flows received or paid — e.g. '
                  'weekly/monthly wages, hire-purchase payments, or mortgage payments.'}},
    {'h4': 'Types of annuity'},
    {'ul': [
      '**Ordinary annuity** — paid at the **end** of each payment period; the one most '
      'commonly used.',
      '**Annuity due (due annuity)** — paid at the **beginning** of each payment period (i.e. '
      'in advance).',
      '**Certain annuity** — a term that begins and ends on fixed dates.',
      '**Perpetual annuity (perpetuity)** — one that goes on indefinitely.',
    ]},
    {'h4': 'Sum of an ordinary annuity (sinking fund)'},
    {'p': 'The sum $S$ of an ordinary annuity of payment $A$ at interest rate $r$ per annum, '
          'compounded over $n$ periods, is $S=A+A(1+r)+A(1+r)^2+\\cdots+A(1+r)^{n-1}$ — a GP '
          'with first term $A$ and common ratio $(1+r)$, giving:'},
    {'tex': 'S = A\\left[\\frac{(1+r)^n - 1}{r}\\right]'},
    {'eg': {'tag': 'Study text', 't': 'Example 12.13 — sinking fund, both directions', 'open': True,
      'q': [
      {'ol': [
        'Find the amount of an annuity of ₦50,000 per year at 4% interest per annum for 7 '
        'years.',
        'Calculate the annual amount to be paid over 4 years for a sinking fund of ₦2,886,555 '
        'if the compound interest rate is 7.5% per annum.',
      ]}],
      'a': [
      {'p': '**(a)** $A=50{,}000$, $r=0.04$, $n=7$: '
            '$S=50{,}000\\left[\\dfrac{(1.04)^7-1}{0.04}\\right]=\\text{\\textnaira}394{,}914.72$.'},
      {'p': '**(b)** $S=2{,}886{,}555$, $r=0.075$, $n=4$, solve for $A$: '
            '$A=\\dfrac{2{,}886{,}555\\times0.075}{(1.075)^4-1}=\\text{\\textnaira}174{,}267.22$.'}]}},
    {'h4': 'Present value of an annuity'},
    {'p': 'The present value of an annuity is the sum of the present values of all the '
          'periodical payments — itself a GP with common ratio $\\dfrac{1}{1+r}$, giving:'},
    {'tex': 'P = \\frac{A\\left[1-(1+r)^{-n}\\right]}{r}'},
    {'eg': {'tag': 'Study text', 't': 'Example 12.14 — present value of an annuity', 'open': True,
      'q': [
      {'p': 'Determine the present value of an annuity of ₦45,000 for 9 years at 5.5% '
            'compounded annually.'}],
      'a': [
      {'tex': 'P = \\frac{45{,}000\\left[1-(1.055)^{-9}\\right]}{0.055} = '
              '\\text{\\textnaira}312{,}848.79'}]}},
  ]},

  {'n': '12.7', 't': 'Net Present Value (NPV) and Internal Rate of Return (IRR)', 'b': [
    {'def': {'t': 'Net Present Value (NPV)', 'd': 'the sum of the present values of all future '
                  'net cash flows of an investment (each may be positive or negative). If the '
                  'NPV is positive the investment is desirable; if negative, it is not worth '
                  'it.'}},
    {'tex': 'NPV = A_0 + \\frac{A_1}{1+r} + \\frac{A_2}{(1+r)^2} + \\frac{A_3}{(1+r)^3} + '
            '\\cdots'},
    {'p': '$A_0$ is the cost of the investment at year 0, always recorded as a **negative** '
          '(cash outflow) in the NPV calculation; $A_1, A_2, \\ldots, A_n$ are the expected net '
          'cash flows for years 1, 2, ..., $n$.'},
    {'p': 'A project is assessed by assuming a discount rate, then finding the present value of '
          'every flow of money in and out; the total present value of the money in (revenue) '
          'less the total present value of the money out (costs) is the NPV.'},
    {'eg': {'tag': 'Study text', 't': 'Example 12.15 — NPV computed year by year', 'open': True,
      'q': [
      {'p': 'A project is presently estimated to cost ₦1.1m. The net cash flows for the first 4 '
            'years are estimated at ₦225,000, ₦475,000, ₦655,000 and ₦300,000. The discount '
            'rate is 12%.'},
      {'ol': [
        'Calculate the NPV for the project.',
        'Is the project desirable?',
        'If ₦95,000 and ₦125,000 were spent on the project during the second and fourth years '
        'respectively, will the project still be desirable?',
      ]}],
      'a': [
      {'table': {'align': 'lrrr',
        'head': ['Year', 'Net cash flow (₦)', 'DF at 12%', 'PV (₦)'], 'rows': [
        ['0', '(1,100,000)', '1.0000', '(1,100,000.0)'],
        ['1', '225,000', '0.8929', '200,902.5'],
        ['2', '475,000', '0.7972', '378,770.0'],
        ['3', '655,000', '0.7118', '466,229.0'],
        ['4', '300,000', '0.6355', '190,650.0'],
        ['NPV', '', '', '136,551.5'],
      ]}},
      {'p': '**(a)** NPV $=\\text{\\textnaira}136{,}551.50$. **(b)** Since the NPV is positive, '
            'the project is **desirable**.'},
      {'p': '**(c)** New net cash flow, year 2 $=475{,}000-95{,}000=380{,}000$; year 4 '
            '$=300{,}000-125{,}000=175{,}000$.'},
      {'table': {'align': 'lrrr',
        'head': ['Year', 'Net cash flow (₦)', 'DF at 12%', 'PV (₦)'], 'rows': [
        ['0', '(1,100,000)', '1.0000', '(1,100,000.0)'],
        ['1', '225,000', '0.8929', '200,902.5'],
        ['2', '380,000', '0.7972', '302,936.0'],
        ['3', '655,000', '0.7118', '466,229.0'],
        ['4', '175,000', '0.6355', '111,212.5'],
        ['NPV', '', '', '(18,720.0)'],
      ]}},
      {'p': 'The NPV is now **negative**, so the project is **not desirable**.'}]}},
    {'h4': 'Internal Rate of Return (IRR)'},
    {'def': {'t': 'Internal Rate of Return (IRR)', 'd': 'the discount rate at which a project\'s '
                  'net present value is zero. If an investor can earn more than the IRR '
                  'elsewhere, or must pay more than the IRR to borrow to finance the project, '
                  'the project is not worthwhile.'}},
    {'eg': {'tag': 'Study text', 't': 'Example 12.16–12.18 — narrowing in on the IRR', 'open': True,
      'q': [
      {'p': 'A company can buy a machine now for ₦2.5m, to manufacture an order paying ₦1.75m '
            'after 2 years and ₦1.25m after 3 years.'},
      {'ol': [
        'At a 5% discount rate, calculate the NPV.',
        'Recompute the NPV at 7%, and again at 8%.',
        'Estimate the internal rate of return.',
      ]}],
      'a': [
      {'p': '**At 5%:**'},
      {'table': {'align': 'lrr', 'head': ['End of year', 'Net cash flow', 'PV (₦)'], 'rows': [
        ['0', '(2,500,000)', '(2,500,000.0)'],
        ['2', '+1,750,000', '1,587,301.6'],
        ['3', '+1,250,000', '1,079,797.0'],
        ['NPV', '', '167,098.6'],
      ]}},
      {'p': 'NPV is positive (₦167,098.60), so the machine purchase is worthwhile at 5%.'},
      {'p': '**At 7%:** NPV falls to **₦48,890.10** (still positive, but much smaller). '
            '**At 8%:** NPV falls to **-₦7,366.80** (now negative).'},
      {'p': 'The project therefore breaks even — NPV $=0$ — at a discount rate between 7% and '
            '8%: this break-even rate is the **IRR**.'},
      {'note': 'Where a project has just one future cash inflow, the IRR can be found directly '
               'by algebra instead of narrowing between two trial rates: if a financial group '
               'invests ₦85m now and receives ₦100m in 2 years\' time, '
               '$-85\\text{m}+\\dfrac{100\\text{m}}{(1+i)^2}=0 \\Rightarrow (1+i)^2=\\dfrac{100}'
               '{85} \\Rightarrow i=\\left(\\dfrac{100}{85}\\right)^{1/2}-1=0.084652$, an IRR of '
               'about **8.47%**.'}]}},
  ]},

  {'n': '12.8', 't': 'Worksheet summary — every term and formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§12.1 Sequences and series** — a sequence follows a definite pattern; a series is the '
      'sum of its terms.',
      '**§12.2 AP** — constant **difference** $d$; $T_n=a+(n-1)d$; $S_n=\\frac n2\\{2a+(n-1)d\\}'
      '=\\frac n2(a+l)$.',
      '**§12.3 GP** — constant **ratio** $r$; $T_n=ar^{n-1}$; $S_n=a(1-r^n)/(1-r)$ (for $r<1$) '
      'or $a(r^n-1)/(r-1)$ (for $r>1$); sum to infinity $S_\\infty=a/(1-r)$, only for $|r|<1$. '
      'Straight-line depreciation is an AP (constant naira amount); reducing-balance '
      'depreciation is a GP (constant rate/ratio) — the **same** asset can be modelled either '
      'way, with a term count of (years $+$ 1) since cost is at the start of year 1 and scrap '
      'value at the end of the final year.',
      '**§12.4 Simple interest** — $I=Prn$; $A_n=P(1+rn)$; $P=A_n/(1+rn)$.',
      '**§12.5 Compound interest** — "multi-stage single-period simple interest"; '
      '$A_n=P(1+r)^n$; $P=A_n/(1+r)^n$ (the basis of every discounted cash flow technique). '
      'The compound amount always exceeds the simple-interest amount over the same term.',
      '**§12.6 Annuities** — a sequence of constant cash flows: **ordinary** (end of period), '
      '**due** (start of period, in advance), **certain** (fixed start/end dates), **perpetual** '
      '(goes on indefinitely). Sum (sinking fund) $S=A[(1+r)^n-1]/r$; present value '
      '$P=A[1-(1+r)^{-n}]/r$ — both derived as a GP.',
      '**§12.7 NPV and IRR** — $NPV=A_0+\\sum A_t/(1+r)^t$, $A_0$ always negative; positive NPV '
      '$\\Rightarrow$ desirable. IRR is the discount rate at which NPV $=0$ — found either by '
      'narrowing between a positive- and a negative-NPV trial rate, or (for a single future '
      'cash flow) directly by algebra.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Sequence** — a set of numbers following a definite pattern. **Series** — their sum.',
      '**Arithmetic Progression (AP)** — constant common **difference** $d$; first term $a$.',
      '**Geometric Progression (GP)** — constant common **ratio** $r$; first term $a$.',
      '**Simple interest** — interest on the original principal only, $I=Prn$.',
      '**Compound interest** — interest earned on interest already accrued, $A_n=P(1+r)^n$.',
      '**Present value (PV)** — the current worth of a future amount, based on prevailing '
      'conditions.',
      '**Annuity** — a sequence of constant cash flows, received or paid.',
      '**Ordinary annuity / annuity in arrears** — paid at the end of each period.',
      '**Annuity due** — paid at the beginning of each period (in advance).',
      '**Certain annuity** — fixed start and end dates. **Perpetuity** — continues '
      'indefinitely.',
      '**Net Present Value (NPV)** — the sum of the present values of all a project\'s future '
      'net cash flows.',
      '**Internal Rate of Return (IRR)** — the discount rate at which NPV $=0$.',
    ]},
  ]},

  {'n': '12.9', 't': 'End-of-chapter questions (study text)', 'b': [
    {'eg': {'tag': 'Study text', 't': 'Multiple-choice and short-answer questions, with answers',
      'open': True, 'q': [
      {'ol': [
        'If the 4th term of a geometric progression is $-108$ and the 6th term is $-972$, the '
        'common ratio is (A) $+3$  (B) $-3$  (C) $3$  (D) $9$  (E) $-9$',
        'Determine the present value of ¢450,000 in 3 years\' time if the discount rate is 6% '
        'compounded annually. (A) ¢377,826.68  (B) ¢386,772.68  (C) ¢268,386.68  '
        '(D) ¢338,277.68  (E) ¢287,768.68',
        'The lifespan of a machine costing ₦2.5m is 15 years and has a scrap value of '
        '₦150,000. If depreciation is on the straight line method, the amount to be provided '
        'each year is (A) ₦157,666.67  (B) ₦167,666.67  (C) ₦156,777.67  (D) ₦156,666.67  '
        '(E) ₦167,777.67',
        'Mr. Nokoe earns ¢50,000 per month with an annual increment of 5%. What will his annual '
        'salary be in the 4th year? (A) ¢561,500  (B) ¢651,500  (C) ¢515,500  (D) ¢615,500  '
        '(E) ¢661,500',
        'If the discount rate of 6% in Question 2 is compounded six-monthly, the present value '
        'will be …',
        'A project is said to be desirable if the net present value is …',
        'The present value of ₦2.8m at 15% simple interest rate over six years is …',
        'The time that a sum of money will take to triple itself using simple interest is '
        '… than that of compound interest.',
        'An annuity is a sequence of … cash flows … or paid.',
        'The discount rate that occurs when the net present value is zero is known as …',
      ]}],
      'a': [
      {'ol': [
        '**B** — $ar^5/ar^3=r^2=(-972)/(-108)=9 \\Rightarrow r=\\pm3$; since $ar^3=-108$ '
        '(negative) with an even power of a negative $r$ giving a negative result, '
        '$r=-3$.',
        '**A** — $P=450{,}000/(1.06)^3=$ ¢377,826.68 (option A, once rounding is carried '
        'through consistently).',
        '**D** — $a=2{,}500{,}000$, $n=16$ (15 years $+$ 1), scrap $=150{,}000$: '
        '$d=(150{,}000-2{,}500{,}000)/15=$ ₦156,666.67.',
        '**E** — ¢50,000/month $=$ ¢600,000/annum; $a=600{,}000$, $r=1.05$: '
        '$T_4=ar^3=600{,}000(1.05)^3=$ ¢661,500.',
        'PV $=450{,}000/(1.03)^6=$ ₦317,232.24 (rate halved, periods doubled for six-monthly '
        'compounding).',
        '**Positive.**',
        '$A_n=P(1+rn)$: $2.8\\text{m}=P\\{1+(0.15)(6)\\}=1.9P \\Rightarrow P=2.8\\text{m}/1.9='
        '\\text{\\textnaira}1.47\\text{m}$.',
        '**More** (simple interest takes longer to triple a sum than compound interest — '
        '21.05 years against 12.11 years at 9.5%, per Examples 12.8 and 12.11).',
        '**Constant**, **received** (in that order).',
        '**Internal Rate of Return (IRR).**',
      ]}]}},
  ]},
 ],
 'formulas': [
  {'lb': 'AP: $n$th term', 'tex': 'T_n = a + (n-1)d'},
  {'lb': 'AP: sum of $n$ terms', 'tex': 'S_n = \\frac{n}{2}\\{2a+(n-1)d\\} = \\frac{n}{2}(a+l)'},
  {'lb': 'GP: $n$th term', 'tex': 'T_n = ar^{\\,n-1}'},
  {'lb': 'GP: sum of $n$ terms',
   'tex': 'S_n = \\frac{a(1-r^n)}{1-r} \\ (r<1) \\quad\\text{or}\\quad \\frac{a(r^n-1)}{r-1} '
          '\\ (r>1)'},
  {'lb': 'GP: sum to infinity', 'tex': 'S_\\infty = \\frac{a}{1-r} \\ (|r|<1)'},
  {'lb': 'Simple interest', 'tex': 'I = Prn'},
  {'lb': 'Simple interest amount', 'tex': 'A_n = P(1+rn)'},
  {'lb': 'Compound interest amount', 'tex': 'A_n = P(1+r)^n'},
  {'lb': 'Present value (compound)', 'tex': 'P = \\frac{A_n}{(1+r)^n}'},
  {'lb': 'Sum of an ordinary annuity (sinking fund)',
   'tex': 'S = A\\left[\\frac{(1+r)^n-1}{r}\\right]'},
  {'lb': 'Present value of an ordinary annuity',
   'tex': 'P = \\frac{A\\left[1-(1+r)^{-n}\\right]}{r}'},
  {'lb': 'Net present value', 'tex': 'NPV = A_0 + \\sum_{t=1}^{n} \\frac{A_t}{(1+r)^t}'},
 ],
 'focus':
   'The single most heavily examined chapter in the paper. Expect Section A marks on AP/GP terms '
   'and sums, simple-vs-compound interest, and sinking-fund/annuity present values, plus a full '
   'Section B question most diets on NPV (often built up year by year exactly as the study text '
   'does it, with a discount-factor column) or occasionally IRR. Learn to recognise whether a '
   'salary/depreciation/cash-flow pattern is an AP (constant naira change) or a GP (constant % '
   'change) before reaching for a formula.',
 'errors': [
   'Using the wrong number of terms in a depreciation AP/GP — remember it is (years $+$ 1), '
   'since cost sits at the start of year 1 and scrap value at the end of the final year.',
   'Confusing the AP common difference with the GP common ratio.',
   'Forgetting that $A_0$ (the initial outlay) is always negative in an NPV calculation and is '
   'already a present value — it is never itself discounted.',
   'Mixing up simple interest ($I=Prn$, grows linearly) with compound interest ($A=P(1+r)^n$, '
   'grows geometrically) when computing how long money takes to triple.',
   'Applying the sum-to-infinity formula when $r>1$ (no sum to infinity exists in that case).',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The amount of ₦100,000 invested for 3 years at 10% per annum compound interest is',
    'o': ['₦130,000', '₦133,100', '₦131,000', '₦121,000', '₦110,000'],
    'a': 1,
    'w': 'Compound interest multiplies by $(1+r)$ each year.',
    'calc': 'A = 100{,}000(1.10)^3 = 100{,}000 \\times 1.331 = ₦133{,}100',
    'src': 'Chapter 12.5', 'sec': '12.5'},
   {'q': 'The present value of ₦1,000,000 receivable in 2 years at a discount rate of 10% is',
    'o': ['₦800,000', '₦826,446', '₦900,000', '₦909,091', '₦1,210,000'],
    'a': 1,
    'w': 'Divide by $(1.10)^2 = 1.21$.',
    'calc': 'P = \\frac{1{,}000{,}000}{1.21} = ₦826{,}446',
    'src': 'Chapter 12.5', 'sec': '12.5'},
   {'q': 'The 10th term of the arithmetic progression 7, 11, 15, … is',
    'o': ['39', '43', '47', '40', '44'],
    'a': 1,
    'w': 'The first term is 7 and the common difference 4.',
    'calc': 'T_{10} = 7 + 9(4) = 43',
    'src': 'Chapter 12.2', 'sec': '12.2'},
   {'q': 'The internal rate of return of a project is the discount rate at which',
    'o': ['the payback period is shortest', 'the net present value is zero',
          'total inflows equal total outflows undiscounted',
          'depreciation is at its lowest', 'the accounting rate of return is maximised'],
    'a': 1,
    'w': 'By definition the IRR is the break-even discount rate — the rate at which the present '
         'value of inflows exactly equals the outlay.',
    'src': 'Chapter 12.7', 'sec': '12.7'},
   {'q': 'The sum to infinity of the geometric progression $8 + 4 + 2 + 1 + \\cdots$ is',
    'o': ['15', '16', '20', '32', 'infinite'],
    'a': 1,
    'w': 'The common ratio is ½, which is less than 1, so the series converges.',
    'calc': 'S_\\infty = \\frac{a}{1-r} = \\frac{8}{1-0.5} = 16',
    'src': 'Chapter 12.3', 'sec': '12.3'},
   {'q': 'Simple interest on ₦300,000 at 8% per annum for 4 years is',
    'o': ['₦96,000', '₦24,000', '₦108,000', '₦300,000', '₦408,000'],
    'a': 0,
    'w': 'Simple interest is $I=Prn$, a single calculation with no compounding.',
    'calc': 'I = 300{,}000 \\times 0.08 \\times 4 = ₦96{,}000',
    'src': 'Chapter 12.4', 'sec': '12.4'},
  ],
  'theory': [
   {'q': 'A businessman deposits ₦100,000 at the end of each year for 6 years into a fund '
         'earning 8% per annum compound. (a) Compute the amount accumulated at the end of the '
         '6th year. (b) A project requires an immediate outlay of ₦1,000,000 and is expected '
         'to produce net cash flows of ₦400,000 a year for the next 4 years. At a discount rate '
         'of 12%, compute the NPV and advise whether the project should be accepted.',
    'marks': 12,
    'a': [
      {'h4': '(a) Sinking fund (future value of an ordinary annuity)'},
      {'tex': 'S = A\\left[\\frac{(1+r)^n-1}{r}\\right] = 100{,}000\\left[\\frac{(1.08)^6-1}'
              '{0.08}\\right]'},
      {'tex': '(1.08)^6 = 1.586874 \\;\\Rightarrow\\; S = 100{,}000 \\times \\frac{0.586874}'
              '{0.08} = ₦733{,}592.50'},
      {'h4': '(b) NPV at 12%'},
      {'p': 'The four inflows are an ordinary annuity, so use the annuity present-value '
            'formula rather than discounting each year separately:'},
      {'tex': 'P = A\\left[\\frac{1-(1+r)^{-n}}{r}\\right] = 400{,}000\\left['
              '\\frac{1-(1.12)^{-4}}{0.12}\\right]'},
      {'tex': '= 400{,}000 \\times 3.037349 = ₦1{,}214{,}940'},
      {'tex': 'NPV = 1{,}214{,}940 - 1{,}000{,}000 = ₦214{,}940'},
      {'p': 'The NPV is **positive**, so the project should be **accepted**: at a 12% cost of '
            'capital it leaves the business better off by ₦214,940 in today\'s money.'}],
    'src': 'Chapter 12.6', 'sec': '12.6'},
  ]},
}
