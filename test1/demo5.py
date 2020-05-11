import requests

response = requests.get("http://www.baidu.com")
print(response.cookies)

for key,value in response.cookies.items():
    print(key+"="+value)