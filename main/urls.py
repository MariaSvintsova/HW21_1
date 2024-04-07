from django.urls import path

from main import views
from main.apps import MainConfig
from main.views import DishListView, DishDetailView, ContactDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', DishListView.as_view(), name='home'),
    path('contact/', ContactDetailView.as_view(), name='contact'),
    path('dish/<int:dish_id>/', DishDetailView.as_view(), name='dish_detail')
]
