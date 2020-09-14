#!/usr/bin/python3
import csv
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

    with open('2.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for key in todos_list:
            writer.writerow(
                [str(sys.argv[1]),
                 emp_username,
                 key['completed'],
                 key['title']])
