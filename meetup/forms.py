from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from meetup.models import Meetup
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

CATEGORIES = [
    ('Tech', 'Tech'),
    ('Music', 'Music'),
    ('Writing', 'Writing'),
    ('Photography', 'Photography'),
    ('Learning', 'Learning'),
    ('Sports', 'Sports'),
]


class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, max_length=254,
                             help_text='Required. Enter a valid email address.')

    helper = FormHelper()
    helper.form_method= 'POST'
    helper.add_input(Submit('signup', 'Sign up', css_class='btn-primary'))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

        def save(self, commit=True):
            user = super(self, UserCreationForm).save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user


class CreateMeetupForm(forms.ModelForm):

    meetup_date = forms.DateTimeField(input_formats=["%d %b %Y"], required=True,
                                      help_text="MM/DD/YYYY format")
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('create_meetup', 'Create', css_class='btn-primary'))

    class Meta:
        model = Meetup
        fields = ('meetup_name', 'meetup_category', 'meetup_date')
