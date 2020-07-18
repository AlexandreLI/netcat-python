# Scripts-Python-Tools

## Introduction
These scripts are to help in some phases of Pentest or to handle with some aplication.

## The Goals of Each Script

### bludit_brute_force
This script try to brute force the Bludit aplication to get access to the login page. 
It'll work until 3.9.0 version of Bludit. I found this script and modify for my own will. 

To this script works you have to modify the following fields:

host = '127.0.0.1'

login_url = host + '/admin/login'

username = 'admin'

The source of the Bludit script is in the link below:

https://rastating.github.io/bludit-brute-force-mitigation-bypass/