## Reverse TCP shell
This script get a reverse shell from windows and linux OS. You can use this script in combining with Netcat to receive the reverse shell.

### Requirements
Python version 3 or later. 

### How to use

You can use with python interpreter, example:

```diff
+ python3 reverse_tcp.py 
```

To make a Windows OS or Linux OS executable, 
you can use pyinstaller.

Example:

```diff
+ pip install pyinstaller
```
```diff
+ pyinstaller.exe .\reverse_tcp.py --onefile --windowed
```

