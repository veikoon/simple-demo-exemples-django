from django.shortcuts import render
from quizz_demo.models import Question
from django.http.response import  HttpResponseRedirect


# Create your views here.
def quizz(request):
    template_name = 'quizz.html'
    
    if "quizz" in request.session:
        data = request.session["quizz"]
    else:
        data = {
            "questions_answered": [],
            "questions_yes": [],
            "questions_no": [],
            "questions_skipped": []
        }

    questions = Question.objects.all().order_by('id').exclude(id__in=data["questions_answered"])

    # If the method used to access the book page is a POST 
    if request.method == 'POST':

        if "question_id" in request.POST:

            question_id = int(request.POST.get("question_id"))

            if "yes" in request.POST:
                data["questions_yes"].append(question_id)
            elif "no" in request.POST:
                data["questions_no"].append(question_id)
            else:
                data["questions_skipped"].append(question_id)
            
            data["questions_answered"].append(question_id)
            request.session["quizz"] = data
        
        if "reset" in request.POST:
            del request.session["quizz"]

        # Once the object is created the user is redirected to the same page with a GET method
        return HttpResponseRedirect(request.path_info)

    main_question = {}
    if questions :
        main_question = questions[0]
        questions = questions.exclude(id=main_question.id)
    questions_yes = questions_no = questions_skipped = []
    for question in data["questions_yes"]:
        questions_yes = Question.objects.all().filter(id__in=data["questions_yes"])
    for question in data["questions_no"]:
        questions_no = Question.objects.all().filter(id__in=data["questions_no"])
    for question in data["questions_skipped"]:
        questions_skipped = Question.objects.all().filter(id__in=data["questions_skipped"])
    context = {
        "questions": questions,
        "main_question": main_question,
        "questions_yes": questions_yes,
        "questions_no": questions_no,
        "questions_skipped": questions_skipped
        }
    print(data)
    return render(request, template_name, context)