from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

def index(request,num1,num2):
    sum=str(num1+num2)
    sum1=int(sum)

    list1=[i for i in range(sum1)]
    context={"sum":sum,"list":list1}
    return render(request,'index1.html',context)

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')



