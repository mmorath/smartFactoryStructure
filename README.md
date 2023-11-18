# FastAPI Application for Fertigungsmaschinen Management

## Overview
This FastAPI application provides a backend service for managing Fertigungsmaschinen (manufacturing machines). It offers a RESTful API for accessing and manipulating data related to various manufacturing machines, their network connections, and participants.

## Features
- Retrieve a list of all Fertigungsmaschinen with detailed information.
- Get the total count of Fertigungsmaschinen.
- Additional management features for Fertigungsmaschinen (TBD).

## Folder Structure
```
.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   ├── data
│   │   │   └── fertigungsmaschinen.json
│   │   ├── dependencies.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── routes
│   │       ├── __init__.py
│   │       ├── fertigungsmaschinen.py
│   │       └── teilnehmer.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       └── test_main.py
├── cleanUp.sh
└── docker-compose.yml
```

- `Dockerfile`: Defines the Docker container setup for the application.
- `app/`: Main application directory.
  - `data/`: Contains JSON data files like `fertigungsmaschinen.json`.
  - `main.py`: Entry point of the FastAPI application.
  - `models.py`: Pydantic models for the application.
  - `routes/`: API routes of the application.
- `requirements.txt`: Lists the Python dependencies of the application.
- `tests/`: Contains test scripts for the application.
- `cleanUp.sh`: Shell script for Docker housekeeping.
- `docker-compose.yml`: Docker Compose configuration file.

## Requirements
- Docker
- Python 3.9+
- FastAPI
- Uvicorn

## Setup and Running the Application

1. Clone the repository:
   ```
   git clone [repository-url]
   ```

2. Navigate to the `backend` directory:
   ```
   cd backend
   ```

3. Build the Docker image:
   ```
   docker build -t fastapi-app .
   ```

4. Run the Docker container:
   ```
   docker run -p 8000:8000 fastapi-app
   ```

5. The application will be available at `http://localhost:8000`.

## API Documentation
After running the application, you can access the auto-generated API documentation by visiting:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These pages provide an interactive way to explore the API's endpoints and their responses.

## Testing
To run tests, navigate to the `backend` directory and execute:

```
pytest
```

## Contributing
(Provide instructions for contributing to this project, if applicable.)
