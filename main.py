import requests
import json
import os
import argparse


taskList = [
    {
        "url" : "/users",
        "filename" : "/users.json"
    },
    {
        "url" : "/tasks",
        "filename" : "/tasks.json"
    },
    {
        "url" : "/history",
        "filename" : "/history.json"
    }
]

def saveFileToJSON (data, fileName):
    with open(contestName + fileName, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def getData (task):
    data = requests.get(url = baseUrl + task["url"]).json()
    saveFileToJSON(data, task["filename"])
    print("Got data from " + task["url"])
    return data

parser = argparse.ArgumentParser()
parser.add_argument('contest_name',type=str)
parser.add_argument('base_url',type=str)
args = parser.parse_args()

baseUrl = args.base_url
contestName = args.contest_name

try:
    # Create target Directory
    os.mkdir(contestName)
    print("Directory " , contestName ,  " created ") 
except FileExistsError:
    print("Directory " , contestName ,  " already exists")


for task in taskList:
    getData(task)

    