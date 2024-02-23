from pyrogram import filters, enums
from pyrogram.types import Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)

import datetime
import random 
from logging import getLogger
from AnnieMusic import LOGGER
from config import LOG_GROUP_ID
from AnnieMusic.misc import SUDOERS
from AnnieMusic import app
from config import OWNER_ID
from pyrogram.types import *
from AnnieMusic.utils.annieban import admin_filter

LOGGER = getLogger(__name__)

KICKIMG = [
"https://telegra.ph/file/c777a8fba33ea23e20f02.jpg",
"https://telegra.ph/file/eb2a1b5875dbd87ad16b5.jpg",
"https://telegra.ph/file/eb360fb4e80d7bb08b941.jpg",
"https://telegra.ph/file/4f5d1d86be0a8b5e7d81d.jpg",
"https://telegra.ph/file/eceb13fc17b0150aa9cea.jpg",
"https://telegra.ph/file/6f3a8b5643d0ca82bd1f6.jpg",
"https://telegra.ph/file/9a12a9d6a9fea986f2ec7.jpg",
"https://telegra.ph/file/fe4c74858d288d5c61e65.jpg",
"https://telegra.ph/file/a6ee40f2a954fdac9cb18.jpg",
]

button = [
       [
            InlineKeyboardButton(
                text="test",     url=f"https://t.me/Pokemon",
            )
        ]
]
def mention(user, name, mention=True):
    if mention == True:
        link = f"[{name}](tg://openmessage?user_id={user})"
    else:
        link = f"[{name}](https://t.me/{user})"
    return link



async def get_userid_from_username(username):
    try:
        user = await app.get_users(username)
    except:
        return None
    
    user_obj = [user.id, user.first_name]
    return user_obj

async def zkick_user(user_id, first_name, admin_id, admin_name, chat_id, message):
    try:
        await app.ban_chat_member(chat_id, user_id)
        await app.unban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "Ban rights? Nah, I'm just here for the digital high-fives 🙌\nGive me ban rights! 😡🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont ban an admin bruh!!"
        return msg_text, False
    except Exception as e:
        if user_id == 6761639198:
            msg_text = "why should i ban myself? sorry but I'm not stupid like you"
            return msg_text, False
        msg_text = f"opps!!\n{e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    await app.send_message(LOG_GROUP_ID, f"{user_mention} was kicked by {admin_mention} in {message.chat.title}")
    ZYEAHHHH = await message.reply_photo(
        photo=random.choice(KICKIMG),
        caption=f"{user_mention} was kicked by {admin_mention}\n",
        reply_markup=InlineKeyboardMarkup(button)
    )
    return ZYEAHHHH, True
    



@app.on_message(filters.command("kick") & admin_filter)
async def kickk_user(client, message):
    chat = message.chat
    reply = message.reply_to_message
    chat_id = message.chat.id
    admin_id = message.from_user.id
    user_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "Sᴏʀʀʏ ʙᴜᴛ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ sᴏᴍᴇᴏɴᴇ"
            return await message.reply_text(msg_text)
    else:
        msg_text = "Sᴏʀʀʏ ʙᴜᴛ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ sᴏᴍᴇᴏɴᴇ"
        return await message.reply_text(msg_text)
        
    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            reason = message.text.split(None, 1)[1]
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return
msg_text, result = await zkick_user(user_id, first_name, admin_id, admin_name, chat_id, message)
if result == False:
        await message.reply_text(msg_text)

@app.on_message(filters.command("kickme") & filters.group)
async def kickme_command(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chat_id = message.chat.id

    try:
        # kick him
        await app.ban_chat_member(chat_id, user_id)
        # Mention the kicked member in the group
        await message.reply_photo(
            photo=random.choice(KICKIMG),
            caption=f"{user_name} ʜᴀs ʙᴇᴇɴ sᴇʟғ ᴋɪᴄᴋᴇᴅ ᴏᴜᴛ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ.",
            reply_markup=InlineKeyboardMarkup(button),
        )
        await app.send_message(LOG_GROUP_ID, f"{user_name} used kickme command from {message.chat.id}")
    except Exception as e:
        # Handle any errors that may occur during the kicking process
        await message.reply_text(f"An error occurred: {str(e)}")
