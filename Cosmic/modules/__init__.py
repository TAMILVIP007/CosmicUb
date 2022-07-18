import time

from config import Vars
from Cosmic import cosmo
from Cosmic.database.varsdb import MongoVars

db = MongoVars()

OWNER_ID = db.get_key("OWNER_ID")
HANDLER = db.get_key("HANDLER") if db.get_key("HANDLER") else "."
BOT_MODE = db.get_key("BOT_MODE") if db.get_key("BOT_MODE") else False
