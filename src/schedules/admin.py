from django.contrib import admin
from .models import User, Shift, News_Messages
# Register your models here.

class News_MessagesModelAdmin(admin.ModelAdmin):
	list_display = ["title", "user", "publish_date"]
	list_filter =  ["publish_date", "user"]
	search_fields = ["title", "content", "user"]
	class Meta:
		model = News_Messages

admin.site.register(User)
admin.site.register(Shift)
admin.site.register(News_Messages, News_MessagesModelAdmin)