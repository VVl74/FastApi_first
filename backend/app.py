# This is a sample Python script.

from fastapi import FastAPI

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()

@app.get("/")
def func():
    return "GOOOOOOOL"

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "Service is running"}

@app.get("/echo/{text}")
def echo(text: str):
    return {"original_text": text, "reversed": text[::-1]}



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


