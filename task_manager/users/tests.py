from django.test import TestCase, Client
from django.urls import reverse

from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ['fixture.json']
    user_in_DB = 'alpa'
    user_not_in_DB = 'user_not_in_db'

    def setUp(self):
        pass

    def test_user_create(self):
        """Test Creating User"""
        c = Client()
        u_name = UserTestCase.user_not_in_DB
        c.post('/users/create/',
               {'first_name': '111', 'last_name': '222',
                'username': u_name,
                'password1': 'http://127.0.0.1:8000/users/create/',
                'password2': 'http://127.0.0.1:8000/users/create/',
                }, follow=True)
        user = User.objects.get(username=u_name)
        self.assertEqual(user.username, u_name)

    def test_user_doubles(self):
        c = Client()
        u_name = UserTestCase.user_in_DB
        response = c.post('/users/create/',
                          {'first_name': 'Balan', 'last_name': 'Balala',
                           'username': u_name,
                           'password1': 'http://127.0.0.1:8000/users/create/',
                           'password2': 'http://127.0.0.1:8000/users/create/',
                           }, follow=True)

        text = 'A user with that username already exists.'
        self.assertContains(response, text)

    def test_read_user(self):
        c = Client()
        u_name = UserTestCase.user_in_DB

        user = User.objects.get(username=u_name)
        response = c.get('/users/')
        self.assertIn(user, response.context['users'])

    def test_update_logged_user(self):
        c = Client()
        u_name = UserTestCase.user_in_DB
        password = 'http://127.0.0.1:8000/users/create/'
        c.login(username=u_name, password=password)
        new_name = 'new_name'
        user = User.objects.get(username=u_name)
        pk = user.pk
        url = reverse('update_user', kwargs={'pk': pk})
        c.post(url,
               {'first_name': user.first_name,
                'last_name': user.last_name,
                'username': new_name,
                'password1': 'http://127.0.0.1:8000/users/create/',
                'password2': 'http://127.0.0.1:8000/users/create/',
                }, follow=True)
        user = User.objects.get(pk=pk)
        self.assertEqual(user.username, new_name)

    def test_update_logout_user(self):
        c = Client()
        u_name = UserTestCase.user_in_DB
        new_name = 'new_name'
        user = User.objects.get(username=u_name)
        pk = user.pk
        url = reverse('update_user', kwargs={'pk': pk})
        c.post(url,
               {'first_name': user.first_name,
                'last_name': user.last_name,
                'username': new_name,
                'password1': 'http://127.0.0.1:8000/users/create/',
                'password2': 'http://127.0.0.1:8000/users/create/',
                }, follow=True)
        user = User.objects.get(pk=pk)
        self.assertEqual(user.username, u_name)

    def test_update_another_user(self):
        c = Client()
        u_name = UserTestCase.user_in_DB

        password = 'http://127.0.0.1:8000/users/create/'
        c.login(username=u_name, password=password)
        new_name = 'new_name'
        user = User.objects.get(username=u_name)
        another_pk = user.pk - 1
        another_user = User.objects.get(pk=another_pk)
        url = reverse('update_user', kwargs={'pk': another_pk})
        c.post(url,
               {'first_name': another_user.first_name,
                'last_name': another_user.last_name,
                'username': new_name,
                'password1': 'http://127.0.0.1:8000/users/create/',
                'password2': 'http://127.0.0.1:8000/users/create/',
                }, follow=True)
        u1 = User.objects.get(pk=another_user.pk)
        self.assertEqual(u1.username, another_user.username)

    def test_delete_logged_user(self):
        c = Client()
        u_name = UserTestCase.user_in_DB
        password = 'http://127.0.0.1:8000/users/create/'
        c.login(username=u_name, password=password)
        user = User.objects.get(username=u_name)
        pk = user.pk
        url = reverse('delete_user', kwargs={'pk': pk})
        c.post(url, follow=True)
        self.assertRaises(
            User.DoesNotExist,
            User.objects.get,
            pk=pk
            )

    def test_delete_logout_user(self):
        c = Client()
        u_name = UserTestCase.user_in_DB
        user = User.objects.get(username=u_name)
        pk = user.pk
        url = reverse('delete_user', kwargs={'pk': pk})
        c.post(url, follow=True)
        user = User.objects.get(pk=pk)
        self.assertEqual(user.username, u_name)

    def test_delete_another_user(self):
        c = Client()
        u_name = UserTestCase.user_in_DB
        password = 'http://127.0.0.1:8000/users/create/'
        c.login(username=u_name, password=password)
        user = User.objects.get(username=u_name)
        another_pk = user.pk - 1
        another_user = User.objects.get(pk=another_pk)
        url = reverse('delete_user', kwargs={'pk': another_pk})
        c.post(url, follow=True)
        u1 = User.objects.get(pk=another_user.pk)
        self.assertEqual(u1.username, another_user.username)