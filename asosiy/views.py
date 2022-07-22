from django.shortcuts import render, redirect
from django.views import View
from .models import *

class AsosiyView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,"page-index-2.html")
        return redirect("login")
class IchkiView(View):
    def get(self,request,pk):
        b=Bolim.objects.get(id=pk)
        i=Ichki.objects.filter(bolim=b)
        return render(request,"page-category.html",{"ichki":i})