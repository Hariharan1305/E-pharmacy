from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from .forms import MedicineForm,AddtocartForm,OrderdetailForm,WishlistForm
from django.core import serializers
from .models import medicine,addtocartmodel,orderdetailsmodel,wishlistmodel
from datetime import timedelta
import datetime
import json
qutyval=0
idpricedetails = {}
# Create your views here.
def ao(request):
    if request.method == "POST":
        form=MedicineForm(request.POST,request.FILES)
        #print(request.POST)
        #print(form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/product/vo')
            except:
                pass
    else:
        form = MedicineForm()
    return render(request,'ao.html',{"form": form})

def vo(request):
    
    objects_list=medicine.objects.all()
    #for ob in objects_list:
        #print(ob.is_favorite)
    return render(request,'vo.html',{"object_list":objects_list})

def edit(request, id):
    #print(id)
    productedit = medicine.objects.get(id=id)
    return render(request,'update.html',{'productedit':productedit})

def update(request, id):
    #print(request)
    productedit = medicine.objects.get(id=id)
    form = MedicineForm(request.POST, instance = productedit)
    print(form.errors)
    if form.is_valid():
        form.save()
        return redirect("/product/vo")
    return render(request, 'update.html', {'productedit': productedit})

def destroy(request, id):
    productdel = medicine.objects.get(id=id)
    productdel.delete()
    return redirect("/product/vo")

def wishdelete(request, id):
    productdel = addtocartmodel.objects.get(id=id)
    productdel.delete()
    return redirect("/product/add_to_cart_buy")

