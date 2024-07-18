from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import Optional, List
from random import randrange
import psycopg2 # type: ignore
from routers import posts, users, authentication
# from psycopg2.extras import RealDictCursor # type: ignore
# import time
import models
# from . import models, schemas, utils
from database import engine, get_db



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(authentication.router)
    
# while True:
#     try:
#         connection = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres',
#                                   password = 'postgres', cursor_factory= RealDictCursor)
#         cursor = connection.cursor()
#         print("Connection established")
#         break
#     except Exception as error:
#         print("Connection: failed")
#         print("error", error)
#     # time.sleep(2)


# my_posts = [{"title": "Here on the moon", "body": "gravity is very less", "id": 1},
#             {"title": "My favorite food", "body": "I love Biryani and karahi", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
        

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
        
@app.get("/")
def read_root():
    return {"Hello": "World"}




