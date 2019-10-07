
from django.conf.urls import url, include
from horsecamp.views import horsecamp


urlpatterns = [
     
    url(r'^$', horsecamp, name="horsecamp"),
]