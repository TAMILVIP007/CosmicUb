from Cosmic.functions.handler import cosmic
from Cosmic.functions.misc import eor


@cosmic(pattern="stat")
async def stat(event):
    await eor(
        event, f"➤ 𝚃𝚘𝚝𝚊𝚕 𝙽𝚘 𝙾𝚏 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝙸𝚗 **{event.chat.title}** **:** `{event.id}`"
    )
