from Cosmic import cosmo
from Cosmic.functions.handler import cosmic
from Cosmic.functions.misc import eor, get_user
from telethon.tl.types import ChatBannedRequest
from telethon.tl.functions.channels import EditBannedRequest
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

@cosmic(pattern="kick ?(.*)")
async def kick(event):
    if event.is_private:
        return await eor(event, "Please use this in groups.")
    try:
        user, extra = await get_user(event)
        await cosmo(EditBannedRequest(event.chat_id, user, KICK_RIGHTS))
        await event.delete()
    except:
        pass



@cosmic(pattern="pin$")
async def pin(event):
    if event.is_private:
        return 
    r = await event.get_reply_message()
    await r.pin()


@cosmic(pattern="kickme")
async def lmao(event):
    await event.client.delete_dialog(event.chat_id)


@cosmic(pattern="del")
async def bruh(event):
    x = await event.get_reply_message()
    await x.delete()
    await event.delete()


@cosmic(pattern="ban  ?(.*)")
async def ban(event):
    if event.is_private:
        return await eor(event, "Please use this in groups.")
    try:
        user, extra = await get_user(event)
        await cosmo(EditBannedRequest(event.chat_id, user, BANNED_RIGHTS))
        await event.delete()
    except:
        pass

@cosmic(pattern="dban ?(.*)")
async def dban(event):
    if event.is_private:
        return await event.edit("Please use this in groups.")
    try:
        user, _ = await get_user(event)
        await cosmo(EditBannedRequest(event.chat_id, user, BANNED_RIGHTS))
        await event.delete()
        await (await event.get_reply_message()).delete() if event.reply_to_msg_id
    except:
        pass


@cosmic(pattern="unban ?(.*)")
async def unban(event):
    if event.is_private:
        return await eor(event, "Please use this in groups.")
    try:
        user, extra = await get_user(event)
        await cosmo(EditBannedRequest(event.chat_id, user, UNBAN_RIGHTS))
        await event.delete()
    except:
        pass
