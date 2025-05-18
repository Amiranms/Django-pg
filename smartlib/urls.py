from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page = "/"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('books/add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('books/<int:book_id>/notes/', views.book_notes, name='book_notes'),
    path('books/<int:book_id>/notes/add/', views.add_note, name='add_note'),
]
