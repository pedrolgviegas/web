from django.http import HttpResponse
from django.shortcuts import render
from workshop.subscriptions.forms import SubscriptionForm

# Create your views here.

def subscription(request):
    form = SubscriptionForm()
    return render(request, 'subscriptions/subscription_form.html', {'form': form})