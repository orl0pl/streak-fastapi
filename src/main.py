from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
import requests
from dataclasses import dataclass
from workers import WorkerEntrypoint,  Response

from services import fetch_userdata, get_user_streak, simplify_user_data

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse('index.html')

@app.get("/user/{username}")
def read_user(username: str):
    response = fetch_userdata(username)
    if response.data:
        if len(response.data["users"]) > 0:
            return simplify_user_data(response.data["users"][0])
        else:
            return JSONResponse(status_code=404, content={"error": "User with username '" + username + "' not found"})
    return JSONResponse(status_code=500, content={"error": response.error})
    

@app.get("/streak/{username}")
def read_streak(username: str):
    response = fetch_userdata(username)
    if response.data:
        if len(response.data["users"]) > 0:
            return get_user_streak(response.data["users"][0])
        else:
            return JSONResponse(status_code=404, content={"error": "User with username '" + username + "' not found"})
    return JSONResponse(status_code=500, content={"error": response.error})

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return Response("Haiii! Cloudflare ")