import requests
from YukkiMusic import app
from config import BOT_USERNAME
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["Arti"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Example:\n\n`/chatgpt Where is TajMahal?`"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                # Try to access "results" key in the JSON response
                x = response.json()["results"]
                end_time = time.time()
                telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                await message.reply_text(
                    f" {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n 💓 ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME}",
                    parse_mode=ParseMode.MARKDOWN
                )
            except KeyError:
                # Print the actual JSON response to understand its structure
                print(response.json())
                await message.reply_text("No 'results' key found in the response.")
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
                
