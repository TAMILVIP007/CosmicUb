from telegraph import Telegraph

from Cosmic.modules import OWNER_ID

telegraph = Telegraph()
r = telegraph.create_account(short_name="Cosmic")
auth_url = r["auth_url"]


def telegraph_(title, text):
    response = telegraph.create_page(title, html_content=text)
    link = "https://telegra.ph/" + response["path"]
    return link


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


async def get_user(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
        return user_id
    elif not event.reply_to_msg_id:
        try:
            args = event.text.split(" ")[1]
        except IndexError:
            return await eor(event, "`Reply to a user or provide username/userid.`")
        if args.startswith("@"):
            user = args[1:]
            try:
                user_object = await event.client.get_entity(user)
                user_id = user_object.id
                return user_id
            except Exception as e:
                return await eor(event, f"`{str(e)}`")
        elif args.isdigit():
            user_id = int(args)
            try:
                user_object = await event.client.get_entity(user_id)
                user = user_object.id
                return user
            except Exception as e:
                return await eor(event, f"`{str(e)}`")


async def eor(e, msg, file=None, parse_mode="md", link_preview=False):
    if e.sender_id == OWNER_ID:
        return await e.edit(
            msg, file=file, parse_mode=parse_mode, link_preview=link_preview
        )
    else:
        return await e.reply(
            msg, file=file, parse_mode=parse_mode, link_preview=link_preview
        )
