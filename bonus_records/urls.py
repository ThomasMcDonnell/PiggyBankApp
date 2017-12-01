from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.CreateRecord.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteRecordView.as_view(), name='record_delete',),
]