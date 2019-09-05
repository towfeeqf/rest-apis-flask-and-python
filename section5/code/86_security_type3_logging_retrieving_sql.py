
from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username,passowrd):
    user= User.find_by_username(username)        ### now we dont use user=username_mapping.get(username,None)
    if user and safe_str_cmp(user.password, passowrd): #if user and user.passowrd==passowrd:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)          ####userid_mapping.get(user_id,None)
