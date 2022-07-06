import telegram
from mobile_bot.handlers.utils import parse_user_data_from_update
from mobile_bot.handlers.utils import handler_logging
import logging

logger = logging.getLogger('default')
logger.info("Command handlers check!")


@handler_logging()
def command_start(update, context):
    user_id = parse_user_data_from_update(update)['user_id']
    logger.debug("")
    text = f'Здарова\n\n{user_id}'
    context.bot.send_message(
        chat_id=user_id,
        text=text
        # reply_markup=make_keyboard_for_start_command(poem_id),
        # parse_mode=telegram.ParseMode.MARKDOWN
    )
