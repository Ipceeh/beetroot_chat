from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets, generics, pagination
from rest_framework import permissions

from .forms import NewMessageForm, AboutYouForm, MessageForm, RegisterForm
from .models import Message
from .serializers import MessageSerializer


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


# class MessageController:
#     def create_message_ui(self):
#         self._create_message_helper1()
#         self._create_message_helper1()
#
#     def create_message_api(self):
#         self._create_message_helper2()
#
#     def _create_message_helper1(self):
#         user = self.request.user
#         message = form.save(commit=False)
#         message.author = user
#         self.object = message.save()
#
#     def _create_message_helper2(self):
#         user = self.request.user
#         message = form.save(commit=False)
#         message.author = user
#         self.object = message.save()


# class MessagesViewApi(viewsets.ModelViewSet):
#     queryset = Message.objects.all().order_by('-date_created')
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]


class CustomPagination(pagination.PageNumberPagination):
    page_size = 5


class MessagesViewApi(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-date_created')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        super().perform_create(serializer)



class MessageViewApi(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]





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

    @method_decorator(permission_required('chat.add_message', raise_exception=True))
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


class RegisterView(UserPassesTestMixin, CreateView):
    object = get_user_model()
    form_class = RegisterForm
    success_url = reverse_lazy('messages')
    template_name = 'registration/registration.html'

    def test_func(self):
        if self.request.user.is_anonymous:
            print(self.request.user)
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect(self.success_url)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        user = form.save(commit=False)
        self.object = user.save()

        my_group = Group.objects.get(name='regular_user')
        my_group.user_set.add(user)

        return super().form_valid(form)

# from django.contrib.auth.models import Group
# my_group = Group.objects.get(name='my_group_name')
# my_group.user_set.add(your_user)