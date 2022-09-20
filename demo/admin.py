from django.contrib import admin

# Register your models here.
from .models import Book
# admin.site.register(Book)
@admin.register(Book)
class BoolAdmin(admin.ModelAdmin):
    # fields=['title', 'description',] 
    list_display=['id','title', 'description','price'] 
    list_filter=['is_published','price']
    search_fields=['title','description']