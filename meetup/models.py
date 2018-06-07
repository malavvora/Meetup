import datetime
from django.db import models
from django.forms import ModelForm


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Meetup(models.Model):
    meetup_name = models.CharField(max_length=200)
    meetup_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    meetup_date = models.DateTimeField('date of meetup')

    class Meta:
        ordering = ['-meetup_date']

    def __str__(self):
        return self.meetup_name


class Group(models.Model):
    group_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class CreateMeetupForm(ModelForm):
    class Meta:
        model = Meetup
        fields = '__all__'

