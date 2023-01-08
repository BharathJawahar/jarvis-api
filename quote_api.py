from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/quote")
async def root():
    lines = open("quote.txt", "r").readlines()
    n = len(lines)
    for i in range(random.randint(0,n-1)):
        random.shuffle(lines)
    return lines[random.randint(0,n-1)][:-1]
