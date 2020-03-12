from selenium.webdriver.common.by import By
from test_appium.page.base_page import BasePage


class SearchPage(BasePage):
    """搜索页"""

    # 搜索股票
    def search_stock(self, value):
        # input_locator = (By.ID, "search_input_text")
        # name_locator = (By.ID, "name")
        # self.find(input_locator).send_keys(value)
        # 点击搜索结果
        # self.find(name_locator).click()
        self._params["value"] = value
        self.steps("../page/search_stock.yml")
        return self

    # 添加自选
    def add_select(self):
        # select_locator = (By.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"follow_btn")]')
        # self.find(value).click()
        self.steps("../page/add_select.yml")
        return self

    # 取消自选
    def cancel_select(self):
        pass

    # 获取股票价格
    def get_stock_price(self):
        pass

    # 返回行情页
    def back_market_page(self):
        # cancel_locator = (By.XPATH, '//*[contains(@resource-id,"action_close")]//*[@text="取消"]')
        # self.find(By.XPATH, '//*[@text="取消"]').click()
        self.steps("../page/back_market.yml")
        from test_appium.page.market_page import MarketPage
        return MarketPage(self._driver)
