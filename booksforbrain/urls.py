from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', registrationForm, name='signup' ),
    path('login/', loginPage, name='login' ),
    path('logout/', logOut, name='logout' ),
    path('', home, name='home'),
    #requires id
    path('book-detail/<int:id>', bookDetail, name='book-detail'),
    path('owned/', ownedBook, name='owned-book'),
    path('publish/', publishBook, name='publish-book'),
    path('update-book/<int:id>', UpdateBook, name='update-book'),
    path('delete-book/<int:id>', DeleteBook, name='delete-book'),
]
