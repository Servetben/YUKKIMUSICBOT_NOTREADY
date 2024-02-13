import inspect
import re
from pathlib import Path

from pymongo import MongoClient
from telethon import events

from YukkiMusic import telethn

MONGO_DB_URI = "mongodb+srv://rahul:rahulkr@cluster0.szdpcp6.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["THEPOLICE"]
gbanned = db.gban


def register(**args):
    """Registers a new message."""
    pattern = args.get("pattern", None)

    r_pattern = r"^[/!.]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        telethn.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator
  
