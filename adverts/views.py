from django.views.generic import ListView, DetailView
from .models import Advert


class AdvertListView(ListView):
    model = Advert
    template_name = 'advert_list.html'

"""
class AdvertListView(ListView):
    model = Advert
    template_name = 'advert_list.html'


class AdvertDetail(DetailView):
    model= Advert
    
    def get(self, request, advert_id):
        try:
            advert = Advert.objects.get(id = advert_id)
        except Exception as e:
            raise e
        return render(request, "adverts/advert.html", {'advert':advert})


"""