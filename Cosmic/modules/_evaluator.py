import asyncio
import io
import os
import sys
import traceback

from Cosmic.functions.handler import cosmic
from Cosmic.functions.misc import eor
from cosmic.database.varsdb import MongoVars

db = MongoVars


@cosmic(pattern="exec ?(.*)")
async def __exec(e):
    try:
        cmd = e.text.split(maxsplit=1)[1]
    except IndexError:
        return
    msg = await e.reply("`Executing...`")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    cresult = f"<b>Bash:~#</b> <code>{cmd}</code>\n<b>Result:</b> <code>{result}</code>"
    if len(str(cresult)) > 4090:
        with io.BytesIO(result.encode()) as file:
            file.name = "bash.txt"
            await e.reply(f"<code>{cmd}</code>", file=file, parse_mode="html")
            return await msg.delete()
    await msg.edit(cresult, parse_mode="html")


@cosmic(pattern="eval ?(.*)")
async def eval_e(event):
    if len(event.text) > 5 and event.text[5] != " ":
        return
    xx = await eor(event, "`Processing..`")
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await xx.edit("`Give some code`")
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    reply_to_id = event.message.id
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "**EVAL**\n```{}``` \n\n __►__ **OUTPUT**: \n```{}``` \n".format(
        cmd,
        evaluation,
    )
    if len(final_output) > 4096:
        lmao = final_output.replace("`", "").replace("**", "").replace("__", "")
        with io.BytesIO(str.encode(lmao)) as out_file:
            out_file.name = "eval.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=f"```{cmd}```" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )
            await xx.delete()
    else:
        await xx.edit(final_output)


async def aexec(code, event):
    exec(
        (
            (
                ("async def __aexec(e, client): " + "\n message = event = e")
                + "\n r = await event.get_reply_message()"
            )
            + ("\n chat = (await event.get_chat()).id")
            + "\n p = print"
        )
        + "".join(f"\n {l}" for l in code.split("\n"))
    )

    return await locals()["__aexec"](event, event.client)


@cosmic(pattern="restart")
async def _(e):
    await eor("`Restarting..`")
    os.execv(sys.executable, ["python3", "-m", "Cosmic"])


@cosmic(pattern="ls")
async def _ls(e):
    try:
        cmd = e.text.split(maxsplit=1)[1]
    except IndexError:
        cmd = "."
    try:
        Files = os.listdir(cmd)
    except BaseException as b:
        return await eor(e, str(b))
    Dir = "**Directory Manager** \n"
    for D in Files:
        if os.path.isdir(cmd + "/" + D):
            Dir += f"`📁 {D}`\n"
        else:
            if D.endswith(("jpg", "png", "webp")):
                Dir += f"`📸 {D}`\n"
            elif D.endswith(("mp4", "mkv", "webm")):
                Dir += f"`🎞 {D}`\n"
            elif D.endswith(("mp3", "m4a", "mpeg")):
                Dir += f"`📀 {D}`\n"
            elif D.endswith(("txt", "doc", "csv", "json")):
                Dir += f"`📝 {D}`\n"
            elif D.endswith("torrent"):
                Dir += f"`🌀 {D}`\n"
            elif D.endswith(("zip", "rar", "7z")):
                Dir += f"`🗜 {D}`\n"
            elif D.endswith(("pdf")):
                Dir += f"`📚 {D}`\n"
            elif D.endswith(("mp3")):
                Dir += f"`🎵 {D}`\n"
            elif D.endswith(("py")):
                Dir += f"`🐍 {D}`\n"
            elif D.endswith(("exe")):
                Dir += f"`💿 {D}`\n"
            elif D.endswith(("mp4")):
                Dir += f"`📹 {D}`\n"
            else:
                Dir += f"`❔ {D}`\n"
    await eor(e, Dir)
