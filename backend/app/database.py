from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL should be set to your database connection URL
# For SQLite, it's typically like: 'sqlite:///./sql_app.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Only needed for SQLite
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
