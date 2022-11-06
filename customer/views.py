from django.shortcuts import render
from django.views import View, generic
from .models import MenuItem, Category, OrderModel


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

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        # create a variable items and assign it the list items from the order_items dictionary
        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            # at the end we add the item_data we have gotten from the menuitem model and add this to the items list
            order_items['items'].append(item_data)
