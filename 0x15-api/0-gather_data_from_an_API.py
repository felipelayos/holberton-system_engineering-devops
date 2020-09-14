#!/usr/bin/python3
"""API Module"""
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

    emp_name = user_info.json()["name"]

    todos_list = json.loads(data.text)

    for key in todos_list:
        if key['completed'] is True:
            done_taks += 1
        total_taks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, done_taks, total_taks))

    for key in todos_list:
        if key['completed'] is True:
            print("\t {}".format(key['title']))
