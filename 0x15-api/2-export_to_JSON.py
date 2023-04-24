#!/usr/bin/python3
"""Fetching json data from an api"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("username")
    user_todo = requests.get("{}/todos".format(user_url))
    user_todo = user_todo.json()
    file_name = user_id + ".json"
    my_dict = {}

    my_dict[user_id] = []

    for elem in user_todo:
        inner_dict = {}
        inner_dict["task"] = elem.get("title")
        inner_dict["completed"] = elem.get("completed")
        inner_dict["username"] = user_name
        my_dict.get(user_id).append(inner_dict)

    with open(file_name, 'w') as f:
        json.dump(my_dict, f)
