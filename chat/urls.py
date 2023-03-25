from django.urls import path
from .views import index, one_message, MessagesView, AboutYouView, MessageView


urlpatterns = [
    path('', index),
    path('messages/<str:id>/', MessageView.as_view()),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('about_you/', AboutYouView.as_view())

]
