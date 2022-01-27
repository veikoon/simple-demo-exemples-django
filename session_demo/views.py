import logging
from django.shortcuts import render
from django.http.response import  HttpResponseRedirect, HttpResponse
from session_demo.forms import OperationForm

# Create your views here.
logger = logging.getLogger(__name__)

def calculator(request):
    template_name = 'calc.html'

    # If the use have a session get back the values else initialize them
    # Exemple of single value session (Total of all operations)
    if request.session.get('total', False):
        total = request.session['total']
    else : 
        total = 0
    
    # Exemple of list value session (List of all operations)
    if request.session.get('history', False):
        history = request.session['history']
    else : 
        history = []

    # If the method used to access the book page is a POST  
    if request.method == 'POST':

        # Check if the user has pressed the reset button
        if "reset" in request.POST:
            reset(request)

        # Then the user has made a new operation
        else:
            # The data from the body of the POST request is put inside a custom form object
            form = OperationForm(request.POST)

            # If the data submited by the form is correct
            if form.is_valid():

                # Get forms values
                value = int(form.cleaned_data["value"])
                sign = form.cleaned_data["sign"]

                # Append this operation to the history
                history.append({"value": value, "sign": sign, "total": total})

                # Update the history, 
                # /!\ Please note that you can't do directly append to the session /!\
                # request.session['history'].append() IS WRONG because a list is not a 'simple' object
                request.session['history'] = history

                # Calculate the operation, dang it python why not using switch as everybody
                if sign == '+': total += value
                elif sign == '-': total -= value
                elif sign == 'x': total *= value
                elif sign == '/': total /= value

                # Update the actual total
                request.session['total'] = total

            else:
                logger.warning("Mauvais formulaire")
        
        # Once the operation is done the user is redirected to the same page with a GET method
        return HttpResponseRedirect(request.path_info)

    context = {"total": total, "operations": history}
    return render(request, template_name, context)

# If the user have a session with those attributes, delete them
def reset(request):
    if request.session.get('history', False):
        del request.session['history']
    if request.session.get('total', False):
        del request.session['total']

    # This can also be done quicker :

    #for key in request.session.keys():
    #    del request.session[key]
