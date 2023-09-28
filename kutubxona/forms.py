from django import forms
from kutubxona.models import BookModel,AuthorModel
class BookForm(forms.ModelForm):
    title = forms.CharField()
    title_ru = forms.CharField()
    title_en = forms.CharField()

    class Meta:
        model = BookModel
        exclude = ('title',)


class AuthorForm(forms.ModelForm):

    description_uz = forms.CharField()
    description_ru = forms.CharField()
    description_en = forms.CharField()

    class Meta:
        model = AuthorModel
        exclude = ('description',)