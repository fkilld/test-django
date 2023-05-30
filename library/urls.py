from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('', views.list_books, name='list_books'),
    # path('add_book/', views.add_book, name='add_book'),
    # path('update/<int:id>/', views.update_book, name='update_book'),
    # path('add_category/', views.add_category, name='add_category'),
    # path('add_author/', views.add_author, name='add_author'),
    # path('delete_book/<int:id>/', views.delete_book, name='delete_book'),

]