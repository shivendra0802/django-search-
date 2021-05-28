from django.contrib import admin
from django.urls import path, include
from course.views import SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SearchView.as_view(), name='search'),
    path('city/', include('cities.urls')),
]
