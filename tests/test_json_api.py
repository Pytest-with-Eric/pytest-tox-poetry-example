from examples.json_api import get_posts

def test_get_posts():
    posts = get_posts()
    assert len(posts) == 100