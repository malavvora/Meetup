from django.contrib import admin

# Register your models here.
from meetup.models import Category, Meetup
from django.contrib.auth.models import User


def make_staff(modeladmin, something, queryset):
    queryset.update(is_staff=True)
    modeladmin.description = "Make selected user staff user"


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'is_staff')
    actions = [make_staff]


class MeetupAdmin(admin.ModelAdmin):

    list_display = ('meetup_name', 'meetup_category', 'meetup_date')
    list_filter = ['meetup_date']
    search_fields = ['meetup_name']
    is_staff = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Category)
