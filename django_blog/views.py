#-*- coding : utf-8 -*-
from django.http import *
 
def hello_world(request):
        return HttpResponse('Hello World')