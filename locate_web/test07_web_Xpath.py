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
# 绝对路径
# dirver.find_element(By.XPATH, "/html/body/div/div/div[3]/a").click()
# id定位
# dirver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("selenium")
# class定位
# dirver.find_element(By.XPATH, '//input[@class="s_ipt"]').send_keys("selenium")
# name定位
# dirver.find_element(By.XPATH, '//input[@name="wd"]').send_keys("selenium")
# 多组属性组合定位
# dirver.find_element(By.XPATH, '//input[@id="kw" and @name="wd" and @class="s_ipt" and @autocomplete="off"]').send_keys("selenium")
# 相对路径
dirver.find_element(By.XPATH, "//div[@id='s-top-left']/a[6]").click()

time.sleep(5)
dirver.quit()

