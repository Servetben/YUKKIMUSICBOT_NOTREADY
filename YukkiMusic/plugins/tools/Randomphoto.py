from pyrogram import Client, filters
import requests
import random
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  

from YukkiMusic import app

regex_photo = ["waifu", "neko"]
pht = random.choice(regex_photo)
url = f"https://api.waifu.pics/sfw/{pht}"


@app.on_message(
    filters.command("ZAnimeph") & filters.private & filters.group)
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        but = [
            [
                InlineKeyboardButton(
                    "summon me ",
                    url=f"https://t.me/meee",
                ),
            ],
            [
                InlineKeyboardButton(
                    "Generate again ✨", 
                    callback_data="again",
                ),
                InlineKeyboardButton(
                    "Owner",
                    url=f"https://t.me/kwajan",
                ),
            ],
        ]
        markup = InlineKeyboardMarkup(but)
        message.reply_photo(up, caption="**animeGenBot**", reply_markup=markup)
    else:
        message.reply("Request failed try /again")
                
@app.on_callback_query(filters.regex("again"))
async def handle_query(client, query):
        response = requests.get(url).json()
        up = response['url']
        if up:
            but = [
                [
                    InlineKeyboardButton(
                        "summon me ",
                        url=f"https://t.me/meee",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Generate again ✨", 
                        callback_data=f'again',
                    ),
                    InlineKeyboardButton(
                        "Owner",
                        url=f"https://t.me/kwajan",
                    ),
                ],
            ]
            markup = InlineKeyboardMarkup(but)
            await query.message.reply_photo(up, caption="**animeGenBot**", reply_markup=markup)
        else:
            await query.message.reply("Request failed try /again")
    
