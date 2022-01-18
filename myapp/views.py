from django.shortcuts import render
from myapp.forms import BookForm
from django.http.response import  HttpResponseRedirect

from myapp.models import Book
import logging

# Create your views here.

logger = logging.getLogger(__name__)

def home(request):
    template_name = 'home.html'
    if request.session.get('last_book_created', False):
        last_book = "Dernier livre ajouté : " + request.session["last_book_created"]
    else:
        last_book = "Pas de livre récemment ajouté"
    context = {"message": last_book}
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
            request.session["last_book_created"] = form.cleaned_data["name"]
        else:
            logger.warning("Mauvais formulaire")
        return HttpResponseRedirect(request.path_info)
    all_books = Book.objects.all()
    context = {"books": all_books}
    return render(request, template_name, context)