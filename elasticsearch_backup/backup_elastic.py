import subprocess
import requests

request = requests.get("http://exemplo.com:9200/_all")  # change me
indexs = list(request.json())

for i in indexs:
    subprocess.run(["docker", "run", "--rm", "-ti", "taskrabbit/elasticsearch-dump",
                    "--input=http://exemplo.com:9200/{}".format(i),  # change me
                    "--output=http://exemplo.com:9200/{}".format(i),  # change me
                    "--type=data"])

print("############## BACKUP COMPLETE ###############")
