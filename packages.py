from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Basic Bot')
#creates an instance of the chatbot with 'basic bot' as it's name
bot.set_trainer(ListTrainer)
for files in os.listdir('/home/nick/.local/lib/python3.5/site-packages/chatterbot_corpus/data/english/'):
#gets the english version of the corpus and iterates through each file and trains the bot with each piece of data
  data = open('/home/nick/.local/lib/python3.5/site-packages/chatterbot_corpus/data/english/' + files, 'r').readlines()
  #turns each file into text that can be read by a machine
  bot.train(data)
  #feeds the readable data into the bot to train it

while  True:
  message = input('You:')
  #gets input from the user
  if message.strip().lower() != 'bye':
  #checks that the user did not say bye
    reply = bot.get_response(message)
    #gets the reply from the bot and prints it
    print('ChatBot: ', reply)
  if message.strip().lower() == 'bye':
    print('ChatBot: Bye')
    break
