from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'author', 'publication_date', 'category')
    list_filter = ('author', 'category', 'publication_date')
    save_as = True
    search_fields = ('title',)
