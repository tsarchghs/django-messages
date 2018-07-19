from django.shortcuts import render,redirect,reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

class CreateMessage(CreateView):
	model = Message
	fields  = ["content"]
	template_name = "create_message.html"
	def form_valid(self,form):
		conversation_id = self.kwargs["conversation_pk"]
		form_valid_redirect = "/message/create_message/{}".format(conversation_id)
		form.instance.conversation = Conversation.objects.get(pk=conversation_id)
		form.instance.from_user = self.request.user
		form.save()
		return HttpResponseRedirect(reverse("CreateMessage",args=(conversation_id,)))