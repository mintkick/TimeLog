# stripped down and generalized version
##############################

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("time-log.json")
firebase_admin.initialize_app(cred)


db = firestore.client()


def inputTime():
    minutes = int(input("Enter time in minutes: "))
    return minutes


collection = db.collection("time_log").get()


# select the database
while True: # loop until user has made a valid input
    # display the names of all the documents in the database
    for documents in collection:   # iterates through all entities in the collection
        print(documents.id)
    choice = input("What do you want to inspect? ") # prompt user for a document in the collection

    document = db.collection("time_log").document(choice).get()   # retrieve and store its DATA
    documentReference = db.collection("time_log").document(choice)   # retrieve and store its REFERENCE

    data = document.to_dict() # make it readable, store in a new variable
    if data is None:    # if it has no data, i.e., if it was an invalid input
        print("No data under that name") # [[[shouldn't actually be the case with Firestore]]]
    else:
        print("..........")
        print("Document: ", document.id)
        print(data)
        # for field in data:
        #     print(field)
        print("..........")
        break

print("\nWhat would you like to do?")
while True:
    # I still need to learn how to refresh the info on this end...
    print(data)
    print("\na: Add time\ne: Edit time\nd: Delete time\nq: Quit")
    action = input("Input code for action: ").lower()
    
    if action == "a": # ADD
        name = input("Give a name to the new field: ") # name for the field *within the document*
        original = True # if that name that already exists, don't overwrite
        for names in db.collection("time_log").document(choice).get().to_dict():
            if name == names:
                print("That name is already being used.")
                original = False
                break
        if original:
            time = inputTime() # user assigns time in minutes
            documentReference.set({name : time}, merge=True) # adds the new data without overwriting the whole doc
    
    elif action == "e": # EDIT
        name = input("Select name of existing field: ")
        # print("Adding time...")
        # time = inputTime() # user assigns time in minutes
        # sum = time + data[name]
        # selectedSprintData.set({name : sum}) # there is also an increment() function in Firestore library...
        print("Replacing value of ", {name}, "...")
        time = inputTime() # user assigns time in minutes
        documentReference.update({name : time})
    
    elif action == "d": # DELETE
        name = input("Delete which field? ")
        documentReference.update({name : firestore.DELETE_FIELD})
        print("Gone.")

    elif action == "q": # QUIT
        print("[Quitting]")
        break

    else: print("Invalid Selection")


# [notes to self]

# advance = False   # flag for valid user input, allowing program to advance
# action = input("Is there anything else? [Y/n] ").lower()
# advance = True if action == "y" else False
# # if action is "y": advance = True
# print(advance)