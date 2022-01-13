from flask import render_template, jsonify, request, session, Blueprint, g
from system.views import user
from system.db.email import Emaildb
from system.function.email_send import Email
import datetime
import os
from system.db. user_db import test_user_manager
import time
from system.function.yaml_handle import ReadHandle




ALLOWED_EXTENSIONS = set(['txt']) #限制上传文件格式

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

mod = Blueprint('company_group', __name__, template_folder='templates')


configure_file = os.path.abspath('.')

configure_data = ReadHandle(f'{configure_file}/system/configure/authority_configure.yaml').yaml_files_read()

@mod.route('/email_company_edit',methods=['POST', 'GET'])
@user.authorize
def group_display():
    group_infor =Emaildb().get_all_group()
    user_list = session.get('user', None)
    user_position = user_list[0]['position']
    return render_template('util/email_company_edit.html',group = group_infor,configure_data = configure_data,user_position=user_position)


@mod.route('/group_company.json',methods=['POST', 'GET'])
@user.authorize
def group_company():
    group_infor = Emaildb().get_all_group()
    group_id = group_infor[0][0]
    customer_infor = Emaildb().get_all_group_company(group_id)
    print(customer_infor)
    data1 = jsonify({'total': len(customer_infor), 'rows': customer_infor})
    return data1


@mod.route('/group_change_company.json',methods=['POST', 'GET'])
@user.authorize
def group_change_company():
    group_id = request.values.get("company_group_id")
    customer_infor = Emaildb().get_all_group_company(group_id)
    data1 = {'total': len(customer_infor), 'rows': customer_infor}
    data = jsonify({"code": 200, "msg": data1})
    return data




@mod.route('/group_del_company.json',methods=['POST', 'GET'])
@user.authorize
def group_del_company():
    id = request.values.get("id")

    if id == "0" or id == None or id == "":
        return jsonify({"code": 500, "msg": "请选择需要删除的销售人员"})
    else:
        Emaildb().del_group_company(id)
        return jsonify({"code": 200, "msg": "删除成功"})


@mod.route('/send_email',methods=['POST', 'GET'])
@user.authorize
def send_email():
    user_list = session.get('user', None)
    user_position = user_list[0]['position']
    if user_position in configure_data['mail_send']:
        group_infor =Emaildb().get_all_group()
        users = test_user_manager().get_all_user_id()
        variable =[

        ]
        for row in users:
            user_infor = {}
            user_infor["label"] = row[0]
            user_infor["value"] = row[1]
            variable.append(user_infor)

        return render_template('util/send_email.html',group = group_infor,variable=variable)
    else:
        return render_template('util/405.html')




@mod.route('/send_email_file',methods=['POST', 'GET'])
@user.authorize
def upload_email_file():
    file = request.files['file']
    basepath = os.path.abspath('.')  # 当前文件所在路径
    upload_path = os.path.join(basepath,"system","email_file",file.filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    print(upload_path)
    print(file)
    file.save(upload_path)
    fil_name = str(file.filename)
    return ({"code": 200, "msg": "发送成功","file_name":fil_name})



@mod.route('/send_email.json',methods=['POST', 'GET'])
@user.authorize
def send_email_json():
    time.sleep(3)
    user_list = session.get('user', None)
    user_name = user_list[0]['username']
    group_id = request.values.get("company_group_id")
    email_message1 =request.values.get("message")
    sql_message = request.values.get("sql_message")
    file_name = request.values.get("file_name")
    email_title = request.values.get("email_title")
    CC_email =  request.values.get("CC_email")
    print(type(CC_email))
    company_infor = Emaildb().get_all_group_company_1(group_id)
    emails_address = []
    email_saleman =[]
    business_develop=[]
    project_manager = []
    for i in range(len(company_infor)):
        email_address =company_infor[i].get("company_email")
        email_saleman.append(company_infor[i].get("company_saleman"))
        business_develop.append(company_infor[i].get("business_develop"))
        project_manager.append(company_infor[i].get("project_manager"))
        emails_address.append(email_address)
    email_saleman = list(set(email_saleman))
    file_name = str(file_name.encode("utf-8"),encoding="utf-8")
    result_salemans=[]
    if file_name:
        basepath = os.path.abspath('.')
        upload_path = os.path.join(basepath, "system", "email_file", file_name)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        result = Email().send_file_email(emails_address, email_title, email_message1, [upload_path],str(file_name))
        for i in email_saleman:
            email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company', 'department','name','email') + ('-' * 100) + "\n"
            k= 1
            for j in range(len(company_infor)):
                company_saleman = company_infor[j].get("company_saleman")
                email_address = company_infor[j].get("company_email")
                if company_saleman == i :
                    email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(k), company_infor[j].get("company_name"),
                                                                      company_infor[j].get("company_department"),company_infor[j].get("company_linkman"),
                                                                      email_address) + "\n"
                    k+=1
            email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
            email_saleman_address = test_user_manager().get_user_id(i)[0][1]
            result_saleman = Email().send_file_email([email_saleman_address], email_title,str(email_saleman_message) , [upload_path],str(file_name))
            result_salemans.append(result_saleman)
        for i in business_develop:
            email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company',
                                                                                          'department', 'name',
                                                                                          'email') + ('-' * 100) + "\n"
            k = 1
            for j in range(len(company_infor)):
                company_saleman = company_infor[j].get("business_develop")
                email_address = company_infor[j].get("company_email")
                if company_saleman == i and i != "无":
                    email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(k),
                                                                             company_infor[j].get("company_name"),
                                                                             company_infor[j].get("company_department"),
                                                                             company_infor[j].get("company_linkman"),
                                                                             email_address) + "\n"
                    k += 1
            email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
            email_business_develop_address = test_user_manager().get_user_id(i)
            if len(email_business_develop_address) != 0:
                email_saleman_address = email_business_develop_address[0][1]
                result_saleman = Email().send_file_email([email_business_develop_address], email_title, str(email_saleman_message),
                                                         [upload_path], str(file_name))
                result_salemans.append(result_saleman)
        for i in project_manager:
            email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company',
                                                                                          'department', 'name',
                                                                                          'email') + ('-' * 100) + "\n"
            k = 1
            for j in range(len(company_infor)):
                company_saleman = company_infor[j].get("project_manager")
                email_address = company_infor[j].get("company_email")
                if company_saleman == i and i != "无":
                    email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(k),
                                                                             company_infor[j].get("company_name"),
                                                                             company_infor[j].get("company_department"),
                                                                             company_infor[j].get("company_linkman"),
                                                                             email_address) + "\n"
                    k += 1
            email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
            email_saleman_address = test_user_manager().get_user_id(i)
            if len(email_saleman_address) != 0:
                email_saleman_address = email_saleman_address[0][1]
                result_saleman = Email().send_file_email([email_saleman_address], email_title, str(email_saleman_message),
                                                         [upload_path], str(file_name))
                result_salemans.append(result_saleman)
        CC_member = test_user_manager().get_user_email()
        email_list =[]
        for z, k, v in CC_member:
            if v in CC_email:
                email_list.append(k)
        company_infor = Emaildb().get_all_group_company_1(group_id)
        email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company', 'department',
                                                                                      'name', 'email') + (
                                '-' * 100) + "\n"
        for j in range(len(company_infor)):
            email_address = company_infor[j].get("company_email")
            email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(j), company_infor[j].get("company_name"),
                                                                         company_infor[j].get("company_department"),
                                                                         company_infor[j].get("company_linkman"),
                                                                         email_address) + "\n"
            email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
        result_saleman = Email().send_file_email(email_list, email_title, str(email_saleman_message),
                                                 [upload_path], str(file_name))


    else:
        result = Email().send_email(emails_address,email_message1,email_title)
        for i in email_saleman:
            email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company', 'department','name','email') + ('-' * 100) + "\n"
            k =1
            for j in range(len(company_infor)):
                company_saleman = company_infor[j].get("company_saleman")
                email_address = company_infor[j].get("company_email")
                if company_saleman == i and i != "无" :
                    email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(k), company_infor[j].get("company_name"),
                                                                      company_infor[j].get("company_department"),company_infor[j].get("company_linkman"),
                                                                      email_address) + "\n"
                    k+=1
            email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
            print(test_user_manager().get_user_id(i),i)
            email_saleman_address = test_user_manager().get_user_id(i)[0][1]

            result_saleman =Email().send_email([email_saleman_address],str(email_saleman_message),email_title)
            result_salemans.append(result_saleman)
        for i in business_develop:
            email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company',
                                                                                          'department', 'name',
                                                                                          'email') + ('-' * 100) + "\n"
            k = 1
            for j in range(len(company_infor)):
                company_saleman = company_infor[j].get("business_develop")
                email_address = company_infor[j].get("company_email")
                if company_saleman == i and i != "无":
                    email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(k),
                                                                             company_infor[j].get("company_name"),
                                                                             company_infor[j].get("company_department"),
                                                                             company_infor[j].get("company_linkman"),
                                                                             email_address) + "\n"
                    k += 1
            email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
            print(i)
            email_saleman_address = test_user_manager().get_user_id(i)
            if len(email_saleman_address) !=0:
                email_saleman_address =email_saleman_address[0][1]
                result_saleman = Email().send_email([email_saleman_address], str(email_saleman_message), email_title)
                result_salemans.append(result_saleman)
        for i in project_manager:
            email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company',
                                                                                          'department', 'name',
                                                                                          'email') + ('-' * 100) + "\n"
            k = 1
            for j in range(len(company_infor)):
                company_saleman = company_infor[j].get("project_manager")
                email_address = company_infor[j].get("company_email")
                print("company_saleman"+company_saleman,)
                if company_saleman == i and i != "无":
                    email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(k),
                                                                             company_infor[j].get("company_name"),
                                                                             company_infor[j].get("company_department"),
                                                                             company_infor[j].get("company_linkman"),
                                                                             email_address) + "\n"
                    k += 1
            email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
            print(i)
            email_saleman_address = test_user_manager().get_user_id(i)
            if len(email_saleman_address) != 0:
                email_saleman_address = email_saleman_address[0][1]
                result_saleman = Email().send_email([email_saleman_address], str(email_saleman_message), email_title)
                result_salemans.append(result_saleman)
        CC_member = test_user_manager().get_user_email()
        email_list = []
        for z, k, v in CC_member:
            if k in CC_email:
                email_list.append(v)

        company_infor = Emaildb().get_all_group_company_1(group_id)
        email_company = "邮件通知已发送给以下客户:\n" + "{:<10}{:<20}{:<20}{:<20}{:<20}\n".format('index', 'company', 'department',
                                                                                      'name', 'email') + (
                                '-' * 100) + "\n"
        for j in range(len(company_infor)):
            email_address = company_infor[j].get("company_email")
            email_company += "{:<10}{:<20}{:<20}{:<20}{:<20}".format(str(j), company_infor[j].get("company_name"),
                                                                     company_infor[j].get("company_department"),
                                                                     company_infor[j].get("company_linkman"),
                                                                     email_address) + "\n"
        email_saleman_message = email_company + "\n邮件内容:\n" + email_message1
        print(email_saleman_message)
        result_saleman = Email().send_email(email_list, str(email_saleman_message), email_title)

    now_time = datetime.datetime.now()
    if len(result)== 0 :

        Emaildb().add_email_record(user_name,group_id,now_time,sql_message,"成功")
        return jsonify({"code": 200, "msg": "发送成功"})
    else:
        results = ''.join(result)
        Emaildb().add_email_record(user_name, group_id, now_time, sql_message,"发送失败")
        return jsonify({"code": 500, "msg": "发送失败" ,"tips":"发送失败"})



@mod.route('/email_record',methods=['POST', 'GET'])
@user.authorize
def email_record():
    user_list = session.get('user', None)
    user_position = user_list[0]['position']
    if user_position in configure_data['send_record']:
        return render_template('util/email_record.html')
    else:
        return render_template('util/405.html')

@mod.route('/email_record.json',methods=['POST', 'GET'])
@user.authorize
def email_record_json():
    email_records = Emaildb().get_email_record()
    data1 = {'total': len(email_records), 'rows': email_records}
    data = jsonify(data1)
    return data


@mod.route('/motify_group_name.json', methods=['POST', 'GET'])
@user.authorize
def motify_group_name():
     id= request.values.get("group_id")
     group_name =request.values.get("group_name")
     if group_name ==0 or group_name ==None or group_name =="":
         return jsonify({"code": 500, "msg": "请输入修改的组名"})
     else:

         Emaildb().motify_group_name(id,group_name)
         return jsonify({"code": 200, "msg": "修改成功"})