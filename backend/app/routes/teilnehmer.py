from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Fertigungsmaschine
import json
import logging
from pathlib import Path

# Set up logger for this module
logger = logging.getLogger(__name__)

router = APIRouter()

# Path to the JSON data file
DATA_FILE = Path(__file__).parent.parent / "data/fertigungsmaschinen.json"

def read_fertigungsmaschinen_data():
    """
    Reads and returns the data from the Fertigungsmaschinen JSON file.
    """
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error reading Fertigungsmaschinen data file: {e}")
        raise

@router.get("/", response_model=List[Fertigungsmaschine])
async def get_fertigungsmaschinen():
    """
    Retrieves a list of all Fertigungsmaschinen.

    Each Fertigungsmaschine includes details such as system names, interfaces,
    IP and MAC addresses, VLAN, and other relevant information.

    Returns:
        A list of Fertigungsmaschinen as defined in the Fertigungsmaschine model.
    """
    try:
        data = read_fertigungsmaschinen_data()
        logger.info("Successfully retrieved Fertigungsmaschinen data.")
        return data["fertigungsmaschinen"]
    except Exception as e:
        logger.error(f"Error retrieving Fertigungsmaschinen data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Add more routes here for further management of Fertigungsmaschinen
