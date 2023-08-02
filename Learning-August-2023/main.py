from typing import Union

from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

'''
    Info about Union keyword:
    An interesting tool that the Python typing library gives us, is Union. 
    This is a special keyword, which allows us to specify multiple allowed 
    datatypes, instead of a single one. If for example, we wanted a string 
    that allows both integers and strings, how would we do so? 
    This is where Union helps.
    Link: https://coderslegacy.com/python/union-in-typing/
'''

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q
    }