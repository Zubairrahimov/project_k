
from django import forms
from .models import BookModel,AuthorModel
class BookForm(forms.ModelForm):
    title_uz = forms.CharField()
    title_ru = forms.CharField()
    title_en = forms.CharField()

    class Meta:
        model = BookModel
        exclude = ('title',)


class AuthorForm(forms.ModelForm):
    # name_uz = forms.CharField()
    # name_ru = forms.CharField()
    # name_en = forms.CharField()

    description_uz = forms.CharField()
    description_ru = forms.CharField()
    description_en = forms.CharField()

    class Meta:
        model = AuthorModel
        exclude = ('description',)