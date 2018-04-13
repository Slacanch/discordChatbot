import re
import os
import sys
import chatterbot
import chatterbot_corpus

def makeCorpusList(textFile, limit = 0):
    initiatorPattern = re.compile("\S: (.+)\n")
    continuingPattern = re.compile("- : (.+)\n")
    retList = []
    with open(textFile, encoding= 'utf-8') as chat:
        currentPhrase = ''
        iteration = 0
        for line in chat:
            if "Media omitted" in line:
                continue
            if ":" not in line:
                continue
            im = initiatorPattern.search(line)
            cm = continuingPattern.search(line)
            if im:
                retList.append(currentPhrase)
                if limit and iteration > limit:
                    return retList
                else:
                    iteration += 1
                currentPhrase = im.group(1) + " "
            elif cm:
                currentPhrase += cm.group(1)
        return retList

print("making training set...")
if os.path.isfile(sys.argv[1]):
    trainingList = makeCorpusList(sys.argv[1], 0)
else:
    raise IOError("no such file or directory")

print("setting up bot...")
chatbot = chatterbot.ChatBot(
    'bot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    trainer= "chatterbot.trainers.ListTrainer"
)

# Train based on provided list
print("training...")
chatbot.train(trainingList)
print("done!")

# Get a response to an input statement
#print("bot, can you answer this question?")
#print(chatbot.get_response("bot, can you answer this question?"))


