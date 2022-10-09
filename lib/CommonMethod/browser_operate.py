from lib.CommonMethod.browser_engine import BrowserEngine


class BrowserOperate(object):
    def __init__(self, url, B_type='IE'):
        browser = BrowserEngine(B_type)
        self.url = url
        self.driver = browser.get_browser()


    def open_browser(self):
        self.driver.get(self.url)

    def close_browser(self):
        self.driver.close()
