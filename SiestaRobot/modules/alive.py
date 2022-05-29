import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/1a73924778901c994e1c1.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ᴋᴏɴɪɴᴄʜɪᴡᴀ [{event.sender.first_name}](tg://user?id={event.sender.id}), ɪ'ᴍ ɴᴀᴍɪ♡ ɪ ᴀᴍ ᴡᴏʀᴋɪɴɢ ᴘᴇʀꜰᴇᴄᴛʟʏ**\nɪ ᴀᴍ ʜᴇʀᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ꜱᴏ ɢɪᴠᴇ ᴍᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ\nꜰᴏʀ ᴀɴʏ ᴘʀᴏʙʟᴇᴍꜱ ɪɴ ʙᴏᴛ ᴀꜱᴋ ᴍʏ ᴅᴇᴠꜱ - @zerohisooka\n\n"
  TEXT += "♡ **I'm Working Properly** \n\n"
  TEXT += f"♡ **Library Version :** `{telever}` \n\n"
  TEXT += f"♡ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += "**Thanks For Adding Me Here ♡**"
  BUTTON = [[Button.url("Help", "https://t.me/namiirobot?start=help"), Button.url("Support", "https://t.me/boahancock_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

#I'm Nami♡.I am Working Perfectly
