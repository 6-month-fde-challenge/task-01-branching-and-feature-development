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
[main (root-commit) 4dc5c45] Add project scaffold with gitignore and environment template
 2 files changed, 24 insertions(+)
 create mode 100644 .env.example
 create mode 100644 .gitignore

$ git add config.py input_variables.py
warning: in the working copy of 'config.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add configuration module and numeric input handling"
[main e2c3e7d] Add configuration module and numeric input handling
 2 files changed, 32 insertions(+)
 create mode 100644 config.py
 create mode 100644 input_variables.py

$ git add login.py profile.py
warning: in the working copy of 'profile.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add login prompt and profile resolution modules"
[main d4c57ca] Add login prompt and profile resolution modules
 2 files changed, 33 insertions(+)
 create mode 100644 login.py
 create mode 100644 profile.py

$ git add addition_module.py subtract_module.py multiply_module.py division_module.py
warning: in the working copy of 'addition_module.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'division_module.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'multiply_module.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'subtract_module.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add arithmetic modules for addition, subtraction, multiplication and division"
[main 76a610f] Add arithmetic modules for addition, subtraction, multiplication and division
 4 files changed, 59 insertions(+)
 create mode 100644 addition_module.py
 create mode 100644 division_module.py
 create mode 100644 multiply_module.py
 create mode 100644 subtract_module.py

$ git add calculator.py dashboard.py
warning: in the working copy of 'calculator.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'dashboard.py', LF will be replaced by CRLF the next time Git touches it

$ git commit -m "Add calculator entry point and dashboard report"
[main 7237e61] Add calculator entry point and dashboard report
 2 files changed, 28 insertions(+)
 create mode 100644 calculator.py
 create mode 100644 dashboard.py

$ git log --oneline
7237e61 Add calculator entry point and dashboard report
76a610f Add arithmetic modules for addition, subtraction, multiplication and division
d4c57ca Add login prompt and profile resolution modules
e2c3e7d Add configuration module and numeric input handling
4dc5c45 Add project scaffold with gitignore and environment template

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
[feature-login 1283846] Add credential validation and is_authenticated helper to login
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
[feature-profile 00d42d4] Add get_display_name and authentication gate to profile
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
[feature-dashboard 8ee8729] Add render_dashboard with aligned summary rows and signed-in header
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
*   be453de (HEAD -> main) Merge feature-dashboard into main
|\  
| * 8ee8729 (feature-dashboard) Add render_dashboard with aligned summary rows and signed-in header
|/  
*   21e1eef Merge feature-profile into main
|\  
| * 00d42d4 (feature-profile) Add get_display_name and authentication gate to profile
|/  
*   eb83da5 Merge feature-login into main
|\  
| * 1283846 (feature-login) Add credential validation and is_authenticated helper to login
|/  
* 7237e61 Add calculator entry point and dashboard report
* 76a610f Add arithmetic modules for addition, subtraction, multiplication and division
* d4c57ca Add login prompt and profile resolution modules
* e2c3e7d Add configuration module and numeric input handling
* 4dc5c45 Add project scaffold with gitignore and environment template

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
[feature-experimental 42bfa3e] Align dashboard value column with the border width
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
Deleted branch feature-experimental (was 42bfa3e).

$ git branch
  feature-dashboard
  feature-login
  feature-profile
* main

$ git log --merges --oneline
9e804f3 Merge feature-experimental into main
be453de Merge feature-dashboard into main
21e1eef Merge feature-profile into main
eb83da5 Merge feature-login into main

```

---

## 2. Final branch list

```console
$ git branch -a
  feature-dashboard
  feature-login
  feature-profile
* main
```

---

## 3. Final git history

```console
$ git log --graph --oneline --all --decorate
*   9e804f3 (HEAD -> main) Merge feature-experimental into main
|\  
| * 42bfa3e Align dashboard value column with the border width
|/  
*   be453de Merge feature-dashboard into main
|\  
| * 8ee8729 (feature-dashboard) Add render_dashboard with aligned summary rows and signed-in header
|/  
*   21e1eef Merge feature-profile into main
|\  
| * 00d42d4 (feature-profile) Add get_display_name and authentication gate to profile
|/  
*   eb83da5 Merge feature-login into main
|\  
| * 1283846 (feature-login) Add credential validation and is_authenticated helper to login
|/  
* 7237e61 Add calculator entry point and dashboard report
* 76a610f Add arithmetic modules for addition, subtraction, multiplication and division
* d4c57ca Add login prompt and profile resolution modules
* e2c3e7d Add configuration module and numeric input handling
* 4dc5c45 Add project scaffold with gitignore and environment template
```

---

## 4. Merge commits

```console
$ git log --merges --oneline
9e804f3 Merge feature-experimental into main
be453de Merge feature-dashboard into main
21e1eef Merge feature-profile into main
eb83da5 Merge feature-login into main
```

---

## 5. Working tree state

```console
$ git status
On branch main
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
## Note on capture timing

The history blocks above were captured one commit before the final documentation
commit that added them, so the newest commit shown here is the last code/merge
commit rather than this documentation commit itself. Everything else - branches,
merges, the deletion and the run output - is exact.
