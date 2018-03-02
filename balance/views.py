# import random
from decimal import Decimal
from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from balance.models import User
from balance.models import Activity


# Create your views here.


def home(request):
    return render(request, 'home.html')


def activity(request):
    _date = request.POST.get('date')
    _totalCost = float(request.POST.get('cost'))
    peoplelist = request.POST.getlist('people[]')
    numOfPeople = len(peoplelist)
    _individuelCost = float("%.2f" % (_totalCost / numOfPeople))
    _people = ', '.join(peoplelist)
    print _people
    _note = request.POST.get('note')
    for person in peoplelist:
        selectUsers = User.objects.filter(name=person)
        selectUser = selectUsers[0]
        selectUser.balance -= Decimal(_individuelCost)
        selectUser.save()
    newActivity = Activity(date=_date, totalCost=_totalCost, individuelCost=_individuelCost, people=_people, note=_note)
    newActivity.save()

    print newActivity
    return HttpResponseRedirect('/')


def charge(request):
    _name = request.POST.get('user')
    selectUsers = User.objects.filter(name=_name)
    if selectUsers.count > 0:
        _money = int(request.POST.get('money')) + selectUsers[0].balance
        selectUser = selectUsers[0]
        selectUser.balance = _money
        selectUser.save()
    return HttpResponseRedirect('/')


def addUser(request):
    _name = request.POST.get('name')
    _gender = request.POST.get('gender')
    _email = request.POST.get('email')
    selectUsers = User.objects.filter(name=_name)
    if not selectUsers.exists():
        newUser = User(joiningDate=timezone.now(), name=_name, gender=_gender, email=_email, balance=0)
        newUser.save()
    return HttpResponseRedirect('/')


def ajax_allObjects(request):
    allObjects = User.objects.all().order_by('name')
    # namelist = [o.name for o in allObjects]
    ret = []
    for o in allObjects:
        ret.append({"Name": o.name, "Balance": o.balance})

    return JsonResponse(ret, safe=False)
