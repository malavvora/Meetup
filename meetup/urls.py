from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = 'meetup'
urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'^register/$', views.RegisterPage.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.MeetupView.as_view(), name='meetup'),
    url(r'^create_meetup/$', views.CreateMeetup.as_view(), name='create_meetup'),
]
