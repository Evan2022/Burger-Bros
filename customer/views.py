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

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price,
        }

        return render(request, '../templates/order.html', context)
