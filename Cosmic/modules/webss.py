from Cosmic.functions.handler import cosmic

from Cosmic.functions.misc import eor
from .driver import ch, pic


@cosmic(pattern="webss ?(.*)")
async def webss_(e):
    args = e.pattern_match.group(1)
    if not args:
        return await eor(e, "`Give a valid web url`")
    ed = await eor(e, "`Processing...`")
    browser = ch()
    try:
        browser.get(args)
        browser.set_window_size(1500, 1500)
        await pic(browser, e)
        await ed.delete()
    except Exception as ex:
        await eor(e, str(ex))
