from time import time

from FastTelethonhelper import fast_download, fast_upload

from Cosmic.functions.handler import cosmic
from Cosmic import cosmo
from Cosmic.functions.misc import eor


@cosmic(pattern="dl ?(.*)")
async def dl(event):
    if not event.is_reply:
        await event.edit("`Reply to a file to download it to local server.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Reply to a file to download it to local server.`")
        return
    try:
        a = time()
        txt = await eor(event, "`Downloading...`")
        args = await fast_download(cosmo, reply_message)
        final = time() - a
        await txt.edit("**Downloaded to** `{} in {}`".format(args, final))
    except BaseException as e:
        await event.edit("`Error Occurred\n{}`".format(str(e)))


@cosmic(pattern="ul")
async def upload(e):
    try:
        cmd = e.text.split(maxsplit=1)[1]
    except IndexError:
        return await eor(e, "Provide the path to file!")
    try:
        a = time()
        await eor(e, "`Uploading...`")
        file = await fast_upload(cosmo, cmd)
        await e.reply(file=file)
        final = time() - a
        await eor(e, "**Uploaded:** `{}` in {}".format(file, final))
    except Exception as c:
        await eor(e, str(c))
