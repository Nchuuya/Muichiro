def sigma(update: Update, context: CallbackContext):
    update.effective_message.reply_video(random.choice(truth_and_dare_string.SIGMA))
SIGMA_HANDLER = DisableAbleCommandHandler("sigma", sigma, run_async=True)
