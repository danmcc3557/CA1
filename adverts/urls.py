from django.urls import path

from .views import (
    AdvertListView,
    AdvertUpdateView,
    AdvertDetailView,
    AdvertDeleteView,
    AdvertCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', AdvertUpdateView.as_view(), name='advert_edit'),
    path('<int:pk>', AdvertDetailView.as_view(), name='advert_detail'),
    path('<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert_delete'),
    path('/new/', AdvertCreateView.as_view(), name='advert_new'),
    path('', AdvertListView.as_view(), name='advert_list'),
]