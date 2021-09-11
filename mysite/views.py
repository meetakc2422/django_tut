# I have created this file - Akash Chauhan
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Akash','post':'python dev'}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse("about this app")

def back(request):
    return HttpResponse('you can go to index page from <a href="/">"here"<a>')

def analyze(request):
    djtext = request.POST.get('text','default')
    remove_punc = request.POST.get('removepunc','off')
    char_counter = request.POST.get('charactercounter','off')
    caps_it = request.POST.get('fullcaps','off')
    new_line = request.POST.get('newline','off')

    if remove_punc == 'on':
        djtext1 = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                djtext1 = djtext1 + char
        params = {'purpose': 'Remove-punctuation', 'analyzed_text': djtext1}
        djtext = djtext1
        # return render(request, 'analyze.html', params)
    if char_counter == 'on':
        djtext1 = 0
        for i in djtext:
            if i == ' ':
                pass
            else:
                djtext1 += 1
        params = {'purpose':'counting characters','analyzed_text':djtext1}
        djtext = djtext1

    if caps_it == 'on':
        dt = ''
        for i in djtext:
            dt += i.upper()
        params = {'purpose': 'All Caps', 'analyzed_text': dt}
        djtext = dt

    if new_line == "on":
        dr = ""
        for i in djtext:
            if i !='\n' and i !='\r':
                dr = dr + i

        params = {'purpose':'newline removal','analyzed_text':dr}
        djtext = dr

    if (remove_punc!="on" and char_counter!="on" and caps_it!="on" and new_line!="on"):
        return HttpResponse('Error! you have to choose atleast one option.')

    return render(request, 'analyze.html', params)




def capitalize(request):
    return HttpResponse('This function capitalize the text')