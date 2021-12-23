from system import app
from flask_apscheduler import APScheduler
from system.db.user_db import test_user_manager
from system.db.contract_db import Contractdb,Tipsdb
from system.function.execl_made import ExeclOperation
from system.function.email_send import Email
from datetime import datetime
from dateutil import  rrule

import os


scheduler = APScheduler()

def tips_email():
    reuslt = Contractdb().display_contract_1()
    for i  in reuslt:
        if i[11] ==1:
            now = datetime.now()
            date_difference = rrule.rrule(rrule.DAILY, dtstart=now, until=i[10]).count()
            print(1)
            if date_difference == 90:
                message ="你的客户:\n"+"{:<20}{:<20}{:<20}\n".format( '合同编号', '客户名称','到期日') + ('-' * 100) + "\n"+"{:<20}{:<20}{:<20}\n".format(i[0], i[1],i[10])+ "维保还有90天到期"
                receivers =test_user_manager().get_user_position_email(i[3])[0]
                Email().send_email([receivers],message,"维保到期提醒")
                tips = Tipsdb().tips_contract_id_get(i[0])
                if len(tips) == 0:
                    Tipsdb().insert_tips_email_record(i[0],1)
                else:
                    Tipsdb().tips_number_update(tips[0][1],int(tips[0][5])+1)
            elif date_difference == 60:
                message = "你的客户:\n" + "{:<20}{:<20}{:<20}\n".format('合同编号', '客户名称', '到期日') + (
                            '-' * 100) + "\n" + "{:<20}{:<20}{:<20}\n".format(i[0], i[1], i[10]) + "维保还有60天到期"
                receivers = test_user_manager().get_user_position_email(i[3])[0]
                Email().send_email([receivers], message, "维保到期提醒")
                tips = Tipsdb().tips_contract_id_get(i[0])
                if len(tips) == 0:
                    Tipsdb().insert_tips_email_record(i[0], 1)
                else:
                    Tipsdb().tips_number_update(tips[0][1], int(tips[0][5]) + 1)
            elif date_difference== 30:
                message = "你的客户:\n" + "{:<20}{:<20}{:<20}\n".format('合同编号', '客户名称', '到期日') + (
                        '-' * 100) + "\n" + "{:<20}{:<20}{:<20}\n".format(i[0], i[1], i[10]) + "维保还有30天到期"
                receivers = test_user_manager().get_user_position_email(i[3])[0]
                Email().send_email([receivers], message, "维保到期提醒")
                tips = Tipsdb().tips_contract_id_get(i[0])
                if len(tips) == 0:
                    Tipsdb().insert_tips_email_record(i[0], 1)
                else:
                    Tipsdb().tips_number_update(tips[0][1], int(tips[0][5]) + 1)
            elif date_difference ==0:
                date_difference_1 = rrule.rrule(rrule.DAILY, dtstart=i[10], until=now).count()
                if date_difference_1 ==30:
                    message = "你的客户:\n" + "{:<20}{:<20}{:<20}\n".format('合同编号', '客户名称', '到期日') + (
                            '-' * 100) + "\n" + "{:<20}{:<20}{:<20}\n".format(i[0], i[1], i[10]) + "已经过期30"
                    receivers = test_user_manager().get_user_position_email(i[3])[0]
                    Email().send_email([receivers], message, "维保到期提醒")
                    Contractdb().remind_need_update(i[0])
                    tips = Tipsdb().tips_contract_id_get(i[0])
                    if len(tips) == 0:
                        Tipsdb().insert_tips_email_record(i[0], 1)
                    else:
                        Tipsdb().tips_number_update(tips[0][1], int(tips[0][5]) + 1)


def saleman_month_report():
     saleman_res = test_user_manager().get_user_position_email("销售人员")
     # saleman_res = [(0,"Rondon.yuan","1808863016@qq.com")]
     for row in saleman_res:
        file_name = ExeclOperation().made_month_report(row[1])
        basepath = os.path.abspath('.')
        upload_path = os.path.join(basepath, "month_report", file_name)
        Email().send_file_email([row[2]],"测试月报",row[1]+"合同月报",[upload_path],file_name)



if __name__ == '__main__':
    # scheduler.add_job(func=tips_email, id='1', trigger='interval', minutes =2)
    scheduler.add_job(func=saleman_month_report, id='2', trigger='cron', day="1", hour="8")
    scheduler.init_app(app=app)
    scheduler.start()
    app.run(host='192.168.23.240', port=3014, debug=False)