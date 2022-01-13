from system.db.sqldb import MysqlDB




class Licensedb:
    def all_license(self):
        sql = "select * from license_manage"
        result = MysqlDB().search(sql)
        return result

    def add_license_manage(self,customer_name,customer_department,customer_linkman,kit_type,contract_id):
        sql =f'insert into license_manage(customer_name,customer_department,customer_linkman,kit_type,contract_id)value ("{customer_name}","{customer_department}","{customer_linkman}","{kit_type}","{contract_id}")'
        MysqlDB().operation(sql)

