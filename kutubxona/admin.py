from django.contrib import admin
from .models import AuthorModel,BookModel
from .forms import BookForm,AuthorForm
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title',)
    search_fields = ('title',)

class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm
    list_display = ('name','dateofbirth','description','date_of_birth','status')
    search_fields = ('name','description')    

admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(BookModel, BookAdmin)