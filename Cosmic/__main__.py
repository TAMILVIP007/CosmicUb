from Cosmic.functions.auto import customizeBot, start_up
import glob
import importlib
import logging
import sys
from pathlib import Path
from Cosmic.database import db
from Cosmic import cosmo, tbot

from . import cosmo, run_async


def load_plugins(plugin_name):
    path = Path(f"Cosmic/modules/{plugin_name}.py")
    name = "Cosmic.modules.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Cosmic.modules." + plugin_name] = load
    print("IMPORTED --> " + plugin_name)


path = "Cosmic/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Userbot Started Successfully ")


def main():
    try:
        run_async(customizeBot())
        run_async(start_up())
        tbot.start(bot_token=db.get_key("TOKEN"))
        from Cosmic.functions.handler import cosmic
        tbot.run_until_disconnected()
    except Exception as e:
        print(e)
        raise e

if __name__ == "__main__":
    main()
