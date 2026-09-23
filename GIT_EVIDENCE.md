# Git evidence - raw terminal capture

This file is the unedited companion to `README.md`. Every block below is real
terminal output captured while this repository was built, in the order it was
produced. Nothing here is retyped or reconstructed.

- Repository: https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development
- Default branch: `main`
- Author: veerandra7 (veerandra.data@gmail.com)

---

## 1. Complete session transcript

Repository creation, the five base commits on `main`, the three feature branches
and their `--no-ff` merges, and the creation, merge and deletion of the
throwaway `feature-experimental` branch:

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

$ git log --oneline --graph --all --decorate
*   e62f09a (HEAD -> main) Merge feature-dashboard into main
|\  
| * d638b95 (feature-dashboard) Add render_dashboard with aligned summary rows and signed-in header
|/  
*   14d657d Merge feature-profile into main
|\  
| * 1ae46c4 (feature-profile) Add get_display_name and authentication gate to profile
|/  
*   b478781 Merge feature-login into main
|\  
| * 95ea76a (feature-login) Add credential validation and is_authenticated helper to login
|/  
* 40b639b Add calculator entry point and dashboard report
* 4e921f5 Add arithmetic modules for addition, subtraction, multiplication and division
* 4394a59 Add login prompt and profile resolution modules
* b04de7b Add configuration module and numeric input handling
* 0da73ab Add project scaffold with gitignore and environment template

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

$ git log --merges --oneline
1d00694 Merge feature-experimental into main
e62f09a Merge feature-dashboard into main
14d657d Merge feature-profile into main
b478781 Merge feature-login into main

```

---

## 2. Final branch list

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

## 3. Final git history

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

---

## 4. Merge commits

```console
$ git log --merges --oneline
1d00694 Merge feature-experimental into main
e62f09a Merge feature-dashboard into main
14d657d Merge feature-profile into main
b478781 Merge feature-login into main
```

---

## 5. Working tree state

```console
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

## 6. Proof the project runs

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

---
## 7. Remote creation, push and verification

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
## 8. Fresh-clone test

The pushed repository was cloned into an empty directory and run from there, to
prove the `api_key` blocker is really gone and that no file the code imports is
gitignored:

```console
$ git clone https://github.com/6-month-fde-challenge/task-01-branching-and-feature-development.git fresh-clone
Cloning into 'fresh-clone'...

$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/feature-dashboard
  remotes/origin/feature-login
  remotes/origin/feature-profile
  remotes/origin/main

$ git rev-parse --abbrev-ref HEAD
main

$ git log --graph --oneline --all --decorate
* ba5dfbc (HEAD -> main, origin/main, origin/HEAD) Add README, git evidence transcript and submission links
*   1d00694 Merge feature-experimental into main
|\  
| * ba1ea27 Align dashboard value column with the border width
|/  
*   e62f09a Merge feature-dashboard into main
|\  
| * d638b95 (origin/feature-dashboard) Add render_dashboard with aligned summary rows and signed-in header
|/  
*   14d657d Merge feature-profile into main
|\  
| * 1ae46c4 (origin/feature-profile) Add get_display_name and authentication gate to profile
|/  
*   b478781 Merge feature-login into main
|\  
| * 95ea76a (origin/feature-login) Add credential validation and is_authenticated helper to login
|/  
* 40b639b Add calculator entry point and dashboard report
* 4e921f5 Add arithmetic modules for addition, subtraction, multiplication and division
* 4394a59 Add login prompt and profile resolution modules
* b04de7b Add configuration module and numeric input handling
* 0da73ab Add project scaffold with gitignore and environment template

$ ls -A
.env.example
.git
.gitignore
GIT_EVIDENCE.md
README.md
addition_module.py
calculator.py
config.py
dashboard.py
division_module.py
input_variables.py
login.py
multiply_module.py
profile.py
submission_links.txt
subtract_module.py

$ ls secrets.py
ls: cannot access 'secrets.py': No such file or directory

$ grep -rnE "^(from|import) secrets" *.py
(exit status 1 - no matches, nothing imports a secrets module)

$ git check-ignore -v config.py login.py profile.py calculator.py dashboard.py
(exit status 1 - no tracked source file is gitignored)

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
exit code: 0
```

---
## Note on capture timing

The history blocks above were captured one commit before the final documentation
commit that added them, so the newest commit shown here is the last code/merge
commit rather than this documentation commit itself. Everything else - branches,
merges, the deletion and the run output - is exact.
