# SIS 2 CI Pipeline with Python and pytest-playwright

This guide adapts the supplied TypeScript-oriented CI instructions to the Python test suite in `assignments/Assignment2`. The workflow is `.github/workflows/playwright.yml` at the repository root.

## How the Python pipeline maps to the assignment

| Goal | Python implementation |
| --- | --- |
| Run on pushes and pull requests | GitHub Actions `push` and `pull_request` triggers |
| Cache dependencies | `actions/setup-python` pip cache, keyed by `requirements.txt` |
| Install browsers | `python -m playwright install --with-deps chromium` on each run; browser caching is omitted because Playwright advises it often costs as much to restore as to download |
| Run the complete suite | `pytest` split into four groups with `pytest-split`; no test-name filters |
| Keep reports and debugging evidence | Per-group self-contained HTML and JUnit reports, plus failure traces, screenshots, and videos; artifacts are retained for 14 days |
| One-group timing baseline | Start `workflow_dispatch` and choose `1` under **groups**; choose `4` for the parallel run |

The workflow installs the packages listed in `assignments/Assignment2/requirements.txt`. The pytest configuration already supplies the base URL.

## Run locally

From the repository root:

```bash
python -m pip install -r assignments/Assignment2/requirements.txt
python -m playwright install --with-deps chromium
cd assignments/Assignment2
pytest
```

To generate local HTML/JUnit reports and keep failure artifacts:

```bash
mkdir -p reports
pytest --tracing=retain-on-failure --screenshot=only-on-failure --video=retain-on-failure \
  --html=reports/report.html --self-contained-html --junitxml=reports/junit.xml
```

`pytest-split` requires both `--splits` and `--group`. For example, to run group 2 of 4 locally:

```bash
pytest --splits=4 --group=2
```

## Reports and Python-specific differences

Each GitHub matrix job uploads its own report and test-results artifacts. pytest-html does not merge these reports into one dashboard in this setup. Pytest also has no direct equivalent of Playwright Test's `forbidOnly`; `test.only` is not a pytest selection API. The pipeline therefore uses pytest's normal collection and explicit group selection.

The guide's TypeScript `playwright.config.ts`, `merge.config.ts`, `npx playwright test --shard`, and blob-report merger are specific to the JavaScript/TypeScript Playwright Test runner. Do not copy those commands into this Python project.

## Record the GitHub evidence

After pushing the workflow to GitHub:

1. Open **Actions** and check that push and pull-request runs complete.
2. Confirm the pip cache is restored on a later run and that each job uploads report and test-results artifacts.
3. Run the workflow manually once with one group and again with four groups. Record each run URL, total workflow duration, and slowest test job duration.
4. Add a timing table and conclusion to the repository README using those measured results. Do not estimate or invent timings.
5. Generate the status badge from the Actions page after a run succeeds on the default branch; use the repository's actual owner and name.

Trace files can contain page content and test data. Keep them in trusted GitHub artifacts and avoid uploading traces with real credentials to public trace viewers.
