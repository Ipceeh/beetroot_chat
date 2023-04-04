from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.urls import reverse_lazy, reverse
from rest_framework import routers

from .forms import AuthenticationFormCustom
from .views import Index, MessagesView, AboutYouView, MessageView, RegisterView, MessagesViewApi, MessageViewApi

# router = routers.DefaultRouter()
# router.register(r'messages', MessagesViewApi)

urlpatterns = [
    path('', Index.as_view()),
    path('messages/<str:id>/', MessageView.as_view()),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('about_you/', AboutYouView.as_view()),
    path(
        'accounts/login/',
        LoginView.as_view(
            authentication_form=AuthenticationFormCustom
        ),
        name='login'
    ),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls) )
    path('api/messages/', MessagesViewApi.as_view()),
    path('api/messages/<str:id>/', MessageViewApi.as_view())
]
