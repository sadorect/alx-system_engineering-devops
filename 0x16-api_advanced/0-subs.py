import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Add a custom User-Agent header

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0  # Invalid subreddit or other error
    except requests.exceptions.RequestException:
        return 0  # Error occurred during the request

# Example usage
subreddit_name = 'programming'
subscriber_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscriber_count} subscribers.")
