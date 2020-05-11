import requests
files= {"files":open("1.png","rb")}
response = requests.post("http://httpbin.org/post",files=files)
print(response.text)