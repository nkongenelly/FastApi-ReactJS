import sqlite3
from pydantic import BaseModel
conn = sqlite3.connect('application.db')

c = conn.cursor()
# Profile Table
c.execute("""CREATE TABLE IF NOT EXISTS profile (
        profileId integer,
        username text,
        firstname text,
        lastname text,
        email text)""")
# User accounts table generated after first time registration
c.execute("""CREATE TABLE IF NOT EXISTS accounts (
        email text,
        password text,
        status text,
        profile_id integer)""")


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

    # Get length of all records and add one to get the auto increament profileid
    profileLength = c.execute("SELECT COUNT(email) FROM profile").fetchone()
    print(profileLength)
    print(profileLength[0])
    # print(Object.freeze(profileLength))
    profileId = profileLength[0] + 1
    # If record does not exist , create a new profile, otherwise show error account already exists
    if profileRecods == [(0,)]:
        with conn:
            c.execute("INSERT INTO profile VALUES (:profileId, :username, :firstname, :lastname, :email)",
                    {'profileId': profileId, 'username': registrationData['username'], 'firstname': registrationData['firstname'], 'lastname': registrationData['lastname'],'email':registrationData['email']})
            c.execute("INSERT INTO accounts VALUES (:email, :password, :status, :profile_id)",
                    {'email':registrationData['email'], 'password':registrationData['password'], "status": "Active", 'profile_id': profileId})
            print("new account created")
            return
    else:
        print("Already exists")
        return "Account already exists"

def showAllRegistrations():
    c.execute("SELECT * FROM profile")
    profiles = c.fetchall()
    print(profiles)
    # print(profiles[0])
    return

def updateRegistrationDB(profileID, registrationData):
    # Sanitize and update registration data as profile (parametize the inputs to DB)
    with conn:
        c.execute("UPDATE profile SET username=:username, firstname=:firstname, lastname=:lastname, email=:email WHERE profileId=:profileId",
        {'username':registrationData['username'], 'firstname': registrationData['firstname'], 'lastname': registrationData['lastname'], 'email':registrationData['email'], "profileId": profileID})
    return

def deleteRegistrationDB(profileID):
    # Sanitize and update registration data as profile (parametize the inputs to DB)
    with conn:
        c.execute("DELETE FROM profile WHERE profileId=:profileId",{'profileId':profileID})
        c.execute("UPDATE accounts SET status=:status WHERE profile_id=:profileId",{'status':'inactive','profileId':profileID})
    return

#
# registrationData = {
#     "username": "JohnDoe1",
#     "firstname": "Jane",
#     "lastname": "Doe",
#     "email": "janedoe@example.com",
#     "password": "janedoejanedoestr"}
# registrationData1 = {
#     "username": "Jane",
#     "firstname": "Jane",
#     "lastname": "Jane",
#     "email": "janedoe@example.com",
#     "password": "janedoejanedoestr"}
#
# createRegistrationDB(registrationData)
# showAllRegistrations()
# updateRegistrationDB("1", registrationData1)
# deleteRegistrationDB("1")

conn.close()