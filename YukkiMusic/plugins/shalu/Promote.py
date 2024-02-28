from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, ChatMember
from pyrogram.errors.exceptions.bad_request_400 import UserAdminInvalid

# Initialize the Pyrogram client
from YukkiMusic import app 
# Function to check if the user is an admin with "add new admins" permission
async def has_add_admin_permission(user_id, chat_id):
    member = await app.get_chat_member(chat_id, user_id)
    return member.status == "administrator" and member.can_promote_members

# Function to promote a member with specific privileges
async def promote_member(chat_id, user_id):
    privileges = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=True
    )
    try:
        await app.promote_chat_member(chat_id, user_id, permissions=privileges)
        return True
    except UserAdminInvalid:
        return False

# Command to promote a member via reply or user ID
@app.on_message(filters.command("zpromote") & filters.group)
async def promote_member_command(client, message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    
    # Check if the message is a reply
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    # Check if user ID is provided in the message
    elif len(message.command) == 2:
        user_id = int(message.command[1])
    else:
        # If neither reply nor user ID is provided, send a message to the group
        await message.reply_text("Please reply to a message or provide a user ID.")
        return
    
    # Check if the user is authorized to use the command
    if not await has_add_admin_permission(from_user_id, chat_id):
        await message.reply_text("You don't have permission to promote members.")
        return
    
    # Check if the bot has permission to promote members
    if not await has_add_admin_permission(await app.get_me().id, chat_id):
        await message.reply_text("I don't have permission to promote members.")
        return
    
    # Promote the member
    success = await promote_member(chat_id, user_id)
    if success:
        # If promoted successfully, send a message to the group
        admin_mention = message.from_user.mention()
        user_mention = message.reply_to_message.from_user.mention() if message.reply_to_message else f"`{user_id}`"
        await message.reply(f"{admin_mention} has promoted {user_mention} to admin!")
    else:
        # If promotion fails, send a message to the group
        await message.reply_text("Failed to promote the member.")

# Run the client
