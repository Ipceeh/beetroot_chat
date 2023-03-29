from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .forms import NewMessageForm, AboutYouForm, MessageForm
from .models import Message


@method_decorator(login_required, name='get')
class Index(View):
    def get(self, request):
        return render(request, template_name='index.html')


# class MessagesView(View):
#     def get(self, request):
#         messages = Message.objects.order_by('date_created').all()
#         return render(
#             request=request,
#             template_name='messages.html',
#             context={
#                 'messages': messages,
#                 'form': MessageForm(),
#                 'user': request.user
#             }
#         )
#
#     def post(self, request):
#         user = request.user
#         form = MessageForm(request.POST)
#
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.author = user
#             message.save()
#         else:
#             print('non valid')
#         return self.get(request)

class MessagesView(ListView, CreateView):
    model = Message
    allow_empty = True
    queryset = Message.objects.all()
    paginate_by = 5
    paginate_orphans = 3
    context_object_name = 'messages'
    page_kwarg = "page"
    ordering = ['-date_created']
    template_name = 'chat/messages.html'

    object = Message()
    form_class = NewMessageForm
    success_url = reverse_lazy('messages')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        user = self.request.user
        message = form.save(commit=False)
        message.author = user
        self.object = message.save()
        return super().form_valid(form)

    @method_decorator(permission_required('chat.delete_message', raise_exception=True))
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    # def get_queryset(self):
    #     room = self.request.GET.get('room')
    #     queryset = self.model.objects
    #     queryset = queryset.filter(room=room)
    #     ordering = self.get_ordering()
    #     if ordering:
    #         if isinstance(ordering, str):
    #             ordering = (ordering,)
    #         queryset = queryset.order_by(*ordering)
    #     return queryset


class MessageView(UpdateView):
    model = Message
    # object = Message()
    form_class = MessageForm
    success_url = reverse_lazy('messages')
    template_name = 'chat/message.html'

    def get_object(self, queryset=None):
        message_id = self.kwargs.get('id')
        object = self.model.objects.get(pk=message_id)
        return object

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.object})
        return kwargs

    def get_initial(self):
        initial = {
            'text': self.object.text
        }
        return initial


class AboutYouView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='chat/about_you.html',
            context={
                'form': AboutYouForm(),
                'user': request.user
            }
        )

    def post(self, request):
        user = request.user
        form = AboutYouForm(request.POST)

        print(form)
        return self.get(request)
