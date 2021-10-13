from django.forms import ModelForm
from .models import medicine,addtocartmodel,orderdetailsmodel,wishlistmodel

class MedicineForm(ModelForm):
    class Meta:
        model=medicine
        fields='__all__'

class AddtocartForm(ModelForm):
    class Meta:
        model=addtocartmodel
        fields='__all__'

class OrderdetailForm(ModelForm):
    class Meta:
        model=orderdetailsmodel
        fields='__all__'

class WishlistForm(ModelForm):
    class Meta:
        model=wishlistmodel
        fields='__all__'
