from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
# from .forms import CustomUserCreationForm

# Create your tests here.

class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'
    password = 'passw0rd!'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    # def test_user_model(self):
    #     get_user_model().objects.create_user(
    #         self.username, self.email, self.password)
    #     self.assertEqual(get_user_model().objects.all().count(), 1)
    #     self.assertEqual(get_user_model().objects.first().username, self.username)
    #     self.assertEqual(get_user_model().objects.first().email, self.email)
    #     self.assertTrue(get_user_model().objects.first().check_password(self.password))

    # def test_valid_form(self):
    #     data = {'username': self.username, 'email': self.email, 'password1': self.password, 'password2': self.password,}
    #     form = CustomUserCreationForm(data=data)
    #     self.assertTrue(form.is_valid())

    # def test_invalid_form(self):
    #     data = {'username': "", 'email': "", 'password1': "", 'password2': "",}
    #     form = CustomUserCreationForm(data=data)
    #     self.assertFalse(form.is_valid())

    def test_new_user_sign_up(self):
        data = {'username': self.username, 'email': self.email, 'password1': self.password, 'password2': self.password,}
        response = self.client.post('/users/signup/', data=data, follow=True)
        self.assertEqual(get_user_model().objects.first().username, self.username)
        self.assertIn(('/users/login/', 302), response.redirect_chain)

        