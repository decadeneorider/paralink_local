from system.db.sqldb import MysqlDB



class test_user_manager:
    def check_login(self, username, password, db_type_num):
        """验证账号登陆"""
        sql = f"select id, username from auto_auth_user where username = '{username}' and password = '{password}'"
        search_list = MysqlDB().search(sql)
        results = []
        for i in range(len(search_list)):
            result = {}
            result['id'] = search_list[i][0]
            result['username'] = search_list[i][1]
            results.append(result)
        return results

    def add_user(self,username,password,email,position1):
        sql = f'insert into auto_auth_user(password,username,email,position1)value ("{password}","{username}","{email}","{position1}")'
        MysqlDB().operation(sql)

    def get_all_user(self):
        sql = 'SELECT * FROM auto_auth_user'
        result = MysqlDB().search(sql)
        user_infors = []
        for i in range(len(result)):
            user_infor = {}
            user_infor["id"] = result[i][0]
            user_infor["username"] = result[i][2]
            user_infor["email"] =result[i][3]
            user_infor["position1"] = result[i][4]
            user_infors.append(user_infor)
        return user_infors

    def get_all_user_id(self):
        sql = 'SELECT id,username FROM auto_auth_user'
        result = MysqlDB().search(sql)
        return result

    def user_del(self, id):
        sql = f"DELETE  from auto_auth_user where id ='{id}' "
        MysqlDB().operation(sql)

    def user_password(self,id,password):
        sql = f"Update auto_auth_user set password = '{password}' where id ='{id}' "
        MysqlDB().operation(sql)

    def get_user_position(self,position1):
         sql = f'SELECT id,username FROM auto_auth_user where position1 ="{position1}" '
         result = MysqlDB().search(sql)
         return result

    def get_user_position_email(self,position1):
         sql = f'SELECT id,username,email FROM auto_auth_user where position1 ="{position1}" '
         result = MysqlDB().search(sql)
         return result

    def get_user_id(self,id):
        sql = f'SELECT username,email FROM auto_auth_user where id ="{id}" '
        result = MysqlDB().search(sql)
        return result

    def get_email_username(self, username):
        sql = f'SELECT email FROM auto_auth_user where username ="{username}" '
        result = MysqlDB().search(sql)
        return result

