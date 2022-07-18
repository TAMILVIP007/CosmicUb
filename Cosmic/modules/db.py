from Cosmic.functions.handler import cosmic
from Cosmic.functions.misc import eor

from . import db


@cosmic(pattern="setvar")
async def setDBvar(event):
    try:
        key = event.text.split(" ")[1]
        value = event.text.split(" ", maxsplit=2)[2]
    except IndexError:
        return await eor(event, "Provide the key and a value!")
    db.set_key(key, value)
    await eor(
        event, "__Configured__\n**◆ Key:**`{}`\n**◆ Value:**`{}`".format(key, value)
    )


@cosmic(pattern="getvar")
async def getDBvar(event):
    try:
        key = event.text.split(" ")[1]
    except IndexError:
        return await eor(event, "Provide the key!")
    value = db.get_key(key)
    await eor(event, "**◆ Key:**`{}`\n**◆ Value:**`{}`".format(key, value))


@cosmic(pattern="delvar")
async def delDBvar(event):
    try:
        key = event.text.split(" ")[1]
    except IndexError:
        return await eor(event, "Provide the key!")
    db.del_key(key)
    await eor(event, "Deleted\n**Key:**`{}`".format(key))
