from django.urls import path
from .views import index, messages, one_message, MessagesView


urlpatterns = [
    path('', index),
    path('messages/<str:id>', one_message),
    # path('messages/', messages),
    path('messages/', MessagesView.as_view()),

]
