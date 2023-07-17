import requests

def recurse(subreddit, hot_list=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Add a custom User-Agent header

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Check if there is a next page
            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list=hot_list)  # Recursive call for next page
            else:
                return hot_list
        else:
            return None  # Invalid subreddit or other error
    except requests.exceptions.RequestException:
        return None  # Error occurred during the request

# Example usage
subreddit_name = 'python'
titles = recurse(subreddit_name)
if titles is not None:
    for title in titles:
        print(title)
else:
    print("No results found or invalid subreddit.")
