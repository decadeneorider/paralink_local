from system.db.sqldb import MysqlDB
from system.db.user_db import test_user_manager

class Emaildb:
    def get_all_group(self):
        sql = 'SELECT * FROM group_name '
        result = MysqlDB().search(sql)
        return result

    def get_group(self,group_id):
        sql = f'SELECT * FROM group_name where id = "{group_id}"'
        result = MysqlDB().search(sql)
        return result

    def get_all_group_company(self,group_id):
        sql = f"select t1.id,t1.company_name,t1.company_department,t1.company_linkman ,t1.company_email,t2.username,t3.username,t4.username from  group_company t1 inner join auto_auth_user t2 on t1.saleman = t2.id LEFT JOIN auto_auth_user t3 on t1.business_develop = t3.id LEFT JOIN auto_auth_user t4 on t1.project_manager = t4.id where t1.company_group = '{group_id}'"
        print(group_id)
        group_company_infors=[]
        result = MysqlDB().search(sql)
        print(result)
        for i in range(len(result)):
            group_company_infor = {}
            group_company_infor["id"] = result[i][0]
            group_company_infor["company_name"] = result[i][1]
            group_company_infor["company_department"] = result[i][2]
            group_company_infor["company_linkman"] = result[i][3]
            group_company_infor["company_email"] = result[i][4]
            group_company_infor["company_saleman"] = result[i][5]
            group_company_infor["business_develop"] = result[i][6]
            group_company_infor["project_manager"] = result[i][7]
            group_company_infors.append(group_company_infor)
        return group_company_infors

    def get_all_group_company_1(self,group_id):
        sql = f'SELECT * FROM group_company where company_group ="{group_id}" '
        group_company_infors=[]
        result = MysqlDB().search(sql)
        for i in range(len(result)):
            group_company_infor = {}
            group_company_infor["id"] = result[i][0]
            group_company_infor["company_name"] = result[i][1]
            group_company_infor["company_department"] = result[i][2]
            group_company_infor["company_linkman"] = result[i][3]
            group_company_infor["company_email"] = result[i][4]
            group_company_infor["company_saleman"] = result[i][5]
            group_company_infor["business_develop"] = result[i][7]
            group_company_infor["project_manager"] = result[i][8]

            group_company_infors.append(group_company_infor)
        return group_company_infors

    def add_group_company(self,company_name,companu_department,company_linkman,company_email,saleman,company_group,business_develop,project_manager):
        sql = f'insert into group_company(company_name,company_department,company_linkman,company_email,saleman,company_group,business_develop,project_manager)value ("{company_name}","{companu_department}","{company_linkman}","{company_email}","{saleman}","{company_group}","{business_develop}","{project_manager}")'
        MysqlDB().operation(sql)

    def del_group_company(self,company_id):
        sql = f"DELETE  from group_company where id ='{company_id}' "
        MysqlDB().operation(sql)

    def add_email_record(self,username,group_id,email_time,email_message,result_success):
        sql = f'insert into email_record(username,group_id,email_time,email_message,result_success)value ("{username}","{group_id}","{email_time}","{email_message}","{result_success}")'
        MysqlDB().operation(sql)


    def get_email_record(self):
        sql = 'SELECT * FROM email_record order by email_time desc '
        email_records = []
        result = MysqlDB().search(sql)
        for i in range(len(result)):
            email_record = {}
            email_record["id"] = result[i][0]
            email_record["username"] = result[i][1]
            group_name = self.get_group(result[i][2])
            email_record["group_id"] = group_name[0][1]
            email_record["email_time"] = result[i][3].strftime("%Y-%m-%d %H:%M:%S")
            email_record["email_message"] = result[i][4]
            email_record["result_success"] = result[i][5]
            email_records.append(email_record)
        return email_records


    def motify_group_name(self,group_id,group_name):
        sql = f'UPDATE group_name SET group_name="{group_name}" where id = "{group_id}"'
        MysqlDB().operation(sql)
