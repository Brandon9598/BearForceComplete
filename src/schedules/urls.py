from django.conf.urls import url

from .views import (
	index,
	shift_pick_up_view,
	shift_release_view,
	staff_view,
	account_view,
)

urlpatterns = [
	url(r'^$', index, name='index'),
]