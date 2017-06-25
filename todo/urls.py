from django.conf.urls import url

from . import views

app_name = 'calc'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='generic_index'),
    # url(r'^ajax/$', views.IndexView.ajax(), name='generic_index'),

    url(r'^$', views.index, name='index'),
    url(r'^ajax/$', views.ajax, name='ajax'),
]
