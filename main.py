# from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from Controllers.Profile.profileController import *
from Controllers.Register.registerController import *

app = FastAPI()

class Profile(BaseModel):
    username: str
    firstname: str
    lastname: None
    email: str
    password: str


@app.get("/")
def read_root():
    return show()

# Registration routes
@app.get("/apis/registrations")
def read_registrations():
    return allRegistrations()

@app.get("/apis/registration/{profile_id}")
def read_registration():
    return registration(profile_id)

@app.post("/apis/registrations")
def create_registration(profile:Profile):
    return createRegistration(profile)

@app.put("/apis/registrations/{profile_id}")
def update_registration(profile_id, profile:Profile):
    return updateRegistration(profile_id, profile)   

@app.delete("/apis/registrations/{profile_id}")
def delete_registration(profile_id, profile:Profile):
    return deleteRegistration(profile_id, profile)   


