#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found for
the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """returns a list containing the titles of all hot articles 
    for a given subreddit."""
    reddit_url = "https://www.reddit.com/r/" + subreddit
    reddit_url2 = reddit_url + "/hot.json?limit=100&after=after"
    header = {"User-Agent": "Chrome/81.0.4044.129"}
    req = requests.get(reddit_url2, headers=header)
    reddit = req.json()

    if (req.status_code == 200):
        """checks if the response status is ok"""
        hot_post = reddit.get("data").get("children")
        after = reddit.get("data").get("after")
        for posts in hot_post:
            hot_list.append(posts.get("data").get("title"))
        if after is None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
