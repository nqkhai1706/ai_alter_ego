from django.http import HttpResponse

from ai_chat.lib import chat
from ai_chat.lib import seq2seq_model_utils as util


vocab, rev_vocab, model, sess = chat.init_chatbot()


def index(request):        
        #print request.GET["id"]
        #request.POST["id"]
        sentence = request.GET["sentence"].encode('utf-8')
        predicted_sentence = util.get_predicted_sentence(sentence, vocab, rev_vocab, model, sess)
        return HttpResponse("AI Alter Ego: {0}".format(predicted_sentence))
