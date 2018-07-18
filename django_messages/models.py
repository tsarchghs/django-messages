from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conversation(models.Model):
	name = models.CharField(max_length=150,blank=True)
	participants = models.ManyToManyField(User)

	def __str__(self):
		if self.name == "":
			return "".join([p.username + "," for p in self.participants.all()])
		else:
			return self.name

class Message(models.Model):
	conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE)
	from_user = models.ForeignKey(User,on_delete=models.CASCADE)
	content = models.TextField()

	def __str__(self):
		return "{} - {}".format(self.conversation,self.from_user)
		
