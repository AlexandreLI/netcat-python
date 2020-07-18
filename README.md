# Scripts-Python-Tools

## Introduction
These scripts are to help in some phases of Pentest or to handle with some aplication.

## The Goals of Each Script

### bludit_brute_force
This script try to brute force the Bludit aplication to get access to the login page. 
It'll work until 3.9.0 version of Bludit. I found this script and modify for my own will. 

Use mode: python3 bludit_brute_force.py 127.0.0.1 /admin/login admin wordlist.txt

The source of the Bludit script is in the link below:

https://rastating.github.io/bludit-brute-force-mitigation-bypass/

### elasticsearch_backup
This script automate the backup from Elasticsearch taking vantage of the following tool:
https://github.com/elasticsearch-dump/elasticsearch-dump

### reverse_shell
This script get a reverse shell from windows and linux OS. 
You can use this script in combination with Netcat to receive the reverse shell.

To make a Windows OS or Linux OS executable, you can use pyinstaller 

Example:

pip install pyinstaller

pyinstaller.exe .\reverse_tcp.py --onefile --windowed 