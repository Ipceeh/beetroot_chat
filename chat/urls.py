from django.urls import path
from .views import index, list_messages, one_message


urlpatterns = [
    path('', index),
    path('messages/<str:id>', one_message),
    path('messages/', list_messages),

]
