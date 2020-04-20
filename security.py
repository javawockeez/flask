from werkzeug.security import safe_str_cmp # for py27
from models.user import UserModel

def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #takes away requirement for ==, takes 2 arguments instead
        return user

def identity(payload): #payload = JWT content
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
# User.find_by_username(username) replaces username_mapping.get(username, None)
# User.find_by_id(user_id) replaces userid_mapping.get(user_id, None)
# mapping to users list is not being used anymore since
# User class is being used isntead
# users = [
#     User(1, 'bob', 'asdf')
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}
