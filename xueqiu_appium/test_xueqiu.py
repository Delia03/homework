from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['automationName'] = 'uiautomator2'
        caps['deviceName'] = 'Android6.0'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        # caps['noRest'] = True
        caps['unicodeKeyBoard'] = True
        caps['resetKeyBoard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)
        self.driver.find_element(MobileBy.ID, "tv_agree").click()

    def test_search(self):
        # 点击输入框
        self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
        # 输入阿里巴巴
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        # 选择搜索结果
        # self.driver.find_element(MobileBy.ID, "name").click()
        # 点击香港上市的阿里巴巴
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]').click()
        # 断言进入股票详情页面
        stock_name = self.driver.find_element(MobileBy.XPATH,
                                              '//*[contains(@resource-id,"ll_title_content")]//*[contains(@resource-id,"action_bar_stock_name")]').text
        stock_code = self.driver.find_element(MobileBy.XPATH,
                                              '//*[contains(@resource-id,"ll_title_content")]//*[contains(@resource-id,"title_bar_symbol")]').get_attribute(
            "text")
        assert stock_name == "阿里巴巴-SW"
        assert stock_code == "09988"

    def test_getStockPrice(self):
        # 点击输入框
        self.driver.find_element(By.ID, "tv_search").click()
        # 往输入框中输入阿里巴巴
        self.driver.find_element(By.ID, "search_input_text").send_keys("阿里巴巴")
        # 点击搜索结果
        self.driver.find_element(By.ID, "name").click()
        # 获取香港上市的阿里巴巴的股价
        # stock_current_price = self.driver.find_element(By.XPATH,
        #                                                '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]').text
        stock_current_price = self.driver.find_element(By.XPATH,
                                                       "//*[@text='BABA']/../../..//*[contains(@resource-id,'current_price')]").text
        # 断言股价
        assert float(stock_current_price) == 194.00

    def test_addOption(self):
        # 点击输入框
        self.driver.find_element(By.ID, "tv_search").click()
        # 往输入框中输入阿里巴巴
        self.driver.find_element(By.ID, "search_input_text").send_keys("阿里巴巴")
        # 点击搜索结果
        self.driver.find_element(By.ID, "name").click()
        # 点击股票
        self.driver.find_element(By.XPATH,
                                 '//*[contains(@resource-id,"title_container")]//*[@text="股票"]').click()
        # 点击添加自选
        self.driver.find_element(By.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id,"follow_btn")]').click()
        # 点击弹框的下次再说
        self.driver.find_element(By.XPATH, '//*[@text="下次再说"]').click()
        # 断言添加自选成功
        res = self.driver.find_element(By.XPATH,
                                       '//*[@text="09988"]/../../..//*[contains(@resource-id,"followed_btn")]').get_attribute(
            "text")
        assert res == "已添加"

    def test_goto_market_page(self):
        self.driver.find_element(By.XPATH, "//*[@text='行情']").click()
        self.driver.find_element(By.ID, "action_search").click()
        self.driver.find_element(By.XPATH, '//*[@text="取消"]').click()

    def test_webview_native(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "输入11位手机号").send_keys("18200000000")
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "输入验证码").send_keys("9999")
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "立即开户").click()

    def test_webview_context(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        print("打印pagesource:" + self.driver.page_source)
        # print("打印window_handles" + self.driver.window_handles)

        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID, "phone-number")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(phone).send_keys("18200000000")

    def teardown(self):
        pass
        # sleep(10)
        # self.driver.quit()
