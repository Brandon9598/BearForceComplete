from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^shift_pick_up/$', views.shift_pick_up, name="Shift pick up"),
	url(r'^shift_release/$', views.shift_release, name="Shift release"),
	url(r'^staff/$', views.staff, name="Staff"),
	url(r'^account/(?P<user_id>[0-9]+)/$', views.account, name="account"),
]