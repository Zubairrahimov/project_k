from django.urls import path
from .views import (CreatePollsAPiView,DeleteUserView,UpdateStatusPollsView,ListPollsApiView,
                    CreateBookView,AllBookView,UpdateBookView,DeleteBookView,BookAuthorView,AuthorBooksView)

urlpatterns = [
    path('Acreate/', CreatePollsAPiView.as_view()),
    path('Bcreate/',CreateBookView.as_view()),
    path('Alist/', ListPollsApiView.as_view()),
    path('update_status/<int:pk>/', UpdateStatusPollsView.as_view()),
    path('Adelete/<int:pk>/', DeleteUserView.as_view()),
    path('Blist/',AllBookView.as_view()),
    path('update_status/<int:pk>/',UpdateBookView.as_view()),
    path('Bdelete/<int:pk>/',DeleteBookView.as_view()),
    path('AutherBook/<int:pk>',AuthorBooksView.as_view()),
    path('BookAuther/<int:pk>',BookAuthorView.as_view())

]