import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch
from YukkiMusic import app

from config import YOUTUBE_IMG_URL,MUSIC_BOT_NAME



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

def circle2(img,Xcenter,Ycenter):
    h,w=img.size
    a = Image.new('L', [h,w], 0)
    b = ImageDraw.Draw(a)
    b.pieslice([(0, 0), (h,w)], 0, 360, fill = 255,outline = "white")
    b.pieslice([(int(Xcenter-50), int(Ycenter-30)), (int(Xcenter+50),int(Ycenter+30))], 0, 360, fill = 0,outline = "black")
    c = np.array(img)
    d = np.array(a)
    e = np.dstack((c, d))
    return Image.fromarray(e)

def squ(img1):
    a = Image.new('L', [640,500], 0)
    b=ImageDraw.Draw(a)
    b.line((320,0,240,550),fill="white",width=670)
    e=Image.fromarray(np.dstack((np.array(img1),np.array(a))))
    return e

async def gen_thumb(videoid,user_id):
    if os.path.isfile(f"cache/{videoid}_{user_id}.png"):
       return f"cache/{videoid}_{user_id}.png"

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
        p=0            
        try: 
            async for photo in app.get_chat_photos(user_id,1): 
                sp=await app.download_media(photo.file_id, file_name=f'{user_id}.jpg')
                p=1
            if p==0:
                raise Exception
        except: 
            async for photo in app.get_chat_photos(app.id,1): 
                sp=await app.download_media(photo.file_id, file_name=f'{app.id}.jpg')
        xp=Image.open(sp)
        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(70))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.5)
        Xcen1 = image1.width / 2
        Ycen1 = image1.height / 2
        Xcen2 =xp.width / 2
        Ycen2 = xp.height / 2
        
        #y=changeImageSize(400,400,circle2(youtube,Xcen1,Ycen1))
        y=changeImageSize(400,400,circle(youtube))
        background.paste(y,(690,40),mask=y)
        b=ImageDraw.Draw(background)
        b.pieslice([(690, 40), (1090,440)], 0, 360,outline = "white",width=10)
        x= changeImageSize(270,270,circle(xp))
        background.paste(x, (960,240), mask=x)
        b=ImageDraw.Draw(background)
        b.pieslice([(960,240), (1230,510)], 0, 360,outline ='black',width=10)
    
        draw=ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/TiltWarp-Regular.ttf",35)
        font2 = ImageFont.truetype("assets/FasterOne-Regular.ttf",75)
        arial = ImageFont.truetype("assets/font2.ttf", 30)
        name_font = ImageFont.truetype("assets/font6.ttf", 30)
        font3=ImageFont.truetype("assets/font3.ttf",30)
        font4=ImageFont.truetype("assets/font4.ttf",30)
        font5=ImageFont.truetype("assets/Gugi-Regular.ttf",40)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
                    (30,10),
                    f"{MUSIC_BOT_NAME}",
                    fill="white",
                    stroke_width=5,
                    stroke_fill="black",
                    font=font5,
        )
        draw.text(
                    (100, 100),
                    "NOW PLAYING",
                    fill="white",
                    stroke_width=8,
                    stroke_fill="black",
                    font=font2,
                )
        for line in para:
                    if j == 1:
                        j += 1
                        draw.text(
                            (120, 280),
                            f"{line}",
                            fill="white",
                            stroke_width=5,
                            stroke_fill="black",
                            font=font,
                        )
                    if j == 0:
                        j += 1
                        draw.text(
                            (120, 220),
                            f"{line}",
                            fill="white",
                            stroke_width=5,
                            stroke_fill="black",
                            font=font,
                        )
        draw.text(
                    (120, 340),
                    f"Views : {views[:23]}",
                    (255, 255, 255),
                    font=arial,
                )
        draw.text(
                    (120, 390),
                    f"Duration : {duration[:23]} Mins",
                    (255, 255, 255),
                    font=arial,
                )
        draw.text(
                    (120, 440),
                    f"Channel : {channel}",
                    (255, 255, 255),
                    font=arial,
                )
        
        draw.text(
                (540,550),
                f"ﮩﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ",
                (255, 255, 255),
                font=name_font,
        )
        draw.text(
            (50, 600),
            f"00:55 ─────────────●─────────────────────────────────────────── {duration}",
            (255, 255, 255),
            font=font3,
        
        )
        draw.text(
                (50,650),
                f"Volume: ■■■■■□□□                      ↻      ◁     II    ▷     ↺",
                (255, 255, 255),
                font=font4,
        )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}_{user_id}.png")
        return f"cache/{videoid}_{user_id}.png"
    except Exception as e:
        return YOUTUBE_IMG_URL



