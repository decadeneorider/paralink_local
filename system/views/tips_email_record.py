from flask import render_template, jsonify, request, session, Blueprint, g
from system.db.contract_db import Tipsdb,Contractdb
from system.views import user


mod = Blueprint('tips_contract_record', __name__, template_folder='templates')

@mod.route('/tips_record_display')
@user.authorize
def tips_display():
    return render_template('util/tips_record.html')


@mod.route('/tips_record_display.json',methods=['POST', 'GET'])
@user.authorize
def tips_record_display_json():
    result =  Tipsdb().tips_conmtract_all()
    tips_infors = []
    for row in result:
        tips_infor = {}
        tips_infor['id'] = row[0]
        tips_infor['contract_id'] = row[1]
        tips_infor['customer'] = row[2]
        tips_infor['saleman'] = row[3]
        tips_infor['due_date'] = row[4].strftime('%Y-%m-%d')
        tips_infor['tips_number'] = row[5]
        tips_infors.append(tips_infor)
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
    return jsonify({'total': len(tips_infors), 'rows': tips_infors[int(offset):(int(offset) + int(limit))]})


@mod.route('/tips_update',methods=['POST', 'GET'])
@user.authorize
def tips_update():
    contract_id = request.values.get("id")
    Contractdb().remind_need_update(contract_id)
    return jsonify({"code": 200,})