CH = {
 'n': 2,
 't': 'The Conceptual Framework and the Structure of Financial Statements',
 'brief': 'The IASB Conceptual Framework in full: why it exists, who it is written for, the two '
          'fundamental and four enhancing qualities information must have, the five elements of '
          'financial statements and exactly when each is recognised, derecognised and measured, '
          'the concepts IAS 1 imposes on presentation (offsetting explained in the book\'s own '
          'words this time), the minimum shape of every primary statement, and IFRS 18 — the '
          'standard now replacing IAS 1 — set out with its three requirements actually all three '
          'of them, unlike the study text\'s own numbered list.',
 'outcomes': [
   'Explain the IASB Conceptual Framework for Financial Reporting: its status, purpose and objectives',
   'State the objective of general-purpose financial statements, and identify their primary users',
   'Distinguish the fundamental from the enhancing qualitative characteristics, and explain each',
   'Explain the reporting entity and why its structure matters',
   'Define the five elements of financial statements and apply the definitions',
   'Apply the recognition and derecognition criteria to a given item',
   'Identify the measurement bases and say when each is used',
   'Explain the two concepts of capital maintenance',
   'Identify the components of a complete set of financial statements under IAS 1',
   'Explain the characteristics of current assets and liabilities, and the minimum line items in '
   'the statement of financial position and the statement of profit or loss and OCI',
   'Explain the requirements of IFRS 18, all three of them, correctly numbered',
 ],
 'secs': [
  {'n': '2.1', 't': 'Status, purpose and objectives of the Framework', 'b': [
    {'p': 'Before anything else, it matters what the Conceptual Framework legally *is*. It '
          '**provides concepts and guidance that underpin the decisions the IASB makes** when it '
          'is developing a standard. Crucially, it is **not a standard itself** — it does not '
          'override any requirement of any actual IAS or IFRS. Where the Framework and a specific '
          'standard conflict, the standard wins; the Framework only fills the gaps a standard has '
          'not addressed, and explains the reasoning behind the standards that do exist.'},
    {'p': 'The Framework sets out four objectives for itself:'},
    {'ol': [
      'to **guide standard-setters** developing future standards and reviewing existing ones, so '
      'that there is a rational, principled basis for reducing the number of alternative '
      'treatments permitted in existing standards;',
      'to **guide preparers** in applying standards, and specifically in applying '
      '**principle-based rather than rule-based** approaches to matters the standards do not '
      'cover;',
      'to **assist auditors** in satisfying themselves that the financial statements they are '
      'auditing are in conformity with the Framework\'s principles;',
      'to **provide stakeholders** generally with the basis for interpreting the information '
      'contained in the financial statements.',
    ]},
    {'note': 'That second objective is worth sitting with: IFRS is deliberately **principle-based**, '
             'not a long list of rules for every possible situation. When a transaction is unusual '
             'and no standard addresses it directly, the preparer is expected to reason from the '
             'Framework\'s principles — the definitions of an asset and a liability, the '
             'qualitative characteristics — rather than search for a missing rule.'},
    {'h3': 'The objective of general-purpose financial statements'},
    {'p': 'The objective of general-purpose financial statements is to provide information about '
          'the **financial position**, the **performance**, and the **changes in financial '
          'position** of an entity. That single sentence is the seed from which the whole rest of '
          'the Framework, and most of this chapter, grows.'},
    {'h3': 'Who general-purpose financial statements are actually written for'},
    {'p': 'The **primary users** of general-purpose financial reporting are **present and '
          'potential investors, lenders, and other creditors**. This is a narrower group than "all '
          'users" (compare the fuller internal/external list in Chapter 1 §1.5) — and it is '
          'narrower for a specific reason: this group cannot demand special-purpose information '
          'directly from the entity, unlike management, so general-purpose statements exist '
          'precisely to meet *their* needs. They use financial statements to make decisions about:'},
    {'ul': [
      'buying, selling or holding equity or debt instruments;',
      'providing or settling loans or other forms of credit;',
      'exercising rights to vote on, or otherwise influence, management\'s actions that affect '
      'the use of the entity\'s resources.',
    ]},
    {'h3': 'Economic resources and claims to the resources'},
    {'p': 'A reporting entity\'s economic resources, and the claims against them, are reported in '
          'the **statement of financial position**. Information about their nature and amounts '
          'helps users to:'},
    {'ul': [
      'assess the entity\'s **financial strengths and weaknesses**;',
      'assess its **liquidity and solvency**, and its need for, and ability to obtain, financing;',
      'predict how future cash flows will be **distributed among those with a claim** on the '
      'entity.',
    ]},
    {'h3': 'Changes in economic resources and claims — and which statement shows which change'},
    {'p': 'Changes to economic resources and claims arise for two different reasons, and the '
          'Framework routes each kind of change to a different statement — a mapping worth '
          'learning cold, because it explains *why* there are four primary statements rather than '
          'just one:'},
    {'table': {'head': ['Kind of change', 'Reported in'], 'align': 'll', 'rows': [
      ['Changes resulting from **financial performance**',
       'The statement of comprehensive income (statement of profit or loss and OCI)'],
      ['Changes **not** resulting from financial performance (e.g. issuing shares)',
       'The statement of changes in equity'],
      ['Financial performance reflected by **past cash flows**',
       'The statement of cash flows'],
    ]}},
    {'note': 'Information about an entity\'s financial performance during a period is useful for '
             'assessing the entity\'s past and future ability to generate net cash inflows — '
             'performance and cash generation are related ideas, but the Framework is careful to '
             'keep them as two separate things reported in two separate places.'},
  ]},

  {'n': '2.2', 't': 'Users of financial statements and their information needs', 'b': [
    {'p': 'Beyond the primary users named above, the Framework separately discusses users more '
          'broadly, and the study text repeats — almost word for word — the internal/external '
          'split you already met in Chapter 1 §1.5. It is worth transcribing here too, because '
          'this is the version tied specifically to the Framework\'s own language about *why* each '
          'user needs what they need.'},
    {'p': '**Internal users** are people within the business organisation who use financial '
          'information: owners, managers and employees. **External users** are people outside the '
          'organisation: suppliers, banks, customers, investors, potential investors and tax '
          'authorities.'},
    {'table': {'head': ['Primary user', 'What they are concerned with'], 'align': 'll', 'rows': [
      ['**Investors**', 'They supply risk capital in the form of funding, so this group is '
       'concerned with the risk inherent in, and the return provided by, their investments'],
      ['**Lenders**', 'Want information that will let them decide whether their loans will be '
       'paid when due, and whether or not to issue new loans to the entity'],
      ['**Suppliers and trade creditors**', 'Interested in information that helps them determine '
       'whether amounts owing to them will be paid on time'],
      ['**Customers**', 'Interested in the continuance of the entity, especially where they '
       'themselves depend on it'],
      ['**Employees**', 'Want to know about the stability and profitability of their employers — '
       'this gives them confidence about their jobs and informs discussions about salary and '
       'conditions of employment'],
      ['**Government and government agencies**', 'Interested in the allocation of resources and '
       'the activities of entities generally'],
      ['**The general public and financial analysts**', 'Interested in how an entity may '
       'contribute to the local economy, which will affect purchasing power'],
    ]}},
    {'key': 'Investor information has **relevance** precisely when it influences the economic '
            'decisions of users — by helping them evaluate past, present or future events, or by '
            'confirming (or correcting) their earlier evaluations. This one sentence is the bridge '
            'into the qualitative characteristics that follow.'},
  ]},

  {'n': '2.3', 't': 'The qualitative characteristics', 'b': [
    {'p': 'Two are **fundamental**: information that lacks either one is simply not useful, '
          'however well it scores on everything else. Four are **enhancing**: they make already '
          'useful information more useful, but on their own cannot rescue information that is '
          'irrelevant or unfaithful — a beautifully clear, perfectly comparable, instantly '
          'available number that measures the wrong thing is still worthless.'},
    {'table': {'head': ['Fundamental', 'Enhancing'], 'align': 'll', 'rows': [
      ['Relevance', 'Comparability'],
      ['Faithful representation', 'Understandability'],
      ['', 'Verifiability'],
      ['', 'Timeliness'],
    ]}},
    {'h3': 'Relevance'},
    {'p': 'To be useful, information must be **relevant** to the decision-making needs of users. '
          'Information has the quality of relevance if it can be used for **predictive** and '
          '**confirmatory** purposes: it has **predictive value** if it can help users evaluate '
          'present or future events, and **confirmatory value** if it helps users confirm the '
          'assessments and predictions they made in the past, or correct their past evaluations. '
          'The relevance of information is affected by its **materiality** — information is '
          'material if its omission or misstatement could influence the economic decisions users '
          'make on the basis of the financial statements.'},
    {'h3': 'Faithful representation'},
    {'p': 'To be useful, information must also **faithfully represent** what it either purports to '
          'represent, or could reasonably be expected to represent. A perfectly faithful '
          'representation would have three characteristics at once:'},
    {'ul': [
      '**Complete** — the financial statement includes all information necessary for a user to '
      'understand the phenomenon being depicted, including all necessary descriptions and '
      'explanations;',
      '**Neutral** — the depiction is without bias in the selection or presentation of financial '
      'information; and',
      '**Free from error** — there is no error or omission in the description of the phenomenon, '
      'and the process used to produce the information has been selected and applied with no '
      'errors.',
    ]},
    {'p': 'Another key element of faithful representation is **substance over form** (see also '
          'Chapter 1 §1.6). A **neutral** depiction is, in turn, supported by the exercise of '
          '**prudence**: caution in preparing financial statements, by making reasonable '
          'allowances so as not to overstate assets or income, or understate expenses or '
          'liabilities. The value of an asset is written down when the amount expected to be '
          'realised from its sale or continued use is less than its carrying amount; accounting '
          'standards usually prescribe exactly how to write assets down in such circumstances.'},
    {'h3': 'Comparability'},
    {'p': 'Users must be able to compare an entity\'s financial statements through time, to '
          'identify trends in its financial position and performance. They must also be able to '
          'compare the financial statements of *different* entities, to evaluate their relative '
          'financial position, performance and changes in financial position. This means the '
          'measurement and display of the financial effect of like transactions and other events '
          'must be carried out **consistently**, both within one entity over time and across '
          'different entities.'},
    {'h3': 'Verifiability'},
    {'p': 'When information can be verified, this gives assurance that it faithfully represents '
          'the economic phenomena it claims to represent. For information to be verifiable, '
          'different knowledgeable and independent parties would need to be able to reach '
          'consensus — although not necessarily complete agreement — that a particular depiction '
          'is a faithful representation.'},
    {'h3': 'Understandability'},
    {'p': 'Users must be able to understand the financial statements. They are assumed to have a '
          'reasonable knowledge of business and economic activities and of accounting, together '
          'with a willingness to study the information with reasonable diligence. Complex matters '
          'must not be left out of the financial statements simply because they are difficult to '
          'understand, if they are relevant to a decision.'},
    {'h3': 'Timeliness'},
    {'p': 'Timeliness refers to having information available in time to influence the decisions '
          'users make. Users need reliable, relevant and timely information to react to changes in '
          'an entity\'s financial position or performance and make informed decisions on the basis '
          'of current information — the longer the gap between the financial report and the '
          'financial year end, the more negative the effect on the timeliness of the information. '
          'Timing can pose a real challenge to faithful representation, because it may be '
          'difficult to accurately measure certain transactions or events by the reporting date. '
          'The constraint of timeliness often forces management to make estimates and judgements '
          'in financial reporting — and these estimates and judgements must still be made '
          'consistently with the Framework and the relevant IFRS Standards, so that the statements '
          'remain a faithful representation of the entity\'s position and performance even under '
          'time pressure. Balancing timeliness against accuracy in this way is central to keeping '
          'financial information both reliable and useful.'},
    {'key': 'Enhancing characteristics can only make useful information more useful. They **cannot '
            'make irrelevant or unfaithfully represented information useful** — comparability, '
            'verifiability, timeliness and understandability are all worthless applied to a number '
            'that measures the wrong thing or misrepresents it.'},
    {'h3': 'The cost constraint'},
    {'p': 'The benefit of reporting information must exceed the cost of providing it. This is the '
          'only **pervasive constraint** recognised by the Framework, and it is the reason '
          'disclosure requirements differ between a large listed company and a small private one.'},
    {'eg': {'t': 'Which characteristic is at stake?', 'q': [
      {'p': 'A company delays publishing its statements by eight months while it perfects the '
            'valuation of an investment property. Identify the trade-off being made.'}],
      'a': [
      {'p': '**Timeliness against faithful representation.** A more precisely measured figure is '
            'a more faithful one, but information that arrives after the decision has been taken '
            'has no relevance at all.'},
      {'p': 'The Framework acknowledges this trade-off explicitly: enhancing characteristics may '
            'have to be balanced against one another, and none of them can be maximised in '
            'isolation. Eight months is almost certainly too long — CAMA itself sets filing '
            'deadlines precisely to stop the trade-off being resolved this way.'}]}},
  ]},

  {'n': '2.4', 't': 'The reporting entity', 'b': [
    {'p': 'The **reporting entity** is the business or organisation for which financial statements '
          'are prepared. It can take one of three forms, and the study text names all three:'},
    {'ol': [
      '**Single company** — one entity that prepares its own financial statements.',
      '**Group of companies** — a parent company and its subsidiaries, together preparing '
      '**consolidated** financial statements.',
      '**Segment reporting** — a company reports financial information for specific business '
      'segments within itself.',
    ]},
    {'p': 'The structure of the reporting entity is significant for several reasons: it '
          'determines the **structure of the financial statements** themselves (a single company\'s '
          'own statements, a parent-and-subsidiary consolidation, or a component such as a '
          'division or segment reporting separately); analysts need to understand this structure '
          'to accurately analyse the statements; and stakeholders use the statements to make '
          'decisions that the reporting entity structure can materially affect. In practice, the '
          'reporting entity\'s structure decides two further things: **which accounting policies '
          'and procedures apply** to its transactions and events, and **the level of disclosure '
          'required** in the financial statements.'},
  ]},

  {'n': '2.5', 't': 'The elements of financial statements', 'b': [
    {'p': 'Transactions and other events are grouped together into broad classes, and it is these '
          'broad classes — the **five elements** of financial statements — through which their '
          'financial effects are shown. The 2018 Framework rewrote the asset and liability '
          'definitions in particular; learn the current wording exactly.'},
    {'def': {'t': 'Asset', 'd': 'a **present economic resource controlled** by the entity **as a '
                  'result of past events**. An economic resource is a right that has the '
                  'potential to produce economic benefits.'}},
    {'p': 'The potential economic benefits **need not** be expected to flow to the entity with '
          'certainty, or even be considered most likely — a low probability of an inflow may '
          'affect *whether* recognising the item gives useful information (see Recognition, '
          'below), but it does not, by itself, stop the item from meeting the definition of an '
          'asset. The rights that can constitute an economic resource include:'},
    {'ol': [
      'rights to receive cash;',
      'rights to receive goods and services;',
      'rights to exchange economic resources on favourable terms;',
      'rights to use intellectual property; and',
      'rights to benefit from the use of physical objects — such as under a lease of property, '
      'plant and equipment.',
    ]},
    {'key': 'The existence of an asset, particularly the question of **control**, does **not** '
            'depend on physical form. A right can be an asset without the entity ever holding the '
            'underlying physical thing.'},
    {'def': {'t': 'Liability', 'd': 'a **present obligation** of the entity to transfer an '
                  'economic resource **as a result of past events**.'}},
    {'p': 'An obligation is a **duty or responsibility that the entity has no practical ability to '
          'avoid**. Note precisely what the liability itself is: it is the obligation *to transfer* '
          'an economic resource — not the ultimate outflow of economic benefits itself. Obligations '
          'may be **legally enforceable**, as a consequence of a binding contract or a statutory '
          'requirement, or they may be **constructive obligations**, arising from an entity\'s own '
          'established pattern of past practice that others have come to rely on.'},
    {'def': {'t': 'Equity', 'd': 'the **residual interest** in the assets of the entity after '
                  'deducting all its liabilities.'}},
    {'p': 'Equity comprises amounts that arise from owners\' contributions, and amounts that arise '
          'from increases in income. It is calculated as total assets less total liabilities, or, '
          'equivalently, as share capital plus all reserves. Examples of equity include share '
          'capital, share premium, revaluation reserves, and retained earnings. Equity interest '
          'confers on its holders the right to receive dividends, and the right to proceeds from '
          'satisfying the equity claims — either in full on liquidation, or in part at other '
          'times.'},
    {'def': {'t': 'Income', 'd': 'increases in assets, or decreases in liabilities, that result '
                  'in increases in equity, **other than** contributions from holders of equity claims.'}},
    {'p': 'Income encompasses both **revenue** and **gains**. Revenue arises in the course of the '
          'ordinary activities of an entity and is referred to by a variety of names, including '
          'sales, fees, interest, dividends, royalties and rent. **Gains** represent other items '
          'that meet the definition of income and may, or may not, arise in the course of an '
          'entity\'s ordinary activities — for instance, where a non-current asset is sold above '
          'its carrying amount, the difference is a gain. Contributions from owners in their '
          'capacity as owners — such as the issue of equity shares — are, by definition, not '
          'income.'},
    {'def': {'t': 'Expenses', 'd': 'decreases in assets, or increases in liabilities, that result '
                  'in decreases in equity, **other than** distributions to holders of equity claims.'}},
    {'p': 'Expenses encompass **losses** as well as those expenses that arise in the ordinary '
          'course of the entity\'s activities. Expenses arising in the ordinary course of activity '
          'include, for example, cost of sales, salaries and wages, rent, and depreciation. '
          '**Losses** represent other items meeting the definition of expenses and may, or may '
          'not, arise in the ordinary course of activity — examples are a loss on disposal of a '
          'non-current asset, and an impairment loss on an asset. Distributions to owners in their '
          'capacity as owners — dividends paid to shareholders — are, by definition, not expenses.'},
    {'warn': 'The three phrases that carry the marks in this section are **control** (not '
             'ownership), **past event** (not intention), and **present obligation** (not future '
             'plan). A signed intention to buy machinery next year creates neither an asset nor a '
             'liability, because there has been no past event yet.'},
    {'eg': {'t': 'Asset or not?', 'q': [
      {'ol': [
        'A delivery van held on a five-year lease, with the entity directing its use.',
        'A staff training course costing ₦2m, completed last month.',
        'An order received from a customer for goods to be delivered next quarter.',
        'A machine bought for ₦8m that has broken down and cannot be repaired or sold.',
      ]}],
      'a': [{'ol': [
        '**Asset.** The entity controls the right to use the van for five years as a result of a '
        'past event (signing the lease). IFRS 16 recognises a right-of-use asset. Legal ownership '
        'is irrelevant — control is the test.',
        '**Not an asset.** The entity cannot control the trained staff, who may leave. The cost '
        'is expensed as incurred.',
        '**Neither asset nor liability.** Nothing has happened yet: this is an executory contract '
        'and neither party has performed. Revenue is recognised on delivery.',
        '**Not an asset any longer.** It no longer has the potential to produce economic '
        'benefits, so it is derecognised and the carrying amount written off as an impairment loss.',
      ]}]}},
    {'h3': 'Recognition'},
    {'p': '**Recognition** is the process of incorporating, into the statement of financial '
          'position or the income statement, an item that meets the definition of one of the five '
          'elements and satisfies two general criteria: it is **probable** that any future '
          'economic benefit associated with the item will flow to or from the entity, and the '
          'item\'s **cost or value can be measured reliably**. Applying these general criteria to '
          'each element in turn:'},
    {'ul': [
      'an **asset** is recognised in the statement of financial position when it is probable that '
      'future economic benefits will flow to the entity and the asset has a cost or value that '
      'can be measured reliably;',
      'a **liability** is recognised when it is probable that an outflow of resources embodying '
      'economic benefits will result from the settlement of a present obligation, and the amount '
      'at which the settlement will take place can be measured reliably;',
      '**income** is recognised in the income statement when an increase in future economic '
      'benefits related to an increase in an asset, or a decrease in a liability, has arisen and '
      'can be measured reliably — recognition of income therefore occurs simultaneously with the '
      'recognition of the increase in assets or the decrease in liabilities;',
      '**expenses** are recognised when a decrease in future economic benefits related to a '
      'decrease in an asset, or an increase in a liability, has arisen and can be measured '
      'reliably — recognition of expenses therefore occurs simultaneously with the recognition of '
      'an increase in liabilities or a decrease in assets (for example, accruing an employee '
      'entitlement, or depreciating equipment).',
    ]},
    {'h3': 'Derecognition'},
    {'p': '**Derecognition** occurs when an item is removed from the financial statements as an '
          'asset, a liability, or a component of equity. This should happen when the item no '
          'longer meets any one of the recognition criteria above. Derecognition often involves the '
          'transfer of the risks and rewards associated with the asset or liability in question. '
          'The key principles:'},
    {'ul': [
      'an **asset** is derecognised when the entity **loses control** over it — this occurs when '
      'the entity no longer has the ability to direct the use of the asset and obtain benefits '
      'from it;',
      'a **liability** is derecognised when the obligation is **discharged, cancelled or expires**.',
    ]},
    {'eg': {'t': 'Recognition and derecognition, worked through', 'q': [
      {'p': 'Entity A purchases a piece of equipment for ₦10,000,000. Walk through why this is '
            'recognised as an asset, and what would cause it to be derecognised.'}],
      'a': [
      {'p': '**Recognition.** The equipment meets the **definition** of an asset (a present '
            'economic resource, controlled as a result of the purchase, with the potential to '
            'produce economic benefits). It is **measurable**: its cost of ₦10,000,000 is known '
            'with certainty. And it can be **faithfully represented** — the cost figure accurately '
            'reflects the economic phenomenon (an asset acquired for that price). All three '
            'conditions are satisfied, so it is recognised.'},
      {'p': '**Derecognition.** If Entity A later sells the equipment, it would be derecognised: '
            'it is no longer an asset **of Entity A**, because Entity A no longer controls it or '
            'has the ability to direct its use and obtain benefits from it. The recognition '
            'criteria are no longer met, so the item comes off the statement of financial '
            'position.'}]}},
    {'h3': 'Measurement'},
    {'p': '**Measurement** relates to the basis on which the elements of financial statements will '
          'actually be included in the financial statements. Selecting a measurement basis must '
          'take into account the fundamental qualitative characteristics — relevance and faithful '
          'representation — together with measurement uncertainty and the cost constraint. The '
          'Framework discusses the following bases:'},
    {'table': {'head': ['Basis', 'What it measures', 'Notes'], 'align': 'lll', 'rows': [
      ['**Historical cost**', 'The cost at which transactions and other events are actually '
       'acquired', 'Non-financial assets held at historical cost are adjusted over time to reflect '
       'usage — through depreciation and amortisation — or, where the carrying amount exceeds the '
       'recoverable amount, an impairment loss is written off. Financial assets held at historical '
       'cost reflect subsequent changes such as interest and payments through the process of '
       'amortised cost.'],
      ['**Fair value**', 'The price at which items are exchanged in an orderly transaction between '
       'market participants', 'Market-based, at the measurement date'],
      ['**Current cost**', 'The value at which the entity would acquire the asset, or transfer '
       'the liability, at the current market price', 'Assets are carried at the amount required '
       'to acquire them currently; liabilities are carried at the undiscounted amount currently '
       'required to repay them'],
      ['**Value in use**', 'The present value of cash flows an entity expects to derive from the '
       'continuing use of an asset and its ultimate disposal', 'Entity-specific and forward-'
       'looking; used in impairment testing'],
    ]}},
    {'h3': 'Presentation and disclosure'},
    {'p': 'A reporting entity communicates information about its assets, liabilities, equity, '
          'income and expenses by presenting and disclosing information in its financial '
          'statements. Presentation and disclosure relate to three things:'},
    {'ol': [
      'determining **where** an item should be presented in the financial statements;',
      '**sorting** assets, liabilities, equity, income or expenses on the basis of shared '
      'characteristics; and',
      '**adding together** (aggregating) assets, liabilities, equity, income or expenses that '
      'share those characteristics.',
    ]},
    {'h3': 'Capital maintenance'},
    {'p': 'Concepts of capital maintenance matter because **only income earned in excess of the '
          'amount needed to maintain capital may be regarded as profit**. The Framework discusses '
          'two capital maintenance concepts:'},
    {'ul': [
      '**Financial capital maintenance** — a profit is earned only if the financial (nominal) '
      'amount of net assets at the end of the period exceeds the financial (nominal) amount of '
      'net assets at the beginning of the period, after excluding any distributions to, and '
      'contributions from, owners during the period. This is the conventional basis, and the one '
      'used throughout the rest of this study text.',
      '**Physical capital maintenance** — a profit is earned only if the physical productive '
      'capacity (or operating capacity) of the entity — or the resources or funds needed to '
      'achieve that capacity — at the end of the period exceeds the physical productive capacity '
      'at the beginning of the period. This basis requires current-cost measurement, since it is '
      'concerned with maintaining *capacity to produce*, not merely a nominal money amount.',
    ]},
    {'eg': {'t': 'Financial capital maintenance', 'q': [
      {'p': 'A business begins the year with net assets of ₦4,200,000. During the year the owner '
            'introduced ₦600,000 of new capital and withdrew ₦350,000. Closing net assets are '
            '₦5,150,000. Compute the profit for the year.'}],
      'a': [
      {'p': 'Under financial capital maintenance, profit is the movement in net assets stripped '
            'of transactions with the owner:'},
      {'tex': '\\text{Profit} = (\\text{Closing NA} - \\text{Opening NA}) + \\text{Drawings} - '
              '\\text{Capital introduced}'},
      {'stmt': {'t': 'Computation of profit', 'rows': [
        ['Closing net assets', 5150000],
        ['Opening net assets', -4200000],
        ['Increase in net assets', 950000, '@t'],
        '@gap',
        ['Add back drawings', 350000],
        ['Less capital introduced', -600000],
        ['Profit for the year', 700000, '@tt'],
      ]}},
      {'note': 'The logic never changes: drawings reduced net assets but were not a loss, so add '
               'them back; capital increased net assets but was not profit, so take it out. This '
               'same computation reappears in Chapter 6 as the capital comparison method for '
               'incomplete records.'}]}},
  ]},

  {'n': '2.6', 't': 'IAS 1\'s other accounting concepts (here in full, and in order)', 'b': [
    {'warn': 'The study text lists these concepts under a numbering scheme of its own (i, ii, '
             'iii, then a jump straight to v, then vi, then ix appears **before** vii and viii). '
             'There is no "iv" anywhere in the source, and "ix" (accruals) is printed out of '
             'sequence, ahead of prudence and substance over form. This is a defect in the '
             'original document, not a hidden fourth concept you have missed — the study text '
             'simply never labels a concept "iv," and the numbering restarts oddly around '
             'accruals. Below, all eight named concepts are given **in a sensible reading order**, '
             'with the source\'s own roman numeral kept alongside each one so you can still match '
             'it back to the book if you are cross-referencing.'},
    {'ul': [
      '**(i) Going concern** — IAS 1 assumes an entity is a going concern. An entity is '
      'considered a going concern if it is capable of earning a reasonable net income, and there '
      'is no intention or threat, from any source, to significantly curtail its line of business '
      'in the near future. The going concern assumption is critical because it affects how assets '
      'and liabilities are valued: an entity that is not considered a going concern may need to '
      'value its assets at liquidation values instead, which can significantly change its reported '
      'financial position — this is exactly the break-up basis introduced in Chapter 1 §1.6. '
      'Entities must assess their ability to continue as a going concern and disclose any material '
      'uncertainties that may affect their future operations.',
      '**(ii) Consistency of presentation** — IAS 1 requires entities to maintain consistency in '
      'the presentation and classification of items in the financial statements from one period '
      'to another. Once an entity selects an accounting policy, it should continue to use that '
      'policy in subsequent periods. Consistency of presentation enables users to compare an '
      'entity\'s financial performance and position over time, identifying trends and patterns, '
      'and it helps entities avoid arbitrary changes in accounting policies or presentation that '
      'would harm comparability.',
      '**(iii) Fair presentation** — IAS 1 requires financial statements to present fairly the '
      'financial position, financial performance and cash flows of an entity: the information '
      'presented must be complete, neutral and free from error. Fair presentation is critical '
      'because it enables users to trust the financial information presented and make informed '
      'decisions on the strength of it. Entities must ensure their financial statements are '
      'transparent, complete and free from material errors, and must provide additional '
      'disclosures whenever necessary for users to understand what the statements are showing.',
      '**(v) Materiality and aggregation** — IAS 1 requires financial statements to present '
      'fairly the financial position, performance and cash flows of an entity, and materiality '
      'and aggregation are essential to that objective. **Materiality** is the threshold at which '
      'information becomes relevant and influential to users\' decisions — information is material '
      'if its omission from, or misstatement in, the financial statements could influence the '
      'economic decisions of users. **Aggregation** is the process of combining similar items to '
      'present a comprehensive picture. The two work together because they can enable entities to '
      'focus users on relevant information and avoid burying it in unnecessary detail — but '
      'entities must ensure that aggregating similar items never obscures information that is, on '
      'its own, material, since that would lead users to make incorrect decisions.',
      '**(vi) Offsetting** — covered in full below, because it is the one candidates most often '
      'get wrong.',
      '**(ix, out of sequence in the source — accruals)** — IAS 1 requires entities to prepare '
      'financial statements using the accrual basis of accounting, described fully in Chapter 1 '
      '§1.6: revenue and expenses are recognised when earned or incurred, regardless of when cash '
      'is received or paid. Accrual accounting provides a more accurate picture of an entity\'s '
      'financial performance because it matches revenues with the expenses incurred to generate '
      'them; it also enables entities to recognise liabilities and assets that would not otherwise '
      'be visible from cash flows alone.',
      '**(vii) Prudence** — IAS 1 requires entities to exercise prudence in preparing financial '
      'statements, involving a degree of caution in making judgements and estimates. Prudence is '
      'essential because it helps entities avoid overstating assets or revenues and understating '
      'liabilities or expenses; it enables entities to account for uncertainties and risks in a '
      'way that reflects their true potential impact on the financial statements — it is caution '
      'under genuine uncertainty, never deliberate understatement (see Chapter 1 §1.6 again for '
      'why deliberate understatement is itself a breach of neutral reporting).',
      '**(viii) Substance over form** — IAS 1 requires entities to account for transactions and '
      'events in accordance with their substance and economic reality, rather than merely their '
      'legal form. This is critical because it ensures financial statements reflect the underlying '
      'economic reality of transactions and events; by accounting for transactions based on their '
      'substance, entities give users a more accurate picture of their financial performance and '
      'position, and help them understand the true drivers behind the reported results.',
    ]},
    {'h3': 'Offsetting, in the study text\'s own words'},
    {'p': '**IAS 1 prohibits offsetting assets and liabilities, or revenues and expenses, unless '
          'required or permitted by a Standard or Interpretation.** Offsetting can distort the '
          'financial position and performance of an entity, making it difficult for users to '
          'understand the underlying financial transactions — by prohibiting it, IAS 1 ensures '
          'entities present a transparent and faithful representation of their financial '
          'transactions. Entities must carefully assess their transactions and ensure they do not '
          'offset assets and liabilities, or revenues and expenses, unless offsetting is expressly '
          'permitted by the specific standard. However, **if the specified criteria in the '
          'relevant standard are met, offsetting is mandatory**, not merely optional.'},
    {'p': 'Offsetting is permitted only where **both** of the following criteria are satisfied:'},
    {'ul': [
      'the entity currently has a **legally enforceable right** to offset the recognised amounts;',
      'the entity **intends** either to settle on a net basis, or to realise the asset and settle '
      'the liability simultaneously.',
    ]},
    {'p': 'Additionally, where an entity does offset in accordance with these requirements, '
          'disclosure of additional quantitative information about the gross amounts is still '
          'required by the relevant standard.'},
    {'warn': 'Not all net presentation of items counts as offsetting. The study text specifically '
             'says the following are **not** offsetting: presenting property, plant and equipment '
             '(PP&E) and intangible assets **net of accumulated depreciation and amortisation**; '
             '**provisions against inventory**; or measuring receivables **net of an expected '
             'credit loss** or allowance for doubtful receivables. These are all ordinary '
             'measurement of a single asset, not the netting of an asset against a liability.'},
    {'p': 'The following are specific examples where offsetting is genuinely permitted:'},
    {'ul': [
      'gains or losses on disposal of non-current assets; and',
      'gains or losses arising from a group of similar transactions — such as gains or losses '
      'arising from foreign exchange transactions.',
    ]},
    {'note': 'See Chapter 1 §1.6 for a worked "is this offsetting?" example applying this exact '
             'two-part test to three scenarios, if you have not already worked through it there.'},
  ]},

  {'n': '2.7', 't': 'The components of a complete set of financial statements', 'b': [
    {'p': 'A full set of financial statements under IAS 1 includes:'},
    {'ol': [
      'A **statement of profit or loss and other comprehensive income**, or a statement of profit '
      'or loss followed by a statement of other comprehensive income;',
      'A **statement of financial position**;',
      'A **statement of changes in equity**;',
      'A **statement of cash flows**; and',
      '**Notes to the financial statements** — not examinable in this syllabus, but part of a '
      'complete set nonetheless.',
    ]},
    {'h3': 'The statement of financial position'},
    {'p': 'The statement of financial position is a structured presentation of an entity\'s assets '
          'and liabilities. The difference between assets and liabilities is capital (equity). '
          'Assets are resources controlled by the business; liabilities are amounts owed by the '
          'business. **IAS 1 requires entities to present current and non-current assets and '
          'liabilities separately** on the face of the statement.'},
    {'p': 'Current assets and current liabilities each share four defining characteristics:'},
    {'table': {'head': ['Current assets — expected to be...', 'Current liabilities — expected '
     'to be...'], 'align': 'll', 'rows': [
      ['realised or consumed within the entity\'s normal operating cycle',
       'settled within the entity\'s normal operating cycle'],
      ['held primarily for trading purposes', 'held primarily for trading purposes'],
      ['realised within 12 months of the reporting date',
       'due to be settled within 12 months of the reporting date'],
      ['cash or a cash equivalent, unless restricted',
       'subject to no unconditional right to defer settlement for at least 12 months after the '
       'reporting date'],
    ]}},
    {'p': 'Examples of current assets include inventories, trade and other receivables, and cash '
          'and cash equivalents. Examples of current liabilities include trade and other payables '
          'and current tax liabilities.'},
    {'h3': 'The minimum line items in the statement of financial position'},
    {'table': {'head': ['Assets', 'Liabilities and equity'], 'align': 'll', 'rows': [
      ['Property, plant and equipment', 'Trade and other payables'],
      ['Investment property', 'Provisions'],
      ['Intangible assets', 'Financial liabilities'],
      ['Financial assets', 'Liabilities included in disposal groups classified as held for sale'],
      ['Investments accounted for using the equity method', 'Current tax liabilities and assets'],
      ['Biological assets', 'Deferred tax liabilities and assets'],
      ['Inventories', 'Issued capital and reserves'],
      ['Trade and other receivables', 'Non-controlling interest'],
      ['Cash and cash equivalents', ''],
      ['Assets classified as held for sale', ''],
    ]}},
    {'h3': 'The statement of profit or loss'},
    {'p': 'This statement provides information about the performance of an entity in a period. It '
          'consists of two parts: a **statement of profit or loss** — a list of income and '
          'expenses that results in a profit or loss for the period; and a **statement of other '
          'comprehensive income** — a list of other gains and losses that have arisen in the '
          'period. Note that, at this level, the statement of other comprehensive income will '
          'include only the **gain on revaluation of non-current assets**. It shows the '
          'performance of the business in terms of its main activities: it is a structured '
          'presentation of all revenue, other income earned in a period, and the costs of earning '
          'those revenues.'},
    {'h3': 'The minimum line items in the statement of profit or loss and OCI'},
    {'p': '**Statement of profit or loss:**'},
    {'ul': [
      'Revenue', 'Cost of sales', 'Gross profit', 'Other income', 'Distribution costs',
      'Administrative expenses', 'Other expenses', 'Finance costs',
      'Share of profit/(loss) of associates and joint ventures', 'Profit/(loss) before tax',
      'Income tax expense', 'Profit/(loss) for the period',
    ]},
    {'p': '**Other comprehensive income:**'},
    {'ul': ['Revaluation gain on non-current assets']},
    {'p': '**Total comprehensive income** is simply: profit/(loss) for the period **plus** other '
          'comprehensive income.'},
    {'h3': 'The structure of the statement of changes in equity'},
    {'ul': [
      'Total comprehensive income, showing separately the amount attributable to the equity '
      'owners of the parent, and the amount attributable to the non-controlling interest group;',
      'The effect of retrospective application of changes in accounting policies, and of prior '
      'period errors;',
      'Amounts recorded separately for the changes arising from: profit or loss; other '
      'comprehensive income; distributions to owners as dividends; and contributions from owners '
      'in the form of the issue of additional shares;',
      'A reconciliation of the amount of equity at the beginning and at the end of the period.',
    ]},
  ]},

  {'n': '2.8', 't': 'IFRS 18 — Presentation and Disclosure in Financial Statements', 'b': [
    {'p': 'In **January 2024**, the IASB introduced **IFRS 18 Presentation and Disclosure in '
          'Financial Statements**, a major update that **replaces IAS 1**. Its objectives are to '
          'provide relevant information about an entity\'s assets, liabilities, equity, income '
          'and expenses, and to set out the general requirements for financial statements. '
          'Overall, IFRS 18 aims to **standardise the structure of the income statement, enhance '
          'the comparability of financial data, and improve disclosure requirements** so that '
          'published statements better reflect a company\'s actual financial performance.'},
    {'warn': 'The study text\'s own sentence reads: **"IFRS 18 introduces three sets of '
             'requirements to achieve these goals. The three requirements are: 1) ... 2) ..."** '
             'and then it simply moves on to a new section header (§2.13, "Aggregation or '
             'disaggregation") without ever writing "3)" — leaving the reader to work out for '
             'themselves that aggregation/disaggregation *is* the third requirement. It is. All '
             'three are set out explicitly, and in full, below.'},
    {'h3': 'Requirement 1 — two new defined subtotals in the statement of profit or loss'},
    {'p': 'IFRS 18 requires companies to report two new **defined subtotals**:'},
    {'ul': ['**Operating profit**; and', '**Profit before financing and income taxes**.']},
    {'p': 'These subtotals provide a consistent structure for the statement of profit or loss, '
          'thereby improving comparability between companies — though the requirement does **not** '
          'change how a company measures its financial performance, nor the overall profit figure '
          'it arrives at. It is purely a presentation requirement: it standardises where the '
          'subtotal lines sit and what they must include, not the underlying arithmetic.'},
    {'h3': 'Requirement 2 — disclosure of management-defined performance measures (MPMs)'},
    {'p': 'IFRS 18 requires companies to disclose **reconciliations** between their '
          'management-defined performance measures and the totals or subtotals listed in IFRS 18 '
          'or required by IFRS Accounting Standards more generally. Entities must now disclose '
          'unusual income or expenses, and explain why they are not expected to recur, together '
          'with the judgements applied in classification and any subtotals presented that are not '
          'required by IFRS.'},
    {'def': {'t': 'Management-defined performance measures (MPMs)', 'd': 'subtotals of income and '
                  'expenses used in public communications to communicate management\'s view of an '
                  'aspect of the company\'s financial performance as a whole.'}},
    {'p': '"Public communications" here includes management commentary, press releases and '
          'investor presentations, but **excludes** oral communications, written transcripts of '
          'oral communications, and social media posts. The official publication containing an MPM '
          'must explicitly point out that the measure is a management performance measure. MPMs '
          'are, by definition, **not** the common income and expense items already listed '
          'elsewhere in IFRS 18 — they are the company\'s own, additional lens on performance '
          '(think EBITDA, or an "adjusted" profit figure). Investors use MPMs to get insight into '
          'how management views the company\'s financial performance, how the company is being '
          'managed, and how its financial performance is developing over time — but precisely '
          'because these measures are chosen by management rather than defined by a standard, IFRS '
          '18 requires them to be reconciled back to an official IFRS subtotal, so a reader can see '
          'exactly what has been added or removed to get from one figure to the other.'},
    {'h3': 'Requirement 3 — aggregation or disaggregation'},
    {'p': 'Companies are required to **aggregate or disaggregate** items to present line items in '
          'the primary financial statements in a way that provides a useful, structured summary. '
          'Furthermore, in the notes to the financial statements, companies are required to '
          'aggregate or disaggregate items to provide material information — but, in doing so, '
          'must **not obscure material information**. This is the same aggregation/disaggregation '
          'discipline already met as one of the "other accounting concepts" in §2.6 above, now '
          'applied specifically within the IFRS 18 presentation requirements.'},
    {'h3': 'Classifying income and expenses: the five categories'},
    {'p': 'IFRS 18 requires a company to classify income and expenses into categories in the '
          'statement of profit or loss, and to present the two new defined subtotals. Specifically, '
          'the standard requires entities to present subtotals for:'},
    {'ul': [
      '**Profit or loss before financing activities and income tax**; and',
      '**Profit or loss resulting from all income and expenses** — i.e. the overall total.',
    ]},
    {'note': 'There is **no** requirement to present sub-totals for the investing category or the '
             'financing category on their own — unlike the statement of cash flows, which does '
             'subtotal each of its categories.'},
    {'h3': 'Nature of expenses versus function of expenses'},
    {'p': 'The standard permits expenses to be presented **by nature** or **by function**. '
          '**Nature of expenses** means classification by the economic resource consumed to '
          'accomplish the company\'s activities — for example, raw materials, labour, lighting and '
          'heating, salaries, advertising cost. **Function of expenses** means classification by '
          'the activity to which the consumed resource relates — for example, cost of sales, '
          'distribution costs, administrative expenses.'},
    {'p': 'A manufacturing company, for instance, may find that raw materials, labour and '
          'production overheads are the line items that give the most useful information about its '
          'activities, and present by nature; other companies may present by function in some '
          'situations and by nature in others. IFRS 18\'s structure and content also specifically '
          'allow **banks, insurance companies and property investment companies** to present their '
          'statement of profit or loss according to their own main specific activities, '
          'differently from other kinds of business.'},
    {'p': 'IFRS 18 classifies income and expenses into **five categories** in the statement of '
          'profit or loss:'},
    {'ol': [
      '**Operating category**', '**Investing category**', '**Financing category**',
      '**Income taxes category**', '**Discontinued operations category**',
    ]},
    {'p': 'This new format enhances clarity and forces consistent classification of income and '
          'expenses across companies, since every item now has one, and only one, of five '
          'categories it belongs to.'},
    {'h4': 'Operating category'},
    {'p': 'The operating category consists of **all income and expenses that are not classified '
          'in the investing, financing, income taxes or discontinued operations categories.** It '
          'is the **default** category. IFRS 18 defines the operating category as all income and '
          'expenses arising from a company\'s operations; it is **not** meant to measure only '
          'recurring operating performance. Operating activity is defined to include: income from '
          'the main activities of the business, and income and expenses from other business '
          'activities — that is, income and expenses that do not meet the requirements to be '
          'classified in any of the other four categories.'},
    {'h4': 'Investing category'},
    {'p': 'Income and expenses in the investing category are those that enable investors to '
          'analyse returns from stand-alone investments separately from a company\'s core '
          'operations. The investing category includes: income and expenses from assets that '
          'generate returns separately from a company\'s business activities, such as rentals from '
          'investment property, dividends from shares in other companies, or income from bonds; '
          'and income and expenses from cash and cash equivalents and from investments in '
          'associates, joint ventures and unconsolidated subsidiaries — such as a company\'s share '
          'of profits from an associate.'},
    {'h4': 'Financing category'},
    {'p': 'The financing category includes: income and expenses on liabilities such as bank loans '
          'and bonds, and other liabilities arising from pure financing transactions; and interest '
          'expenses on any other liability — for example, lease and pension liabilities. The '
          'financing category, together with the subtotal for profit before financing and income '
          'taxes, enables investors to analyse a company\'s performance **before** the effects of '
          'how it is financed.'},
    {'h4': 'Income taxes category'},
    {'p': 'The income taxes category consists of income tax expense (or income) included in profit '
          'or loss in accordance with **IAS 12 Income Taxes**, and any related foreign exchange '
          'differences.'},
    {'h4': 'Discontinued operations category'},
    {'p': 'The discontinued operations category consists of income and expenses from discontinued '
          'operations, recognised in accordance with **IFRS 5 Non-current Assets Held for Sale and '
          'Discontinued Operations**.'},
    {'h3': 'What IFRS 18 carries forward unchanged from IAS 1'},
    {'p': 'IFRS 18 does **not** change how an entity recognises or measures revenue, expenses, '
          'assets, liabilities or equity — that remains the job of the individual standards '
          '(IFRS 15, IAS 2, IAS 16, and so on). The following principles specifically remain '
          'unchanged from IAS 1:'},
    {'ul': [
      'the accrual basis;', 'the going concern assumption;', 'materiality;', 'consistency;',
      'offsetting; and', 'fair presentation.',
    ]},
    {'p': 'The structure and content of the statement of financial position and the statement of '
          'changes in equity are also unchanged. The statement of cash flows is likewise '
          'essentially unchanged **except** for one specific point: the classification of '
          'dividends and interest paid, and dividends and interest received.'},
    {'table': {'head': ['Cash flow', 'IFRS 18 classification'], 'align': 'll', 'rows': [
      ['Dividends and interest **paid**', 'Financing activities'],
      ['Dividends and interest **received**', 'Investing activities'],
    ]}},
    {'warn': 'Under IAS 7, entities previously had a choice — dividends and interest paid or '
             'received could, in some circumstances, be classified as operating activities '
             'instead. **IFRS 18 discontinues that flexibility.** If you have learned the old, '
             'more permissive IAS 7 classification options from an older source, replace that '
             'understanding with the fixed IFRS 18 rule above: paid always sits in financing; '
             'received always sits in investing.'},
  ]},

  {'n': '2.9', 't': 'Further reading', 'b': [
    {'note': 'The IFRS Foundation publishes the primary source material behind this whole '
             'chapter, free to read: the '
             '[Conceptual Framework for Financial Reporting](https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/), '
             '[IAS 1 Presentation of Financial Statements](https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/), '
             'and [IFRS 18 Presentation and Disclosure in Financial Statements](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) '
             '— the IFRS 18 project page also carries the IASB\'s own project summary and '
             'effective-date timeline (annual periods beginning on or after 1 January 2027). For '
             'a plain-English run-through of the qualitative characteristics and the five '
             'elements before you dig into the standards themselves, '
             '[Investopedia\'s explainer on the FASB/IASB Conceptual Framework](https://www.investopedia.com/terms/c/conceptual-framework.asp) '
             'and its shorter note on '
             '[materiality](https://www.investopedia.com/terms/m/materiality.asp) are both good '
             'starting points. If a link has moved, search the standard\'s name directly on '
             'ifrs.org — the Foundation reorganises its site occasionally.'},
  ]},
 ],
 'formulas': [
  {'lb': 'Financial capital maintenance', 'tex': '\\text{Profit} = \\Delta\\text{Net assets} + '
   '\\text{Drawings} - \\text{Capital introduced}',
   'nt': 'The basis of the capital comparison method in Chapter 6.'},
  {'lb': 'The accounting identity behind equity', 'tex': '\\text{Equity} = \\text{Assets} - '
   '\\text{Liabilities}', 'nt': 'Equity is defined as a residual, never measured directly.'},
 ],
 'focus':
   'Chapter 2 is short-answer territory and it is generous. The qualitative characteristics (which '
   'two are fundamental, which four enhancing) come up nearly every diet, as do the element '
   'definitions. Learn the definitions of asset and liability in the exact Framework wording — '
   'part-marks follow the key phrases *control*, *past event*, *present obligation*. Offsetting is '
   'the single most commonly misunderstood "other concept": learn the two-part test, and learn the '
   'named exceptions (PP&E net of depreciation, receivables net of an allowance) that are NOT '
   'offsetting at all. On IFRS 18, be ready to name all three requirements — subtotals, MPMs, and '
   'aggregation/disaggregation — and the five income/expense categories with the operating category '
   'as the default. The one purely computational item is capital maintenance, which is the same '
   'arithmetic as incomplete records in Chapter 6.',
 'errors': [
   'Listing comparability as a fundamental characteristic. It is enhancing; only relevance and '
   'faithful representation are fundamental.',
   'Defining an asset by ownership. The test is control.',
   'Saying financial statements show the value of the entity. They provide inputs for users to '
   'estimate it.',
   'Forgetting that materiality is entity-specific, and quoting a fixed percentage as if it were a rule.',
   'Naming only two of IFRS 18\'s three requirements (usually forgetting aggregation/disaggregation, '
   'exactly the trap the study text\'s own wording sets).',
   'Treating any "net" figure as offsetting — PP&E net of depreciation and receivables net of a '
   'doubtful debt allowance are ordinary measurement, not offsetting.',
   'Applying the old IAS 7 flexibility to classify interest/dividends paid or received as operating '
   'activities. IFRS 18 fixes paid to financing and received to investing.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'Which TWO of the following are the fundamental qualitative characteristics?',
    'o': ['Comparability and verifiability', 'Relevance and faithful representation',
          'Timeliness and understandability', 'Prudence and neutrality',
          'Materiality and consistency'],
    'a': 1,
    'w': 'Relevance and faithful representation are fundamental — information lacking either is '
         'not useful. Comparability, verifiability, timeliness and understandability are enhancing.',
    'src': 'Chapter 2.3'},
   {'q': 'An entity controls a machine held under a five-year lease but does not own it. Under '
         'the Conceptual Framework the machine is',
    'o': ['not an asset, because the entity does not own it',
          'an asset, because the entity controls the resource as a result of a past event',
          'an asset only if the lease is longer than the useful life',
          'a contingent asset disclosed in the notes',
          'an expense of the period in which the lease was signed'],
    'a': 1,
    'w': 'The definition turns on control, not legal ownership. The past event is signing the '
         'lease; the right to direct the use of the machine is the economic resource.',
    'src': 'Chapter 2.5'},
   {'q': 'A business had opening net assets of ₦3,000,000 and closing net assets of ₦4,100,000. '
         'The owner introduced ₦500,000 and withdrew ₦200,000 during the year. Profit for the '
         'year is',
    'o': ['₦800,000', '₦1,100,000', '₦1,400,000', '₦1,800,000', '₦600,000'],
    'a': 0,
    'w': 'Strip out the two owner transactions from the movement in net assets.',
    'calc': '\\text{Profit} = (4{,}100{,}000 - 3{,}000{,}000) + 200{,}000 - 500{,}000 = 800{,}000',
    'src': 'Chapter 2.5'},
   {'q': 'The pervasive constraint on the information provided in financial reports is',
    'o': ['materiality', 'prudence', 'the cost of providing it', 'going concern', 'consistency'],
    'a': 2,
    'w': 'Cost is described in the Framework as the pervasive constraint: the benefits of '
         'reporting information must justify the cost of providing it.',
    'src': 'Chapter 2.3'},
   {'q': 'Under IFRS 18, which subtotal must be presented in the statement of profit or loss?',
    'o': ['Gross profit', 'EBITDA', 'Operating profit',
          'Profit attributable to non-controlling interests', 'Net current assets'],
    'a': 2,
    'w': 'IFRS 18 requires two defined subtotals: operating profit, and profit before financing '
         'and income taxes. EBITDA is a management-defined performance measure and must be '
         'reconciled in a note.',
    'src': 'Chapter 2.8'},
   {'q': 'Which measurement basis reflects the present value of the cash flows an entity expects '
         'to derive from the continuing use of an asset and its ultimate disposal?',
    'o': ['Fair value', 'Historical cost', 'Current cost', 'Value in use', 'Fulfilment value'],
    'a': 3,
    'w': 'Value in use is entity-specific and forward-looking, and is the basis used in '
         'impairment testing. Fair value is market-based.',
    'src': 'Chapter 2.5'},
   {'q': 'A company shows trade receivables of ₦2,000,000 owed by a customer, and separately owes '
         'the same customer ₦1,800,000, with no legally enforceable right of set-off between the '
         'two balances. Presenting only the ₦200,000 net figure would be',
    'o': ['correct, because it reflects the economic substance',
          'a breach of IAS 1\'s prohibition on offsetting, since the legal right of set-off is missing',
          'required under the prudence concept',
          'acceptable provided both balances are with the same customer',
          'a valid application of the materiality concept'],
    'a': 1,
    'w': 'Offsetting is only permitted where the entity has a legally enforceable right to offset '
         'AND intends to settle net or simultaneously. Without the legal right, the gross amounts '
         'must be shown separately.',
    'src': 'Chapter 2.6'},
  ],
  'theory': [
   {'q': 'The IASB Conceptual Framework identifies two fundamental and four enhancing qualitative '
         'characteristics. Identify them and explain each briefly.',
    'marks': 8,
    'a': [
      {'h4': 'Fundamental'},
      {'ol': [
        '**Relevance** — information is relevant if it is capable of making a difference to a '
        'decision. It does so through predictive value, confirmatory value, or both. Materiality '
        'is the entity-specific aspect of relevance.',
        '**Faithful representation** — the information depicts the substance of the economic '
        'phenomenon. A perfectly faithful depiction is complete, neutral and free from error.']},
      {'h4': 'Enhancing'},
      {'ol': [
        '**Comparability** — like items look alike and unlike items look different, both between '
        'entities and across periods.',
        '**Verifiability** — knowledgeable, independent observers could reach consensus that the '
        'depiction is faithful.',
        '**Timeliness** — the information is available while it can still influence decisions.',
        '**Understandability** — it is classified, characterised and presented clearly and concisely.']},
      {'note': 'Add the cost constraint for a mark: the benefits of reporting must justify the cost.'},
    ],
    'src': 'Chapter 2.3'},
   {'q': 'Define an asset and a liability as set out in the 2018 Conceptual Framework, and state '
         'the recognition criteria that must additionally be satisfied.',
    'marks': 6,
    'a': [
      {'p': '**Asset** — a present economic resource controlled by the entity as a result of past '
            'events, an economic resource being a right that has the potential to produce '
            'economic benefits.'},
      {'p': '**Liability** — a present obligation of the entity to transfer an economic resource '
            'as a result of past events.'},
      {'p': '**Recognition.** An item meeting a definition is recognised only if recognition '
            'provides users with information that is:'},
      {'ul': ['**relevant** — recognition may fail where existence is uncertain or the '
              'probability of an inflow or outflow is low; and',
              '**a faithful representation** — recognition may fail where the only available '
              'measure carries such high measurement uncertainty that the resulting information '
              'would not be useful.']},
      {'p': 'Recognition is also subject to the cost constraint: the benefit of recognising the '
            'item must exceed the cost of doing so.'},
    ],
    'src': 'Chapter 2.5'},
   {'q': 'State and explain the THREE requirements introduced by IFRS 18 to achieve its '
         'objective of improving how companies communicate financial performance.',
    'marks': 9,
    'a': [{'ol': [
      '**Presentation of new defined subtotals.** IFRS 18 requires companies to present two new '
      'subtotals in the statement of profit or loss: operating profit, and profit before '
      'financing and income taxes. This gives a consistent structure and improves comparability, '
      'without changing how performance itself is measured.',
      '**Disclosure of management-defined performance measures (MPMs).** Companies must disclose '
      'a reconciliation between any management-defined performance measure (such as an adjusted '
      'profit figure) and the nearest IFRS-defined total or subtotal, together with the '
      'judgements applied and an explanation of why any unusual income or expense is not expected '
      'to recur.',
      '**Aggregation or disaggregation.** Companies must aggregate or disaggregate items to '
      'present useful, structured line items in the primary statements and useful information in '
      'the notes — without ever letting the aggregation obscure material information.',
    ]},
    {'note': 'The study text itself only labels the first two of these "1)" and "2)" before moving '
             'to a new section header for the third — see Chapter 2.8 for the full explanation of '
             'this gap in the source material.'}],
    'src': 'Chapter 2.8'},
  ]},
}
