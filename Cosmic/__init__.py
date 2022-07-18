import asyncio
import logging
import time

from pytgcalls import GroupCallFactory
from telethon import TelegramClient
from telethon.sessions import StringSession

from config import Vars

"""Cosmic"""
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
LOGGER = logging.getLogger(__name__)

StartTime = time.time()


cosmo = TelegramClient(StringSession(Vars.SESSION), Vars.APP_KEY, Vars.APP_HASH).start()
tbot = TelegramClient(None, Vars.APP_KEY, Vars.APP_HASH)
VCLIENT = GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON


def run_async(*args, **kwargs):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(*args, **kwargs)
