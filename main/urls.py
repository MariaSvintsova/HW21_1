from django.urls import path

from main import views
from main.apps import MainConfig
from main.views import contact, home


app_name = MainConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail')
]
