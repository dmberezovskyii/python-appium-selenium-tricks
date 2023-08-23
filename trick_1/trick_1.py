import time
import json


class Connections:
    def __init__(self, driver):
        self.driver = driver

    def _get_networks(self):
        resp = self.driver.execute_script("mobile: deviceInfo")
        data_dump = json.dumps(resp)
        data = json.loads(data_dump)["networks"]
        return data

    def check_connection(self, max_attempts=10, wait_time=1):
        for _ in range(max_attempts):
            networks = self._get_networks()
            if networks:
                return networks[0]["isConnected"]
            time.sleep(wait_time)
        return False
