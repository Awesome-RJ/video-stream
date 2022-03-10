# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{Veez.ASSISTANT_NAME } to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /vplay (reply to video) to start streaming.
6.) type /vstop to end the video streaming.

📝 **note: stream & stop command can only be executed by group admin only!**

⚡ __Maintained by Veez Project Team__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        "✨ **Hello there, I am a telegram group video streaming bot.**\\n\\n💭 **I was created to stream videos in group ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❔ HOW TO USE THIS BOT", callback_data="cbguide"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Terms & Condition", callback_data="cbinfo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url=f"https://t.me/{Veez.GROUP_NAME}"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel", url=f"https://t.me/{Veez.CHANNEL_NAME}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🧙🏻‍♂️ Owner", url=f"https://t.me/{Veez.OWNER_NAME}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 All Command List", callback_data="cblist"
                    )
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        """🌐 **bot information !**\x1f\x1f🤖 __This bot was created to stream video in telegram group video chats using several methods from WebRTC.__\x1f\x1f💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API \x1fClient Library and Framework in Pure Python for Users and Bots.__\x1f\x1f👨🏻\u200d💻 __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__\x1f\x1f👩🏻\u200d✈️ » [Levina Shavila](https://github.com/levina-lab)\x1f🤵🏻 » [Sammy-XD](https://github.com/Sammy-XD)\x1f🤵🏻 » [Zxce3](https://github.com/Zxce3)\x1f🤵🏻 » [Tofik Denianto](https://github.com/tofikdn)\x1f🤵🏻 » [Shohih Abdul](https://github.com/DoellBarr)\x1f\x1f__This bot licensed under GNU-GPL 3.0 License__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🏡 Go Back", callback_data="cbstart")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        """📚 All Command List:\x1f\x1f» /vplay (reply to video or yt/live url) - to stream video\x1f» /vstop - stop the video streaming\x1f» /song (song name) - download song from YT\x1f» /vsong (video name) - download video from YT\x1f» /lyric (song name) - lyric scrapper\x1f» /vjoin - invite assistant join to your group\x1f» /vleave - order assistant leave from your group\x1f\x1f🎊 FUN CMD:\x1f\x1f» /asupan - check it by yourself\x1f» /chika - check it by yourself\x1f» /wibu - check it by yourself\x1f» /truth - check it by yourself\x1f» /dare - check it by yourself\x1f\x1f🔰 EXTRA CMD:\x1f\x1f» /tts (reply to text) - text to speech\x1f» /alive - check bot alive status\x1f» /ping - check bot ping status\x1f» /uptime - check bot uptime status\x1f» /sysinfo - check bot system information\x1f\x1f💡 SUDO ONLY:\x1f\x1f» /rmd - remove all downloaded files\x1f» /rmw - remove all downloaded raw files\x1f» /leaveall - order assistant leave from all group\x1f\x1f⚡ __Maintained by Veez Project Team__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🏡 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
