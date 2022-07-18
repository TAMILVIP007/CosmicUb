from ..functions.handler import cosmic
from . import db
from ..functions.misc import eor, get_user


@cosmic(pattern="addsudo")
async def add_sudo(event):
    user = await get_user(event)
    if user is None:
        return await eor(event, "`User not found!`")
    SUDOS = db.get_key("SUDOS")
    if not SUDOS:
        SUDOS = []
    elif user.id in SUDOS:
        return await eor(event, "`User is already a sudo user!`")
    SUDOS.append(user.id)
    db.set_key("SUDOS", SUDOS)
    return await eor(event, "`User has been added to sudo list!`")

@cosmic(pattern="rmsudo")
async def rm_sudo(event):
    user = await get_user(event)
    SUDOS = db.get_key("SUDOS")
    if not SUDOS:
        return await eor(event, "`Sudo list is empty!`")
    elif user.id not in SUDOS:
        return await eor(event, "`User is not a sudo user!`")
    SUDOS.remove(user.id)
    db.set_key("SUDOS", SUDOS)
    return await eor(event, "`User has been removed from sudo list!`")

@cosmic(pattern="listsudo")
async def list_sudo(event):
    SUDOS = db.get_key("SUDOS")
    if not SUDOS:
        return await eor(event, "`Sudo list is empty!`")
    else:
        return await eor(event, "`Sudo list:`\n" + ", ".join(str(x) for x in SUDOS))