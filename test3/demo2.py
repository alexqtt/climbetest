import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://book.douban.com/subject/1084336/comments/hot?p=1'
urls = ["https://book.douban.com/subject/1084336/comments/hot?p={}".format(str(i)) for i in range(1,3)]
print (urls)
r = requests.get(url)
resp =  r.content.decode("utf-8")
soup =BeautifulSoup(resp,'lxml')
print (soup.title)
dp = soup.find_all(attrs={"class":"short"})   #拿到属性值short的标签
print (len(dp))

for i in dp:
    a = (str(i))
    print (a[20:-7])  #切片去除多余的数据



