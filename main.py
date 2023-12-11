from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()


@app.get("/pro_players")
async def read_root():
    filename = "pro_players_data.json"
    return FileResponse(filename)

@app.get("/heroes")
async def read_root():
    filename = "heroes_data.json"
    return FileResponse(filename)