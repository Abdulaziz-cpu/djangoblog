from django.contrib import admin

from .models import Article,Comment

admin.site.register(Comment)

# Register your models here.
@admin.register(Article)
class Articleadmin(admin.ModelAdmin):
    list_display= ["title","author","created_date"]#bu bizim cedvelimizde listimizde yeni bashliq istifadeci adi ve yaranma tarixinide gostermek ucundur
    search_fields= ["title"]#bu kod search hissesinde bashliq ile search etmek ucundur
    list_filter=["created_date"]#buda yan terefde bu gn son 7 gun bu ay ve bu il icinde yaranan article'leri axtarish vermek ucundur
    class Meta:
        model = Article


