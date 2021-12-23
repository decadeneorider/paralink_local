from flask import render_template, jsonify, request, session, Blueprint, g
from system.db.vender_db import Venderdb
from system.views import user


mod = Blueprint('vender', __name__, template_folder='templates')

@mod.route('/vender',methods=['POST', 'GET'])
@user.authorize
def vender():
    return render_template('util/vender.html')


@mod.route('/vender.json', methods=['POST', 'GET'])
@user.authorize
def vender_json():
    vender_infor = Venderdb().get_all_vender()
    data1 = jsonify({'total': len(vender_infor), 'rows': vender_infor})
    return data1, {'Content-Type': 'application/json'}


@mod.route('/add_vender', methods=['POST', 'GET'])
@user.authorize
def vender_add():
    vender_name = request.values.get("vender_name")
    print(vender_name)
    if vender_name ==None or vender_name =="":
        return jsonify({"code": 500, "msg": "请填写原厂名称"})
    else :
        Venderdb().vender_add(vender_name)
        return jsonify({"code": 200, "msg": "添加成功"})


@mod.route('/del_vender', methods=['POST', 'GET'])
@user.authorize
def vender_del():
     id= request.values.get("id")
     if id ==0 or id ==None or id =="":
         return jsonify({"code": 500, "msg": "请选择需要删除的销售人员"})
     else:
         Venderdb().vender_del(id)
         return jsonify({"code": 200, "msg": "删除成功"})