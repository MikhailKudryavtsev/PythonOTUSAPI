import pytest
import requests


def test_success():
    r = requests.get(url='https://dog.ceo/api/breeds/image/random')
    assert 'success' == r.json().get('status')


def test_bulldog_list():
    r = requests.get(url='https://dog.ceo/api/breed/bulldog/list')
    bulldog_list = ['boston', 'english', 'french']
    assert bulldog_list == r.json().get('message')


@pytest.mark.parametrize('breed_name', ['affenpinscher', 'african', 'airedale', 'akita', 'appenzeller', 'australian'])
def test_breeds(breed_name):
    r = requests.get(url=f'https://dog.ceo/api/breed/{breed_name}/images')
    assert [] != r.json().get('message')


@pytest.mark.parametrize('item', [3, 6, 9])
def test_len_breed_list(item):
    r = requests.get(url=f'https://dog.ceo/api/breed/hound/images/random/{item}')
    breed_list = r.json().get('message')
    assert len(breed_list) == item


def test_status_code():
    r = requests.get('https://dog.ceo/api/breed/hound/list')
    assert r.status_code == 200
