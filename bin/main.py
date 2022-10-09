import unittest
import pymysql
from db import db_main
from lib.CommonMethod.browser_operate import BrowserOperate



if __name__ == "__main__":
    url = 'https://www.12306.cn/index/'
    type = 'Chrome'
    BrowserOperate = BrowserOperate(url,type)
    BrowserOperate.open_browser()
    BrowserOperate.close_browser()