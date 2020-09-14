#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":

    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(sys.argv[1])).json()
    todos_list = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(sys.argv[1])).json()

    done_taks = 0
    total_taks = 0

    emp_name = user_info["name"]

    for key in todos_list:
        if key['completed'] is True:
            done_taks += 1
        total_taks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, done_taks, total_taks))

    for key in todos_list:
        if key['completed'] is True:
            print("\t {}".format(key['title']))
