# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Create a new instance of a ChatBot
bot = ChatBot(
    "bot",
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter'
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        inputSentence = input('Enter your input:')
        botResp = bot.get_response(inputSentence.strip())
        print(botResp)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
