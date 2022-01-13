from system.db.sqldb import MysqlDB


class Contractdb:
    "合同数据的操作"

    def add_contract(self, contract_id, customer, vender, saleman,configure,receipt_date, order_date,shipmemt_date,arrival_date,acceptment_date,due_date,remind_need,remark):
        if receipt_date:
            receipt_date = '"'+receipt_date+'"'
        else:
            receipt_date="NULL"
        if order_date:
            order_date = '"' + order_date + '"'
        else:
            order_date="NULL"
        if shipmemt_date:
            shipmemt_date = '"' + shipmemt_date + '"'
        else:
            shipmemt_date="NULL"
        if arrival_date:
            arrival_date = '"' + arrival_date + '"'
        else:
            arrival_date="NULL"
        if acceptment_date:
            acceptment_date = '"' + acceptment_date + '"'
        else:
            acceptment_date="NULL"
        sql = f'INSERT INTO contract_infor (contract_id, customer, vender, saleman,configure,receipt_date, order_date,shipment_date,arrival_date,acceptance_date,due_date,remind_need,remark) VALUES("{contract_id}", "{customer}", "{vender}", "{saleman}","{configure}",{receipt_date},{order_date},{shipmemt_date},{arrival_date},{acceptment_date},"{due_date}",{remind_need},"{remark}")'
        print(sql)
        MysqlDB().operation(sql)


    #查询客户 暂时放在合同
    def get_all_customer(self):
        sql = 'SELECT * FROM customer'
        return MysqlDB().search(sql)

    # 查询客户暂时放在合同
    def get_all_vender(self):
        sql = 'SELECT * FROM vender'
        return MysqlDB().search(sql)

    # 查询客户暂时放在合同
    def get_all_salemam(self):
        sql = 'SELECT * FROM saleman'
        return MysqlDB().search(sql)

    def get_contract_id(self,contract_id):
        sql = f"select * from contract_infor where contract_id ='{contract_id}' "
        result = MysqlDB().search(sql)
        return result

    def display_contract_detail(self,contract_id):

            sql = f"select * from contract_infor where contract_id ='{contract_id}' "
            result = MysqlDB().search(sql)
            contract_infor = {}
            contract_infor['contract_id'] = result[0][0]
            contract_infor['customer'] = result[0][1]
            contract_infor['vender'] = result[0][2]
            contract_infor['saleman'] = result[0][3]
            contract_infor['configure'] = result[0][4]
            if result[0][5] == None:
                contract_infor['receipt_date'] = "无"
            else:
                contract_infor['receipt_date'] = result[0][5].strftime('%Y-%m-%d')
            if result[0][6] == None:
                contract_infor['order_date'] = "无"
            else:
                contract_infor['order_date'] = result[0][6].strftime('%Y-%m-%d')
            if result[0][7] == None:
                contract_infor['shipmemt_date'] = "无"
            else:
                contract_infor['shipmemt_date'] = result[0][7].strftime('%Y-%m-%d')
            if result[0][8] == None:
                contract_infor['arrival_date'] = "无"
            else:
                contract_infor['arrival_date'] = result[0][8].strftime('%Y-%m-%d')
            if result[0][9] == None:
                contract_infor['acceptment_date'] = "无"
            else:
                contract_infor['acceptment_date'] = result[0][9].strftime('%Y-%m-%d')
            contract_infor['due_date'] = result[0][10].strftime('%Y-%m-%d')
            if result[0][11] == 0:
                contract_infor['remind_need'] = "是"
            else:
                contract_infor['remind_need'] = "否"
            contract_infor['remark'] = result[0][12]
            return contract_infor
            # 显示所有维保合同

    def display_contract_1(self):
        sql = 'select * from contract_infor order by due_date desc '
        result = MysqlDB().search(sql)
        return result


    #显示所有维保合同
    def display_contract(self):
        contract_infors =[]
        sql='select * from contract_infor order by due_date desc '
        result =  MysqlDB().search(sql)
        for i in range(len(result)):
            contract_infor = {}
            contract_infor['contract_id'] = result[i][0]
            contract_infor['customer'] = result[i][1]
            contract_infor['vender'] = result[i][2]
            contract_infor['saleman'] = result[i][3]
            contract_infor['configure'] = result[i][4]
            if result[i][5]==None:
                contract_infor['receipt_date'] = result[i][5]
            else:
                contract_infor['receipt_date'] = result[i][5].strftime('%Y-%m-%d')
            if result[i][6]==None:
                contract_infor['order_date'] = result[i][6]
            else:
                contract_infor['order_date'] = result[i][6].strftime('%Y-%m-%d')
            if result[i][7]==None:
                contract_infor['shipmemt_date'] = result[i][7]
            else:
                contract_infor['shipmemt_date'] = result[i][7].strftime('%Y-%m-%d')
            if result[i][8]==None:
                contract_infor['arrival_date'] = result[i][8]
            else:
                contract_infor['arrival_date'] = result[i][8].strftime('%Y-%m-%d')
            if result[i][9]==None:
                contract_infor['acceptment_date'] = result[i][9]
            else:
                contract_infor['acceptment_date'] = result[i][9].strftime('%Y-%m-%d')
            contract_infor['due_date'] = result[i][10].strftime('%Y-%m-%d')
            if result[i][11] ==0:
                contract_infor['remind_need'] = "是"
            else:
                contract_infor['remind_need'] = "否"
            contract_infor['remark'] = result[i][12]
            contract_infors.append(contract_infor)
        return contract_infors

    def del_contract(self,contract_id):
        sql = f"DELETE  from contract_infor where contract_id ='{contract_id}' "
        MysqlDB().operation(sql)

    def sreach_contract(self,contract_id ,customer,vender,saleman,configure,due_date_first,due_date_second):
        sql = "select * from contract_infor where"
        if contract_id:
            sql=sql+f" contract_id like '%{contract_id}%'"

        if  (contract_id ==None or contract_id =="") and customer:
            sql = sql + f"  customer like '%{customer}%'"
        elif contract_id !=None and customer:
            sql = sql + f" and customer like '%{customer}%'"


        if (contract_id ==None or contract_id =="") and (customer ==None or customer =="") and vender:
            sql = sql + f" vender like '%{vender}%'"
        elif (customer != None or contract_id !=None) and vender :
            sql = sql + f" and vender like '%{vender}%'"

        if(contract_id ==None or contract_id =="")and (customer ==None or customer =="") and (vender ==None or vender =="") and saleman:
            sql = sql + f" saleman like '%{saleman}%'"
        elif (vender != None or customer != None or contract_id !=None) and saleman:
            sql = sql + f" and saleman like '%{saleman}%'"

        if (saleman == None or saleman =="") and (contract_id ==None or contract_id =="")and (customer ==None or customer =="") and (vender ==None or vender =="") and configure:
            sql = sql+ f" configure like '%{configure}%'"
        elif (vender != None or customer != None or contract_id !=None or saleman != None) and configure :
            sql = sql + f"and configure like '%{configure}%'"

        if (saleman == None or saleman =="") and (contract_id ==None or contract_id =="")and (customer ==None or customer =="") and (vender ==None or vender =="")and (configure ==None or configure=="") and due_date_first and due_date_second :
            sql =sql +f" due_date BETWEEN '{due_date_first}' AND '{due_date_second}'"
        elif (vender != None or customer != None or contract_id !=None or saleman != None or configure !=None)and(vender !="" or customer !="" or contract_id !="" or saleman != "" or configure !="") and due_date_first and due_date_second :
            sql = sql + f" and due_date BETWEEN '{due_date_first}' AND '{due_date_second}'"
        contract_infors =[]
        print(sql)
        result = MysqlDB().search(sql+"order by due_date desc")
        for i in range(len(result)):
            contract_infor = {}
            contract_infor['contract_id'] = result[i][0]
            contract_infor['customer'] = result[i][1]
            contract_infor['vender'] = result[i][2]
            contract_infor['saleman'] = result[i][3]
            contract_infor['configure'] = result[i][4]
            if result[i][5] == None:
                contract_infor['receipt_date'] = result[i][5]
            else:
                contract_infor['receipt_date'] = result[i][5].strftime('%Y-%m-%d')
            if result[i][6] == None:
                contract_infor['order_date'] = result[i][6]
            else:
                contract_infor['order_date'] = result[i][6].strftime('%Y-%m-%d')
            if result[i][7] == None:
                contract_infor['shipmemt_date'] = result[i][7]
            else:
                contract_infor['shipmemt_date'] = result[i][7].strftime('%Y-%m-%d')
            if result[i][8] == None:
                contract_infor['arrival_date'] = result[i][8]
            else:
                contract_infor['arrival_date'] = result[i][8].strftime('%Y-%m-%d')
            if result[i][9] == None:
                contract_infor['acceptment_date'] = result[i][9]
            else:
                contract_infor['acceptment_date'] = result[i][9].strftime('%Y-%m-%d')
            contract_infor['due_date'] = result[i][10].strftime('%Y-%m-%d')
            if result[i][11] == 0:
                contract_infor['remind_need'] = "是"
            else:
                contract_infor['remind_need'] = "否"
            contract_infor['remark'] = result[i][12]
            contract_infors.append(contract_infor)
        return contract_infors


    def contract_modify_display(self,contract_id):
        sql = f'SELECT * FROM  contract_infor where contract_id = "{contract_id}"'
        result =MysqlDB().search(sql)
        print(result)
        contract_infor={}
        contract_infor['contract_id'] = result[0][0]
        contract_infor['customer'] = result[0][1]
        contract_infor['vender'] = result[0][2]
        contract_infor['saleman'] = result[0][3]
        contract_infor['configure'] = result[0][4]
        if result[0][5] == None:
            contract_infor['receipt_date'] = result[0][5]
        else:
            contract_infor['receipt_date'] = result[0][5].strftime('%Y-%m-%d')
        if result[0][6] == None:
            contract_infor['order_date'] = result[0][6]
        else:
            contract_infor['order_date'] = result[0][6].strftime('%Y-%m-%d')
        if result[0][7] == None:
            contract_infor['shipmemt_date'] = result[0][7]
        else:
            contract_infor['shipmemt_date'] = result[0][7].strftime('%Y-%m-%d')
        if result[0][8] == None:
            contract_infor['arrival_date'] = result[0][8]
        else:
            contract_infor['arrival_date'] = result[0][8].strftime('%Y-%m-%d')
        if result[0][9] == None:
            contract_infor['acceptment_date'] = result[0][9]
        else:
            contract_infor['acceptm ent_date'] = result[0][9].strftime('%Y-%m-%d')
        contract_infor['due_date'] = result[0][10].strftime('%Y-%m-%d')
        if result[0][11] == 0:
            contract_infor['remind_need'] = "是"
        else:
            contract_infor['remind_need'] = "否"
        contract_infor['remark'] = result[0][12]
        return contract_infor

    def contract_motify_updtae(self, contract_id, customer, vender, saleman,configure,receipt_date, order_date,shipmemt_date,arrival_date,acceptment_date,due_date,remind_need,remark):
        if receipt_date:
            receipt_date = '"'+receipt_date+'"'
        else:
            receipt_date="NULL"
        if order_date:
            order_date = '"' + order_date + '"'
        else:
            order_date="NULL"
        if shipmemt_date:
            shipmemt_date = '"' + shipmemt_date + '"'
        else:
            shipmemt_date="NULL"
        if arrival_date:
            arrival_date = '"' + arrival_date + '"'
        else:
            arrival_date="NULL"
        if acceptment_date:
            acceptment_date = '"' + acceptment_date + '"'
        else:
            acceptment_date="NULL"
        sql = f'UPDATE contract_infor SET customer="{customer}",vender ="{vender}",saleman ="{saleman}",configure="{configure}",receipt_date={receipt_date},order_date={order_date},shipment_date={shipmemt_date},arrival_date={arrival_date}, acceptance_date ={acceptment_date},due_date="{due_date}" ,remind_need={remind_need} , remark ="{remark}" where contract_id = "{contract_id}"'
        print(sql)




    def contract_display_saleman(self,saleman):
        sql = f"select * from contract_infor where saleman = '{saleman}'"
        result = MysqlDB().search(sql)
        return result

    def remind_need_update(self,contract_id):
        sql= f'UPDATE contract_infor SET remind_need = 1 where contract_id = "{contract_id}"'
        print(sql)
        MysqlDB().operation(sql)





class Tipsdb:

    def  insert_tips_email_record(self,contract_id,tips_number):
        sql = f'INSERT INTO tips_email_record (contract_id, tips_number) VALUES("{contract_id}","{tips_number}")'
        MysqlDB().operation(sql)


    def tips_conmtract_all(self):
        sql = "select t1.id,t2.contract_id,t2.customer,t2.saleman,t2.due_date,t1.tips_number from tips_email_record t1 left join contract_infor t2 on t1.contract_id = t2.contract_id "
        result = MysqlDB().search(sql)
        return result

    def tips_contract_id_get(self,contract_id):
        sql =f"select t1.id,t2.contract_id,t2.customer,t2.saleman,t2.due_date,t1.tips_number from tips_email_record t1 left join contract_infor t2 on t1.contract_id = t2.contract_id where t1.contract_id = '{contract_id}'"
        result = MysqlDB().search(sql)
        return result

    def tips_number_update(self,contract_id,tips_number):
        sql = f'UPDATE tips_email_record SET tips_number={tips_number} where contract_id = "{contract_id}"'
        MysqlDB().operation(sql)


if __name__ == '__main__':
    i = Contractdb().sreach_contract(None,None,None,None,None,"2021-11-17","2021-11-19")
    print(i)
