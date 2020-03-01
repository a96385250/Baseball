from django.shortcuts import render
from django.http import HttpResponse
from member.models import member

# Create your views here.
def login(request):
    return render(request,'login.html')

def information(request):
    return render(request,'information.html',locals())

def register(request):
    return render(request,'register.html')

def create(request):
    name = request.POST['name']
    account = request.POST['account']
    password = request.POST['password']
    team_id = request.POST['team_id']

    member.objects.create(name=name,account=account,password=password,team_id=team_id)

    return render(request,'information.html',locals())




