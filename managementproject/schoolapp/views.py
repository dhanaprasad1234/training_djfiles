from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
# Create your views here.
def show(request):
    student=Student.objects.all()
    return render(request,'index.html',{'student':student})

def update(request,student_id):
    student = Student.objects.get(student_id=student_id)
    if request.method == "POST":
        student.student_name=request.POST.get('student_name')
        student.student_attendence=request.POST.get('student_attendence')
        student.student_Email = request.POST.get('student_Email')
        student.student_contactNo = request.POST.get('student_contactNo')
        student.save()
        return redirect('show')
    return render(request,'edit.html',{'student':student})

def edit(request,student_id):
    student= Student.objects.get(student_id=student_id)
    return render(request,'edit.html',{'student':student})
# def home(request):
#     if request.method=="POST":
#         student.student_name=request.POST.get('name')
#         student.student_attendence=request.POST.get('attendence')
#         student.student_Email = request.POST.get('email')
#         student.student_contactNo = request.POST.get('contact')
#         student.save()
#         return redirect('show/')
#     return




