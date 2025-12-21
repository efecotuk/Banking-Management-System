import json
import os

def load_users_from_file(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_users_to_file(path, users):
    with open(path, "w") as f:
        json.dump(users, f, indent=4)



