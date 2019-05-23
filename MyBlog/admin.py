from django.contrib import admin

# Register your models here.
from MyBlog.models import Category,Article

admin.site.register(
    Category,
    list_display = ['id', 'catName', 'catKey','catDescription'],
    list_display_links = ['id', 'catName'],
    search_fields = ['id', 'catName'],

)
admin.site.register(
    Article,
    list_display = ['id', 'artName','artAuthor', 'artDateCreate','artCatID']
)