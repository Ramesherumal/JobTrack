from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from database import engine
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Welcome to JobTrack"}



class Job(BaseModel):
    company: str
    position: str
    status: str


@app.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(models.Job).all()


@app.post("/jobs")
def create_job(job: Job, db: Session = Depends(get_db)):

    new_job = models.Job(
        company=job.company,
        position=job.position,
        status=job.status
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job
@app.get("/jobs/status/{status}")
def get_jobs_by_status(status: str, db: Session = Depends(get_db)):
    jobs = db.query(models.Job).filter(models.Job.status == status).all()

    return jobs
@app.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return job
@app.put("/jobs/{job_id}")
def update_job(
    job_id: int,
    updated_job: Job,
    db: Session = Depends(get_db)
):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    job.company = updated_job.company
    job.position = updated_job.position
    job.status = updated_job.status

    db.commit()
    db.refresh(job)

    return job
@app.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(job)
    db.commit()

    return {"message": "Job deleted successfully"}
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()