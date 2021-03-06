from flask import render_template, jsonify, request, session, Blueprint, g
from system.db.contract_db import Contractdb
from system.db.customer_db import Customerdb
from system.db.email import Emaildb
from system.db.vender_db import Venderdb
from system.db.user_db import test_user_manager
from system.function.yaml_handle import ReadHandle
import os




from system.views import user



mod = Blueprint('customer', __name__, template_folder='templates')



configure_file = os.path.abspath('.')

configure_data = ReadHandle(f'{configure_file}/system/configure/authority_configure.yaml').yaml_files_read()



@mod.route('/customer',methods=['POST', 'GET'])
@user.authorize
def customer():
    user_list = session.get('user', None)
    user_position = user_list[0]['position']
    group_name = Emaildb().get_all_group()
    return render_template('util/customer.html',group_name=group_name ,configure_data = configure_data,user_position=user_position)


@mod.route('/customer.json', methods=['POST', 'GET'])
@user.authorize
def customer_json():
    result = Customerdb().get_all_customer()
    customers_infor = []
    for row in result:
        customer_infor = {}
        customer_infor["id"] = row[0]
        customer_infor["company_name"] = row[1]
        customer_infor["location"] = row[2]
        customer_infor["configure"] = row[3]
        customer_infor["test_subject"] = row[4]
        customer_infor["product_type"] = row[5]
        customer_infor["saleman"] = row[6]
        customer_infor["chief_task"] = row[7]
        customer_infor["provide_js"] = row[8]
        customer_infor["linkman_name"] = row[9]
        customer_infor["department"] = row[10]
        customer_infor["position1"] = row[11]
        customer_infor["email"] = row[12]
        customer_infor["vender"] = row[13]
        customer_infor["business_develop"] = row[14]
        customer_infor["project_manager"] = row[15]
        customers_infor.append(customer_infor)
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # ?????????????????????
        offset = info.get('offset', 0)  # ????????????(??????-1)*limit?????????????????????????????????

    return jsonify({'total': len(customers_infor), 'rows': customers_infor[int(offset):(int(offset) + int(limit))]})

@mod.route('/search_customer.json', methods=['POST', 'GET'])
@user.authorize
def search_customer_json():
    company_name = request.values.get("company_name")
    linkman_name = request.values.get("linkman_name")
    email = request.values.get("email")
    if company_name or linkman_name or email:
        result = Customerdb().seaech_customer(company_name,linkman_name,email)
    else:
        result = Customerdb().get_all_customer()
    customers_infor = []
    for row in result:
        customer_infor = {}
        customer_infor["id"] = row[0]
        customer_infor["company_name"] = row[1]
        customer_infor["location"] = row[2]
        customer_infor["configure"] = row[3]
        customer_infor["test_subject"] = row[4]
        customer_infor["product_type"] = row[5]
        try:
            customer_infor["saleman"] = test_user_manager().get_user_id(row[6])[0][0]
        except:
            customer_infor["saleman"] = None
        customer_infor["chief_task"] = row[7]
        customer_infor["provide_js"] = row[8]
        customer_infor["linkman_name"] = row[9]
        customer_infor["department"] = row[10]
        customer_infor["position1"] = row[11]
        customer_infor["email"] = row[12]
        try:
            customer_infor["vender"] = Venderdb().vender_select(row[13])[0][1]
        except:
            customer_infor["vender"] = None
        try:
            customer_infor["business_develop"] =test_user_manager().get_user_id(row[14])[0][1]
        except:
            customer_infor["business_develop"] = None
        try:
            customer_infor["project_manager"] = test_user_manager().get_user_id(row[15])[0][1]
        except:
            customer_infor["project_manager"] = None
        customers_infor.append(customer_infor)
    data = {'total': len(customers_infor), 'rows': customers_infor}
    data = jsonify({"code": 200, "msg": data})
    return data



@mod.route('/customer_add',methods=['POST', 'GET'])
@user.authorize
def customer_add():
    vender_res = Contractdb().get_all_vender()
    salemam_res = test_user_manager().get_user_position("????????????")
    business_develop =test_user_manager().get_user_position("????????????")
    project_manager =test_user_manager().get_user_position("????????????")
    return render_template('util/customer_company_add.html',vender =vender_res,saleman=salemam_res,business_develop =business_develop,project_manager =project_manager)




@mod.route('/add_customer', methods=['POST', 'GET'])
@user.authorize
def customer_add_json():
    company_name = request.values.get("company_name")
    location = request.values.get("location")
    configure = request.values.get("configure")
    test_subject = request.values.get("test_subject")
    product_type = request.values.get("product_type")
    saleman = request.values.get("saleman")
    chief_task =request.values.get("chief_task")
    provide_js = request.values.get("provide_js")
    linkman_name = request.values.get("linkman_name")
    department = request.values.get("department")
    position1 = request.values.get("position1")
    email = request.values.get("email")
    vender = request.values.get("vender")
    business_develop = request.values.get("business_develop")
    project_manager = request.values.get("project_manager")
    if company_name ==None or company_name =="":
        return jsonify({"code": 500, "msg": "?????????????????????"})
    else :
        Customerdb().customer_add(company_name,location,configure,test_subject,product_type,saleman,chief_task,provide_js,linkman_name,department,position1,email,vender,business_develop,project_manager)
        return jsonify({"code": 200, "msg": "????????????"})


