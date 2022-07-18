from Cosmic import cosmo
from Cosmic.functions.handler import cosmic

from Cosmic.functions.misc import eor, get_user

@cosmic(pattern="kick ?(.*)")
async def kick(event):
    if event.is_private:
        return await event.edit("Please use this in groups.")
    try:
        user, extra = await get_user(event)
    except TypeError:
        pass
    if not user:
        await eor(event, "Failed to fetch user.")
    if not event.chat.admin_rights.ban_users:
        return await eor(event, "Failed to Kick, No CanBanUsers Right.")
    try:
        await cosmo.kick_participant(event.chat_id, user.id)
        await eor(event, 
            f"Kicked **[{user.first_name}](tg://user?id={user.id})** from [{event.chat.title}](http://t.me/{event.chat.username})!"
        )
    except:
        await eor(event, "Can't kick admins.")


@cosmic(pattern="pin$")
async def pin(event):
    if event.is_private:
        return await eor(event, "Please use this in groups.")
    r = await event.get_reply_message()
    await r.pin()


@cosmic(pattern="kickme")
async def lmao(event):
    await eor(event, f"My Master is leaving from **{event.chat.title}**")
    await event.client.kick_participant(event.chat_id, "me")


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
    except TypeError:
        pass
    if not user:
        await eor(event,  "Failed to fetch user.")
    perms = await cosmo.get_permissions(event.chat_id, "me")
    if not event.chat.admin_rights.ban_users:
        return await eor(event, "Dont have enough ryts")
    try:
        await cosmo.edit_permissions(event.chat_id, user.id, view_messages=False)
        await eor(event, 
            f"Banned **[{user.first_name}](tg://user?id={user.id})** from [{event.chat.title}](http://t.me/{event.chat.username})!"
        )
    except:
        await eor(event, "Can't ban admins.")


@cosmic(pattern="dban ?(.*)")
async def dban(event):
    if event.is_private:
        return await event.edit("Please use this in groups.")
    elif not event.chat.admin_rights.ban_users:
        return await eor(event, "Failed to ban, No CanBanUsers Right.")
    try:
        lol = await event.get_reply_message()
        await cosmo.edit_permissions(event.chat_id, lol.sender.id, view_messages=False)
        await lol.delete()
        await event.delete()
    except:
        await eor(event, "Can't ban admins.")
    
@cosmic(pattern="unban ?(.*)")
async def unban(event):
    if event.is_private:
        return await event.edit("Please use this in groups.")
    try:
        user, extra = await get_user(event)
    except TypeError:
        pass
    if not user:
        await event.edit("Failed to fetch user.")
    elif not event.chat.admin_rights.ban_users:
        return await eor(event, "Failed to Unban, No CanBanUsers Right.")
    try:
        await cosmo.edit_permissions(event.chat_id, user, view_messages=True)
    except:
        await eor(event, "Can't ban admins.")

