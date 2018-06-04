# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Category, Meetup


class IndexPageView(TemplateView):
    template_name = 'index.html'
    cat = Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        return context


class RegisterPage(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class MeetupView(TemplateView):

    template_name = 'meetup.html'
    meetup_objects = Meetup.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MeetupView, self).get_context_data(**kwargs)
        context['meetup_list'] = self.meetup_objects
        return context


class RegisterPage(TemplateView):
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get("name"):
            return HttpResponse("Success" + " " + request.POST.get("username"))


class CreateMeetup(TemplateView):
    template_name = "create_meetup.html"

    def post(self, request, *args, **kwargs):
        if request.POST.get("meetup_name"):
            return HttpResponse("Successfully created"
                                + " " + request.POST.get("meetup_name"))
