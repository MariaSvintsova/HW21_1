from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Dish

class DishListView(ListView):
    model = Dish
    template_name = 'main/material_list.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'SkyStore'}


# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name}, ({email}): {message}')
#
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'main/contacts.html', context)

class ContactDetailView(DetailView):
    template_name = 'main/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, ({email}): {message}')
        return self.render_to_response(self.get_context_data())

class DishDetailView(DetailView):
    model = Dish
    template_name = 'main/dish_detail.html'
    context_object_name = 'dish'



