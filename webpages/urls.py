from django.urls import path
from .views import home_page,book_page,picture_page,program_page
urlpatterns = [
    path('',home_page,name="home"),
    path('book.html/',book_page,name='book'),
    path('picture.html/',picture_page,name='picture'),
    path('program.html/',program_page,name='program'),
]