#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Prints the titles of ist 10 hot post a given subreddit."""
    reddit_url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    header = {"User-Agent": "Chrome/81.0.4044.129"}
    req = requests.get(reddit_url, headers=header)
    reddit = req.json()

    if (req.status_code == 200):
        """checks if the response status is ok"""
        kali_post = reddit.get("data").get("children")
        for post in kali_post:
            print(post.get("data").get("title"))
    else:
        print("None")
