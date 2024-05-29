from django.urls import path

from my_app.views import get_item, get_all_items, delete

urlpatterns = [
    path('get/', get_item, name='get_item'),
    path('get-all/', get_all_items, name='get_all_items'),
    path('delete/', delete, name='delete')
]
