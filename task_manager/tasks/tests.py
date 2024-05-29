from random import choice
from django.contrib.auth.models import User
from django.test import Client, TestCase

from task_manager.tasks.models import Task
from task_manager.statuses.models import Status

class TestCRUD(TestCase):
    fixtures = ['mydump.json']
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.username = 'caller'
        self.password = 'MMzZ@Yf8gh5eJAn'
        self.executor = choice(User.objects.all())
        self.status = choice(Status.objects.all())

    def test_read_not_logged(self):
        response = self.client.get(f'/tasks/', follow=True)
        self.assertTemplateUsed(response, 'login.html')

    def test_read_not_logged(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(f'/tasks/', follow=True)
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_add_notlogged(self):
        form_data = {
            'name': "test_task_name",
            'description': 'some descr',
            'status': self.status.name,
            'executor': self.executor.username,
            'labels': []
            }
        self.assertIsNone(Task.objects.filter(name=form_data['name']).first())
        response = self.client.post(f'/tasks/create/', form_data, follow=True)
        self.assertIsNone(Task.objects.filter(name=form_data['name']).first())
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, '<div class="alert alert-danger alert-dismissible fade show" role="alert">')

    def test_add_logged(self):
        form_data = {
            'name': "The taskbbb",
            'status': self.status.pk,
            #'labels': []
            }
        self.assertTrue(self.client.login(username=self.username, password=self.password))
        self.assertIsNone(Task.objects.filter(name=form_data['name']).first())
        response = self.client.post(f'/tasks/create/', form_data, follow=True)
        self.assertTemplateUsed(response, 'tasks/index.html')
        self.assertEqual(response.status_code, 200)
        task = Task.objects.filter(name=form_data['name']).first()
        self.assertIsNotNone(task)
        self.assertEqual(task.author.username, self.username)

        self.assertContains(response, '<div class="alert alert-success alert-dismissible fade show" role="alert">')
"""
    def test_update_not_logged(self):
        status = Status.objects.all().first()
        self.assertIsNotNone(status)
        old_name = status.name
        form_data = {'name': 'new_test_stat'}
        response = self.client.post(f'/statuses/{status.pk}/update/', form_data, follow=True)
        status.refresh_from_db()
        self.assertEqual(status.name, old_name)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, '<div class="alert alert-danger alert-dismissible fade show" role="alert">')

    def test_update_logged(self):
        self.client.login(username=self.username, password=self.password)
        status = Status.objects.all().first()
        self.assertIsNotNone(status)
        old_name = status.name
        form_data = {'name': 'new_test_stat'}
        response = self.client.post(f'/statuses/{status.pk}/update/', form_data, follow=True)
        status.refresh_from_db()
        self.assertEqual(status.name, form_data['name'])
        self.assertTemplateUsed(response, 'statuses/index.html')
        self.assertContains(response, '<div class="alert alert-success alert-dismissible fade show" role="alert">')

    def test_delete_not_logged(self):
        status = Status.objects.all().first()
        self.assertIsNotNone(status)
        response = self.client.post(f'/statuses/{status.pk}/delete/', follow=True)
        self.assertIsNotNone(Status.objects.filter(name=status.name).first())
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, '<div class="alert alert-danger alert-dismissible fade show" role="alert">')

    def test_delete_logged(self):
        self.client.login(username=self.username, password=self.password)
        status = Status.objects.all().first()
        self.assertIsNotNone(status)
        response = self.client.post(f'/statuses/{status.pk}/delete/', follow=True)
        self.assertIsNone(Status.objects.filter(name=status.name).first())
        self.assertTemplateUsed(response, 'statuses/index.html')
        self.assertContains(response, '<div class="alert alert-success alert-dismissible fade show" role="alert">')
"""
