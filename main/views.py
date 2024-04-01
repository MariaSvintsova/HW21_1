from django.shortcuts import render

from main.models import Dish


def home(request):
    context = {
        'object_list': Dish.objects.all(),
        'title': 'SkyStore'
    }
    return render(request, 'main/home.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contacts.html', context)


def dish_detail(request, dish_id):
    # Получаем информацию о товаре по его ID из базы данных
    dish = Dish.objects.get(pk=dish_id)
    return render(request, 'main/dish_detail.html', {'dish': dish})

