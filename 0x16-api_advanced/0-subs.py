#!/usr/bin/python3
""" Reddit API """
from requests import get


def number_of_subscribers(subreddit):
    """ Return number of suscribers of a given subredit """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/70.0.3538.77 Safari/537.36"
                }
    response = get(
        'https://www.reddit.com/r/' + subreddit + '/about.json',
        allow_redirects=False,
        headers=headers)
    if response.status_code != 200:
        return 0
    json_data = response.json()
    get_data = json_data.get('data')
    number_suscribers = get_data.get('subscribers')
    return number_suscribers
