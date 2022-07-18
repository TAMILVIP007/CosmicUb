from telethon.tl.functions.users import GetFullUserRequest

from Cosmic import cosmo
from Cosmic.functions.handler import cosmic

from Cosmic.functions.misc import get_user

@cosmic(pattern="info ?(.*)")
async def new_(event):
    if not event.reply_to_msg_id and not event.pattern_match.group(1):
        user = await cosmo.get_entity(event.sender_id)
    else:
        try:
            user, extra = await get_user(event)
        except TypeError as e:
            print(e)
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    text = "╒═══「<b>User info</b>:\n"
    if first_name:
        text += f"<b>First Name:</b> {first_name}\n"
    if last_name:
        text += f"<b>Last Name:</b> {last_name}\n"
    ups = None
    if username:
        text += f"<b>Username:</b> @{username}\n"
        ups = await event.client(GetFullUserRequest(user.username))
    text += f"<b>ID:</b> <code>{user_id}</code>\n"
    text += f'<b>User link:</b> <a href="tg://user?id={user_id}">{first_name}</a>'
    if ups:
        text += f"\n\n<b>Bio:</b> <code>{ups.about}</code>"
        text += f"\n\n<b>Gbanned: No</b>"
        text += f"\n\n╘══「 <b>Groups count:</b> {ups.common_chats_count} 」"
    await event.edit(text, parse_mode="html")


@cosmic(pattern="id ?(.*)")
async def _t(event):
    if not event.reply_to_msg_id and not event.pattern_match.group(1):
        user = await cosmo.get_entity(event.sender_id)
    else:
        try:
            user, extra = await get_user(event)
        except TypeError as e:
            print(e)
    user_id = user.id
    chat_id = event.chat_id
    event.id
    event_id = event.id
    c_id = str(chat_id).replace("-100", "")
    if event.reply_to_msg_id:
        event_id = event.reply_to_msg_id
    text = f"**[Chat ID]**(http://t.me/{event.chat.username}) : `{chat_id}`\n"
    text += f"**[Message ID]**(http://t.me/c/{c_id}/{event_id}) : `{event_id}`\n"
    text += f"**[User ID]**(tg://user?id={user_id}) : `{user_id}`"
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        if msg.sticker:
            type = "Sticker"
        elif msg.audio:
            type = "Audio"
        elif msg.gif:
            type = "Gif"
        elif msg.video:
            type = "Video"
        elif msg.media:
            type = "Media"
        if msg.media:
            file_id = msg.file.id
            text += f"\n\n**Media Type:** `{type}`\n"
            text += f"**Fid:** `{file_id}`"
    await event.edit(text)
