from flask import render_template, jsonify, request, session, Blueprint, g
from system.db.contract_db import Contractdb
from system.views import user
from system.db.user_db import test_user_manager
from system.function.yaml_handle import ReadHandle
import os
from system.function.execl_made import ExeclOperation
from flask import send_file, send_from_directory


mod = Blueprint('contract', __name__, template_folder='templates')

global_contract_id =""


configure_file = os.path.abspath('.')

configure_data = ReadHandle(f'{configure_file}/system/configure/authority_configure.yaml').yaml_files_read()

@mod.route('/contract_display')
@user.authorize
def contract_display():
    user_list = session.get('user', None)
    user_position = user_list[0]['position']
    return render_template('util/contract_display.html',configure_data = configure_data,user_position = user_position)

@mod.route('/contract.json', methods=['POST', 'GET'])
@user.authorize
def show_contract():
    contract_infor = Contractdb().display_contract()
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点

    return jsonify({'total': len(contract_infor), 'rows': contract_infor[int(offset):(int(offset) + int(limit))]})



@mod.route('/contract_add',methods=['POST', 'GET'])
@user.authorize
def contract_add():
    customer_res = Contractdb().get_all_customer()
    vender_res = Contractdb().get_all_vender()
    salemam_res = test_user_manager().get_user_position("销售人员")
    customer_re = []
    for row in customer_res:
        customer_re.append(row[1])
    customer_re =list(set(customer_re))
    return render_template('util/contract_add.html',customer =customer_re,vender=vender_res,saleman=salemam_res)


@mod.route('/contract_add.json',methods=['POST', 'GET'])
@user.authorize
def contract_add_json():
    contract_id =request.values.get('contract_id')
    customer = request.values.get('customer')
    vender = request.values.get('vender')
    saleman = request.values.get('saleman')
    configure = request.values.get('configure')
    receipt_date = request.values.get('receipt_date')
    order_date = request.values.get('order_date')
    shipmemt_date = request.values.get('shipmemt_date')
    arrival_date = request.values.get('arrival_date')
    acceptment_date = request.values.get('acceptment_date')
    due_date = request.values.get('due_date')
    remind_need = request.values.get('remind_need')
    remark = request.values.get('remark')

    if len(contract_id)==0:
        return jsonify({"code": 500, "msg": "请填写合同编号"})
    elif len(customer)==0:
        return jsonify({"code": 500, "msg": "请选择客户"})
    elif len(vender) == 0:
        return jsonify({"code": 500, "msg": "请选择原厂"})
    elif len(saleman) == 0:
        return jsonify({"code": 500, "msg": "请选择销售人员"})
    elif len(configure) == 0:
        return jsonify({"code": 500, "msg": "请填写配置"})
    elif len(due_date) == 0:
        return jsonify({"code": 500, "msg": "请填写维保到期日"})
    else:
        contract_repeat = Contractdb().get_contract_id(contract_id)
        if len(contract_repeat)>0:
            return jsonify({"code": 500, "msg": "该合同编号已存在"})
        else:
            configure = str(configure).replace('"','\\"')
            Contractdb().add_contract(contract_id, customer, vender, saleman,configure,receipt_date, order_date,shipmemt_date,arrival_date,acceptment_date,due_date,remind_need,remark)
            return jsonify({"code": 200, "msg": "保存成功"})


@mod.route('/contract_del.json',methods=['POST', 'GET'])
@user.authorize
def contract_del_json():
    contract_id = request.values.get('contract_id')
    if contract_id != "0" and contract_id:
        Contractdb().del_contract(contract_id)
        return jsonify({"code": 200})

    else:
        return jsonify({"code": 500, "msg": "请选择要删除的合同"})


@mod.route('/contract_search1.json',methods=['POST', 'GET'])
@user.authorize
def contract_search_json():
    contract_id = request.values.get('contract_id')
    customer = request.values.get('customer')
    vender = request.values.get('vender')
    saleman = request.values.get('saleman')
    configure = request.values.get('configure')
    due_date_first = request.values.get('due_date_first')
    due_date_second = request.values.get('due_date_second')
    if contract_id or customer or vender or saleman or configure or (due_date_first and due_date_second):
        code = 200
        contract_infor = Contractdb().sreach_contract(contract_id,customer,vender,saleman,configure,due_date_first,due_date_second)
    else :
        code = 200
        contract_infor=  Contractdb().display_contract()
    data ={'total': len(contract_infor), 'rows': contract_infor}
    data =jsonify({"code": code, "msg": data})
    return data

@mod.route('/contract_modify_display',methods=['POST', 'GET'])
@user.authorize
def contract_modify_display():
    global global_contract_id
    global_contract_id = request.values.get('contract_id')
    if global_contract_id==None or global_contract_id == 0 or global_contract_id=="":
        return ({"code": 500 , "msg": "请选择需要修改的合同"})
    return jsonify({"code": 200})


@mod.route('/contract_modify',methods=['POST', 'GET'])
@user.authorize
def contract_modify():
    contract_id = global_contract_id
    contract_data = Contractdb().contract_modify_display(contract_id)
    contract_data["configure"] =str(contract_data["configure"]).replace('<br/>',"\r\n")
    print(contract_data)
    customer_res = Contractdb().get_all_customer()
    vender_res = Contractdb().get_all_vender()
    salemam_res = test_user_manager().get_user_position("销售人员")
    customer_re=[]
    for row in customer_res:
        customer =[]
        customer.append(row[0])
        customer.append(row[1])
        customer_re.append(customer)
    return render_template('util/contract_motify.html', customer=customer_re, vender=vender_res, saleman=salemam_res,data=contract_data)


@mod.route('/contract_modify.json',methods=['POST', 'GET'])
@user.authorize
def contract_modify_json():
    contract_id = request.values.get('contract_id')
    customer = request.values.get('customer')
    vender = request.values.get('vender')
    saleman = request.values.get('saleman')
    configure = request.values.get('configure')
    receipt_date = request.values.get('receipt_date')
    order_date = request.values.get('order_date')
    shipmemt_date = request.values.get('shipmemt_date')
    arrival_date = request.values.get('arrival_date')
    acceptment_date = request.values.get('acceptment_date')
    due_date = request.values.get('due_date')
    remind_need = request.values.get('remind_need')
    remark = request.values.get('remark')
    if len(contract_id) == 0:
        return jsonify({"code": 500, "msg": "请填写合同编号"})
    elif len(customer) == 0:
        return jsonify({"code": 500, "msg": "请选择客户"})
    elif len(vender) == 0:
        return jsonify({"code": 500, "msg": "请选择原厂"})
    elif len(saleman) == 0:
        return jsonify({"code": 500, "msg": "请选择销售人员"})
    elif len(configure) == 0:
        return jsonify({"code": 500, "msg": "请填写配置"})
    elif len(due_date) == 0:
        return jsonify({"code": 500, "msg": "请填写维保到期日"})
    else:
        Contractdb().contract_motify_updtae(contract_id, customer, vender, saleman, configure, receipt_date, order_date,
                                      shipmemt_date, arrival_date, acceptment_date, due_date, remind_need, remark)
        return jsonify({"code": 200, "msg": "保存成功"})


@mod.route('/contract_detail',methods=['POST', 'GET'])
def contract_detail():
    contract_id = request.args.get("contract_id")
    data= Contractdb().display_contract_detail(contract_id)
    return render_template('util/contract_detail.html',data=data)


@mod.route('/contract_download',methods=['POST', 'GET'])
@user.authorize
def contract_down_load():
    name,upload_path= ExeclOperation().made_all_contract()
    return send_file(upload_path)

