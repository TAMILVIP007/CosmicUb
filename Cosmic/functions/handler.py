import logging
import sys
from time import gmtime, strftime
from traceback import format_exc

from telethon import Button, events

from config import Vars
from Cosmic import cosmo, tbot
from Cosmic.functions.decorators import msg_link
from Cosmic.functions.misc import eor, telegraph_
from Cosmic.functions.vars import authorized_


def cosmic(**args):
    args["pattern"] = "^[" + Vars.HANDLER + "](?i)" + args["pattern"]
    args["from_users"] = authorized_()

    def decorator(func):
        async def wrapper(ev):
            try:
                await func(ev)
            except BaseException as exception:
                logging.info(exception)
                await log_error(ev)

        cosmo.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator


async def log_error(event):
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    text = "**Sorry, I encountered an error!**\n"
    link = "[https://t.me/cosmicsupport](Userbot Support Chat)"
    text += "If you want to report it, "
    text += f"just forward this message to {link}.\n"
    ftext = "--------BEGIN USERBOT TRACEBACK LOG--------"
    ftext += "<br>Date: " + date
    if event:
        ftext += "\nGroup ID: " + str(event.chat_id)
        ftext += "\nSender ID: " + str(event.sender_id)
        ftext += "\n\nEvent Trigger:\n"
        ftext += str(event.text)
    ftext += "\n\nTraceback info:\n"
    ftext += str(format_exc())
    ftext += "\n\nError text:\n"
    ftext += str(sys.exc_info()[1])
    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"
    ftext = telegraph_("Cosmic - Error Report", ftext)
    text += f"Logs here: [logs]({ftext}) | [support]({link})"
    if Vars.LOGGER:
        buttons = Button.url("Userbot Support Chat", "https://t.me/cosmicsupport")
        msg = await tbot.send_message(Vars.LOGGER, text, buttons=buttons)
        try:
            await eor(
                event,
                f"**Sorry, I encountered an error!**\n\n Check logs [here]({msg_link(msg)})",
            )
        except BaseException:
            return await eor(event, "`LOGGER ID INVALID`")
