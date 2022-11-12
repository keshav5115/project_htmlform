from django.shortcuts import render
from django.http import HttpResponse
from form.models import usermodel

# Create your views here.

def registerview(request):
    print(request.method)
    if request.method =='POST':
        name=request.POST['user']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        loc=request.POST['location']
        usermodel.objects.create(name=name,email=email,phone=phone,age=age,location=loc)
        return HttpResponse('data has been stored in the database')

    return render(request,'register.html')

def readview(request):
    details=usermodel.objects.all()
    return render(request,'data.html',{'details':details})

def getrecord(request,pk):
    data=usermodel.objects.get(id=pk)
    return render(request,'record.html',{'data':data})

def updateview(request,pk):
    if request.method=='POST':
        name=request.POST['user']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        loc=request.POST['location']
        usermodel.objects.filter(id=pk).update(name=name,email=email,phone=phone,age=age,location=loc)
        return HttpResponse('data has been updated')
    data=usermodel.objects.get(id=pk)
    return render(request,'update.html',{'data':data})

def updaterecord(request):
    if request.method == 'POST':
        record=request.POST['record']
        data=usermodel.objects.get(name=record)
        return render(request,'update.html',{'data':data})
    data=usermodel.objects.all()
    return render(request,'uprecord.html',{'data':data})


def deleterecord(request):
    if request.method == 'POST':
        record=request.POST['record']
        data=usermodel.objects.filter(name=record).delete()
        return HttpResponse(f'{record} data has been deleted')
    data=usermodel.objects.all()
    return render(request,'uprecord.html',{'data':data})
