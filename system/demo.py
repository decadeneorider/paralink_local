
from system.db.customer_db import Customerdb
import xlwt,xlrd

data = xlrd.open_workbook('D:\paralink 开发文件\客户信息2022-01-06.xls')

table = data.sheets()[0]
i = table.col_values(19)
print(i)
j = set(i)
print(j)

for i  in range(418):
    name =table.cell(i+2,0).value + "-"+table.cell(i+2,1).value
    location =  table.cell(i+2,8).value + "-"+table.cell(i+2,9).value
    product_type = table.cell(i+2,6 ).value
    Customerdb().customer_add(name,location,None,None,product_type,None,None,None,None,None,None,None,None,None,None)