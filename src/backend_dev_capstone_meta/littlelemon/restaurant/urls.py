from django.urls import path
from .views import MenuItemsView, SingleMenuItemView
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]