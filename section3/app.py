# simulate online store using flask

from flask import Flask,jsonify, request, render_template
app = Flask(__name__)

stores =[ 
    {
        'name': "my wonderful store",
        'items':[
                    {
                        'name': 'my item',
                        'price': 15.99
                    }

                ]        
    }
]


@app.route('/')
def home():
    return render_template('index.html')


# Creating our applicaton endpoints

# POST /store data: {name:}  # create a store with a given name 
@app.route('/store', methods = ['POST']) # by default @app.route is a GET request so we mention POST methods
def create_store():
    request_data=request.get_json() # request is the one that is made to the end point /store and the browser will
                                    # send us some json data , the name of the store.
    new_store={
        'name':request_data['name'],
        'items':[]
    }                               
    stores.append(new_store)
    return jsonify(new_store)
#GET /store/<string:name>   # get a store with a given name and extra information
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})                         # to retrieve a specific store...iterate over the stores finding the one that matches 
                            # this name and returning that one 
                            # if none matches, return error message

# GET /store        # returns the list of all the stores
@app.route('/store')
def get_stores():   
    return jsonify({'stores': stores})   #jsonify convert the variable stores into json 
    # we want to return not a single store but a dictionary with all our stores

    # implementation of first end point

# POST /store/<string:name>/item {name:,price}  # create a item inside a specific store
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name': request_data['name'],
                'price':request_data['price']    
            }
            store['items'].append(new_item)
            return jsonify(new_item)  # or jsonify(store)
    return jsonify({'message': 'store not found'})      
    
# GET /store/<string:name>/item # get all the items in the given store 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


# Returning a list of End points  --- done preparing the end points 

# Implementing other end points

app.run(debug=True,port=5000)







