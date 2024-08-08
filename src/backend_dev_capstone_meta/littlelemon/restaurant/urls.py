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
    path('book/', views.book, name="book"),
    path('bookings/', views.bookings, name="bookings"),
    path('create-menu/', views.MenuItemsView.as_view()),
    path('menu/', views.menu, name ="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"), 
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('book-api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]