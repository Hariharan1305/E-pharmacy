from django.shortcuts import render
from .models import payment
from .forms import PaymentForm
from datetime import timedelta
import datetime
# Create your views here.
def paymentview(request):
    object_list=paymentdetails.objects.all()
    return render(request,'paymentview.html',{'object_list':object_list})

def paymentpost(request):
    deliverydate=(datetime.date.today() + timedelta(days=10)).strftime('%Y-%m-%d')
    if request.method=='POST':
        form=PaymentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
    else:
        form = PaymentForm()
    return render(request,'payment.html',{"form":form,'deliverydate':deliverydate})

def update(request,id):
    productedit=organicfood.objects.get(id=id)
    print(request.POST)
    form=OrganicForm(request.POST,instance=productedit)
    if form.is_valid():
            form.save()
            redirect('home')
    return render(request,'update.html',{"productedit":productedit})


def edit(request,id):
    productedit=organicfood.objects.get(id=id)
    return render(request,'update.html',{"productedit":productedit})

