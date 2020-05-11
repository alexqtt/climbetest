import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://book.douban.com/subject/1084336/comments/'

r = requests.get(url)
resp = r.content.decode("utf-8")
soup = BeautifulSoup(resp, 'lxml')
print(soup.title)
dp = soup.find_all(attrs={"class": "short"})  # 拿到属性值short的标签
print (type(dp))


df = pd.DataFrame(dp)
df.to_excel('pinglun.xlsx')


