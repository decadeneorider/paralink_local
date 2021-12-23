

class TestConfig:
    """本地环境，数据库等配置信息"""
    DEBUG = True
    # 数据库配置
    DB_HOST = 'localhost'
    DB_PORT = '3306'
    DB_USER = 'root'
    DB_PASSWORD = '123456'
    DATABASE = 'paralink'

class MysqlDB:

    def connect(self):
        """数据库连接"""
        import mysql.connector
        config_class = TestConfig
        conn = mysql.connector.connect(host=config_class.DB_HOST,
                                       port=config_class.DB_PORT,
                                       user=config_class.DB_USER,
                                       password=config_class.DB_PASSWORD,
                                       database=config_class.DATABASE,
                                       auth_plugin='mysql_native_password',
                                       charset="utf8")
        return conn

    def search(self, sql):
        """数据库查询"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        cursor.close()
        conn.close()
        return values

    def operation(self, sql):
        """数据库操作"""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        try:
            conn.commit()
        except:
            conn.rollback()
        conn.close()