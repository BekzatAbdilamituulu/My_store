from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Categories
from django.urls import reverse_lazy
from .forms import *
from .models import *
from cart.forms import CartAddProductForm


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'
        }]
def index(request):
    viewss = Products.objects.all()
    cats = Categories.objects.all()
    context = {
        'viewss': viewss,
        'cats': cats,
    }
    return render(request, 'viewapp/index.html', context)


def about(request):
    return render(request, 'viewapp/about.html', {'menu': menu, 'title': 'О сайте'})

def contact(request):
    return HttpResponse('Обратная связь')

def show_post(request, post_id):
    contexts = Products.objects.get(id=post_id)
    cart_product_form = CartAddProductForm()
    context = {
        'data': contexts,
        'cart_product_form': cart_product_form,
    } 
    
    
    return render(request, 'viewapp/detail.html', context=context)

def category_detail(request, cat_id):
    cat = Categories.objects.get(id=cat_id)
    products = Products.objects.filter(categories__exact=cat)

    return render (request, 'viewapp/category.html', {'cat': cat, 'products': products})



