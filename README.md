# Telegram Bot

This Telegram bot allows you to send private messages to individual participants in a Telegram group and fetch the participant IDs of a group.

## Features

- Send private messages to users using the `/sendprivate` command.
- Fetch participant IDs of a group using the `/getparticipants` command.

## Usage

1. Create a new bot with the help of [BotFather](https://core.telegram.org/bots#botfather) and obtain the bot token.

2. Install the required Python packages:
   ```shell
   pip install python-telegram-bot
   
3. Replace 'YOUR_BOT_TOKEN' in the bot_script.py file with your actual bot token.

4. Run the bot script: 
   ```shell 
   python bot_script.py
   
5. Open the Telegram app and search for your bot by its username.
6. Start a chat with your bot.

## Sending Private Messages
To send a private message to a user:

   `/sendprivate <user_id> <message>`
   - <user_id>: The ID of the user you want to send the message to.
   - <"message">: The content of the message you want to send.
    
   - Example: `/sendprivate 123456789 Hello there!`

## Fetching Participant IDs
To fetch the participant IDs of a group:

  `/getparticipants <group_id>`
  - <group_id>: The ID of the group you want to fetch participant IDs from.
  
  - Example: `/getparticipants -123456789`

## Deployment
To deploy the bot, you have several options:

- **Local Machine**: Run the bot script on your local machine.
- **Cloud Hosting Platforms**: Deploy the bot on platforms like Heroku, AWS, Google Cloud Platform, or Azure.
- **Server or VPS**: Deploy the bot on a dedicated server or virtual private server (VPS).

Ensure that the bot script is running continuously to receive and respond to messages.

## License
This project is licensed under the MIT License.
