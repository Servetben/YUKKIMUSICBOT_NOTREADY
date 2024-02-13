import glob
import io
import os
import random

import requests
from PIL import Image, ImageDraw, ImageFont

from MukeshRobot import BOT_USERNAME, OWNER_ID,BOT_NAME, , telethn
from MukeshRobot.events import register
button_row = [
        InlineKeyboardButton('Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ', f'https://t.me/Botusernamebot?startgroup=new')
]

