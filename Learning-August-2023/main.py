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

'''

Open your browser at http://127.0.0.1:8000/items/5?q=somequery.

You will see the JSON response as:
{"item_id": 5, "q": "somequery"}

You already created an API that:

Receives HTTP requests in the paths / and /items/{item_id}.
Both paths take GET operations (also known as HTTP methods).
The path /items/{item_id} has a path parameter item_id that should be an int.
The path /items/{item_id} has an optional str query parameter q.
'''

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q
    }