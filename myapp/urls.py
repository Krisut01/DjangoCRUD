from django.urls import path
from . import views


urlpatterns= [
    path('',views.item_list, name='item_list'),
    path('item/new',views.create_item, name ='create_item'),
    path('item/<int:id>/edit',views.update_item,name='update_item' ),
    path('item/<int:id>/delete/', views.delete_item,name='delete_item')
]