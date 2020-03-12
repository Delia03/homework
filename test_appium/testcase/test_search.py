from selenium.webdriver.common.by import By

from test_appium.page.app import APP


class TestSearch:
    def test_search(self):
        # select_locator = (By.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"follow_btn")]')
        # APP().start_app().goto_home_page().goto_market_page().search().search_stock("阿里巴巴").add_select(
        #     select_locator).back_market_page()
        APP().start_app().goto_home_page().goto_market_page().search().search_stock(
            "阿里巴巴").add_select().back_market_page()
