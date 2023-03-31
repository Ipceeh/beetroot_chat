from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.urls import reverse_lazy, reverse

from .forms import AuthenticationFormCustom
from .views import Index, MessagesView, AboutYouView, MessageView, RegisterView

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

]
