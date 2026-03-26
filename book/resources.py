from import_export import resources
from .models import Author, Book


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author
        fields = ('id', 'ism', 'familya')
        export_order = ('id', 'ism', 'familya')


class BookResource(resources.ModelResource):
    class Meta:
        model = Book        
        fields = ('id', 'author', 'title', 'description', 'created_at')
        export_order = ('id', 'author', 'title', 'description', 'created_at')