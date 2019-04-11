from django.test import TestCase
from workshop.subscriptions.forms import SubscriptionForm

# Create your tests here.

class SubscriptonTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/subscriptions/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html_form(self):
        #verifica estrutura do formulario html (tags)
        tags = (('form', 10),
                ('<input', 6),
                ('type="text', 11),
                ('type="email', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrt_token(self):
        #verifica so o HTML form possui o csrf_token
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        #verifica se existe uma variavel de contexto para o form
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)