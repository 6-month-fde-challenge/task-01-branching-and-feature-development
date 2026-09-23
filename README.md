# Task 1 - Branching and Feature Development

A small multi-module Python calculator project used to demonstrate a complete
Git branching workflow: a `main` branch, three feature branches, a real change
on every feature branch, and three `--no-ff` merges back into `main`.

> **Everything the reviewer needs is committed on the default branch `main`.**
> The blocks below are verbatim terminal output captured while this repository
> was built - the commands, their real output, the branch listings, the merge
> commits and the full `git log --graph`.

---

## 1. What this project is

`dashboard.py` is the final integration point. It pulls results from
`calculator.py`, which in turn uses four arithmetic modules. Each arithmetic
module is guarded by an API key (`config.py`) and by the logged-in profile
(`profile.py`), so the project exercises configuration, login, profile and
reporting code paths.

| File | Purpose |
| --- | --- |
| `config.py` | Reads `API_KEY` from the environment, with a safe demo fallback |
| `.env.example` | Template for a local `.env` file |
| `input_variables.py` | Reads the two numbers (falls back to defaults when stdin is empty) |
| `login.py` | Reads the credentials, validates them, exposes `is_authenticated()` |
| `profile.py` | Derives `profile_name`, exposes `get_display_name()` |
| `addition_module.py` | `addition(a, b)` |
| `subtract_module.py` | `subtract(a, b)` |
| `multiply_module.py` | `multiply(a, b)` |
| `division_module.py` | `division(a, b)`, guards against division by zero |
| `calculator.py` | Entry point that computes all four results |
| `dashboard.py` | Final report, `render_dashboard()` |

---

## 2. How to run

```bash
git clone https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development.git
cd task-01-branching-and-feature-development
python dashboard.py
```

No dependencies and no setup are required - the project runs on a fresh clone.
Optionally copy `.env.example` to `.env` and set your own `API_KEY`; otherwise
`config.py` falls back to a harmless demo value.

### Real output

The project prompts for input, so it was run with no stdin at all to prove it
never crashes in a non-interactive environment:

```console
$ python dashboard.py < /dev/null
Enter a number 1 :    -> no input available, using default: 10
Enter a number 2 :    -> no input available, using default: 5
Enter username :    -> no input available, using default: veerandra
Enter password :    -> no input available, using default: demo-password
API key present and logged in as veerandra
API key present and logged in as veerandra
API key present and logged in as veerandra
API key present and logged in as veerandra
*************************************************
|                   DASHBOARD                   |
|            Signed in as Veerandra             |
*************************************************
| Result of addition                         15 |
| Result of subtraction                       5 |
| Result of multiplication                   50 |
| Result of division                        2.0 |
*************************************************
```

Run interactively (`python dashboard.py`) it uses the numbers and credentials
you type instead of the defaults.

---

## 3. Branch strategy

Four branches were used. `main` is the default branch and holds the final,
fully merged code. Each feature was developed on its own branch and merged back
with `git merge --no-ff`, so every feature appears in the history as a visible
merge commit.

| Branch | What it contains | GitHub link |
| --- | --- | --- |
| `main` | Scaffold, config, input handling, arithmetic modules, entry points, plus all three merged features. **Default branch.** | [tree/main](https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/main) |
| `feature-login` | `login.py`: password-length validation and the `is_authenticated()` helper | [tree/feature-login](https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/feature-login) |
| `feature-profile` | `profile.py`: `get_display_name()` and an authentication gate around `profile_name` | [tree/feature-profile](https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/feature-profile) |
| `feature-dashboard` | `dashboard.py`: `render_dashboard()` with aligned summary rows and a signed-in header | [tree/feature-dashboard](https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/feature-dashboard) |

A fifth, throwaway branch `feature-experimental` was created, committed on,
merged and then **deleted** with `git branch -d` to demonstrate branch deletion.
It no longer exists - the captured deletion output is in section 7. The three
required feature branches are deliberately kept alive and pushed so the reviewer
can open each one.

