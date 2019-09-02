from flask import Flask,request
from flask_restful import Resource, Api 

app=Flask(__name__)
api=Api(app)

#items = []          #instead of database we use memory database .... the list contains a dictionary of items 
# we should be able to get items and also create item
# we will start with those 2 capabilities
# later, we will then add the ability to modify and delete items

items= []

class Item(Resource):
    def get(self,name):
        for item in items:
            if item['name']==name:
                return item # 200 Ok if item found
        return {'item': None},404
        #return {'message': 'item not found'},404   # 200 OK is standard response for successful http request
        
        # if the specific item is not found... we throw a message error 404
        # flask-restful does the jsonify..so we dont have to jsonify the 

    # for creating item, we will use POST and without looking at JSON 
    # for implementing the POST, we need to modify the GET method as above

#    def post(self,name):  # it will have json payload
#        item ={
#            'name': name,   
#            'price': 12.00
#        }


    def post(self,name):  # it will have json payload
        request_data=request.get_json()
        item ={
            'name': request_data['name'],   
            'price': request_data['price']
        }
        items.append(item)
        return item, 201   # 201 is standard new response being created

class ItemList(Resource):
    def get(self):
        return {'items':items}



#api.add_resource(Item,'/item/<string:name>')   # http://127.0.0.1:5000/student/towfeeq

api.add_resource(Item,'/item/<string:name>')   # http://127.0.0.1:5000/student/towfeeq

api.add_resource(ItemList,'/items')

app.run(port=5000,debug=True)
 