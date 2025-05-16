import json
import allure
import curlify
import requests
from allure_commons.types import AttachmentType
from requests import Session


class BaseRequest(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs):
        response = super().request(
            method=method,
            url=f'{self.base_url}{url}',
            *args,
            **kwargs
        )
        with allure.step(f'{method} {url}'):
            allure.attach(
                body=str(response.status_code),
                name='status code',
                attachment_type=AttachmentType.TEXT,
                extension='txt'
            )
            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=4).encode('utf8'),
                    name='response body',
                    attachment_type=AttachmentType.JSON,
                    extension='json'
                )
            except requests.exceptions.JSONDecodeError:
                allure.attach(
                    body='no body or not JSON',
                    name='response body',
                    attachment_type=AttachmentType.TEXT,
                    extension='txt'
                )
            curl = curlify.to_curl(response.request)
            allure.attach(
                body=curl.encode('utf8'),
                name='curl',
                attachment_type=AttachmentType.TEXT,
                extension='txt'
            )
        return response


base_request = BaseRequest('https://api.demoblaze.com')