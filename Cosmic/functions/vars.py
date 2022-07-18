from config import Vars

def authorized_():
    auth_ = []
    for x in Vars.SUDOS:
        auth_.append(int(x))
    auth_.append(Vars.OWNER_ID)
    return auth_
