from django.shortcuts import render, redirect,HttpResponse
from .models import Students
from django.contrib import messages


def home(request):
    data = Students.objects.all()
    context = {'data': data}
    return render(request, 'home.html', context)


def AddStudent(request):
    if request.method == 'POST':
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        roll1 = request.POST.get('roll')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        address1 = request.POST.get('address')

        data = Students(
            fname=fname1,
            lname=lname1,
            roll=roll1,
            email=email1,
            phone=phone1,
            address=address1

        )

        data.save()
        return redirect('/')

    else:
        return render(request, 'addstudent.html')


def update_form(request, pk):
    student = Students.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'update_student.html', context)


def saveUpdate(request,pk):
    student = Students.objects.get(id=pk)
    student.fname = request.POST.get('fname')
    student.lname = request.POST.get('lname')
    student.email = request.POST.get('email')
    student.roll = request.POST.get('roll')
    student.phone = request.POST.get('phone')
    student.address = request.POST.get('address')

    student.save()
    return redirect('/')

def deleteStudent(request,pk):
    student = Students.objects.get(id=pk)
    student.delete()
    return redirect('/')    
        
def loginPage(request):
    return render(request,'login.html')

def loginStudent(request):
    if request.method=='POST':
        fname1=request.POST.get('fname')
        email1=request.POST.get('email')

        student=Students.objects.filter(
            fname=fname1,
            email=email1
        ) 

        if student:
            messages.warning(request,"LogIn Successfully")
          
        if not student:
            messages.warning(request,"Incorrect Details")  
    return render(request, 'login.html')

            