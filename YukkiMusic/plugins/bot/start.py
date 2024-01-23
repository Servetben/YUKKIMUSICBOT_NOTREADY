#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
import random
from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

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
"https://telegra.ph/file/e19f14793913c7947973d.jpg"

]


loop = asyncio.get_running_loop()


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(YUMI_PICS),
              caption=_["start_2"].format(config.SUPPORT_CHAT),
                reply_markup=start_pannel,
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
🔍__**Video Track Information**__

❇️**Title:** {title}

⏳**Duration:** {duration} Mins
👀**Views:** `{views}`
⏰**Published Time:** {published}
🎥**Channel Name:** {channel}
📎**Channel Link:** [Visit From Here]({channellink})
🔗**Video Link:** [Link]({link})

⚡️ __Searched Powered By {config.MUSIC_BOT_NAME}__"""
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
                parse_mode=ParseMode.MARKDOWN,
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
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
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
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
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
