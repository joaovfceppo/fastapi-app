from fastapi import FastAPI

app = FastAPI()
# teste do pipeline
@app.get("/")
async def root():
    return {"Mensagem teste para verificar se o CI/CD está funcionando!"}
