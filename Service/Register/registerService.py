import sqlite3
from pydantic import BaseModel
conn = sqlite3.connect('profile.db')

c = conn.cursor()
# Profile Table
c.execute("""CREATE TABLE IF NOT EXISTS profile (
        username text,
        firstname text,
        lastname text,
        email text)""")
# User accounts table generated after first time registration
c.execute("""CREATE TABLE IF NOT EXISTS accounts (
        email text,
        password text,
        status text)""")


# class Profile(BaseModel):
#     username: str
#     firstname: str
#     lastname: None
#     email: str
#     password: str

def createRegistrationDB(registrationData):
    # Sanitize and save registration data as profile (parametize the inputs to DB)
    # check if user exists
    c.execute("SELECT COUNT(email) FROM profile WHERE email=:email", {"email": registrationData['email']})
    profileRecods = c.fetchall()
    print(profileRecods)
    # If record does not exist , create a new profile, otherwise show error account already exists
    if profileRecods == [(0,)]:
        with conn:
            c.execute("INSERT INTO profile VALUES (:username, :firstname, :lastname, :email, :password)",
                    {'username': registrationData['username'], 'firstname': registrationData['firstname'], 'lastname': registrationData['lastname'],'email':registrationData['email'], 'password':registrationData['password']})
            c.execute("INSERT INTO profile VALUES (:email, :password, :status)",
                    {'email':registrationData['email'], 'password':registrationData['password'], "status": "Active"})
            print("new account created")
            return
    else:
        print("Already exists")
        return "Account already exists"

def showAllRegistrations():
    c.execute("SELECT * FROM profile")
    profiles = c.fetchall()
    print(profiles)
    print(profiles[0][0])
    return

def updateRegistrationDB(profileID, registrationData):
    # Sanitize and update registration data as profile (parametize the inputs to DB)
    return {}

def deleteRegistrationDB(profileID, registrationData):
    # Sanitize and update registration data as profile (parametize the inputs to DB)
    return {}


# registrationData = {
#     "username": "JohnDoe",
#     "firstname": "Jane",
#     "lastname": "Doe",
#     "email": "janedoe@example.com",
#     "password": "janedoejanedoestr"}

# createRegistrationDB(registrationData)
# showAllRegistrations()

conn.close()