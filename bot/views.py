from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create your views here.

bot = ChatBot('chatbot', read_only=False, 
              logic_adapters=[
                  {'import_path':'chatterbot.logic.BestMatch',
#                   'default_response': 'Sorry, I dont know what it means',
#                   'maximum_similarity_threshold': 0.90,
                   }
                  ])


chatter = ChatterBotCorpusTrainer(bot)
chatter.train('chatterbot.corpus.english')

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)


def index(request):
    return render(request, 'bot/index.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')    
    chatResp = str(bot.get_response(userMessage))
    
    return HttpResponse(chatResp)
