from django.shortcuts import render,redirect,reverse
from django.views.generic.edit import CreateView,DeleteView
from django.http import HttpResponseRedirect
from django.http import Http404
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

class DeleteMessage(DeleteView):
	model = Message
	success_url = ""
	template_name = "message_confirm_delete.html"
	def get_object(self):
		message = super(DeleteMessage,self).get_object()
		if not message.from_user == self.request.user:
			raise Http404
		return message
	def get_success_url(self):
		if self.success_url:
			return success_url
		else:
			message = self.get_object()
			default_success_url = reverse("CreateMessage",args=(message.conversation.id,))
			return default_success_url
	def delete(self):
		message = self.get_object()
		message.deleted = True
		message.save()
		return HttpResponseRedirect(success_url)