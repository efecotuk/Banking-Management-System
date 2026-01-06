import json
import os

def load_users_from_file(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)
# Reads user data from a JSON file and returns it as a dictionary. 

def save_users_to_file(path, users):
    with open(path, "w") as f:
        json.dump(users, f, indent=4)
# Writes the current users dictionary to a JSON file. 




