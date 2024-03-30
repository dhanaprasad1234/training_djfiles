from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    list1=range(10)
    # list2=int(list2)
    return render(request,'index1.html',{"list":list1})

