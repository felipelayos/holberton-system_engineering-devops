#!/usr/bin/python3
"""API Module"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    to_json = {}
    for user in users:
        tasks = []
        for key in todos:
            if key["userId"] == user["id"]:
                my_dict = {}
                my_dict["task"] = key.get("title")
                my_dict["completed"] = key.get("completed")
                my_dict["username"] = user.get("username")
                tasks.append(my_dict)
        to_json[user["id"]] = tasks
    with open("todo_all_employees.json", "w") as file:
        json.dump(to_json, file)
