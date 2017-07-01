from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='generic_index'),
    # url(r'^ajax/$', views.IndexView.ajax(), name='generic_index'),

    url(r'^$', views.index, name='index'),
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^complete_item/$', views.complete_item, name='complete_item'),
]
