from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage
from test_appium.page.market_page import MarketPage
from test_appium.page.my_page import MyPage
from test_appium.page.search_page import SearchPage


class HomePage(BasePage):
    """首页"""

    def goto_search_page(self):
        """进入搜索页"""
        # search_locator = (By.ID, "tv_search")
        # self.find(search_locator).click()
        self.steps("../data/goto_search.yml")
        return SearchPage(self._driver)

    def goto_my_page(self):
        self.steps("../data/goto_my.yml")
        return MyPage(self._driver)

    def goto_market_page(self):
        # market_locator = (By.XPATH, '//*[@text="行情"]')
        # self.find(market_locator).click()
        self.steps("../data/goto_market.yml")
        return MarketPage(self._driver)
