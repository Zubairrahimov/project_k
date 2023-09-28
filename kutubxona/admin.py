from django.contrib import admin
from .models import AuthorModel,BookModel
from .forms import BookForm
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(AuthorModel)
admin.site.register(BookModel, BookAdmin)