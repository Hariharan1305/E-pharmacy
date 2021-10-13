from django.db import models
CAT=(('Syrup','Syrup'),('Tablet','Tablet'),('Health Drinks','Health Drinks'))
# Create your models here.
class medicine(models.Model):
    brand_name=models.CharField(max_length=100)
    category=models.CharField(max_length=300,choices=CAT)
    manufacturing_date=models.DateField()
    expiry_date=models.DateField()
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    delivery_days=models.CharField(max_length=200)
    productimg=models.ImageField()
    is_favorite = models.BooleanField(default=False)
    

class addtocartmodel(models.Model):
    product_id=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    userid= models.IntegerField(default=0)

class orderdetailsmodel(models.Model):
    orderdate=models.DateField()
    totalamount=models.IntegerField()
    brand_name=models.CharField(max_length=150,default=0)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    userid=models.IntegerField()
    deliverydate=models.DateField()
    paymenttype=models.CharField(max_length=500)
    product_id=models.IntegerField()
    class Meta:
        db_table = "orderdetails"
    
class wishlistmodel(models.Model):
    product_id=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    userid=models.IntegerField()

    class Meta:
        db_table = "wishlist"
