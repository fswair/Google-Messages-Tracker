from fastapi import FastAPI
from utilities.getlast import get_last

app = FastAPI()

@app.get("/getMessages")
def read_root(lastmin: int = None):
    return get_last(lastmin)

import uvicorn

uvicorn.run(app, port=8080)