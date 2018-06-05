# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from meetup.forms import SignUpForm
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Category, Meetup

# def adduser(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(**form.cleaned_data)
#             login(new_user)
#             # redirect, or however you want to get to the main view
#             return HttpResponseRedirect('main.html')
#     else:
#         form = UserForm()
#
#     return render(request, 'adduser.html', {'form': form})


class IndexPageView(TemplateView):
    template_name = 'index.html'
    cat = Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        return context


class RegisterPage(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, username=username,
                                password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


class MeetupView(TemplateView):

    template_name = 'meetup.html'
    meetup_objects = Meetup.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MeetupView, self).get_context_data(**kwargs)
        context['meetup_list'] = self.meetup_objects
        return context


class CreateMeetup(TemplateView):
    template_name = "create_meetup.html"

    def post(self, request, *args, **kwargs):
        if request.POST.get("meetup_name"):
            return HttpResponse("Successfully created"
                                + " " + request.POST.get("meetup_name"))
