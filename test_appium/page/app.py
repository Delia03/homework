from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.home_page import HomePage


class APP(BasePage):
    """封装app的方法，用于启动 打开 重启 停止APP"""
    _package = 'com.xueqiu.android'
    _activity = '.view.WelcomeActivityAlias'

    def start_app(self):
        """启动APP"""
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['automationName'] = 'uiautomator2'
            caps['deviceName'] = 'Android6.0'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['noRest'] = True
            caps['unicodeKeyBoard'] = True
            caps['resetKeyBoard'] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self._driver.implicitly_wait(2)
        else:
            self._driver.start_activity(self._package, self._activity)
        return self

    def restart_app(self):
        """重新启动APP"""
        pass

    def stop_app(self):
        """停止APP"""
        pass

    def quit_appium(self):
        """退出测试"""
        pass

    def goto_home_page(self):
        """打开APP首页"""
        return HomePage(self._driver)
