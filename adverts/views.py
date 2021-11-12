from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Advert


class AdvertListView(ListView):
    model = Advert
    template_name = 'advert_list.html'


class AdvertDetailView(DetailView):
    model = Advert
    template_name = "advert_detail.html"


class AdvertUpdateView(UpdateView):
    model = Advert
    fields = ('title', 'body',)
    template_name = 'advert_edit.html'


class AdvertDeleteView(DeleteView):
    model = Advert
    template_name = 'advert_delete.html'
    success_url = reverse_lazy('advert_list')


class AdvertCreateView(CreateView):
    model = Advert
    fields = ('title', 'body', 'seller')
    template_name = 'advert_new.html'