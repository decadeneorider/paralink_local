from random import choice
from flask import Flask, jsonify, render_template, request,Blueprint
from system.db.contract_db import Contractdb
from system.views import user


mod = Blueprint('test', __name__, template_folder='templates')




@mod.route('/test')
def hi():
    return render_template('util/customer_motify.html')
