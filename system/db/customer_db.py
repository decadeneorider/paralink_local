from system.db.sqldb import MysqlDB


class Customerdb:
    # 查询客户
    def get_all_customer(self):
        sql = 'SELECT * FROM customer'
        result =MysqlDB().search(sql)

        return result

    def get_customer(self,id):
        sql = f'SELECT * FROM customer where id = "{id}"'
        result =MysqlDB().search(sql)
        return result

    def seaech_customer(self,company_name,linkman_name,email):
         sql = 'SELECT * FROM customer where'
         if company_name:
             sql = sql + f" company_name like '%{company_name}%'"

         if (company_name == None or company_name == "") and linkman_name:
            sql = sql + f"  linkman_name like '%{linkman_name}%'"
         elif company_name != None and linkman_name:
            sql = sql + f" and linkman_name like '%{linkman_name}%'"


         if (company_name ==None or company_name =="") and (linkman_name ==None or linkman_name =="") and email:
            sql = sql + f" email like '%{email}%'"
         elif (company_name != None or linkman_name !=None) and email :
            sql = sql + f" and email like '%{email}%'"
         result = MysqlDB().search(sql)
         return result


    def customer_add(self,company_name,location,configure,test_subject,product_type,saleman,chief_task,provide_js,linkman_name,department,position1,email,vender,business_develop,project_manager):
        sql = f'insert into customer(company_name,location,configure,test_subject,product_type,saleman,chief_task,provide_js,linkman_name,department,position1,email,vendor,business_develop,project_manager)value ("{company_name}","{location}","{configure}","{test_subject}","{product_type}","{saleman}","{chief_task}","{provide_js}","{linkman_name}","{department}","{position1}","{email}","{vender}","{business_develop}","{project_manager}")'
        MysqlDB().operation(sql)

    def customer_update(self,id,company_name,location,configure,test_subject,product_type,saleman,chief_task,provide_js,linkman_name,department,position1,email,vender,business_develop,project_manager):
        sql = f'UPDATE customer SET company_name="{company_name}",location ="{location}",configure ="{configure}",test_subject="{test_subject}",product_type="{product_type}",saleman="{saleman}",chief_task="{chief_task}",provide_js="{provide_js}", linkman_name ="{linkman_name}",department="{department}" ,position1="{position1}" , email ="{email}",vendor="{vender}",business_develop="{business_develop}",project_manager ="{project_manager}" where id = "{id}"'
        MysqlDB().operation(sql)

    def customer_del(self,id):
        sql = f"DELETE  from customer where id ='{id}' "
        MysqlDB().operation(sql)
