from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import config 
import time
from YukkiMusic import app
from strings import get_string
from config import BANNED_USERS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic.utils.decorators.language import LanguageStart

SHALINI_PICS = [
"https://telegra.ph/file/86ee02ba743844f861333.jpg",
"https://telegra.ph/file/158353fb837ca6ee8a77e.jpg",
"https://telegra.ph/file/9bf45ac99de2417e76bad.jpg",
"https://telegra.ph/file/72268e50261c5b9667f59.jpg",
"https://telegra.ph/file/90a3d8099817f471e66fe.jpg",
"https://telegra.ph/file/d6e53e25328d168eb37b7.jpg",
"https://telegra.ph/file/fda43826dded3e4738a9e.jpg",
"https://telegra.ph/file/77243a965fb002157c3f8.jpg",
"https://telegra.ph/file/9650e40e47e766cd81e35.jpg",
"https://telegra.ph/file/481a75960ca5d23f1db16.jpg",
"https://telegra.ph/file/a9ce7ce4258279cfbff31.jpg",
"https://telegra.ph/file/990bae958f00140b8ee2c.jpg",
"https://telegra.ph/file/02b80a77aaa39d88b2c79.jpg",
"https://telegra.ph/file/2e85d11aefdf6cd01301b.jpg",
"https://telegra.ph/file/0a08b180583f13952336a.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/bb0a28259990c6a978985.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/a0db46dfacd94e489117b.jpg",
"https://telegra.ph/file/cd77be2595cdc2fca60a3.jpg",
"https://telegra.ph/file/632724b3d30c691247c77.jpg",
"https://telegra.ph/file/a2d01afe4f2cb1d4b650c.jpg",
"https://telegra.ph/file/94dc035df11dfb159b999.jpg",
"https://telegra.ph/file/fed9a5b1cbaaefc3a818c.jpg",
"https://telegra.ph/file/66fd03632cbb38bdb4193.jpg"
]


@app.on_message(filters.command(["owner"]) & filters.private & ~BANNED_USERS )
@LanguageStart
async def str(client, message: Message, _):
    await message.reply_photo(
        random.choice(SHALINI_PICS),
      caption=f"""✨ Cʅιƈƙ Bҽʅσɯ Bυƚƚσɳ Tσ Dɱ Mყ Oɯɳҽɾ ✨""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 ƈʟɨƈӄ ɦɛʀɛ 💫", url=f"https://t.me/itz_shalini")
                ]
            ]
        ),
    )

