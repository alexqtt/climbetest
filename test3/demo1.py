from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.zhihu.com/")
#print(browser.page_source)
browser.close()