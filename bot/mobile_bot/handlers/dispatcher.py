
import telegram
from bot.settings import TELEGRAM_TOKEN

from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    InlineQueryHandler, CallbackQueryHandler,
    ChosenInlineResultHandler, PollAnswerHandler,
)

from mobile_bot.handlers import commands
# from tgbot.handlers.commands import broadcast_command_with_message
# from tgbot.handlers import handlers as hnd
# from tgbot.handlers import manage_data as md
# from tgbot.handlers.static_text import broadcast_command

def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """

    dp.add_handler(CommandHandler("start", commands.command_start))

    # admin commands
    # dp.add_handler(CommandHandler("admin", admin.admin))
    # dp.add_handler(CommandHandler("stats", admin.stats))
    #
    # dp.add_handler(MessageHandler(
    #     Filters.animation, files.show_file_id,
    # ))

    # base buttons
    # dp.add_handler(CallbackQueryHandler(hnd.send_more, pattern=f'^{md.SEND_MORE}'))
    # dp.add_handler(CallbackQueryHandler(hnd.add_to_fav, pattern=f'^{md.ADD_TO_FAV}'))
    # dp.add_handler(CallbackQueryHandler(hnd.view_fav, pattern=f'^{md.VIEW_FAV}'))
    # dp.add_handler(CallbackQueryHandler(hnd.show_authors, pattern=f'^{md.AUTHOR_BTN}'))
    # dp.add_handler(CallbackQueryHandler(hnd.show_author_poems, pattern=f'^{md.POEMS_BY_AUTHOR}'))
    # dp.add_handler(CallbackQueryHandler(hnd.show_poem_by_id, pattern=f'^{md.POEM_BY_NAME}'))
    #
    # dp.add_handler(CallbackQueryHandler(hnd.back_to_main_menu_handler, pattern=f'^{md.BUTTON_BACK_IN_PLACE}'))
    #
    # # location
    # dp.add_handler(CommandHandler("ask_location", location.ask_for_location))
    # dp.add_handler(MessageHandler(Filters.location, location.location_handler))
    #
    # dp.add_handler(CallbackQueryHandler(hnd.secret_level, pattern=f"^{md.SECRET_LEVEL_BUTTON}"))
    #
    # dp.add_handler(MessageHandler(Filters.regex(rf'^{broadcast_command} .*'), broadcast_command_with_message))
    # dp.add_handler(CallbackQueryHandler(hnd.broadcast_decision_handler, pattern=f"^{md.CONFIRM_DECLINE_BROADCAST}"))

    return dp


def run_pooling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    updater.start_polling(timeout=123)
    updater.idle()
