import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 驱动地址

print(111)
# 驱动初始化
dirver = webdriver.Chrome()
print(222)
# 输入网址
# dirver.get("https://www.saucedemo.com/")
dirver.get("https://www.baidu.com/")
print(333)
# 窗口最大化
dirver.maximize_window()
# id 定位
dirver.find_element(By.ID, "kw").send_keys("selenium")

dirver.find_element(By.ID, "su").click()
time.sleep(5)
dirver.quit()

