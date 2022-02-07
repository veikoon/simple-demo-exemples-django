from django.shortcuts import render
from quizz_demo.models import Question
from django.http.response import  HttpResponseRedirect


# Create your views here.
def quizz(request):
    template_name = 'quizz.html'
    
    # Recover the user session or create a new one
    if "quizz" in request.session:
        data = request.session["quizz"]
    else:
        data = {
            "questions_answered": [],
            "questions_yes": [],
            "questions_no": [],
            "questions_skipped": []
        }

    # If the method used to access the page is a POST 
    if request.method == 'POST':

        # If the user has submited a question form
        if "question_id" in request.POST:

            # Get the question id from the hidden input
            question_id = int(request.POST.get("question_id"))

            # Put the question in the corresponding list depending on the button pressed
            if "yes" in request.POST:
                data["questions_yes"].append(question_id)
            elif "no" in request.POST:
                data["questions_no"].append(question_id)
            else:
                data["questions_skipped"].append(question_id)
            
            # In any ways set the question as answered
            data["questions_answered"].append(question_id)

            # Save changes in the user session
            request.session["quizz"] = data
        
        # If the user has pressed the reset button and have a session
        if "reset" in request.POST and "quizz" in request.session :
            del request.session["quizz"]

        # The user is redirected to the same page with a GET method
        return HttpResponseRedirect(request.path_info)

    # Get all questions, order by their id while excluding those already answered
    questions = Question.objects.all().order_by('id').exclude(id__in=data["questions_answered"])

    # Extract the main question from all remaining questions
    main_question = {}
    if questions :
        main_question = questions[0]
        questions = questions.exclude(id=main_question.id)

    # Extract questions texts based on their id
    questions_yes = Question.objects.all().filter(id__in=data["questions_yes"])
    questions_no = Question.objects.all().filter(id__in=data["questions_no"])
    questions_skipped = Question.objects.all().filter(id__in=data["questions_skipped"])

    # Generate context
    context = {
        "questions": questions,
        "main_question": main_question,
        "questions_yes": questions_yes,
        "questions_no": questions_no,
        "questions_skipped": questions_skipped
        }
    return render(request, template_name, context)