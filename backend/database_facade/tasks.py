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
    tasks_list = get_tasks()
    return pd.DataFrame.from_records(task.__dict__ for task in tasks_list)

def get_tasks():
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
    return tasks_list

def update_task_rating(task_id, new_rating):
    connection = pymysql.connect(
        host="mysql.agh.edu.pl", 
        user="swoznia2",
        password="rMBsvPsTJQ8etui0",
        database="swoznia2"
        )
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE tasks" + " SET Rating = " + "'%s'" + " WHERE ID = " + "'%s'"
            val = (new_rating, task_id)
            cursor.execute(sql, val)
            connection.commit()
    finally:
        connection.close()

def get_solution_url(task_id):
    tasks = get_tasks()
    return list(filter(lambda task: task.id == task_id, tasks))[0].solution_link
    