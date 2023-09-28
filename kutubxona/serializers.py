from rest_framework.serializers import ModelSerializer
from .models import AuthorModel,BookModel


class AutherSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('name','dateofbirth','description','date_of_birth','status')


class BookSerializer(ModelSerializer):
    class Meta :
        model = BookModel
        fields = ('title','author','status')
