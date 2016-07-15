from django.conf.urls import url

from . import views

app_name = "schedules"
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new_message/$', views.new_message, name="new_message"),
	url(r'^shift_pick_up/$', views.shift_pick_up, name="shift pick up"),
	url(r'^shift_release/$', views.shift_release, name="shift release"),
	url(r'^staff/$', views.staff, name="staff"),
	url(r'^account/(?P<user_id>[0-9]+)/$', views.account, name="account"),
]