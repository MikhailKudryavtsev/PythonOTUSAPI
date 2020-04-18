import pytest
import requests


def test_users():
    r = requests.get(url='https://jsonplaceholder.typicode.com/users')
    users_list = r.json()
    assert 10 == len(users_list)


def test_keys():
    r = requests.get(url='https://jsonplaceholder.typicode.com/posts')
    posts_list = r.json()
    for i in range(len(posts_list)):
        item = posts_list[i]
        assert sorted(['userId', 'id', 'title', 'body']) == sorted(item.keys())


@pytest.mark.parametrize('postId', range(5), ids=['postId=1', 'postId=2', 'postId=3', 'postId=4', 'postId=5'])
def test_comments(postId):
    r = requests.get(url=f'https://jsonplaceholder.typicode.com/posts/{postId}/comments')
    comments_list = r.json()
    for i in range(len(comments_list)):
        item = comments_list[i]
        assert postId == item.get('postId')


@pytest.mark.parametrize('id', [('1', '1'), ('2', '11'), ('3', '21'), ('4', '31'), ('5', '41')])
def test_albums(id):
    r = requests.get(url=f'https://jsonplaceholder.typicode.com/albums?userId={id[0]}&id={id[1]}')
    item_list = r.json()
    user_id = item_list[0].get('userId')
    album_id = item_list[0].get('id')
    assert id[0] == str(user_id), 'В ответе на запрос содержится неверный пользователь'
    assert id[1] == str(album_id), 'В ответе на запрос содержится неверный альбом'


def test_header():
    r = requests.get(url='https://jsonplaceholder.typicode.com/photos')
    header = r.headers.get('Content-Type')
    assert 'application/json; charset=utf-8' == header
