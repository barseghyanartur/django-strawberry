from django.contrib import admin

from .models import Book

__all__ = (
    'BookAdmin',
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book admin."""

    list_display = ('title', 'isbn', 'price', 'publication_date')
    search_fields = ('title',)
