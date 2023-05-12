import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Create the bot and set up the dispatcher
bot = Bot(token=TOKEN)
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

# Handler to send private messages
def send_private_message(bot, user_id, message):
    bot.send_message(chat_id=user_id, text=message)

# Command handler for sending private messages
def private_message_handler(update, context):
    # Extract the command arguments
    args = context.args

    # Check if the command has the correct format
    if len(args) < 2:
        update.message.reply_text('Usage: /sendprivate <user_id> <message>')
        return

    try:
        # Parse the user_id from the command arguments
        user_id = int(args[0])

        # Extract the message from the command arguments
        message = ' '.join(args[1:])

        # Send the private message
        send_private_message(context.bot, user_id, message)

        update.message.reply_text('Private message sent successfully!')
    except ValueError:
        update.message.reply_text('Invalid user ID. Please provide a valid user ID.')

# Command handler to get participant IDs
def get_participant_ids(update, context):
    # Check if the command has the correct format
    if len(context.args) < 1:
        update.message.reply_text('Usage: /getparticipants <group_id>')
        return

    try:
        # Parse the group_id from the command arguments
        group_id = int(context.args[0])

        # Fetch participant IDs of the group
        participant_ids = fetch_participant_ids(group_id)

        if participant_ids:
            update.message.reply_text('Participant IDs: ' + ', '.join(str(id) for id in participant_ids))
        else:
            update.message.reply_text('No participants found in the group.')
    except ValueError:
        update.message.reply_text('Invalid group ID. Please provide a valid group ID.')

# Function to fetch participant IDs
def fetch_participant_ids(group_id):
    participant_ids = []

    try:
        # Fetch participants in batches of 200
        members = bot.get_chat_members(chat_id=group_id, limit=200)

        # Extract user IDs from the participants
        participant_ids = [member.user.id for member in members]
    except Exception as e:
        logger.error(f'Error fetching participant IDs: {str(e)}')

    return participant_ids

# Error handler
def error_handler(update, context):
    logger.error(context.error)
    update.message.reply_text('An error occurred.')

# Set up command handlers
private_message_handler = CommandHandler('sendprivate', private_message_handler)
get_participant_handler = CommandHandler('getparticipants', get_participant_ids)
dispatcher.add_handler(private_message_handler)
dispatcher.add_handler(get_participant_handler)

# Set up error handler
dispatcher.add_error_handler(error_handler)

if __name__ == '__main__':
    # Start the bot
    updater.start_polling()
