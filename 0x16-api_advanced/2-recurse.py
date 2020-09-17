#!/usr/bin/python3
"""Module that contains a handler to interact with the Reddit API.
"""
from requests import get


def recurse(subreddit, hot_list=[], next=None):
    """ titles of all hot articles for a given subreddit"""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/70.0.3538.77 Safari/537.36"
                }
    parameters = {'limit': 100}
    if next:
        parameters['after'] = next
    response = get(
        'https://www.reddit.com/r/' + subreddit + '/hot.json',
        allow_redirects=False,
        headers=headers,
        params=parameters)
    if response.status_code != 200:
        return(None)
    else:
        json_data = response.json()
        get_data = json_data.get('data')
        post_list = get_data.get('children')
        hot_list += post_list
        next_page = get_data.get('after')
        if next_page:
            return(recurse(subreddit, hot_list, next_page))
        else:
            return(hot_list)
