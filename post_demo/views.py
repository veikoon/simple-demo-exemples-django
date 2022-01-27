from django.shortcuts import render
from post_demo.forms import BookForm
from django.http.response import  HttpResponseRedirect
from post_demo.models import Book
import logging

logger = logging.getLogger(__name__)

def addBook(request):
    template_name = 'library.html'
    
    # If the method used to access the book page is a POST 
    if request.method == 'POST':

        # The data from the body of the POST request is put inside a custom form object
        form = BookForm(request.POST)

        # If the data submited by the form is correct
        if form.is_valid():

            # A new Book is created in the database
            Book.objects.create(
                name = form.cleaned_data["name"],
                autor = form.cleaned_data["autor"],
                price = form.cleaned_data["price"],
                stock = form.cleaned_data["stock"]
            )
        else:
            logger.warning("Mauvais formulaire")
        
        # Once the object is created the user is redirected to the same page with a GET method
        return HttpResponseRedirect(request.path_info)

    all_books = Book.objects.all()
    context = {"books": all_books}
    return render(request, template_name, context)