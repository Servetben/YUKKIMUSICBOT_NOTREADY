from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, ChatMember
from YukkiMusic import app
import random 
# Initialize the Pyrogram client


# Function to check if a user has the "add new admins" permission
async def has_add_admin_permission(user_id, chat_id):
    member = await app.get_chat_member(chat_id, user_id)
    return member.status == "administrator" and member.can_promote_members

# Function to promote a member
async def promote_member(chat_id, user_id):
    # Replace these privileges with the ones you want to grant
    privileges = ChatPermissions(
        can_change_info=False,
        can_invite_users=True,
        can_delete_messages=True,
        can_restrict_members=False,
        can_pin_messages=True,
        can_promote_members=False,
        can_manage_chat=True,
        can_manage_video_chats=True,
    )
    await app.promote_chat_member(chat_id, user_id, permissions=privileges)

# Command to promote a member by reply or user ID
@app.on_message(filters.command("promote") & filters.reply)
async def promote_by_reply(client, message):
    chat_id = message.chat.id
    if await has_add_admin_permission(message.from_user.id, chat_id):
        replied_user_id = message.reply_to_message.from_user.id
        await promote_member(chat_id, replied_user_id)
        admin_mention = message.from_user.mention()
        user_mention = message.reply_to_message.from_user.mention()
        await message.reply(f"{admin_mention} has promoted {user_mention} to admin!")
    else:
        await message.reply("You don't have permission to promote members.")

# Command to promote a member by user ID
@app.on_message(filters.command("promote") & filters.group)
async def promote_by_user_id(client, message):
    chat_id = message.chat.id
    if len(message.command) == 2:
        if await has_add_admin_permission(message.from_user.id, chat_id):
            user_id = int(message.command[1])
            await promote_member(chat_id, user_id)
            admin_mention = message.from_user.mention()
            await message.reply(f"{admin_mention} has promoted a user to admin!")
        else:
            await message.reply("You don't have permission to promote members.")
    else:
        await message.reply("Please provide a user ID.")


      
