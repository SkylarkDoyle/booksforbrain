from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .filter import BookFilter
from django.contrib.auth.decorators import login_required
from .decorators import *


# Create your views here.
@unauthenticated_user
def registrationForm(request):
    form = RegForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="bookreader")
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for Reader " + username + " ✔️")
            return redirect('login')
        

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Check out your books')
            return redirect('home')
        else:
            messages.error(request, 'Username or password incorrect 🤔')

    return render(request, 'login.html', ) 

def logOut(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    
    all_books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=all_books)
    all_books = book_filter.qs
    books_available = all_books.count()
    ownedbook = OwnedBook.objects.all()
    books_sold = ownedbook.count()
    group = User.objects.filter(groups__name='bookreader')
    readers = group.count()
    
    context = {
        'all_books': all_books,
        'books_available': books_available,
        'readers': readers,
        'books_sold': books_sold,
        'book_filter': book_filter
    }

    return render(request, 'home.html', context)

@allowed_user(allowed_roles=['bookreader'])
@login_required(login_url='login')
def bookDetail(request, id):
    book = get_object_or_404(Book, id=id)
    reader = request.user
    

    if request.method == 'POST':
        own = OwnedBook.objects.create(
            reader = reader,
            book = book,
            owned = 'owned'

        )
        book.quantity -= 1
        book.save()
        own.save()
        messages.success(request, "You bought a book")
        
        return redirect("owned-book")
    context = {
        'book': book,
        'reader': reader,
       
    
    }

    return render(request, 'book_detail.html', context)

@allowed_user(allowed_roles=['bookreader'])
@login_required(login_url='login')
def ownedBook(request):
    reader = request.user
    owned_books = reader.owned.all()

    context = {
        'owned_books': owned_books
    }
    
    
    return render(request, 'owned_book.html', context)


@admin_only
@login_required(login_url='login')
def publishBook(request):
    publishForm = PublishBook(request.POST)
    if request.method == 'POST':
        if publishForm.is_valid():
            publishForm.save()
            publishForm = PublishBook()
            messages.success(request, 'A book was published 📚')
            return redirect('home')
            

    context = {
        'publishForm': publishForm
    }
      

    return render(request, 'publish_book.html', context)

@login_required(login_url='login')
def UpdateBook(request, id):
    book = Book.objects.get(id=id)
    publishForm = PublishBook(request.POST or None, instance=book)
    if request.method == 'POST':
        if publishForm.is_valid():
            publishForm.save()
            messages.success(request, 'A book was updated ✒️')
            return redirect('home')

    context = {
        'publishForm': publishForm
    }
      

    return render(request, 'publish_book.html', context)

@login_required(login_url='login')
def DeleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.info(request, 'A Book was Deleted 😧')
    return redirect('home')

