import requests
from bs4 import BeautifulSoup
import xlwt

list = []
def get_evaluate():
    print("正在写入请稍后...")
    for i in range(0,50,20):  # 循环设置爬取的页数,设置步数，根据url翻页的规律来设置
        url_i = 'https://movie.douban.com/subject/1292052/comments?start=%s&limit=20&sort=new_score&status=P'%(i)
        print (url_i)
        response_i = requests.get(url_i)
        #print(url_i)
        html_i = response_i.content.decode("utf-8")
        soup_i = BeautifulSoup(html_i, "lxml")
        dp = soup_i.find_all(attrs={"class": "short"})
        for i in dp:
            a = (str(i))
            ate = (a[20:-7])
            #print (ate)
            list.append(ate)  #把每条评论加入到列表中
        #print(len(list))

def save():
    myxls = xlwt.Workbook()
    sheet1 = myxls.add_sheet(u'top250', cell_overwrite_ok=True)
    for i in range(0, len(list)):    #根据评论列表的长度循环写入多少次
        sheet1.write(i, 0, i + 1)
        sheet1.write(i, 1, list[i])  #把列表的每条评论依次写入excel
    myxls.save('top100xsk.xls')
    print("写入成功")


if __name__=="__main__":
    get_evaluate()
    save()


