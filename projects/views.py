from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, "main.html")

def add_books(request):
    if request.method == "POST":
        id = request.Post['id']
        name = request.POST['name'] 
        author = request.POST['author'] 
        description = request.POST['description'] 
        tags = request.POST['tags']



# Create your views here.
