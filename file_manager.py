import json
import os
from datetime import datetime
from typing import Tuple, List


BASE_DATA_DIR = "data"
USERS_FILE = os.path.join(BASE_DATA_DIR, "users.json")
TXNS_FILE = os.path.join(BASE_DATA_DIR, "transactions.json")
BACKUP_DIR = "backups"




def initialize_storage(base_dir: str = BASE_DATA_DIR) -> dict:
os.makedirs(base_dir, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)


if not os.path.exists(USERS_FILE):
with open(USERS_FILE, "w") as f:
json.dump({}, f)


if not os.path.exists(TXNS_FILE):
with open(TXNS_FILE, "w") as f:
json.dump([], f)


return {"users_path": USERS_FILE, "transactions_path": TXNS_FILE}




def load_data(users_path: str = USERS_FILE, transactions_path: str = TXNS_FILE) -> Tuple[dict, list]:
try:
with open(users_path, "r") as f:
users = json.load(f)
except Exception:
users = {}


try:
with open(transactions_path, "r") as f:
transactions = json.load(f)
except Exception:
transactions = []


return users, transactions




def save_data(users_path: str, transactions_path: str, users: dict, transactions: list) -> None:
with open(users_path, "w") as f:
json.dump(users, f, indent=2, default=str)


with open(transactions_path, "w") as f:
json.dump(transactions, f, indent=2, default=str)


backup_data([users_path, transactions_path], BACKUP_DIR)




def backup_data(source_paths: List[str], backup_dir: str) -> List[str]:
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
os.makedirs(backup_dir, exist_ok=True)
created = []


for p in source_paths:
if not os.path.exists(p):
continue
base = os.path.basename(p)
return True

