from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    complete: bool

tasks = {
    1: Task(
        title= "Do grocery shopping at 6",
        description= "buy sashimi, eggs, bananas",
        complete= True
    ),
        
    2: Task(
        title= "Do swimming for 40 laps",
        description= "don't forget to do warmups first",
        complete= False
    ),

    3: Task(
        title= "Learn a new song",
        description= "drink plenty of water",
        complete= True
    ),

    4: Task(
        title= "Submit web app homework before monday midnight",
        description= "feel free to procrastinate",
        complete= False
    )
}

filteredtasks = {
    1: Task(
        title= "Do grocery shopping at 6",
        description= "buy sashimi, eggs, bananas",
        complete= True
    ),
        
    2: Task(
        title= "Do swimming for 40 laps",
        description= "don't forget to do warmups first",
        complete= False
    ),

    3: Task(
        title= "Learn a new song",
        description= "drink plenty of water",
        complete= True
    ),

    4: Task(
        title= "Submit web app homework before monday midnight",
        description= "feel free to procrastinate",
        complete= False
    ),

}


class UpdateTask(BaseModel):
    title : Optional[str] = None
    description :Optional[str] = None
    complete:  Optional[bool] = None 


@app.get("/")
def index():
    return {"Message": "This is Tiffany's FastAPI Todo App"}

#get all tasks
@app.get("/get-all-tasks/")
def get_task():
    return tasks

#get task by ID
@app.get("/get-task-by-id/{task_id}")
def get_task(task_id: int = Path(description = "ID of task")):
    if task_id in tasks:
        return tasks[task_id]
    return {"Error" : "The task ID does not exist."}
    
#get task by title
@app.get("/get-task-by-title/{title}")
def get_task(title: str = Path(description= "Title of task")):
    for task_id in tasks:
        if tasks[task_id].title == title:
            return tasks[task_id]
        if tasks[task_id].title != title:
            return {"Error": "The task with this title does not exist"}

#get task by filter
@app.get("/get-task-by-filter/{complete}")
def get_task(complete: bool = Path(description= "Select true or false")):
    global filteredtasks
    filteredtasks.clear()
    for task_id in tasks:
        if tasks[task_id].complete == complete:
            filteredtasks[task_id] = tasks[task_id]
    return filteredtasks

#create task 
@app.post("/create-task/{task_id}")
def create_task(task_id: int, app:Task):
    if task_id in tasks:
        return {"Error": "The task with the same ID already exists"} 
    tasks[task_id] = app
    return tasks[task_id]

#update task
@app.put("/update-task/{task_id}")
def update_task(task_id:int, app: UpdateTask):
    if task_id not in tasks:
        return {"Error": "The task does not exist. Please check the task ID again."}
    if app.title != None:
        tasks[task_id].title = app.title
    if app.description != None:
        tasks[task_id].description = app.description
    if app.complete != None:
        tasks[task_id].complete = app.complete
    return tasks[task_id]

#delete task
@app.delete("/delete-task/{task_id}")
def delete_task(task_id:int):
    if task_id not in tasks:
        return {"Error" : "The task does not exist. Please check the task ID again."}
        del tasks[task_id]
        return {"Message": "The task has been deleted successfully"}
    

class User(BaseModel):
    name : str
    email : str

users = {
    11162: User(
        name="Hoshino Ai",
        email="hoshinoai19@gmail.com"),

    23479: User(
        name="Dazai Osamu",
        email="dazaiosamu@hotmail.com")
}

#get all users
@app.get("/get-all-users/")
def get_user():
    return users

#get user by uid
@app.get("/get-user-by-uid/{uid}")
def get_user(uid: int = Path(description="GET a user by uid")):
    if uid in users:
        return users[uid]
    return {"Error" : "UID doesn't exist."}

#get user by name
@app.get("/get-user-by-name/{name}")
def get_user(name: str = Path(description="GET name of the user")):
    for user_id in users:
        if users[user_id].name== name:
            return users[user_id]
    return {"Error": "The user does not exist"}

#get user by email
@app.get("/get-user-by-email/{email}")
def get_user(email: str = Path(description="GET email of the user")):
    for user_id in users:
        if users[user_id].email== email:
            return users[user_id]
    return {"Error": "The user does not exist"}

#create user
@app.post("/create-user/{uid}")
def create_user(uid: int, user: User):
    if uid in users:
        return {"Error":"The user already exists. Please select another uid"}
    if uid not in users:
        users[uid]=user
        return users[uid], {"Message": "User has been created successfully"}

#delete user
@app.delete("/delete-user/{uid}")
def delete_user(user_id:int):
    if user_id not in users:
        return {"Error" : "The user does not exist"}
    if user_id in users:
        del users[user_id]
        return {"Message": "User has been deleted successfully"}

