from django.conf.urls import url, include

from . import views


company_patterns = [
    url(r'^create/$', views.CompanyCreate.as_view(), name='create'),
    url(r'^invites/$', views.Invites.as_view(), name='invites'),
    url(r'^invites/(?P<code>\w+)/(?P<response>accept|reject)/$', views.InviteResponse.as_view(), name='invite_response'),
    url(r'^edit/(?P<slug>[-\w]+)$', views.CompanyUpdate.as_view(), name='update'),
    url(r'^view/(?P<slug>[-\w]+)$', views.CompanyDetail.as_view(), name='detail'),
    url(r'^leave/(?P<slug>[-\w]+)/$', views.Leave.as_view(), name='leave'),
]


urlpatterns = [
    url(r'^companies/', include(company_patterns, namespace='companies'))
]
