from fastapi import FastAPI

app=FastAPI()
@app.get('/')
def index():
    #return "heyy"
    return {'data':{'name':'Sarthak'}}

@app.get('/about') 
def about():
    return {'data':'about page'}
