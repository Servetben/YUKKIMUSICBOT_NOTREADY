import requests
from YukkiMusic import app
from config import BOT_USERNAME
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["chatgpt","ai","ask","gpt"],  prefixes=["+", ".", "/", "-", "", "$","#","&"]))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        
        if len(message.command) < 2:
            await message.reply_text(
                "Example:\n\n`/chatgpt Where is TajMahal?`"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://mukesh-api.vercel.app/chatgpt/{a}')

            try:
                # Check if the response contains valid JSON
                json_response = response.json()

                # Check if "results" key is present in the JSON response
                if "results" in json_response:
                    x = json_response["results"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
                    await message.reply_text(
                        f" {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n 💓 ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME}",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except ValueError as ve:
                # Handle the case when the response is not valid JSON
                await message.reply_text(f"Invalid JSON format in the response: {ve}")
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
                    
