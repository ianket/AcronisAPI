import requests


class Acronis:

    def __init__(self, url, tenant_id, tenant_locator):
        self._url = url
        self._tenant_id = tenant_id
        self._tenant_locator = tenant_locator

    def get_alerts(self, severity, show_deleted):
        return requests.get(
            self._url + "/api/alert_manager/v1/alerts?severity=%s&show_deleted=%s" % (severity, show_deleted),
            headers={'X-Apigw-Tenant-ID': self._tenant_id, 'X-Apigw-Tenant-Locator': self._tenant_locator}).json()
