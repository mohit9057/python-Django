# I have created this file -Mohit Taneja
from django.shortcuts import render
global params
def index(request):
    return render(request,'index.html')
def analyze(request):
   # get the text
    input_text = request.POST.get('text', 'default')
   #get checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    case = request.POST.get('case', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numrem = request.POST.get('numrem', 'off')

    if(input_text != ""):
        if (
                removepunc != "on" or extraspaceremover != "on" or newlineremover != "on" or case != "on" or numrem != "on"):
            if (removepunc == "on"):
                punctuations = '''!()-{}[];:'"\,<>./?@#$%^&*_~+=|'''
                analyzed = ""
                for char in input_text:
                    if char not in punctuations:
                        analyzed += char
                params = {'purpose': 'Changed according as per selecteted', 'analyzed_text': analyzed}
                # analyze the text
                input_text = analyzed

            if (numrem == "on"):
                numbers = '''0123456789'''
                analyzed = ""
                for char in input_text:
                    if char not in numbers:
                        analyzed += char
                params = {'purpose': 'Changed according as per selecteted', 'analyzed_text': analyzed}
                # analyze the text
                input_text = analyzed

            if (case == "capitilized"):
                analyzed = ""
                for char in input_text:
                    analyzed += char.upper()
                params = {'purpose': 'Changed according as per selecteted', 'analyzed_text': analyzed}
                input_text = analyzed
            if (case == "lowercase"):
                analyzed = ""
                for char in input_text:
                    analyzed += char.lower()
                    params = {'purpose': 'Changed according as per selecteted', 'analyzed_text': analyzed}
                    input_text = analyzed

            if (extraspaceremover == "on"):
                analyzed = " "
                for index, char in enumerate(input_text):
                    if not (input_text[index] == " " and input_text[index + 1] == " "):
                        analyzed += char
                    #    analyzed = "".join([i.strip() for i in input_text.split()])
                params = {'purpose': 'Changed according as per selecteted', 'analyzed_text': analyzed}
                input_text = analyzed

            if (newlineremover == "on"):
                analyzed = " "
                for char in input_text:
                    if char != "\n" and char != "\r":
                        analyzed = analyzed + char

                params = {'purpose': 'Changed according as per selecteted', 'analyzed_text': analyzed}

        if (removepunc != "on"  and extraspaceremover != "on" and newlineremover != "on" and case != "on" and numrem != "on" ):
            params = {'purpose': 'Analyze Text', 'analyzed_text': input_text}
            return render(request, 'analyze.html', params)

        return render(request, 'analyze.html', params)
    else:
        params = {'purpose': 'Error !!!!', 'analyzed_text': 'please enter your text to se magic of Text Utils......'}
        return render(request, 'error.html', params)

def about(request):
    return  render(request, 'about.html')
def error(request):
    return  render(request, 'error.html')
def contact(request):
    return  render(request, 'contact.html')
