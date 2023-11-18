from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import Fertigungsmaschine  # Import the model
from .routes import fertigungsmaschinen, teilnehmer
import json
import logging
from pathlib import Path

# Configure logging for this module
logger = logging.getLogger(__name__)

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include the routers from the fertigungsmaschinen and teilnehmer modules
app.include_router(fertigungsmaschinen.router, prefix="/fertigungsmaschinen", tags=["fertigungsmaschinen"])
app.include_router(teilnehmer.router, prefix="/teilnehmer", tags=["teilnehmer"])

# Path to the JSON file
DATA_FILE = Path(__file__).parent / "data/fertigungsmaschinen.json"

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

@app.get("/fertigungsmaschinen", response_model=List[Fertigungsmaschine])
async def get_all_fertigungsmaschinen():
    """
    Endpoint to retrieve a list of all Fertigungsmaschinen.
    Returns a list of Fertigungsmaschinen as defined in the Fertigungsmaschine model.
    """
    try:
        data = read_fertigungsmaschinen_data()
        logger.info("Successfully retrieved Fertigungsmaschinen data.")
        return data["fertigungsmaschinen"]
    except Exception as e:
        logger.error(f"Error retrieving Fertigungsmaschinen data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fertigungsmaschinen-count")
def get_fertigungsmaschinen_count():
    """
    Endpoint to get the count of all Fertigungsmaschinen.
    Returns the total count of Fertigungsmaschinen.
    """
    try:
        data = read_fertigungsmaschinen_data()
        return {"count": len(data["fertigungsmaschinen"])}
    except Exception as e:
        logger.error(f"Error counting Fertigungsmaschinen: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Add any additional endpoint definitions here
