import requests
from requests.exceptions import ConnectTimeout,ConnectionError,RequestException

try:
    response = requests.get("http://httpbin.org/get",timeout=0.1)
    print(response.status_code)

except ConnectTimeout:
    print("超时")
except ConnectionError:
    print("连接错误")
except RequestException:
    print("error")