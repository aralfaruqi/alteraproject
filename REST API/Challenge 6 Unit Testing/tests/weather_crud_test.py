import json
from . import *
from unittest import mock
from unittest.mock import patch

class TestMockWeatherBit():
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
        
        if len(args)>0:
            if args[0] == "https://api.weatherbit.io/v2.0/ip":
                return MockResponse({
                    "latitude" : "-7.983908",
                    "longitude" : "112.621391",
                    "city" : "Malang",
                    "organization" : "Alterra Group",
                    "timezone" : "WIB"
                }, 200)
            elif args[0] == "https://api.weatherbit.io/v2.0/current":
                return MockResponse({                
                        "count": "1",
                        "data": [
                            {"temp": 23.5,
                            "datetime": "2017-03-15:13"}  
                        ]
                }, 200)
            else:
                return MockResponse(None, 404)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def weather(self, test_reqget_mock, client):
        token = create_token(True)

        data = {
            'ip' : '182.1.82.246'
        }

        res = client.get('/weather/ip',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

        

