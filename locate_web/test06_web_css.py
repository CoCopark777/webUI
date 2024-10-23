import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 驱动地址

# 驱动初始化
dirver = webdriver.Chrome()

# 输入网址
# dirver.get("https://www.saucedemo.com/")
dirver.get("https://www.baidu.com/")

# 窗口最大化
dirver.maximize_window()
# cssID 定位
# dirver.find_element(By.CSS_SELECTOR, "#kw").send_keys("css定位用id元素")
# dirver.find_element(By.CSS_SELECTOR, "#su").click()
#css classname属性值定位
# dirver.get("https://www.bilibili.com/")
# dirver.find_element(By.CSS_SELECTOR, ".nav-search-input").send_keys("css定位用class元素")
# dirver.find_element(By.CSS_SELECTOR, ".nav-search-btn").click()
# 根据name属性值定位
# dirver.find_element(By.CSS_SELECTOR, '[name="wd"]').send_keys("css定位用name元素")
# 根据标签属性定位
# dirver.find_element(By.CSS_SELECTOR, 'a[href="http://image.baidu.com/"]').click()
# 模糊匹配-包含
# dirver.find_element(By.CSS_SELECTOR, 'a[href*="image.baidu.com"]').click()
# 模糊匹配-开头
# dirver.find_element(By.CSS_SELECTOR, 'a[href^="http://image.baidu"]').click()
# 模糊匹配-结尾
# dirver.find_element(By.CSS_SELECTOR, 'a[href$="baidu.com"]').click()
# 模糊匹配-组合定位  拼接时.#和之前属性值保持一致
# dirver.find_element(By.CSS_SELECTOR, 'input.s_ipt').send_keys("selenium")
# 定位子元素 默认取第一个值，id定位
# dirver.find_element(By.CSS_SELECTOR, 'div#s-top-left>a').click()
# 定位子元素 默认取第一个值 class定位
# dirver.find_element(By.CSS_SELECTOR, 'div.s-top-left-new.s-isindex-wrap>a').click()
# 定位子元素 默认取第一个值，id唯一不用加div
# dirver.find_element(By.CSS_SELECTOR, '#s-top-left>a').click()
# 定位子元素 取其他值最后加 :nth-child() 排在第几位就是数字几   /可以右键copy>copy selector
# dirver.find_element(By.CSS_SELECTOR, 'div#s-top-left>a:nth-child(3)').click()
# 定位子元素 elements要带下标
dirver.find_elements(By.CSS_SELECTOR, 'div#s-top-left>a')[3].click()
time.sleep(5)
dirver.quit()

