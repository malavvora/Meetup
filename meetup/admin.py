from django.contrib import admin

# Register your models here.
from meetup.models import Category, Meetup


class MeetupAdmin(admin.ModelAdmin):

    list_display = ('meetup_name', 'meetup_category', 'meetup_date')
    list_filter = ['meetup_date']
    search_fields = ['meetup_name']


admin.site.register(Category)
admin.site.register(Meetup, MeetupAdmin)
