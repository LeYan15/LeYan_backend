import pytest


@pytest.mark.django_db(transaction=True)
class TestAuthUrls:

    @pytest.fixture
    def client(self, client):
        return client

    @pytest.mark.parametrize('url', [
        '/swagger/',
        '/auth/',
        '/auth/users/',
        '/api/',
        '/api/shops/',
        '/api/forecast/',
        '/api/products/',
        '/api/sales/',
        '/redoc/'
    ])
    def test_auth_urls(self, client, url):
        response = client.get(url)
        assert response.status_code != 404, f'Страница `{url}` не найдена, проверьте этот адрес в *urls.py*'
        assert response.status_code == 200, f'Ошибка {response.status_code} при открытиии `{url}`. Проверьте ее view-функцию'
