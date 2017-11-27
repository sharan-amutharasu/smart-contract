
#add_to_end: 2017-11-22 11:04:20.580039
from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^$', views.sc_home, name='sc_home'),
]

#add_to_end: 2017-11-22 11:04:20.580076

#add_to_end: 2017-11-22 13:06:48.272941

urlpatterns += [
	url(r'^create_contract/', views.sc_create_contract, name='sc_create_contract'),
	url(r'^confirm_transaction/', views.sc_confirm_transaction, name='sc_confirm_transaction'),
]

#add_to_end: 2017-11-22 13:06:48.272983

#add_to_end: 2017-11-24 13:03:47.825509

urlpatterns += [
	url(r'^contract/', views.sc_contract, name='sc_contract'),
]

#add_to_end: 2017-11-24 13:03:47.825577
