import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self,_id,username,password):
        self.id =_id
        self.username = username
        self.password = password
    

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor=connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result=cursor.execute(query,(username,))   # single value tuple can be by using (username,)

        row = result.fetchone() # it gets the first row out of the result set, if there are no rows, the result will fetch none

        if row:  # ##### if row is not None:
            user =cls(*row)  ###(row[0],row[1],row[2])
        else:
            user = None

        connection.close()          # we did not any data so we do not write connection.commit()
        return user


    # we are not using self but we are using the class method User... so change User to cls and write classmethod

    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor=connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result=cursor.execute(query,(_id,))   # single value tuple can be by using (username,)

        row = result.fetchone() # it gets the first row out of the result set, if there are no rows, the result will fetch none

        if row:  # ##### if row is not None:
            user =cls(*row)  ###(row[0],row[1],row[2])
        else:
            user = None

        connection.close()          # we did not any data so we do not write connection.commit()
        return user


    # now we have two mappings: mapping by username and then mapping by id

class UserRegister(Resource):   #  this is like a resource just like an item in item list was. we coud just create flask end point 
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required = True,
    help = "This field cannot be left blank"
    )

    parser.add_argument('password',
    type=str,
    required = True,
    help = "This field cannot be left blank"
    )


    def post(self):
        data= UserRegister.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL,?,?)"

        cursor.execute(query,(data['username'],data['password'],))


        connection.commit()
        connection.close()

        return {'message': 'user created successfully'}, 201       # 201 created successfully 

        
        
