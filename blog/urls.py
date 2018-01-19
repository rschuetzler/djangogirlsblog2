from django.conf.urls import url
from . import views

# This is where my URL patterns go
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
