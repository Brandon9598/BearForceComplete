from django.conf.urls import url

from . import views

#app_name = "schedules"
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^messages$', views.messages, name="messages"),

	url(r'^shift_pick_up$', views.shift_pick_up, name="shift_pick_up"),
	url(r'^shift_release$', views.shift_release, name="shift_release"),

	url(r'^management$', views.management_users, name="management"),
	url(r'^management/Create_Users/$', views.UserCreate.as_view(), name="user-add"),

	url(r'^staff$', views.staff, name="staff"),
	url(r'^account/(?P<user_id>[0-9]+)$', views.account, name="account"),
]