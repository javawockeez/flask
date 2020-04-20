from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity #from security.py
from resources.user import UserRegister
from resources.item import Item, ItemList#from db import db
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turnning off modification flaskalchemy tracker, but not SQLAlchemy tracker
app.secret_key = 'jose' #should not be shown lol
api = Api(app)#will create all tables before any action, unless they already exist and wi# only creates tables that SQLAlchemy sees (importing from other .py files)
jwt = JWT(app,authenticate,identity) # /auth is endpoint

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register') #post request

if __name__ =='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) #will produce HTML page with errors


# from class Item / function get
                                                    # None acts as default
        # lambda function same as for loop below
        # for item in items:
        #     if item['name'] ==name:
        #         return item
