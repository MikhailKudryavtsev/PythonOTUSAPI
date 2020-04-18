# PythonOTUSAPI

**Тестирование REST сервиса 1.**

Тестируем следующие запросы:
- 'https://dog.ceo/api/breeds/image/random';
- 'https://dog.ceo/api/breed/bulldog/list';
- 'https://dog.ceo/api/breed/`{breed_name}`/images', где `breed_name` - параметр, в который мы передаем название пароды;
- 'https://dog.ceo/api/breed/hound/images/random/`{item}`', где `item` - параметр, в который мы передаем число рандомных изображений;
- 'https://dog.ceo/api/breed/hound/list'.

Модуль testing_api_dog.py содержит следующие тесты:
- test_success
- test_bulldog_list
- test_breeds
- test_len_breed_list
- test_status_code


**Тестирование REST сервиса 2**

Тестируем следующие запросы:
- 'https://api.openbrewerydb.org/breweries';
- 'https://api.openbrewerydb.org/breweries/`{brewery[1]}`', где `brewery[1]` - параметр, в который мы передаем id пивоварни;
- 'https://api.openbrewerydb.org/breweries?by_type=`{breweries_type}`', где `breweries_type` - параметр, в который мы передаем тип пивоварен;
- 'https://api.openbrewerydb.org/breweries?per_page=25';
- 'https://api.openbrewerydb.org/breweries/search?query=Brewhouse'.

Модуль testing_api_openbrewerydb.py содержит следующие тесты:
- test_success
- test_name_and_id
- test_status_code
- test_list_length
- test_brewhouse_in_name


**Тестирование REST сервиса 3**

Тестируем следующие запросы:
- 'https://jsonplaceholder.typicode.com/users';
- 'https://jsonplaceholder.typicode.com/posts';
- 'https://jsonplaceholder.typicode.com/posts/`{postId}`/comments', где `postId` - параметр, в который мы передаем id поста;
- 'https://jsonplaceholder.typicode.com/albums?userId=`{id[0]}`&id=`{id[1]}`', где `id[0]` - параметр, в который мы передаем id пользователя, id[1] - параметр, в который мы передаем id альбома;
- 'https://jsonplaceholder.typicode.com/photos'.

Модуль testing_api_jsonplaceholder.py содержит следующие тесты:
- test_users
- test_keys
- test_comments
- test_albums
- test_header


**Тестирование url и status_code с помощью pytest.addoption**

Тестовая функция `test_url_status` принимает 2 параметра:
`url` - по умолчанию https://ya.ru
`status_code` - по умолчанию 200

Пример запуска `pytest testing_add_options.py --url=https://mail.ru --status_code=200`