import asyncio

from telebot import CMD_HELP
from telebot.utils import admin_cmd


@telebot.on(admin_cmd(pattern="by ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Bye 🙂🙂")
        await asyncio.sleep(2)
        await event.edit("Goodbye 😕😕 ")
        await asyncio.sleep(2)
        await event.edit("See You Soon 🙁🙁")
        await asyncio.sleep(2)
        await event.edit("I Know No One Would Miss Me 😔😔")
        await asyncio.sleep(2)
        await event.edit("I Know No One Would Remember Me 🤧🤧")
        await asyncio.sleep(2)
        await event.edit("Until They Have A Work 🌝🌝")
        await asyncio.sleep(2)
        await event.edit("But A Good Bye To You 😃😃")
        await asyncio.sleep(2)
        await event.edit("Goodbye Until I Come Back 🙃🙃")


CMD_HELP.update({"by": ".by\nUse - None Try It Yourself."})
