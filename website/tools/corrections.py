"""
Hand-curated corrections applied on the way out of the extractors.

CHAPTER_KEYS  distinctive vocabulary per chapter. Retrieval alone mis-files a
              question whose subject-matter words are rare in the study text
              ("shadow price", "dummy activity"); these terms are boosted hard.
PIN           explicit chapter for a question retrieval still gets wrong.
FLAGS         defects in the printed papers, shown to the reader rather than
              silently patched.
"""

# ── chapter seed vocabulary ───────────────────────────────────────────────
CHAPTER_KEYS = {
 'FA': {
  1: 'bookkeeping stewardship ifrs iasb frcn ias standard-setting sole proprietorship '
     'partnership company entity types stakeholder governance director',
  2: 'conceptual framework qualitative characteristic faithful representation relevance '
     'comparability verifiability timeliness understandability recognition derecognition '
     'measurement historical cost fair value capital maintenance going concern accrual '
     'element asset liability equity income expense ifrs18',
  3: 'accounting equation double entry debit credit ledger trial balance journal daybook '
     'prime entry source document invoice credit note petty cash imprest suspense '
     'error omission commission principle compensating reversal chart of accounts worksheet',
  4: 'prepayment accrual accrued prepaid deferred revenue bad debt irrecoverable allowance '
     'doubtful provision matching discount receivable written off recovered',
  5: 'control account reconciliation bank statement uncredited unpresented cheque lodgement '
     'standing order direct debit dishonoured overdraft cash book adjusted balance contra',
  6: 'incomplete record single entry statement of affairs net asset margin markup '
     'unbanked cash sales capital comparison method missing figure',
  7: 'ias8 accounting policy estimate error retrospective prospective restatement '
     'prior period comparative change disclosure consistency',
  8: 'not-for-profit club society receipts and payments income and expenditure subscription '
     'accumulated fund life membership bar trading surplus deficit levy donation legacy',
  9: 'non-current asset depreciation straight line reducing balance revaluation disposal '
     'carrying amount residual value useful life impairment ias16 ias38 intangible '
     'amortisation register componentisation gain loss on disposal',
  10: 'partnership appropriation current account capital account interest on drawings '
      'interest on capital salary profit sharing ratio guaranteed share goodwill',
  11: 'admission retirement death dissolution amalgamation realisation garner murray '
      'revaluation account conversion to company piecemeal',
  12: 'inventory ias2 fifo lifo weighted average cost net realisable value periodic '
      'perpetual continuous stocktake cut-off write down valuation',
  13: 'company financial statement share capital premium bonus issue rights issue '
      'debenture loan note dividend taxation reserve ias1 statement of changes in equity',
  14: 'statement of cash flows ias7 operating investing financing direct indirect method '
      'working capital movement corporate entity presentation',
  15: 'ratio analysis interpretation profitability liquidity gearing efficiency current '
      'ratio acid test quick gross margin roce return on equity inventory turnover '
      'receivable days payable days earnings per share dividend cover horizontal vertical',
  16: 'ethics integrity objectivity confidentiality professional competence behaviour '
      'threat safeguard blockchain cloud artificial intelligence spreadsheet accounting '
      'software cyber ifac code',
 },
 'PS': {
  1: 'public sector accounting definition objective cash basis accrual basis commitment '
     'fund accounting government difference private sector users',
  2: 'constitution 1999 finance control management act audit act fiscal responsibility '
     'regulatory framework financial regulations treasury circular legislation',
  3: 'standardisation reporting format chart of accounts gifmis npc national chart '
     'segment code economic administrative functional',
  4: 'pension gratuity pencom pension reform act contributory scheme retirement savings '
     'account pfa pfc rsa defined benefit defined contribution',
  5: 'ipsas 39 employee benefit short-term post-employment termination retirement benefit '
     'plan actuarial defined',
  6: 'budget budgeting zero-based incremental performance planning programming ppbs '
     'medium term expenditure framework mtef envelope appropriation warrant virement '
     'call circular capital recurrent estimate',
  7: 'accounting officer accountant general auditor general treasury minister permanent '
     'secretary sub-accounting officer authorisation warrant expenditure responsibility',
  8: 'voucher payment voucher receipt voucher journal voucher adjustment classification '
     'register loss of voucher security',
  9: 'revenue tax non-tax independent statutory allocation federation account vat '
     'customs excise royalty licence fine fee earning',
  10: 'procurement bureau public procurement act tender bid due process open competitive '
      'selective restricted certificate of no objection threshold prequalification',
  11: 'inventory store ledger bin card losses cash shortage stock verification board of '
      'survey pilferage write-off surcharge',
  12: 'local government councillor chairman joint account allocation committee '
      'model financial memoranda departmental revenue rate tenement',
  13: 'cashbook transcript subsidiary account monthly return below the line above the line '
      'ipsas cash basis payment schedule mandate',
  14: 'statutory financial statement cash basis consolidated revenue fund statement of '
      'cash receipts and payments ipsas cash notes to the account',
  15: 'ipsas 33 first-time adoption transitional provision three-year exemption opening '
      'statement deemed cost',
  16: 'accrual basis ipsas statement of financial performance financial position net '
      'assets equity consolidated general purpose financial statement',
  17: 'government business entity parastatal agency commercialised privatised '
      'public corporation tertiary institution hospital',
  18: 'internal control internal audit financial management control system check '
      'segregation of duty variance monitoring evaluation value for money',
  19: 'interpretation ratio public sector liquidity solvency budget performance '
      'index analysis trend',
  20: 'investment appraisal project payback net present value internal rate of return '
      'discounted cash flow profitability index cost benefit social discount rate',
  21: 'treasury single account tsa e-payment e-collection atrrs ippis gifmis ghost worker '
      'open treasury portal e-receipt fter e-invoicing nrs tmras remita zero balanced '
      'account cash management economic reform governance project ergp',
  22: 'efcc economic financial crimes commission icpc corrupt practices code of conduct '
      'bureau tribunal public complaints commission ombudsman money laundering '
      'gratification bribery asset declaration judiciary ethics',
  23: 'audit auditor general public accounts committee compliance financial performance '
      'value for money economy efficiency effectiveness internal audit intosai code of '
      'ethics audit query surcharge sanction pre-payment post-payment interim final '
      'management operational vouching verification audit',
 },
 'QA': {
  1: 'primary secondary data questionnaire census sample sampling frame random stratified '
     'systematic cluster quota histogram bar chart pie chart ogive frequency distribution '
     'class interval tally spss population enumeration',
  2: 'arithmetic mean median mode geometric harmonic quartile decile percentile partition '
     'grouped ungrouped assumed mean midpoint modal class',
  3: 'range mean deviation variance standard deviation quartile deviation semi interquartile '
     'coefficient of variation skewness dispersion spread pearson',
  4: 'correlation regression scatter spearman rank pearson product moment least squares '
     'gradient slope intercept coefficient of determination dependent independent variable',
  5: 'time series trend seasonal cyclical irregular moving average centred additive '
     'multiplicative deseasonalised seasonal index forecast semi average',
  6: 'index number price relative quantity relative laspeyres paasche fisher marshall '
     'edgeworth base year weighted unweighted aggregate consumer price index inflation',
  7: 'probability sample space event mutually exclusive independent conditional addition '
     'multiplication law complement expected value permutation combination tree diagram dice coin',
  8: 'hypothesis null alternative type i type ii error significance level critical region '
     'test statistic two-tailed one-tailed z test t test population mean proportion',
  9: 'cost price selling price profit loss percentage markup margin trade discount cash '
     'discount marked price commission',
  10: 'set union intersection complement subset universal venn euler cardinality element '
      'disjoint de morgan',
  11: 'function linear quadratic domain range polynomial exponential logarithmic simultaneous '
      'equation break-even inequality graph gradient roots factorisation',
  12: 'simple interest compound interest annuity perpetuity sinking fund amortisation '
      'arithmetic progression geometric progression sequence series present value future '
      'value discounting net present value internal rate of return principal',
  13: 'differentiation derivative integration integral marginal cost marginal revenue '
      'maxima minima turning point stationary elasticity consumer surplus producer surplus '
      'definite indefinite constant of integration chain product quotient rule',
  14: 'operations research model stages methodology deterministic stochastic '
      'formulation validation implementation',
  15: 'linear programming objective function constraint feasible region corner point '
      'graphical simplex slack surplus artificial variable shadow price dual '
      'maximisation minimisation optimal',
  16: 'inventory economic order quantity eoq holding cost ordering cost carrying cost '
      'reorder level buffer safety stock lead time stockout shortage cost',
  17: 'network analysis critical path activity event node arrow dummy float total free '
      'independent earliest latest start finish pert cpm duration project',
  18: 'replacement deteriorate wear out gradual failure sudden failure group individual '
      'replacement policy optimal replacement period running cost resale value maintenance',
  19: 'transportation assignment north west corner least cost vogel approximation '
      'hungarian degenerate balanced unbalanced dummy row column allocation origin destination',
  20: 'simulation monte carlo random number pseudo random queue arrival service '
      'random number range trial replication',
 },
 'IT': {
  1: 'system theory subsystem environment coupling decoupling feedback control data '
     'information characteristic value binary decimal number base conversion database '
     'field record file data cleansing acquisition analysis computer generation '
     'classification analogue digital mainframe mini micro',
  2: 'hardware input output device keyboard mouse scanner ocr omr micr printer monitor '
     'plotter cpu alu control unit register cache ram rom primary secondary storage '
     'magnetic optical solid state cloud application control',
  3: 'software operating system utility loader editor compiler interpreter assembler '
     'language processor multitasking multiprogramming multiprocessing spooling virtual '
     'memory application package off-the-shelf bespoke integrated programming language '
     'generation grid computing windows explorer',
  4: 'batch processing online real time remote job entry centralised decentralised '
     'distributed information centre bureau management information system decision '
     'support executive expert transaction processing e-commerce e-government atm '
     'remita open treasury electronic payment revenue model',
  5: 'network lan wan man topology bus star ring mesh protocol tcp ip osi layer internet '
     'intranet extranet bandwidth modem multiplexer router gateway hub switch bridge '
     'network interface card coaxial twisted pair fibre optic wireless simplex duplex '
     'synchronous asynchronous email browser url isp',
  6: 'system development life cycle feasibility analysis design implementation maintenance '
     'prototyping jad rad outsourcing computer security virus worm trojan malware phishing '
     'firewall encryption backup disaster recovery cybercrime data protection forensics '
     'big data analytics visualisation ergonomics health',
 },
}

# ── explicit pins ─────────────────────────────────────────────────────────
# (diet, subject, part, question number) -> chapter
PIN = {}

# ── defects in the printed papers ─────────────────────────────────────────
FLAGS = {
 ('2024-09', 'FA', 'mcq', 16):
     'The printed answer key gives "Bonus" for this question, which is not one '
     'of the options — it appears to be a short-answer solution set in the wrong '
     'column. No official letter is available; the answer given here is worked '
     'from the study text. Verify with your tutor.',
}
