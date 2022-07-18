import asyncio, os 
from Cosmic.functions.misc import eor
from Cosmic import cosmo
from youtubesearchpython import VideosSearch
import youtube_dl
from FastTelethonhelper import fast_download

async def transcode(filename):
    outname = filename.replace(".mp3", "")
    proc = await asyncio.create_subprocess_shell(
        cmd=(
            "ffmpeg "
            "-y -i "
            f"{filename} "
            "-f s16le "
            "-ac 2 "
            "-ar 48000 "
            "-acodec pcm_s16le "
            f"{outname}.raw"
        ),
        stdin=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await proc.communicate()
    os.remove(filename)
    return f"{outname}.raw"

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "%(id)s.mp3",
    "quiet": True,
}


async def get_file(event):
    if event.reply_to_msg_id:
        reply = await event.get_reply_message()
        if not reply.audio or not reply.voice:
            return await eor(event, "`Reply to a Audio file`")
        name = await fast_download(cosmo, reply.media.file_id)
        return name
'''
    elif len(event.pattern_match.group(1)) > 1:
        try:
            search = VideosSearch(event.pattern_match.group(1), limit=1)
            results = search.results()["result"]
            reply = results[0]
        except IndexError:
            return await eor(event, "`No results found!`")
        except Exception as e:
            return await eor(event, f"`{e}`")
'''