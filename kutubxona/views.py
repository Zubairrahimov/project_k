from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AutherSerializer,BookSerializer
from .models import AuthorModel,BookModel
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import StaffPermissionClass,AdminPermissionClass,UserPermission

# Create your views here.



class CreatePollsAPiView(generics.CreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (IsAuthenticated,StaffPermissionClass)

class ListPollsApiView(generics.ListAPIView):
    serializer_class = AutherSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return AuthorModel.objects.filter(status=True)
    

class UpdateStatusPollsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class DeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (IsAuthenticated, UserPermission)


class AllBookView(generics.ListAPIView):
    queryset = BookModel
    serializer_class = BookSerializer

    def get_queryset(self):
        return AuthorModel.objects.filter(status=True)

class CreateBookView(generics.CreateAPIView):
    queryset = BookModel
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,StaffPermissionClass)

class UpdateBookView(generics.UpdateAPIView):
    queryset = BookModel
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, UserPermission)

class DeleteBookView(generics.DestroyAPIView):
    queryset = BookModel
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, UserPermission)


class AuthorBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['Auther_id'] 
        return BookModel.objects.filter(pk=pk)
    
class BookAuthorView(generics.RetrieveAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        pk = self.kwargs['book_id']  
        book = BookModel.objects.get(pk=pk)
        return book.author


