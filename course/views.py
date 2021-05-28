from django.shortcuts import render
from . models import *
from itertools import chain, count
from django.views.generic import ListView
from django.contrib.auth.models import UserManager


# Create your views here.
class SearchView(ListView):
    template_name = 'course/view.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results        = Post.post_objects.search(query)
            lesson_results      = Lession.less_objects.search(query)
            profile_results     = Profile.prof_objects.search(query)
            # blog_results         =  Post.objects.filter(title__search=query)
            # lesson_results         =  Post.objects.filter(title__search=query)
            # profile_results         =  Post.objects.filter(title__search=query)

            
            # combine querysets 
            queryset_chain = chain(
                    blog_results,
                    lesson_results,
                    profile_results
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return Post.objects.none() # just an empty queryset as default

