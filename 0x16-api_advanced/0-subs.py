#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers in a given subreddit."""
    reddit_url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {"User-Agent": "Chrome/81.0.4044.129"}
    req = requests.get(reddit_url, headers=header)
    reddit = req.json()

    if (req.status_code == 200):
        """checks if the response status is ok"""
        subs = reddit.get("data").get("subscribers")
        return (subs)
    else:
        return 0
