from src.response import Response
import pytest


@pytest.mark.parametrize('url, method, params, control_response', [
    ('https://8ca170bc-8350-40fd-93ac-09e69ece423d.serverhub.praktikum-services.ru/api/v1/courier',
     'POST',
     {
         "login": "ninja",
         "password": "1234",
         "firstName": "saske"
     },
     {
    'ok': True
     }
     )
] )
def test_api(url, method, params, control_response, response_fixture):
    # print(response_fixture.response_json)
    assert response_fixture.response_json == control_response, 'Ай - яй -яй!!!'

