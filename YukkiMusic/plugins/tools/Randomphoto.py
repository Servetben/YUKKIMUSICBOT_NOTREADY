from pyrogram import Client, filters
import requests
import random
from time import time, strftime, gmtime
import config 
from typing import Union
from config import *
from pyrogram import *
import os
from pyrogram.types import (CallbackQuery, InlineKeyboardButton, InputMediaVideo, InputMediaPhoto, 
                            InlineKeyboardMarkup, Message)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  

from YukkiMusic import app

regex_photo = ["waifu", "neko"]
pht = random.choice(regex_photo)
url = f"https://api.waifu.pics/sfw/{pht}"


@app.on_message(
    filters.command("ZAnimeph") & filters.private)
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
async def handle_callback(client: app, update: Union[types.Message, types.CallbackQuery]):
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
        is_callback = isinstance(update, types.CallbackQuery)
        if is_callback:
            try:
                await update.answer()
            except:
                pass
            chat_id = update.message.chat.id
            await CallbackQuery.edit_message_media(
      media=InputMediaPhoto(up),
            reply_markup=InlineKeyboardMarkup(but))
        else:
            await query.message.reply("Request failed try /again")
          
