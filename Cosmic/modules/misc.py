from Cosmic.functions.handler import cosmic
from Cosmic.functions.misc import eor


@cosmic(pattern="stat")
async def stat(event):
    await eor(
        event, f"β€ πππππ π½π πΎπ πΌπππππππ πΈπ **{event.chat.title}** **:** `{event.id}`"
    )
