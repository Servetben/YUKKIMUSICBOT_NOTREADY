#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
from unidecode import unidecode 
import os
import re
import textwrap
import numpy as np
import aiofiles
from unidecode import unidecode
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch

from config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

def circle(img): 
     h,w=img.size 
     a = Image.new('L', [h,w], 0) 
     b = ImageDraw.Draw(a) 
     b.pieslice([(0, 0), (h,w)], 0, 360, fill = 255,outline = "white") 
     c = np.array(img) 
     d = np.array(a) 
     e = np.dstack((c, d)) 
     return Image.fromarray(e)


def clear(text):
    list = text.split(" ")
    title = ""
    for i in list:
        if len(title) + len(i) < 60:
            title += " " + i
    return title.strip()

async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"cache/thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(900, 900, youtube)
        image2 = image1.convert("RGBA")
        background = Image.open(f"Love/Stream2.jpg")
        enhancer = ImageEnhance.Brightness(youtube)
        youtube = enhancer.enhance(1.4)
        y=changeImageSize(1050,1050,circle(youtube)) 
        background.paste(y,(410,520),mask=y)
        draw = ImageDraw.Draw(background)
        arial = ImageFont.truetype("Love/font2.ttf", 30)
        font = ImageFont.truetype("Love/font.ttf", 120)
        draw.text((1820, 740), f"Title: {title[:50]} .", (255, 255, 255), font=font)
        draw.text((1820, 890), f"Views: {views}", (255, 255, 255), font=font)
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL

async def get_qthumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"cache/thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()
     
        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1050, 1050, youtube)
        image2 = image1.convert("RGBA")
        background = Image.open(f"Love/Newpic.jpg")
        enhancer = ImageEnhance.Brightness(youtube)
        youtube = enhancer.enhance(1.4)
        y=changeImageSize(879, 879,circle(youtube)) 
        background.paste(y,(538,625),mask=y)
        draw = ImageDraw.Draw(background)
        arial = ImageFont.truetype("Love/font2.ttf", 30)
        font = ImageFont.truetype("Love/font.ttf", 120)
        draw.text((1820, 640), f"Title: {title[:50]} .", (255, 255, 255), font=font)
        draw.text((1820, 840), f"Duration: {duration}", (255, 255, 255), font=font)
        draw.text((1820, 1040), f"Views: {views}", (255, 255, 255), font=font)
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
