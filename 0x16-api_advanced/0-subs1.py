#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers in a given subreddit."""
    if not subreddit:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)

    # Check if the request was successful.
    if response.status_code != 200:
        return 0

    # Parse the JSON response.
    data = response.json()

    # Return the number of subscribers.
    return data["subscribers"]
