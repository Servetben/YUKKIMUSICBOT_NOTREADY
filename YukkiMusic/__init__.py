#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from YukkiMusic.core.bot import YukkiBot
from YukkiMusic.core.dir import dirr
from YukkiMusic.core.git import git
from YukkiMusic.core.userbot import Userbot
from YukkiMusic.misc import dbb, heroku, sudo
import telegram.ext as tg
from aiohttp import ClientSession
from pyrogram import Client
from telethon import TelegramClient
from .logging import LOGGER
from config import *

telethn = TelegramClient("YukkiBoot", API_ID, API_HASH)
# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
