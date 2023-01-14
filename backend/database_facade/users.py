import pymysql
import pandas as pd

class TaskEntry:
    def __init__(self, task_id, name, rating):
        self.id = task_id
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

print(get_users_df())