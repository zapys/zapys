from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class Signupform(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'role')
