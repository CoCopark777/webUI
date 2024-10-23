import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 驱动地址

# 驱动初始化
dirver = webdriver.Chrome()

# 输入网址

#dirver.get("https://www.bilibili.com/")
dirver.get("https://www.baidu.com/")
# 窗口最大化
dirver.maximize_window()
# tagname 定位
# dirver.find_element(By.TAG_NAME, "input").send_keys("2024")
# dirver.find_element(By.NAME, "wd").send_keys("2024")
dirver.find_elements(By.NAME, "wd")[0].send_keys("根据name属性")
time.sleep(5)
dirver.quit()

