from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
# Create your views here.

def home(request):
    return render(request,'home.html')



def saveform(request):
    if request.method == "POST":
        student = Student(
            student_id=request.POST.get('student_id'),
            student_name=request.POST.get('student_name'),
            student_attendence=request.POST.get('student_attendence'),
            student_Email=request.POST.get('student_Email'),
            student_contactNo=request.POST.get('student_contactNo'),
            Student_gender=request.POST.get('Student_gender'),
            student_Course = request.POST.get('student_Course')

        )

        student.student_photo = request.FILES.get('student_photo')
        student.student_assignment = request.FILES.get('student_assignment')
        print("upload image",request.FILES.get('student_photo'))
        student.save()
        return redirect('show')
        # Handle file upload
        # student_photo = request.FILES.get('student_photo')
        # print("upload images ",  student_photo)
        # if student_photo:
            # student.student_photo = student_photo
            # print("upload photo")
        # else:
            # Handle case where no file is uploaded
            # You might want to provide a default photo or handle the error differently
            # pass

        '''try:
            student.save()
            return redirect('show')
        except Exception as e:
            # Handle any exceptions that occur during saving
            # You might want to log the error or provide a meaningful mestsage to the user
            print(e)
            return render(request, "error.html", {'error_message': 'An error occurred while saving the student information.'})'''

    return render(request, "home.html")

'''
# without upload images and videos  for code
def saveform(request):
    if request.method == "POST":
        student=Student()
        student.student_id=request.POST.get('student_id')
        student.student_name = request.POST.get('student_name')
        student.student_attendence = request.POST.get('student_attendence')
        student.student_Email = request.POST.get('student_Email')
        student.student_contactNo = request.POST.get('student_contactNo')
        student.student_photo = request.FILES.get('student_photo')
        # student.student_assignment = request.FILES.get('student_assignment')
        student.save()
        return redirect('show')
    return render(request,"home.html")'''


def show(request):
    student=Student.objects.all()
    return render(request,'index.html',{'student':student})

def update(request,student_id):
    student = Student.objects.get(student_id=student_id)
    print("update")
    if request.method == "POST":
        print("post in update")
        student.student_name = request.POST.get('student_name')
        student.student_attendence=request.POST.get('student_attendence')
        student.Student_gender = request.POST.get('Student_gender')
        student.student_Course = request.POST.get('student_Course')
        student.student_Email = request.POST.get('student_Email')
        student.student_contactNo = request.POST.get('student_contactNo')
        student.student_gender = request.POST.get('student_gender')
        student.student_photo = request.FILES.get('student_photo')
        student.save()
        # print(request.POST.get('student_name'),request.POST.get('student_attendence'),request.POST.get('student_contactNo'),request.POST.get('student_Email'))
        return redirect('show')
    return render(request,'edit.html',{'student':student})


def edit(request,student_id):
    student= Student.objects.get(student_id=student_id)

    return render(request,'edit.html',{'student':student})

def delete(request,student_id):
    student=Student.objects.get(student_id=student_id)
    student.delete()
    return redirect('show')




