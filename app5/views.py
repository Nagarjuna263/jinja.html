from django.shortcuts import render

# Create your views here.
def jinja(request):
    d=context={'name':'Nag','age':3}
    
    return render(request,'jinja.html',d)