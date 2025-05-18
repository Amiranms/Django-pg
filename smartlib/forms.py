from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Note
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
    

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
