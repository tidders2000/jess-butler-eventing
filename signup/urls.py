from django.conf.urls import url, include

from .views import signups, emailadd

urlpatterns=[
    url(r'^signup/',signups, name='signups'),
    url(r'^emailadd/',emailadd, name='emailadd')
    ]