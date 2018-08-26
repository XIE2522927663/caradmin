from django.shortcuts import render
from django.http import HttpResponse
from useradmin.models import User
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def userAdmin (request):
    if request.method == 'GET':
        userList = User.objects.all()
        return HttpResponse(userList)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        active = request.POST.get('active', '')

        user = User(name= name, password = password, active = active)
        user.save()
        return HttpResponse('success')


def putUserAdmin (request, id):
    if request.method == 'PUT':
        print(id)
        print(request)
        # name = request.PUT.get('name', '')
        # password = request.POST.get('password', '')
        # active = request.POST.get('active', '')
        # bb = User.objects.filter(id=id)
        # print(name)
        # User.objects.filter(id=id).update(name=name)
        # user = User(name=name, password=password, active=active)
        # user.save()
        return HttpResponse('success')