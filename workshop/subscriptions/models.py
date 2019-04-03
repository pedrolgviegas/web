from django.db import models

# Create your models here.

class Subscriptions(models.Model):

    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

