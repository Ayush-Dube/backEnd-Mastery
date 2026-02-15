## backEnd Beginning


delete effect observation 

```python 
python -m venv <env_name>

<env_name> \Scripts\activate

deactivate

rmdir /s /q <env_name>

/s - subdirectories
It tells the command to delete all files and subdirectories within the specified directory. Without this, the command will only delete the directory if it's empty.
/q - quite mode (no promts)
```

| Step                      | 🪟 Windows (PowerShell / CMD) | 🐧 Linux (Ubuntu / Amazon Linux) | WHY difference?                             |
| ------------------------- | ----------------------------- | -------------------------------- | ------------------------------------------- |
| Check Python              | `python --version`            | `python3 --version`              | Linux me multiple python versions hote hain |
| Check venv module         | `python -m venv --help`       | `python3 -m venv --help`         | Same concept, different binary name         |
| Install venv (if missing) | Mostly preinstalled           | `sudo apt install python3-venv`  | Linux minimal installs hota hai             |
| Create venv               | `python -m venv venv`         | `python3 -m venv venv`           | Same command                                |
| Folder created            | `venv\Scripts\`               | `venv/bin/`                      | OS structure difference                     |
| Activate                  | `.\venv\Scripts\Activate`     | `source venv/bin/activate`       | Shell mechanism different                   |
| Prompt change             | `(venv) PS C:\project>`       | `(venv) user@machine:~/project$` | Visual confirmation                         |
| Check active python       | `where python`                | `which python`                   | Windows vs Unix command                     |
| Deactivate                | `deactivate`                  | `deactivate`                     | Same everywhere                             |



```bash
PS D:\backEND_ALL\using_Python\project_101a> .\.prakaENV\Scripts\activate

.\.prakaENV\Scripts\activate : File D:\backEND_ALL\using_Python\project_101a\.prakaENV\Scripts\Activate.ps1 cannot be loaded because running        
scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\.prakaENV\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

Get-ExecutionPolicy
Restricted
PS D:\backEND_ALL\using_Python\project_101a>



```

![alt text](image.png)



## Issue 1

PYTHON ERROR: Non-UTF-8 code starting with '\xff' (PowerShell Issue)

PROBLEM:
When running a Python file, error appears:

SyntaxError: Non-UTF-8 code starting with '\xff'

CAUSE:
File was created using PowerShell command:

echo "" > test.py

PowerShell '>' redirect saves files in UTF-16 LE encoding by default.
Python 3 expects source files in UTF-8 encoding.
UTF-16 files start with bytes FF FE (\xff), causing the error.

WHY test2.py WORKED:
File created using:

ni test2.py

This creates a normal empty file (UTF-8 compatible), so Python runs it.

SOLUTIONS:

1. BEST — Create Python file properly in PowerShell:

ni script.py

### or

New-Item script.py

2. Create file with UTF-8 encoding explicitly:

Set-Content script.py "" -Encoding utf8

3. Fix an existing broken file:

Get-Content test.py | Set-Content test.py -Encoding utf8

4. In VS Code:
   Bottom-right → Click Encoding → Save with Encoding → UTF-8

RULE TO REMEMBER:

PowerShell:

> redirect  → UTF-16 ❌ (causes Python error)

ni command → UTF-8 / empty ✅ (safe)

SUMMARY:
Never use `echo "" > file.py` in PowerShell for Python files.
Use `ni file.py` or save as UTF-8 instead.
