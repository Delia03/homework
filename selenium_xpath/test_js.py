from time import sleep

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_executeScript():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 隐式等待3秒
    driver.implicitly_wait(3)
    driver.get("https://baidu.com")
    # searchInputBoxJS = "document.getElementById('kw').value='光荣之路';"
    # searchButtonJS = "document.getElementById('su').click()"
    # driver.execute_script(searchInputBoxJS)
    # driver.execute_script(searchButtonJS)
    settingMouseEnterJS = "document.getElementById('s_usersetting_top').onmouseover()"
    driver.execute_script(settingMouseEnterJS)
    # 等待高级搜索元素出现
    wait_element = driver.find_element(By.LINK_TEXT, "高级搜索")
    # 点击高级搜索元素
    wait_element.click()

    sleep(3)
    driver.quit()
