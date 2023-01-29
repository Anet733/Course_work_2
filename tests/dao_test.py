import pytest
import json
from dao.dao import PostsDAO

posts = PostsDAO('./data/posts.json', './data/comments.json')

def test_load_posts_json():
    test_posts = []
    with open('./data/posts.json', 'r', encoding='utf-8') as file:
        test_posts = json.load(file)
    assert test_posts == posts.load_posts_json()
