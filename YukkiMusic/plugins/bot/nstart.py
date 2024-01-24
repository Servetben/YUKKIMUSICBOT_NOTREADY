import asyncio
import random
from pyrogram import *
from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import config
from config import BANNED_USERS
from config.config import OWNER_ID
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

YUMI_PICS = [
    "https://telegra.ph/file/6c885935e50762da25472.jpg",
    "https://telegra.ph/file/bf8ea432e132ec30cb0c2.jpg",
    "https://telegra.ph/file/30250b09029076698e4b2.jpg",
    "https://telegra.ph/file/bce5cfde2ed72fe655e69.jpg",
    "https://telegra.ph/file/92f3de73c8a0c541dd672.jpg",
    "https://telegra.ph/file/7145ff6c8877f27bf64ca.jpg",
    "https://telegra.ph/file/d82e218980ec409672c68.jpg",
    "https://telegra.ph/file/43693df3a30172b954632.jpg",
    "https://telegra.ph/file/30b92f86ea0a712f4d0ed.jpg",
    "https://telegra.ph/file/8cc5b6fe5a047a1ce1cbd.jpg",
    "https://telegra.ph/file/e2c2fb24469b1b19a0866.jpg",
    "https://telegra.ph/file/46b596a04f9db8041a9d1.jpg",
    "https://telegra.ph/file/549ad9de7da164636e201.jpg",
    "https://telegra.ph/file/2eb793749061146a6037c.jpg",
    "https://telegra.ph/file/7ce0ef5e9216273b8bc27.jpg",
    "https://telegra.ph/file/66a8e54145c27468f0c69.jpg",
    "https://telegra.ph/file/da416ecfcc3e50973172e.jpg",
    "https://telegra.ph/file/0708854fe104da9e1445e.jpg",
    "https://telegra.ph/file/48aa2e6b48a32efaf7017.jpg",
    "https://telegra.ph/file/920b88f2d2b0ccb4e648c.jpg",
    "https://telegra.ph/file/fda8146fd6b22f9637733.jpg",
    "https://telegra.ph/file/5417d79b1eea8d122008f.jpg",
    "https://telegra.ph/file/a43806329815ecc6c2aa3.jpg",
    "https://telegra.ph/file/7c4bf50287cc170d167c4.jpg"
]

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start(client, message: Message, _):
    await message.reply_photo(
        random.choice(YUMI_PICS),
        caption=_["start_2"].format(config.MUSIC_BOT_NAME),
        reply_markup=InlineKeyboardMarkup(
          [
          [
                InlineKeyboardButton(
                  "★ Add Me ★", url="https://t.me/I_Love_You_828")
            ]
          [
            InlineKeyboardButton(
                "help", callback_data="settings_back_helper"
            ),
           ]
          [
                InlineKeyboardButton(
                    "chnl", url="{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    "grp", url="{SUPPORT_GROUP}"
                ),
          ]
          [
                InlineKeyboardButton(
                  "owner", user_id=OWNER),
      ]
]
        )
    )
