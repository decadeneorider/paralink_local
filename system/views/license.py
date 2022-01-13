from flask import render_template, jsonify, request, session, Blueprint, g
from system.views import user
from system.db.license_db import Licensedb
from system.db.contract_db import Contractdb
import os


mod = Blueprint('license', __name__, template_folder='templates')



@mod.route('/license_manage',methods=['POST', 'GET'])
@user.authorize
def license_manage():
    return render_template('util/license_manage.html')


@mod.route('/license_manage.json',methods=['POST', 'GET'])
@user.authorize
def license_manage_json():
    result = Licensedb().all_license()
    license_manage_results = []
    for row in result:
        license_manage_result = {}
        license_manage_result['id'] = row[0]
        license_manage_result['customer_name'] = row[1]
        license_manage_result['customer_department'] = row[2]
        license_manage_result['customer_linkman'] = row[3]
        license_manage_result['kit_type'] = row[4]
        license_manage['contract_id'] = row[5]
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
    return jsonify({'total': len(license_manage_results), 'rows': license_manage_results[int(offset):(int(offset) + int(limit))]})


@mod.route('/add_license_manage.json',methods=['POST', 'GET'])
@user.authorize
def add_license_manage_json():
    customer_name = request.values.get('customer_name')
    customer_department = request.values.get('customer_department')
    customer_linkman = request.values.get('customer_linkman')
    kit_type = request.values.get('kit_type')
    contract_id = request.values.get('contract_id')
    result1 = Contractdb().get_contract_id(contract_id)
    if customer_name =="" or customer_name ==None:
        return jsonify({"code": 500, "msg": "请填写客户名称"})
    elif contract_id =="" or contract_id ==None:
        return jsonify({"code": 500, "msg": "请填写合同编号"})
    elif  len(result1) == 0:
        return jsonify({"code": 500, "msg": "填写正确的合同编号"})
    else:
        Licensedb().add_license_manage(customer_name,customer_department,customer_linkman,kit_type,contract_id)




@mod.route('/upload_license_file',methods=['POST', 'GET'])
@user.authorize
def upload_license_file():
    file = request.files['file']
    basepath = os.path.abspath('.')  # 当前文件所在路径
    upload_path = os.path.join(basepath,"system","email_file",file.filename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    print(upload_path)
    print(file)
    file.save(upload_path)
    fil_name = str(file.filename)
    message = "上传成功"
    return ({"code": 200, "msg": "发送成功","file_name":fil_name ,"message":message})