```text
                        feature-login        feature-profile      feature-dashboard
                             |                     |                     |
 main --o--o--o--o--o--------M---------------------M---------------------M--> default
                             ^                     ^                     ^
                          --no-ff               --no-ff               --no-ff
```

---

## 4. Full git history

Verbatim output of `git log --graph --oneline --all --decorate`.
*Note: this capture was taken one commit before the final documentation
commit that pastes it in, so the newest commit shown below is the
commit immediately preceding this file's last update.*

```console
$ git log --graph --oneline --all --decorate
* ba5dfbc (HEAD -> main, origin/main) Add README, git evidence transcript and submission links
*   1d00694 Merge feature-experimental into main
|\  
| * ba1ea27 Align dashboard value column with the border width
|/  
*   e62f09a Merge feature-dashboard into main
|\  
| * d638b95 (origin/feature-dashboard, feature-dashboard) Add render_dashboard with aligned summary rows and signed-in header
|/  
*   14d657d Merge feature-profile into main
|\  
| * 1ae46c4 (origin/feature-profile, feature-profile) Add get_display_name and authentication gate to profile
|/  
*   b478781 Merge feature-login into main
|\  
| * 95ea76a (origin/feature-login, feature-login) Add credential validation and is_authenticated helper to login
|/  
* 40b639b Add calculator entry point and dashboard report
* 4e921f5 Add arithmetic modules for addition, subtraction, multiplication and division
* 4394a59 Add login prompt and profile resolution modules
* b04de7b Add configuration module and numeric input handling
* 0da73ab Add project scaffold with gitignore and environment template
```

Linear view of `main`:

```console
$ git log --oneline
ba5dfbc Add README, git evidence transcript and submission links
1d00694 Merge feature-experimental into main
ba1ea27 Align dashboard value column with the border width
e62f09a Merge feature-dashboard into main
d638b95 Add render_dashboard with aligned summary rows and signed-in header
14d657d Merge feature-profile into main
1ae46c4 Add get_display_name and authentication gate to profile
b478781 Merge feature-login into main
95ea76a Add credential validation and is_authenticated helper to login
40b639b Add calculator entry point and dashboard report
4e921f5 Add arithmetic modules for addition, subtraction, multiplication and division
4394a59 Add login prompt and profile resolution modules
b04de7b Add configuration module and numeric input handling
0da73ab Add project scaffold with gitignore and environment template
```

---

## 5. Merge evidence

Each of the three required features produced a real merge commit on `main`.
`--no-ff` was used every time, so no merge was fast-forwarded away:

```console
$ git log --merges --oneline
1d00694 Merge feature-experimental into main
e62f09a Merge feature-dashboard into main
14d657d Merge feature-profile into main
b478781 Merge feature-login into main
```

Branches, local and remote:

```console
$ git branch -a
  feature-dashboard
  feature-login
  feature-profile
* main
  remotes/origin/feature-dashboard
  remotes/origin/feature-login
  remotes/origin/feature-profile
  remotes/origin/main
```

---

## 6. Command walkthrough

Every command that built this repository, in order, with its real output.

### 6.1 Repository setup and the base commits on `main`

