import pytest
import yaml
from selenium.webdriver.common.by import By

from test_appium.page.app import APP


class TestSearch:
    def test_market_search(self):
        # select_locator = (By.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"follow_btn")]')
        # APP().start_app().goto_home_page().goto_market_page().search().search_stock("阿里巴巴").add_select(
        #     select_locator).back_market_page()
        APP().start_app().goto_home_page().goto_market_page().search().search_stock(
            "阿里巴巴").add_select().back_market_page()

    def test_search(self):
        print(APP().start_app().goto_home_page().goto_search_page().search_stock("阿里巴巴").get_stock_price())
        assert APP().start_app().goto_home_page().goto_search_page().search_stock("阿里巴巴").get_stock_price() == 194.00

    @pytest.mark.parametrize("stock,price", yaml.safe_load(open("../data/data0.yml")))
    def test_search_data(self, stock, price):
        assert APP().start_app().goto_home_page().goto_search_page().search_stock(stock).get_stock_price() == price
