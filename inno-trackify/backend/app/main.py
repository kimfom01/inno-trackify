from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Dummy data for demonstration
activities_db = [
    {"id": 1, "name": "Coding"},
    {"id": 2, "name": "Reading"},
    {"id": 3, "name": "Exercise"},
    {"id": 4, "name": "My task"}
]

# Pydantic model for Activity
class Activity(BaseModel):
    id: int
    name: str

# Route to fetch all activities
@app.get("/activities/", response_model=List[Activity])
def get_activities():
    return activities_db

# Route to fetch a single activity by ID
@app.get("/activities/{activity_id}", response_model=Activity)
def get_activity(activity_id: int):
    activity = next((act for act in activities_db if act["id"] == activity_id), None)
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

# Route to create a new activity
@app.post("/activities/", response_model=Activity)
def create_activity(activity: Activity):
    activities_db.append(activity.dict())
    return activity

# Route to update an existing activity
@app.put("/activities/{activity_id}", response_model=Activity)
def update_activity(activity_id: int, activity: Activity):
    index = next((i for i, act in enumerate(activities_db) if act["id"] == activity_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    activities_db[index] = activity.dict()
    return activity

# Route to delete an activity
@app.delete("/activities/{activity_id}")
def delete_activity(activity_id: int):
    index = next((i for i, act in enumerate(activities_db) if act["id"] == activity_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    del activities_db[index]
    return {"message": "Activity deleted successfully"}