#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import time
from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message
import random
from config import BANNED_USERS
from strings import get_command, get_string, helpers
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils import help_pannel
from YukkiMusic.utils.database import get_lang, is_commanddelete_on
from YukkiMusic.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from YukkiMusic.utils.inline.help import (help_back_markup,
                                          private_help_panel)

#image 
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

### Command
HELP_COMMAND = get_command("HELP_COMMAND")


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.private
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await message.reply_photo(
                    photo=random.choice(YUMI_PICS),
                    await update.message.reply_text(
                _["help_1"], reply_markup=keyboard ))
        else:
            await message.reply_photo(
                    photo=random.choice(YUMI_PICS),
                    await update.message.reply_text(
                _["help_1"], reply_markup=keyboard ),
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await message.reply_photo(
                    photo=random.choice(YUMI_PICS),
                    await update.message.reply_text(
                _["help_1"], reply_markup=keyboard ),
            )


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
        _["help_2"], reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb5":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "Only for Sudo Users", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_5, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4, reply_markup=keyboard
        )
