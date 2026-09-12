CH = {
 'n': 12,
 't': 'Mathematics of Finance',
 'brief': 'Simple and compound interest, arithmetic and geometric progressions, annuities and '
          'perpetuities, sinking funds, amortisation, and the appraisal of capital projects by '
          'net present value and internal rate of return.',
 'outcomes': [
   'Compute simple and compound interest and the effective annual rate',
   'Sum an arithmetic or geometric progression',
   'Value an annuity and a perpetuity, in advance and in arrears',
   'Compute a sinking fund instalment and prepare an amortisation schedule',
   'Appraise a project using net present value',
   'Estimate an internal rate of return by interpolation',
 ],
 'secs': [
  {'n': '12.1', 't': 'Simple and compound interest', 'b': [
    {'fbox': {'h': 'Interest', 'rows': [
      {'lb': 'Simple interest', 'tex': 'I = Prt'},
      {'lb': 'Amount, simple interest', 'tex': 'A = P(1 + rt)'},
      {'lb': 'Compound amount', 'tex': 'A = P(1 + r)^{n}'},
      {'lb': 'Compounded $m$ times a year',
       'tex': 'A = P\\left(1 + \\frac{r}{m}\\right)^{mn}'},
      {'lb': 'Effective annual rate',
       'tex': 'i = \\left(1 + \\frac{r}{m}\\right)^{m} - 1'},
      {'lb': 'Present value', 'tex': 'P = \\frac{A}{(1+r)^{n}} = A(1+r)^{-n}'},
    ]}},
    {'p': 'Under **simple interest** the interest each period is calculated on the original '
          'principal only, so the amount grows linearly. Under **compound interest** interest '
          'is added to the principal and itself earns interest, so the amount grows '
          'geometrically. Over one period the two are identical; the gap widens with time.'},
    {'eg': {'t': 'Simple against compound', 'q': [
      {'p': '₦500,000 is invested for 5 years at 12% per annum. Compute the amount under '
            '(a) simple interest and (b) interest compounded annually, and comment.'}],
      'a': [
      {'p': '**(a) Simple interest**'},
      {'tex': 'I = Prt = 500{,}000 \\times 0.12 \\times 5 = ₦300{,}000'},
      {'tex': 'A = 500{,}000 + 300{,}000 = ₦800{,}000'},
      {'p': '**(b) Compound interest**'},
      {'tex': 'A = P(1+r)^n = 500{,}000 (1.12)^5 = 500{,}000 \\times 1.762342 = ₦881{,}170.84'},
      {'p': 'Compounding produces ₦81,170.84 more — the interest earned on interest. The gap '
            'is not the rate but the reinvestment: at simple interest the ₦60,000 earned in '
            'year 1 lies idle, while under compounding it earns 12% for the remaining four '
            'years.'}]}},
    {'eg': {'t': 'Nominal against effective rate', 'q': [
      {'p': 'A bank quotes 18% per annum compounded quarterly. Compute the effective annual '
            'rate.'}],
      'a': [
      {'tex': 'i = \\left(1 + \\frac{0.18}{4}\\right)^{4} - 1 = (1.045)^4 - 1'},
      {'tex': '= 1.192519 - 1 = 0.192519 = 19.25\\% \\text{ per annum}'},
      {'note': 'The **nominal** rate of 18% understates the true cost. Whenever two offers are '
               'compounded at different frequencies, convert both to effective annual rates '
               'before comparing them.'}]}},
  ]},

  {'n': '12.2', 't': 'Progressions', 'b': [
    {'fbox': {'h': 'Arithmetic and geometric progressions', 'rows': [
      {'lb': 'AP: $n$th term', 'tex': 'T_n = a + (n-1)d'},
      {'lb': 'AP: sum of $n$ terms',
       'tex': 'S_n = \\frac{n}{2}\\big[2a + (n-1)d\\big] = \\frac{n}{2}(a + l)'},
      {'lb': 'GP: $n$th term', 'tex': 'T_n = ar^{\\,n-1}'},
      {'lb': 'GP: sum of $n$ terms',
       'tex': 'S_n = \\frac{a(r^n - 1)}{r - 1}, \\quad r \\ne 1'},
      {'lb': 'GP: sum to infinity',
       'tex': 'S_\\infty = \\frac{a}{1-r}, \\quad |r| < 1'},
    ]}},
    {'key': 'An **AP** has a constant *difference* between terms — straight-line depreciation, '
            'a salary rising by a fixed naira amount. A **GP** has a constant *ratio* — '
            'reducing-balance depreciation, compound interest, a salary rising by a fixed '
            'percentage. Deciding which model applies is usually worth more marks than the '
            'summation itself.'},
    {'eg': {'t': 'An arithmetic progression', 'q': [
      {'p': 'An employee starts on ₦5,000,000 a year and receives an increase of ₦500,000 at '
            'the end of each year. Compute the salary in the twelfth year and the total earned '
            'over twelve years.'}],
      'a': [
      {'p': 'Here $a = 5{,}000{,}000$, $d = 500{,}000$, $n = 12$ (in ₦ thousand for brevity: '
            '$a = 5{,}000$, $d = 500$).'},
      {'tex': 'T_{12} = a + (n-1)d = 5{,}000 + 11(500) = ₦10{,}500\\text{k}'},
      {'tex': 'S_{12} = \\frac{12}{2}\\big[2(5{,}000) + 11(500)\\big] = 6(10{,}000 + 5{,}500) '
              '= 6 \\times 15{,}500 = ₦93{,}000\\text{k}'},
      {'p': 'The twelfth-year salary is **₦10.5 million** and total earnings over the period '
            '**₦93 million**.'}]}},
    {'eg': {'t': 'A geometric progression', 'q': [
      {'p': 'A company deposits ₦100,000 at the end of each year for 10 years into an account '
            'paying 10% per annum compound. Compute the accumulated sum.'}],
      'a': [
      {'p': 'The last deposit earns no interest, the one before earns interest for one year, '
            'and so on. The deposits therefore form a GP with $a = 100{,}000$ and $r = 1.10$:'},
      {'tex': 'S_{10} = \\frac{a(r^{n} - 1)}{r - 1} = \\frac{100{,}000\\big[(1.10)^{10} - 1\\big]}'
              '{0.10}'},
      {'tex': '= \\frac{100{,}000 (2.593742 - 1)}{0.10} = 100{,}000 \\times 15.937425 '
              '= ₦1{,}593{,}742'},
      {'note': 'This quantity, $\\dfrac{(1+r)^n - 1}{r}$, is the **future value of an annuity '
               'factor**. Ten deposits of ₦100,000 accumulate to ₦1,593,742 rather than '
               '₦1,000,000; the ₦593,742 difference is compound interest.'}]}},
  ]},

  {'n': '12.3', 't': 'Annuities, perpetuities and sinking funds', 'b': [
    {'def': {'t': 'Annuity',
             'd': 'A series of equal payments made at equal intervals. An **ordinary annuity** '
                  '(annuity in arrears) pays at the *end* of each period; an **annuity due** '
                  '(in advance) pays at the *beginning*.'}},
    {'fbox': {'h': 'Annuity and sinking-fund formulae', 'rows': [
      {'lb': 'PV of an ordinary annuity',
       'tex': 'PV = A \\left[\\frac{1 - (1+r)^{-n}}{r}\\right]'},
      {'lb': 'FV of an ordinary annuity',
       'tex': 'FV = A \\left[\\frac{(1+r)^{n} - 1}{r}\\right]'},
      {'lb': 'Annuity due (either case)',
       'tex': '\\text{Ordinary value} \\times (1 + r)'},
      {'lb': 'Perpetuity', 'tex': 'PV = \\frac{A}{r}'},
      {'lb': 'Growing perpetuity',
       'tex': 'PV = \\frac{A}{r - g}, \\quad g < r'},
      {'lb': 'Sinking-fund instalment',
       'tex': 'A = S \\left[\\frac{r}{(1+r)^{n} - 1}\\right]'},
      {'lb': 'Loan instalment (amortisation)',
       'tex': 'A = P \\left[\\frac{r}{1 - (1+r)^{-n}}\\right]'},
    ]}},
    {'eg': {'t': 'Present value of an annuity', 'q': [
      {'p': 'What is the present value of ₦200,000 receivable at the end of each year for six '
            'years, if the required rate of return is 10% per annum?'}],
      'a': [
      {'tex': 'PV = 200{,}000 \\left[\\frac{1 - (1.10)^{-6}}{0.10}\\right]'},
      {'tex': '(1.10)^{-6} = \\frac{1}{1.771561} = 0.564474'},
      {'tex': 'PV = 200{,}000 \\times \\frac{1 - 0.564474}{0.10} = 200{,}000 \\times 4.355261 '
              '= ₦871{,}052'},
      {'p': 'Six receipts totalling ₦1,200,000 are worth only ₦871,052 today, because money '
            'received later is worth less.'},
      {'note': 'If the receipts were at the **beginning** of each year, multiply by $1.10$: '
               '$871{,}052 \\times 1.10 = ₦958{,}157$. Each receipt arrives one year earlier, '
               'so each is discounted one period less.'}]}},
    {'eg': {'t': 'Sinking fund', 'q': [
      {'p': 'A company must replace an asset costing ₦5,000,000 in five years\' time. Equal '
            'annual amounts are to be set aside at the end of each year in a fund earning 8% '
            'per annum. Compute the annual instalment.'}],
      'a': [
      {'tex': 'A = S\\left[\\frac{r}{(1+r)^n - 1}\\right] '
              '= 5{,}000{,}000 \\left[\\frac{0.08}{(1.08)^5 - 1}\\right]'},
      {'tex': '(1.08)^5 = 1.469328 \\quad\\Rightarrow\\quad (1.08)^5 - 1 = 0.469328'},
      {'tex': 'A = 5{,}000{,}000 \\times \\frac{0.08}{0.469328} = 5{,}000{,}000 \\times 0.170456 '
              '= ₦852{,}282'},
      {'p': 'Five instalments of ₦852,282 total ₦4,261,410; the remaining ₦738,590 is interest '
            'earned within the fund.'}]}},
    {'eg': {'t': 'Perpetuity', 'q': [
      {'p': 'A trust is to pay a scholarship of ₦50,000 a year in perpetuity. If the fund earns '
            '8% per annum, what capital sum is required?'}],
      'a': [
      {'tex': 'PV = \\frac{A}{r} = \\frac{50{,}000}{0.08} = ₦625{,}000'},
      {'p': 'At 8%, ₦625,000 generates exactly ₦50,000 a year for ever without touching the '
            'capital.'}]}},
  ]},

  {'n': '12.4', 't': 'Investment appraisal', 'b': [
    {'fbox': {'h': 'Discounted cash flow', 'rows': [
      {'lb': 'Discount factor', 'tex': 'DF = (1 + r)^{-n}'},
      {'lb': 'Net present value',
       'tex': 'NPV = \\sum_{t=0}^{n} \\frac{C_t}{(1+r)^t}'},
      {'lb': 'IRR by interpolation',
       'tex': 'IRR \\approx r_1 + \\frac{NPV_1}{NPV_1 - NPV_2}(r_2 - r_1)'},
      {'lb': 'Profitability index',
       'tex': 'PI = \\frac{\\text{PV of inflows}}{\\text{Initial outlay}}'},
    ]}},
    {'ul': [
      '**NPV > 0** — accept: the project earns more than the cost of capital and increases '
      'shareholder wealth.',
      '**NPV = 0** — indifferent: the project earns exactly the required return.',
      '**NPV < 0** — reject.',
      '**IRR** is the discount rate at which $NPV = 0$; accept if the IRR exceeds the cost of '
      'capital.',
    ]},
    {'eg': {'t': 'NPV and IRR of a project', 'q': [
      {'p': 'A project requires an immediate outlay of ₦1,000,000 and generates net cash inflows '
            'of ₦400,000 at the end of each of the next four years. The cost of capital is 15%. '
            'Compute the NPV and estimate the IRR.'}],
      'a': [
      {'h4': 'Net present value at 15%'},
      {'p': 'The inflows are a four-year annuity, so use the annuity factor rather than '
            'discounting each year separately:'},
      {'tex': 'AF_{4,15\\%} = \\frac{1 - (1.15)^{-4}}{0.15} = \\frac{1 - 0.571753}{0.15} '
              '= 2.854978'},
      {'stmt': {'t': 'NPV at 15%', 'rows': [
        ['Present value of inflows (400,000 × 2.854978)', 1141991],
        ['Less: Initial outlay', -1000000],
        ['Net present value@tot', 141991],
      ]}},
      {'p': 'The NPV is positive, so on this criterion the project should be **accepted**.'},
      {'h4': 'Internal rate of return'},
      {'p': 'A second, higher rate is needed to produce a negative NPV. Try 25%:'},
      {'tex': 'AF_{4,25\\%} = \\frac{1 - (1.25)^{-4}}{0.25} = \\frac{1 - 0.4096}{0.25} '
              '= 2.3616'},
      {'tex': 'NPV_{25\\%} = 400{,}000(2.3616) - 1{,}000{,}000 = 944{,}640 - 1{,}000{,}000 '
              '= -₦55{,}360'},
      {'p': 'Interpolate between the two:'},
      {'tex': 'IRR \\approx 15 + \\frac{141{,}991}{141{,}991 + 55{,}360} \\times (25 - 15)'},
      {'tex': '= 15 + \\frac{141{,}991}{197{,}351} \\times 10 = 15 + 7.19 = 22.19\\%'},
      {'p': 'The IRR of about **22.2%** comfortably exceeds the 15% cost of capital, confirming '
            'the accept decision.'},
      {'warn': 'Interpolation assumes the NPV falls in a straight line between the two rates, '
               'but the true NPV curve is convex. The estimate is therefore slightly **below** '
               'the true IRR, and the error grows as the two trial rates move further apart. '
               'Keep them within about ten percentage points of each other.'}]}},
  ]},

  {'n': '12.5', 't': 'Amortisation', 'b': [
    {'p': 'A loan repaid by equal instalments is the mirror image of an annuity: the lender '
          'pays out a lump sum today and receives an annuity. Each instalment covers the '
          'interest for the period, and the balance reduces the principal. Because the '
          'principal falls, the interest element falls and the capital element rises over the '
          'life of the loan.'},
    {'eg': {'t': 'Loan instalment and schedule', 'q': [
      {'p': 'A loan of ₦1,000,000 is to be repaid by three equal annual instalments at 10% per '
            'annum. Compute the instalment and prepare the amortisation schedule.'}],
      'a': [
      {'tex': 'AF_{3,10\\%} = \\frac{1 - (1.10)^{-3}}{0.10} = \\frac{1 - 0.751315}{0.10} '
              '= 2.486852'},
      {'tex': 'A = \\frac{1{,}000{,}000}{2.486852} = ₦402{,}114.80'},
      {'table': {'align': 'lrrrr',
        'head': ['Year', 'Opening (₦)', 'Interest 10% (₦)', 'Instalment (₦)', 'Closing (₦)'],
        'rows': [
        ['1', '1,000,000.00', '100,000.00', '402,114.80', '697,885.20'],
        ['2', '697,885.20', '69,788.52', '402,114.80', '365,558.92'],
        ['3', '365,558.92', '36,555.89', '402,114.80', '0.01'],
      ]}},
      {'p': 'The closing balance of ₦0.01 is rounding in the instalment and would be absorbed '
            'in the final payment. Note how the interest element falls from ₦100,000 to '
            '₦36,556 while the capital element rises from ₦302,115 to ₦365,559.'},
      {'note': 'Only the interest column is an expense in profit or loss. The capital element '
               'reduces the liability in the statement of financial position — a point that '
               'links directly to the lease and loan questions in Financial Accounting.'}]}},
  ]},

  {'n': '12.6', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'All the terms'},
    {'ul': [
      '**Sequence (progression)** — an ordered list of numbers; **series** — their sum.',
      '**Arithmetic progression (AP)** — successive terms differ by a constant **common '
      'difference $d$**. First term $a$, last term $l$.',
      '**Geometric progression (GP)** — successive terms are in a constant ratio, the **common '
      'ratio $r$**.',
      '**Principal $P$** — the sum invested or borrowed. **Rate $r$** — interest rate per '
      'period (as a decimal). **$n$** — number of periods. **Amount $A$** — principal plus '
      'interest.',
      '**Simple interest** — interest on the original principal only.',
      '**Compound interest** — interest earns interest ("multi-stage single-period simple '
      'interest").',
      '**Nominal rate** — the stated annual rate; **effective (annual) rate** — the rate '
      'actually earned once compounding within the year is allowed for.',
      '**Present value (PV)** — the amount now equivalent to a future sum, found by '
      '*discounting*. **Future value (FV)** — the accumulated amount later.',
      '**Annuity** — a sequence of equal periodic cash flows. **Ordinary annuity** — paid at '
      'the *end* of each period; **annuity due** — at the *beginning*; **annuity certain** — '
      'fixed start and end dates; **perpetuity** — continues indefinitely.',
      '**Sinking fund** — a series of equal deposits accumulated at compound interest to reach '
      'a target sum.',
      '**Amortisation** — repaying a loan by equal instalments, each part interest and part '
      'capital.',
      '**Net present value (NPV)** — the present value of all a project\'s cash inflows less '
      'all its outflows. NPV $> 0$ → accept.',
      '**Internal rate of return (IRR)** — the discount rate at which NPV $= 0$.',
      '**Discount factor** — $(1 + r)^{-n}$, the PV of ₦1 receivable in $n$ periods.',
    ]},
    {'h3': 'A. Progressions'},
    {'fbox': {'h': 'Arithmetic progression', 'rows': [
      {'lb': '$n$-th term', 'tex': 'T_n = a + (n - 1)d'},
      {'lb': 'Sum of $n$ terms',
       'tex': 'S_n = \\dfrac{n}{2}\\bigl[2a + (n - 1)d\\bigr] = \\dfrac{n}{2}(a + l)'},
    ]}},
    {'fbox': {'h': 'Geometric progression', 'rows': [
      {'lb': '$n$-th term', 'tex': 'T_n = ar^{\\,n-1}'},
      {'lb': 'Sum of $n$ terms',
       'tex': 'S_n = \\dfrac{a(1 - r^{n})}{1 - r} \\ (r < 1) \\quad\\text{or}\\quad '
              '\\dfrac{a(r^{n} - 1)}{r - 1} \\ (r > 1)'},
      {'lb': 'Sum to infinity', 'tex': 'S_\\infty = \\dfrac{a}{1 - r} \\quad (|r| < 1)'},
    ]}},
    {'h3': 'B. Simple interest'},
    {'fbox': {'h': 'Simple interest', 'rows': [
      {'lb': 'Interest', 'tex': 'I = Prn'},
      {'lb': 'Amount', 'tex': 'A = P(1 + rn)'},
      {'lb': 'Present value', 'tex': 'P = \\dfrac{A}{1 + rn}'},
    ]}},
    {'h3': 'C. Compound interest'},
    {'fbox': {'h': 'Compound interest', 'rows': [
      {'lb': 'Amount (annual compounding)', 'tex': 'A = P(1 + r)^{n}'},
      {'lb': 'Compounding $m$ times a year',
       'tex': 'A = P\\left(1 + \\dfrac{r}{m}\\right)^{mn}'},
      {'lb': 'Compound interest earned', 'tex': 'I = A - P = P\\bigl[(1 + r)^{n} - 1\\bigr]'},
      {'lb': 'Present value', 'tex': 'P = A(1 + r)^{-n} = \\dfrac{A}{(1 + r)^{n}}'},
      {'lb': 'Effective annual rate',
       'tex': 'i = \\left(1 + \\dfrac{r}{m}\\right)^{m} - 1'},
      {'lb': 'Finding $n$', 'tex': 'n = \\dfrac{\\log(A/P)}{\\log(1 + r)}'},
    ]}},
    {'h3': 'D. Annuities, perpetuities, sinking funds'},
    {'fbox': {'h': 'Annuity formulae (ordinary annuity, payment $A$)', 'rows': [
      {'lb': 'Future value (amount)',
       'tex': 'S = A\\left[\\dfrac{(1 + r)^{n} - 1}{r}\\right]'},
      {'lb': 'Present value',
       'tex': 'PV = A\\left[\\dfrac{1 - (1 + r)^{-n}}{r}\\right]'},
      {'lb': 'Perpetuity', 'tex': 'PV = \\dfrac{A}{r}'},
      {'lb': 'Sinking fund deposit (to accumulate $S$)',
       'tex': 'A = S\\left[\\dfrac{r}{(1 + r)^{n} - 1}\\right]'},
      {'lb': 'Loan instalment (amortisation of loan $L$)',
       'tex': 'A = L\\left[\\dfrac{r}{1 - (1 + r)^{-n}}\\right]'},
      {'lb': 'Annuity due (multiply the ordinary result by $(1+r)$)',
       'tex': 'PV_{due} = PV_{ordinary}\\,(1 + r)'},
    ]}},
    {'h3': 'E. Investment appraisal'},
    {'fbox': {'h': 'NPV and IRR', 'rows': [
      {'lb': 'Net present value',
       'tex': 'NPV = -A_0 + \\sum_{t=1}^{n} \\dfrac{A_t}{(1 + r)^{t}}'},
      {'lb': 'Decision rule', 'tex': 'NPV > 0 \\Rightarrow \\text{accept}; \\ NPV < 0 '
              '\\Rightarrow \\text{reject}'},
      {'lb': 'IRR by linear interpolation',
       'tex': 'IRR \\approx r_1 + \\dfrac{NPV_1}{NPV_1 - NPV_2}\\,(r_2 - r_1)',
       'nt': '$r_1$ gives a positive $NPV_1$, $r_2$ a negative $NPV_2$.'},
    ]}},
    {'note': 'For a growing/declining cash stream (fixed % change each period) the terms form a '
             '**GP**; for a fixed-amount change each period they form an **AP**.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Simple interest', 'tex': 'I = Prn'},
  {'lb': 'Simple interest amount', 'tex': 'A = P(1 + rn)'},
  {'lb': 'Simple interest present value', 'tex': 'P = \\frac{A}{1 + rn}'},
  {'lb': 'Compound amount', 'tex': 'A = P(1+r)^n'},
  {'lb': 'Compounding $m$ times a year',
   'tex': 'A = P\\left(1+\\frac{r}{m}\\right)^{mn}'},
  {'lb': 'Compound interest earned', 'tex': 'I = P[(1+r)^n - 1]'},
  {'lb': 'Effective annual rate',
   'tex': 'i = \\left(1+\\frac{r}{m}\\right)^{m} - 1'},
  {'lb': 'Present value (compound)', 'tex': 'P = A(1+r)^{-n}'},
  {'lb': 'Number of periods', 'tex': 'n = \\frac{\\log(A/P)}{\\log(1+r)}'},
  {'lb': 'AP: $n$-th term', 'tex': 'T_n = a + (n-1)d'},
  {'lb': 'AP: sum', 'tex': 'S_n = \\frac{n}{2}[2a + (n-1)d] = \\frac{n}{2}(a + l)'},
  {'lb': 'GP: $n$-th term', 'tex': 'T_n = ar^{\\,n-1}'},
  {'lb': 'GP: sum', 'tex': 'S_n = \\frac{a(r^n-1)}{r-1} = \\frac{a(1-r^n)}{1-r}'},
  {'lb': 'GP: sum to infinity', 'tex': 'S_\\infty = \\frac{a}{1-r}'},
  {'lb': 'PV of an annuity',
   'tex': 'PV = A\\left[\\frac{1-(1+r)^{-n}}{r}\\right]'},
  {'lb': 'FV of an annuity',
   'tex': 'FV = A\\left[\\frac{(1+r)^{n}-1}{r}\\right]'},
  {'lb': 'Perpetuity', 'tex': 'PV = \\frac{A}{r}'},
  {'lb': 'Sinking fund', 'tex': 'A = S\\left[\\frac{r}{(1+r)^n-1}\\right]'},
  {'lb': 'IRR by interpolation',
   'tex': 'IRR \\approx r_1 + \\frac{NPV_1}{NPV_1-NPV_2}(r_2-r_1)'},
 ],
 'focus':
   'The single most heavily examined chapter in the paper. Expect three or four Section A marks '
   'on compound amounts, annuity factors and discount factors, and a full Section B question '
   'most diets on NPV and IRR or on a sinking fund. Learn to recognise an annuity so you can '
   'use one factor instead of discounting four separate years — it saves several minutes and '
   'removes most of the arithmetic risk.',
 'errors': [
   'Using $n$ = number of years when interest is compounded quarterly; the exponent is $mn$ '
   'and the rate $r/m$.',
   'Comparing nominal rates of different compounding frequencies without converting to '
   'effective rates.',
   'Applying the ordinary annuity factor to payments made in advance (multiply by $1+r$).',
   'Confusing the sinking-fund factor $r/[(1+r)^n-1]$ with the loan-repayment factor '
   '$r/[1-(1+r)^{-n}]$.',
   'Discounting the year-0 outlay; it is already a present value.',
   'Interpolating an IRR between two rates that are far apart, or between two positive NPVs.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The amount of ₦100,000 invested for 3 years at 10% per annum compound interest is',
    'o': ['₦130,000', '₦133,100', '₦131,000', '₦121,000', '₦110,000'],
    'a': 1,
    'w': 'Compound interest multiplies by $(1+r)$ each year.',
    'calc': 'A = 100{,}000(1.10)^3 = 100{,}000 \\times 1.331 = ₦133{,}100',
    'src': 'Chapter 12.1'},
   {'q': 'The present value of ₦1,000,000 receivable in 2 years at a discount rate of 10% is',
    'o': ['₦800,000', '₦826,446', '₦900,000', '₦909,091', '₦1,210,000'],
    'a': 1,
    'w': 'Divide by $(1.10)^2 = 1.21$.',
    'calc': 'PV = \\frac{1{,}000{,}000}{1.21} = ₦826{,}446',
    'src': 'Chapter 12.1'},
   {'q': 'A perpetuity of ₦30,000 per annum at a discount rate of 12% has a present value of',
    'o': ['₦360,000', '₦250,000', '₦300,000', '₦240,000', '₦336,000'],
    'a': 1,
    'w': 'The present value of a perpetuity is the annual amount divided by the rate.',
    'calc': 'PV = \\frac{30{,}000}{0.12} = ₦250{,}000',
    'src': 'Chapter 12.3'},
   {'q': 'The 10th term of the arithmetic progression 7, 11, 15, … is',
    'o': ['39', '43', '47', '40', '44'],
    'a': 1,
    'w': 'The first term is 7 and the common difference 4.',
    'calc': 'T_{10} = 7 + 9(4) = 43',
    'src': 'Chapter 12.2'},
   {'q': 'The internal rate of return of a project is the discount rate at which',
    'o': ['the payback period is shortest', 'the net present value is zero',
          'total inflows equal total outflows undiscounted',
          'the profitability index is zero', 'the accounting rate of return is maximised'],
    'a': 1,
    'w': 'By definition the IRR is the break-even discount rate — the rate at which the present '
         'value of inflows exactly equals the outlay.',
    'src': 'Chapter 12.4'},
   {'q': 'A nominal rate of 12% per annum compounded semi-annually gives an effective annual '
         'rate of',
    'o': ['12.00%', '12.36%', '12.68%', '24.00%', '6.00%'],
    'a': 1,
    'w': 'Two periods of 6% each: $(1.06)^2 = 1.1236$.',
    'calc': 'i = (1.06)^2 - 1 = 0.1236 = 12.36\\%',
    'src': 'Chapter 12.1'},
   {'q': 'The sum to infinity of the geometric progression $8 + 4 + 2 + 1 + \\cdots$ is',
    'o': ['15', '16', '20', '32', 'infinite'],
    'a': 1,
    'w': 'The common ratio is ½, which is less than 1, so the series converges.',
    'calc': 'S_\\infty = \\frac{a}{1-r} = \\frac{8}{1-0.5} = 16',
    'src': 'Chapter 12.2'},
  ],
  'theory': [
   {'q': 'Oyo Manufacturing Limited is considering a project requiring an immediate investment '
         'of ₦2,400,000 in plant, which will have a residual value of ₦200,000 at the end of '
         'its four-year life. Net cash inflows before depreciation are expected to be '
         '₦900,000, ₦1,000,000, ₦800,000 and ₦600,000 in years 1 to 4 respectively. The cost '
         'of capital is 16%. (a) Compute the net present value. (b) Advise the company. '
         '(c) State three advantages of the net present value method over the payback period.',
    'marks': 15,
    'a': [
      {'h4': '(a) Net present value at 16%'},
      {'p': 'The residual value is a year-4 inflow and is discounted with the year-4 cash flow. '
            'Discount factors at 16% are $(1.16)^{-n}$:'},
      {'table': {'align': 'lrrr',
        'head': ['Year', 'Cash flow (₦)', 'DF at 16%', 'Present value (₦)'], 'rows': [
        ['0', '(2,400,000)', '1.0000', '(2,400,000)'],
        ['1', '900,000', '0.8621', '775,890'],
        ['2', '1,000,000', '0.7432', '743,200'],
        ['3', '800,000', '0.6407', '512,560'],
        ['4', '600,000', '0.5523', '331,380'],
        ['4 (residual value)', '200,000', '0.5523', '110,460'],
        ['Net present value', '', '', '73,490'],
      ]}},
      {'p': 'Sum of the positive present values: $775{,}890 + 743{,}200 + 512{,}560 + 331{,}380 '
            '+ 110{,}460 = ₦2{,}473{,}490$. Deducting the outlay of ₦2,400,000 gives:'},
      {'tex': 'NPV = 2{,}473{,}490 - 2{,}400{,}000 = ₦73{,}490'},
      {'h4': '(b) Advice'},
      {'p': 'The net present value is **positive at ₦73,490**, so the project earns more than '
            'the 16% cost of capital and should be **accepted**. In wealth terms, undertaking '
            'the project makes the shareholders ₦73,490 better off in today\'s money than '
            'investing the same ₦2,400,000 at 16% elsewhere.'},
      {'p': 'The margin is thin, however — about 3% of the outlay. Two cautions follow. First, '
            'the decision is sensitive to the estimates: a shortfall of much more than ₦100,000 '
            'in undiscounted inflows, or a rise in the cost of capital of two or three '
            'percentage points, would turn the NPV negative. A sensitivity analysis should be '
            'run before committing. Second, the residual value contributes ₦110,460 — more than '
            'the whole of the NPV — so the reliability of that estimate matters '
            'disproportionately.'},
      {'h4': '(c) Advantages of NPV over payback'},
      {'ol': [
        '**It recognises the time value of money.** Every cash flow is discounted to a common '
        'date, so ₦1 received in year 4 is not treated as equal to ₦1 received in year 1. '
        'Payback, in its simple form, adds undiscounted flows.',
        '**It considers the whole life of the project.** Payback ignores every cash flow '
        'arising after the payback date, so it would ignore the ₦600,000 in year 4 and the '
        'residual value entirely if the outlay were recovered earlier. A project with large '
        'later inflows is systematically undervalued by payback.',
        '**It measures the absolute increase in shareholder wealth** in naira, so competing '
        'projects can be ranked directly and the results of several projects can be added '
        'together. Payback yields a period, which says nothing about profitability.',
        '**It explicitly incorporates the cost of capital and risk**, since the discount rate '
        'can be raised for a riskier project. Payback treats risk only crudely, by preferring '
        'a shorter recovery period.',
      ]},
      {'note': 'Payback is not worthless — it is simple, it is understood by non-financial '
               'managers, and it is a rough guide to liquidity and to risk where cash is '
               'tight. The usual recommendation is to use it as a screening device alongside '
               'NPV, not instead of it.'}],
    'src': 'Chapter 12.4'},
  ]},
}
