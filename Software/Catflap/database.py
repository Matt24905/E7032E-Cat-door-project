import urequests as requests
from secrets import APIKEY, URL
        
#If document == null, return false
def findOne(filter_dictionary):
    try:
        headers = {"api-key": APIKEY}
        searchPayload = {
            "dataSource": "Pico",
            "database": "Catflap",
            "collection": "Cats",
            "filter": filter_dictionary,
        }
        response = requests.post(URL + "/action/findOne", headers=headers, json=searchPayload)
        #print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            itemFound = str(response.text)
            if(len(itemFound)) == 17:
                #print("No item found")
                return False
            else:
                #print("Item found: " + response.text)
                return True
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)


def insertOne(filter_dictionary):
    try:
        headers = {"api-key": APIKEY}
        insertPayload = {
            "dataSource": "Pico",
            "database": "Catflap",
            "collection": "Cats",
            "document": filter_dictionary,
        }
        response = requests.post(URL + "/action/insertOne", headers=headers, json=insertPayload)
        print(response)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Document added!")
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)

def entryExit(filter_dictionary):
    try:
        headers = {"api-key": APIKEY}
        insertPayload = {
            "dataSource": "Pico",
            "database": "Catflap",
            "collection": "entries",
            "document": filter_dictionary,
        }
        response = requests.post(URL + "/action/insertOne", headers=headers, json=insertPayload)
        print(response)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Document added!")
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)

def deleteOne(filter_dictionary):
    print("Is deleteOne running?")
    try:
        headers = {"api-key": APIKEY}
        searchPayload = {
            "dataSource": "Pico",
            "database": "Catflap",
            "collection": "Cats",
            "filter": filter_dictionary,
        }
        response = requests.post(URL + "/action/deleteOne", headers=headers, json=searchPayload)
        print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))
        if response.status_code >= 200 and response.status_code < 300:
            print("Document removed")
        else:
            print(response.status_code)
            print("Error")
        response.close()
    except Exception as e:
        print(e)