from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import Config  # Import the Config class

# Create the SQLAlchemy engine using the database URL from the configuration
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": Config.SQLALCHEMY_CHECK_SAME_THREAD}
)

# SessionLocal is an instance of sessionmaker, used to get database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your models
Base = declarative_base()

def get_db():
    """
    Dependency that can be used to get a database session.

    Yields a session that is bound to the SQLAlchemy engine.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
