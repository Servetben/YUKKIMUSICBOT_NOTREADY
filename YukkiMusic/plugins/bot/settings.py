#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
from time import time, strftime, gmtime
import config 
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from pyrogram.types import (CallbackQuery, InlineKeyboardButton, InputMediaVideo, 
                            InlineKeyboardMarkup, Message)

from config import (BANNED_USERS, CLEANMODE_DELETE_MINS,
                    MUSIC_BOT_NAME, OWNER_ID)
from strings import get_command
from YukkiMusic import app
import random 
from YukkiMusic.utils.database import (add_nonadmin_chat,
                                       cleanmode_off, cleanmode_on,
                                       commanddelete_off,
                                       commanddelete_on,
                                       get_aud_bit_name, get_authuser,
                                       get_authuser_names,
                                       get_playmode, get_playtype,
                                       get_vid_bit_name,
                                       is_cleanmode_on,
                                       is_commanddelete_on,
                                       is_nonadmin_chat,
                                       is_suggestion,
                                       remove_nonadmin_chat,
                                       save_audio_bitrate,
                                       save_video_bitrate,
                                       set_playmode, set_playtype,
                                       suggestion_off, suggestion_on)
from YukkiMusic.utils.decorators.admins import ActualAdminCB
from YukkiMusic.utils.decorators.language import language, languageCB
from YukkiMusic.utils.inline.settings import (
    audio_quality_markup, auth_users_markup,
    cleanmode_settings_markup, playmode_users_markup, setting_markup,
    video_quality_markup)
from YukkiMusic.utils.inline.start import private_panel

### Command
SETTINGS_COMMAND = get_command("SETTINGS_COMMAND")

VIDEO_URL = [
"https://telegra.ph/file/994be8612ef77a7f58a28.mp4",
"https://telegra.ph/file/192e3530d0825cb34f8e0.mp4",
"https://telegra.ph/file/bbe808e82960f66a32a33.mp4",
"https://telegra.ph/file/60984b88fceb89a2e4c43.mp4",
"https://telegra.ph/file/ef34cfb6939a318b73945.mp4",
"https://telegra.ph/file/1a8d35a6a9fba39c4c4b5.mp4",
"https://telegra.ph/file/689265192b9ab13a12545.mp4",
"https://telegra.ph/file/a596fcfd5e417135902a2.mp4",
"https://telegra.ph/file/3cdacd3b646c7b7182218.mp4",
"https://telegra.ph/file/05a70425e6d290a21f9de.mp4",
"https://telegra.ph/file/276bc97d487f7c69e6167.mp4",
"https://telegra.ph/file/03d1292236ddb3197f212.mp4",
"https://telegra.ph/file/f6171217c55cb4747a7da.mp4",
"https://telegra.ph/file/38e7abacc8c8f88c2fafc.mp4",
"https://telegra.ph/file/3f5602d66591fbd5793ec.mp4"
]
  
