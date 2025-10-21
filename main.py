from fastapi import FastAPI

app = FastAPI()
# teste do pipeline
@app.get("/")
async def root():
    return {"message": "Hello World"}
