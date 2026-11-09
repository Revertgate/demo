# Revertgate demo

A tiny invoice module and three pull requests, each the kind a coding agent might open. All
three pass the ordinary **Tests** check. Open each PR to see what
[Revertgate](https://github.com/revertgate/revertgate) says:

| PR | What the "agent" did | Tests | Revertgate |
|---|---|---|---|
| Add discount | Changed the code and added a test that needs the change | ✅ | ✅ the tests catch this change |
| Add tax | Broke the totals, then loosened an assertion, skipped a test and swallowed the error | ✅ | ❌ blocked |
| Add tax helper | Added a function and a "test" that never calls it | ✅ | ❌ blocked |

Revertgate reverts each PR's code (not its tests) and reruns the suite. If the tests still
pass, they don't test the change.
