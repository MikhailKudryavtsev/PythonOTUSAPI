import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default='200',
        choices=['200', '404', '500', '408'],
        help="Expected status_code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    status_code = request.config.getoption("--status_code")
    if status_code == '200':
        return 200
    elif status_code == '404':
        return 404
    elif status_code == '500':
        return 500
    elif status_code == '408':
        return 408