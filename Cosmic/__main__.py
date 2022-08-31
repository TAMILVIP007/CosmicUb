import importlib

from config import Vars
from Cosmic import LOGGER, tbot


def import_modules(logger):
    """Imports all modules in the modules folder."""
    path = "Vexa/modules/"
    for filename in os.listdir(path):
        if filename.endswith(".py"):
            importlib.import_module("Vexa.modules." + filename[:-3])
            logger.info("Imported module: " + filename)

import_modules(LOGGER)

print("Userbot Started Successfully ")


def main():
    try:
        # run_async(start_up())
        tbot.start(bot_token=Vars.TOKEN)
        tbot.run_until_disconnected()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
