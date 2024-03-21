from django.test import Client, TestCase
from django.contrib.auth.models import User

class TestPaths(TestCase):

    USER = 'Al7777'
    PASSWORD = '7dhff_ahs'
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        user = User.objects.create_user(TestPaths.USER, "mail@server.com", TestPaths.PASSWORD)
        user.save()

    def test_root(self):
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

    def test_create_user(self):
        new_user = {
            "username": 'new_u_name',
            "password1": '1ewcncJCo8a_8',
            "password2": '1ewcncJCo8a_8',
            "first_name": 'fn',
            'last_name': 'sn'
            }
        response = self.client.post('/users/create/', 
                                    new_user,
                                     follow=True)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIsNotNone(User.objects.filter(username=new_user['username']).first())
        

    def test_update_user(self):
        base_user = {
            "username": 'new_u_name2',
            "password1": '1ewcncJCo8a_8',
            "password2": '1ewcncJCo8a_8',
            "first_name": 'fn',
            'last_name': 'sn'
            }
        
        new_user = base_user.copy()
        new_user['last_name'] = 'new_ln'
        user = User.objects.create_user(base_user['username'],
                                        None, base_user['password1'],
                                        first_name=base_user['first_name'],
                                        last_name=base_user['last_name'])
        user.save()
        response = self.client.post(f'/users/{user.pk}/update/', new_user, follow=True)
        user.refresh_from_db()
        self.assertEqual(user.last_name, new_user['last_name'])
        self.assertTemplateUsed(response, 'users/index.html')