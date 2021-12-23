from flask import Flask
from flask_bootstrap import Bootstrap
from flask_caching import Cache
# from flask_session import Session
# from flask_wtf import CSRFProtect

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

Bootstrap(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

from system.views import user
from system.views import contract
from system import view
from system.views import customer
from system.views import vender
from system.views import test
from system.views import company_group
from system.views import tips_email_record
app.register_blueprint(user.mod)
app.register_blueprint(contract.mod)
app.register_blueprint(customer.mod)
app.register_blueprint(vender.mod)
app.register_blueprint(test.mod)
app.register_blueprint(company_group.mod)
app.register_blueprint(tips_email_record.mod)

