from TNI_Project.timeline import views
from django.contrib.auth import authenticate


def login_test():
    user = authenticate(username='Shah', password='123')
    if user is not None:
        assert True
    else:
        assert False
