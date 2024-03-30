from django.urls import path
from .views import index,home,about

urlpatterns =[ path('/index/<int:num1>/<int:num2>',index),
                 path('/home/',home),
                    path('/about/',about),
               ]