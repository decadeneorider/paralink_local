from system.db.contract_db import Contractdb
import xlwt
from datetime import datetime
import os




class ExeclOperation:
    def made_month_report(self,saleman_res):

        contract_res = Contractdb().contract_display_saleman(saleman_res)
        wb = xlwt.Workbook()
        ws = wb.add_sheet('month_report')
        ws.write(0, 0, "合同编号")
        ws.write(0, 1, "客户名")
        ws.write(0, 2, "原厂")
        ws.write(0, 3, "销售人员")
        ws.write(0, 4, "接单日期")
        ws.write(0, 5, "下单日期")
        ws.write(0, 6, "原厂发货日期")
        ws.write(0, 7, "货到客户日期")
        ws.write(0, 8, "验收日期")
        ws.write(0, 9, "维保到期日")
        ws.write(0, 10, "配置")
        ws.write(0, 11, "备注")
        for i in range (len(contract_res)):
            ws.write(i+1,0,contract_res[i][0])
            ws.write(i+1,1,contract_res[i][1])
            ws.write(i+1,2,contract_res[i][2])
            ws.write(i+1,3,contract_res[i][3])
            if contract_res[i][5] == None:
                ws.write(i + 1, 4, contract_res[i][5])
            else:
                ws.write(i + 1, 4, contract_res[i][5].strftime('%Y-%m-%d'))
            if contract_res[i][6] == None:
                ws.write(i + 1, 5, contract_res[i][6])
            else:
                ws.write(i + 1, 5, contract_res[i][6].strftime('%Y-%m-%d'))
            if contract_res[i][7] == None:
                ws.write(i + 1, 6, contract_res[i][7])
            else:
                ws.write(i + 1, 6, contract_res[i][7].strftime('%Y-%m-%d'))
            if contract_res[i][8] == None:
                ws.write(i + 1, 7, contract_res[i][8])
            else:
                ws.write(i + 1, 7, contract_res[i][8].strftime('%Y-%m-%d'))
            if contract_res[i][9] == None:
                ws.write(i + 1, 8, contract_res[i][9])
            else:
                ws.write(i + 1, 8, contract_res[i][9].strftime('%Y-%m-%d'))
            ws.write(i+1,9,contract_res[i][10].strftime('%Y-%m-%d'))
            configure = contract_res[i][4].replace("<br/>","\n")
            ws.write(i+1,10,configure)
            ws.write(i+1,11,contract_res[i][12])
        now_time =datetime.now().strftime('%Y-%m-%d')
        name = saleman_res+now_time+".xls"
        basepath = os.path.abspath('.')
        upload_path = os.path.join(basepath, "month_report", name)
        wb.save(upload_path)

        return name



if __name__ == '__main__':
    result  = ExeclOperation().made_month_report(["Rondon.yuan"])