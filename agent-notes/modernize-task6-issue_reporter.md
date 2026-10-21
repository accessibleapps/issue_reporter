# Close report attachments after delivery errors

## Goal

Close report attachments on send failure while preserving the exact existing payload and delivery exception. Scope is issue_reporter source and a new mock-only regression file; no live sends, host inventory, GUI, credentials or consumer pins.

## State

- Current landed prerequisite: #2 merged at 2026-10-21 02:44:57 UTC. Authenticated origin/master is bb35092034bb727cd3bd5c689416afc0e919f682, independently fetched/read back; its reviewed source a4d29c370130aaa25f08f4083017e6a5fb2521f9 had the safe six-test Python3.8/3.13 hosted matrix green.
- Genuinely rebased original feature4dadcc465310ae9992691e93f497d82e08823333 onto actual master with git rebase --no-update-refs, cleanly. Production ExitStack cleanup and its two offline regressions remain byte-identical to original4dad. Restore only the previously approved note's current/historical context, updated for the landed prerequisite.
- Published PR #1 remains4dad; backup/task6-issue-reporter-{published,local}-before-master-rebase preserve4dad and backup/task6-issue-reporter-stacked-before-master-rebase preservesba229fe080b5d8a37234651329ec70751fc56c48. Its original stack branch/worktree, baseline publisheda4, canonical local masterc5 and generated untracked outputs remain untouched.
- The inherited six baseline tests plus the two original attachment cases form the safe eight-test suite. Existing offline Python3.8/3.13 CI/build remains unchanged. New final-head hosted/Claude gates remain pending; no full local CI, live inventory/email or legacy-test/credential read/execution occurred.
- Historical approved local preparation: ba229fe stacked the same feature on then-unmergeda4, with original4dad tips preserved by the earlier feature-local/published-before-stack archives. The following original-worker state and verification describe feature preparation before the separate safe baseline existed.

- Worker 01a15b4c-c035-7355-a97b-abcada04c033; exact origin git@github.com:accessibleapps/issue_reporter.git; authenticated ctoth.
- Fresh API/fetched default master c5c9870036bbb6d9d219f2514f32292d81d3a68a. No open PR. Direct isolated worktree worktrees/issue_reporter on modernize/task6-issue_reporter created after verifying destination absent and canonical only registered worktree.
- Preserve canonical tracked source and its 34 untracked generated build/catalog/bytecode paths. No applicable repository/nested guidance or active commit hook found. Global instructions read. Topology issue-reporter is the verified report owner.
- Tracked pyproject.toml/uv.lock remain authoritative package inputs: Python >=3.8.6, i18n_core and Git sysinfo/mailgun_api/wx_utils/gui_builder. No dependency resolution or pin changes needed for isolated mocked source tests.

## Decisions and why

- issue_reporter.py send_report opens log attachments, calls Mailgun, then closes files only after success. An exception skips closure. Existing GUI/docs/test are real callers; the legacy test contains a credential-like literal and calls delivery, so it must not run.
- Smallest slice: existing standard-library ExitStack manages StringIO and opened attachments, ~20 changed source lines, plus a self-contained mock-only file (~80 lines) that exercises the real source. No new runtime abstraction or dependency.
- Parent explicitly authorized controlled real-source import, Mailgun/sysinfo mocks, reserved addresses, file-open mocks, red/fix/green and success payload characterization. New file only: uv run --isolated --no-project --with pytest pytest tests/test_attachment_cleanup.py -v. This directly loads the source under fake external modules and does not resolve/import project dependencies or legacy tests. No previous tracked test command exists; this is task-specific authority.
- Full legacy pytest is explicitly unsafe/unrun: issue_reporter/test_issue_reporter.py calls send_report against configured Mailgun addresses with a credential-like value. Do not disclose value, execute test, suppress it to claim full success, or contact production. Tracked README uv build is a separate non-publishing authority.

## Surprises

No safe full unit suite exists in this owner. Parent approved focused-only review with this exact full-check limitation recorded privately.

## Verification

- Exact authorized focused command before source fix: 1 failed, 1 passed in 1.01s. Success payload characterization passes; error regression fails at `assert attachment.closed` (False) after the fake send raises the same RuntimeError instance.
- Same entire new file after ExitStack cleanup: 2 passed in 0.28s. Checks include attachment names/content, JSON system fixture, subject/Reply-To/custom kwargs, closure of both buffers, and unchanged exception identity. CPython 3.13.15 / pytest 9.1.1; no actual API, logs, credentials or host inventory used.
- Full legacy pytest remains explicitly unsafe/unrun under coordinator instruction; not silently skipped or represented as pass. No prior tracked test authority or hosted CI was invented.
- Documented non-publishing `uv build`: exit 0, creates dist/issue_reporter-0.1.2.tar.gz and dist/issue_reporter-0.1.2-py3-none-any.whl. No upload.
- Tracked pyproject.toml/uv.lock diffs empty; isolated pytest --no-project does not resolve package dependencies. Pre-build lock SHA256 D6A7A4DD3A8281777C38DBCA27FFDFB96C44D1F79985145DB550E5E3E81A6702; verify stable after build. No active commit hook. Source CRLF retained.
- Direct real-source import generates issue_reporter/__pycache__/issue_reporter.cpython-313.pyc in this new worktree; it is an excluded untracked test output, not a source slice or canonical file. Commit only named source/test/note. Build outputs are excluded too.

## Next step

Return the complete actual-master-to-rebased-head source/test/note diff and exact head to coordinator before publication. Keep PR #1 remote unchanged; no push/merge/model or full local CI. Actual final-head eight-test hosted green and Claude review remain separate gates.
