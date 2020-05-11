import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#加header不然无法访问知乎
response =requests.get("https://www.zhihu.com",headers=headers)
if response.status_code == 200:
    print("访问成功")
print(response.text)