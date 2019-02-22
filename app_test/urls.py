from django.conf.urls import url

#from . import views
from app_test.views import *

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^lista/$', Tabla01ListView.as_view(), name='tabla01_list'),
    url(r'^crear/$', Tabla01CreateView.as_view(), name='tabla01_create' ),
    url(r'^actualizar/(?P<pk>\d+)/$', Tabla01UpdateView.as_view(), name='tabla01_update'),
    url(r'^borrar/(?P<pk>\d+)/$', Tabla01DeleteView.as_view(), name='tabla01_delete'),
]