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
# classname 定位
# dirver.find_element(By.CLASS_NAME, "nav-search-input").send_keys("2024")
# 单个元素用法
# dirver.find_element(By.CLASS_NAME, "channel-link").click()
# 多个元素用法
# dirver.find_elements(By.CLASS_NAME, "channel-link")[5].click()
# 获取所有classname下面的元素
# for ele in dirver.find_elements(By.CLASS_NAME, "channel-link"):
#     print(ele.text)
#错误用法 classname 带有空格不能用
dirver.find_element(By.CLASS_NAME, "icon side-icon").click()
time.sleep(5)
dirver.quit()

