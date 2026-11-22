# AI Use Disclosure — SIS 2 CI Pipeline

## Model

OpenAI Codex, GPT-6.

## Prompts used

1. “check SIS 2_ CI pipeline for Playwright  step-by-step guide.docx”
2. “Can we do it in python pytest-playwright? Help me do it. I am intereseted”

## AI assistance and review

The assistant reviewed the supplied guide against the repository and identified that its TypeScript commands did not match this project's Python `pytest-playwright` tests. At the user's request, it added a Python GitHub Actions workflow, pytest HTML/JUnit report dependencies, CI instructions, and artifact ignore rules. The implementation uses pytest-split to divide test collection among four workflow jobs and keeps a one-group manual run available for timing comparisons.

The workflow and documentation were prepared with AI assistance. The user should inspect the changes, push them to the SIS 2 GitHub repository, review the Actions run and artifacts, and record actual run links and timings. No GitHub run, badge status, or timing result is claimed by this disclosure. No browser tests were run by the assistant during this change.

## Important Python/TypeScript differences

The TypeScript guide's `forbidOnly`, blob reporter, and `merge-reports` steps are specific to Playwright Test. This pytest implementation uses separate HTML and JUnit artifacts for each parallel group; it does not merge them into one report.
