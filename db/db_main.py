# 导入pymysql模块
import pymysql
from config import db_config


class DB(object):
    # 连接database
    def __init__(self):
        # 连接database
        self.conn = pymysql.connect(
            host=db_config.host,
            port=db_config.port,
            user=db_config.user,
            password=db_config.password,
            database=db_config.database,
            charset=db_config.charset
        )
        # 获取数据的游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close_connect(self):
        # 关闭数据连接
        # 提交，物理存储
        self.conn.commit()
        # 游标关闭
        self.cur.close()
        # 连接对象关闭
        self.conn.close()

    def get_api_list(self):
        """获取所有的对象数据"""
        sqlStr = "select * from chip"
        self.cur.execute(sqlStr)
        data = self.cur.fetchall()
        # 转成一个list
        apiList = list(data)
        return apiList

    def get_api_case(self, chip_name):
        """获取某一条数据"""
        sqlStr = "select * from chip where chip_name='{}'".format(chip_name)
        self.cur.execute(sqlStr)
        api_case_list = list(self.cur.fetchall())
        return api_case_list

    def write_check_result(self, table_name, chip_name, platfrom_id):
        """更新数据库表"""
        sqlStr = "update {} set chip_name='{}' where id={}".format(table_name, chip_name, platfrom_id)
        self.cur.execute(sqlStr)
        print(sqlStr)
        self.conn.commit()

    def insert_dab(self):
        sqlStr = "INSERT INTO `interface_api` VALUES (4, '修改博文', 'http://39.106.41.11:8080/getBlogContent/', 'get', 'url','0', '2018-07-27 22:13:30')"
        self.cur.execute(sqlStr)

    def get_api_case(self, api_id):
        """获取表中id"""
        sqlStr = "select * from interface_test_case where api_id=%s and status=1" % api_id
        self.cur.execute(sqlStr)
        api_case_list = list(self.cur.fetchall())
        return api_case_list

# --------------------------
    def get_api_id(self, api_name):
        """获取表中id"""
        sqlStr = "select api_id from interface_api where api_name='%s'" % api_name
        self.cur.execute(sqlStr)
        api_id = self.cur.fetchall()[0][0]
        return api_id

    def update_store_data(self, api_id, case_id, store_data):

        sqlStr = "select data_store from interface_data_store where api_id=%s and case_id=%s" % (api_id, case_id)
        self.cur.execute(sqlStr)
        if self.cur.fetchall():
            sqlStr = "update interface_data_store set data_store=\"%s\" where api_id=%s and case_id=%s" % (
                store_data, api_id, case_id)
            print(sqlStr)
            self.cur.execute(sqlStr)
            self.conn.commit()
        else:
            sqlStr = "insert into interface_data_store values(%s, %s, \"%s\", '%s')" % (
                api_id, case_id, store_data, datetime.now())
            self.cur.execute(sqlStr)
            self.conn.commit()
