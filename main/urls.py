from django.urls import path

from main import views
from main.apps import MainConfig
from main.views import DishListView, DishDetailView, contacts

app_name = MainConfig.name

urlpatterns = [
    path('', DishListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish_detail')
]
