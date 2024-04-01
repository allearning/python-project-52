from django.contrib.auth.models import User
from django.test import Client, TestCase


class TestCRUD(TestCase):
    fixtures = ['mydump.json']
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.username = 'New_guy'
        self.password = 'H8d9sxy@SL3g8uX'
        self.other_user = 'Pali'
    
    def test_delete_notlogged(self):
        user = User.objects.filter(username=self.username).first()
        self.assertIsNotNone(user)
        response = self.client.post(f'/users/{user.pk}/delete/', follow=True)
        self.assertIsNotNone(User.objects.filter(username=self.username).first())
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, '<div class="alert alert-danger alert-dismissible fade show" role="alert">')
        
    def test_delete_logged(self):
        user = User.objects.filter(username=self.username).first()
        self.assertIsNotNone(user)
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(f'/users/{user.pk}/delete/', follow=True)
        self.assertIsNone(User.objects.filter(username=self.username).first())
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, '<div class="alert alert-success alert-dismissible fade show" role="alert">')

    def test_delete_other_user(self):
        user = User.objects.filter(username=self.username).first()
        other_user = User.objects.filter(username=self.other_user).first()
        self.assertIsNotNone(user)
        self.assertIsNotNone(other_user)
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(f'/users/{other_user.pk}/delete/', follow=True)
        self.assertIsNotNone(User.objects.filter(username=self.other_user).first())
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, '<div class="alert alert-danger alert-dismissible fade show" role="alert">')

    def test_update_notlogged(self):
        user = User.objects.filter(username=self.username).first()
        self.assertIsNotNone(user)
        new_user = {}
        for field in ['username', 'first_name', 'last_name']:
            new_user[field] = user.__dict__[field]
        new_user['last_name'] = 'another'
        new_user['password1'] = user.__dict__['password']
        new_user['password2'] = user.__dict__['password']
        response = self.client.post(f'/users/{user.pk}/update/', new_user, follow=True)
        self.assertIsNotNone(User.objects.filter(username=self.username).first())
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, '<div class="alert alert-danger alert-dismissible fade show" role="alert">')
        
    def test_update_logged(self):
        user = User.objects.filter(username=self.username).first()
        self.assertIsNotNone(user)
        new_user = {}
        for field in ['username', 'first_name', 'last_name']:
            new_user[field] = user.__dict__[field]
        new_user['last_name'] = 'another'
        new_user['password1'] = user.__dict__['password']
        new_user['password2'] = user.__dict__['password']
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(f'/users/{user.pk}/update/', new_user, follow=True)
        self.assertEqual(User.objects.filter(username=self.username).first().last_name, new_user['last_name'])
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, '<div class="alert alert-success alert-dismissible fade show" role="alert">')

    def test_update_other_user_logged(self):
        user = User.objects.filter(username=self.username).first()
        other_user = User.objects.filter(username=self.other_user).first()
        self.assertIsNotNone(user)
        self.assertIsNotNone(other_user)
        new_user = {}
        for field in ['username', 'first_name', 'last_name']:
            new_user[field] = other_user.__dict__[field]
        new_user['last_name'] = 'another'
        new_user['password1'] = other_user.__dict__['password']
        new_user['password2'] = other_user.__dict__['password']
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(f'/users/{other_user.pk}/update/', new_user, follow=True)
        self.assertNotEqual(User.objects.filter(username=self.other_user).first().last_name, new_user['last_name'])
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, '<div class="alert alert-danger alert-dismissible fade show" role="alert">')

    def test_create_user(self):
        new_username = 'new_user_from_test'
        self.assertIsNone(User.objects.filter(username=new_username).first())
        new_user = {
            'username': new_username,
            'first_name': 'ALexander',
            'last_name': 'Bantikov',
            'password1': 'loP04H.Kdskk',
            'password2': 'loP04H.Kdskk'
        }
        response = self.client.post(f'/users/create/', new_user, follow=True)
        self.assertIsNotNone(User.objects.filter(username=new_username).first())
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, '<div class="alert alert-success alert-dismissible fade show" role="alert">')