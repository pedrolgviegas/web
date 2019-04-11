from django import forms

class SubscriptionForm(forms.Form):

    name = forms.CharField(label='Nome',
                           widget=forms.TextInput(attrs={'class': 'contact_input', 'placeholder': 'Nome'}))

    cpf = forms.CharField(label='CPF',
                          widget=forms.TextInput(attrs={'class': 'contact_input', 'placeholder': 'CPF'}))

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'contact_input', 'placeholder': 'Email'}))

    phone = forms.CharField(label='Telefone',
                            widget=forms.TextInput(attrs={'class': 'contact_input', 'placeholder': 'Telefone'}))