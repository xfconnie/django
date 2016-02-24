from django.contrib import admin

# Register your models here.
from mysite.books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email')
    search_fields = ('first_name','last_name')

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)