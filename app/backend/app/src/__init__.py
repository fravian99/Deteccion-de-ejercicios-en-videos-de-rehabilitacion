import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

HOST = '0.0.0.0'
PORT = 4200

"""origins = [
    "http://localhost:" + str(PORT),
    HOST + ":" + str(PORT),
]"""

app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/test")
async def main():
    return {"message": "Hello World"}

