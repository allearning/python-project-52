from django.test import Client, TestCase
from django.contrib.auth.models import User

class TestPaths(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.USER = 'Al7777'
        self.PASSWORD = '7dhff_ahs'
        user = User.objects.create_user(self.USER, "mail@server.com", self.PASSWORD)
        user.save()

    def test_root(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_logged_out_header(self):
        response = self.client.get('/')
        self.assertContains(response, '<a class="nav-link" href="/login/">')
        self.assertContains(response, '<a class="nav-link" href="/users/create/">')
        self.assertNotContains(response, '<a class="nav-link" href="/statuses/">')
        self.assertNotContains(response, '<a class="nav-link" href="/labels/">')
        self.assertNotContains(response, '<a class="nav-link" href="/tasks/">')
        self.assertNotContains(response, '<form action="/logout/" method="post">')

    def test_logged_in_header(self):
        response = self.client.post('/login/', {"username": self.USER, "password": self.PASSWORD}, follow=True)
        self.assertContains(response, '<div class="alert alert-success alert-dismissible fade show" role="alert">')
        self.assertTrue(response.context.get('user').is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertNotContains(response, '<a class="nav-link" href="/login/">')
        self.assertNotContains(response, '<a class="nav-link" href="/users/create/">')
        self.assertContains(response, '<a class="nav-link" href="/statuses/">')
        self.assertContains(response, '<a class="nav-link" href="/labels/">')
        self.assertContains(response, '<a class="nav-link" href="/tasks/">')
        self.assertContains(response, '<form action="/logout/" method="post">')

    def test_logout_logged(self):
        response = self.client.post('/login/', {"username": self.USER, "password": self.PASSWORD}, follow=True)
        self.assertTrue(response.context.get('user').is_authenticated)
        response = self.client.get('/logout/', follow=True)
        self.assertContains(response, '<div class="alert alert-info alert-dismissible fade show" role="alert">')
        self.assertFalse(response.context.get('user').is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        response = self.client.post('/login/', {"username": self.USER, "password": self.PASSWORD}, follow=True)
        self.assertTrue(response.context.get('user').is_authenticated)
        response = self.client.post('/logout/', follow=True)
        self.assertContains(response, '<div class="alert alert-info alert-dismissible fade show" role="alert">')
        self.assertFalse(response.context.get('user').is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_logout_not_logged(self):
        response = self.client.get('/logout/', follow=True)
        self.assertContains(response, '<div class="alert alert-info alert-dismissible fade show" role="alert">')
        self.assertFalse(response.context.get('user').is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        response = self.client.post('/logout/', follow=True)
        self.assertContains(response, '<div class="alert alert-info alert-dismissible fade show" role="alert">')
        self.assertFalse(response.context.get('user').is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')