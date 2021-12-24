from types import MethodDescriptorType
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book
from .forms import BookFrom

def main(request):
    return render(request, "main.html")

def add_books(request):
    if request.method == "POST":
        id = request.Post['id']
        name = request.POST['name'] 
        author = request.POST['author'] 
        description = request.POST['description'] 
        tags = request.POST['tags']
    return render(request, 'templates/add_book.html')

def updateBook(request, bn):
    book = Book.objects.get(id=bn)
    form = BookFrom(instance=book)
    if request.method == 'POST':
        form = BookFrom(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'templates/add_book.html', context)

def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('projects')
    context = {'object': book}
    return render(request, 'templates/delete_book.html', context)

# Create your views here.
