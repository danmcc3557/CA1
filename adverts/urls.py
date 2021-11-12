from django.urls import path
from .views import AdvertListView

urlpatterns = [
    path('', AdvertListView.as_view(), name='advert_list'),
]