def favorite_project(request, id):
    projectprofile = get_object_or_404(medicine, pk=id)
    try:
        if projectprofile.is_favorite:
            projectprofile.is_favorite = False
        else:
            projectprofile.is_favorite = True
        projectprofile.save()
        return redirect("/product/vo")
    except (KeyError, medicine.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

"""def favorite_remove(request, id):
    projectprofile = get_object_or_404(medicine, pk=id)
    try:
        projectprofile.is_favorite = False
        projectprofile.save()
        return redirect("/product/favorite")
    except (KeyError, medicine.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})"""

def favorite(request):
    objectlist={}
    cartlist=wishlistmodel.objects.all()
    organiclist=medicine.objects.all()
    print(cartlist)
    j=0;
    for cart in cartlist:
        objectli=medicine.objects.filter(id=cart.product_id)
       
        
        for ob in objectli:
            if request.user.id == cart.userid:
                objectlist[j]={"price":cart.price,"image":ob.productimg.url,"brand_name":ob.brand_name,"quantity":cart.quantity,"category":ob.category,"product_id":cart.product_id,"manufacturing_date":ob.manufacturing_date,"expiry_date":ob.expiry_date}
            print(objectlist[j])
            #listobj.append(list(objectlist))
        j+=1
    
    return render(request,'wishlist.html',{"object_list":objectlist})


def addtocart(request):
    addtocart=addtocartmodel.objects.all()
    productid=request.GET['id']
    price=request.GET['price']
    qty = 1
    userid=request.user.id
    print('rajafinal')
    print(productid)
    retval = chekproductid(productid,price)
    if retval:
        if userid is None:
           userid=0
        try: 
            form=AddtocartForm({'product_id':productid,'quantity':qty,'price': price,'userid':userid})
            form.save()
            return JsonResponse({'success': True}) 
        except (KeyError, medicine.DoesNotExist):
            return JsonResponse({'success': False}) 
    else :
        return JsonResponse({'success': True}) 

def chekproductid(id,price):
    addtocart=addtocartmodel.objects.filter(product_id=id).count()
    userid=0
    if addtocart == 0:
        return True
    else :
         
        try: 
            addtocart1= get_object_or_404(addtocartmodel, product_id=id)
            print(addtocart1.id)
            addtocart1.delete()
            addtocart1.quantity = addtocart1.quantity + 1
            addtocart1.price = int(addtocart1.price) + int(price)
            addtocart1.save()
            return False
        except (KeyError, medicine.DoesNotExist):
            return False

def removetocart(request, id):
    projectprofile = get_object_or_404(medicine, pk=id)
    try:  
        projectprofile.is_addcart = False
        projectprofile.save()
        return redirect("/product/add_to_cart_buy")
    except (KeyError, medicine.DoesNotExist):
        return JsonResponse({'success': False}) 
    else:
        return JsonResponse({'success': True})

def addtocartbuy(request):
    print("Raja")
    print(request.POST) 
    global qutyval,idpricedetails
    #idpricedetails = {}
    details = {}
    qutyval=0
    objects_list=addtocartmodel.objects.all()
    #deliverydate=(datetime.date.today() + timedelta(days=4)).strftime('%Y-%m-%d')
    #todaydate=(datetime.date.today()).strftime('%Y-%m-%d')
    j=0
    for objects in objects_list:
        print(objects.product_id)
        objects_list1=medicine.objects.filter(id=objects.product_id)[0]
        qutyval=qutyval+objects.price
        st=str(objects.id)
        
        details[j] = {"quantity":objects_list1.quantity,"product_id":objects.product_id,"id":objects.id,"brand_name":objects_list1.brand_name,"price":objects.price,"image":objects_list1.productimg}
        
        j+=1 
    if request.method=="POST":
        productid=request.POST.getlist('product_id')
        priceval = request.POST.getlist('price')   
        quantityval = request.POST.getlist('quantity')
        brand_name = request.POST.getlist('brand_name')
        paymenttype = request.POST.getlist('payment_option')
        #print(request.POST.totamt)
        totamt = request.POST.getlist('totalprice')
        print(quantityval)
        userid=request.user.id
        deliverydate=(datetime.date.today() + timedelta(days=4)).strftime('%Y-%m-%d')
        orderdate=(datetime.date.today()).strftime('%Y-%m-%d')
        if userid == None:
            return redirect('/users/login')
        c=len(objects_list)
        saved = False
        for i in range(c):
            
            form = OrderdetailForm({'paymenttype':paymenttype[0],'totalamount':totamt[0],'brand_name':brand_name[i],'orderdate':orderdate,'deliverydate':deliverydate,'userid':userid,'price':priceval[i],'quantity':quantityval[i],'product_id':productid[i]})
            if form.is_valid():
                try: 
                    print(form.errors)
                    form.save()
                    saved = True
                except: 
                    print("Error")
        if saved:     
            addtocartmodel.objects.all().delete()
            return redirect("/payment/paymentpost")
    else:  
        form = OrderdetailForm()
    print(objects_list)
    print(details)
    return render(request,'cart.html',{"object_list":details,'qutyval':qutyval,'lendthcount':len(objects_list)})

def changequty(request):
    print(request.GET)
    global qutyval
    priceval=0   
    objects_list=medicine.objects.filter(is_addcart=1)
    print(objects_list)
    for objects in objects_list:
        print(objects.id==int(request.GET['id']))
        if int(request.GET['id']) == objects.id:
            print("hello")
            #print(len(idpricedetails))
            priceval= int(request.GET['quty'])*objects.price
            for i in range(len(idpricedetails)):
                #print(idpricedetails[i]["id"])
                if idpricedetails[i]["id"] == int(request.GET['id']):
                    qutyval=qutyval-idpricedetails[i]["price"] 
                    idpricedetails[i] = {"id":int(request.GET['id']),"price":priceval}                
            qutyval=qutyval+priceval
            print(qutyval)
    return HttpResponse(str(qutyval))

def orderdetails(request):
    
    objectlist={}

    organiclist=medicine.objects.all()
    cartlist=orderdetailsmodel.objects.all()
    j=0;
    for cart in cartlist:
        print("hello")
        
        objectli=medicine.objects.filter(id=cart.product_id)
        print(objectli)
        for ob in objectli:
            print(ob)
            if request.user.id == cart.userid:
                objectlist[j]={"orderdate":cart.orderdate,"price":cart.price,"image":ob.productimg.url,"foodname":ob.brand_name,"quantity":cart.quantity}
        j+=1
    #dump = json.dumps(objectlist)
    print(objectlist)
    
    return render(request,'orderdetails.html',{"dump": objectlist})

def addwishlist(request):
    wishlist = wishlistmodel.objects.all()
    productid = request.GET['id']
    price = request.GET['price']
    qty = 1
    userid=request.user.id
    retval = chekwishproductid(productid,price,userid)
    if retval:
        if userid is None:
           userid=0
        try:
            form=WishlistForm({'product_id':productid,'quantity':qty,'price': price,'userid':userid})
            form.save()
            return JsonResponse({'success': True}) 
        except (KeyError, medicine.DoesNotExist):
            return JsonResponse({'success': False}) 
    else:
        return JsonResponse({'success': True}) 
        
def chekwishproductid(id,price,useridval):
    wishlist=wishlistmodel.objects.filter(product_id=id,userid=useridval).count()
    userid=0
    if wishlist == 0:
        return True
    else:
        try: 
            wishlist1= get_object_or_404(wishlistmodel, product_id=id,userid=useridval)
            #print(addtocart1.id)
            wishlist1.delete()
            wishlist1.quantity = wishlist1.quantity + 1
            wishlist1.price = int(wishlist1.price) + int(price)
            wishlist1.save()
            return False
        except (KeyError, medicine.DoesNotExist):
            return False

def favorite_remove(request, id):

    userid=request.user.id
    wishlist=wishlistmodel.objects.filter(product_id=id,userid=userid)
    wishlist.delete()
    return redirect("/product/favorite")
