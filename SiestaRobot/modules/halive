import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/6c63db45cd26d0a711da8.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Boa Hancock, Nice to meet you you are my Luffy💖💜** \n\n"
  TEXT += "🐍 **I'm Working Properly** \n\n"
  TEXT += f"🐍 **My Master : [Kazutora Hanemiya](https://t.me/zerohisoka)** \n\n"
  TEXT += f"🐍 **Library Version :** `{telever}` \n\n"
  TEXT += f"🐍 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"🐍 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/BoaHancock_Robot?start=help"), Button.url("ᴀɴɪᴍᴇ ᴄʜᴀᴛ", "https://t.me/straydogs")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
