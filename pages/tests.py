from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home')

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_about_us_page_url_by_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_content(self):
        response = self.client.get(reverse('about_us'))
        self.assertContains(response, 'About us')

    def test_about_us_template_used(self):
        response = self.client.get(reverse('about_us'))
        self.assertTemplateUsed(response, template_name='pages/about_us.html')