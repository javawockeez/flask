from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', #only price is listed, so any other argumetn will be ignored
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('store_id', #only price is listed, so any other argumetn will be ignored
        type=int,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required() #auth is required bfore functions can run
    def get(self,name):
        item = ItemModel.find_by_name(name) #returns item object
        if item:
            return item.json() #add json() due to item object property
        return {'message': 'Item not found'}, 404

    def post(self,name):
        if ItemModel.find_by_name(name): # replaces lambda function taht looks through list objects
            return {'message': "An item with name'{}' already exists.".format(name)}, 400 #request is wrong

        data = Item.parser.parse_args()

        item = ItemModel(name, **data) #data['price'], data['store_id']) # replaces {'name':name, 'price':data['price']}

        try:
            item.save_to_db()# replaces ItemModel.insert(item)
        except:
            return {'message': 'An error occurred inserting the item.'}, 500 #internal server error

        return item.json(), 201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item Deleted'}

    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data) #data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x:x.json(),ItemModel.query.all()))}# 1.) list comprehension[item.json() for item in ItemModel.query.all()]}| # replacing return {'items':ItemModel.query.all()}
