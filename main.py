from fastapi import FastAPI
from src.controller import student_router
import uvicorn

app = FastAPI()

app.include_router(student_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
