# COPILOT — Google Sheets sync

Downloads the published Google Sheets tab (`gid=1991175050`) to `data/google_sheets.csv`.

## Installation

Upload `.github/workflows/sync.yml` and `scripts/sync_sheet.py` to the root of your GitHub repository. Commit to the default branch (`main`).

In GitHub, open **Settings → Actions → General → Workflow permissions** and enable **Read and write permissions** if your repository allows it. Make sure branch protection permits the GitHub Actions bot to push, or adjust the workflow to create a pull request instead.

Run **Actions → Sync Google Sheets → Run workflow**. The workflow also runs daily at 00:00 UTC (07:00 WIB). Scheduled runs may be delayed by GitHub.

## Behavior

The script downloads only the specified published tab as CSV. Validation runs on Ubuntu, Windows, and macOS; the Ubuntu `save` job commits the file if it changed. Publicly published Sheets do not require API credentials. The CSV will also be visible to anyone with access to this repository; avoid storing sensitive information in a public repository.
