# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

from asyncio import wait

from telebot import CMD_HELP
from telebot.telebotConfig import Var
from telebot.utils import admin_cmd


@telebot.on(admin_cmd(pattern=r"bigspam", outgoing=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])

        await wait([e.respond(spam_message) for i in range(1,counter)])

        await e.delete()
        if Var.PRIVATE_GROUP_ID:
            await e.client.send_message(
                Var.PRIVATE_GROUP_ID, "#BIGSPAM \n\n" "BIGSpam was executed successfully"
            )


CMD_HELP.update({"bigspam": ".bigspam <n> <text>\nUse -Spam the word/sentence 'n' times."})
