#-*- coding : utf-8 -*-
from django.http import *

def hello_world(request):
        return HttpResponse('Hello World')
        
def merhaba(request, gelen):
        isimler={'ahmet':'Kurucu','mehmet':'Kurucu','veysel':'yonetici'}
        if not gelen in isimler:
            raise Http404("Bu isimde bir kullanici yok")
        else:
            icerik="%s isimli kullanici yetkisi : %s" % (gelen, isimler[gelen])
            return HttpResponse(icerik)