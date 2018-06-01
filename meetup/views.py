# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import User, Category, Meetup, Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect


class IndexPageView(generic.TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        """Return all categories."""
        return Category.objects.all()


class CategoryPageView(generic.ListView):
    template_name = 'category.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        """Return all the groups under that category."""
        return Category.objects.all()


class MeetupPageView(generic.TemplateView):
    model = Meetup
    template_name = 'meetup.html'


class GroupPageView(generic.TemplateView):
    model = Group
    template_name = 'group.html'


# def LoginPage(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     template_name = 'login.html'


class RegisterPage(generic.TemplateView):
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get("name"):
            return HttpResponse("Success" + " " + request.POST.get("username"))


class CreateMeetup(generic.TemplateView):
    template_name = "create_meetup.html"

    def post(self, request, *args, **kwargs):
        if request.POST.get("meetup_name"):
            return HttpResponse("Success" + " " + request.POST.get("meetup_name"))


class Profile(generic.TemplateView):
    template_name = 'profile.html'
