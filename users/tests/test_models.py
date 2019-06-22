from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'
    password = 'passw0rd!'

    def test_user_model(self):
        get_user_model().objects.create_user(
            self.username, self.email, self.password)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.first().username,
            self.username
        )
        self.assertEqual(
            get_user_model().objects.first().email,
            self.email
        )
        self.assertTrue(
            get_user_model().objects.first().check_password(self.password)
        )
