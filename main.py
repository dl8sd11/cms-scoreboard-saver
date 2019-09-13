import requests
import json

baseUrl = "https://cms.nehs.hc.edu.tw/rank/34/"

taskList = [
    {
        "url" : "users",
        "filename" : "users.json"
    },
    {
        "url" : "tasks",
        "filename" : "tasks.json"
    },
    {
        "url" : "history",
        "filename" : "history.json"
    }
]

def saveFileToJSON (data, fileName):
    with open(fileName, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def getData (task):
    response = requests.get(url = baseUrl + task["url"])
    print(response.headers)
    data = response.json()
    print(task["filename"])
    saveFileToJSON(data, task["filename"])
    return data

for task in taskList:
    getData(task)

    