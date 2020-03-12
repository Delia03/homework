from time import sleep

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_actionchains():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 隐式等待3秒
    driver.implicitly_wait(3)
    driver.get("https://baidu.com")
    # 定位到要悬停的元素
    element = driver.find_element(By.LINK_TEXT, "设置")
    # element = driver.find_element(By.CSS_SELECTOR, '.setting-text')
    # 对定位到的元素执行悬停操作
    hov = ActionChains(driver).move_to_element(element).perform()
    # 显示等待高级搜索元素出现
    wait_element = driver.find_element(By.LINK_TEXT, "高级搜索")
    # WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "高级搜索")))
    # WebDriverWait(driver, 10).until(expected_conditions.visibility_of(wait_element))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "高级搜索")))
    # 点击高级搜索元素
    wait_element.click()

    sleep(3)
    driver.quit()
