from django.urls import path, include
from .views import MenuItemsView, SingleMenuItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('book/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]