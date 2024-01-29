from telegraph import upload_file
from pyrogram import filters
from YukkiMusic import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "tl" , "telegraph"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ 🔗 {url}')

###Hello


@app.on_message(filters.command(["graph" , "grf"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ 🔗 {url}')
      
