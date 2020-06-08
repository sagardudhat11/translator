from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from googletrans import Translator,LANGUAGES

def index(request):
    text1 = request.POST.get('text')
    lan= LANGUAGES
    lan_list = list(lan.values())
    choosen_lan = request.POST.get('numbers')
    if(choosen_lan == None and text1 == None):
        text1 = ""
        choosen_lan = "afrikaans"
    result = Translator().translate(text1,dest = choosen_lan)
    trans = result.text
   
    return render(request,'index.html',{'lan_list': lan_list,'trans':trans,'choosen_lan':choosen_lan,'text1':text1})

def my_func1(request):
    
    text1 = request.POST.get('text')
    lan= LANGUAGES
    lan_list = list(lan.values())
    choosen_lan = request.POST.get('numbers')
    if(choosen_lan == None and text1 == None):
        text1 = " "
        choosen_lan = "hindi"
    result = Translator().translate(text1,dest = choosen_lan)
    trans = result.text
    ico = '&#xf240;'  
    return render(request,'main1.html',{'lan_list': lan_list,'trans':trans,'choosen_lan':choosen_lan,'ico':ico,'text1':text1})  
 

def my_func2(request):
    return render(request,'main2.html')        