
#add_to_end: 2017-11-22 11:04:20.580039
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from . import views
urlpatterns = [
	url(r'^$', views.sc_home, name='sc_home'),
]

#add_to_end: 2017-11-22 11:04:20.580076

#add_to_end: 2017-11-22 13:06:48.272941

urlpatterns += [
	url(r'^create_contract/', views.sc_create_contract, name='sc_create_contract'),
	url(r'^access_contract/', views.sc_access_contract, name='sc_access_contract'),
]

#add_to_end: 2017-11-22 13:06:48.272983

#add_to_end: 2017-11-24 13:03:47.825509

urlpatterns += [
	url(r'^contract/', views.sc_contract, name='sc_contract'),
]

#add_to_end: 2017-11-24 13:03:47.825577
#url(r'^contract/(?P<pk>\d+)$', views.sc_contract, name='sc_contract'),
#add_to_end: 2017-11-30 09:07:45.712514

urlpatterns += [
	url(r'^approve_contract/', views.sc_approve_contract, name='sc_approve_contract'),
]

#add_to_end: 2017-11-30 09:07:45.712553

#add_to_end: 2017-11-30 20:59:01.028029

urlpatterns += [
	url(r'^confirm_contract/', views.sc_confirm_contract, name='sc_confirm_contract'),
	url(r'^download/', views.sc_download, name='sc_download'),
	url(r'^request_credentials/', views.request_credentials, name='request_credentials'),
]

#add_to_end: 2017-11-30 20:59:01.028063
