from django.shortcuts import render
from django.http import HttpResponse
from useradmin.models import User
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def getUserAdmin (request):
    if request.method == 'GET':
        userList = User.objects.all()
        return HttpResponse(userList)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        active = request.POST.get('active', '')
        type = request.POST.get('active', '')
        user = User(name= name, password = password, active = active)
        user.save()
        return HttpResponse('保存成功')
