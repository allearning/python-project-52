from django.test import Client, TestCase

class TestPaths(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

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