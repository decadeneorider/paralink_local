from system.db.sqldb import MysqlDB


class Venderdb:
    # 查询原厂
    def get_all_vender(self):
        sql = 'SELECT * FROM vender'
        result = MysqlDB().search(sql)
        vender_infors = []
        for i in range(len(result)):
            vender_infor = {}
            vender_infor["id"] = result[i][0]
            vender_infor["vender_name"] = result[i][1]
            vender_infors.append(vender_infor)
        print(vender_infors)
        return vender_infors

    def vender_select(self, id):
        sql = f'SELECT * FROM vender where id  ="{id}"'
        result = MysqlDB().search(sql)
        return result

    def vender_add(self, vender_name):
        sql = f'insert into vender(vender_name)value ("{vender_name}")'
        MysqlDB().operation(sql)

    def vender_del(self, id):
        sql = f"DELETE  from vender where id ='{id}' "
        MysqlDB().operation(sql)

if __name__ == '__main__':
    vender_infor = Venderdb().get_all_vender()
    print(vender_infor)