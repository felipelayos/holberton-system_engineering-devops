#!/usr/bin/python3
import requests
import sys
import json

if __name__ == "__main__":

    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(sys.argv[1]))

    emp_username = user_info.json()["username"]

    todos_list = json.loads(data.text)

    my_dictio = {}
    my_format = []

    for key in todos_list:
        task_dictionary = {}
        task_dictionary.append('"task": {}, "completed": {}, "username": "{}"')
        .format(key['title'], key['completed'], emp_username)
        my_format.append(task_dictionary)

    my_dictio.append("{}": my_format).format(sys.argv[1])

    with open('{}.json', 'w').format(sys.argv[1]) as file:
        json.dump(my_dictio, file, indent=4)
