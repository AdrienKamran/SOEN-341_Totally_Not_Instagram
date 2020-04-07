from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
# from TNI_Project.timeline import views
from django.contrib.auth import authenticate
# Create your tests here.


class UnitTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('TestUser', 'Tester@test.com', 'TestPassword')
        user.save()

    def test_login_authentication_true(self):
        user = authenticate(request=None, username='TestUser', password='TestPassword')
        if user is not None:
            assert True
        else:
            assert False

    def test_login_authentication_false(self):
        user = authenticate(request=None, username='DOES', password='NOTWORK')
        if user is None:
            assert True
        else:
            assert False
