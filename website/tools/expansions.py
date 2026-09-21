"""
Worked-calculation explanations for past-paper questions, shown as the "why"
in a chapter quiz or exam-sit review once a candidate answers.

NOTES        {"<diet>/<SUBJECT>/mcq/<n>": "<explanation string>"} — plain
             text with inline $TeX$ and **bold** (goes through the same
             R.inl() renderer as everything else), one line of working per
             entry. Only questions whose answer requires a calculation need
             one; a purely definitional MCQ's own options are usually
             self-explanatory once the correct letter is known.
SECB_NOTES   {"<diet>/<SUBJECT>/<n>": [blocks]} — an optional block-schema
             list rendered above the official Section B solution, for a
             worked expansion where the official solution's own workings
             are terse or the OCR extraction garbled a figure.

Verified against each diet's own printed answer key before being written
here; where the source paper prints its own working (papers.json's
mcq_workings / saq_workings, extracted but never previously used), that
working was cross-checked and, where correct, is what these entries are
based on — rewritten cleanly rather than pasted raw, since the OCR extract
of those workings is frequently garbled (misaligned fractions, dropped
signs, run-together numbers).
"""

NOTES = {
    # ---- 2016-09 FA ----
    '2016-09/FA/mcq/3': 'Cost of inventory includes every cost of bringing it to its present location and condition: '
        '$Le\\,17{,}500 + Le\\,1{,}500 = Le\\,19{,}000$.',
    '2016-09/FA/mcq/8': 'Nominal value per share $= \\dfrac{\\text{Authorised share capital}}{\\text{Number of shares}} '
        '= \\dfrac{\\text{\\textnaira}8{,}000{,}000}{20{,}000{,}000} = \\text{\\textnaira}0.4$.',
    '2016-09/FA/mcq/9': 'Shares actually issued $= 20{,}000{,}000 \\times 85\\% = 17{,}000{,}000$. Premium per share '
        '$= \\text{\\textnaira}0.5 - \\text{\\textnaira}0.4 = \\text{\\textnaira}0.1$. Total premium '
        '$= 17{,}000{,}000 \\times 0.1 = \\text{\\textnaira}1{,}700{,}000$.',
    '2016-09/FA/mcq/15': 'Total joint venture cost $= GH\\text{\\textcent}60{,}000 + 15{,}000 + 6{,}000 = 81{,}000$. '
        'Profit $= 120{,}000 - 81{,}000 = 39{,}000$. Jonah\'s share (ratio 4:6 of 4:2) '
        '$= 39{,}000 \\times \\frac{4}{6} = GH\\text{\\textcent}26{,}000$.',
    '2016-09/FA/mcq/20': 'Shares of $\\text{\\textnaira}1.00$ nominal issued at $90k$ raise less than nominal value: '
        'a **discount** of $\\text{\\textnaira}1.00 - \\text{\\textnaira}0.90 = 10k$ per share.',
    '2016-09/FA/mcq/21': 'Goodwill (L\\$1,200m) is credited to the **old** partners in the **old** ratio before Ted '
        'is admitted. Rex:Ken $= 2:5, 3:5$, so Ken\'s credit $= 1{,}200\\text{m} \\times \\frac{3}{5} = L\\$720\\text{m}$.',
    '2016-09/FA/mcq/22': 'Ted brings in L\\$360m, then bears his share of the goodwill written off in the **new** '
        'ratio $3:6:1$: $1{,}200\\text{m} \\times \\frac{1}{10} = 120\\text{m}$. Balance '
        '$= 360\\text{m} - 120\\text{m} = L\\$240\\text{m}$.',
    '2016-09/FA/mcq/26': 'Inventory turnover $= \\dfrac{\\text{Cost of sales}}{\\text{Average inventory}} = '
        '\\dfrac{180{,}000}{(18{,}000+30{,}000)/2} = \\dfrac{180{,}000}{24{,}000} = 7.5$ times.',
    '2016-09/FA/mcq/28': 'A 25% mark-up is on **cost**: if cost $=x$, then $1.25x = Le\\,1{,}200{,}000$, so '
        '$x = Le\\,960{,}000$.',

    # ---- 2014-03 FA ----
    '2014-03/FA/mcq/4':
        'Gross profit is $33\\frac13\\%$ **on cost**, so cost of sales $= \\dfrac{240{,}000}{1+\\frac13} = '
        '180{,}000$. Goods available $= 24{,}000+180{,}000 = 204{,}000$. Stock lost '
        '$= 204{,}000 - 180{,}000 = \\text{\\textnaira}24{,}000$.',
    '2014-03/FA/mcq/5': 'Sum-of-the-years\'-digits over 5 years $= 5+4+3+2+1=15$. Year 3 uses the '
        '3rd-highest remaining-life digit, $3/15 = 1/5$.',
    '2014-03/FA/mcq/12': 'Kwame takes $\\frac15=20\\%$; the remaining 80% is split in the old 3:2 ratio: '
        'Kofi $=80\\%\\times\\frac35=48\\%$, Annan $=80\\%\\times\\frac25=32\\%$ — giving 48%:32%:20%.',
    '2014-03/FA/mcq/14': 'Subscription income $=$ cash received $+$ opening advance $-$ closing advance '
        '$+$ closing arrears $-$ opening arrears: $600{,}000+300{,}000-380{,}000+180{,}000-230{,}000 '
        '= GH\\text{\\textcent}470{,}000$.',
    '2014-03/FA/mcq/16': 'The Le1,800,000 maintenance cost was wrongly capitalised and expenses fall by '
        'it once corrected ($-1{,}800{,}000$); the wrongly-charged depreciation on it '
        '($25\\% \\times 1{,}800{,}000 = 450{,}000$) is added back. Corrected profit '
        '$= 6{,}500{,}000 - 1{,}800{,}000 + 450{,}000 = \\text{\\textnaira}5{,}150{,}000$.',
    '2014-03/FA/mcq/17': 'Payables account: opening $+$ purchases $=$ cash paid $+$ discount received $+$ '
        'closing. $75{,}000 + P = 65{,}000+3{,}000+65{,}000 \\Rightarrow P = Le\\,58{,}000$.',
    '2014-03/FA/mcq/18': 'A 40% mark-up is on cost: $1.4 \\times \\text{cost} = \\text{\\textnaira}175{,}000 '
        '\\Rightarrow \\text{cost} = \\text{\\textnaira}125{,}000$.',
    '2014-03/FA/mcq/23': 'Goods sent to branch is recorded **at cost** here: cost of goods sent '
        '$= 289{,}200 \\div 1.25 = 231{,}360$; cost of the ₦10,000 (invoice-price) return '
        '$= 10{,}000\\div 1.25 = 8{,}000$. Net credited $= 231{,}360-8{,}000 = \\text{\\textnaira}223{,}360$.',
    '2014-03/FA/mcq/24': 'Branch inventory is controlled **at invoice price**, so the return is credited to '
        'the Branch Inventory Control account at its full invoice price, ₦10,000 — no conversion to cost.',

    # ---- 2014-09 FA ----
    '2014-09/FA/mcq/8': 'The roofing component is depreciated separately: $Le\\,10{,}000{,}000 \\div 10 = '
        '1{,}000{,}000$/year. The rest of the building ($50{,}000{,}000-10{,}000{,}000=40{,}000{,}000$) is '
        'depreciated over 50 years: $40{,}000{,}000\\div 50 = 800{,}000$/year. Total '
        '$= 1{,}000{,}000+800{,}000 = \\text{\\textnaira}1{,}800{,}000$.',
    '2014-09/FA/mcq/13': 'On the new ratio $4:3:1$, Agodo\'s raw share $= GH\\text{\\textcent}108\\text{m}\\times\\frac18 '
        '= 13.5\\text{m}$, short of his $23\\text{m}$ guarantee by $9.5\\text{m}$. Kweku and Kwame make up this '
        'deficiency between themselves in their share of the new ratio, $4:3$: Kweku bears '
        '$9.5\\text{m}\\times\\frac47 \\approx 5.43\\text{m}$. Kweku\'s final share '
        '$= 54\\text{m}-5.43\\text{m}\\approx GH\\text{\\textcent}49$ million (to the nearest million).',
    '2014-09/FA/mcq/17': 'Nominal value $= 5{,}000 \\times L\\$0.50 = L\\$2{,}500$ (Share Capital). Premium '
        '$= L\\$6{,}000 - L\\$2{,}500 = L\\$3{,}500$ (Share Premium).',
    '2014-09/FA/mcq/30': 'With no partnership agreement, the Partnership Act default applies: profits are shared '
        '**equally**. $Le\\,750{,}000 \\div 3 = Le\\,250{,}000$ each.',

    # ---- 2015-03 / 2015-09 FA (identical question, both diets) ----
    '2015-03/FA/mcq/3': 'Gross profit is 25% **on cost of sales**: if COGS $=x$, Sales $=1.25x$, so '
        '$x = \\dfrac{360{,}000}{1.25} = 288{,}000$. Opening inventory '
        '$= COGS - Purchases + Closing\\;inventory = 288{,}000 - 270{,}000 + 45{,}000 = N\\,63{,}000$.',
    '2015-03/FA/mcq/4': 'Gross profit is 25% on cost of sales: $COGS = \\dfrac{360{,}000}{1.25}=288{,}000$. '
        'Gross profit $= Sales - COGS = 360{,}000-288{,}000 = \\text{\\textnaira}72{,}000$.',
    '2015-03/FA/mcq/12': 'Goodwill (Le10m) is raised in the **old** ratio (1:1) then written off in the **new** '
        'ratio (2:2:1). Seidu: credited $10\\text{m}\\times\\frac12=5\\text{m}$, debited '
        '$10\\text{m}\\times\\frac25=4\\text{m}$, net $+1\\text{m}$. Capital after '
        '$= Le\\,8\\text{m}+1\\text{m}=Le\\,9$ million.',
    '2015-03/FA/mcq/15': 'The N50m life membership fund is credited to income at $50\\text{m}\\div5=10\\text{m}$ '
        'per year. In year 2: Income and Expenditure gets that year\'s instalment, N10m; the Accumulated Fund '
        'balance still held is $50\\text{m}-(2\\times10\\text{m})=N30$ million.',
    '2015-03/FA/mcq/23': 'Total venture cost $= L\\$20{,}000+5{,}000+2{,}000=27{,}000$. Profit '
        '$=40{,}000-27{,}000=13{,}000$. Saleh\'s share (ratio 5:3) $=13{,}000\\times\\frac58=L\\$8{,}125$.',
    '2015-03/FA/mcq/24': 'Total venture cost $= L\\$20{,}000+5{,}000+2{,}000=27{,}000$. Profit '
        '$=40{,}000-27{,}000=13{,}000$. Johnson\'s share (ratio 5:3) $=13{,}000\\times\\frac38=L\\$4{,}875$.',
    '2015-09/FA/mcq/3': 'Gross profit is 25% **on cost of sales**: if COGS $=x$, Sales $=1.25x$, so '
        '$x = \\dfrac{360{,}000}{1.25} = 288{,}000$. Opening inventory '
        '$= COGS - Purchases + Closing\\;inventory = 288{,}000 - 270{,}000 + 45{,}000 = N\\,63{,}000$.',
    '2015-09/FA/mcq/4': 'Gross profit is 25% on cost of sales: $COGS = \\dfrac{360{,}000}{1.25}=288{,}000$. '
        'Gross profit $= Sales - COGS = 360{,}000-288{,}000 = \\text{\\textnaira}72{,}000$.',
    '2015-09/FA/mcq/12': 'Goodwill (Le10m) is raised in the **old** ratio (1:1) then written off in the **new** '
        'ratio (2:2:1). Seidu: credited $10\\text{m}\\times\\frac12=5\\text{m}$, debited '
        '$10\\text{m}\\times\\frac25=4\\text{m}$, net $+1\\text{m}$. Capital after '
        '$= Le\\,8\\text{m}+1\\text{m}=Le\\,9$ million.',
    '2015-09/FA/mcq/15': 'The N50m life membership fund is credited to income at $50\\text{m}\\div5=10\\text{m}$ '
        'per year. In year 2: Income and Expenditure gets that year\'s instalment, N10m; the Accumulated Fund '
        'balance still held is $50\\text{m}-(2\\times10\\text{m})=N30$ million.',
    '2015-09/FA/mcq/23': 'Total venture cost $= L\\$20{,}000+5{,}000+2{,}000=27{,}000$. Profit '
        '$=40{,}000-27{,}000=13{,}000$. Saleh\'s share (ratio 5:3) $=13{,}000\\times\\frac58=L\\$8{,}125$.',
    '2015-09/FA/mcq/24': 'Total venture cost $= L\\$20{,}000+5{,}000+2{,}000=27{,}000$. Profit '
        '$=40{,}000-27{,}000=13{,}000$. Johnson\'s share (ratio 5:3) $=13{,}000\\times\\frac38=L\\$4{,}875$.',

    # ---- 2017-03 FA ----
    '2017-03/FA/mcq/2': 'Cost is every amount needed to bring the asset to use: '
        '$7{,}350{,}000 - 255{,}000\\;(\\text{trade discount}) + 67{,}500\\;(\\text{installation}) = '
        '\\text{\\textnaira}7{,}162{,}500$.',
    '2017-03/FA/mcq/6': 'Reducing-balance NBV after 4 years (2012–2015) at 25%/yr: '
        '$9{,}600{,}000\\times0.75^4 = 9{,}600{,}000\\times0.316406 = L\\$3{,}037{,}500$. Profit on disposal '
        '$= 4{,}500{,}000-3{,}037{,}500 = L\\$1{,}462{,}500$.',
    '2017-03/FA/mcq/13': 'Cost of goods sold $= 7.5\\text{m}+62.5\\text{m}-5\\text{m}=65\\text{m}$. Gross profit '
        '$= Sales - COGS = 87.5\\text{m}-65\\text{m}=\\text{\\textnaira}22.5$ million profit.',
    '2017-03/FA/mcq/14': 'Cost of goods sold $= Opening\\;inventory+Purchases-Closing\\;inventory '
        '= 7.5\\text{m}+62.5\\text{m}-5\\text{m}=\\text{\\textnaira}65.0$ million.',
    '2017-03/FA/mcq/16': 'Using the receivables control account: Sales $=$ cash received $+$ closing balance '
        '$-$ opening balance $= 7{,}500{,}000+3{,}500{,}000-2{,}500{,}000 = GH\\text{\\textcent}8{,}500{,}000$.',
    '2017-03/FA/mcq/20': 'Pascal\'s share of the ratio 5:3:2 (10 parts) $= GH\\text{\\textcent}1{,}034{,}200 '
        '\\times\\frac{3}{10} = GH\\text{\\textcent}310{,}260$.',
    '2017-03/FA/mcq/23': 'Of the ₦90,000 sale-or-return goods still unsold, their cost (at cost-plus-25%) '
        '$= 90{,}000\\div1.25=72{,}000$ must be added back to inventory: '
        '$Le\\,312{,}000+72{,}000 = Le\\,384{,}000$.',
    '2017-03/FA/mcq/24': 'The ₦90,000 (selling-price) worth of sale-or-return goods still unsold at year end was '
        'wrongly treated as a sale and must be removed: $Le\\,1{,}800{,}000 - 90{,}000 = Le\\,1{,}710{,}000$.',
    '2017-03/FA/mcq/27': 'Subscriptions account: Dr side $=$ opening arrears $50{,}000$ + closing advance '
        '$14{,}000$ = $64{,}000$. Cr side $=$ opening advance $32{,}000$ + cash received for 2015 $310{,}000$ + '
        'closing arrears $10{,}000$ = $352{,}000$. Income (balancing figure) $= 352{,}000-64{,}000 = '
        '\\text{\\textnaira}288{,}000$.',
    '2017-03/FA/mcq/28': 'The subscription in arrears at 31 December 2015 is given directly in the account '
        'balances: ₦10,000.',

    # ---- 2017-09 FA ----
    '2017-09/FA/mcq/13': 'Gross profit margin $33\\tfrac13\\%$ on sales, GP $=L\\$8{,}000 \\Rightarrow Sales '
        '= 8{,}000\\div\\tfrac13 = 24{,}000$. Net profit $= 8{,}000-6{,}800=1{,}200$. Net profit \\% '
        '$= 1{,}200\\div24{,}000 = 5.00\\%$.',
    '2017-09/FA/mcq/20': 'Suleiman\'s raw share of the 7:5:2 ratio $= 63{,}000{,}000\\times\\frac{2}{14} = '
        '9{,}000{,}000$, which already **exceeds** his ₦8,000,000 guarantee, so no top-up is needed. Razak\'s '
        'share $= 63{,}000{,}000\\times\\frac{7}{14} = \\text{\\textnaira}31{,}500{,}000$.',
    '2017-09/FA/mcq/28': 'Profit $= GH\\text{\\textcent}300{,}000-240{,}000=60{,}000$. Margin (profit on '
        '**selling price**) $= 60{,}000\\div300{,}000 = 20\\%$.',

    # ---- 2018-03 FA ----
    '2018-03/FA/mcq/5': 'Issue price (90k) is below the ₦1.00 nominal value, so shares are issued at a '
        '**discount** of $\\text{\\textnaira}1.00-0.90 = 10k$ per share.',
    '2018-03/FA/mcq/7': 'Monthly premium $= 27{,}000\\div15 = 1{,}800$. Year 2015 (12 months) expense '
        '$= 12\\times1{,}800 = \\text{\\textnaira}21{,}600$.',
    '2018-03/FA/mcq/8': 'The remaining 3 months (Jan–Mar 2016) already paid for is a prepayment at 31 Dec 2015: '
        '$3\\times1{,}800 = \\text{\\textnaira}5{,}400$, shown as a **current asset**.',
    '2018-03/FA/mcq/11': 'The cheque (L$8,000) was wrongly **credited** instead of debited to Tajudeen\'s '
        'account. Correcting this needs double the error: debit his account with $2\\times8{,}000=L\\$16{,}000$ '
        '(to cancel the wrong credit and post the correct debit), crediting Suspense L$16,000.',
    '2018-03/FA/mcq/19': 'Issue price (50k) is below the 75k nominal value, so shares are issued at a discount '
        'of $75k-50k = 25k$ per share.',
    '2018-03/FA/mcq/23': 'Annual rent under the 3-year prepayment $= Le\\,1{,}800{,}000\\div3 = Le\\,600{,}000$ '
        'per year — this is the charge for 2016; the ₦250,000 still outstanding for 2015 relates to the prior '
        'year and does not affect 2016\'s own charge.',

    # ---- 2018-09 FA ----
    '2018-09/FA/mcq/5': 'Goodwill (¢12m) is raised in the **old** ratio (1:1) — Ade credited ¢6m — then written '
        'off in the **new** equal ratio (1:1:1) — Ade debited ¢4m. Net effect on Ade '
        '$= 6\\text{m}-4\\text{m} = +GH\\text{\\textcent}2$ million.',
    '2018-09/FA/mcq/7': 'A 50% mark-up on cost: if cost $=100$, gross profit $=50$, selling price $=150$. As a '
        '\\% of selling price, $50\\div150 = 33\\tfrac13\\%$.',
    '2018-09/FA/mcq/10': 'The ₦10,000 receipt was posted to the **wrong side** of the cash book (credited '
        'instead of debited) — a full reversal. Correcting it needs **double** the amount: '
        'Dr. Cash book with $2\\times10{,}000 = \\text{\\textnaira}20{,}000$, Cr. John Marku account ₦20,000.',
    '2018-09/FA/mcq/15': 'Annual depreciation $= \\dfrac{5{,}000{,}000-400{,}000}{5} = 920{,}000$. After 4 years, '
        'accumulated depreciation $= 4\\times920{,}000=3{,}680{,}000$. Carrying amount '
        '$= 5{,}000{,}000-3{,}680{,}000 = Le\\,1{,}320{,}000$.',
    '2018-09/FA/mcq/23': 'A 35% mark-up on cost: $1.35\\times\\text{cost} = Le\\,450{,}000 \\Rightarrow '
        '\\text{cost} = 450{,}000\\div1.35 = Le\\,333{,}333$.',
    '2018-09/FA/mcq/24': 'Average inventory $= \\dfrac{72{,}000+120{,}000}{2} = 96{,}000$. Inventory turnover '
        '$= \\dfrac{720{,}000}{96{,}000} = 7.5$ times.',
    '2018-09/FA/mcq/26': 'Total HP price $= deposit + instalments = 2{,}500{,}000 + (5\\times3{,}500{,}000) = '
        '20{,}000{,}000$. Total interest $= 20{,}000{,}000-10{,}000{,}000 = 10{,}000{,}000$, spread equally '
        '(straight line) over 5 years: $10{,}000{,}000\\div5 = L\\$2{,}000{,}000$ for the first year.',
    '2018-09/FA/mcq/29': 'Actual royalty earned $= \\text{\\textnaira}3\\times15{,}000{,}000 = 45{,}000{,}000$, '
        'below the ₦48,000,000 minimum rent. Short workings $= 48{,}000{,}000-45{,}000{,}000 = '
        '\\text{\\textnaira}3{,}000{,}000$.',
    '2018-09/FA/mcq/30': 'The ₦6,000,000 debited to Chief John\'s account is at the **invoice price** '
        '($33\\tfrac13\\%$ above cost). Since the sale is not yet confirmed, the goods must be valued in '
        'inventory **at cost**: $6{,}000{,}000\\div1.3333 = \\text{\\textnaira}4{,}500{,}000$.',

    # ---- 2019-03 FA ----
    '2019-03/FA/mcq/1': 'A credit sale increases what the customer owes (an asset) and records the revenue: '
        'Dr. Receivables, Cr. Sales.',
    '2019-03/FA/mcq/8': 'Payables Ledger Control a/c — Dr total (purchases returns 3,000 + contra 9,000 + bank '
        '12,200 + discount received 400) $=24{,}600$; Cr total (balance b/d 10,000 + purchases 21,000 + '
        'cheques dishonoured 600) $=31{,}600$. Closing payables (balancing figure) '
        '$=31{,}600-24{,}600=\\text{\\textnaira}7{,}000$.',
    '2019-03/FA/mcq/9': 'Net credit purchases $=$ gross purchases $-$ purchases returns $= 21{,}000-3{,}000 = '
        '\\text{\\textnaira}18{,}000$.',
    '2019-03/FA/mcq/24': 'Output VAT $= 65{,}296{,}000\\times\\frac{10}{110}=5{,}936{,}000$. Input VAT '
        '$=47{,}806{,}000\\times\\frac{10}{110}=4{,}346{,}000$. Net VAT for the month '
        '$=5{,}936{,}000-4{,}346{,}000=1{,}590{,}000$. Closing balance '
        '$=583{,}000+1{,}590{,}000=GH\\text{\\textcent}2{,}173{,}000$.',

    # ---- 2019-09 FA ----
    '2019-09/FA/mcq/6': 'A 25% mark-up is on cost: $1.25\\times\\text{cost}=\\text{\\textnaira}1{,}500{,}000 '
        '\\Rightarrow \\text{cost} = \\text{\\textnaira}1{,}200{,}000$.',
    '2019-09/FA/mcq/10': 'The partner is charged with the plant at the **agreed (taken-over) price**, not its '
        'carrying amount: Dr. Partners\' Capital account with ₦840,000; the ₦50,000 shortfall against the '
        '₦890,000 carrying amount goes to the Revaluation account.',
    '2019-09/FA/mcq/11': 'Profit for distribution $=$ profit before adjustments $-$ Weah\'s repair expense $-$ '
        'interest on Ade\'s loan $+$ interest on drawings ($5\\%$ of $1{,}800{,}000+1{,}200{,}000=150{,}000$): '
        '$5{,}400{,}000-20{,}000-25{,}000+150{,}000 = Le\\,5{,}505{,}000$.',
    '2019-09/FA/mcq/12': 'Ade\'s share of the Le5,505,000 distributable profit (ratio 3:2) '
        '$=5{,}505{,}000\\times\\frac35=3{,}303{,}000$. Less interest on his own drawings '
        '($5\\%\\times1{,}800{,}000=90{,}000$) and his cash drawings (Le1,800,000): '
        '$3{,}303{,}000-90{,}000-1{,}800{,}000 = Le\\,1{,}413{,}000$ (the loan interest is a business expense '
        'settled outside the current account, not a current-account credit).',
    '2019-09/FA/mcq/13': 'Cash actually received in 2017 $=$ subscriptions from the $230-16=214$ members who '
        'paid for 2017 ($214\\times2{,}000=428{,}000$) $+$ the 12 members\' advance payments for 2018 '
        '($12\\times2{,}000=24{,}000$) $= GH\\text{\\textcent}452{,}000$ — the Receipts and Payments account '
        'records cash on a pure cash basis, regardless of which year it relates to.',
    '2019-09/FA/mcq/14': 'The Income and Expenditure account records the full amount **due** for the year '
        'regardless of collection: $230\\;\\text{members}\\times GH\\text{\\textcent}2{,}000 = '
        'GH\\text{\\textcent}460{,}000$.',
    '2019-09/FA/mcq/15': 'The 16 members who had not paid are a receivable (current asset): '
        '$16\\times2{,}000=GH\\text{\\textcent}32{,}000$. The 12 members who prepaid for 2018 are a liability '
        '(current liability): $12\\times2{,}000=GH\\text{\\textcent}24{,}000$.',
    '2019-09/FA/mcq/19': 'Capital $=$ net book value of non-current assets $+$ current assets $-$ current '
        'liabilities, all at 31/12/17: NBV $=960{,}000-210{,}000=750{,}000$; Capital '
        '$=750{,}000+2{,}250{,}000-450{,}000=L\\$2{,}550{,}000$.',
    '2019-09/FA/mcq/20': 'The asset sold had accumulated depreciation of $162{,}000-60{,}000=102{,}000$, removed '
        'from the provision account on disposal. Depreciation charge for 2018 (balancing figure): '
        '$222{,}000-210{,}000+102{,}000 = L\\$114{,}000$.',
    '2019-09/FA/mcq/21': 'A 25% mark-up is on cost: $1.25\\times\\text{cost}=\\text{\\textnaira}800{,}000 '
        '\\Rightarrow \\text{cost}=\\text{\\textnaira}640{,}000$.',
    '2019-09/FA/mcq/25': 'Cost of goods sent (removing the 25% mark-up) $=244{,}600\\div1.25=195{,}680$. Cost '
        'of the GMD6,000 (invoice-price) return $=6{,}000\\div1.25=4{,}800$. Net amount credited to Goods Sent '
        'to Branch (kept at cost) $=195{,}680-4{,}800=GMD\\,190{,}880$.',
    '2019-09/FA/mcq/26': 'The Branch Inventory Control account is kept **at invoice price**, so the return is '
        'credited there at its full invoice value, GMD6,000 — no conversion to cost.',

    # ---- 2020-03 FA ----
    '2020-03/FA/mcq/6': 'Foday\'s Le750,000 capital is bought out by Marie and Tejan in ratio 3:1: Marie '
        '$+750{,}000\\times\\frac34=562{,}500$, Tejan $+750{,}000\\times\\frac14=187{,}500$. New capitals: '
        'Marie $=1{,}000{,}000+562{,}500=Le\\,1{,}562{,}500$; Tejan $=500{,}000+187{,}500=Le\\,687{,}500$.',
    '2020-03/FA/mcq/7': 'Nominal value per share $= \\dfrac{\\text{\\textnaira}10{,}000{,}000}{20{,}000{,}000} '
        '= \\text{\\textnaira}0.50$.',
    '2020-03/FA/mcq/8': 'Shares issued $=95\\%\\times20{,}000{,}000=19{,}000{,}000$. Proceeds '
        '$=19{,}000{,}000\\times0.75=14{,}250{,}000$. Nominal value issued $=19{,}000{,}000\\times0.50='
        '9{,}500{,}000$. Premium $=14{,}250{,}000-9{,}500{,}000=\\text{\\textnaira}4{,}750{,}000$.',
    '2020-03/FA/mcq/17': 'Capital $=$ Assets $-$ Liabilities $= (125{,}000+50{,}000+25{,}000)-75{,}000 = '
        'GH\\text{\\textcent}125{,}000$.',
    '2020-03/FA/mcq/18': 'Current assets $=$ Trade receivables $+$ Bank $= 50{,}000+25{,}000 = '
        'GH\\text{\\textcent}75{,}000$.',
    '2020-03/FA/mcq/21': 'Total instalments (half-yearly over 4 years $=8$ instalments) '
        '$=85{,}000\\times8=680{,}000$. HP price $=$ deposit $+$ instalments $=68{,}000+680{,}000='
        'GH\\text{\\textcent}748{,}000$.',
    '2020-03/FA/mcq/22': 'Total HP interest $=$ HP price $-$ cash price $=748{,}000-150{,}000=598{,}000$, over '
        '8 instalments $=74{,}750$ each. Year one (2 instalments) $=74{,}750\\times2=GH\\text{\\textcent}'
        '149{,}500$.',
    '2020-03/FA/mcq/25': 'Annual depreciation $= \\dfrac{2{,}500{,}000-12{,}500}{10}=248{,}750$. Over 6 years '
        '(2009–2014) $=248{,}750\\times6 = L\\$1{,}492{,}500$.',
    '2020-03/FA/mcq/26': 'Over 8 years (2009–2016), accumulated depreciation $=248{,}750\\times8=1{,}990{,}000$. '
        'Carrying amount $=2{,}500{,}000-1{,}990{,}000=L\\$510{,}000$.',
    '2020-03/FA/mcq/27': 'Income $=$ cash received $-$ opening arrears (last year\'s debt collected) $-$ '
        'closing advance (next year\'s prepayment) $+$ closing arrears (this year\'s income not yet received): '
        '$840{,}000-90{,}000-45{,}000+54{,}000 = \\text{\\textnaira}759{,}000$.',
    '2020-03/FA/mcq/28': 'Monthly rent $=162{,}000\\div10=16{,}200$. The charge for the full 2016 year (12 '
        'months, continuing at the same monthly rate past the October renewal) '
        '$=12\\times16{,}200 = GMD\\,194{,}400$.',
    '2020-03/FA/mcq/29': 'The last 2 months of 2016 (Nov–Dec) are unpaid rent expense already incurred: '
        '$2\\times16{,}200=GMD\\,32{,}400$, a liability — an **accrual**, not a prepayment.',

    # ---- 2020-09 FA ----
    '2020-09/FA/mcq/1': 'Reducing balance at 15%/year: Y1 $50{,}000{,}000\\times0.85=42{,}500{,}000$; Y2 '
        '$\\times0.85=36{,}125{,}000$; Y3 $\\times0.85=30{,}706{,}250$. Cumulative depreciation after 3 years '
        '$=50{,}000{,}000-30{,}706{,}250=\\text{\\textnaira}19{,}294{,}000$ (to the nearest thousand).',
    '2020-09/FA/mcq/2': 'Continuing the reducing-balance schedule to Y5: '
        '$50{,}000{,}000\\times0.85^5 = \\text{\\textnaira}22{,}185{,}000$ (to the nearest thousand).',
    '2020-09/FA/mcq/7': 'The week-52 purchases (Le12,000) were omitted from the **control account**: '
        '$125{,}000+12{,}000=137{,}000$. The supplier balance (Le9,000) was omitted from the **list**: '
        '$128{,}000+9{,}000=137{,}000$. Both reconcile to Le137,000.',
    '2020-09/FA/mcq/9': 'Purchases of PPE (balancing figure in the PPE-at-cost account): closing cost '
        '$1{,}875{,}000$ + disposed cost $225{,}000$ − opening cost $1{,}500{,}000 = 600{,}000$ (outflow). '
        'Net investing cash flow $= -600{,}000 + 75{,}000\\;(\\text{sale proceeds}) = \\text{\\textnaira}'
        '525{,}000$ **outflow**.',
    '2020-09/FA/mcq/10': 'New share proceeds $=$ increase in share capital $+$ increase in share premium '
        '$=(6{,}000-3{,}000)+1{,}500=4{,}500$ (inflow). Loan stock repayment $=3{,}000-2{,}250=750$ (outflow). '
        'Net financing cash flow $=4{,}500-750=\\text{\\textnaira}3{,}750{,}000$ **inflow**.',
    '2020-09/FA/mcq/14': 'Recording the GH¢260 purchase twice means an extra, unmatched debit of GH¢260 in the '
        'Purchases account — the trial balance\'s debit total then exceeds its credit total by GH¢260, needing '
        'a GH¢260 **credit** to Suspense to balance, exactly the credit balance described.',
    '2020-09/FA/mcq/22': 'A zero-rated entity cannot reclaim input VAT, so the VAT becomes part of the cost: '
        '$45{,}000 + (5\\%\\times45{,}000) = 45{,}000+2{,}250 = \\text{\\textnaira}47{,}250$ charged to repairs.',
    '2020-09/FA/mcq/25': 'Net profit $+$ adjustment for non-cash items $=$ cash generated before working-capital '
        'changes: Net profit $= 3{,}540-(-2{,}080) = \\text{\\textnaira}5{,}620{,}000$.',
    '2020-09/FA/mcq/26': 'The non-cash adjustment total (−2,080) is made up of: $-2{,}440\\;(\\text{revaluation '
        'gain}) + 840\\;(\\text{depreciation}) + 140\\;(\\text{loss on machinery}) - X\\;(\\text{profit on sale '
        'of investment}) = -2{,}080$, giving $X = \\text{\\textnaira}620{,}000$.',

    # ---- 2021-03 FA ----
    '2021-03/FA/mcq/4': 'Goodwill (₦4m) is credited in the **old** ratio (2:3) then written off in the '
        '**new** ratio (3:6:1) — Paul\'s share is $\\frac35$ under both ($3\\div5=6\\div10$), so his goodwill '
        'credit and debit exactly cancel. Revaluation surplus (₦3.5m) is credited only in the old ratio: Paul '
        '$=3{,}500{,}000\\times\\frac35=\\text{\\textnaira}2{,}100{,}000$ — his entire net credit from the two.',
    '2021-03/FA/mcq/5': 'Peter\'s ratio changes from $\\frac25$ (old) to $\\frac{3}{10}$ (new), so his goodwill '
        'nets to a credit of $4{,}000{,}000\\times(\\frac25-\\frac{3}{10})=400{,}000$. Adding his revaluation '
        'share $3{,}500{,}000\\times\\frac25=1{,}400{,}000$: total credit $=1{,}800{,}000$. Balance '
        '$=4{,}500{,}000+1{,}800{,}000=\\text{\\textnaira}6{,}300{,}000$.',
    '2021-03/FA/mcq/9': 'Drawings $=$ Net profit $+$ Capital introduced $-$ Increase in net assets '
        '$= 1{,}051{,}000+100{,}000-733{,}000 = GH\\text{\\textcent}418{,}000$.',
    '2021-03/FA/mcq/13': 'Income $=$ cash collected $+$ opening advance (now earned) $-$ closing advance (not '
        'yet earned) $= 400{,}000+50{,}000-25{,}000 = L\\$425{,}000$.',
    '2021-03/FA/mcq/15': 'Commission is 5% of the surplus **after** charging itself: '
        '$C = \\dfrac{0.05}{1.05}\\times Le\\,50{,}400 = Le\\,2{,}400$.',
    '2021-03/FA/mcq/23': 'Profit $=$ closing net assets $-$ opening net assets $+$ drawings '
        '$=5{,}914{,}583-4{,}250{,}000+3{,}152{,}084=GMD\\,4{,}816{,}667$.',
    '2021-03/FA/mcq/26': 'HP price $=$ deposit $+$ instalments $=50{,}000+(45{,}000\\times10)=\\text{\\textnaira}'
        '500{,}000$.',
    '2021-03/FA/mcq/27': 'Total interest $=$ HP price $-$ cash price $=500{,}000-400{,}000=100{,}000$, spread '
        'equally over 10 months: $100{,}000\\div10=\\text{\\textnaira}10{,}000$/month.',
    '2021-03/FA/mcq/30': 'A 25% mark-up is on cost: $1.25\\times\\text{cost}=GH\\text{\\textcent}9{,}000{,}000 '
        '\\Rightarrow \\text{cost}=GH\\text{\\textcent}7{,}200{,}000$.',

    # ---- 2021-09 FA ----
    '2021-09/FA/mcq/2': 'Issue price (₦1.20) exceeds the ₦1.00 par value: premium '
        '$=\\text{\\textnaira}1.20-1.00 = 20$kobo per share.',
    '2021-09/FA/mcq/3': 'Average inventory $=\\dfrac{370{,}000+260{,}000}{2}=315{,}000$. Turnover '
        '$=\\dfrac{3{,}307{,}500}{315{,}000}=10.5$ times.',
    '2021-09/FA/mcq/7': 'Good receivables after bad debts $=1{,}200{,}000-5{,}000=1{,}195{,}000$; required '
        'provision $=3\\%\\times1{,}195{,}000=35{,}850$. The **charge to profit or loss** is only the increase '
        'over the existing ₦25,000 provision: $35{,}850-25{,}000=\\text{\\textnaira}10{,}850$.',
    '2021-09/FA/mcq/8': 'Statement of financial position value $=$ good receivables $-$ the full closing '
        'provision $=1{,}195{,}000-35{,}850=\\text{\\textnaira}1{,}159{,}150$.',
    '2021-09/FA/mcq/11': 'Net receivable after doubtful debts $=750{,}000-75{,}000=675{,}000$. Discount '
        'provision $=5\\%\\times675{,}000=33{,}750$. Receivable shown $=750{,}000-75{,}000-33{,}750='
        '\\text{\\textnaira}641{,}250$.',
    '2021-09/FA/mcq/21': 'The return was overstated by $96{,}960-96{,}690=270$, overstating both Purchases '
        'Returns (credit) and Payables (debit) by that amount. Correct by reversing the excess: Dr. Purchases '
        'returns ₦270, Cr. Payables ₦270.',
    '2021-09/FA/mcq/29': 'Cost of sales $=220{,}000+1{,}500{,}000-260{,}000=1{,}460{,}000$. Average inventory '
        '$=\\dfrac{220{,}000+260{,}000}{2}=240{,}000$. Turnover $=\\dfrac{1{,}460{,}000}{240{,}000}\\approx6.1$ '
        'times.',
    '2021-09/FA/mcq/30': 'Under the average clause, the claim is scaled by the ratio of the policy to the total '
        'stock at risk (destroyed $+$ salvaged): $1{,}800{,}000\\times\\dfrac{1{,}600{,}000}{1{,}800{,}000+'
        '200{,}000} = \\text{\\textnaira}1{,}440{,}000$.',

    # ---- 2022-03 FA ----
    '2022-03/FA/mcq/3': 'The GMD15,000 receipt was posted to the **wrong side** of the cash book — a full '
        'reversal. Correcting it needs **double** the amount: Dr. Cash Book GMD30,000, Cr. Teniola Amusan '
        'account GMD30,000.',
    '2022-03/FA/mcq/4': 'Net profit 2,800,000 $+$ interest on drawings ($4\\%\\times300{,}000=12{,}000$ for '
        'Alex, $4\\%\\times400{,}000=16{,}000$ for Umaru, total 28,000) $-$ interest on capital '
        '($3\\%\\times1{,}500{,}000=45{,}000$ for Alex, $3\\%\\times2{,}500{,}000=75{,}000$ for Umaru, total '
        '120,000) $= 2{,}800{,}000+28{,}000-120{,}000 = \\text{\\textnaira}2{,}708{,}000$ distributable.',
    '2022-03/FA/mcq/5': 'Alex\'s profit share (ratio 2:5 of ₦2,708,000) $=2{,}708{,}000\\times\\frac25='
        '1{,}083{,}200$. Adding his own interest on capital (₦45,000) and deducting his own interest on '
        'drawings (₦12,000): $1{,}083{,}200+45{,}000-12{,}000 = \\text{\\textnaira}1{,}116{,}200$.',
    '2022-03/FA/mcq/6': 'Umaru\'s profit share (ratio 3:5 of ₦2,708,000) $=2{,}708{,}000\\times\\frac35='
        '\\text{\\textnaira}1{,}624{,}800$, debited to the Appropriation Account and credited to his Capital '
        'account.',
    '2022-03/FA/mcq/10': 'Capitalised building cost $=$ new construction $+$ architect fees $+$ cost of razing '
        'the old building on the site (all directly attributable to getting the new building ready): '
        '$1{,}850{,}000+95{,}000+60{,}000 = GH\\text{\\textcent}2{,}005{,}000$ (the insurance/legal fee to '
        'purchase the land is a **land** cost, not part of the building).',
    '2022-03/FA/mcq/11': 'By 30 June, the 16 May–15 June bill (Le6,000,000) is fully incurred but still unpaid, '
        'and half of the 16 June–15 July bill (15 of its 30 days) is also accrued: '
        '$6{,}000{,}000 + \\tfrac12\\times8{,}000{,}000 = Le\\,10{,}000{,}000$ outstanding.',
    '2022-03/FA/mcq/17': 'Total estimated contract profit $=3{,}500{,}000-2{,}500{,}000=1{,}000{,}000$. '
        'Interim (attributable) profit is taken in proportion to progress, approximated here by cash received '
        'to date over contract price: $1{,}000{,}000\\times\\dfrac{2{,}625{,}000}{3{,}500{,}000} = '
        'GH\\text{\\textcent}750{,}000$.',
    '2022-03/FA/mcq/24': 'Closing cash & equivalents $=1{,}000+20{,}402-0=21{,}402$. Opening cash & equivalents '
        '$=1{,}100+0-26{,}071=-24{,}971$ (an overdraft). Net movement for the period '
        '$=21{,}402-(-24{,}971) = L\\$46{,}373$.',
    '2022-03/FA/mcq/27': 'Expected cost of sales at the standard 25% margin $=306{,}000\\times(1-0.25)='
        '229{,}500$. Inventory that should remain $=159{,}000+206{,}000-229{,}500=135{,}500$. Inventory lost '
        '$=135{,}500-107{,}000 = GMD\\,28{,}500$ thousand $=$ GMD28,500,000.',
    '2022-03/FA/mcq/29': 'Cost of goods sold $=300{,}000+2{,}500{,}000-200{,}000=2{,}600{,}000$. Gross profit '
        '$=3{,}500{,}000-2{,}600{,}000 = Le\\,900{,}000$ **profit**.',

    # ---- 2022-09 FA ----
    '2022-09/FA/mcq/3': 'Combined old capital $=600{,}000+750{,}000+1{,}050{,}000=2{,}400{,}000$. Adding Dapo\'s '
        '₦750,000 cash gives a new total of ₦3,150,000; his one-fifth interest '
        '$=3{,}150{,}000\\div5=\\text{\\textnaira}630{,}000$.',
    '2022-09/FA/mcq/9': 'Gross profit $=$ net profit $+$ other expenses $=180{,}000+400{,}000=580{,}000$. Cost '
        'of sales $=2{,}200{,}000-580{,}000=1{,}620{,}000$. Purchases $=$ COGS $-$ opening inventory $+$ '
        'closing inventory $=1{,}620{,}000-480{,}000+1{,}280{,}000 = GH\\text{\\textcent}2{,}420{,}000$.',
    '2022-09/FA/mcq/10': 'Wages expense $=$ paid ₦25,000 $+$ accrued-but-unpaid ₦5,000 $=$ ₦30,000 charged to '
        'profit or loss; the unpaid ₦5,000 is shown as an accrual (current liability) in the statement of '
        'financial position.',
    '2022-09/FA/mcq/20': 'Of the ₦820,000 paid, ₦100,000 settles last year\'s (2019) outstanding rent, leaving '
        '$820{,}000-100{,}000=720{,}000$ as the genuine 3-year prepayment. Annual charge '
        '$=720{,}000\\div3=\\text{\\textnaira}240{,}000$.',
    '2022-09/FA/mcq/27': 'Issue price (50k) is below the 80k nominal value: discount '
        '$=80k-50k=30k$ per share.',
    '2022-09/FA/mcq/28': 'Omitting an accrual means the corresponding **payable is never recorded**, so '
        'liabilities are understated by the full GMD365,000.',

    # ---- 2023-03 FA ----
    '2023-03/FA/mcq/7': 'Revenue reported $=$ Sales $-$ returns $=5{,}000-400=GH\\text{\\textcent}4{,}600{,}000$ '
        '(thousand). The gain on the motor vehicle is other income, not revenue, and cash collected is '
        'irrelevant on the accrual basis.',
    '2023-03/FA/mcq/13': 'The partner is charged with the vehicle at the **agreed (taken-over) value**, not its '
        'carrying amount: Debit the partner\'s capital account with ₦177,000; the ₦63,000 shortfall against '
        'the ₦240,000 carrying amount goes to the Realisation account.',
    '2023-03/FA/mcq/20': 'A decrease in trade receivables means more cash was collected than revenue earned: '
        'Cash collected $=$ Revenue $+$ decrease in receivables $=245+38=Le\\,283$ million (the change in '
        'inventory is unrelated to cash collected from customers).',
    '2023-03/FA/mcq/21': 'Gross profit at $33\\tfrac13\\%$ of sales $=6{,}900\\times\\tfrac13=2{,}300$. Cost of '
        'sales $=6{,}900-2{,}300=4{,}600$. Purchases $=$ COGS $-$ opening inventory $+$ closing inventory '
        '$=4{,}600-1{,}400+540 = GMD\\,3{,}740$ thousand.',
    '2023-03/FA/mcq/22': 'The ₦2,000 contra was posted to the **wrong side**, a full reversal that overstates '
        'the balance by double the amount: $84{,}750-(2\\times2{,}000) = \\text{\\textnaira}80{,}750$.',
    '2023-03/FA/mcq/23': 'Last year\'s ₦25,000 over-provision reduces **this year\'s tax charge**: '
        '$141{,}000-25{,}000=GMD\\,116{,}000$. The **liability** carried forward is the full current-year '
        'estimate, GMD141,000 (the over-provision is a P&L adjustment, not a balance-sheet one).',
    '2023-03/FA/mcq/28': 'Required allowance $=2.5\\%\\times1{,}000{,}000=25{,}000$, down from the ₦40,000 '
        'opening allowance — a **decrease** of $40{,}000-25{,}000=GH\\text{\\textcent}15{,}000$, recognised as '
        'a **credit** (income) in profit or loss.',

    # ---- 2023-09 FA ----
    '2023-09/FA/mcq/3': 'Income for 2021 $=$ cash received $-$ the ₦35,000 meant for 2022 $-$ the ₦50,000 '
        'opening arrears (which relates to the prior year, even though collected this year): '
        '$650{,}000-35{,}000-50{,}000 = Le\\,565{,}000$.',
    '2023-09/FA/mcq/4': 'Of the Le650,000 received, only the Le35,000 advance for 2022 remains unresolved at '
        'year end — the full 2021 income (Le565,000) was collected in cash, leaving just this advance '
        '(a current liability) on the statement of financial position.',
    '2023-09/FA/mcq/8': 'Carrying amount $=80\\text{m}-68\\text{m}=12\\text{m}$. Net proceeds '
        '$=10\\text{m}-5\\text{m}\\;(\\text{disposal cost})=5\\text{m}$. Loss on disposal '
        '$=12\\text{m}-5\\text{m}=\\text{\\textnaira}7$m.',
    '2023-09/FA/mcq/10': 'Reducing balance at 20%/year: Y1 $100\\text{m}\\times0.8=80\\text{m}$; Y2 '
        '$\\times0.8=64\\text{m}$; Y3 $\\times0.8=\\text{\\textnaira}51.2$m.',
    '2023-09/FA/mcq/11': 'Existing shares $=\\text{\\textnaira}200{,}000\\div0.50=400{,}000$. A 1-for-4 rights '
        'issue adds $400{,}000\\div4=100{,}000$ shares at ₦1.50: value $=100{,}000\\times1.50='
        '\\text{\\textnaira}150{,}000$.',
    '2023-09/FA/mcq/12': 'Premium per rights share $=1.50-0.50=1.00$; new premium '
        '$=100{,}000\\times1.00=100{,}000$. Balance $=150{,}000+100{,}000 = \\text{\\textnaira}250{,}000$.',
    '2023-09/FA/mcq/28': 'Rent in arrears is an unrecorded accrued liability, so omitting it means liabilities '
        'are **understated** by ₦120,000.',

    # ---- 2024-03 FA ----
    '2024-03/FA/mcq/2': 'Receivable collection period $= \\dfrac{\\text{Receivables}}{\\text{Revenue}}\\times '
        '\\text{days in year} = \\dfrac{25}{500}\\times366 = 18.30$ days (a leap year has 366 days).',
    '2024-03/FA/mcq/5': 'Closing equity $=$ opening net assets $+$ profit $-$ drawings $+$ capital injected '
        '$=2{,}680{,}000+1{,}000{,}000-880{,}000+160{,}000 = GH\\text{\\textcent}2{,}960{,}000$.',
    '2024-03/FA/mcq/6': '"Motor vehicle sales" is **income**, which belongs in the 600–699 range, not 192 '
        '(current assets, 200–299).',
    '2024-03/FA/mcq/7': '"Injection of share capital" is equity, and 521 falls correctly within the 500–599 '
        'equity range.',
    '2024-03/FA/mcq/8': 'Straight-line depreciation $= \\dfrac{100{,}000-20{,}000}{5} = \\text{\\textnaira}'
        '16{,}000$ per year.',
    '2024-03/FA/mcq/11': 'Cost of sales $=$ opening inventory $+$ purchases $-$ closing inventory '
        '$=3{,}100+42{,}100-4{,}000=41{,}200$. At a 40% mark-up on cost, revenue '
        '$=41{,}200\\times1.4 = Le\\,57{,}680$.',
    '2024-03/FA/mcq/12': 'A **decrease** in receivables ($32{,}000\\to27{,}000$) releases cash ($+5{,}000$); an '
        '**increase** in inventory ($49{,}000\\to53{,}000$) ties up cash ($-4{,}000$); a **decrease** in '
        'payables ($17{,}000\\to11{,}000$) uses cash ($-6{,}000$). Net: $5{,}000-4{,}000-6{,}000 = '
        '\\text{\\textnaira}5{,}000$ **decrease**.',
    '2024-03/FA/mcq/13': 'Carrying amount $=50\\text{m}-20\\text{m}=30\\text{m}$. Since the loss on disposal is '
        '₦8m, proceeds $=30\\text{m}-8\\text{m}=\\text{\\textnaira}22$m — the amount shown as an investing '
        '**inflow**.',
    '2024-03/FA/mcq/14': 'After deducting salaries (Y ₦100,000, Z ₦150,000) from the ₦1,000,000 net profit, '
        'the residual ₦750,000 is split 2:2:1: X and Y each get $750{,}000\\times\\frac25=300{,}000$, Z gets '
        '$750{,}000\\times\\frac15=150{,}000$. Adding back salaries: X=₦300,000, Y=$300{,}000+100{,}000='
        '400{,}000$, Z=$150{,}000+150{,}000=300{,}000$.',
    '2024-03/FA/mcq/24': 'Gross profit margin $33\\tfrac13\\%$ on sales, GP $=\\text{\\textnaira}800{,}000 '
        '\\Rightarrow Sales = 800{,}000\\div\\tfrac13=2{,}400{,}000$. Net profit '
        '$=800{,}000-680{,}000=120{,}000$. Net margin $=120{,}000\\div2{,}400{,}000=5.00\\%$.',
    '2024-03/FA/mcq/30': 'Selling goods at a profit: $+\\text{\\textnaira}50{,}000$ net assets. Recovering a '
        'previously written-off debt in full: $+\\text{\\textnaira}50{,}000$ net assets. Paying suppliers: cash '
        'and payables fall by the same amount — **no** net-asset effect. Combined: '
        '$50{,}000+50{,}000 = \\text{\\textnaira}100{,}000$ increase.',

    # ---- 2024-09 FA ----
    '2024-09/FA/mcq/8': 'Good receivables after bad debts $=4{,}800{,}000-20{,}000=4{,}780{,}000$; required '
        'allowance $=3\\%\\times4{,}780{,}000=143{,}400$. The **charge for the year** is only the increase over '
        'the existing ₦100,000 allowance: $143{,}400-100{,}000=\\text{\\textnaira}43{,}400$.',
    '2024-09/FA/mcq/9': 'Statement of financial position value $=$ good receivables $-$ the full closing '
        'allowance $=4{,}780{,}000-143{,}400=\\text{\\textnaira}4{,}636{,}600$.',
    '2024-09/FA/mcq/10': 'Reducing balance at 20%/year from 1 Jan 2019: 2019 dep $=100{,}000$, CA$=400{,}000$; '
        '2020 dep $=80{,}000$, CA$=320{,}000$; Jan–Mar 2021 (3 months) dep $=\\frac{3}{12}\\times20\\%\\times'
        '320{,}000=16{,}000$, CA at disposal$=304{,}000$. Loss $=304{,}000-300{,}000=GH\\text{\\textcent}4{,}000$.',
    '2024-09/FA/mcq/11': 'The GH¢202,500 premium covers 15 months (Jan 2021–Mar 2022): $202{,}500\\div15='
        '13{,}500$/month. The 2021 charge (12 months) $=12\\times13{,}500=GH\\text{\\textcent}162{,}000$.',
    '2024-09/FA/mcq/13': 'Net profit 2,800,000 $+$ interest on drawings ($4\\%\\times300{,}000=12{,}000$ for '
        'Ajax, $4\\%\\times400{,}000=16{,}000$ for United) $-$ interest on capital ($3\\%\\times1{,}500{,}000='
        '45{,}000$ for Ajax, $3\\%\\times2{,}500{,}000=75{,}000$ for United) $=2{,}800{,}000+28{,}000-120{,}000 '
        '= L\\$2{,}708{,}000$.',
    '2024-09/FA/mcq/14': 'Ajax\'s profit share (ratio 2:5) $=2{,}708{,}000\\times\\frac25=1{,}083{,}200$. Adding '
        'his own interest on capital (₦45,000) and deducting his own interest on drawings (₦12,000): '
        '$1{,}083{,}200+45{,}000-12{,}000 = L\\$1{,}116{,}200$.',
    '2024-09/FA/mcq/15': 'A $\\frac14$ mark-up on cost (cost 4, profit 1, price 5) gives a margin of '
        '$1\\div5=20\\%$ for X. A $\\frac13$ mark-up (cost 3, profit 1, price 4) gives a margin of '
        '$1\\div4=25\\%$ for Y.',
    '2024-09/FA/mcq/18': 'Dividends on ordinary shares are a percentage of **nominal (par) value**, not issue '
        'price: nominal value $=10{,}000{,}000\\times0.50=5{,}000{,}000$; dividend '
        '$=5\\%\\times5{,}000{,}000=\\text{\\textnaira}250{,}000$.',
    '2024-09/FA/mcq/23': 'Cash from customers $=$ opening receivables $+$ revenue $-$ closing receivables '
        '$=160{,}000+5{,}200{,}000-120{,}000=5{,}240{,}000$. Cash to suppliers $=$ opening payables $+$ '
        'purchases $-$ closing payables $=200{,}000+2{,}260{,}000-220{,}000=GMD\\,2{,}240{,}000$.',
    '2024-09/FA/mcq/24': 'Cash flow from operations (direct method) $=5{,}240{,}000-2{,}240{,}000\\;'
        '(\\text{suppliers})-1{,}620{,}000\\;(\\text{employees})-480{,}000\\;(\\text{general expenses}) = '
        'GMD\\,900{,}000$.',

    # ---- 2025-03 FA ----
    '2025-03/FA/mcq/3': 'Annual depreciation $=\\dfrac{5{,}000{,}000-1{,}000{,}000}{4}=1{,}000{,}000$. With '
        'depreciation charged in the year of disposal, 3 full years (2020–2022) are charged: '
        '$3\\times1{,}000{,}000=3{,}000{,}000$. Carrying amount at disposal $=5{,}000{,}000-3{,}000{,}000='
        '2{,}000{,}000$. Loss $=2{,}000{,}000-1{,}600{,}000=\\text{\\textnaira}400{,}000$.',
    '2025-03/FA/mcq/20': 'A 25% mark-up is on cost: $1.25\\times\\text{cost}=\\text{\\textnaira}1{,}500{,}000 '
        '\\Rightarrow \\text{cost}=\\text{\\textnaira}1{,}200{,}000$.',
    '2025-03/FA/mcq/26': 'IAS 2 values inventory at the **lower of cost and NRV**, item by item: A (cost 300 '
        '$<$ NRV 420) stays at cost, $150\\times300=45{,}000$; B (NRV 350 $<$ cost 400) is written down, '
        '$175\\times350=61{,}250$. Total $=45{,}000+61{,}250=\\text{\\textnaira}106{,}250$.',
    '2025-03/FA/mcq/27': 'Only item B needs writing down (NRV 350 $<$ cost 400): '
        '$(400-350)\\times175=\\text{\\textnaira}8{,}750$ charged to profit or loss.',
    '2025-03/FA/mcq/29': 'Total assets $=750{,}000+120{,}000=870{,}000$. Equity $=$ assets $-$ liabilities '
        '$=870{,}000-50{,}000=820{,}000$. Retained earnings $=$ equity $-$ share capital '
        '$=820{,}000-500{,}000=\\text{\\textnaira}320{,}000$ thousand $=$ ₦320,000,000.',

    # ---- 2025-09 FA ----
    '2025-09/FA/mcq/2': 'Sales was wrongly **debited** ₦16,898 instead of credited — a full reversal on that '
        'account. Correcting it needs **double** the amount: Dr. Suspense ₦33,796, Cr. Sales ₦33,796 (Bank was '
        'already correctly debited).',
    '2025-09/FA/mcq/3': 'Since **no entry at all** was made, both the missing debit (drawings) and missing '
        'credit (purchases/inventory) are equally absent — the trial balance still balances and is '
        '**correctly stated**, even though drawings and inventory are individually wrong.',
    '2025-09/FA/mcq/12': 'Share premium $=2{,}000{,}000\\;\\text{shares}\\times\\text{\\textnaira}15='
        '\\text{\\textnaira}30{,}000{,}000$.',
    '2025-09/FA/mcq/13': 'X\'s entire goodwill share (ratio 4:7, since X retires completely) '
        '$=300{,}000\\times\\frac47 = \\text{\\textnaira}171{,}429$, paid to X by Y.',
    '2025-09/FA/mcq/19': 'Gross profit margin $=\\dfrac{200\\text{m}}{500\\text{m}}=40\\%$.',
    '2025-09/FA/mcq/20': 'Straight-line depreciation $=\\dfrac{12{,}000{,}000-0}{5}=\\text{\\textnaira}'
        '2{,}400{,}000$ per year.',
    '2025-09/FA/mcq/25': 'A $\\frac13$ mark-up on cost X (cost 3, profit 1, price 4) gives a margin of '
        '$1\\div4=25\\%$. A $\\frac14$ mark-up on cost Y (cost 4, profit 1, price 5) gives a margin of '
        '$1\\div5=20\\%$.',
    '2025-09/FA/mcq/27': 'Distributable profit $=$ net profit $+$ interest on drawings $-$ interest on capital '
        '$= 5{,}600{,}000+(12{,}000+16{,}000)-(45{,}000+75{,}000) = \\text{\\textnaira}5{,}508{,}000$.',
    '2025-09/FA/mcq/28': 'Ajadi\'s profit share (ratio 2:5) $=5{,}508{,}000\\times\\frac25=2{,}203{,}200$. '
        'Adding his own interest on capital (₦45,000) and deducting his own interest on drawings (₦12,000): '
        '$2{,}203{,}200+45{,}000-12{,}000 = \\text{\\textnaira}2{,}236{,}200$.',

    # ---- 2026-03 FA ----
    '2026-03/FA/mcq/3': 'Removing the asset\'s carrying amount decreases non-current assets by ₦200,000; the '
        'cash received increases current assets by ₦180,000 (the ₦20,000 difference is a loss on disposal, '
        'not an asset).',
    '2026-03/FA/mcq/7': 'With debit and credit totals of L$23,500,000 and L$25,500,000, the errors causing the '
        'imbalance net out at the midpoint: $\\dfrac{23{,}500+25{,}500}{2} = L\\$24{,}500{,}000$.',
    '2026-03/FA/mcq/12': 'Cash is received before the service is performed, so the obligation is a liability, '
        'not revenue yet: Dr. Cash L$10,000; Cr. Unearned Revenue L$10,000.',
    '2026-03/FA/mcq/13': 'Profit $=$ closing capital $-$ opening capital $+$ drawings $-$ capital introduced '
        '$=70{,}000-50{,}000+10{,}000-5{,}000 = L\\$25{,}000$.',
    '2026-03/FA/mcq/30': 'Increases in inventory and receivables **use** cash; increases in payables and bills '
        'payable **release** cash: $-2{,}240-4{,}640+920+960 = -GH\\text{\\textcent}5{,}000$ thousand, i.e. a '
        '₦5,000,000 net use of cash.',
}
SECB_NOTES = {}
