import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('合同信息')
ws.write(1, 0, '股票代码')
ws.write(1, 1, '股票名称')
ws.write(1, 2, '股票板块')
ws.write(0, 3, '统计时间')
ws2 = wb.add_sheet('industry')
ws2.write(1, 0, '股票板块')
ws2.write(0, 1, '统计时间')
wb.save("hello.xls")
