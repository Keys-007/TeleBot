"""Plugin to Do Promo Of Moi Channel
.logo"""

from telebot.utils import admin_cmd


@telebot.on(admin_cmd(outgoing=True, pattern="logo"))
async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit(
            "Check Out Moi Lomgo [Channel](https://t.me/ByKeys)\nAnd Join It Else Gey !!!"
        )
