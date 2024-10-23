import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 驱动地址

# 驱动初始化
dirver = webdriver.Chrome()

# 输入网址
# dirver.get("https://www.saucedemo.com/")
dirver.get("https://www.bilibili.com/")

# 窗口最大化
dirver.maximize_window()
# tagname 定位
# dirver.find_element(By.TAG_NAME, "input").send_keys("2024")
dirver.find_element(By.TAG_NAME, "svg").click()
time.sleep(5)
dirver.quit()

