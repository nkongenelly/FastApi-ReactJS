import sys
sys.path.append("..")
from Service.Register.registerService import * 

def allRegistrations():
    # This shold not be available to the public but to maybe the admins only
    return {}

def registration(profile_id):
    # This shold not be available to the public but to maybe the admins only
    return {}

def createRegistration(profile):
    #Call service for storing this data in database after sanitizing and parametizing
    saveRegistration = createRegistrationDB(registrationData)
    return {}

def updateRegistration(profile):
    #Call service for updating this data in database after sanitizing and parametizing
    updateRegistration = updateRegistrationDB(profileID, registrationData)
    return {}

def deleteRegistration(profile):
    #Call service for deleting this data in database 
    deleteRegistration = deleteRegistrationDB(profileID, registrationData)
    return {}
