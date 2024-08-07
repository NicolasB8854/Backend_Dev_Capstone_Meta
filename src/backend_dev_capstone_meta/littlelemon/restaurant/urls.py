from django.urls import path, include
from .views import MenuItemsView, SingleMenuItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]