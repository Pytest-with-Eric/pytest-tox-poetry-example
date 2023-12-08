import requests


def get_posts():
    # URL for the JSONPlaceholder API endpoint for posts
    url = "https://jsonplaceholder.typicode.com/posts"

    # Sending a GET request to the API
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Parsing the response to JSON
        posts = response.json()
        return posts
    else:
        # Handling the case where the request failed
        return "Error: Unable to fetch posts"


if __name__ == "__main__":
    # Fetch and print the posts
    print(get_posts())
