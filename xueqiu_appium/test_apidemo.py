from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestApiDemo:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['automationName'] = 'uiautomator2'
        caps['deviceName'] = 'Android6.0'
        #获取APP入口：adb logcat | grep -i displayed
        caps['appPackage'] = 'io.appium.android.apis'
        caps['appActivity'] = '.ApiDemos'
        # caps['noRest'] = True
        caps['unicodeKeyBoard'] = True
        caps['resetKeyBoard'] = True
        caps['skipServerInstallation'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)
        self.driver.find_element(MobileBy.ID, "tv_agree").click()

    def teardown(self):
        sleep(10)
        self.driver.quit()