```console
$ mkdir task-01-branching-and-feature-development
$ cd task-01-branching-and-feature-development

$ git init -b main
Initialized empty Git repository in C:/Users/asus/Desktop/work/6-month-fde-challenge/03_git_and_git_hub/task-01-branching-and-feature-development/.git/

$ git config user.name "veerandra7"

$ git config user.email "veerandra.data@gmail.com"

$ git status --short
?? .env.example
?? .gitignore

$ git add .gitignore .env.example
warning: in the working copy of '.env.example', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add project scaffold with gitignore and environment template"
[main (root-commit) 0da73ab] Add project scaffold with gitignore and environment template
 2 files changed, 24 insertions(+)
 create mode 100644 .env.example
 create mode 100644 .gitignore

$ git add config.py input_variables.py
warning: in the working copy of 'config.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add configuration module and numeric input handling"
[main b04de7b] Add configuration module and numeric input handling
 2 files changed, 32 insertions(+)
 create mode 100644 config.py
 create mode 100644 input_variables.py

$ git add login.py profile.py
warning: in the working copy of 'profile.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add login prompt and profile resolution modules"
[main 4394a59] Add login prompt and profile resolution modules
 2 files changed, 33 insertions(+)
 create mode 100644 login.py
 create mode 100644 profile.py

$ git add addition_module.py subtract_module.py multiply_module.py division_module.py
warning: in the working copy of 'addition_module.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'division_module.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'multiply_module.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'subtract_module.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add arithmetic modules for addition, subtraction, multiplication and division"
[main 4e921f5] Add arithmetic modules for addition, subtraction, multiplication and division
 4 files changed, 59 insertions(+)
 create mode 100644 addition_module.py
 create mode 100644 division_module.py
 create mode 100644 multiply_module.py
 create mode 100644 subtract_module.py

$ git add calculator.py dashboard.py
warning: in the working copy of 'calculator.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'dashboard.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add calculator entry point and dashboard report"
[main 40b639b] Add calculator entry point and dashboard report
 2 files changed, 28 insertions(+)
 create mode 100644 calculator.py
 create mode 100644 dashboard.py

$ git log --oneline
40b639b Add calculator entry point and dashboard report
4e921f5 Add arithmetic modules for addition, subtraction, multiplication and division
4394a59 Add login prompt and profile resolution modules
b04de7b Add configuration module and numeric input handling
0da73ab Add project scaffold with gitignore and environment template

$ git branch
* main

```

### 6.2 `feature-login` - branch, commit, merge

```console
$ git checkout -b feature-login
Switched to a new branch 'feature-login'

$ git status --short
 M login.py

$ git diff --stat
warning: in the working copy of 'login.py', LF will be replaced by CRLF the next time Git touches it
 login.py | 19 ++++++++++++++++++-
 1 file changed, 18 insertions(+), 1 deletion(-)

$ git add login.py
warning: in the working copy of 'login.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add credential validation and is_authenticated helper to login"
[feature-login 95ea76a] Add credential validation and is_authenticated helper to login
 1 file changed, 18 insertions(+), 1 deletion(-)

$ git checkout main
Switched to branch 'main'

$ git merge --no-ff feature-login -m "Merge feature-login into main"
Merge made by the 'ort' strategy.
 login.py | 19 ++++++++++++++++++-
 1 file changed, 18 insertions(+), 1 deletion(-)

```

### 6.3 `feature-profile` - branch, commit, merge

```console
$ git switch -c feature-profile
Switched to a new branch 'feature-profile'

$ git status --short
 M profile.py

$ git add profile.py
warning: in the working copy of 'profile.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add get_display_name and authentication gate to profile"
[feature-profile 1ae46c4] Add get_display_name and authentication gate to profile
 1 file changed, 12 insertions(+), 2 deletions(-)

$ git switch main
Switched to branch 'main'

$ git merge --no-ff feature-profile -m "Merge feature-profile into main"
Merge made by the 'ort' strategy.
 profile.py | 14 ++++++++++++--
 1 file changed, 12 insertions(+), 2 deletions(-)

```

### 6.4 `feature-dashboard` - branch, commit, merge

```console
$ git switch -c feature-dashboard
Switched to a new branch 'feature-dashboard'

$ git status --short
 M dashboard.py

$ git add dashboard.py
warning: in the working copy of 'dashboard.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add render_dashboard with aligned summary rows and signed-in header"
[feature-dashboard d638b95] Add render_dashboard with aligned summary rows and signed-in header
 1 file changed, 35 insertions(+), 7 deletions(-)

$ git switch main
Switched to branch 'main'

$ git merge --no-ff feature-dashboard -m "Merge feature-dashboard into main"
Merge made by the 'ort' strategy.
 dashboard.py | 42 +++++++++++++++++++++++++++++++++++-------
 1 file changed, 35 insertions(+), 7 deletions(-)

$ git branch
  feature-dashboard
  feature-login
  feature-profile
* main

```

