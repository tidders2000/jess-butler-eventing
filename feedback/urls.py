
from django.conf.urls import url, include
from feedback.views import feedback


urlpatterns = [
     
    url(r'^$', feedback, name="feedback"),
]