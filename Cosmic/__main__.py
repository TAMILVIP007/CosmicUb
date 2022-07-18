
import glob
import importlib
import logging
import asyncio
import sys
from pathlib import Path
from . import LOGGER, cosmo, start_up

from Cosmic import tbot, cosmo


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
    tbot.run_until_disconnected()
    cosmo.run_until_disconnected()
        



loop = asyncio.get_event_loop()
loop.run_until_complete(start_up())


if __name__ == "__main__":
    main()
