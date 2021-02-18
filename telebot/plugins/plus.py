from . import TELE_NAME

bruh = """
{}
╭━━━━━━━━━━━━━╮
┃╱╱╱╱╱╱╱╱┏┓╱╱╱┃
┃╱╱╱┏┓╱╱┏╯┃╱╱╱┃
┃╱╱┏┛┗┓╱┗┓┃╱╱╱┃
┃╱╱┗┓┏┛╱╱┃┃╱╱╱┃
┃╱╱╱┗┛╱╱╱┃┃╱╱╱┃
┃╱╱╱╱╱╱╱╱┗┛╱╱╱┃
╰━━━━━━━━━━━━━╯
""".format(TELE_NAME)

@telebot.on(admin_cmd(pattern="plus"))
async def thisisstoopid(event):
	await event.edit(bruh)