---

## 7. Branch deletion

`feature-experimental` was created, committed on, merged into `main` and then
deleted. This is the captured proof of branch creation *and* branch deletion:

```console
$ git branch feature-experimental

$ git switch feature-experimental
Switched to branch 'feature-experimental'

$ git diff --unified=0
warning: in the working copy of 'dashboard.py', LF will be replaced by CRLF the next time Git touches it
diff --git a/dashboard.py b/dashboard.py
index 2b6a6af..de79ee2 100644
--- a/dashboard.py
+++ b/dashboard.py
@@ -18 +18 @@ def format_row(label, value):
-    return "| {:<28}{:>16} |".format(label, value)
+    return "| {:<28}{:>17} |".format(label, value)

$ git add dashboard.py
warning: in the working copy of 'dashboard.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Align dashboard value column with the border width"
[feature-experimental ba1ea27] Align dashboard value column with the border width
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git switch main
Switched to branch 'main'

$ git merge --no-ff feature-experimental -m "Merge feature-experimental into main"
Merge made by the 'ort' strategy.
 dashboard.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git branch --merged
  feature-dashboard
  feature-experimental
  feature-login
  feature-profile
* main

$ git branch -d feature-experimental
Deleted branch feature-experimental (was ba1ea27).

$ git branch
  feature-dashboard
  feature-login
  feature-profile
* main

```

The three required feature branches (`feature-login`, `feature-profile`,
`feature-dashboard`) were intentionally **not** deleted, so they stay visible on
GitHub for review.

---
## 8. Publishing and remote verification

```console
$ git status --short
?? GIT_EVIDENCE.md
?? README.md
?? submission_links.txt

$ git add README.md GIT_EVIDENCE.md submission_links.txt
warning: in the working copy of 'GIT_EVIDENCE.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'submission_links.txt', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add README, git evidence transcript and submission links"
[main ba5dfbc] Add README, git evidence transcript and submission links
 3 files changed, 884 insertions(+)
 create mode 100644 GIT_EVIDENCE.md
 create mode 100644 README.md
 create mode 100644 submission_links.txt

$ gh repo create 6-month-fde-challenge/task-01-branching-and-feature-development --public -d "Task 1 - Git branching and feature development: main plus feature-login, feature-profile and feature-dashboard, each merged into main with full visible history." --source=. --remote=origin --push
https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development
To https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development.git
 * [new branch]      HEAD -> main
branch 'main' set up to track 'origin/main'.

$ git push -u origin --all
To https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development.git
 * [new branch]      feature-dashboard -> feature-dashboard
 * [new branch]      feature-login -> feature-login
 * [new branch]      feature-profile -> feature-profile
branch 'main' set up to track 'origin/main'.
branch 'feature-dashboard' set up to track 'origin/feature-dashboard'.
branch 'feature-login' set up to track 'origin/feature-login'.
branch 'feature-profile' set up to track 'origin/feature-profile'.

$ git ls-remote --heads origin
d638b95fca50dd7466122861d554076828b5a973	refs/heads/feature-dashboard
95ea76a1deff225a2bc9079e0781ccbcde111f06	refs/heads/feature-login
1ae46c4085b18f4ddb2c7d7f2be74d3576fc7f58	refs/heads/feature-profile
ba5dfbcfa5feb30401978053cbc48c9df46f8cf9	refs/heads/main

$ gh repo view 6-month-fde-challenge/task-01-branching-and-feature-development --json defaultBranchRef
{"defaultBranchRef":{"name":"main"}}

$ git branch -a
  feature-dashboard
  feature-login
  feature-profile
* main
  remotes/origin/feature-dashboard
  remotes/origin/feature-login
  remotes/origin/feature-profile
  remotes/origin/main

```

---

## 9. Fixes applied after review feedback

The previous submission scored 8/15. Every point raised has been addressed, and
this section records exactly how.

### (a) The default branch is `main`, not `master`

