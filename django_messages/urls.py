from django.urls import path
from . import views

urlpatterns = [
	path("create_message/<conversation_pk>", views.CreateMessage.as_view(),name="CreateMessage"),
]