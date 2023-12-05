import random

from database import *
from helpers import motor1, motor2, getTime
from motor import turnOn


#DO NOT NAME RETURNS FROM GETTIME TIME DUM DUM
data = []

#Fake data from the buttons, add cat to database. This function is only called when
# the buttons are pressed, i.e the owner wishes to add a cat to the database. To ensure
#correct functionality, the function should only run when the IR sensors reads a cat. 
def addCat():
    print("Adding chipnumber to the database")
    #if IR_sensor_reading == True:
    chipNumber = generateChipnumber()
    data.append(chipNumber)
        #chipNumber = generateChipnumber()
    insertOne({"Chipnumber": chipNumber})
    print("Cat successfully added")

#Fake data from the buttons, remove cat from the database. This function is only called
#when the button is pressed, i.e the owner wishes to remove a cat from the database. A
#function to remove cats from the app should also be implemented. 
def removeCat():
    chipNumber = data[0]
    temp = findOne({"Chipnumber": chipNumber})
    if temp == True:
        deleteOne({"Chipnumber": chipNumber})
        data.remove(chipNumber)
    else:
        print("No cat with that chip number in the database")

# Fake data from the antenna to generate random chip numbers :) This will not
#be used in the actual cat flap. 
def generateChipnumber():
    temp = []
    for i in range (15):
        k = random.randint(0,9)
        temp.append(k)
    chipNumber = ''.join(str(e) for e in temp)
    return chipNumber

#test = "0844901"
#Is the cat in the database? If it is, engage motor and add entry to the database. 
def checkIfCat():
    #addCat has to be run here, because if not upon restart, data will be empty. Will be removed later!
    #addCat()
    chipNumber = data[0]
    #if IR_sensor_reading == True:
    temp = findOne({"Chipnumber": chipNumber})
    if temp == True:
        timestamp, date = getTime()
        turnOn(motor1, motor2)
        entryExit({"Chipnumber": chipNumber, "Time": timestamp, "Date": date})
        return True
    else:
        print("Cat does not exist in database")
        return False
    #else:
     #   print("No cat located")