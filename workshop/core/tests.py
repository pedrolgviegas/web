from django.test import TestCase

# Create your tests here.

#classe TestCase é a classe mãe de testes
# .client consegue driblar a infraestrutura de rede, para testes
# setUp deve iniciar cada classe de testes
# TDL test drive developer (desenvolvimento dirigido a testes)

class HomeTeste(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/index.html')

    def test_about_link(self):
        self.assertContains(self.response, 'href="/about/"')

    def test_speakers_link(self):
        self.assertContains(self.response, 'href="/speakers/"')

    def test_events_link(self):
        self.assertContains(self.response, 'href="/events/"')

    def test_news_link(self):
        self.assertContains(self.response, 'href="/news/"')

    def test_contacts_link(self):
        self.assertContains(self.response, 'href="/contact/"')

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/subscription/"')

class AboutTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/about/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/about.html')

class SpeakersTeste(TestCase):

    def setUp(self):
        self.response = self.client.get('/speakers/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/speakers.html')

    def test_home_link(self):
        self.assertContains(self.response, 'href="/"')

    def test_about_link(self):
        self.assertContains(self.response, 'href="/about/"')

    def test_events_link(self):
        self.assertContains(self.response, 'href="/events/"')

    def test_news_link(self):
        self.assertContains(self.response, 'href="/news/"')

    def test_contacts_link(self):
        self.assertContains(self.response, 'href="/contact/"')

class EventsTeste(TestCase):

    def setUp(self):
        self.response = self.client.get('/events/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/events.html')

    def test_home_link(self):
        self.assertContains(self.response, 'href="/"')

    def test_about_link(self):
        self.assertContains(self.response, 'href="/about/"')

    def test_speakers_link(self):
        self.assertContains(self.response, 'href="/speakers/"')

    def test_news_link(self):
        self.assertContains(self.response, 'href="/news/"')

    def test_contacts_link(self):
        self.assertContains(self.response, 'href="/contact/"')

class NewsTeste(TestCase):

    def setUp(self):
        self.response = self.client.get('/news/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/news.html')

    def test_home_link(self):
        self.assertContains(self.response, 'href="/"')

    def test_about_link(self):
        self.assertContains(self.response, 'href="/about/"')

    def test_speakers_link(self):
        self.assertContains(self.response, 'href="/speakers/"')

    def test_events_link(self):
        self.assertContains(self.response, 'href="/events/"')

    def test_contacts_link(self):
        self.assertContains(self.response, 'href="/contact/"')

class ContactTeste(TestCase):

    def setUp(self):
        self.response = self.client.get('/contact/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/contact.html')

    def test_home_link(self):
        self.assertContains(self.response, 'href="/"')

    def test_about_link(self):
        self.assertContains(self.response, 'href="/about/"')

    def test_speakers_link(self):
        self.assertContains(self.response, 'href="/speakers/"')

    def test_events_link(self):
        self.assertContains(self.response, 'href="/events/"')

    def test_news_link(self):
        self.assertContains(self.response, 'href="/news/"')