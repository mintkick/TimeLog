## Overview

**Project Title**:
Project Time Log Tool

**Project Description**:
This software allows you to store and track time using a cloud database, including the ability to create, read, update, and delete time submissions. It uses Python and Firestone (Google Firebase) for cloud databasing.

**Project Goals**:

- utilize a cloud database with at least one table (or "collection" in Firestore)
- query data from the database
- add new data to the database
- update data from the database
- delete data from the database

## Instructions for Build and Use

Steps to build and/or run the software:

1. Run the Python file in the terminal with `python cloud_link.py`

Instructions for using the software:

1. Input a document name from the collection. (Documents will be queried automatically.)
2. Input an action code to add, edit, or delete a field.
3. Specify the field to perform the desired action on.
   - If relevant, input an integer value to assign to that field.
4. When finished, input `q` to quit.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

- VSCode
- Python 3.12.6
- Google Firestore -- I used this code block to implement the library of Firestore functions:

  ```
  import firebase_admin
  from firebase_admin import credentials, firestore

  cred = credentials.Certificate("YOUR_PRIVATE_KEY.json")
  firebase_admin.initialize_app(cred)
  ```

## Useful Websites to Learn More

I found these websites useful in developing this software:

- [Firestore Docs - Manage Data](https://firebase.google.com/docs/firestore/manage-data/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

- [ ] Refresh the database info for the user during runtime
- [ ] Access collections other than the hard-coded one
- [ ] Add more error-handling
- [ ] Make more readable

## Ideas for Future Projects

What I want to make based off of this project:

- [ ] Event Planner
