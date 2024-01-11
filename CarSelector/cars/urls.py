from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import car_list, add_car, edit_car
from .views import car_detail_view

urlpatterns = [
    path('', car_list, name='car_list'),
    path('add/', add_car, name='add_car'),
    path('edit/<int:car_id>/', edit_car, name='edit_car'),
    path('car_detail/<int:pk>/', car_detail_view, name='car_detail'),
]

# Add the following line to serve media files during development
