from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage
from test_appium.page.search_page import SearchPage


class MarketPage(BasePage):
    """行情页"""

    # 点击搜索按钮
    def search(self):
        # search_locator = (By.ID, "action_search")
        # self.find(search_locator).click()
        self.steps("../page/search.yml")
        return SearchPage(self._driver)
