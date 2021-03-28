from django.urls import path,include
from webapp.views import *

urlpatterns = [

    path('',index.as_view()),
    path('output/<int:id>',output.as_view()),
    
    
]
