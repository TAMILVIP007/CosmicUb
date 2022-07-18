from os import getenv
from sys import exit

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
    if not getenv("TOKEN"):
        print("TOKEN not found")
        exit(1)
    TOKEN = getenv("TOKEN")
    APP_KEY = getenv("APP_KEY")
    APP_HASH = getenv("APP_HASH")
