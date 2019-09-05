from flask import Flask  # jwt jason web token
from flask_restful import Api

from flask_jwt import JWT

from security import authenticate,identity
from user import UserRegister

from item import Item, ItemList

app=Flask(__name__)
app.secret_key='tf123'
api=Api(app)

jwt =JWT(app,authenticate,identity)     #auth  endpoint

#items = []          #instead of database we use memory database .... the list contains a dictionary of items 
# we should be able to get items and also create item
# we will start with those 2 capabilities
# later, we will then add the ability to modify and delete items

#api.add_resource(Item,'/item/<string:name>')   # http://127.0.0.1:5000/student/towfeeq

api.add_resource(Item,'/item/<string:name>')   # http://127.0.0.1:5000/student/towfeeq

api.add_resource(ItemList,'/items')

api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    app.run(port=5000,debug=True)
 