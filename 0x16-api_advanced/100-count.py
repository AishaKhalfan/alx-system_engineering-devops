import requests

def count_words(subreddit, word_list):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'bhalut'}
    response = requests.get(url, headers=headers)
    data = response.json()

    words_count = {word.lower(): 0 for word in word_list}
    for topic in data['data']['children']:
        title_words = topic['data']['title'].lower().split()
        for word in title_words:
            if word in words_count:
                words_count[word] += 1

    sorted_words = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        if count > 0:
            print(f"{word}: {count}")

