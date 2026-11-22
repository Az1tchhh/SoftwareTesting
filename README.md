# SoftwareTesting

## Assignment 2: Playwright with Python

The end-to-end tests are in [`assignments/Assignment2`](assignments/Assignment2). They use Python, pytest, and `pytest-playwright` against the Practice Software Testing demo site.

Install and run locally from the repository root:

```bash
python -m pip install -r assignments/Assignment2/requirements.txt
python -m playwright install chromium
cd assignments/Assignment2
pytest
```

## CI

**CI system:** GitHub Actions. The pipeline lives at [`.github/workflows/playwright.yml`](.github/workflows/playwright.yml) and runs on every push and pull request.

[![Playwright Python Tests](https://github.com/Az1tchhh/SoftwareTesting/actions/workflows/playwright.yml/badge.svg?branch=main)](https://github.com/Az1tchhh/SoftwareTesting/actions/workflows/playwright.yml)

For the Python version of the assignment, see the [pytest-playwright CI guide](assignments/sis2/Python_Pytest_Playwright_CI_Guide.md). The supplied DOCX describes the JavaScript/TypeScript Playwright Test runner, so its commands do not apply directly to this Python project.

The submitted screenshots and their findings are summarized in the [CI pipeline report](assignments/sis2/SIS2_CI_Pipeline_Report.docx).

It sets up Python, restores pip's dependency cache, installs the project requirements and Chromium system dependencies, then runs the complete pytest suite in four parallel groups. Each group uploads its HTML report, JUnit XML, and failure diagnostics (trace, screenshot, and video) for 14 days. Use the `workflow_dispatch` input to run one group as a timing baseline or all four groups for the parallel run.

The Python runner does not provide Playwright Test's `forbidOnly`, blob reporter, or `merge-reports` command. Pytest collection does not treat `test.only` as a filter, and each parallel group therefore keeps its own HTML and JUnit report. There is no single merged HTML report.

The workflow creates CI evidence, but the timing table and repository badge need real GitHub runs and the repository's owner/name. Add those measured run links and the generated badge after pushing this repository to GitHub.

### Local CI-style run

```bash
python -m pip install -r assignments/Assignment2/requirements.txt
python -m playwright install chromium
cd assignments/Assignment2
mkdir -p reports
pytest --tracing=retain-on-failure --screenshot=only-on-failure --video=retain-on-failure \
  --html=reports/report.html --self-contained-html --junitxml=reports/junit.xml
```
