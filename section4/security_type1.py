users=[
    {
        'id' =1,
        'username': 'bob'
        'passowrd': 'asdf'
    }
]

username_mapping={'bob':{
        'id' =1,
        'username': 'bob'
        'passowrd': 'asdf'
    }
}

userid_maping = { 1 :{
        'id' =1,
        'username': 'bob'
        'passowrd': 'asdf'
    }
}

def authenticate(username,passowrd):
    user=username_mapping.get(username,None)
    if user and user.passowrd==passowrd:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)
