import os

from pytgcalls import GroupCallFactory

from Cosmic import VCLIENT, cosmo
from Cosmic.functions.handler import cosmic
from Cosmic.functions.misc import eor
from Cosmic.functions.vcfuncs import get_file, transcode


@cosmic(pattern="play")
async def play(event):
    if event.is_private:
        return await eor(event, "Please use this in groups.")
    try:
        file = await get_file(event)
    except TypeError:
        return await eor(event, "`Reply to a Audio file`")
    if not file:
        return await eor(event, "`File not found`")
    msg = await eor(event, "`Transcoding...`")
    file = await transcode(file)
    call = GroupCallFactory(cosmo, VCLIENT).get_group_call()
    await call.join(event.chat_id)
    await call.start_audio(file)
    os.remove(file)
    await msg.edit("`Playing...`")
