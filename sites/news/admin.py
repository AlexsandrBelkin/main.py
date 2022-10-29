from django.contrib import admin
from news.models import News, Commentary

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "is_published", "views")

admin.site.register(News, NewsAdmin)
admin.site.register(Commentary)