The reviewer noted *"the submission was reviewed on branch master"*. This
repository was initialised with `git init -b main`, so `master` never existed at
any point:

```console
$ git init -b main
Initialized empty Git repository in .../task-01-branching-and-feature-development/.git/
```

The default branch on GitHub is confirmed to be `main`:

```console
$ gh repo view 6-month-fde-challenge/task-01-branching-and-feature-development --json defaultBranchRef
{"defaultBranchRef":{"name":"main"}}
```

### (b) BLOCKER - the `api_key` import crash is fixed

The reviewer reported: *"subtract_module.py and multiply_module.py import
api_key from Python's secrets module, but that module does not define api_key,
so running dashboard.py will fail."*

**Root cause.** The old project kept the key in a local file named `secrets.py`
and did `from secrets import api_key`. That filename shadows Python's
standard-library `secrets` module - and, critically, `secrets.py` was listed in
`.gitignore`, so it was **never pushed to GitHub**. On a fresh clone the local
file was missing, the import silently fell through to the standard-library
`secrets` module, which defines no `api_key`, and `dashboard.py` died with
`ImportError: cannot import name 'api_key' from 'secrets'`.

**Fix.** `secrets.py` is gone for good and is not recreated anywhere.
Configuration now lives in `config.py`, which reads the key from the environment
and falls back to a harmless demo value so a fresh clone runs with zero setup:

```python
# config.py
import os

api_key = os.getenv("API_KEY", "demo-api-key-not-a-real-secret")
```

All four arithmetic modules now use `from config import api_key`. `config.py` is
committed and is **not** gitignored - nothing the code imports is ignored.
`.env.example` documents the real variable, and only the real `.env` file is
ignored.

### (c) MINOR - `profile_name` can no longer be undefined

The reviewer reported that `profile_name` was only assigned inside an `if`
block, so empty input left it undefined and every importing module failed. It is
now initialised before the branch:

```python
# profile.py
profile_name = ""

if is_authenticated(user_name, pass_word):
    profile_name = user_name
```

### (d) The features are visibly merged into `main`

The reviewer asked to *"push feature-login, feature-profile, and
feature-dashboard, and merge each feature into main with visible commits in the
Git history"*. All three branches are pushed, and each was merged with
`git merge --no-ff`, producing the three merge commits shown in section 5 and in
the graph in section 4.

### (e) Input handling no longer crashes without a terminal

The `input()` calls in `input_variables.py` and `login.py` are wrapped so the
program falls back to documented defaults instead of raising `EOFError` when it
is run with no stdin.

---

## 10. Requirement checklist

| Assignment requirement | Where it is evidenced |
| --- | --- |
| Project with a `main` branch | Sections 3 and 9(a) |
| At least three feature branches | Section 3 - `feature-login`, `feature-profile`, `feature-dashboard` |
| A small change in each branch | Sections 6.2, 6.3, 6.4 - each shows the edit and its commit |
| Merge all three features into `main` | Section 5 - three `--no-ff` merge commits |
| Branch creation | Sections 6.2-6.4 (`git checkout -b`, `git switch -c`, `git branch`) |
| Checkout / switch | Sections 6.2-6.4 (`git checkout`, `git switch`) |
| Commits | Section 6 - descriptive, imperative commit messages |
| Merging | Sections 4, 5 and 6 |
| **Branch deletion** | Section 7 - `git branch -d feature-experimental` with its output |
| Final git history | Section 4 - `git log --graph --oneline --all --decorate` |
| Pushed to a public GitHub repo | Section 8 and `submission_links.txt` |

---

## 11. Links

- Repository: https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development
- `main`: https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/main
- `feature-login`: https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/feature-login
- `feature-profile`: https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/feature-profile
- `feature-dashboard`: https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development/tree/feature-dashboard

A raw, unedited copy of the whole terminal session is in
[`GIT_EVIDENCE.md`](GIT_EVIDENCE.md), and the links are also in
[`submission_links.txt`](submission_links.txt).

---

*Author: veerandra7 (veerandra.data@gmail.com)*
