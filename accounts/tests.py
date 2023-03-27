from django.test import TestCase
from .models import CustomUser


class AccountsTestCase(TestCase):

    def setUp(self):
        self.email = 'helloworld@user.zt'
        self.user = CustomUser.objects.create_user(email=self.email)

    def test_user_creation(self):
        assert self.user.email == self.email
