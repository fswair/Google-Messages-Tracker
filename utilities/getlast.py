from pysondb.db import getDb
import time

db = getDb("./database/db.json")

def get_last(minutes: int = None):
    data = db.getAll()
    if minutes:
        data = list(filter(lambda x: (time.time() - x["added_date"]) <= (minutes * 60) + 1, data))
    return data[::-1]