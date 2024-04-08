from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Dish


class DishListView(ListView):
    model = Dish
    template_name = 'main/home.html'
    object_list = Dish.objects.all()
    context_object_name = f'{object_list}'
    extra_context = {'title': 'SkyStore'}


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name},{phone} ({email}): {message}')
    return render(request, 'main/contacts.html')


class DishDetailView(DetailView):
    model = Dish
    template_name = 'main/dish_detail.html'
    context_object_name = 'dish'



