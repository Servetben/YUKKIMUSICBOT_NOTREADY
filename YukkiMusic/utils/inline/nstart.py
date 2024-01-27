from typing import Union

from pyrogram.types import InlineKeyboardButton
import config 
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app

def nstart_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/shalini_69_NBot?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_7"], callback_data="gib_source"),
        ],
        [
            InlineKeyboardButton("• ʙᴏᴛ ɪɴғᴏ •", callback_data="bot_info_data"),
        ],
    ]
    return buttons
