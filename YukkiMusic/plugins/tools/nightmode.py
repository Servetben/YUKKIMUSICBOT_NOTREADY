import random 
from pyrogram import filters,Client,enums
from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from YukkiMusic.mongo.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = False )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("๏ ᴇɴᴀʙʟᴇ ๏", callback_data="add_night"),InlineKeyboardButton("๏ ᴅɪsᴀʙʟᴇ ๏", callback_data="rm_night")]])         

@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph/file/91370f62c00ccc0c69841.jpg", caption="**ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ɴɪɢʜᴛᴍᴏᴅᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("**๏ ᴀᴅᴅᴇᴅ ᴄʜᴀᴛ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ . ᴛʜɪs ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ᴄʟᴏsᴇᴅ ᴏɴ 𝟷𝟸ᴀᴍ [IST] ᴀɴᴅ ᴡɪʟʟ ᴏᴘᴇɴᴇᴅ ᴏɴ 𝟶𝟼ᴀᴍ [IST] .**") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ !**")
            elif not check_night:
                await query.message.edit_caption("**๏  ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ  ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**") 
            
    
    
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://telegra.ph/file/83a4c8921c49934558542.jpg",
                caption= f"**Bᴇғᴏʀᴇ ʏᴏᴜ ɢᴏ ᴛᴏ sʟᴇᴇᴘ\nᴅᴏ ɴᴏᴛ ғᴏʀɢᴇᴛ ᴛᴏ sᴀʏ ᴛʜᴀɴᴋs ғᴏʀ ᴇᴠᴇʀʏᴛʜɪɴɢ ɢᴏᴏᴅ ᴛʜᴀᴛ ʜᴀs ʜᴀᴘᴘᴇɴᴇᴅ ᴛᴏ ʏᴏᴜ ɪɴ ᴛʜᴇ ʟᴀsᴛ 𝟸𝟺 ʜᴏᴜʀs. I ᴀᴍ ᴛʜᴀɴᴋғᴜʟ ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ ғᴏʀ ʏᴏᴜ**")
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://telegra.ph/file/d289562698b698711c3cd.jpg",
                caption= f"**Nᴏ ᴍᴀᴛᴛᴇʀ ʜᴏᴡ ʙᴀᴅ ᴛʜɪɴɢs ᴀʀᴇ, ʏᴏᴜ ᴄᴀɴ ᴀᴛ ʟᴇᴀsᴛ ʙᴇ ʜᴀᴘᴘʏ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴏᴋᴇ ᴜᴘ ᴛʜɪs ᴍᴏʀɴɪɴɢ**")
            
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()


