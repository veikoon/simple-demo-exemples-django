from django.shortcuts import render
from myapp.forms import BookForm

from myapp.models import Book

# Create your views here.

def home(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)

def addBook(request):
    template_name = 'add_book.html'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                name = form.cleaned_data["name"],
                autor = form.cleaned_data["autor"],
                price = form.cleaned_data["price"],
                stock = form.cleaned_data["stock"]
            )
            print(form.cleaned_data["autor"])
    all_books = Book.objects.all()
    context = {"books": all_books}
    return render(request, template_name, context)