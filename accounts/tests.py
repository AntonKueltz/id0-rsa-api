from django.contrib.auth.models import User
from django.test import TestCase


class PasswordTestCase(TestCase):
    def test_password_is_hashed(self):
        u = User.objects.create_user(username='user', password='pass')
        self.assertNotEqual(u.password, 'pass')
        self.assertIn('bcrypt', u.password)
