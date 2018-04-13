import sys
import chatterbot

sborraBot = chatterbot.ChatBot(
    "Sborra bot",
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter'
)

print(sborraBot.get_response(sys.argv[1]))
