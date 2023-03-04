# Set up Python on Mac and Windows

<!-- TOC -->

- [1. File and Author Information](#1-file-and-author-information)
- [2. Python Versions](#2-python-versions)
  - [2.1. Mac](#21-mac)
    - [2.1.1. Let `python` linked to `python3` in terminal using `alias`](#211-let-python-linked-to-python3-in-terminal-using-alias)
  - [2.2. Windows](#22-windows)
- [3. How to use Python](#3-how-to-use-python)
  - [3.1. Interactive Prompt](#31-interactive-prompt)
  - [3.2. IDLE - Integrated Development Learning Environment](#32-idle---integrated-development-learning-environment)
  - [3.3. Common IDE](#33-common-ide)
  - [3.4. Run a Python script](#34-run-a-python-script)
  - [3.5. Add comments in Python](#35-add-comments-in-python)

<!-- /TOC -->

<div style="page-break-after:always"></div>

## 1. File and Author Information

/*

- File: python setup.md
- Project: setup environment
- File Created: Thursday, 2nd March 2023 5:41:13 pm
- Author: Hanlin Gu (hg_fine_codes@163.com)

- -----

- Last Modified: Thursday, 2nd March 2023 10:19:19 pm
- Modified By: Hanlin Gu (hg_fine_codes@163.com>)
 */

## 2. Python Versions

### 2.1. Mac

In Mac computers, by default there would be `python 2.7` installed already with
the computer. To check if python is pre-installed, open terminal and key in

```terminal
python --version
```

Output

```terminal
python 2.7.10
```

First, one would like to download the latest version of python. Current, `python 3.x` is generally used.

> Python Download Page
>
> <https://www.python.org/getit/>

After the installation, in the `Application` folder, one is able to find the folder of the installed python, for example `python 3.10`.

```terminal
python3 --version
```

Output

```terminal
python 3.10.0
```

If one use `python --version`, it will still show `python 2.7.10`.

#### 2.1.1. Let `python` linked to `python3` in terminal using `alias`

```terminal
nano ~/.bash_profile
```

There are a few lines added about python at the bottom of the file. And input
the following line

```terminal
alias python=python3
```

Hit `ctrl + x` to exit, `Y` to confirm change and then hit `enter` to keep the
same file name.

If one check the `python --version`, they will get `python 3.10.0` instead.

### 2.2. Windows

During the installation, check the box `Add Python 3.10 to PATH` to allow the `python` command to work with the command prompt. Similarly, one can check the version of python by `python --version` in `cmd` or `Windows Powershell` etc.

## 3. How to use Python

### 3.1. Interactive Prompt

In `Mac` one can use `terminal` or `iTerm2` and `Windows` user can choose `cmd` or `Windows Powershell` or `Anaconda Powershell Prompt`.

```shell
python
```

Interactive prompt allows to write one line of code at a time. It's suitable for testing python command rather than writing python scripts.

### 3.2. IDLE - Integrated Development Learning Environment

By default, the IDLE interface is also only allow for one line at a time as the three arrows `>>>` in the front indicts.

If one want to write a script, click `File` and `New File` to create a blank script window.

### 3.3. Common IDE

- Sublime Text
- Atom
- PyCharm
- VS Code

Either of the IDE works great. The author uses VS Code since it's also easy to write markdown, LaTex file with it.

### 3.4. Run a Python script

In the prompt,

```shell
python file_address/file_name.py
```

Directly use `python` to open the `file_name.py` script file at the `file_address` folder.

![python script](./python%20scripts.png)

### 3.5. Add comments in Python

Add `#` sign at the front of the line of the comments, the program will not run the comments part.
