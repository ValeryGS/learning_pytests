import requests
from config import headers, surl



class Response():
    def __init__(self, url=surl, method='get', params={}, hdrs=headers):
        if method == 'GET':
            self.response = requests.get(url=url, data=params, headers=hdrs)
            self.response_status_code = self.response.status_code
            self.response_json = self.response.json()
        if method == 'POST':
            self.response = requests.post(url=url, data=params, headers=hdrs)
            self.response_status_code = self.response.status_code
            self.response_json = self.response.json()
        if method == 'DELETE':
            self.response = requests.delete(url=url, data=params, headers=hdrs)
            self.response_status_code = self.response.status_code
            self.response_json = self.response.json()