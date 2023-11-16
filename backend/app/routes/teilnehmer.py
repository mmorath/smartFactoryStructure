# fertigungsmaschinen.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Fertigungsmaschine
import json
from pathlib import Path

router = APIRouter()

DATA_FILE = Path(__file__).parent.parent / "data/fertigungsmaschinen.json"

def read_fertigungsmaschinen_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

@router.get("/", response_model=List[Fertigungsmaschine])
async def get_fertigungsmaschinen():
    data = read_fertigungsmaschinen_data()
    return data["fertigungsmaschinen"]

# Weitere Routen zur Verwaltung der Fertigungsmaschinen
