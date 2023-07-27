import json
import time
import log



class Connections():

    def __init__(self, driver):
        self.driver = driver


    def check_connection(self):
        count: int = 0
        resp = self.driver.execute_script("mobile: deviceInfo")
        data_dump = json.dumps(resp)
        data = json.loads(data_dump)['networks']
        while not data:
            count += 1
            time.sleep(1)
            data = self.driver.execute_script("mobile: deviceInfo")
            data_dump = json.dumps(data)
            data = json.loads(data_dump)['networks']
            if count == 10:
                break
        if data:
            log.info(f"Connected : {data[0]['isConnected']}")
            return data[0]['isConnected']