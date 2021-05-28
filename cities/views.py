from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.db.models import Q # new

from .models import City


class HomePageView(TemplateView):
    template_name = 'cities/home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'cities/search_results.html'
    # queryset = City.objects.filter(name__icontains='query')


    # def get_queryset(self): # new
    #     return City.objects.filter(
    #         Q(name__icontains='Boston') | Q(state__icontains='NY')
    #     )


    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list