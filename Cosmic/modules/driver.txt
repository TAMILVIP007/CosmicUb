import base64
import io
import math
import random
import string

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import Vars

safety_check = []


def ch():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.binary_location = Vars.CHROME_BIN
    b = webdriver.Chrome(options=chrome_options)
    b.delete_all_cookies()
    return b


def fb(b):
    s = b.page_source
    s = BeautifulSoup(s, "html.parser")
    b = s.findAll("button")
    for x in b:
        print(xpath(x))


def xpath(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:  # type: bs4.element.Tag
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if 1 == len(siblings)
            else "%s[%d]"
            % (child.name, next(i for i, s in enumerate(siblings, 1) if s is child))
        )
        child = parent
    components.reverse()
    return "/%s" % "/".join(components)


def progress_bar(percentage: int) -> str:
    progress_str = "[{0}{1}] {2}%\n".format(
        "".join(["▰" for i in range(math.floor(percentage / 10))]),
        "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
        round(percentage, 2),
    )
    return "\n" + progress_str


def gen_email():
    CHAR = string.ascii_letters
    return "".join(random.choice(CHAR) for a in range(10)) + "@gmail.com"


async def pic(browser, e, txt=None):
    with io.BytesIO(base64.b64decode(browser.get_screenshot_as_base64())) as f:
        f.name = "screenshot.png"
        await e.respond(txt, file=f)
