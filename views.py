from django.shortcuts import render
from .models import Student
from django.contrib import messages

# Create your views here.
def data(request):
    if request.method == "POST":
        if request.POST['sName'] and request.POST['sPhno'] and request.POST['sRollno']:
            datatosave = Student()
            datatosave.sName = request.POST['sName']
            datatosave.sPhno = request.POST['sPhno']
            datatosave.sRollno = request.POST['sRollno']
            datatosave.save()
            messages.success(request,"your data is saved Successfully")
            return render(request,'student.html') 
        else:
            messages.error(request,'Check the given data onceagain')
            return redirect("/")

    else:
        return render (request,"student.html")