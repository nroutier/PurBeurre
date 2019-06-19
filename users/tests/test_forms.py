
from django.test import TestCase
from ..forms import CustomUserCreationForm


class SignupUsercreationFormTests(TestCase):

    
    username = 'newuser'
    email = 'newuser@email.com'
    password = 'passw0rd!'

    def test_valid_form(self):
        data = {'username': self.username, 'email': self.email, 'password1': self.password, 'password2': self.password,}
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'username': "", 'email': "", 'password1': "", 'password2': "",}
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())