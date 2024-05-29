from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import Item


# Create your views here.
def get_item(request):
    item = Item.objects.first()
    response = f'{item.id}<br>{item.name}<br>{item.price}<br>{item.count}<br>{item.created_at}<br>'
    return HttpResponse(response)


def get_all_items(request):
    items = Item.objects.all()
    response = ''
    for i in items:
        response += f'*{i.id}<br>{i.name}<br>{i.price}<br>{i.count}<br>{i.created_at}<br>'
    return HttpResponse(response)


def delete(request):
    items = Item.objects.first().delete()
    return HttpResponse('Deleted!')
