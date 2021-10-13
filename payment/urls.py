from django.urls import path
from .import views

urlpatterns=[
    path('',views.paymentview,name="pay"),
    path('paymentpost/',views.paymentpost,name="payment"),
    path('update/<int:id>',views.update,name="update"),
    path('edit/<int:id>',views.edit,name="edit"),
]
