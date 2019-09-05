import sqlite3
from flask import Request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    @jwt_required()
    def get(self,name):             # retrieve items from the database 
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items WHERE name =?"
        result = cursor.execute(query,(name,))  

        row = result.fetchone()
        
        # connection.commit()  we are not adding any new info or data so need not use commit
        connection.close()

        if row:
            return {'item': { 'name' : row[0], 'price': row[1]}}

        return {'message': 'item not found'},404   # we do not use else because it is kind of logically same

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
        parser=reqparse.RequestParser()
        parser.add_argument('price',
        type = float,
        required=True,
        help = 'This field cannot be left blank')
        
        request_data=parser.parse_args()
        #request_data=request.get_json()
        item = next(filter(lambda x: x['name'],items),None)
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
