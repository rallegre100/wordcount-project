# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

#def eggs(request):
#    return HttpResponse('<h1>Eggs are Great</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split() 
    worddic = {}
    for word in wordlist:
        if word in worddic:
            #Increase
            worddic[word] +=  1
        else:
            #add to the dictionary
            worddic[word] =   1
             
    return render(request, 'count.html', {'fulltext':fulltext,'count': len(wordlist), 'worddic': worddic})

def about(request):
    return render(request, 'about.html')
