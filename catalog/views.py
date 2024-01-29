
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.contrib import messages
from .forms import UserImage

def home(request):
    return render(request,"catalog/index.html")

def Addproduct(request):
    if(request.method == "POST"):
        form=UserImage(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form=UserImage()
    return render(request,"catalog/Addproduct.html",{'form':form})

def shop(request):
    category=Category.objects.filter(status=0)
    return render(request,"catalog/shop.html",{"category":category})

def shopview(request,name):
    if(Category.objects.filter(name=name,status=0)).exists():
        items=Products.objects.filter(category__name=name)
        return render(request,"catalog/items/index.html",{"items":items,"category_name":name})
    else:
        messages.warning(request, "No such category found")
        return redirect("shopview")

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            product_items=Products.objects.filter(name=pname,status=0).first()
            return render(request,'catalog/items/product_details.html',{"product_items":product_items})
        else:
            messages.error(request,"No such category found")
            return redirect('shop')   
    
    else:
        messages.error(request,"No such category found")
        return redirect('shop')
    
def update(request,pk):
    data = Products.objects.get(id=pk)

    form = UserImage(instance=data)
    if request.method == 'POST':
        form = UserImage(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect("shop")

    context={
        'form':form
    }
    return render(request,'catalog/update.html',context)

def delete(request, pk):

    delete_product=Products.objects.get(id=pk)
 
    if request.method == "GET":
        context = {'item': delete_product}
        return render(request, 'catalog/delete.html', context)
 
    elif request.method == "POST":
        confirm_delete = request.POST.get('confirm_delete', True)
 
        if confirm_delete:
            delete_product.delete()
            return HttpResponseRedirect(reverse('shop'))
        else:
            return HttpResponseRedirect(reverse('delete'))


