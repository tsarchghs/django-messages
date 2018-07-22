from django import template
from django.template import RequestContext
from collections import OrderedDict
from ..models import Conversation,Message

register = template.Library()

@register.filter(name='getInbox')
def getInbox(current_user):
	conv_lastMessage = OrderedDict()
	current_user_conv = Conversation.objects.filter(participants__in=[current_user])
	for conversation in current_user_conv:
		last_message = Message.objects.filter(conversation=conversation).order_by("-id")[0]
		conv_lastMessage[conversation] = last_message
	return conv_lastMessage.items()
