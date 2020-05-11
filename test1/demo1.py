import requests

response  = requests.get("https://www.baidu.com",verify=False) #https的访问关闭证书验证，不然返回报错
#print(type(response))
#print(response.status_code)
#print(type(response.text))
print(response.text)  #返回页面数据，但是有时会出现乱码
#print(response.cookies)
#print(response.content)
print(response.content.decode("utf-8"))  #返回页面html，解决乱码的输出
