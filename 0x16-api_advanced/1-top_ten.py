#!/usr/bin/python3
""" Reddit API """
from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit."""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/70.0.3538.77 Safari/537.36"
                }
    response = get(
        'https://www.reddit.com/r/' + subreddit + '/hot.json',
        allow_redirects=False,
        headers=headers,
        params={'limit': 10})
    if response.status_code != 200:
        print(None)
    else:
        json_data = response.json()
        parsed_data = json_data.get('data')
        post_list = parsed_data.get('children')
        for post in post_list:
            get_post = post.get('data')
            topic = get_post.get('title')
            print(topic)
