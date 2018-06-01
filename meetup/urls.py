from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'meetup'
urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    # url(r'^login/$', views.LoginPage, name='login'),
    url(r'^register/$', views.RegisterPage.as_view(), name='register'),
    # url(r'^category/$', views.CategoryPageView.as_view(), name='category'),
    url(r'^profile/$', views.Profile.as_view(), name='profile'),
    url(r'^create_meetup/$', views.CreateMeetup.as_view(), name='create_meetup'),
]
