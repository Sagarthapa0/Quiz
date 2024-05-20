from django.urls import path
from .views import *


urlpatterns=[
    path("",home),
    path("api/get-quiz/",get_quiz,name="get_quiz"),
    path("quiz/",quiz),
    
]