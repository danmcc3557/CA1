from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class AdvertUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advert
    fields = ('title', 'body',)
    template_name = 'advert_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user


class AdvertDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advert
    template_name = 'advert_delete.html'
    success_url = reverse_lazy('advert_list')

    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user

class AdvertCreateView(LoginRequiredMixin, CreateView):
    model = Advert
    fields = ('title', 'body', 'image', 'price')
    template_name = 'advert_new.html'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)