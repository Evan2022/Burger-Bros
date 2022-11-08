from django.shortcuts import render
from django.views import View, generic
from .models import MenuItem, Category, OrderModel
from django.core.mail import send_mail

# https://www.youtube.com/watch?v=TXv2lbbhsOc&list=LL&index=5&t=1472s tutorial was followed for this project.



class Index(View):
    def get(self, request, *args, **kwargs):
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')

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

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            postcode=postcode,
        )
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price,
        }

        return render(request, '../templates/order.html',  context)
