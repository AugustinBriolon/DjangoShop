from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Product
from .form import createForm

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'djangoIIM/index.html', context)

def create(request):
    if request.method == 'POST':
        form = createForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('djangoIIM:index')
    else:
        form = createForm()
    context = {
        'form': form
    }
    return render(request, 'djangoIIM/create.html', context)

def update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = createForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('djangoIIM:index')
    else:
        form = createForm(instance=product)
    context = {
        'form': form
    }
    return render(request, 'djangoIIM/update.html', context)

def product(request, id):
    context = {
        'product': Product.objects.get(id=id)
    }
    return render(request, 'djangoIIM/product.html', context)

def delete(request, id):
    context ={}
    obj = get_object_or_404(Product, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "djangoIIM/delete.html", context)
