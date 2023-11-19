class Config:
    # Database configuration
    DATABASE_URL = "sqlite:///./sql_app.db"  # Example URL for SQLite

    # FastAPI settings
    FASTAPI_TITLE = "smart factory bridge"
    FASTAPI_VERSION = "1.0.0"
    FASTAPI_DESCRIPTION = "Your API Description"
    FASTAPI_DEBUG = False  # Set to True for development, False for production
    FASTAPI_SECRET_KEY = "your-secret-key"  # Replace with a secure secret key

    # CORS settings
    ALLOWED_ORIGINS = ["*"]  # Allow all origins; configure as needed
    ALLOWED_METHODS = ["*"]  # Allow all methods; configure as needed

    # Logging settings
    LOG_LEVEL = "INFO"  # Adjust the log level as needed
