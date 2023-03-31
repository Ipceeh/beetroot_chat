from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url

from .models import Message


class NewMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'messages'

        self.helper.add_input(Submit('submit', 'Send'))

    class Meta:
        model = Message
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.TextInput()
        }


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Send'))

    class Meta:
        model = Message
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.TextInput()
        }


class AboutYouForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'about_you'

        # self.helper.add_input(Submit('submit', 'Send'))

        self.helper.layout = Layout(
            Fieldset(
                'Enter information about yourself',
                'your_location',
                'your_interests',
                'your_name',
                'your_age'
            ),
            Submit('submit', 'Send', css_class='button'),
        )

    your_name = forms.CharField(label='Your name', max_length=100, initial='Pavlo')
    your_age = forms.IntegerField(
        label='Your age', min_value=18, max_value=100, step_size=1,
        widget=forms.Select(choices=[(i, i) for i in range(18, 100, 1)]))
    your_interests = forms.CharField(label='Your interests', max_length=100)
    your_location = forms.CharField(label='Your location', max_length=100)


class AuthenticationFormCustom(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = resolve_url('login')

        self.helper.add_input(Submit('submit', 'Login!'))


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = resolve_url('register')

        self.helper.add_input(Submit('submit', 'Login!'))

    class Meta:
        model = get_user_model()
        fields = [get_user_model().USERNAME_FIELD, "password1", "password2"]
