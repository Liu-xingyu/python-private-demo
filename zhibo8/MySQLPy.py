# coding=utf-8

'''

Python连接MySQl

'''
import pymysql


class Python_MySQL():
    '''
    host:主机名
    userName：数据库拥有者
    password：数据库登录密码
    tableName：数据库名
    '''

    def __init__(self, host, userName, paassword, tableName):
        self.host = host
        self.userName = userName
        self.password = paassword
        self.tableName = tableName

        db = pymysql.connect(self.host, self.userName, self.password, self.tableName)
        cursor = db.cursor()

        # self.insertData(cursor, db)

        self.delData(cursor, db, 4)

        self.getMySQLData(cursor)

        self.closeMySQL(db)

    # 创建数据表
    def createTable(self, cursor, db, sql):
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('Error For It')
            db.rollback()

    # 查询
    def getMySQLData(self, cursor):
        # sql = "select version()"
        sql = "select * from java"

        cursor.execute(sql)

        all_datas = cursor.fetchall()

        for data in all_datas:
            print(u'id=', data[0], u' name=', data[1], u' gender=', data[2], u' age=', data[3])

    # 插值
    def insertData(self, cursor, db):
        sql = "insert into java VALUES (4,'Alexis Sanches','male',28)"

        try:
            cursor.execute(sql)
            print('成功添加数据')
            db.commit()
        except:
            print('SQL语句有错误')
            db.rollback()

    def delData(self, cursor, db, id):
        sql = "delete from java where id=" + str(id)

        try:
            cursor.execute(sql)
            print('成功删除数据')
            db.commit()
        except:
            print('删除数据出现错误')
            db.rollback()

    # 关闭连接
    def closeMySQL(self, db):
        db.close()


mysql = Python_MySQL('localhost', 'root', '1210933445', 'test')
