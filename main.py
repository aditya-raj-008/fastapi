from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()
@app.get('/blog')
def index(limit=10,published:bool =True, sort: Optional[str]= None):
    #return "heyy"
    if published:
        return {'data':f'{limit}blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/about') 
def about():
    return {'data':'about page'}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title:str
    body:str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f'blog is created with title as{blog.title}'}

if __name__=="main":
    uvicorn.run(app,host="127.0.0.1",port=9000)
