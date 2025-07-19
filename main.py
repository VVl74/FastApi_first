
from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/html", response_class=HTMLResponse)
def html():
    return """
    <html>
        <body>
            <b>HHHH</b>
        </body>
    </html>
    """