def gbam(update, context):
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    message = update.effective_message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gbam_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbam_user.first_name)

    else:
        user1 = curr_user
        user2 = bot.first_name

    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        gbamm = fun.GBAM
        reason = random.choice(fun.GBAM_REASON)
        gbam = gbamm.format(user1=user1, user2=user2, chatid=chat.id, reason=reason)
        context.bot.sendMessage(chat.id, gbam, parse_mode=ParseMode.HTML)
GBAM = "<b>Beginning Of Global Bam For {user2}</b>  \n \nChat Id : <code>{chatid}</code> \nReason : <i>{reason}</i> \nGBammed By {user1}"


GBAM_REASON = (
    "sasta noob",
    "sasta waifu stealer",
    "sasta white-het hekur",
    "sasta white-het codur",
    "sasta white-het vala chintu",
    "sasta hexa hekur",
    "sasta hexa playur",
    "sasta tiktokur💃🏾",
    "sasta membor of team 7",
    "sasta selmon boi",
    "sasta fri-fire player",
    "sasta chhota bhim",
    "sasta chhapri",
    "sasta jony sin",
    "sasta chhapri nibba",
    "sasta nibba",
    "sasti ria chokroborti",
    "sasti nibbi",
    "sasta camper",
)
