from django.test import TestCase, RequestFactory
from django.http import HttpRequest
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.test import Client
import timeline.views as views
from timeline.models import Image, Comment
import datetime
# Create your tests here.


class AuthenticationTests(TestCase):
    # Creating a test user:
    def setUp(self):
        self.test_client = Client()
        self.user = User.objects.create_user('TestUser', 'Tester@test.com', 'TestPassword')
        self.user.save()
        #self.factory = RequestFactory()

    # Authenticating the test user against the database (SHOULD PASS):
    def test_login_authentication_true(self):
        user = authenticate(request=None, username='TestUser', password='TestPassword')
        if user is not None:
            assert True
        else:
            assert False

    # Authenticating a non-existent user against the database (SHOULD FAIL):
    def test_login_authentication_false(self):
        user = authenticate(request=None, username='SHOULD', password='NOTWORK')
        if user is None:
            assert True
        else:
            assert False

    '''
        def test_login_redirect(self):
            test_request = self.factory.post('/login', {'username': 'TestUser', 'password': 'TestPassword'})
            test_request.user = self.user
            test_response = views.signIn(test_request)
            self.assertRedirects(self, test_response, '/home/')
    '''


class RedirectTests(TestCase):

    def setUp(self):
        self.test_client = Client()
        self.user = User.objects.create_user('TestUser', 'Tester@test.com', 'TestPassword')
        self.user.save()
        self.factory = RequestFactory()

    # Testing the URL redirect when a user successfully logs in from the login page:
    def test_login_redirect(self):
        test_response = self.test_client.post('/login/', {'username': 'TestUser', 'password': 'TestPassword'})
        test_response.status_code
        self.assertRedirects(test_response, '/home/')

    # Testing the URL redirect when a logged-in user attempts to log in, again:
    def test_already_logged_in_redirect(self):
        test_request = self.test_client.post('/login/', {'username': 'TestUser', 'password': 'TestPassword'})
        test_request.user = self.user
        test_response = views.signIn(test_request)
        test_response.client = Client()
        test_response.status_code
        self.assertRedirects(test_response, '/home/', target_status_code=302)


class LikeTests(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = User.objects.create_user('TestUser', 'Tester@test.com', 'TestPassword')
        self.user.save()
        self.factory = RequestFactory()
        #self.test_image = Image.objects.create(name='test_image', caption='test_caption', user=self.user, post_date='1990-10-09', likes='0')

    # Testing that clicking the "LIKE" button on a post actually increments that post's "like" attribute in the database:
    def test_like_increment(self):
        test_image = Image.objects.create(name='test_image', caption='test_caption', user=self.user,
                                          post_date='1990-10-09', likes='0')
        test_image.save()
        test_request = self.factory.post('/home/like/', {'name': 'test_image'})
        test_request.user = self.user
        test_request.client = Client()
        views.image_like(test_request)
        test_image.refresh_from_db()
        self.assertEqual(test_image.likes, 1)

    # Testing that clicking the "LIKE" button on a post refreshes the page and updates the information on the browser:
    def test_like_redirect(self):
        test_image = Image.objects.create(name='test_image', caption='test_caption', user=self.user,
                                          post_date='1990-10-09', likes='0')
        test_image.save()
        test_request = self.factory.post('/home/like/', {'name': 'test_image'})
        test_request.user = self.user
        test_response = views.image_like(test_request)
        test_response.client = Client()
        self.assertRedirects(test_response, '/home/', target_status_code=302)


class CommentTests(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = User.objects.create_user('TestUser', 'Tester@test.com', 'TestPassword')
        self.user.save()
        self.factory = RequestFactory()

    # Testing that typing a comment on a test post actually creates a comment for that post in the database:
    def test_comment_creation(self):
        test_image = Image.objects.create(name='test_image_comment_1', caption='test_caption', user=self.user,
                                          post_date='1990-10-09', likes='0')
        test_image.save()
        test_request = self.factory.post('/home/comment/', {'user': self.user, 'msg': 'Test Comment 1',
                                                            'post_date': '1990-10-09', 'img': 'test_image_comment_1'})
        test_request.user = self.user
        views.image_comment(test_request)
        test_image.refresh_from_db
        test_comment_message = 'default'
        for c in Comment.objects.all():
            test_comment_message = c.msg
        self.assertEqual(test_comment_message, 'Test Comment 1')

    # Testing that clicking the "Submit Comment" button on a post refreshes the page and updates the information on the browser:
    def test_comment_redirect(self):
        test_image = Image.objects.create(name='test_image_comment_2', caption='test_caption', user=self.user,
                                          post_date='1990-10-09', likes='0')
        test_image.save()
        test_request = self.factory.post('/home/comment/', {'user': self.user, 'msg': 'Test Comment 2',
                                                            'post_date': '1990-10-09', 'img': 'test_image_comment_2'})
        test_request.user = self.user
        test_response = views.image_comment(test_request)
        test_response.client = Client()
        self.assertRedirects(test_response, '/home/', target_status_code=302)


class PostTests(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = User.objects.create_user('TestUser', 'Tester@test.com', 'TestPassword')
        self.user.save()
        self.factory = RequestFactory()

    # Testing that clicking the "Create Post" button (with a filled form) actually creates a post object in the database:
    def test_post_creation(self):
        self.test_client.login(username='TestUser', password='TestPassword')
        with open("TNILogo.png", mode='rb') as ti:
            test_request = self.factory.post('/home/imageupload/', {'user': self.user, 'name': 'TestImage',
                                                                        'Img': ti, 'caption': 'TestCaption'})
        test_request.user = self.user
        views.image_view(test_request)
        test_post_name = 'default'
        for p in Image.objects.all():
            test_post_name = p.name
        self.assertEqual(test_post_name, 'TestImage')

    def test_post_redirect(self):
        self.test_client.login(username='TestUser', password='TestPassword')
        with open("TNILogo.png", mode='rb') as ti:
            test_request = self.factory.post('/home/imageupload/', {'user': self.user, 'name': 'TestImage',
                                                                        'Img': ti, 'caption': 'TestCaption'})
        test_request.user = self.user
        test_response = views.image_view(test_request)
        test_response.client = Client()
        self.assertRedirects(test_response, '/home/', target_status_code=302)