from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newliner = request.POST.get('newliner', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    countalpha = request.POST.get('countalpha', 'off')

    if removepunc == "on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if( fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        param = {'purpose': 'Changed To UpperCase', 'analyzed_text': analyzed}
        djtext=analyzed

    if (newliner == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        param = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
        djtext=analyzed

    if (spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        param = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
        djtext=analyzed

    if (countalpha == "on"):
        analyzed=len(djtext)
        param = {'purpose': 'countalpha', 'analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc != "on" and fullcaps!="on" and newliner != "on" and spaceremover != "on" and countalpha!="on"):
        return HttpResponse("SELECT ANY BOX")

    return render(request, 'analyze.html', param)
