# Import the Config class
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .config.config import Config
from .database import get_db
from .routes import manufacturing_machine as manufacturing_machine_router
from .routes import participant as participant_router
import logging

# Configure logging for the application
logger = logging.getLogger(__name__)

# Create an instance of FastAPI
app = FastAPI(
    title=Config.FASTAPI_TITLE,           # Use configuration for title
    version=Config.FASTAPI_VERSION,       # Use configuration for version
    description=Config.FASTAPI_DESCRIPTION,  # Use configuration for description
    debug=Config.FASTAPI_DEBUG            # Use configuration for debug mode
)

# Setup CORS middleware for handling cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ALLOWED_ORIGINS,  # Use configuration for allowed origins
    allow_credentials=True,
    allow_methods=Config.ALLOWED_METHODS,  # Use configuration for allowed methods
    allow_headers=["*"]                   # Allows all headers
)

# Include routers for Manufacturing Machines and Participants
app.include_router(
    manufacturing_machine_router.router,
    prefix="/manufacturing_machines",
    tags=["manufacturing_machines"]
)
app.include_router(
    participant_router.router,
    prefix="/participants",
    tags=["participants"]
)

# Define an event handler for startup
@app.on_event("startup")
async def startup_event():
    # Perform startup tasks here
    # For example, create database tables
    Base.metadata.create_all(bind=engine)

# Define additional endpoint(s) if necessary
@app.get("/example")
async def example_endpoint(db: Session = Depends(get_db)):
    try:
        # Example database operation
        # result = db.query(...).all()
        return {"message": "Example endpoint response"}
    except Exception as e:
        logger.error(f"Error in example endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Add any other configurations or event handlers if needed
