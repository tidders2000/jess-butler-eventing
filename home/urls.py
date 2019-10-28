
from django.conf.urls import url, include
from home.views import index, index1


urlpatterns = [
     
    url(r'^$', index, name="index"),
    url(r'^index1/', index1, name="index1"),
]