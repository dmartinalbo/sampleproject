import re
import requests
import os
import sys
import json

p = re.compile("\[[kK][bB]-(\d+)\]")

labels = json.loads(sys.argv[1])

url = "https://wiris.kanbanize.com/index.php/api/kanbanize/add_comment/"

for label in labels:
    o = p.finditer(label)
    for match in o: 
        filtered_commit_message = p.sub("",label).strip()
        taskid = match.groups()[0]
        
        requests.post(url, json={"taskid": taskid, "comment": filtered_commit_message}, headers={"apikey": os.environ["KEY_API_KANBANIZE"]})
#        print(taskid, filtered_commit_message)

