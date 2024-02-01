from telegraph import upload_file
from pyrogram import filters
from YukkiMusic import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tele"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("Please wait..")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'{url}')
      
