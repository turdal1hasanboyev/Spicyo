from django.urls import path

from apps.user.views import about, home


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]
