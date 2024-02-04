from django.shortcuts import render
from store.models import Product
from django.views import View



class Home(View):
    def get(self, request):
        products = Product.objects.filter(is_available=True)
        context = {
            'products': products
        }
        return render(request, 'home.html', context)



