from django.test import Client, TestCase
from django.contrib.auth.models import User

class TestPaths(TestCase):

    USER = 'test'
    PASSWORD = 'testpass'
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        user = User.objects.create_user(TestPaths.USER, "mail@server.com", TestPaths.PASSWORD)
        user.save()

    def test_root(self):
        paths = [
            '/'
            '/users/',
            '/users/create/',
            '/users/<int:pk>/update/',
            '/users/<int:pk>/delete/',
            '/login/',
            '/logout/',
        ]
        
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_logged_out(self):
        response = self.client.get('/')
        self.assertContains(response, '<a class="nav-link" href="/login/">')
        self.assertContains(response, '<a class="nav-link" href="/users/create/">')
        self.assertNotContains(response, '<a class="nav-link" href="/statuses/">')
        self.assertNotContains(response, '<a class="nav-link" href="/labels/">')
        self.assertNotContains(response, '<a class="nav-link" href="/tasks/">')
        self.assertNotContains(response, '<form action="/logout/" method="post">')

    def test_logged_in(self):
        response = self.client.post('/login/', {"username": TestPaths.USER, "password": TestPaths.PASSWORD}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertNotContains(response, '<a class="nav-link" href="/login/">')
        self.assertNotContains(response, '<a class="nav-link" href="/users/create/">')
        self.assertContains(response, '<a class="nav-link" href="/statuses/">')
        self.assertContains(response, '<a class="nav-link" href="/labels/">')
        self.assertContains(response, '<a class="nav-link" href="/tasks/">')
        self.assertContains(response, '<form action="/logout/" method="post">')