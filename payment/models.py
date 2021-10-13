from django.db import models
PAY_OPTIONS=(('Debit card','Debit card'),('Credit card','Credit card'),('UPI','UPI'),('Net Banking','Net Banking'))
# Create your models here.
class payment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=200)
    product_name=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.IntegerField()
    payment_option=models.CharField(max_length=100,choices=PAY_OPTIONS)
