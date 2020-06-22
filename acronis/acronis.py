import requests


class Acronis:

    def __init__(self, url, username, password):
        self._url = url
        self._username = username
        self._password = password

    def _get_auth_headers(self):
        payload = dict(grant_type=self._grant_type.name, scope='openid')
        payload.update(
            dict(
                username=self._username,
                password=self._password,
                scope='offline_access',
            )
        )
        response = requests.post(
            f'{self._url}/api/2/idp/token',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=payload,
        )
        access_token = response.json().get('access_token')
        return dict(Authorization=f'Bearer {access_token}')

    def get_alerts(self):
        return requests.get(self._url + "/api/alert_manager/v1/alerts",
                            headers=self._get_auth_headers()).json()
