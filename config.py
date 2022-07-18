from os import getenv
from sys import exit
from Cosmic.database import db

from dotenv import load_dotenv

load_dotenv()


class Vars:
    if not getenv("SESSION"):
        print("SESSION not found")
        exit(1)
    SESSION = getenv("SESSION")
    if not getenv("MONGO_URL"):
        print("DB_URL not found")
        exit(1)
    MONGO_URL = getenv("MONGO_URL")
    TOKEN = getenv("TOKEN")
    APP_KEY = getenv("APP_KEY")
    HANDLER = db.get_key("HANDLER") or "."
    BOT_MODE = db.get_key("BOT_MODE") or False
    APP_HASH = getenv("APP_HASH")
