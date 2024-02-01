from time import time, strftime, gmtime
from YukkiMusic import app
import asyncio

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
import random 
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube
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

@app.on_message(
    filters.command([start])
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    start = time()
    x = await c.send_message(q.message.chat.id, "Fᴇᴛᴄʜɪɴɢ Iɴғᴏʀᴍᴀᴛɪᴏɴ....")
    delta_ping = time() - start
    await x.delete()
    txt = f"""
HELLO
    """
    await q.answer(txt, show_alert=True)
    return
