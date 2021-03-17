# from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from Controllers.Profile.profileController import *
from Controllers.Register.registerController import *
from starlette.middleware.cors import CORSMiddleware
# from fastapi.middleware.cors import CORSMiddleware
from Service.Register.registerService import *


app = FastAPI()

origins = [
    "http://localhost:3000/register",
    "http://localhost:3000",
    "http://localhost:3000/",
    "http://127.0.0.1:3000/*",
    "http://localhost:3000/*",
    "http://localhost:*",
    "http://127.0.0.1:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"]
)


class Profile(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: str
    password: str


@app.get("/")
def read_root():
    return {
        "data": { "Todo added." }
    }
# Registration routes
@app.get("/apis/registrations")
def read_registrations():
    return showAllRegistrations()

@app.get("/apis/registration/{profile_id}")
def read_registration(profile_id):
    return registration(profile_id)

@app.post("/apis/registrations")
def create_registration(profile:Profile):
    return createRegistrationDB(profile)

@app.put("/apis/registrations/{profile_id}")
def update_registration(profile_id, profile:Profile):
    return updateRegistration(profile_id, profile)   

@app.delete("/apis/registrations/{profile_id}")
def delete_registration(profile_id):
    return deleteRegistration(profile_id)   


