from django.test import TestCase
from django.urls import reverse
from django.test import Client
# Create your tests here.
from django.contrib.auth.models import User


class Model_Views_Test(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        c = Client()
        logged_in = c.login(username='testuser', password='12345')

    def test_home_view(self):
        self.client.login(username=self.user.username, password='12345')
        resp = self.client.post(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'places_remember/index.html')

    def test_create_view(self):
        self.client.login(username=self.user.username, password='12345')
        resp = self.client.post(reverse('create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'places_remember/create.html')

    def test_about_view(self):
        resp = self.client.post(reverse('about'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'places_remember/about.html')

    def test_login_view(self):
        resp = self.client.post(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'places_remember/login.html')

    def test_register_view(self):
        resp = self.client.post(reverse('register'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'places_remember/register.html')

    def test_logout_view(self):
        self.client.login(username=self.user.username, password='12345')
        resp = self.client.post(reverse('logout'))
        self.assertRedirects(resp, '/login')

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('home'))
        self.assertRedirects(resp, '/login?next=%2F')