@app.on_message(
    filters.command(SETTINGS_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@language
async def settings_mar(client, message: Message, _):
    buttons = setting_markup(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(
    filters.regex("settings_helper") & ~BANNED_USERS
)
@languageCB
async def settings_cb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer(_["set_cb_8"])
    except:
        pass
    buttons = setting_markup(_)
    return await CallbackQuery.edit_message_text(
        _["setting_1"].format(
            CallbackQuery.message.chat.title,
            CallbackQuery.message.chat.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@app.on_callback_query(filters.regex("gib_source"))
async def gib_repo_callback(c: app, q: CallbackQuery):
    start = time()
    x = await c.send_message(q.message.chat.id, "ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ....")
    delta_ping = time() - start
    await x.delete()
    txt = f"""
Bʜᴀɢ Yᴀʜᴀ Sᴇ 😂 ʀᴇᴘᴏ ɴᴀʜɪ ᴍɪʟᴇɢɪ ✨
    """
    await q.answer(txt, show_alert=True)
    return

@app.on_callback_query(filters.regex("^bot_info_data$"))
async def show_bot_info(c: app, q: CallbackQuery):
    start = time()
    x = await c.send_message(q.message.chat.id, "Fᴇᴛᴄʜɪɴɢ Iɴғᴏʀᴍᴀᴛɪᴏɴ....")
    delta_ping = time() - start
    await x.delete()
    txt = f"""
    💫 Pɪɴɢ: {delta_ping * 1000:.3f} ms   
    ✨ Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ: 3.10.4
    🎀 Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ: 2.0.106
    """
    await q.answer(txt, show_alert=True)
    return


@app.on_callback_query(
    filters.regex("settingsback_helper") & ~BANNED_USERS
)
@languageCB
async def settings_back_markup(
    client, CallbackQuery: CallbackQuery, _
):
    try:
        await CallbackQuery.answer()
    except Exception as e:
        print(f"An error occurred: {e}")

    if CallbackQuery.message.chat.type == ChatType.PRIVATE:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        buttons = private_panel(_, app.username, OWNER)
        try:
            await CallbackQuery.edit_message_text(
                _["start_2"].format(MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            pass
    else:
        buttons = setting_markup(_)
        try:
            await CallbackQuery.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except MessageNotModified:
            pass


## Audio and Video Quality
async def gen_buttons_aud(_, aud):
    if aud == "STUDIO":
        buttons = audio_quality_markup(_, STUDIO=True)
    elif aud == "HIGH":
        buttons = audio_quality_markup(_, HIGH=True)
    elif aud == "MEDIUM":
        buttons = audio_quality_markup(_, MEDIUM=True)
    elif aud == "LOW":
        buttons = audio_quality_markup(_, LOW=True)
    return buttons


async def gen_buttons_vid(_, aud):
    if aud == "UHD_4K":
        buttons = video_quality_markup(_, UHD_4K=True)
    elif aud == "QHD_2K":
        buttons = video_quality_markup(_, QHD_2K=True)
    elif aud == "FHD_1080p":
        buttons = video_quality_markup(_, FHD_1080p=True)
    elif aud == "HD_720p":
        buttons = video_quality_markup(_, HD_720p=True)
    elif aud == "SD_480p":
        buttons = video_quality_markup(_, SD_480p=True)
    elif aud == "SD_360p":
        buttons = video_quality_markup(_, SD_360p=True)
    return buttons


# without admin rights


@app.on_callback_query(
    filters.regex(
        pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|CMANSWER|COMMANDANSWER|SUGGANSWER|CM|AQ|VQ|PM|AU)$"
    )
    & ~BANNED_USERS
)
@languageCB
async def without_Admin_rights(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "SEARCHANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_3"], show_alert=True
            )
        except:
            return
    if command == "PLAYMODEANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_10"], show_alert=True
            )
        except:
            return
    if command == "PLAYTYPEANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_11"], show_alert=True
            )
        except:
            return
    if command == "AUTHANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_4"], show_alert=True
            )
        except:
            return
    if command == "CMANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_9"].format(CLEANMODE_DELETE_MINS),
                show_alert=True,
            )
        except:
            return
    if command == "COMMANDANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_14"], show_alert=True
            )
        except:
            return
    if command == "SUGGANSWER":
        try:
            return await CallbackQuery.answer(
                _["setting_16"], show_alert=True
            )
        except:
            return
    if command == "CM":
        try:
            await CallbackQuery.answer(_["set_cb_5"], show_alert=True)
        except:
            pass
        sta = None
        cle = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            cle = True
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            sta = True
        sug = None
        if await is_suggestion(CallbackQuery.message.chat.id):
            sug = True
        buttons = cleanmode_settings_markup(
            _, status=cle, dels=sta, sug=sug
        )
    if command == "AQ":
        try:
            await CallbackQuery.answer(_["set_cb_1"], show_alert=True)
        except:
            pass
        aud = await get_aud_bit_name(CallbackQuery.message.chat.id)
        buttons = await gen_buttons_aud(_, aud)
    if command == "VQ":
        try:
            await CallbackQuery.answer(_["set_cb_2"], show_alert=True)
        except:
            pass
        aud = await get_vid_bit_name(CallbackQuery.message.chat.id)
        buttons = await gen_buttons_vid(_, aud)
    if command == "PM":
        try:
            await CallbackQuery.answer(_["set_cb_4"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "AU":
        try:
            await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except:
            pass
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            buttons = auth_users_markup(_, True)
        else:
            buttons = auth_users_markup(_)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


# Audio Video Quality


@app.on_callback_query(
    filters.regex(pattern=r"^(LOW|MEDIUM|HIGH|STUDIO|SD_360p|SD_480p|HD_720p|FHD_1080p|QHD_2K|UHD_4K)$")
    & ~BANNED_USERS
)
@ActualAdminCB
async def aud_vid_cb(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    try:
        await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
    except:
        pass
    if command == "LOW":
        await save_audio_bitrate(CallbackQuery.message.chat.id, "LOW")
        buttons = audio_quality_markup(_, LOW=True)
    if command == "MEDIUM":
        await save_audio_bitrate(
            CallbackQuery.message.chat.id, "MEDIUM"
        )
        buttons = audio_quality_markup(_, MEDIUM=True)
    if command == "HIGH":
        await save_audio_bitrate(
            CallbackQuery.message.chat.id, "HIGH"
        )
        buttons = audio_quality_markup(_, HIGH=True)
    if command == "STUDIO":
        await save_audio_bitrate(
            CallbackQuery.message.chat.id, "STUDIO"
        )
        buttons = audio_quality_markup(_, STUDIO=True)
    if command == "SD_360p":
        await save_video_bitrate(CallbackQuery.message.chat.id, "SD_360p")
        buttons = video_quality_markup(_, SD_360p=True)
    if command == "SD_480p":
        await save_video_bitrate(
            CallbackQuery.message.chat.id, "SD_480p"
        )
        buttons = video_quality_markup(_, SD_480p=True)
    if command == "HD_720p":
        await save_video_bitrate(
            CallbackQuery.message.chat.id, "HD_720p"
        )
        buttons = video_quality_markup(_, HD_720p=True)
    if command == "FHD_1080p":
        await save_video_bitrate(
            CallbackQuery.message.chat.id, "FHD_1080p"
        )
        buttons = video_quality_markup(_, FHD_1080p=True)
    if command == "QHD_2K":
        await save_video_bitrate(
            CallbackQuery.message.chat.id, "QHD_2K"
        )
        buttons = video_quality_markup(_, QHD_2K=True)
    if command == "UHD_4K":
        await save_video_bitrate(
            CallbackQuery.message.chat.id, "UHD_4K"
        )
        buttons = video_quality_markup(_, UHD_4K=True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


# Play Mode Settings
@app.on_callback_query(
    filters.regex(
        pattern=r"^(|MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE)$"
    )
    & ~BANNED_USERS
)
@ActualAdminCB
async def playmode_ans(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "CHANNELMODECHANGE":
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = None
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            Group = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = None
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "MODECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
        except:
            pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            await set_playmode(
                CallbackQuery.message.chat.id, "Inline"
            )
            Direct = None
        else:
            await set_playmode(
                CallbackQuery.message.chat.id, "Direct"
            )
            Direct = True
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            Group = True
        else:
            Group = None
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            Playtype = False
        else:
            Playtype = True
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    if command == "PLAYTYPECHANGE":
        try:
            await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
        except:
            pass
        playty = await get_playtype(CallbackQuery.message.chat.id)
        if playty == "Everyone":
            await set_playtype(CallbackQuery.message.chat.id, "Admin")
            Playtype = False
        else:
            await set_playtype(
                CallbackQuery.message.chat.id, "Everyone"
            )
            Playtype = True
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        if playmode == "Direct":
            Direct = True
        else:
            Direct = None
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            Group = True
        else:
            Group = None
        buttons = playmode_users_markup(_, Direct, Group, Playtype)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


# Auth Users Settings
@app.on_callback_query(
    filters.regex(pattern=r"^(AUTH|AUTHLIST)$") & ~BANNED_USERS
)
@ActualAdminCB
async def authusers_mar(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "AUTHLIST":
        _authusers = await get_authuser_names(
            CallbackQuery.message.chat.id
        )
        if not _authusers:
            try:
                return await CallbackQuery.answer(
                    _["setting_5"], show_alert=True
                )
            except:
                return
        else:
            try:
                await CallbackQuery.answer(
                    _["set_cb_7"], show_alert=True
                )
            except:
                pass
            j = 0
            await CallbackQuery.edit_message_text(_["auth_6"])
            msg = _["auth_7"]
            for note in _authusers:
                _note = await get_authuser(
                    CallbackQuery.message.chat.id, note
                )
                user_id = _note["auth_user_id"]
                admin_id = _note["admin_id"]
                admin_name = _note["admin_name"]
                try:
                    user = await client.get_users(user_id)
                    user = user.first_name
                    j += 1
                except Exception:
                    continue
                msg += f"{j}➤ {user}[`{user_id}`]\n"
                msg += (
                    f"   {_['auth_8']} {admin_name}[`{admin_id}`]\n\n"
                )
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=_["BACK_BUTTON"], callback_data=f"AU"
                        ),
                        InlineKeyboardButton(
                            text=_["CLOSE_BUTTON"],
                            callback_data=f"close",
                        ),
                    ]
                ]
            )
            try:
                return await CallbackQuery.edit_message_text(
                    msg, reply_markup=upl
                )
            except MessageNotModified:
                return
    try:
        await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
    except:
        pass
    if command == "AUTH":
        is_non_admin = await is_nonadmin_chat(
            CallbackQuery.message.chat.id
        )
        if not is_non_admin:
            await add_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_)
        else:
            await remove_nonadmin_chat(CallbackQuery.message.chat.id)
            buttons = auth_users_markup(_, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return


## Clean Mode


@app.on_callback_query(
    filters.regex(
        pattern=r"^(CLEANMODE|COMMANDELMODE|SUGGESTIONCHANGE)$"
    )
    & ~BANNED_USERS
)
@ActualAdminCB
async def cleanmode_mark(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    try:
        await CallbackQuery.answer(_["set_cb_6"], show_alert=True)
    except:
        pass
    if command == "CLEANMODE":
        sta = None
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            sta = True
        sug = None
        if await is_suggestion(CallbackQuery.message.chat.id):
            sug = True
        cle = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            await cleanmode_off(CallbackQuery.message.chat.id)
        else:
            await cleanmode_on(CallbackQuery.message.chat.id)
            cle = True
        buttons = cleanmode_settings_markup(
            _, status=cle, dels=sta, sug=sug
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    if command == "COMMANDELMODE":
        cle = None
        sta = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            cle = True
        sug = None
        if await is_suggestion(CallbackQuery.message.chat.id):
            sug = True
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            await commanddelete_off(CallbackQuery.message.chat.id)
        else:
            await commanddelete_on(CallbackQuery.message.chat.id)
            sta = True
        buttons = cleanmode_settings_markup(
            _, status=cle, dels=sta, sug=sug
        )
    if command == "SUGGESTIONCHANGE":
        cle = None
        sta = None
        if await is_cleanmode_on(CallbackQuery.message.chat.id):
            cle = True
        if await is_commanddelete_on(CallbackQuery.message.chat.id):
            sta = True
        if await is_suggestion(CallbackQuery.message.chat.id):
            await suggestion_off(CallbackQuery.message.chat.id)
            sug = False
        else:
            await suggestion_on(CallbackQuery.message.chat.id)
            sug = True
        buttons = cleanmode_settings_markup(
            _, status=cle, dels=sta, sug=sug
        )
    try:
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except MessageNotModified:
        return

