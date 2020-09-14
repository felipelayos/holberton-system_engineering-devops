#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(sys.argv[1]))

    done_taks = 0
    total_taks = 0

    emp_username = user_info.json()["username"]

    todos_list = json.loads(data.text)

    file = "" + sys.argv[1] + ".json"
    tasks = []
    to_json = {}
    for key in todos_list:
        my_dict = {}
        my_dict["task"] = key["title"]
        my_dict["completed"] = key["completed"]
        my_dict["username"] = emp_username
        tasks.append(my_dict)
    to_json[sys.argv[1]] = tasks
    with open(file, "w") as f:
        json.dump(to_json, f)
