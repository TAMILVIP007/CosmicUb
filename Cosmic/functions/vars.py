from . import db

def authorized_():
    auth_ = []
    db.get_key("SUDOS")
    if db.get_key("SUDOS") is not None:
        for i in db.get_key("SUDOS"):
            auth_.append(i)
    auth_.append(db.get_key("OWNER_ID"))
    return auth_
