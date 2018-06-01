from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


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
        return self.meetup_name, self.meetup_category, self.meetup_date


class Group(models.Model):
    group_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name
