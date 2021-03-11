from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""🥳🤩 Hello {message.from_user.first_name}!

 😘😍Sangram Ghangale Music bot don't allow to play music in your group through the new voice chats recently introduce by telegram
❌don't add the bot and your group and read the command list to find out how to use it!!

😍Bot developer - @sangramghangale

Use these buttons below to know more❤️👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎛Music Bot Command", url="https://t.me/sangramghangale96k"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "😍 Study Material", url="https://t.me/hscscienceMaharashtraboard"
                    ),
                    InlineKeyboardButton(
                        "😍 Official Channel", url="https://t.me/digestnotes"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**Sangram -** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
