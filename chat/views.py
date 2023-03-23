from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Message, get_user_model
from .forms import MessageForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def one_message(request, id):
    message = Message.objects.get(id=id)
    response = f"<i>{message.author.username}</i> : {message.text}<br>"
    return HttpResponse(response)

def messages(request):
    if request.method == 'POST':
        return add_message(request)
    elif request.method == 'GET':
        return list_messages(request)

def list_messages(request):
    messages = Message.objects.order_by('date_created').all()
    return render(
        request=request,
        template_name='messages.html',
        context={
            'messages': messages,
            'form': MessageForm(),
            'user': request.user
        }
    )

def add_message(request):
    user = request.user
    form = MessageForm(request.POST)

    if form.is_valid():
        message = form.save(commit=False)
        message.author = user
        message.save()
    else:
        print('non valid')
    return list_messages(request)


class MessagesView(View):
    def get(self, request):
        messages = Message.objects.order_by('date_created').all()
        return render(
            request=request,
            template_name='messages.html',
            context={
                'messages': messages,
                'form': MessageForm(),
                'user': request.user
            }
        )

    def post(self, request):
        user = request.user
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.author = user
            message.save()
        else:
            print('non valid')
        return self.get(request)

