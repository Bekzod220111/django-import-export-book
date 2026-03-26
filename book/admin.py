from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Author, Book
from .resources import AuthorResource, BookResource

# Register your models here.

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    list_display = ('id', 'ism', 'familya')
    search_fields = ('ism', 'familya')


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ('id', 'author', 'title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)