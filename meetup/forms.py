from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a '
                                                       'valid email '
                                                       'address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

        # def save(self, commit=True):
        #     user = super(self, UserCreationForm).save(commit=False)
        #     user.set_password(self.cleaned_data["password1"])
        #     if commit:
        #         user.save()
        #     return user
        # # user = User.objects.create_user(email='downtownbarista@coffeehouse.com',
        #                                 username='dotown',
        #                                 password='cappuccino', is_staff=True)
