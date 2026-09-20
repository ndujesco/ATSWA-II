/* The four Part II subjects. Chapter content lives in data/<file>.js and is
   fetched the first time a subject is opened. */
var SUBJECTS = [
  { code: 'FA', file: 'fa', n: 16, name: 'Financial Accounting',
    blurb: 'From the accounting equation to company financial statements, cash flows and ratio analysis — the calculation-heavy core of Part II.' },
  { code: 'PS', file: 'ps', n: 23, name: 'Public Sector Accounting',
    blurb: 'Government accounting under IPSAS: the constitutional framework, budgeting, revenue, procurement and the statutory financial statements.' },
  { code: 'QA', file: 'qa', n: 20, name: 'Quantitative Analysis',
    blurb: 'Statistics, mathematics of finance, calculus and operations research — every method set out as worked mathematics.' },
  { code: 'IT', file: 'it', n: 6, name: 'Information Technology',
    blurb: 'Systems and data, hardware, software, processing, networks, and the development and security of information systems.' }
];

/* Standalone one-topic reference pages under guides/ — plain static HTML,
   not part of the hash-routed app, so linked with a real href rather than
   a #/ route. Add an entry here to have a new guide show up on the home
   page automatically. */
var GUIDES = [
  { tag: 'PS · Ch 9', href: 'guides/crf.html', title: 'The Consolidated Revenue Fund',
    blurb: 'Every source of CRF income, what it finances, the full warrant system, the Development and Contingency Funds, Ghana’s parallel system, and every past question on the topic.' },
  { tag: 'PS · Ch 2', href: 'guides/ipsas.html', title: 'IPSAS in this course',
    blurb: 'Every IPSAS the syllabus treats, indexed by number and by theme, with Nigeria’s own adoption timeline and exactly which chapter covers which standard.' },
  { tag: 'PS · Ch 14 & 16', href: 'guides/statements.html', title: 'Cash vs accrual statements',
    blurb: 'Every required financial statement, cash basis and accrual basis side by side, with worked-example checkpoints and every past question on the topic.' }
];
