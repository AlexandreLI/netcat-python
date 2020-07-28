import requests
import sys

if len(sys.argv) != 2:
    print("Use mode: python3 methods_allowed.py path/filename.txt")
else:
    with open(sys.argv[1], "r") as f:
        for u in f:
            url = u.strip("\n")
            result = requests.options(url)
            if "Allow" in result.headers:
                print("URL: %s --- Methods Allowed: %s" % (url, result.headers["Allow"]))
