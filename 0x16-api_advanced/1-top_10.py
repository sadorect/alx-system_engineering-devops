import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Add a custom User-Agent header

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children'][:10]  # Retrieve first 10 posts
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print("None")  # Invalid subreddit or other error
    except requests.exceptions.RequestException:
        print("None")  # Error occurred during the request

# Example usage
subreddit_name = 'python'
top_ten(subreddit_name)
