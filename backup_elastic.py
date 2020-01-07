import subprocess
import requests

request = requests.get("http://10.99.40.25:9200/_all")
indexs = list(request.json())

for i in indexs:
    subprocess.run(["docker", "run", "--rm", "-ti", "taskrabbit/elasticsearch-dump",
                    "--input=http://10.99.40.25:9200/{}".format(i),
                    "--output=http://10.99.40.28:9200/{}".format(i),
                    "--type=data"])

print("############## BACKUP COMPLETE ###############")
