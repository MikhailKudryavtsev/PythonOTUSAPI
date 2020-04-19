import pytest
import requests


def test_success():
    r = requests.get(url='https://api.openbrewerydb.org/breweries')
    assert [] != r.json()


@pytest.mark.parametrize('brewery', [('Alameda Island Brewing Company', 292),
                                     ('Almanac Beer Company', 299),
                                     ('Faction Brewing Co', 579)])
def test_name_and_id(brewery):
    r = requests.get(url=f'https://api.openbrewerydb.org/breweries/{brewery[1]}')
    assert brewery[0] == r.json().get('name')


@pytest.mark.parametrize('breweries_type',
                         ['micro', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor'])
def test_status_code(breweries_type):
    r = requests.get(url=f'https://api.openbrewerydb.org/breweries?by_type={breweries_type}')
    assert 200 == r.status_code


def test_list_length():
    r = requests.get(url='https://api.openbrewerydb.org/breweries?per_page=50')
    breweries_list = r.json()
    assert 50 == len(breweries_list)


def test_brewhouse_in_name():
    r = requests.get(url='https://api.openbrewerydb.org/breweries/search?query=Brewhouse')
    breweries_list = r.json()
    array = []
    for i in range(len(breweries_list)):
        array.append(breweries_list[i].get('name'))
    assert 'brewhouse' or 'Brewhouse' or 'BrewHouse' or 'Brew House' in array

