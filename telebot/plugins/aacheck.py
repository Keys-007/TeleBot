# Original Plug By @Swonit {Tania Aunty}
# Its Just Edited (shortened) For Specific Use 
#Original Plug Can Be Found In Freaky Ub.By @Swonit


from telethon.errors.rpcerrorlist import YouBlockedUserError

from telebot import CMD_HELP

@telebot.on(admin_cmd(pattern="aa ?(.*)"))
@telebot.on(sudo_cmd(pattern="aa ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking for @TheAnonymousArmy Bans...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
    if sysarg == "":
        await ok.edit(
            "`Give me someones id, or reply to somones message to check his/her stats.`"
        )
        return
    else:
        async with borg.conversation("@MissRose_Bot") as conv:  # AnonymousArmy
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(
                    f"/fbanstat {sysarg} 21029270-28da-425c-9a4a-8f0514624ef0"
                )
                msg = await conv.get_response()
                await ok.edit(
                    msg.text
                    + "\n\nAnonymousArmy bancodes explaination [Here](https://t.me/TheAnonymousArmy/24)"
                )
            # Direct bancodes explaination later
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")
