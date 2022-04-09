import datetime
import re
from SiestaRobot import telethn as tbot
from SiestaRobot.modules.helper_funcs.tools import post_to_telegraph
from hentai import Hentai, Utils
from natsort import natsorted
import html
import textwrap
client = tbot
import asyncio
import time
from SiestaRobot.events import register
from telethon import Button
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
import os
import html
import nekos
import requests
from PIL import Image
from telegram import ParseMode
from SiestaRobot import dispatcher, updater
import SiestaRobot.modules.sql.nsfw_sql as sql
from SiestaRobot.modules.log_channel import gloggable
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CommandHandler, run_async, CallbackContext
from SiestaRobot.modules.helper_funcs.filters import CustomFilters
from SiestaRobot.modules.helper_funcs.chat_status import user_admin
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown




@register(pattern=r"^/boanh ?(.*)")
@register(pattern=r"^/nh ?(.*)")
async def nhe(event):
    message_id = event.message.id
    chat_id = event.chat_id
    input_str = event.pattern_match.group(1)
    code = input_str
    is_nsfw = sql.is_nsfw(chat_id)
    if not is_nsfw:
        await event.reply("`Dude! enable NSFW before getting any doujins from me.`")
        return
    if "nhentai" in input_str:
        link_regex = r"(?:https?://)?(?:www\.)?nhentai\.net/g/(\d+)"
        match = re.match(link_regex, input_str)
        code = match.group(1)
    if input_str == "random":
        code = Utils.get_random_id()
    if input_str == "" or input_str == " ":
        await event.reply("Gimme some valid code to search. It'll work like:\n • `/nhentai <code>` or `/nhentai random`.")
        return
    try:
        doujin = Hentai(code)
    except BaseException as n_e:
        if "404" in str(n_e):
            return await event.edit(
                f"No doujin found for `{code}`. You shouldn't use nhentai:-("
            )

    msg = ""
    imgs = "".join(f"<img src='{url}'/>" for url in doujin.image_urls)
    imgs = f"&#8205; {imgs}"
    title = doujin.title()
    graph_link = await post_to_telegraph(title, imgs)
    msg += f"[{title}]({graph_link})"
    msg += f"\n**Source :**\n[{code}]({doujin.url})"
    if doujin.parody:
        msg += "\n**Parodies :**"
        parodies = [
            "#" + parody.name.replace(" ", "_").replace("-", "_")
            for parody in doujin.parody
        ]

        msg += "\n" + " ".join(natsorted(parodies))
    if doujin.character:
        msg += "\n**Characters :**"
        charas = [
            "#" + chara.name.replace(" ", "_").replace("-", "_")
            for chara in doujin.character
        ]

        msg += "\n" + " ".join(natsorted(charas))
    if doujin.tag:
        msg += "\n**Tags :**"
        tags = [
            "#" + tag.name.replace(" ", "_").replace("-", "_") for tag in doujin.tag
        ]

        msg += "\n" + " ".join(natsorted(tags))
    if doujin.artist:
        msg += "\n**Artists :**"
        artists = [
            "#" + artist.name.replace(" ", "_").replace("-", "_")
            for artist in doujin.artist
        ]

        msg += "\n" + " ".join(natsorted(artists))
    if doujin.language:
        msg += "\n**Languages :**"
        languages = [
            "#" + language.name.replace(" ", "_").replace("-", "_")
            for language in doujin.language
        ]

        msg += "\n" + " ".join(natsorted(languages))
    if doujin.category:
        msg += "\n**Categories :**"
        categories = [
            "#" + category.name.replace(" ", "_").replace("-", "_")
            for category in doujin.category
        ]

        msg += "\n" + " ".join(natsorted(categories))
    msg += f"\n**Pages :**\n{doujin.num_pages}"
    #msg += f"\n[😋 Read 😋](buttonurl://{graph_link})"
    #button = InlineKeyboardButton(text="😋 Read 😋", url=graph_link)
    #await event.send_message(chat_id, msg, button)
    await event.reply(msg)

