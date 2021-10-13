from django.forms import ModelForm
from .models import payment

class PaymentForm(ModelForm):
    class Meta:
        model=payment
        fields="__all__"
