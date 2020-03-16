import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    """页面基类，封装一些公共的方法"""
    _error_count = 0
    _max_error_count = 3
    _params = {}
    _black_list = [(By.ID, 'tv_agree'), (By.XPATH, '//*[@text="确定"]'), (By.XPATH, '//*[@text="下次再说"]')]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    """当有广告、评价等各种场景出现时，要进行异常情况处理"""

    # def find(self, by, locator=None):
    #     try:
    #         element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(
    #             by, locator)
    #         # element = self._driver.find_element(*by)
    #         # 成功找到元素后，将错误次数清零
    #         self._error_count = 0
    #         return element
    #     except Exception as e:
    #         # 如果错误次数大于设定最大错误次数，直接报错
    #         if self._error_count >= self._max_error_count:
    #             raise e
    #         # 记录循环次数
    #         self._error_count += 1
    #         # 在黑名单中遍历
    #         for black_element in self._black_list:
    #             elements = self._driver.find_elements(*black_element)
    #             if len(elements) > 0:
    #                 elements[0].click()
    #                 break
    #         return self.find(by, locator)
    def deal_exception(function):
        def warp(self, *args, **kw):
            try:
                elment = function(self, *args, **kw)
                self._error_count = 0
                return elment
            except Exception as e:
                if self._error_count >= self._max_error_count:
                    raise e
                self._error_count += 1
                for black in self._black_list:
                    elments = self._driver.find_elements(*black)
                    if len(elments) > 0:
                        elments[0].click()
                        break
                return function(self, *args, **kw)

        return warp

    @deal_exception
    def find(self, by, locator=None):
        element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
        return element

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count > self._max_error_count:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.send(value, by, locator)

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps: list = yaml.safe_load(f)
            # [{'by': 'xpath', 'locator': '//*[@text="我的"]', 'action': 'click'},
            # {'by': 'xpath', 'locator': '//*[@text="行情"]', 'action': 'click'}]
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "text" == step["action"]:
                        print("打印")
                        element.text
                        print(element.text)
                    if "send" == step["action"]:
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        self.send(content, step["by"], step["locator"])
