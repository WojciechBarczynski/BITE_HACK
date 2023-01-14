import sys
import os
dir = os.path.dirname(__file__)
filepath = os.path.join(dir, '../..')
sys.path.insert(0, filepath)

from backend.database_facade.users import get_users_df, create_user


def login_user(req_user_name):
    db_users = get_users_df()
    user = db_users.loc[db_users['name'] == req_user_name]
    match len(user.index):
        case 0:
            return create_user(req_user_name)
        case 1:
            return user['id'].values[0]
        case other:
            raise "More than one user with same name in db!!!"
