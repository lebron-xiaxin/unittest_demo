from selenium import webdriver
import os


class BrowserEngine(object):
    """定义一个浏览器引擎，根据brower_type的值去控制启动不同的浏览器，这里主要IE，chrome"""

    def __init__(self, browser_type):
        self.browser_type = browser_type

    def get_browser(self):
        # 通过判断来控制初始化不同的浏览器启动，默认是Chrome
        if self.browser_type == "IE":
            os.chdir("F:/iedriver_win32")
            driver = webdriver.Ie()
        elif self.browser_type == "Chrome":
            os.chdir("F:/chromedriver_win32")
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
