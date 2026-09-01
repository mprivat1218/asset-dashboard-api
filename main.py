from fastapi import FastAPI

app = FastAPI(title="Asset & Risk Dashboard")

@app.get("/")
def read_root():
    return {"status":"dashboard API is running"}

