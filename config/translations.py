from modeltranslation.translator import translator, TranslationOptions
from kutubxona.models import BookModel, AuthorModel


class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = ('uz', )

class BookTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('uz',)

translator.register(BookModel, AuthorModel, AuthorTranslationOptions, BookTranslationOptions)