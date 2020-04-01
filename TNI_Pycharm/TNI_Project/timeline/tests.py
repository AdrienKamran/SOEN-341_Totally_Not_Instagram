from django.test import TestCase
from TNI_Project.timeline import views
from django.contrib.auth import authenticate
# Create your tests here.


class UnitTestCase(TestCase):
    def test_login_authentication(self):
        user = authenticate(username='Shah', password='123')
        if user is not None:
            assert True
        else:
            assert False
