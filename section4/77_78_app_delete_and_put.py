from flask import Flask,request  # jwt jason web token
from flask_restful import Resource, Api 

from flask_jwt import JWT, jwt_required

from security import authenticate,identity

app=Flask(__name__)
app.secret_key='tf123'
api=Api(app)

jwt =JWT(app,authenticate,identity)     #auth  endpoint

#items = []          #instead of database we use memory database .... the list contains a dictionary of items 
# we should be able to get items and also create item
# we will start with those 2 capabilities
# later, we will then add the ability to modify and delete items

items= []

class Item(Resource):
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name']==name , items), None) 
        #item = next(filter(lambda x:x['name']==name ,items),"item not found") 
        return {'item':item}, 200 if item else 404  # 200 if item found and 404 if not found

    def post(self,name):  # it will have json payload
        if next(filter(lambda x: x['name']==name , items), None):
            return {'message': 'an item with the name {} already exists'.format(name)}, 400 ## 400 is for http bad request
        
        request_data=request.get_json()
        item ={
            'name': name,   
            'price': request_data['price']
        }
        items.append(item)
        return item, 201   # 201 is standard new response being created
    
    def delete(self,name):
        global items
        items=list(filter(lambda x: x['name']!=name, items))
        return {'message': 'Item deleted'}
    
    
    def put(self,name):
        request_data=request.get_json()

        item = next(filter(lambda x: x['name'],names),None)
        if item is None:
            item ={
                'name': name, 
                'price': request_data['price']
                }
            items.append(item)
        else:
            item.update(request_data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items':items}

#api.add_resource(Item,'/item/<string:name>')   # http://127.0.0.1:5000/student/towfeeq

api.add_resource(Item,'/item/<string:name>')   # http://127.0.0.1:5000/student/towfeeq

api.add_resource(ItemList,'/items')

app.run(port=5000,debug=True)
 