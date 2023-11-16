from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import Fertigungsmaschine  # Import the model
from .routes import fertigungsmaschinen, teilnehmer
import json
from pathlib import Path

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
    with open(DATA_FILE, "r") as file:
        return json.load(file)

@app.get("/fertigungsmaschinen", response_model=List[Fertigungsmaschine])
async def get_all_fertigungsmaschinen():
    data = read_fertigungsmaschinen_data()
    return data["fertigungsmaschinen"]

@app.get("/fertigungsmaschinen-count")
def get_fertigungsmaschinen_count():
    data = read_fertigungsmaschinen_data()
    return {"count": len(data["fertigungsmaschinen"])}

# Add any additional endpoint definitions here