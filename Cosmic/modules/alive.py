import datetime
import time

from telethon import version

from Cosmic import StartTime
from Cosmic.functions.handler import cosmic
from Cosmic.functions.misc import eor, get_readable_time

from .. import cosmo


@cosmic(pattern="ping")
async def _(event):
    start_time = datetime.datetime.now()
    message = await eor(event, "`Pinging..`")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b>『 ☛ Pᴏɴɢ :</b> <code>{}</code>\n"
        "<b>     ☛ Uᴘᴛɪᴍᴇ :</b> <code>{}</code>』".format(telegram_ping, uptime),
        parse_mode="html",
    )


@cosmic(pattern="repo$")
async def repo(event):
    await eor(event, "Here is Cosmic **[Rᴇᴘᴏ](http://github.com/tamilvip007/cosmic)**")


@cosmic(pattern="alive$")
async def alive(event):
    try:
        id = (await cosmo.get_entity("me")).id
        name = (await cosmo.get_entity("me")).first_name
        uptime = get_readable_time((time.time() - StartTime))
        x = "**               【  𝙳𝙰𝚂𝙷𝙰 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴 】 **\n\n"
        x += "**Sʏsᴛᴇᴍs ᴀʀᴇ ᴡᴏʀᴋɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ...**\n\n"
        x += "**✘** 🄰🄱🄾🅄🅃 🄼🅈 🅂🅈🅂🅃🄴🄼🅂 **✘**\n\n"
        x += f"**=============================**\n"
        x += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ `{version.__version__}`\n"

        x += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ `{uptime}`\n"
        x += f"**=============================**\n\n"
        x += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ **『 [{name}](tg://user?id={id}) 』** \n\n"
        x += f"© @Tamilvip007\n\n"
        await eor(event, x)
    except Exception as v:
        await event.respond(str(v))
