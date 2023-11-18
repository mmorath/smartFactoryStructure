from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Fertigungsmaschine
import json
import logging
from pathlib import Path

# Configure logging for this module
logger = logging.getLogger(__name__)

router = APIRouter()

DATA_FILE = Path(__file__).parent.parent / "data/fertigungsmaschinen.json"

def read_fertigungsmaschinen_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error reading Fertigungsmaschinen data file: {e}")
        raise

@router.get("/", response_model=List[Fertigungsmaschine])
async def get_fertigungsmaschinen():
    try:
        data = read_fertigungsmaschinen_data()
        logger.info("Successfully retrieved Fertigungsmaschinen data.")
        return data["fertigungsmaschinen"]
    except Exception as e:
        logger.error(f"Error retrieving Fertigungsmaschinen data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Weitere Routen zur Verwaltung der Fertigungsmaschinen
