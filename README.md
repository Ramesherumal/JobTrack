# JobTrack

JobTrack is a REST API built with FastAPI for managing and tracking job applications.

## Features

- Create a job application
- View all job applications
- View a specific job by ID
- Update a job application
- Delete a job application
- SQLite database integration
- API error handling with HTTP status codes
- Interactive API documentation using Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Git & GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/jobs` | Create a job |
| GET | `/jobs` | Get all jobs |
| GET | `/jobs/{job_id}` | Get a job by ID |
| PUT | `/jobs/{job_id}` | Update a job |
| DELETE | `/jobs/{job_id}` | Delete a job |

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt