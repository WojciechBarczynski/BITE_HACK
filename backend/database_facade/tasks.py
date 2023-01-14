import pymysql
import pandas as pd

class TaskEntry:
    def __init__(self, task_id, question_link, solution_link, answer, rating, description):
        self.id = task_id
        self.question_link = question_link
        self.solution_link = solution_link
        self.answer = answer
        self.rating = rating
        self.description = description

def get_tasks_df():
    connection = pymysql.connect(
        host="mysql.agh.edu.pl", 
        user="swoznia2",
        password="rMBsvPsTJQ8etui0",
        database="swoznia2"
        )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks")
            database_output = cursor.fetchall()
    finally:
        connection.close()
    
    tasks_list = []
    for database_entry in list(database_output):
        tasks_list.append(TaskEntry(*database_entry))
    
    return pd.DataFrame.from_records(task.__dict__ for task in tasks_list)