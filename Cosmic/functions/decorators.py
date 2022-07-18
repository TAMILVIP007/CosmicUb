from functools import wraps

from Cosmic.functions import NO_SPAM
from Cosmic.functions.misc import eor


def nospam(func):
    @wraps(func)
    def wrapper(e):
        if e.chat_id in NO_SPAM:
            return
        return func(e)

    return wrapper


def grp_only(func):
    @wraps(func)
    def wrapper(e):
        if e.is_group:
            return func(e)
        return eor(e, "This command is only available in groups.")

    return wrapper


def msg_link(e):
    if e.chat.username:
        return f"https://t.me/{e.chat.username}/'{e.id}"
    return f"https://t.me/c/{e.chat.id}/{e.id}"
