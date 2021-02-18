"""Plugin to Do Promo Of Moi Channel
.moiinfo"""

from telebot.utils import admin_cmd


@telebot.on(admin_cmd(outgoing=True, pattern="moiinfo"))
async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit(
            "Check Out Moi  [Info](https://t.me/About_Keys) Here\nAnd Join It Else Gey !!!"
        )
