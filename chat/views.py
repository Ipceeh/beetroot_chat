from django.http import HttpResponse
from .models import Message, get_user_model


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def one_message(request, id):
    message = Message.objects.get(id=id)
    response = f"<i>{message.author.username}</i> : {message.text}<br>"
    return HttpResponse(response)

def list_messages(request):
    if request.method == 'POST':
        return add_message(request)
    elif request.method == 'GET':
        user_to_show = get_user_model().objects.filter(username='admin').get()
        messages = Message.objects.filter(author_id=user_to_show.id).order_by('date_created').all()
        response = ''
        for message in messages:
            response += f"<i>{message.author.username}</i> : {message.text}<br>"

        return HttpResponse(response)

def add_message(request):
    user = request.user
    text = request.POST.get('text', '')
    message = Message.objects.create(
        author=user,
        text=text
    )
    message.save()
    return HttpResponse(f"Message {message.id} created")


