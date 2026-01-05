import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(users, username, password):
    if username in users:
        raise ValueError("User already exists")

    users[username] = {
        "username": username,
        "hashed_password": hash_password(password),
        "balance": 0.0,
        "transactions": [],
        "failed_attempts": 0,
        "locked": False
    }
    return users[username]

def login_user(users, username, password):
    if username not in users:
        return None

    user = users[username]

    if user["locked"]:
        return None

    if user["hashed_password"] == hash_password(password):
        user["failed_attempts"] = 0
        return user
    else:
        user["failed_attempts"] += 1
        if user["failed_attempts"] >= 3:
            user["locked"] = True
        return None


