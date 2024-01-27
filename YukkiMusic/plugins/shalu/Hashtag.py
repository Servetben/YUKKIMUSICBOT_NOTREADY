import requests
from YukkiMusic import app 
from pyrogram import filters

@app.on_message(filters.command("hastag"))
async def hastag(bot, message):
    
    try:
        text = message.text.split(' ',1)[1]
        res = requests.get(f"https://mukesh-api.vercel.app/hastag/{text}").json()["results"]

    except IndexError:
        return await message.reply_text("Example:\n\n`/hastag python`")
        
    
    await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ  ʜᴀsᴛᴀɢ :\n<pre>{res}</pre>", quote=True)

