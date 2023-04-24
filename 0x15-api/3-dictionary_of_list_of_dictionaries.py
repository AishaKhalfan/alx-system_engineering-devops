#!/usr/bin/python3
"""Fetching JSON data from an API
Dictionary of list of dictionaries
"""

import json
import requests


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    user_dict = requests.get(user_url).json()
    file_name = "todo_all_employees.json"
    my_dict = {}

    for elem in user_dict:
        name = elem.get("username")
        user_id = str(elem.get("id"))
        user_data = requests.get("{}{}/todos".format(user_url, user_id))
        user_data = user_data.json()
        my_dict[user_id] = []
        for item in user_data:
            inner_dict = {}
            inner_dict["username"] = name
            inner_dict["task"] = item.get("title")
            inner_dict["completed"] = item.get("completed")
            my_dict[user_id].append(inner_dict)

        with open(file_name, 'w') as f:
            json.dump(my_dict, f)
