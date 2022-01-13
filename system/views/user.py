from flask import render_template, jsonify, request, session, Blueprint, g
from system.db.user_db import test_user_manager
from functools import wraps
from system.function.yaml_handle import ReadHandle
import os



mod = Blueprint('user', __name__, template_folder='templates')


configure_file = os.path.abspath('.')

configure_data = ReadHandle(f'{configure_file}/system/configure/authority_configure.yaml').yaml_files_read()

# 设置登录认证
def authorize(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = session.get('user', None)
        if user:
            g.user_name = user[0].get('username')
            g.user_id = user[0].get('id')
            return fn(*args, **kwargs)
        else:
            return render_template("util/login.html")

    return wrapper

@mod.route('/')
def login():
    return render_template('util/login.html')


# 检查登陆
@mod.route('/checklogin.json', methods=['POST', 'GET'])
def checklogin():
    username = request.values.get('username')
    password = request.values.get('password')
    remember = request.values.get('remember')
    if username == '' or password == '':
        result = jsonify({'msg': '用户名或密码不能为空'})
    else:

        # 检查用户是否存在
        res_list = test_user_manager().check_login(username, password, db_type_num=1)
        if len(res_list) > 0:
            result = jsonify({'msg': '登录成功'})
            # 登录成功设置会话
            session['user'] = res_list
            if remember:
                session.permanent = True
        else:
            result = jsonify({'msg': '用户名或密码错误'})
    return result, {'Content-Type': 'application/json'}

@mod.route('/user',methods=['POST', 'GET'])
@authorize
def user():
    user_list = session.get('user', None)
    user_position = user_list[0]['position']
    return render_template('util/user.html',configure_data = configure_data,user_position=user_position)


@mod.route('/user.json', methods=['POST', 'GET'])
@authorize
def user_json():
    user_infor = test_user_manager().get_all_user()
    data1 = jsonify({'total': len(user_infor), 'rows': user_infor})
    return data1, {'Content-Type': 'application/json'}


@mod.route('/add_user', methods=['POST', 'GET'])
@authorize
def user_add():
    username = request.values.get("username")
    pwd = request.values.get("password")
    email = request.values.get("email")
    position1 = request.values.get("position1")
    print(username)
    if username ==None or username =="":
        return jsonify({"code": 500, "msg": "请填写用户名称"})
    if pwd ==None or pwd =="":
        return jsonify({"code": 500, "msg": "请填写用户密码"})
    if email ==None or email =="":
        return jsonify({"code": 500, "msg": "请填写用户邮箱"})
    else :
        test_user_manager().add_user(username,pwd,email,position1)
        return jsonify({"code": 200, "msg": "修改成功"})


@mod.route('/del_user', methods=['POST', 'GET'])
@authorize
def user_del():
     id= request.values.get("id")
     if id ==0 or id ==None or id =="":
         return jsonify({"code": 500, "msg": "请选择需要删除的用户"})
     else:
         test_user_manager().user_del(id)
         return jsonify({"code": 200, "msg": "删除成功"})



@mod.route('/user_password',methods=['POST', 'GET'])
@authorize
def user_password():
    return render_template('util/password_change.html')


@mod.route('/user_password.json', methods=['POST', 'GET'])
@authorize
def user_password_json():
     user_list = session.get('user', None)
     user_id = user_list[0]['id']
     password  = request.values.get("user_password")
     if password ==0 or password ==None or password =="":
         return jsonify({"code": 500, "msg": "请选择新的密码"})
     else:
         test_user_manager().user_password(user_id, password)
         return jsonify({"code": 200, "msg": "修改成功"})