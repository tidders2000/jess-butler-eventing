
from django.conf.urls import url, include
from horsecamp.views import horsecamp, lessons


urlpatterns = [
     
    url(r'^$', horsecamp, name="horsecamp"),
    url(r'^lessons/', lessons, name="lessons"),
]