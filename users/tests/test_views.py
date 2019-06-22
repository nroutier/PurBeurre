from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignupViewTests(TestCase):

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

    def test_new_user_sign_up(self):
        data = {'username': self.username, 'email': self.email, 'password1': self.password, 'password2': self.password,}
        response = self.client.post('/users/signup/', data=data, follow=True)
        self.assertEqual(get_user_model().objects.first().username, self.username)
        self.assertIn(('/users/login/', 302), response.redirect_chain)


class LoginViewTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'
    password = 'passw0rd!'

    def test_login_page_status_code(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_successfull_login(self):
        get_user_model().objects.create_user(
            self.username, self.email, self.password)
        data = {'username': self.username, 'password': self.password}
        response = self.client.post('/users/login/', data=data, follow=True)
        self.assertIn(('/users/account/', 302), response.redirect_chain)
        self.assertIn('_auth_user_id', self.client.session)

    def test_failed_login(self):
        get_user_model().objects.create_user(
            self.username, self.email, self.password)
        data = {'username': self.username, 'password': ""}
        self.client.post('/users/login/', data=data, follow=True)
        self.assertTrue('_auth_user_id' not in self.client.session)


class AccountViewTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'
    password = 'passw0rd!'

    def setUp(self):
        get_user_model().objects.create_user(
            self.username, self.email, self.password)
        self.client.login(username=self.username, password=self.password)

    def test_account_page_status_code(self):
        response = self.client.get('/users/account/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')