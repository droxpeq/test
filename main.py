from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html") as f:
        return f.read()

@app.get("/page1", response_class=HTMLResponse)
async def page1():
    with open("page1.html") as f:
        return f.read()

@app.get("/page2", response_class=HTMLResponse)
async def page2():
    with open("page2.html") as f:
        return f.read()
