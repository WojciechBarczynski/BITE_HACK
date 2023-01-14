import pymysql
import pandas as pd

default_rating = 1000

class TaskEntry:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating
        
def get_users_df():
    connection = pymysql.connect(
        host="mysql.agh.edu.pl", 
        user="swoznia2",
        password="rMBsvPsTJQ8etui0",
        database="swoznia2"
        )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            database_output = cursor.fetchall()
    finally:
        connection.close()
    
    users_list = []
    for database_entry in list(database_output):
        users_list.append(TaskEntry(*database_entry))
    
    return pd.DataFrame.from_records(user.__dict__ for user in users_list)


def create_user(user_name):
    users = get_users_df()
    new_id = users['id'].max() + 1
    
    connection = pymysql.connect(
        host="mysql.agh.edu.pl", 
        user="swoznia2",
        password="rMBsvPsTJQ8etui0",
        database="swoznia2"
        )
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (ID, Name, Rating)" + "\n" + "VALUES (%s, %s, %s)"
            val = (f"{new_id}", f"{user_name}", f"{default_rating}")
            cursor.execute(sql, val)
            connection.commit()
    finally:
        connection.close()
    return new_id
    