@mod.route('/del_customer', methods=['POST', 'GET'])
@user.authorize
def customer_del():
     id= request.values.get("id")
     if id ==0 or id ==None or id =="":
         return jsonify({"code": 500, "msg": "??????????????????????????????"})
     else:
         Customerdb().customer_del(id)
         return jsonify({"code": 200, "msg": "????????????"})



@mod.route('/add_into_group', methods=['POST', 'GET'])
@user.authorize
def add_into_group():
    customer_id =request.values.get("customer_id")
    group_id = request.values.get("group_id")
    if customer_id ==None or customer_id =="":
        return jsonify({"code": 500, "msg": "??????????????????????????????"})
    else:
        result_1 = Emaildb().check_group_company(customer_id,group_id)
        result = Customerdb().get_customer(customer_id)
        print(result_1)
        if result[0][12] ==None or result[0][12]=="":
            return jsonify({"code": 500, "msg": "???????????????????????????,??????:????????????"})
        elif len(result_1) != 0 :
            return jsonify({"code": 500, "msg": "?????????????????????????????????"})
        else:
            Emaildb().add_group_company(customer_id, group_id)
            return jsonify({"code": 200, "msg": "????????????"})


@mod.route('/customer_modify_display',methods=['POST', 'GET'])
@user.authorize
def customer_modify_display():
    global global_customer_id
    global_customer_id = request.values.get('customer_id')
    if global_customer_id==None or global_customer_id == 0 or global_customer_id=="":
        return ({"code": 500 , "msg": "??????????????????????????????"})
    return jsonify({"code": 200})


@mod.route('/customer_motify',methods=['POST', 'GET'])
@user.authorize
def customer_motify():
    customer_id = global_customer_id
    row = Customerdb().get_customer(customer_id)
    customer_infor = {}
    customer_infor["id"] = row[0][0]
    customer_infor["company_name"] = row[0][1]
    customer_infor["location"] = row[0][2]
    customer_infor["configure"] = row[0][3]
    customer_infor["test_subject"] = row[0][4]
    customer_infor["product_type"] = row[0][5]
    customer_infor["saleman"] = str(row[0][6])
    customer_infor["chief_task"] = row[0][7]
    customer_infor["provide_js"] = row[0][8]
    customer_infor["linkman_name"] = row[0][9]
    customer_infor["department"] = row[0][10]
    customer_infor["position1"] = row[0][11]
    customer_infor["email"] = row[0][12]
    customer_infor["vender"] = row[0][13]
    customer_infor["business_develop"] = str(row[0][14])
    customer_infor["project_manager"] = str(row[0][15])

    vender_res = Contractdb().get_all_vender()
    salemam_res = test_user_manager().get_user_position("????????????")
    salemans = []
    business_develops = []
    project_managers =[]
    for row in salemam_res:
        saleman =[]
        saleman.append(str(row[0]))
        saleman.append(row[1])
        salemans.append(saleman)

    business_develop_res = test_user_manager().get_user_position("????????????")
    for row in business_develop_res:
        business_develop = []
        business_develop.append(str(row[0]))
        business_develop.append(row[1])
        business_develops.append(business_develop)

    project_manager_res = test_user_manager().get_user_position("????????????")
    for row in project_manager_res:
        project_manager = []
        project_manager.append(str(row[0]))
        project_manager.append(row[1])
        project_managers.append(project_manager)
    print(type(customer_infor["saleman"]),customer_infor["saleman"])
    print(type(salemans[0][0]),salemans[0][0])

    return render_template('util/customer_motify.html', vender=vender_res, saleman=salemans, customer_infor=customer_infor ,business_develop =business_develops,project_manager =project_managers)




@mod.route('/customer_motify.json',methods=['POST', 'GET'])
@user.authorize
def customer_motify_motify():
    id = request.values.get("id")
    company_name = request.values.get("company_name")
    location = request.values.get("location")
    configure = request.values.get("configure")
    test_subject = request.values.get("test_subject")
    product_type = request.values.get("product_type")
    saleman = request.values.get("saleman")
    chief_task = request.values.get("chief_task")
    provide_js = request.values.get("provide_js")
    linkman_name = request.values.get("linkman_name")
    department = request.values.get("department")
    position1 = request.values.get("position1")
    email = request.values.get("email")
    vender = request.values.get("vender")
    business_develop = request.values.get("business_develop")
    project_manager = request.values.get("project_manager")

    if company_name == None or company_name == "":
        return jsonify({"code": 500, "msg": "?????????????????????"})
    else:
        Customerdb().customer_update(id,company_name, location, configure, test_subject, product_type, saleman, chief_task,
                                  provide_js, linkman_name, department, position1, email, vender,business_develop,project_manager )
        return jsonify({"code": 200, "msg": "????????????"})






