import pytest
from src.response import Response

@pytest.fixture()
def response_fixture(url, method, params):
    res = Response(method=method, params=params, url=url)
    #print(res.response_status_code)
    return res

