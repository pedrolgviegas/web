from django.core import mail
from django.test import TestCase
from workshop.subscriptions.forms import SubscriptionForm


class SubscriptionTest(TestCase):


    def setUp(self):
        self.response = self.client.get('/subscriptions/')


    def test_get(self):
        self.assertEqual(200, self.response.status_code)


    def test_template_used(self):
        self.assertTemplateUsed(self.response,
                                'subscriptions/subscription_form.html')

    def test_html_form(self):
        """
        Verifica a estrutura do formulário HTML (tags)

        """
        tags = (('form',10),
                ('<input', 6),
                ('type="text', 11),
                ('type="email',1),
                ('type="submit"',1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)


    def test_csrf_token(self):
        """
        Verifica se o HTML form possui o csrf_token
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """
        Verifica se existe um variável de contexto para o form

        """
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


    def test_form_has_field(self):

        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscriptionTestPostValid(TestCase):


    def setUp(self):

        self.data = dict(name='Paulo', cpf='99999999999',
                         email='pcego36@gmail.com', phone='32122980')
        self.response = self.client.post('/subscriptions/',self.data)


    def test_post(self):
        """
        Para POST válido redirecionar para /subscriptions/
        """
        self.assertEqual(302, self.response.status_code)


    def test_send_email(self):
        """
        Verifica se um email foi enviado
        """
        self.assertEqual(1, len(mail.outbox))


# Inicio testes POST
class SubscriptionTestPostInvalid(TestCase):


    def setUp(self):
        self.response = self.client.post('/subscriptions/', {})


    def test_post(self):
        """
        Se POST for inválido não redireciona
        """
        self.assertEqual(200, self.response.status_code)


    def test_template(self):
        """
        Verifica template
        """
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')


    def test_has_form(self):
        """
        Verifica se existe context form
        """
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


    def test_has_form_errors(self):
        """
        Verifica se o dicionário form possui erros
        """
        form = self.response.context['form']
        self.assertTrue(form.errors)


class SubscribeTestMailContent(TestCase):


    def setUp(self):

        self.data = dict(name='Paulo', cpf='99999999999',
                         email='pcego36@gmail.com', phone='32122980')
        self.client.post('/subscriptions/', self.data)
        self.email = mail.outbox[0]


    def test_send_subscribe_email_subject(self):
        """
        Verifica o subject do email
        """
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)


    def test_send_subscribe_email_from(self):
        """
        Verifica o remetente do email
        """
        expect = 'contact@workshop.com.br'
        self.assertEqual(expect, self.email.from_email)


    def test_send_subscribe_email_to(self):
        """
        Verifica para quem é o email
        """
        expect = ['pcego36@gmail.com', 'contact@workshop.com.br']
        self.assertEqual(expect, self.email.to)


    def test_send_subscribe_email_body(self):

        content = ['Paulo',
                   '99999999999',
                   'pcego36@gmail.com',
                   '32122980']

        for text in content:

            with self.subTest():
                self.assertIn(text, self.email.body)


class SubscribeSucessMessage(TestCase):


    def setUp(self):
        self.data = dict(name='Paulo', cpf='99999999999',
                         email='pcego36@gmail.com', phone='32122980')
        self.response = self.client.post('/subscriptions/', self.data, follow=True)


    """
    Verifica a exibição da mensagem de sucesso
    """
    def test_sucess_message(self):

        self.assertContains(self.response, 'Inscrição Realizada com Sucesso!')