from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.models import Material


class MaterialCreateView(SuccessMessageMixin, CreateView):
    model = Material
    fields = ('title', 'slug', 'body', 'preview', 'is_published', 'views_count')
    success_url = reverse_lazy('materials:list')
    success_message = "Материал успешно создан!"


    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'slug', 'body', 'preview', 'is_published', 'views_count')
    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialListView(ListView):
    model = Material
    template_name = 'main/material_list.html'
    context_object_name = 'object_list'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class MaterialDetailView(DetailView):
    model = Material
    context_object_name = 'material'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')