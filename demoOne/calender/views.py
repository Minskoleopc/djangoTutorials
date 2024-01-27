from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

# def january(request):
#     return HttpResponse("I will start going to yoga classes")

# def february(request):
#     return HttpResponse("I will start going to dance classes")

# def march(request):
#     return HttpResponse("I will start going to coding classes")

# def april(request):
#     return HttpResponse("I will start going to django classes")

# def may(request):
#     return HttpResponse("I will start going to react classes classes")

# def june(request):
#     return HttpResponse("I will start going to cypress classes")

# def july(request):
#     return HttpResponse("I will start going to playwright classes")

# def august(request):
#     return HttpResponse("I will start going to sql classes")

# def september(request):
#     return HttpResponse("I will start going to c classes")

# def octomber(request):
#     return HttpResponse("I will start going to Cpp classes")

# def novemeber(request):
#     return HttpResponse("I will start going to Ajax classes")

# def decemeber(request):
#     return HttpResponse("I will start going to Python classes")

challenge = {
    "january":"Learning code 1",
    "february":"Learning code 2",
    "march":"Learning code 3",
    "april":"Learning code 4",
    "may":"Learning code 5",
    "june":"Learning code 6",
    "july":"Learning code 7",
    "august":"Learning code 8",
    "september":"Learning code 9",
    "octomber":"Learning code 10",
    "november":"Learning code 11",
    "december":"Learning code 12",
} 

# def montly_challenge(request,month):
#     reponseText = None
#     if month == "january":
#         reponseText = "I will start going to yoga classes"
#     elif month == "february":
#         reponseText = "I will start going to dance classes" 
#     elif month == "march":
#         reponseText = "I will start going to coding classes"
#     return HttpResponse(reponseText)

def index(request):
    list_items = ""
    months =  list(challenge.keys())
    for month in months:
          c_month = month.capitalize()
          p_month = reverse('month-challenge',args=[month])
          list_items  = list_items+f"<li><a href=\"{p_month}\">{c_month}</a></li>"
    reponse_data =f"<ul>{list_items}<ul>"
    return HttpResponse(reponse_data)

          
def montly_challenge(request,month):# may
    try:
        reponseText = challenge[month]
        #return HttpResponse(f"<h1>{reponseText}</h1>")
        #reponseText = render_to_string('calender/calender.html')
        #return HttpResponse(reponseText)
        return render(request,'calender/calender.html',{"text":reponseText})

    except:
        return HttpResponse(f"<h1>This kind of month is not supported</h1>")

def monthly_challenge_by_number(request,month): # 2
      months =  list(challenge.keys())
     #["jan","Feb","Mar",'Apr',"May","june","july","Aug","Sept","Oct","Nov","Dec"]
      if month >len(months):
           return HttpResponse("Invalid month")
      
      redirect_month = months[month-1]  # 
      redirect_path = reverse('month-challenge',args=[redirect_month])
      return HttpResponseRedirect(redirect_path)

            
    