async def get_qthumb(videoid, user_id):
    if os.path.isfile(f"cache/que{videoid}_{user_id}.png"):
        return f"cache/que{videoid}_{user_id}.png"
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
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        try:
            wxyz = await bot.get_profile_photos(user_id)
            wxy = await bot.download_media(wxyz[0]['file_id'], file_name=f'{user_id}.jpg')
        except:
            abc = await bot.get_profile_photos(bot.id)
            wxy = await bot.download_media(abc[0]['file_id'], file_name=f'{bot.id}.jpg')
        xy = Image.open(wxy)
        a = Image.new('L', [640, 640], 0)
        b = ImageDraw.Draw(a)
        b.pieslice([(0, 0), (640,640)], 0, 360, fill = 255, outline = "white")
        c = np.array(xy)
        d = np.array(a)
        e = np.dstack((c, d))
        f = Image.fromarray(e)
        x = f.resize((107, 107))

        images = random.choice(thumbs)
        border = random.choice(colors)
        youtube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"YukkiMusic/Lol/{images}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)

        image3 = changeImageSize(1280, 720, bg)
        image5 = image3.convert("RGBA")
        Image.alpha_composite(background, image5).save(f"cache/temp{videoid}.png")

        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo.save(f"cache/chop{videoid}.png")
        if not os.path.isfile(f"cache/cropped{videoid}.png"):
            im = Image.open(f"cache/chop{videoid}.png").convert("RGBA")
            add_corners(im)
            im.save(f"cache/cropped{videoid}.png")

        crop_img = Image.open(f"cache/cropped{videoid}.png")
        logo = crop_img.convert("RGBA")
        logo.thumbnail((365, 365), Image.ANTIALIAS)
        width = int((1280 - 365) / 2)
        background = Image.open(f"cache/temp{videoid}.png")
        background.paste(logo, (width + 2, 138), mask=logo)
        background.paste(x, (710, 427), mask=x)
        background.paste(image3, (0, 0), mask=image3)
        img = ImageOps.expand(background, border=10, fill=f"{border}")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("YukkiMusic/Lol/font2.ttf", 45)
        ImageFont.truetype("YukkiMusic/Lol/font2.ttf", 70)
        arial = ImageFont.truetype("YukkiMusic/Lol/font2.ttf", 30)
        ImageFont.truetype("YukkiMusic/Lol/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        try:
            draw.text(
                (455, 35),
                "ADDED TO QUEUE",
                fill="white",
                stroke_width=1,
                stroke_fill="white",
                font=font,
            )
            if para[0]:
                text_w, text_h = draw.textsize(f"{para[0]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 560),
                    f"{para[0]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if para[1]:
                text_w, text_h = draw.textsize(f"{para[1]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 610),
                    f"{para[1]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
        except:
            pass
        text_w, text_h = draw.textsize(f"Duration: {duration} Mins", font=arial)
        draw.text(
            ((1280 - text_w) / 2, 665),
            f"Duration: {duration} Mins",
            fill="white",
            font=arial,
        )

        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        file = f"cache/que{videoid}_{user_id}.png"
        img.save(f"cache/que{videoid}_{user_id}.png")
        return f"cache/que{videoid}_{user_id}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
