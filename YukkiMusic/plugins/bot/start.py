#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import time
from time import time, strftime, gmtime
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
import random 
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

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]

STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

YUMI_PICS = [
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
"https://telegra.ph/file/7c4bf50287cc170d167c4.jpg",
"https://telegra.ph/file/4d0230d9ed3bf635c712a.jpg",
"https://telegra.ph/file/e2f9e93ba5af08a7930da.jpg",
"https://telegra.ph/file/60a2c14dadf79cd394d59.jpg",
"https://telegra.ph/file/2c564f940bf888aff4721.jpg",
"https://telegra.ph/file/4ba7e7a4c99f29fad2fb8.jpg",
"https://telegra.ph/file/912a1496be6da2e021a9a.jpg",
"https://telegra.ph/file/9a8ecf040565f18b480e4.jpg",
"https://telegra.ph/file/4b637281b81d3f637f643.jpg",
"https://telegra.ph/file/02fa944693f8fbcddbdde.jpg",
"https://telegra.ph/file/393d12eb83a47a0499312.jpg",
"https://telegra.ph/file/4899608b9d4efeb30ab3d.jpg",
"https://telegra.ph/file/3992f6c841bbeadad51c2.jpg",
"https://telegra.ph/file/31c70758a9f35665ee769.jpg",
"https://telegra.ph/file/d1a1932b2d0d3085c3e8c.jpg",
"https://telegra.ph/file/cb13f1b053b99afde7b6e.jpg",
"https://telegra.ph/file/21bc78f527468bc17974f.jpg",
"https://telegra.ph/file/4db7502007aeeced8ba6f.jpg",
"https://telegra.ph/file/616dcf138c736cde4e3e6.jpg",
"https://telegra.ph/file/4ba0f55315b322b77ed17.jpg",
"https://telegra.ph/file/c26dafda0eaa0e9eb6535.jpg",
"https://telegra.ph/file/ac895ede3b122f7c34129.jpg",
"https://telegra.ph/file/54e4428eb161f2198e328.jpg",
"https://telegra.ph/file/5084957be8730f10d8e18.jpg",
"https://telegra.ph/file/e1b2272788148fc8f7dba.jpg",
"https://telegra.ph/file/6cd7dde536d6202f03445.jpg",
"https://telegra.ph/file/502f442b5b1792ea3d5d5.jpg",
"https://telegra.ph/file/aaca55c2ee7a6b07b21bc.jpg",
"https://telegra.ph/file/09934be4fddb038bb95c3.jpg",
"https://telegra.ph/file/4c0871bf5a164e4f110ed.jpg",
"https://telegra.ph/file/9527e8096fd1b45dd7f56.jpg",
"https://telegra.ph/file/d87eeeee3e1a6a285fd1a.jpg",
"https://telegra.ph/file/319ee44d3e1716761e654.jpg",
"https://telegra.ph/file/cba4d51f4b705343b6d18.jpg",
"https://telegra.ph/file/62e42e5debdf2f01223c1.jpg",
"https://telegra.ph/file/1cf6a751b82d46b0fc72b.jpg",
"https://telegra.ph/file/0cada0f858519a4152de1.jpg",
"https://telegra.ph/file/1c3349bce3f6ac80370a9.jpg",
"https://telegra.ph/file/864ac650da888172e868e.jpg",
"https://telegra.ph/file/aa168dc664cd4d36786d7.jpg",
"https://telegra.ph/file/310977b8c34cf82f84068.jpg",
"https://telegra.ph/file/fd96eb737941a8b8038b0.jpg",
"https://telegra.ph/file/e5df7da7247223d697d51.jpg",
"https://telegra.ph/file/1c578106c6ee7d684e243.jpg",
"https://telegra.ph/file/e170aa7205bb17191b6e3.jpg",
"https://telegra.ph/file/353333477732b8974de7c.jpg",
"https://telegra.ph/file/bd306d487af6665d39cc9.jpg",
"https://telegra.ph/file/65e271ef53ddcc278b236.jpg",
"https://telegra.ph/file/7c426176b62451c850407.jpg",  
"https://telegra.ph/file/8c57ff583f318c3ec0c64.jpg",
"https://telegra.ph/file/5cb2cedfc9b9b4920153f.jpg",
"https://telegra.ph/file/9aedda90fe8a0eedad19f.jpg",
"https://telegra.ph/file/c283c008b1c1bf9d2d975.jpg",
"https://telegra.ph/file/f689f10776c7190fd6746.jpg",
"https://telegra.ph/file/d5a0f6e76dc4b966486f0.jpg",
"https://telegra.ph/file/58bc56c9bc188e85d1b5c.jpg",
"https://telegra.ph/file/0f26e6356ff84ba45a05f.jpg",
"https://telegra.ph/file/1fbb0542ff62dc4ab0782.jpg",
"https://telegra.ph/file/e19f14793913c7947973d.jpg",
"https://telegra.ph/file/c4896c1bc28dbda543e9a.jpg",
"https://telegra.ph/file/04ec410a5e098a31ef05c.jpg",
"https://telegra.ph/file/6d91dbc82b9985dd7f5bd.jpg", 
"https://telegra.ph/file/742122358afbdce1812aa.jpg",
"https://telegra.ph/file/9992032cde0ebdc5ce22f.jpg",
"https://telegra.ph/file/b0678a2763abd78550cb1.jpg",
"https://telegra.ph/file/08aed3ff4207ab128599c.jpg",
"https://telegra.ph/file/012b897f0dc2cf5e46dd7.jpg",
"https://telegra.ph/file/28e8a842f83ef8a936a73.jpg",
"https://telegra.ph/file/b652fb712536b64644cd0.jpg",
"https://telegra.ph/file/80fb21d13da79f45a6b3c.jpg",
"https://telegra.ph/file/ebbdac8dbe121ad724a1a.jpg",
"https://telegra.ph/file/b5baf462b6afbfe11cfd8.jpg",
"https://telegra.ph/file/2a2c5d6e11611635813c8.jpg",
"https://telegra.ph/file/2952e480c6748f481acec.jpg",
"https://telegra.ph/file/4c9c874eb27f47d1744ee.jpg",
"https://telegra.ph/file/71b4c5143532982fbf326.jpg",
"https://telegra.ph/file/0e7864982ddd768c0e268.jpg",
"https://telegra.ph/file/3dbbf7c02a601864333ff.jpg",
"https://telegra.ph/file/21b828d6f52395fee7347.jpg",
"https://telegra.ph/file/b1b4860b4bcc63ea06020.jpg",
"https://telegra.ph/file/efe8d6d5e451eaf2c823b.jpg",
"https://telegra.ph/file/6915fa51b93f102d728d1.jpg",
"https://telegra.ph/file/aac96626fff9e97719d99.jpg",
"https://telegra.ph/file/d9f451277fc14ab8fb046.jpg",
"https://telegra.ph/file/af76e0e0369877ff9ee96.jpg",
"https://telegra.ph/file/a62f55e1ee715c5fda49e.jpg",
"https://telegra.ph/file/e63fad358a31971d0226e.jpg",
"https://telegra.ph/file/d329dab2265ee38e8596c.jpg",
"https://telegra.ph/file/8e409dd00351e52c0b832.jpg",
"https://telegra.ph/file/d81edcb736dd1eb3e3f28.jpg",
"https://telegra.ph/file/c1e9ea3472d2e88e2cd9e.jpg",
"https://telegra.ph/file/fce7a6531e493d3f170d2.jpg",
"https://telegra.ph/file/dac47da8d3c34944d905e.jpg",
"https://telegra.ph/file/3db89104698f8c59c9f2f.jpg",
"https://telegra.ph/file/3ab1242f4c692cee890b3.jpg",
"https://telegra.ph/file/989a133f1a1fa91eef931.jpg",
"https://telegra.ph/file/2c14b613bfb4e21ddf66b.jpg",
"https://telegra.ph/file/67e09a6b45f9210db54a7.jpg",
"https://telegra.ph/file/d36acf08120d275c76555.jpg",
"https://telegra.ph/file/3f69614121059aba0aa53.jpg",
"https://telegra.ph/file/a884b01bfd9749edf1e44.jpg",
"https://telegra.ph/file/6c1b34786d6aa1427aa34.jpg",
"https://telegra.ph/file/6255f3e1a0d1935d81686.jpg",
"https://telegra.ph/file/63f82e98e24c5a9c2dc2c.jpg",
"https://telegra.ph/file/8aa6c354fc55c8aa40e1e.jpg",
"https://telegra.ph/file/40c70455f620b8a1c5f2b.jpg",
"https://telegra.ph/file/638e6c6e615f75683c97e.jpg",
"https://telegra.ph/file/c49862ca13d5f96e1055f.jpg",
"https://telegra.ph/file/1538811747a6c3c26d0c7.jpg",
"https://telegra.ph/file/5dc97f410e8886477f45c.jpg",
"https://telegra.ph/file/df6d158f8cd3a82d1aa81.jpg",
"https://telegra.ph/file/78ab7d6fcae20817167bb.jpg",
"https://telegra.ph/file/6a33f6c47069cdcb6699b.jpg",
"https://telegra.ph/file/3b415bcf9ef3f3c5f71c1.jpg",
"https://telegra.ph/file/fc150e19584ceb9532b84.jpg",
"https://telegra.ph/file/52b4f1556b87806118651.jpg",
"https://telegra.ph/file/31f7ce3848156e77521f7.jpg",
"https://telegra.ph/file/dc3210c66a61143fe134d.jpg",
"https://telegra.ph/file/2102f3b08150b2355fa55.jpg",
"https://telegra.ph/file/3d3d19956d3f62717b7b3.jpg",
"https://telegra.ph/file/282229aa4ad14450f19f4.jpg",
"https://telegra.ph/file/c3e4a11ddc59c29c896b5.jpg",
"https://telegra.ph/file/f2ecb3cc334cb184ceb0a.jpg"
]



loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start_command(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_text(
                _["help_1"], reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                "🔎 Fetching your personal stats.!"
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[Telegram Files and Audios](https://t.me/telegram) ** played {count} times**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} has just started bot to check <code>SUDOLIST</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "Failed to get lyrics."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 Fetching Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
ㅤㅤ**💓 ❰ 𝐒ᴏɴɢ ♫ 𝐈ɴғᴏʀᴍᴀᴛɪᴏɴ ❱ 💓**
        
**𝐍𝐚𝐦𝐞 ➪ [{title}]({link})**　　

**𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 ➪ [{duration} ᴍɪɴ.]({link})**
**𝐕𝐢𝐞𝐰𝐬 ➪ [{views}]({link})**
**𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐎𝐧 ➪ [{published}]({link})**
**𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ➪ [{channel}]({link})**
**𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐋𝐢𝐧𝐤 ➪ [ᴠɪsɪᴛ ᴄʜᴀɴɴᴇʟ]({channellink})**
**𝐋𝐢𝐧𝐤 ➪ [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})**

☆........☆...ᴍᴀᴅᴇ ʙʏ » Ꮥʜꫝʟɪɴɪ....☆"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Watch ", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🔄 Close", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} has just started bot to check <code>VIDEO INFORMATION</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        accha = await message.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await message.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await message.reply_photo(
                   random.choice(YUMI_PICS),
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME ),
                  reply_markup=InlineKeyboardMarkup(out),
      )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} has just started Bot.\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    out = start_pannel(_)
    return await message.reply_text(
        _["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**Private Music Bot**\n\nOnly for authorized chats from the owner. Ask my owner to allow your chat first."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
