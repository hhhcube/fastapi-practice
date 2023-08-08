from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor
import time
# ------------------------------------------------------------------


# create an instance of FastAPI
app = FastAPI()


# Class representation of a Post extending Pydantic BaseModel
#  Does validation and schema for frontend to send to us
# e.g. title str, content str, category str, published or draft bool

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None


# ------------  Connect to our Database using SQL until true using while statement--------------------
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='chat247now', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
        print("Connecting to database failed")
        print("error: ", error)
        time.sleep(2)


# Temporary store post in memeory until I build database
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
             {"title": "title of post 2", "content": "I like pizza", "id": 2}]


# ------------ Functions -----------------

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        

#  --------------------------create path operations ----------------------------------
@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/posts")
def get_posts():

    cursor.execute("""SELECT * FROM post""")
    
    posts = cursor.fetchall()
    
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED) 
def create_posts(post: Post): # Stored as a pydantic modal
    
    cursor.execute("""INSERT INTO post (title, content, published) VALUES (%s, %s, %s) RETURNing * """, (post.title, post.content, post.published)) # prevent SQL injections by using placeholders and varables outside of SQL statememnt
    
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


@app.get("/post/{id}") # validation with pydantic "id: int"
def get_post(id: int):

    cursor.execute(""" SELECT * FROM post WHERE id = %s """, (str(id),))
   
    post = cursor.fetchone()
    conn.commit()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return{"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) # When you delete you want to send the 204 status code
def delete_post(id: int):

    cursor.execute(""" DELETE FROM post WHERE id = %s RETURNING * """, (str(id),))

    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT) # Need to send 204 whenever we delete from database


@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    cursor.execute(""" UPDATE post SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, (str(id)),))

    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    
    return {'data': updated_post}

# Path opertions End-------------------