#!/usr/bin/python3
"""fetching json data from an api"""

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("name")
    user_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todo = user_todo.json()
    total_todo = 0
    completed_titles = []
    number_completed = 0

    for item in user_todo:
        if item.get("userId") == int(user_id):
            total_todo += 1
            if item.get("completed") is True:
                number_completed += 1
                completed_titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, number_completed, total_todo))
    for title in completed_titles:
        print("\t {}".format(title))
