from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category, OrderModel


# class Index(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, '../templates/index.html')


class Index(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        burgers = MenuItem.objects.filter(category__name__contains='BURGERS')
        desserts = MenuItem.objects.filter(category__name__contains='DESSERT')
        drinks = MenuItem.objects.filter(category__name__contains='DRINKS')
        sides = MenuItem.objects.filter(category__name__contains='SIDES')

        context = {
            'burgers': burgers,
            'desserts': desserts,
            'drinks': drinks,
            'sides': sides,

        }

        return render(request, '../templates/index.html', context)

    
