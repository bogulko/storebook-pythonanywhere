from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^',views.stores_list, name='store list'),
]