from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    param = {'name': 'Sid', 'work': 'Developer'}
    return render(request, 'index.html', param)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcounter == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Count', 'analyzed_text': int(analyzed)}
        djtext = analyzed
    return render(request, 'analyze.html', params)

