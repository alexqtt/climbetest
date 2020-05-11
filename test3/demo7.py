import requests # 导入requests包
from bs4 import BeautifulSoup
r = requests.get('http://www.youdao.com/w/eng/test/') # 向有道词典请求资源
html = r.text
soup = BeautifulSoup(html, 'html.parser') # 结构化文本soup
div = soup.find(name='div', attrs={'class': 'trans-container'}) # 获取中文释义所在的标签
print(div.get_text()) # 获取标签内文本

