from django.test import Client, TestCase
from django.contrib.auth.models import User


class TestCRUD(TestCase):
    fixtures = ['mydump.json']
    
    def test_delete(self):
        user = User.objects.filter(username='caller').first()
        self.assertIsNotNone(user)
        response = self.client.post(f'/users/{user.pk}/delete/', follow=True)
        self.assertIsNone(User.objects.filter(username='caller').first())
