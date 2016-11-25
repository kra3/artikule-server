from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'author', 'publication_date', 'category')
    list_filter = ('author', 'category', 'publication_date')
    save_as = True
    search_fields = ('title',)

    def get_queryset (self, request):
        qs = self.model._default_manager.every_article()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
