from django.contrib import admin
from django.urls import path, include
from . import views
from .views import menuview, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuview.as_view()),
    path('menu-items/', MenuItemView.as_view(), name='menu_items'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(),
         name='single_menu_item'),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
]
