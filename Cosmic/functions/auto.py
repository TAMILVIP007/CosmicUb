import asyncio, re
import sys
from secrets import token_hex

from telethon import Button, version

from config import Vars
from Cosmic import LOGGER, cosmo, tbot
from Cosmic.database.varsdb import MongoVars

def strip_token(text):
    a = re.findall(r"\d+:.+", text)
    token = a[0].strip()
    return token


db = MongoVars()
async def start_up():
    owner_id = (await cosmo.get_me()).id
    db.set_key("OWNER_ID", owner_id)
    bot_id = (await tbot.get_me()).id
    db.set_key("BOT_ID", bot_id)
    db.set_key("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    LOGGER.info("Bot Vars Configured Successfully")
    msg = f"""
    **SYSTEMS ARE NOW ONLINE**

    __Telethon version:__ `{version.__version__}`
    __Python version:__ `{sys.version}`  
    """
    buttons = Button.url("SUPPORT CHAT", "t.me/cosmicsupport")
    try:
        await tbot.send_message(Vars.LOGGER, msg, buttons=buttons)
    except Exception:
        print("check ur logger ID in vars")


async def customizeBot():
    chat = "@botfather"
    if db.get_key("TOKEN"):
        return
    name = (await cosmo.get_me()).first_name + "'s bot"
    uname = (await cosmo.get_me()).username + "_bot"
    msg1 = await cosmo.send_message(chat, "/cancel")
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "/newbot")
    await asyncio.sleep(1)
    msg2 = await cosmo.get_messages(chat, limit=1)
    if not "choose a name" in msg2.text:
        return LOGGER.critical("Cant create bot.. Exiting")
    await cosmo.send_message(chat, name)
    await asyncio.sleep(1)
    await cosmo.send_message(chat, uname)
    msg3 = await cosmo.get_messages(chat, limit=1)
    if "Sorry," in msg3.text:
        uname = (await cosmo.get_me()).username + token_hex(2) + "_bot"
        await cosmo.send_message(chat, uname)
    msg4 = await cosmo.get_messages(chat, limit=1)
    db.set_key("TOKEN", strip_token(msg4.text))
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "/setdescription")
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "@" + uname)
    await asyncio.sleep(1)
    DESCRIPTION = f"Hi. I am {(await cosmo.get_me()).first_name}'s bot.\n\n"
    DESCRIPTION += "SUPPORT CHAT: @cosmicsupport\n"
    DESCRIPTION += "UPDATES: @cosmicubupdates\n"
    DESCRIPTION += "GITHUB: http://github.com/tamilvip007/Cosmic\n"
    await cosmo.send_message(chat, DESCRIPTION)
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "/setabouttext")
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "@" + uname)
    await asyncio.sleep(1)
    await cosmo.send_message(chat, DESCRIPTION)
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "/setinline")
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "@" + uname)
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "Cosmic Userbot")
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "/setuserpic")
    await asyncio.sleep(1)
    await cosmo.send_message(chat, "@" + uname)
    await cosmo.send_file(chat, "assets/log_image.jpg")
    await asyncio.sleep(1)
    last = await cosmo.send_message(chat, "/done")
    for x in range(msg1.id, last.id):
        await cosmo.delete_messages(chat, x)

