import asyncio
import time
from time import time, strftime, gmtime
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
import random 
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from pyrogram.enums import ChatAction, ParseMode
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,  
                                     start_pannel)

@app.on_message(filters.command(["Heyy","Lol"],  prefixes=["+", ".", "/", "-", "", "$","#","&"]))
async def hello(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
       x=await.message.reply_sticker(
                "CAACAgUAAxkBAAI33mLYLNLilbRI-sKAAob0P7koTEJNAAIOBAACl42QVKnra4sdzC_uKQQ")
            x.delete()
      lol=await.message.reply_text(
        "hello")
           lol.delete()
            time.sleep(0.4)
            lol.edit_text("💛")
            time.sleep(0.5)
            lol.edit_text("🤍")
            time.sleep(0.3)
            lol.edit_text("❤️")
            time.sleep(0.4)
            lol.delete()
