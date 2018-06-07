# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from meetup.forms import SignUpForm, CreateMeetupForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Category, Meetup


class IndexPageView(TemplateView):
    template_name = 'index.html'
    category_list = Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['categories'] = self.category_list
        return context


class RegisterPage(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                raw_password = form.cleaned_data['password1']
                m = User(username=username, email=email,
                         password=raw_password)
                m.save()
                return HttpResponseRedirect('/')

        else:
            form = SignUpForm()

        return render(request, 'register.html', {'form': form})


class MeetupView(TemplateView):

    template_name = 'meetup.html'
    meetups_object = Meetup.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MeetupView, self).get_context_data(**kwargs)
        context['meetup_list'] = self.meetups_object
        return context


class CreateMeetup(CreateView):
    form_class = CreateMeetupForm
    template_name = "create_meetup.html"
    cat = Category.objects.all()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(CreateMeetup, self).get_context_data(**kwargs)
    #     context['category'] = self.cat
    #     return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CreateMeetupForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['meetup_name']
                category = form.cleaned_data['meetup_category']
                date = form.cleaned_data['meetup_date']
                m = Meetup(meetup_name=name, meetup_category=category,
                           meetup_date=date)
                m.save()
                return HttpResponse("Successfully created"
                                    + " " + request.POST.get("meetup_name"))

        else:
            form = CreateMeetupForm()

        return render(request, 'create_meetup.html', {'form': form})
