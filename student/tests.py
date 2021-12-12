from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
# TDD

User = get_user_model()

class UserTestCast(TestCase):

    def setUp(self): # Python's builtin unittest
        user_a = User(username='ashish', email='ashish@gmail.com')
        user_a_pw = 'password1234'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
    
    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1) # ==
        self.assertNotEqual(user_count, 0) # !=

    def test_user_password(self):
        user_a = User.objects.get(username="ashish")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )

# Create your tests here.
