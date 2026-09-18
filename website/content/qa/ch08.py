CH = {
 'n': 8,
 't': 'Test of Hypothesis',
 'brief': 'Null and alternative hypotheses, the two types of error, significance levels and '
          'critical regions, and the z and t tests for a mean and for a proportion.',
 'outcomes': [
   'State a null and an alternative hypothesis correctly',
   'Distinguish Type I from Type II error',
   'Choose between a one-tailed and a two-tailed test',
   'Select and compute the right test statistic',
   'Compare with the critical value and state a conclusion in context',
 ],
 'secs': [
  {'n': '8.1', 't': 'The vocabulary', 'b': [
    {'p': 'A **hypothesis test** asks whether a sample result is far enough from a claimed '
          'population value to be inconsistent with that claim. The logic is that of a court: the '
          'claim is presumed true until the evidence against it is strong enough.'},
    {'def': {'t': 'Null hypothesis $H_0$',
             'd': 'The claim being tested, always stated as an equality — for example '
                  '$H_0: \\mu = 500$. It is the position we hold unless the data force us out '
                  'of it.'}},
    {'def': {'t': 'Alternative hypothesis $H_1$',
             'd': 'What we accept if $H_0$ is rejected: $\\mu \\ne 500$ (two-tailed), '
                  '$\\mu > 500$ or $\\mu < 500$ (one-tailed). The wording of the question '
                  'decides which.'}},
    {'def': {'t': 'Significance level $\\alpha$',
             'd': 'The probability of rejecting $H_0$ when it is in fact true. Conventionally '
                  '5% or 1%. It is chosen **before** the test, not after seeing the result.'}},
    {'def': {'t': 'Critical region',
             'd': 'The set of values of the test statistic for which $H_0$ is rejected. Its '
                  'boundary is the critical value read from tables.'}},
    {'h4': 'The two errors'},
    {'table': {'align': 'lll', 'head': ['', '$H_0$ is true', '$H_0$ is false'], 'rows': [
      ['Reject $H_0$', '**Type I error** (probability $\\alpha$)', 'Correct decision'],
      ['Do not reject $H_0$', 'Correct decision', '**Type II error** (probability $\\beta$)'],
    ]}},
    {'key': 'A **Type I error** rejects a true claim — convicting the innocent. A **Type II '
            'error** fails to reject a false claim — acquitting the guilty. Lowering '
            '$\\alpha$ (say from 5% to 1%) makes a Type I error less likely but a Type II '
            'error more likely. Only a larger sample reduces both.'},
  ]},

  {'n': '8.2', 't': 'The five steps', 'b': [
    {'steps': [
      'State $H_0$ and $H_1$, and note whether the test is one- or two-tailed.',
      'Choose the significance level $\\alpha$ and find the critical value from tables.',
      'Compute the test statistic from the sample.',
      'Compare the statistic with the critical value.',
      'State the conclusion **in the words of the question** — not merely "reject $H_0$".',
    ]},
    {'fbox': {'h': 'Critical values you should know by heart', 'rows': [
      {'lb': 'Two-tailed, 5%', 'tex': 'z = \\pm 1.96'},
      {'lb': 'Two-tailed, 1%', 'tex': 'z = \\pm 2.58'},
      {'lb': 'One-tailed, 5%', 'tex': 'z = 1.645'},
      {'lb': 'One-tailed, 1%', 'tex': 'z = 2.33'},
    ]}},
    {'note': 'The word **"differs from"** signals a two-tailed test. The words **"exceeds", '
             '"is greater than", "has improved", "is less than"** all signal a one-tailed test. '
             'Reading this wrongly changes the critical value and usually the conclusion.'},
  ]},

  {'n': '8.3', 't': 'Choosing the test statistic', 'b': [
    {'fbox': {'h': 'Test statistics', 'rows': [
      {'lb': 'Mean, $\\sigma$ known or $n \\ge 30$',
       'tex': 'z = \\frac{\\bar{x} - \\mu}{\\sigma / \\sqrt{n}}'},
      {'lb': 'Mean, $\\sigma$ unknown and $n < 30$',
       'tex': 't = \\frac{\\bar{x} - \\mu}{s / \\sqrt{n}}, \\quad \\nu = n - 1'},
      {'lb': 'Proportion',
       'tex': 'z = \\frac{p - \\pi}{\\sqrt{\\dfrac{\\pi(1-\\pi)}{n}}}'},
      {'lb': 'Difference of two means',
       'tex': 'z = \\frac{\\bar{x}_1 - \\bar{x}_2}'
              '{\\sqrt{\\dfrac{\\sigma_1^2}{n_1} + \\dfrac{\\sigma_2^2}{n_2}}}'},
    ]}},
    {'p': 'The denominator in every case is the **standard error** — the standard deviation of '
          'the sampling distribution of the statistic. The test statistic is simply "how many '
          'standard errors is the sample result from the claimed value".'},
    {'warn': 'In the proportion test the standard error uses $\\pi$, the **hypothesised** '
             'proportion, not the sample proportion $p$. Under $H_0$ we assume $\\pi$ is true, '
             'so it is $\\pi$ that generates the sampling distribution.'},
  ]},

  {'n': '8.4', 't': 'Worked tests', 'b': [
    {'eg': {'t': 'Two-tailed test of a mean (large sample)', 'q': [
      {'p': 'A manufacturer claims that its bags of cement weigh 500 kg on average. A random '
            'sample of 64 bags has a mean weight of 496 kg with a standard deviation of 12 kg. '
            'Test at the 5% level whether the mean weight differs from the claim.'}],
      'a': [
      {'p': '**Step 1.** The word "differs" gives a two-tailed test.'},
      {'tex': 'H_0: \\mu = 500 \\qquad H_1: \\mu \\ne 500'},
      {'p': '**Step 2.** At $\\alpha = 0.05$, two-tailed, the critical values are '
            '$z = \\pm 1.96$.'},
      {'p': '**Step 3.** $n = 64 \\ge 30$, so use $z$ with $s$ in place of $\\sigma$:'},
      {'tex': 'z = \\frac{\\bar{x} - \\mu}{s/\\sqrt{n}} = \\frac{496 - 500}{12/\\sqrt{64}} '
              '= \\frac{-4}{12/8} = \\frac{-4}{1.5} = -2.67'},
      {'p': '**Step 4.** $|-2.67| = 2.67 > 1.96$, so the statistic falls in the critical '
            'region.'},
      {'p': '**Step 5.** Reject $H_0$. There is significant evidence at the 5% level that the '
            'mean weight of the bags differs from 500 kg; on this sample they are '
            '**underweight**.'},
      {'note': 'Note how the conclusion names the cement, not just $H_0$. At the 1% level the '
               'critical value is $\\pm 2.58$ and $2.67$ still exceeds it, so the conclusion '
               'would be unchanged — worth a sentence if the question asks you to comment.'}]}},

    {'eg': {'t': 'Small sample: the t test', 'q': [
      {'p': 'A supplier claims that its cable has a mean breaking strain of 50 kg. A sample of '
            '16 lengths gives a mean of 51.2 kg with a standard deviation of 3.2 kg. Test at '
            'the 5% level whether the breaking strain differs from the claim.'}],
      'a': [
      {'tex': 'H_0: \\mu = 50 \\qquad H_1: \\mu \\ne 50'},
      {'p': '$\\sigma$ is unknown and $n = 16 < 30$, so use $t$ with '
            '$\\nu = 16 - 1 = 15$ degrees of freedom. From tables, '
            '$t_{0.025,\\,15} = \\pm 2.131$.'},
      {'tex': 't = \\frac{51.2 - 50}{3.2/\\sqrt{16}} = \\frac{1.2}{3.2/4} '
              '= \\frac{1.2}{0.8} = 1.50'},
      {'p': '$1.50 < 2.131$, so the statistic is **not** in the critical region.'},
      {'p': 'Do not reject $H_0$. There is no significant evidence at the 5% level that the mean '
            'breaking strain differs from 50 kg.'},
      {'warn': 'Say "**do not reject** $H_0$", never "accept $H_0$". Failing to find evidence '
               'against a claim is not proof that the claim is true — the sample may simply be '
               'too small to detect a real difference.'}]}},

    {'eg': {'t': 'Test of a proportion (one-tailed)', 'q': [
      {'p': 'A bank believes that more than 20% of its customers use the mobile app weekly. In '
            'a random sample of 400 customers, 96 do so. Test the belief at the 5% level.'}],
      'a': [
      {'p': 'The belief to be supported is "more than 20%", so that becomes $H_1$ and the test '
            'is one-tailed to the right.'},
      {'tex': 'H_0: \\pi = 0.20 \\qquad H_1: \\pi > 0.20'},
      {'p': 'Critical value at 5%, one-tailed: $z = 1.645$. Sample proportion:'},
      {'tex': 'p = \\frac{96}{400} = 0.24'},
      {'tex': 'z = \\frac{p - \\pi}{\\sqrt{\\dfrac{\\pi(1-\\pi)}{n}}} '
              '= \\frac{0.24 - 0.20}{\\sqrt{\\dfrac{0.20 \\times 0.80}{400}}} '
              '= \\frac{0.04}{\\sqrt{0.0004}} = \\frac{0.04}{0.02} = 2.00'},
      {'p': '$2.00 > 1.645$, so reject $H_0$. There is significant evidence at the 5% level '
            'that more than 20% of the bank\'s customers use the mobile app weekly.'},
      {'note': 'At the 1% level the critical value is $2.33$ and $2.00 < 2.33$, so the evidence '
               'would **not** be strong enough. The conclusion depends on the significance '
               'level, which is exactly why it must be fixed in advance.'}]}},
  ]},

  {'n': '8.5', 't': 'Worksheet summary — every term defined and every formula', 'b': [
    {'h3': 'Section-by-section checklist'},
    {'ol': [
      '**§8.1 The vocabulary** — $H_0$ (the claim, always an equality) vs $H_1$ (accepted if '
      '$H_0$ is rejected — $\\ne$ two-tailed, $>$/$<$ one-tailed); significance level $\\alpha$ '
      '(fixed **before** testing); critical region (test-statistic values that reject $H_0$). '
      'Type I error = rejecting a true $H_0$ (probability $\\alpha$); Type II = failing to '
      'reject a false $H_0$ (probability $\\beta$). Lowering $\\alpha$ cuts Type I risk but '
      'raises Type II risk — only a bigger sample reduces both together.',
      '**§8.2 The five steps** — state $H_0$/$H_1$ and tail; fix $\\alpha$ and find the '
      'critical value; compute the test statistic; compare; conclude **in the words of the '
      'question**. Memorise: two-tailed 5% $z=\\pm1.96$, 1% $z=\\pm2.58$; one-tailed 5% '
      '$z=1.645$, 1% $z=2.33$. "Differs from" → two-tailed; "exceeds/greater than/improved/'
      'less than" → one-tailed.',
      '**§8.3 Choosing the test statistic** — $z=(\\bar{x}-\\mu)/(\\sigma/\\sqrt{n})$ when '
      '$\\sigma$ is known or $n\\ge30$; $t=(\\bar{x}-\\mu)/(s/\\sqrt{n})$, $\\nu=n-1$, when '
      '$\\sigma$ is unknown and $n<30$; proportion $z=(p-\\pi)/\\sqrt{\\pi(1-\\pi)/n}$ — using '
      'the **hypothesised** $\\pi$, not the sample $p$, in the standard error, since $H_0$ '
      'assumes $\\pi$ true. The denominator is always the standard error of the statistic.',
      '**§8.4 Worked tests** — three full worked examples (two-tailed mean/large sample, '
      't-test/small sample, one-tailed proportion) demonstrating the five steps end to end. '
      'Always say "**do not reject** $H_0$", never "accept $H_0$" — failing to find evidence '
      'against a claim is not proof the claim is true.',
    ]},
    {'h3': 'All the terms'},
    {'ul': [
      '**Hypothesis** — an assumption or guess about a population parameter.',
      '**Null hypothesis $H_0$** — states there is *no difference* / no effect (e.g. '
      '$\\mu = \\mu_0$). Always contains "=".',
      '**Alternative hypothesis $H_1$ (or $H_a$)** — any hypothesis that differs from $H_0$ '
      '($\\mu \\neq \\mu_0$, $\\mu > \\mu_0$ or $\\mu < \\mu_0$).',
      '**Parameter** — a numerical property of the *population* ($\\mu$, $\\sigma$, $P_0$). '
      '**Statistic** — the corresponding quantity computed from the *sample* '
      '($\\bar{x}$, $s$, $p$).',
      '**Type I error** — rejecting $H_0$ when it is true. Its probability is $\\alpha$.',
      '**Type II error** — accepting $H_0$ when it is false. Its probability is $\\beta$.',
      '**Level of significance $\\alpha$** — the maximum probability of a Type I error the '
      'investigator will accept; stated *before* testing. Common values 5% (0.05) and 1% '
      '(0.01). Confidence $= 1 - \\alpha$.',
      '**Test statistic** — the value computed from the sample ($z_{cal}$ or $t_{cal}$) that is '
      'compared with the table (critical) value to decide.',
      '**Critical value / table value** — the value from the $z$ or $t$ table at the chosen '
      '$\\alpha$; it bounds the critical region.',
      '**Critical (rejection) region** — the set of test-statistic values, of total area '
      '$\\alpha$, that lead to rejecting $H_0$.',
      '**One-tailed (one-sided) test** — $H_1$ is directional ($\\mu > \\mu_0$ *or* '
      '$\\mu < \\mu_0$); the whole $\\alpha$ is in one tail.',
      '**Two-tailed (two-sided) test** — $H_1$ is $\\mu \\neq \\mu_0$; $\\alpha$ is split, '
      '$\\alpha/2$ in each tail.',
      '**Degrees of freedom $\\nu$** — for the one-sample $t$-test, $\\nu = n - 1$.',
      '**Large sample** — $n > 30$: use the $z$-test (normal). **Small sample** — $n \\le 30$ '
      '(study text: $n < 30$): use the $t$-test.',
      '**Sample proportion** — $p = x/n$, where $x$ items out of $n$ have the attribute; '
      '$P_0$ is the claimed population proportion.',
    ]},
    {'h3': 'The five steps'},
    {'ol': [
      'State $H_0$ and $H_1$ and the significance level $\\alpha$.',
      'Choose the test statistic ($z$ for a large sample or a proportion; $t$, $\\nu = n-1$, '
      'for a small sample).',
      'Compute the test statistic from the sample.',
      'Find the critical value: at $\\alpha$ for a one-tailed test, at $\\alpha/2$ for a '
      'two-tailed test.',
      'Decision — see the decision rules below — then state the conclusion in words.',
    ]},
    {'h3': 'Decision rules'},
    {'ul': [
      'Right one-tailed ($H_1: \\mu > \\mu_0$) — reject $H_0$ if $z_{cal} > z_{tab}$ (or '
      '$t_{cal} > t_{tab}$).',
      'Left one-tailed ($H_1: \\mu < \\mu_0$) — reject $H_0$ if $z_{cal} < -z_{tab}$ (or '
      '$t_{cal} < -t_{tab}$).',
      'Two-tailed ($H_1: \\mu \\neq \\mu_0$) — reject $H_0$ if $|z_{cal}| > z_{tab}$ (or '
      '$|t_{cal}| > t_{tab}$).',
      'Otherwise — do not reject (accept) $H_0$.',
    ]},
    {'note': 'Common critical values: two-tailed 5% → **1.96**; one-tailed 5% → **1.645**; '
             'two-tailed 1% → **2.58**; one-tailed 1% → **2.33**.'},
    {'h3': 'A. Test of a single population mean'},
    {'fbox': {'h': 'Test statistic — mean', 'rows': [
      {'lb': 'Large sample ($n > 30$), $z$-test',
       'tex': 'z_{cal} = \\dfrac{\\bar{x} - \\mu_0}{\\sigma/\\sqrt{n}}',
       'nt': 'If $\\sigma$ is unknown, use $s$ (large sample).'},
      {'lb': 'Small sample ($n \\le 30$), $t$-test, $\\nu = n - 1$',
       'tex': 't_{cal} = \\dfrac{\\bar{x} - \\mu_0}{s/\\sqrt{n}}'},
      {'lb': 'Sample mean', 'tex': '\\bar{x} = \\dfrac{\\sum x}{n}'},
      {'lb': 'Sample variance (with $n - 1$)',
       'tex': 's^2 = \\dfrac{\\sum (x - \\bar{x})^2}{n - 1}'},
      {'lb': 'Standard error of the mean',
       'tex': '\\text{SE}(\\bar{x}) = \\dfrac{\\sigma}{\\sqrt{n}} \\ \\text{ or } \\ '
              '\\dfrac{s}{\\sqrt{n}}'},
    ]}},
    {'h3': 'B. Test of a single population proportion'},
    {'fbox': {'h': 'Test statistic — proportion', 'rows': [
      {'lb': 'Sample proportion', 'tex': 'p = \\dfrac{x}{n}'},
      {'lb': 'Hypotheses', 'tex': 'H_0: P_0 = p \\qquad H_1: P_0 \\neq p \\ (\\text{or } >, <)'},
      {'lb': '$z$-test (using $P_0$ in the standard error)',
       'tex': 'z_{cal} = \\dfrac{p - P_0}{\\sqrt{\\dfrac{P_0(1 - P_0)}{n}}}'},
      {'lb': 'alternative form (using $p$ in the standard error)',
       'tex': 'z_{cal} = \\dfrac{p - P_0}{\\sqrt{\\dfrac{p(1 - p)}{n}}}'},
    ]}},
    {'h3': 'C. Confidence interval for a mean'},
    {'tex': '\\bar{x} \\pm z_{\\alpha/2}\\,\\dfrac{\\sigma}{\\sqrt{n}} \\qquad '
            '(\\text{small sample: } \\bar{x} \\pm t_{\\alpha/2, \\, n-1}\\,\\dfrac{s}{\\sqrt{n}})'},
  ]},
 ],
 'formulas': [
  {'lb': 'Sample mean', 'tex': '\\bar{x} = \\frac{\\sum x}{n}'},
  {'lb': 'Sample variance ($n-1$)', 'tex': 's^2 = \\frac{\\sum (x - \\bar{x})^2}{n - 1}'},
  {'lb': 'Test statistic — mean, large sample ($z$)',
   'tex': 'z_{cal} = \\frac{\\bar{x} - \\mu_0}{\\sigma/\\sqrt{n}}'},
  {'lb': 'Test statistic — mean, small sample ($t$, $\\nu = n-1$)',
   'tex': 't_{cal} = \\frac{\\bar{x} - \\mu_0}{s/\\sqrt{n}}'},
  {'lb': 'Sample proportion', 'tex': 'p = \\frac{x}{n}'},
  {'lb': 'Test statistic — proportion',
   'tex': 'z_{cal} = \\frac{p - P_0}{\\sqrt{P_0(1-P_0)/n}}'},
  {'lb': 'Standard error of the mean',
   'tex': '\\text{SE}(\\bar{x}) = \\frac{\\sigma}{\\sqrt{n}}'},
  {'lb': 'Confidence interval for a mean',
   'tex': '\\bar{x} \\pm z_{\\alpha/2}\\,\\frac{\\sigma}{\\sqrt{n}}'},
 ],
 'focus':
   'One or two Section A marks on the meaning of a Type I or Type II error, or on identifying '
   'the correct critical value. Section B occasionally asks for a full test — the marks are '
   'spread evenly over the five steps, so an examinee who states the hypotheses and the '
   'conclusion clearly scores well even with an arithmetic slip in the middle.',
 'errors': [
   'Stating $H_0$ as an inequality; it is always an equality.',
   'Using 1.96 for a one-tailed test (it should be 1.645) or 1.645 for a two-tailed test.',
   'Using the sample proportion $p$ instead of $\\pi$ inside the standard error.',
   'Using $z$ when the sample is small and $\\sigma$ unknown, or forgetting $\\nu = n-1$.',
   'Writing "accept $H_0$" rather than "do not reject $H_0$".',
   'Stopping at "reject $H_0$" without a sentence in the context of the question.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'A Type I error occurs when',
    'o': ['a false null hypothesis is not rejected',
          'a true null hypothesis is rejected',
          'the sample size is too small',
          'the wrong test statistic is used',
          'the alternative hypothesis is two-tailed'],
    'a': 1,
    'w': 'Type I rejects a true $H_0$; its probability is the significance level $\\alpha$. '
         'Option A describes a Type II error.',
    'src': 'Chapter 8.1', 'sec': '8.1'},
   {'q': 'The critical value for a two-tailed test at the 5% level of significance is',
    'o': ['$\\pm 1.645$', '$\\pm 1.96$', '$\\pm 2.33$', '$\\pm 2.58$', '$\\pm 1.28$'],
    'a': 1,
    'w': 'With 5% split between two tails, 2.5% lies in each, giving $z = \\pm 1.96$. '
         '$\\pm 1.645$ is the one-tailed 5% value.',
    'src': 'Chapter 8.2', 'sec': '8.2'},
   {'q': 'A sample of 100 items has mean 52 and standard deviation 10. Testing $H_0: \\mu = 50$, '
         'the value of the test statistic is',
    'o': ['0.2', '2.0', '5.0', '20.0', '0.5'],
    'a': 1,
    'w': 'The standard error is $10/\\sqrt{100} = 1$, and the sample mean is 2 above the '
         'hypothesised mean.',
    'calc': 'z = \\frac{52 - 50}{10/\\sqrt{100}} = \\frac{2}{1} = 2.0',
    'src': 'Chapter 8.4', 'sec': '8.4'},
   {'q': 'In testing a hypothesis about a mean with $n = 12$ and the population standard '
         'deviation unknown, the appropriate distribution is',
    'o': ['normal with 12 degrees of freedom',
          '$t$ with 11 degrees of freedom',
          '$t$ with 12 degrees of freedom',
          'normal, since means are always normal',
          'chi-square with 11 degrees of freedom'],
    'a': 1,
    'w': 'A small sample with $\\sigma$ unknown requires the $t$ distribution, and the degrees '
         'of freedom are $n - 1 = 11$.',
    'src': 'Chapter 8.3', 'sec': '8.3'},
   {'q': 'Reducing the significance level from 5% to 1%, with the sample size unchanged,',
    'o': ['reduces the probability of both errors',
          'reduces the probability of a Type I error but increases that of a Type II error',
          'increases the probability of a Type I error',
          'has no effect on either error',
          'makes rejection of $H_0$ more likely'],
    'a': 1,
    'w': 'A smaller $\\alpha$ pushes the critical value further out, so $H_0$ is rejected less '
         'readily: fewer true nulls are rejected, but more false nulls survive.',
    'src': 'Chapter 8.1', 'sec': '8.1'},
   {'q': 'The phrase "the new process produces a higher yield" indicates',
    'o': ['a two-tailed test', 'a one-tailed test', 'a chi-square test',
          'a test of proportions', 'that no test is possible'],
    'a': 1,
    'w': 'Direction is specified ("higher"), so the whole of $\\alpha$ goes into the upper tail.',
    'src': 'Chapter 8.2', 'sec': '8.2'},
  ],
  'theory': [
   {'q': 'Explain the meaning of Type I and Type II errors and outline the steps involved in '
         'testing a statistical hypothesis.',
    'marks': 10,
    'a': [
      {'h4': 'The two errors'},
      {'p': 'A hypothesis test reaches a decision from incomplete evidence, so two mistakes are '
            'possible.'},
      {'ul': [
        '**Type I error** — rejecting a null hypothesis that is in fact true. Its probability '
        'is the significance level $\\alpha$, which the investigator fixes in advance. In an '
        'audit context this is rejecting a set of accounts that are actually fairly stated.',
        '**Type II error** — failing to reject a null hypothesis that is in fact false. Its '
        'probability is denoted $\\beta$. This is passing accounts that are in fact misstated.',
      ]},
      {'table': {'align': 'lll', 'head': ['Decision', '$H_0$ true', '$H_0$ false'], 'rows': [
        ['Reject $H_0$', 'Type I error ($\\alpha$)', 'Correct'],
        ['Do not reject $H_0$', 'Correct', 'Type II error ($\\beta$)'],
      ]}},
      {'p': 'The two are in tension. For a fixed sample size, lowering $\\alpha$ widens the '
            'region in which $H_0$ survives and therefore raises $\\beta$. The only way to '
            'reduce both at once is to increase the sample size, which narrows the sampling '
            'distribution. Which error matters more is a matter of consequences: where a false '
            'rejection is costly, choose a small $\\alpha$; where missing a real effect is '
            'costly, a larger $\\alpha$ may be justified.'},
      {'h4': 'Steps in testing a hypothesis'},
      {'ol': [
        '**State the hypotheses.** $H_0$ is the claim under test and is always an equality. '
        '$H_1$ is what is accepted if $H_0$ is rejected, and its wording — "differs from" '
        'versus "exceeds" — determines whether the test is two-tailed or one-tailed.',
        '**Choose the significance level** $\\alpha$, typically 0.05 or 0.01, before looking '
        'at the data.',
        '**Select the test statistic** appropriate to the parameter and the sample: $z$ for a '
        'mean with $\\sigma$ known or $n \\ge 30$, $t$ with $n - 1$ degrees of freedom for a '
        'small sample with $\\sigma$ unknown, and the proportion statistic for a percentage.',
        '**Determine the critical value and critical region** from tables, using $\\alpha$ and, '
        'for a $t$ test, the degrees of freedom.',
        '**Compute the statistic** from the sample data.',
        '**Compare and decide.** If the statistic falls in the critical region, reject $H_0$; '
        'otherwise do not reject it.',
        '**State the conclusion in the context of the problem**, and note the significance '
        'level at which it holds.',
      ]},
      {'note': 'The correct form of words is "there is (or is not) sufficient evidence at the '
               '5% level to conclude that…". Never write "$H_0$ is proved true": a test that '
               'fails to reject $H_0$ has found no evidence against it, which is a much weaker '
               'statement.'}],
    'src': 'Chapter 8.1–8.2', 'sec': '8.1'},
  ]},
}
