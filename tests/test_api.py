from src.response import Response
from src.baseclasses.builder import BuilderJson
import pytest
from config import surl


@pytest.mark.parametrize('url, method, params, control_response', [
    (surl+'/api/v1/courier',
     'POST',
      {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
    }
     ,
     {
    'ok': True
     }
     )
] )
# @pytest.mark.parametrize(params['login'],[('ho', '123123', 'вася')])
@pytest.mark.production
def test_api(url, method, params, control_response, response_fixture):
    ''' API ЯндексСамокат. Создание нового курьера. Структура ответа при успешном создании.'''
    # print(response_fixture.response_json)
    assert response_fixture.response_json == control_response, 'Сеуктура ответа содержит ошибки!'

obj = BuilderJson()
# сразу создать структуру и добавить к url ручку
# obj.reset().add('login').add('password').add('firstname')
# затем через parametrize  передавать данные одного КЭ и структуру ответа для сравнения
obj.add(['key1','key2','key3','key4'], 123) # пример создания вложенной структуры
@pytest.mark.development
@pytest.mark.parametrize('value', ('Vasa', 'Вася', '1234', '@#%$@'))
@pytest.mark.parametrize('key', ('first_name', 'last_name', 'age'))
def test_create_courier(key, value): # вызвать response_fixture
    ''' Идея в том чтобы в этой точке, в зависимости от ручки определять json структуру и передавать набор данных для
    валидации одного КЭ с json ответом ожидаемым для этого КЭ.'''
    obj.add(key, value)
    print(obj.structure)
