from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from .models import Book, Note
from .forms import RegisterForm, BookForm, NoteForm



def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home') 
    return render(request, 'confirm_delete.html', {'book': book})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})




def home(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = BookForm()

    return render(request, 'home.html', {'books': books, 'form': form})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_notes(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    notes = book.notes.all()
    return render(request, 'book_notes.html', {'book': book, 'notes': notes})

def add_note(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.book = book
            note.author = request.user
            note.save()
            return redirect('book_notes', book_id=book.id)
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form, 'book': book})
