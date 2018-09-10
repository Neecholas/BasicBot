from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Basic Bot')
#creates an instance of the chatbot with 'basic bot' as it's name
bot.set_trainer(ListTrainer)
for files in os.listdir('home/nick/.local/lib/python3.5/site-packages/chatterbot_corpus')
