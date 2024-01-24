from django.urls import path
from . import views

urlpatterns = [
    # path("january",views.january),
    # path("february",views.february),
    # path("march",views.march)
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.montly_challenge,name="month-challenge"),
    path("",views.index) # /calender
    
]