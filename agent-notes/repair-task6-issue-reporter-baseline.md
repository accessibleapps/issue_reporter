# Replace the live sending smoke test with offline report coverage

## Goal

Make complete default collection and execution safe, with meaningful real-source assertions. Preserve report behavior and separate attachment-failure feature PR #1. No live services, system inventory, credentials, or consumer changes.

## State

- Exact origin git@github.com:accessibleapps/issue_reporter.git; fresh fetched master c5c9870036bbb6d9d219f2514f32292d81d3a68a. Isolated worktree issue-reporter-baseline on repair/task6-issue-reporter-baseline.
- Canonical master and untracked build/bytecode files preserved. Feature worktree and OPEN/DRAFT PR #1 at 4dadcc465310ae9992691e93f497d82e08823333 unchanged.
- Global instructions, repair prompts and Accessible Apps ownership/CI skills read. No repository/nested AGENTS.md, CLAUDE.md or .agents/skills found. Current repair authority explicitly authorizes offline coverage and full local checks. Parent also authorizes minimal hosted PR/default-push CI using repository-ci: one Linux interpreter, verified pinned actions, workflow audits.
- README records uv build. pyproject.toml and tracked uv.lock unchanged; no production source/dependency change. Current topology issue-reporter record is in C:/Users/Q/code/accessible-apps-skills/accessible_apps_topology.json.

## Decisions and why

- Legacy issue_reporter/test_issue_reporter.py has one credential-bearing sending function, zero assertions, an implicit system-info constructor, and send_report(test=True). It is an obsolete/broken live-integration smoke/demo. It also omits application_name (default None), so current subject concatenation would raise TypeError before delivery if reached. Real inventory collection and credential-bearing construction still make execution unsafe. test=True is merely forwarded; the production Mailgun implementation uses its actual request method if invoked. No successful live delivery is claimed.
- Legacy AST inspected without any string values, import, collection, system inventory or service invocation. Static red characterization: assertions=0, unmocked inventory constructors=1, send calls=1; assertion failed without executing legacy code. No behavioral red production defect is claimed for this unsafe-test replacement.
- Replace legacy module with tests/test_issue_reporter.py so default full pytest collection does not import the production package before mocked dependencies are installed. The actual sending scenario now has payload/attachment assertions, plus construction coverage; no skips or opt-in live boundary.
- Direct real-source loading uses fake Mailgun/sysinfo modules, fake file handles, dummy fixture key and example.invalid addresses. Inventory fails closed unless a test explicitly configures its mocked return. No sender abstraction or feature cherry-pick.
- Smallest slice: ~125 lines offline coverage replacing 18-line live smoke test, README test authority, then one minimal CI workflow. Separate commits establish owner authority before workflow YAML.

## Surprises

The editing tool reported a failed legacy-file deletion, but read-only inspection showed that file absent and no added files. Partial outcome verified before completing the replacement with the editing tool. No legacy collection happened during the intermediate state.

## Verification

- Red characterization was static AST only: actual unsafe legacy module had 0 assertions, 1 unmocked inventory constructor and 1 send call. It was never imported or collected; literal values withheld.
- Safe full collection: 6 tests collected. Complete offline execution: 6 passed in 0.37s on CPython 3.13.15 / pytest 9.1.1; final pinned README command also passed all 6 in 0.35s. No skip, deselection, production dependency import, service call, real logs or inventory.
- README uv build succeeded with wheel and source distribution. Manifest SHA256 50B14F7D65DE49D45FBB63B69435B8867BEDB7FA59018D516DE0C020C4E25C56; tracked lock SHA256 D6A7A4DD3A8281777C38DBCA27FFDFB96C44D1F79985145DB550E5E3E81A6702 unchanged before/after. No resolver graph change.
- Existing shared-owner topology verifies issue-reporter report ownership and README build authority; test purpose previously unavailable because no documented command. Explicit current task authorizes establishing the offline default suite. Existing consumers need no source/pin change for this test-only repair.
- Command now pins the observed pytest 9.1.1; hosted environment will be one Linux CPython 3.13 interpreter, without any package support declaration change.
- Built wheel and source distribution are readable and nonempty; neither contains the old test or legacy credential-like literal (compared without printing/copying its value). Replacement tests are present in the source distribution.
- Final actionlint 1.7.12 syntax/expression audit passed with optional shellcheck/pyflakes integrations disabled. Final zizmor 1.31.1 --offline --pedantic reports zero findings after naming the job. Both final workflow audits exit 0.

## Next step

Owner coverage/README authority committed as 6d1f3c4fbdc373a0ae76bfe1c5fe7820474b4b94. Added one Linux/Python 3.13 job running the complete suite, uv build and exact wheel/sdist existence checks, on PRs and master pushes. Read-only permissions, no persisted checkout credentials, no service/private dependency secrets or cache, 10-minute timeout and superseded-run concurrency. Official action manifests read and tag SHAs verified via GitHub API: checkout v7.0.1 and setup-uv v10.3.0; uv release 0.13.4 verified. Local audits complete; commit workflow/README/note and return exact head/report/proposed PR for coordinator and actual Claude review. Hosted results unavailable before authorized publication. Coordinator must authorize any publication, prerequisite merge or later affected-feature rebase explicitly. No push, merge, ready transition, rebase, release or settings changes.
