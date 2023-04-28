from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from student.models import Student, City, Course


# Create your views here.
@login_required
def home(request):
    return redirect('displaystudent')

@login_required
def displaystudent(request):
    return render(request,'displaystudent.html',{'students':Student.objects.all()})
def addstudent(request):
    cities=City.objects.all()
    courses=Course.objects.all()
    return render(request,'addstudent.html',{'cities':cities,'courses':courses})
def readstudentdata(request):
    s=Student()
    s.fname=request.POST['tbfname']
    s.lname=request.POST['tblname']
    s.mobile=request.POST['tbmobile']
    s.email=request.POST['tbemail']
    s.cityname=City.objects.get(cityname=request.POST['ddlcity'])
    s.coursename=Course.objects.get(coursename=request.POST['ddlcourse'])
    s.save()
    return redirect('displaystudent')




def updatedata(request,id):
    cities = City.objects.all()
    courses = Course.objects.all()
    s = Student.objects.get(id=id)
    if request.method == 'POST':
        s.fname = request.POST['tbfname']
        s.lname = request.POST['tblname']
        s.mobile = int(request.POST['tbmobile'])
        s.email = request.POST['tbemail']
        s.cityname = City.objects.get(cityname=request.POST['ddlcity'])
        s.coursename = Course.objects.get(coursename=request.POST['ddlcourse'])
        s.save()
        return redirect('displaystudent')
    return render(request, 'updatestudent.html', {'data': s, 'cities': cities, 'courses': courses})


def deletedata(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect('displaystudent')


def logoutfun(request):
    logout(request)
    return redirect('login')