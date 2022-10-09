import time


def test_login_01(self):
    # 用户名、密码为空
    self.browser.switch_to.frame(0)
    self.browser.find_element_by_name('email').send_keys('')
    self.browser.find_element_by_name('password').send_keys('')
    self.browser.find_element_by_id('dologin').click()
    self.browser.switch_to.default_content()
    time.sleep(3)
    try:
        name = self.browser.find_element_by_id('spnUid')
        print('登录成功')
    except:
        print('登陆失败')


def test_login_02(self):
    # 用户名正确、密码为错误
    self.browser.switch_to.frame(0)
    self.browser.find_element_by_name('email').send_keys('sanzang520')
    self.browser.find_element_by_name('password').send_keys('xxx')
    self.browser.find_element_by_id('dologin').click()
    self.browser.switch_to.default_content()
    time.sleep(3)
    try:
        name = self.browser.find_element_by_id('spnUid')
        print('登录成功')
    except:
        print('登陆失败')


def test_login_03(self):
    # 用户名、密码正确
    self.browser.switch_to.frame(0)
    self.browser.find_element_by_name('email').send_keys('lebron_xx@yeah.net')
    self.browser.find_element_by_name('password').send_keys('mxylfbczXIA.3')
    self.browser.find_element_by_id('dologin').click()
    self.browser.switch_to.default_content()
    time.sleep(3)
    try:
        name = self.browser.find_element_by_id('spnUid').text
        if name == 'lebron_xx@yeah.net':
            print('登录成功')
        time.sleep(30)
    except:
        print('登陆失败')


def tearDown(self):
    self.browser.quit()
