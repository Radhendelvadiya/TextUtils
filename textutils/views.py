# I crated this file - Radhen
from django.http import HttpResponse
from django.shortcuts import render
from .models import FeedBack


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


# def about(request):
#     return HttpResponse("About King Radhen</br><a href= '/'>Back</a>")


# def home(request):
#     file = open("textutils/a1.html", 'r+')
#     return HttpResponse(file.read())

def analyze(request):
    # Get the text
    djtaxt = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtaxt:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtaxt = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtaxt:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtaxt = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtaxt:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtaxt = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtaxt):
            if not (char == " " and djtaxt[index - 1] == " "):
                analyzed += char

        params = {'purpose': 'Removed Extera Space ', 'analyzed_text': analyzed}

    elif charactercounter == "on":
        analyzed = len(djtaxt)

        params = {'purpose': 'Character Counted ', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on":
        return HttpResponse("<h1>Please select operations among of them !!</h1>")

    return render(request, 'analyze.html', params)


def AboutUs(request):
    return render(request, 'AboutUs.html')


def Feedback(request):
    return render(request, 'Feedback.html')


def Submit(request):
    if request.method == "POST":
        usermail = request.POST['Uemail']
        feedback = request.POST['words']
        obj = FeedBack(email=usermail, feedback=feedback)
        obj.save()

    return render(request, 'Submit.html')
