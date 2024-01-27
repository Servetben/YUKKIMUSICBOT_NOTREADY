from pyrogram import filters
from pyrogram.types import Message
from YukkiMusic.utils.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from YukkiMusic import app
import random

IMP_PICS = [
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
"https://telegra.ph/file/502f442b5b1792ea3d5d5.jpg"
]


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""

**✰ɴᴀᴍᴇ** : {message.from_user.mention}
**✰ᴜsᴇʀ ɪᴅ** : {message.from_user.id}

\n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
** ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ **

**★Bᴇғᴏʀᴇ** : {bef}
**★Aғᴛᴇʀ** : {aft}

\n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ**

**♡Bᴇғᴏʀᴇ** : {bef}
**♡Aғᴛᴇʀ** : {aft}

""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ **

**✷Bᴇғᴏʀᴇ** : {bef}
**✷Aғᴛᴇʀ** : {aft}

\n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random.choice(IMP_PICS), caption=msg)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
  
