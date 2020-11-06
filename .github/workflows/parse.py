import re
import requests
import os
import sys
import json

p = re.compile("\[[kK][bB]-(\d+)\]")

commits = json.loads(sys.argv[1])

url = "https://wiris.kanbanize.com/index.php/api/kanbanize/add_comment/"

for commit in commits:
    commit_message = commit["message"]
    commit_username = commit["author"]["username"]
    commit_url = commit["url"]

    for match in p.finditer(commit_message): 
        filtered_commit_message = p.sub("", commit_message).strip()
        taskid = match.groups()[0]
       
        # todo: add link to commit or repo and include who made the commit
        comment = f"{commit_username}: {filtered_commit_message} \n {commit_url}"
        requests.post(url, json={"taskid": taskid, "comment": comment}, headers={"apikey": os.environ["KEY_API_KANBANIZE"]})

